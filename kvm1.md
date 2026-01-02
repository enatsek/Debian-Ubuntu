---
title: "KVM Virtualization (Beginner)"
description: "Introduction to KVM virtualization"
next: false
prev: false
sidebar: 
   label: KVM Virtualization (Beginner)
---

##### Introduction to KVM virtualization 

## 0. Specs

---
### 0.0. The What
KVM Virtualization Tutorial 1 for Debian and Ubuntu Server.

Our objective is to install and configure a host system for virtual machines.

This tutorial aims to bring you (and me) to a moderate level of virtualization administration proficiency.

### 0.1. How It Works
**KVM** (Kernel-based Virtual Machine) is a loadable kernel module that provides virtualization capabilities via APIs.

**QEMU** (Quick EMUlator) is a virtualizer that uses the KVM API. QEMU also supports other virtualization solutions.

**Libvirt** is a library for managing virtualization hosts. The `virsh` command originates from Libvirt.

**Libguestfs** is a collection of tools for accessing and managing virtual machine images.

**virt-manager** is a GUI for managing virtual machines. I use it on my workstation for simple tasks.

### 0.2. Infrastructure
- **Server (Host)**: Debian (12/13) or Ubuntu (24.04/22.04) Server
    - IP: 192.168.1.121
    - Name: elma
    - NIC: enp3s0f0
- **Workstation**: Debian 13 or Ubuntu 24.04 LTS Desktop
- **Network**: 192.168.1.0/24 supplied by my internet modem/router

### 0.3. (Very) Basic Terminology
- **Domain**: Virtual Machine (VM)
- **Image**: A file containing a virtual machine or its disk
- **Host**: A server running virtualization software
- **Guest**: A virtual machine running on a host
- **Snapshot**: A saved state of an image that can be restored later

### 0.4. Resources
- [ostechnix.com](https://ostechnix.com/install-and-configure-kvm-in-ubuntu-20-04-headless-server/)
- [www.qemu.org](https://www.qemu.org/docs/master/tools/qemu-img.html)
- [www.libvirt.org](https://www.libvirt.org/manpages/virsh.html)
- https://docs.fedoraproject.org/en-US/Fedora/18/html/Virtualization_Administration_Guide/index.html (not working now
- [libguestfs.org](https://libguestfs.org/)
- [fabianlee.org](https://fabianlee.org/2020/02/23/kvm-testing-cloud-init-locally-using-kvm-for-an-ubuntu-cloud-image/)
- [cloudinit.readthedocs.io](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)
- ISBN: 979-10-91414-20-3 **The Debian Administrator's Handbook** by Raphaël Hertzog and Roland Mas
- ISBN: 978-1-78829-467-6 **KVM Virtualization Cookbook** by Konstantin Ivanov

<br>

## 1. Installation and Configuration

---
### 1.1. Installation
Install necessary packages:

```
sudo apt update
sudo apt install libvirt-clients libvirt-daemon-system qemu-kvm \
     virtinst virt-manager virt-viewer bridge-utils --yes
```

Add your user to the libvirt group (replace `exforge` with your username):

```
sudo usermod -aG libvirt exforge
```

### 1.2. Bridge Configuration
For guest computers to access the network, a bridge configuration on the host is required.

Bridge configuration differs slightly between Debian and Ubuntu, so we'll handle them separately.

#### 1.2.1. Ubuntu Bridge Configuration
By default, KVM creates a virtual bridge named `virbr0`. This bridge allows VMs to communicate with each other and the host. However, we want VMs to join our network by obtaining IP addresses from it.

First, disable netfilter (enabled on bridges by default):

```
sudo nano /etc/sysctl.d/bridge.conf
```

Add the following lines (file is initially empty):

```
net.bridge.bridge-nf-call-ip6tables=0
net.bridge.bridge-nf-call-iptables=0
net.bridge.bridge-nf-call-arptables=0
```

Create a udev rule to apply these settings:
 
```
sudo nano /etc/udev/rules.d/99-bridge.rules
```

Add this line (file is initially empty):

```
ACTION=="add", SUBSYSTEM=="module", KERNEL=="br_netfilter", RUN+="/sbin/sysctl -p /etc/sysctl.d/bridge.conf"
```

Reboot to apply changes:

```
sudo reboot
```

Remove the default KVM bridge. List networks with `ip link` to see `virbr0`.

Delete and undefine KVM networks:

```
virsh net-destroy default
virsh net-undefine default
```

If errors occur, force removal:

```
sudo ip link delete virbr0 type bridge
```

Run `ip link` again to confirm `virbr0` is removed. Note your physical interface name(s) (e.g., `enp0s0`).

Back up your network configuration file (if `50-cloud-init.yaml` doesn't exist, look for another `.yaml` file):

```
sudo cp /etc/netplan/50-cloud-init.yaml{,.backup}
```

Edit your network configuration:

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Replace the content with the following (adjust `enp3s0f0` to your interface name, and use your local network IP and gateway):

```
network:
  ethernets:
    enp3s0f0:
      dhcp4: false
      dhcp6: false
  bridges:
    br0:
      interfaces: [enp3s0f0]
      addresses:
      - 192.168.1.121/24
      routes:
      - to: default
        via: 192.168.1.1
      mtu: 1500
      nameservers:
        addresses:
        - 8.8.8.8
        - 8.8.4.4
      parameters:
        stp: true
        forward-delay: 4
      dhcp4: false
      dhcp6: false
  version: 2
```

Apply changes (SSH connection may drop; reconnect if needed):

```
sudo netplan apply
```

Verify the bridge with `ip link`; you should see `br0`.

#### 1.2.2. Debian Bridge Configuration
By default, KVM creates a virtual bridge named `virbr0`. This bridge allows VMs to communicate with each other and the host. However, we want VMs to join our network by obtaining IP addresses from it.

First, disable netfilter (enabled on bridges by default):

```
sudo nano /etc/sysctl.d/bridge.conf
```

Add the following lines (file is initially empty):

```
net.bridge.bridge-nf-call-ip6tables=0
net.bridge.bridge-nf-call-iptables=0
net.bridge.bridge-nf-call-arptables=0
```

Create a udev rule to apply these settings:

```
sudo nano /etc/udev/rules.d/99-bridge.rules
```

Add this line (file is initially empty):

```
ACTION=="add", SUBSYSTEM=="module", KERNEL=="br_netfilter", RUN+="/sbin/sysctl -p /etc/sysctl.d/bridge.conf"
```

Reboot to apply changes:

```
sudo reboot
```

Back up your network configuration file:

```
sudo cp /etc/network/interfaces{,.backup}
```

Edit your network configuration:

```
sudo nano /etc/network/interfaces
```

Replace the content with the following (adjust `enp3s0f0` to your interface name, and use your local network IP and gateway):

```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug enp3s0f0
#make sure we don't get addresses on our raw device
iface enp3s0f0 inet manual
#set up bridge and give it a static ip
auto br0
iface br0 inet static
        address 192.168.1.121
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.1.255
        gateway 192.168.1.1
        bridge_ports enp3s0f0
        bridge_stp off
        bridge_fd 0
        bridge_maxwait 0
        dns-nameservers 8.8.8.8
```

Apply changes (SSH connection may drop; reconnect if needed):

```
sudo systemctl restart networking.service
```

### 1.3. Add Our Bridge to KVM
Create an XML file for the bridge definition:

```
nano host-bridge.xml
```

```
<network>
  <name>host-bridge</name>
  <forward mode="bridge"/>
  <bridge name="br0"/>
</network>
```

Define, start, and enable autostart for the bridge:

```
virsh net-define host-bridge.xml
virsh net-start host-bridge
virsh net-autostart host-bridge
```

### 1.4. Configure Directories
Set up directories for disk images and installation ISOs:

- `/srv/kvm` for VM disk images
- `/srv/isos` for installation ISO images

```
sudo mkdir /srv/kvm /srv/isos
sudo virsh pool-create-as srv-kvm dir --target /srv/kvm
```

At this point, you may want to copy some installation ISOs to the server's `/srv/isos` directory.

<br>




## 2. VM Creation

---
### 2.1. Create the First VM
Now it's time to create our first virtual machine.

It will be Ubuntu Server 24.04 LTS with 1 GB RAM and 10 GB HDD.

I've already copied the Ubuntu Server ISO `ubuntu-24.04.2-live-server-amd64.iso` to `/srv/isos`.

Install a VM named `testkvm`:

```
sudo virt-install --name testkvm \
    --connect qemu:///system  --virt-type kvm \
    --memory 1024 --vcpus 1 \
    --disk /srv/kvm/testkvm.qcow2,format=qcow2,size=10 \
    --cdrom /srv/isos/ubuntu-24.04.2-live-server-amd64.iso  \
    --network bridge=br0 \
    --graphics vnc,port=5901,listen=0.0.0.0 \
    --os-variant ubuntu24.04 \
    --noautoconsole
```

Parameters explained:
- `--name`: VM name
- `--connect`: Connection URI (local system)
- `--virt-type`: Virtualization type (KVM)
- `--memory`: RAM in MB
- `--vcpus`: Virtual CPU count
- `--disk`: Storage location, format, and size (GB)
- `--cdrom`: Installation media
- `--network`: Network bridge for VM connectivity
- `--graphics`: VNC settings (listens on all interfaces)
- `--os-variant`: Guest OS optimization profile
- `--noautoconsole`: Don't automatically connect to console

**Note**: Ubuntu 22.04 may not recognize `ubuntu24.04` OS variant; use `ubuntu22.04` instead.


### 2.2. OS Variant List
Many OS variants are available. Find yours with:

```
sudo apt install libosinfo-bin --yes
osinfo-query os
```

This helps the hypervisor optimize for the guest OS. The parameter can be omitted if unsure.

### 2.3. Connecting to the VM
A graphical desktop is required to connect via VNC. Install `virt-viewer` on your workstation:

**Run on your workstation:** 

```
sudo apt update
sudo apt install virt-viewer --yes
virt-viewer --connect qemu+ssh://exforge@elma/system testkvm
```

Replace `exforge` with your username on the server and `elma` with your server's hostname.

<br>

## 3. Remote Graphical Management

---
Our server lacks a graphical interface (like most servers). For graphical management, install `virt-manager` on your workstation:

**Run on your workstation:**

```
sudo apt update
sudo apt install virt-manager --yes
virt-manager
```

The application appears in the Applications Menu as "Virtual Machine Manager."

<br>


## 4. Installing VMs from Pre-built Images

---
Installing an OS from scratch is time-consuming. An alternative is using pre-built cloud images with cloud-init configuration.

### 4.0. Installing cloud-image-utils
```
sudo apt update
sudo apt install cloud-image-utils --yes
```

### 4.1. Acquiring Cloud Images
Search for cloud images:

- **Ubuntu**: [cloud-images.ubuntu.com](https://cloud-images.ubuntu.com/)
- **Debian**: [cloud.debian.org](https://cloud.debian.org/images/cloud/)

Download the latest images (e.g., Ubuntu 24.04 Noble and Debian 13 Trixie) to `/srv/isos`.

```
cd /srv/isos
sudo wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img
sudo wget https://cloud.debian.org/images/cloud/trixie/latest/debian-13-generic-amd64.qcow2
```

### 4.2. Creating a New Image From the Original Image
Create new images with increased size (20 GB) and convert to qcow2 format.

**Ubuntu image:**

```
sudo qemu-img create -b /srv/isos/noble-server-cloudimg-amd64.img \
    -F qcow2 -f qcow2 /srv/kvm/ubuntusrv-cloudimg.qcow2 20G
```

**Debian image:**

```
sudo qemu-img create -b /srv/isos/debian-13-generic-amd64.qcow2 \
    -F qcow2 -f qcow2 /srv/kvm/debiansrv-cloudimg.qcow2 20G
```



### 4.3. Cloud-init Configuration
The next step is to crate a cloud-init config file. This file contains instructions for the cloud image. There is a wide range of instructions like; creating a user, creating and filling files, adding apt repositories, running initial commands, installing packages, reboot and poweroff after finishing, disk and configuration. See below url for details:

[cloudinit.readthedocs.io](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)

Our cloud-init file will configure the following:

- Set hostname and Fully Qualified Domain Name, 
- Create a user named exforge with sudo privileges, 
- assign its password, 
- add it to exforge group as primary, 
- also add it to users group, 
- create its home directory as /home/exforge, 
- and set its shell to bash.

First, generate a password hash:

```
sudo apt install whois --yes
mkpasswd --method=SHA-512 --rounds=4096
```

Enter the desired password and copy the hash output.


We will create configuration files in `/srv/init`. Create the folder:

```
sudo mkdir /srv/init
```

**Ubuntu cloud-init configuration:**

```
sudo nano /srv/init/ubuntu-cloud-init.cfg
```

Fill as below (Remember updating password with the hash you get):

```
#cloud-config
hostname: ubuntu24
fqdn: ubuntu24.x386.org
manage_etc_hosts: true
groups: exforge
users:
   - name: exforge
     sudo: ALL=(ALL) ALL
     primary_group: exforge
     groups: users
     home: /home/exforge
     shell: /bin/bash
     lock_passwd: false
     passwd: $6$rounds=4096$hVAmry7V/zE8KHCT$Ha.qFtVJLDxRhmKTFY3hFhQqXmWrbF3n39dlWMXnmIAmdm5hJriRWRHVlT7FtaVUHIPeSm5u966vOcXFfXCyI/
packages: qemu-guest-agent
```

**Debian cloud-init configuration:**


```
sudo nano /srv/init/debian-cloud-init.cfg
```

Fill as below (Again remember updating password with the hash you get):

```
#cloud-config
hostname: debian13
fqdn: debian13.x386.org
manage_etc_hosts: true
groups: exforge
users:
   - name: exforge
     sudo: ALL=(ALL) ALL
     primary_group: exforge
     groups: users
     home: /home/exforge
     shell: /bin/bash
     lock_passwd: false
     passwd: $6$rounds=4096$hVAmry7V/zE8KHCT$Ha.qFtVJLDxRhmKTFY3hFhQqXmWrbF3n39dlWMXnmIAmdm5hJriRWRHVlT7FtaVUHIPeSm5u966vOcXFfXCyI/
packages: qemu-guest-agent
```


### 4.4. Cloud-init Network Configuration
For static IP configuration, create network config files.

**Ubuntu network configuration:**

```
sudo nano /srv/init/ubuntu-network-init.cfg
```

```
#cloud-config
version: 2
ethernets:
  enp1s0:
     dhcp4: false
     addresses: [ 192.168.1.243/24 ]
     gateway4: 192.168.1.1
     nameservers:
       addresses: [ 192.168.1.1,8.8.8.8 ]
```

**Debian network configuration:**

```
sudo nano /srv/init/debian-network-init.cfg
```

Fill as below:

```
#cloud-config
version: 2
ethernets:
  enp1s0:
     dhcp4: false
     addresses: [ 192.168.1.244/24 ]
     gateway4: 192.168.1.1
     nameservers:
       addresses: [ 192.168.1.1,8.8.8.8 ]
```

Adjust IP addresses according to your network.

### 4.5. Creating Cloud-init Seed Images
Create seed images containing cloud-init and network configurations.

**Ubuntu seed image:**

```
sudo cloud-localds --network-config /srv/init/ubuntu-network-init.cfg \
   /srv/kvm/ubuntu24-seed.qcow2 \
   /srv/init/ubuntu-cloud-init.cfg
```

**Debian seed image:**

```
sudo cloud-localds --network-config /srv/init/debian-network-init.cfg \
   /srv/kvm/debian13-seed.qcow2 \
   /srv/init/debian-cloud-init.cfg
```

### 4.6. Start VMs from Cloud Images
**Ubuntu Server VM:**

```
virt-install --name ubuntu24 \
  --connect qemu:///system \
  --virt-type kvm --memory 2048 --vcpus 2 \
  --boot hd,menu=on \
  --disk path=/srv/kvm/ubuntu24-seed.qcow2,device=cdrom \
  --disk path=/srv/kvm/ubuntusrv-cloudimg.qcow2,device=disk \
  --graphics vnc,port=5902,listen=0.0.0.0 \
  --os-variant ubuntu24.04 \
  --network bridge=br0 \
  --noautoconsole \
  --install no_install=yes
```

**Debian Server VM:**

```
virt-install --name debian13 \
  --connect qemu:///system \
  --virt-type kvm --memory 2048 --vcpus 2 \
  --boot hd,menu=on \
  --disk path=/srv/kvm/debian13-seed.qcow2,device=cdrom \
  --disk path=/srv/kvm/debiansrv-cloudimg.qcow2,device=disk \
  --graphics vnc,port=5903,listen=0.0.0.0 \
  --os-variant debian13 \
  --network bridge=br0 \
  --noautoconsole \
  --install no_install=yes
```

**Note**: If `--os-variant debian13` fails on Ubuntu servers, try `--os-variant debian11`.

Cloud-init may take several minutes to complete. Connect via virt-viewer:

** Run on your workstation **

```
virt-viewer --connect qemu+ssh://exforge@elma/system ubuntu24
virt-viewer --connect qemu+ssh://exforge@elma/system debian13
```

### 4.7. Disable Cloud-init After Initial Configuration
On each VM, run:

```
sudo touch /etc/cloud/cloud-init.disabled
```

This prevents cloud-init from running on subsequent boots.

### 4.8. Automation with Python Script

The entire process (except step 4.7) can be automated with a Python script:

1. Download the latest cloud image (or use cached)
2. Create a new base image with `qemu-img create`
3. Generate password hash and create cloud-init files
4. Create seed image with `cloud-localds`
5. Launch VM with `virt-install`

Script parameters could include:
- Image name and size
- Username and password
- Network properties (IP, gateway, DNS)
- Memory size and vCPU count
- VNC port number

<br>


## 5. virsh: Shell Based VM Management

---
virt-manager handles basic management tasks, but advanced administration requires the command-line interface.

The `virsh` command offers extensive capabilities. I'll cover the most useful commands here (in my opinion).

For complete documentation, visit: [www.libvirt.org](https://www.libvirt.org/manpages/virsh.html)

In all examples, replace `NAME` with your VM's name.

### 5.0. Environment Variable Set
On Debian, to run `virsh` commands without `sudo`, set an environment variable:

```
export LIBVIRT_DEFAULT_URI='qemu:///system'
```

For permanent setup, add to your shell profile:

```
nano ~/.bashrc
```

Add this line:

```
export LIBVIRT_DEFAULT_URI='qemu:///system'
```

Then reload:

```
source ~/.bashrc
```

### 5.1. Host Information
Display host system details:

```
virsh nodeinfo
```

### 5.2. List VMs and Their States
List running VMs:

```
virsh list
```

List all VMs (running and stopped):

```
virsh list --all
```

### 5.3. VM Lifecycle Management
Start, stop, reboot, force stop, or remove a VM:

```
virsh start NAME                  # Start VM
virsh shutdown NAME               # Graceful shutdown
virsh reboot NAME                 # Reboot VM
virsh destroy NAME                # Force shutdown (power off)
virsh undefine NAME               # Remove VM definition
virsh undefine NAME --remove-all-storage  # Remove VM with all storage
```

### 5.4. Pause and Resume VM
Suspend and resume VM execution:

```
virsh suspend NAME                # Pause VM
virsh resume NAME                 # Resume VM
```

### 5.5. Autostart Configuration
Configure VM to start automatically with host boot:

```
virsh autostart NAME              # Enable autostart
virsh autostart --disable NAME    # Disable autostart
```

### 5.6. VM Information
Display various VM details:

```
virsh dominfo NAME                # General VM information
virsh domid NAME                  # VM ID
virsh domuuid NAME                # VM UUID
virsh domstate NAME               # Current state (running, shut off, etc.)
virsh domdisplay NAME             # VNC/display connection details
```


### 5.7. VM Memory Management
VMs have two memory parameters:
- **Current Memory**: Currently allocated RAM
- **Maximum Memory**: Maximum allocatable RAM

View current allocation:

```
virsh dominfo NAME
```

Change maximum memory (requires shutdown and start to activate):

```
virsh setmaxmem NAME 2G --config
```

**Note**: Size can be specified as `2G`, `1536M`, etc.

Change current memory allocation:

```
virsh setmem NAME 2G              # Current session only
virsh setmem NAME 2G --live       # Live change (immediate)
virsh setmem NAME 2G --config     # Persistent after shutdown/start
virsh setmem NAME 2G --live --config  # Immediate + persistent
```

**Warning**: Decreasing memory on a running VM is not recommended.

**Beware of Shutdown and Start. Reboots do not count.**
 
### 5.8. VM vCPU Management
VMs have two vCPU parameters:
- **Current**: Active vCPUs
- **Maximum**: Maximum allocatable vCPUs

Two states exist:
- **Config**: Persistent state (after shutdown and start)
- **Live**: Current running state

A cartesian product gives us 4 values:

- **maximum config**: Max number of vCPUs, valid after shutdown and start.
- **maximum live**: Max number of vCPUs, valid now (while running).
- **current config**: Active number of vCPUs, valid after shutdown and start.
- **current live**: Active number of vCPUs, valid now (while running).

View vCPU information:

```
virsh vcpucount NAME
```

I keep saying shutdown and start instead of restart or reboot, because kvm, qemu or whatever it is, acts differently when you reboot or shutdown  and then start the VM. 

So when I say shutdown and start, I mean shutdown first, wait a while (from 0.001 miliseconds to as long as you want) and then start the VM.

Change maximum vCPUs (config state only - requires shutdown and start to activate):

```
virsh setvcpus NAME NUMBER --maximum --config
virsh setvcpus ubuntu24 3 --maximum --config
```

Change current vCPU count:

```
virsh setvcpus NAME 3             # Current session
virsh setvcpus NAME 3 --live      # Live change
virsh setvcpus NAME 3 --config    # Persistent change
virsh setvcpus NAME 3 --live --config  # Both immediate and persistent
virsh setvcpus ubuntu24 3 
virsh setvcpus ubuntu24 3 --live
virsh setvcpus ubuntu24 3 --current
virsh setvcpus ubuntu24 3 --live --config
```

**Important**: After increasing vCPUs on a running VM, new vCPUs may be offline. Check online status on the VM:

```
lscpu | head
```

Activate offline vCPU (on the VM):

```
sudo sh -c 'echo 1 > /sys/devices/system/cpu/cpu2/online'
```

Replace `cpu2` with the appropriate vCPU number (starting from 0).

### 5.9. Snapshots
Create a live snapshot:

```
virsh snapshot-create-as VMNAME \
  --name SNAPSHOTNAME \
  --description "Description text"
```

Example:

```
virsh snapshot-create-as ubuntu24 \
  --name ss1-ubuntu24 \
  --description "First snapshot of Ubuntu24"
```

Manage snapshots:

```
virsh snapshot-revert VMNAME --current            # Revert to current snapshot
virsh snapshot-revert VMNAME --snapshotname SNAPSHOTNAME  # Revert to specific
virsh snapshot-current VMNAME --name              # Show current snapshot
virsh snapshot-delete VMNAME --current            # Delete current snapshot
virsh snapshot-delete VMNAME --snapshotname SNAPSHOTNAME  # Delete specific
virsh snapshot-list VMNAME                        # List all snapshots
```

### 5.10. Attach Another Disk to a VM
Add a secondary disk to a VM (e.g., 20GB for Ubuntu24).

Create a new disk image:

```
sudo qemu-img create -f qcow2 /srv/kvm/ubuntu24-disk2.qcow2 20G
```

Identify disk naming on VM (run on VM):

```
lsblk -o name -d | grep vd
```

Typical names: `vda` (primary), `vdb` (secondary), etc.

Attach disk to VM:

```
virsh attach-disk ubuntu24 \
  /srv/kvm/ubuntu24-disk2.qcow2 \
  vdb \
  --persistent
```

Options:
- `--persistent`: Survives shutdown/start
- `--live`: Current session only
- `--config`: Persistent but not immediate

Detach disk:

```
virsh detach-disk ubuntu24 vdb --persistent
```

As in virsh attach-disk, you can change --persistent option to --live or  --config.

### 5.11. Other virsh Commands
Get the list of all virsh subcommands:

```
virsh --help
```

<br>



## 6. qemu-img: Shell Based Image Management

---
`qemu-img` manipulates VM disk images. **Important**: Always stop the VM before using `qemu-img` on its images.

Complete documentation: [www.qemu.org](https://www.qemu.org/docs/master/tools/qemu-img.html)

### 6.1. Get Basic Image Information
```
qemu-img info FILENAME
```

Example for Ubuntu24 VM:

```
qemu-img info /srv/kvm/ubuntusrv-cloudimg.qcow2
```

### 6.2. Creating an Image
Create a new image:

```
qemu-img create -f FORMAT FILENAME SIZE
```

Example (from section 5.10):

```
sudo qemu-img create -f qcow2 /srv/kvm/ubuntu24-disk2.qcow2 20G
```

Create an image backed by another image (differencing image):

```
sudo qemu-img create \
  -b BACKINGFILENAME \
  -F BACKINGFILEFORMAT \
  -f OUTPUTFILEFORMAT \
  OUTPUTFILENAME \
  SIZE
```

Example (from section 4.2):

```
sudo qemu-img create \
  -b /srv/isos/noble-server-cloudimg-amd64.img \
  -F qcow2 \
  -f qcow2 \
  /srv/kvm/ubuntusrv2-cloudimg.qcow2 \
  20G
```
 
### 6.3. Converting Image Formats

Common formats:
- **raw**: Simple, unformatted binary
- **qcow2**: QEMU format with snapshots, compression, encryption
- **qcow**: Older QEMU format
- **vdi**: VirtualBox format
- **vmdk**: VMware format
- **vhdx**: Microsoft Hyper-V format
- **dmg**: Apple Disk Image


Convert between formats:

```
qemu-img convert \
  -f SOURCEFORMAT \
  -O DESTINATIONFORMAT \
  SOURCEFILE \
  DESTFILE
```


### 6.4. Resize a Disk Image.
Increase or decrease image size:

```
sudo qemu-img resize FILENAME [+|-]SIZE
```

Increase Ubuntu24 image by 5GB:

```
sudo qemu-img resize /srv/kvm/ubuntusrv-cloudimg.qcow2 +5G
```

**Warning**: To shrink an image:

1. Use `--shrink` flag: `qemu-img resize --shrink FILENAME -SIZE`
2. Shrink partitions/filesystem inside VM first
3. Verify disk usage before shrinking


### 6.5. Check an Image For Errors
```
qemu-img check FILENAME
```

Use if you suspect image corruption.

<br>


## 7. Export and Import of VMs

---
Migrate VMs between hosts or create backups.

### 7.1. Export
---
**Important**: Shut down the VM before export for data consistency.

Create backup directory:
```
mkdir /tmp/kvmbackup
```

Export VM definition (XML):

```
virsh dumpxml ubuntu24 > /tmp/kvmbackup/ubuntu24.xml
```

Identify disk images from XML:

```
grep "source file" /tmp/kvmbackup/ubuntu24.xml
```

Example output:

```
      <source file='/srv/kvm/ubuntu24-seed.qcow2'/>
      <source file='/srv/kvm/ubuntusrv-cloudimg.qcow2'/>
```

Copy disk images to backup location:

```
cp /srv/kvm/ubuntu24-seed.qcow2 /srv/kvm/ubuntusrv-cloudimg.qcow2 \
   /tmp/kvmbackup
```

Create archive:

```
tar -cf /tmp/ubuntu24.tar -C /tmp/kvmbackup .
```

You have to copy this file to another server, before importing there.

### 7.2. Import
**Important**: Remove or rename VM on source host to avoid IP conflicts.

Copy archive to new host, then:

Create import directory:

```
mkdir /tmp/import
```

Extract archive:

```
tar -xf /tmp/ubuntu24.tar -C /tmp/import
```

Copy disk images to storage location:

```
sudo cp \
  /tmp/import/ubuntu24-seed.qcow2 \
  /tmp/import/ubuntusrv-cloudimg.qcow2 \
  /srv/kvm/
```
 
Define VM from XML:

```
virsh define /tmp/import/ubuntu24.xml
```

Start VM:

```
virsh start ubuntu24
```

**Note**: If using different directory structure, edit XML file paths before defining.

<br>


## 8. libguestfs: VM Disk Management

---
Tools for accessing and modifying VM disk images without starting the VM.

Documentation: [libguestfs.org](https://libguestfs.org/)

### 8.1. Installation
```
sudo apt update
sudo apt-get --yes install libguestfs-tools
```

### 8.2. Mounting VM's Disks
Mount VM disk read-only (safer):

```
sudo guestmount -d ubuntu24 -i --ro /mnt
```

Mount with write access (use with caution -  VM must be shut down):

```
sudo guestmount -d ubuntu24 -i /mnt
```

Unmount:


```
sudo guestunmount /mnt
```


Details for guestmount and guestunmount commands:

```
guestmount --help
guestunmount --help
```

### 8.3. Common libguestfs Commands
- **guestfish**: Interactive shell for disk manipulation
- **guestmount**: Mount guest filesystem on host
- **guestunmount**: Unmount guest filesystem
- **virt-cat**: Display file from VM
- **virt-copy-in**: Copy files into VM
- **virt-copy-out**: Copy files from VM
- **virt-edit**: Edit file in VM
- **virt-ls**: List files in VM
- **virt-df**: Show disk usage
- **virt-filesystems**: List filesystems and partitions
- **virt-inspector**: Inspect VM image contents
- **virt-resize**: Resize disk partitions
- **virt-sparsify**: Make VM disks sparse (thin-provisioned)
- **virt-sysprep**: Prepare VM for cloning

**Example**: Copy file from VM:

```
sudo virt-copy-out -d ubuntu24 /etc/hostname /tmp/
```

**Example**: List files in VM:

```
sudo virt-ls -d ubuntu24 /etc/
```

**Security Note**: These tools allow host administrators to access VM data without VM knowledge—consider encryption for sensitive VMs.

<br>

