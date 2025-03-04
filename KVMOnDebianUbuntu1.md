##### KVMOnDebianUbuntu1: 
# KVM Tutorial On Debian and Ubuntu Server (Beginner)

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. Start
KVM Virtualization Tutorial 1 on Debian and Ubuntu Server. 

Our aim is to install and configure a host computer for virtual  machines. 

This tutorial aims to bring you (and me) to a moderate level of  Virtualization Administration.

### 0.1. How It Works
**KVM** (Kernel-based Virtual Machine) is a loadable kernel module which  supply virtualization with APIs.

**QEMU** (Quick EMUlator) is a virtualizer which uses KVM API. QEMU supports other  virtualization solutions too.

**Libvirt** is a library for managing virtualization hosts. virsh command  comes from Libvirt.

**Libguestfs** is a collection of tools for accessing and managing VM  images.

**virt-manager** is a GUI for managing VMs. I use it on my workstation for simple tasks.

### 0.2. Infrastructure
- Server (Host): Debian (12/11) or Ubuntu (24.04/22.04) Server
   - IP: 192.168.1.121 
   - Name: elma
   - NIC: enp3s0f0
- Workstation: Debian 12 or Ubuntu 24.04 LTS Desktop
- Network: 192.168.1.0/24 which is supplied by my internet modem

### 0.3. (Very) Basic Terminology
**Domain**: Virtual Machine (VM)  
**Image**: A file in which a VM (or a disk of VM) is stored.   
**Host**: A server which runs virtualization software  
**Guest**: A VM running on a host  
**Snapshot**: A saved state of an image. You can revert to that stage later.

### 0.4. Resources
[ostechnix.com](https://ostechnix.com/install-and-configure-kvm-in-ubuntu-20-04-headless-server/)  
[www.qemu.org](https://www.qemu.org/docs/master/tools/qemu-img.html)  
[www.libvirt.org](https://www.libvirt.org/manpages/virsh.html)  
https://docs.fedoraproject.org/en-US/Fedora/18/html/Virtualization_Administration_Guide/index.html (not working now)  
[libguestfs.org](https://libguestfs.org/)  
[fabianlee.org](https://fabianlee.org/2020/02/23/kvm-testing-cloud-init-locally-using-kvm-for-an-ubuntu-cloud-image/)  
[cloudinit.readthedocs.io](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)  
ISBN: 979-10-91414-20-3 **The Debian Administrator's Handbook** by Raphaël Hertzog and Roland Mas  
ISBN: 978-1-78829-467-6 **KVM Virtualization Cookbook** by Konstantin Ivanov

<br>
</details>

<details markdown='1'>
<summary>
1. Installation and Configuration
</summary>

---
### 1.1. Installation
Install necessary packages

```
sudo apt update
sudo apt install libvirt-clients libvirt-daemon-system qemu-kvm \
     virtinst virt-manager virt-viewer bridge-utils --yes
```

Add your user to libvirt group:
(Change exforge to your user name)

```
sudo usermod -aG libvirt exforge
```

### 1.2. Bridge Configuration
For the guest computers to reach a network, a bridge configuration on the host computer is needed.

Bridge Configuration differs slighty for Debian and Ubuntu. So it is  better to handle them in different sections.

#### 1.2.1. Ubuntu Bridge Configuration
By default KVM creates a virtual bridge named virbr0. This bridge allows  the VMs to communicate between each other and the host. But we prefer that the VMs join to our network by getting IP address from our network.

That is we will create a public filter.

First we need to disable netfilter, which is enabled on bridges by  default.

```
sudo nano /etc/sysctl.d/bridge.conf
```

File is empty, add the following lines

```
net.bridge.bridge-nf-call-ip6tables=0
net.bridge.bridge-nf-call-iptables=0
net.bridge.bridge-nf-call-arptables=0
```
 
```
sudo nano /etc/udev/rules.d/99-bridge.rules
```

File is empty, the add following line

```
ACTION=="add", SUBSYSTEM=="module", KERNEL=="br_netfilter", RUN+="/sbin/sysctl -p /etc/sysctl.d/bridge.conf"
```

A reboot is necessary

```
sudo reboot
```

Now we need to remove the bridge created by KVM

With "ip link" command we see all the networks. KVM network is named as  virbr0.

Delete and undefine KVM networks

```
virsh net-destroy default
virsh net-undefine default
```

If in any case an error occurs, you can try the following command:

```
sudo ip link delete virbr0 type bridge
```

Now if you run "ip link" again, you will see that virbr0 is removed.

When you run "ip link", take a note of your interface name(s), it must  be something like enp0s0. If you have more than 1 interface there will be  more than 1 name.

Backup your network configuration file  
If that file does not exist, there must be another file there with yaml  extension. Proceed with that file.

```
sudo cp /etc/netplan/50-cloud-init.yaml{,.backup}
```

Edit your network config file

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Remove its content , fill it as below, beware of changing enp3s0f0 to  your interface name. If you have more than 1 interfaces, add them too.
 
Also you should add an IP address and default gateway from your local  network. 

Mine are 192.168.1.121 and 192.168.1.1

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

Apply the changes. If you connect through ssh, you connection may break. In this case, close the terminal and reconnect.

```
sudo netplan apply
```

If you run "ip link" now, you can see our bridge br0

#### 1.2.2. Debian Bridge Configuration
By default KVM creates a virtual bridge named virbr0. This bridge allows  the VMs to communicate between each other and the host. But we want the  VMs join to our network by getting IP address from our network.

First we need to disable netfilter, which is enabled on bridges by  default.

```
sudo nano /etc/sysctl.d/bridge.conf
```

File is empty, add following lines

```
net.bridge.bridge-nf-call-ip6tables=0
net.bridge.bridge-nf-call-iptables=0
net.bridge.bridge-nf-call-arptables=0
```

```
sudo nano /etc/udev/rules.d/99-bridge.rules
```

File is empty, add following line

```
ACTION=="add", SUBSYSTEM=="module", KERNEL=="br_netfilter", RUN+="/sbin/sysctl -p /etc/sysctl.d/bridge.conf"
```

A reboot is necessary

```
sudo reboot
```

Now it is time to create a Bridge configuration for the KVM

Backup your network configuration file

```
sudo cp /etc/network/interfaces{,.backup}
```

Edit your network config file

```
sudo nano /etc/network/interfaces
```

Remove its content , fill it as below, beware of changing enp3s0f0 to  your interface name. If you have more than 1 interfaces, add them too. 

Also you should add an IP address and default gateway from your local  network. 

Mine are 192.168.1.121 and 192.168.1.1

```
auto lo
iface lo inet loopback
# The primary network interface
auto enp3s0f0
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

Apply the changes. If you connect through ssh, your connection may break. In this case, close the terminal and reconnect.


```
sudo systemctl restart networking.service
```

### 1.3. Add Our Bridge to KVM
Adding our Bridge to KVM. We have to create an XML file for the bridge  definition:

```
nano host-bridge.xml
```

Fill as below:

```
<network>
  <name>host-bridge</name>
  <forward mode="bridge"/>
  <bridge name="br0"/>
</network>
```

Define the bridge, start it and make it autostart.


```
virsh net-define host-bridge.xml
virsh net-start host-bridge
virsh net-autostart host-bridge
```

### 1.4. Configure Directories
Set places for disk images and installation isos

/srv/kvm for VM disk images  
/srv/isos for installation iso images  

```
sudo mkdir /srv/kvm /srv/isos
sudo virsh pool-create-as srv-kvm dir --target /srv/kvm
```

At this point, you may want to copy some installation isos to server's /srv/isos dir

<br>
</details>

<details markdown='1'>
<summary>
2. VM Creation
</summary>

---
### 2.1. Create the 1st VM
Now it is time to create our first vm

It will be Ubuntu Server 22.04 LTS with 1 GB RAM and 10 GB HDD

I already copied Ubuntu server iso ubuntu-22.04.2-live-server-amd64.iso  to /srv/isos

Install a VM named testkvm:

- through QEMU with KVM virtualization, 
- with 1024MiB memory and 1 vcpu, 
- prepare a qcow2 format disk of 10GiB, 
- connect a CDROM drive to it with the specified image, 
- use the server's network bridge br0, 
- allow VNC connections to the VM through the server, 
- optimize it as Ubuntu 22.04 server and 
- don't try to attach a console from server.

```
sudo virt-install --name testkvm \
    --connect qemu:///system  --virt-type kvm \
    --memory 1024 --vcpus 1 \
    --disk /srv/kvm/testkvm.qcow2,format=qcow2,size=10 \
    --cdrom /srv/isos/ubuntu-22.04.2-live-server-amd64.iso  \
    --network bridge=br0 \
    --graphics vnc,port=5901,listen=0.0.0.0 \
    --os-variant ubuntu22.04 \
    --noautoconsole
```


Debian 11 does not recognize ubuntu22.04 os variant, so you can change  it as --os-variant ubuntu20.04

### 2.2. os-variant List
There are lots of OS Variant selections. You can find yours with the  following command. It helps hypervisor to optimize the system for the  guest OS. It can be skipped.

```
sudo apt install libosinfo-bin --yes
osinfo-query os
```

### 2.3. Connecting to the VM
A graphical desktop is needed to connect to the VM. You can install  virt-viewer package on your Debian or Ubuntu workstation and connect to the VM.

**Run on your workstation:**

```
sudo apt update
sudo apt install virt-viewer --yes
virt-viewer --connect qemu+ssh://exforge@elma/system testkvm
```

Remember to replace exforge with your user name on the server and elma  with your server's hostname

<br>
</details>

<details markdown='1'>
<summary>
3. Remote Graphical Management
</summary>

---
Our server has no graphical interface (like the most servers). If you  really want a graphical management, you can install virt-manager on your  workstation and manage your VMs from there. 

**Run on your workstation:**

```
sudo apt update
sudo apt install virt-manager --yes
virt-manager
```
 
The application is added to Applications Menu with the name "Virtual Machine Manager"

<br>

</details>

<details markdown='1'>
<summary>
4. Installing VMs from Ready Images
</summary>

---
Starting a new VM and installing OS into it is a good but time consuming way. Another way would be preparing an installed image and start it as a  new VM. 

Most server distros supply cloud images. By adding them some necessary  configurations (user and network definitions), you can use them as ready  images.

### 4.0. Installing cloud-image-utils
```
sudo apt update
sudo apt install cloud-image-utils --yes
```

### 4.1. Acquiring Cloud Images
A search for "ubuntu cloud image" in duckduck2 gives the following  address:  
[cloud-images.ubuntu.com](https://cloud-images.ubuntu.com/)

Following noble and current, download kvm image noble-server-cloudimg-amd64.img, and put it in the server's /srv/isos folder.

Similarly a search for "debian cloud images" in duckduck2 gives the  following address:  
[cloud.debian.org](https://cloud.debian.org/images/cloud/)

Following bookworm and latest, download debian-12-generic-amd64.qcow2 and put it in the server's /srv/isos folder.

### 4.2. Creating a New Image From the Original Image
We will create new images from the images we downloaded. Image sizes will be increased to 20 GiB and the Ubuntu image will be converted to qcow2, the preferred format for KVM.

Ubuntu image:

```
sudo qemu-img create -b /srv/isos/noble-server-cloudimg-amd64.img \
    -F qcow2 -f qcow2 /srv/kvm/ubuntusrv-cloudimg.qcow2 20G
```

Debian image:

```
sudo qemu-img create -b /srv/isos/debian-12-generic-amd64.qcow2 \
    -F qcow2 -f qcow2 /srv/kvm/debiansrv-cloudimg.qcow2 20G
```

### 4.3. Cloud-init Configuration
The next step is to crate a cloud-init config file. This file contains  instructions for the cloud image. There is a wide range of instructions  like; creating a user, creating and filling files, adding apt  repositories, running initial commands, installing  packages, reboot and  poweroff after finishing, disk and configuration. See below url for  details:

[cloudinit.readthedocs.io](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)

Our cloud-init file will configure the following:

- Set hostname and Fully Qualified Domain Name, 
- Create a user named exforge with sudo privileges, 
- assign its password, 
- add it to exforge group as primary, 
- also add it to users group, 
- create its home directory as /home/exforge, 
- and set its shell to bash.

To add our user's password, we need to have the hash of it.

```
sudo apt install whois --yes
mkpasswd --method=SHA-512 --rounds=4096
```

Enter the user's assigned password here, it will display the hash, copy  the hash, we will use it later.

Create a place for our cloud-init files. /srv/init would be fine.

```
sudo mkdir /srv/init
```

Create our ubuntu server's cloud-init file

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
     passwd: $6$rounds=4096$u5D5VbBZD7NcG/8Y$sc8WH5R9YU/xx1QqjQnMzNbQJOptj33DQGJqyHHju5EzJkvGF913gPVhjw.CsL8QLX5G79C0312tAuGIhWEhf1
packages: qemu-guest-agent
```

Create our debian server's cloud-init file


```
sudo nano /srv/init/debian-cloud-init.cfg
```

Fill as below:

```
#cloud-config
hostname: debian12
fqdn: debian12.x386.org
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
     passwd: $6$rounds=4096$u5D5VbBZD7NcG/8Y$sc8WH5R9YU/xx1QqjQnMzNbQJOptj33DQGJqyHHju5EzJkvGF913gPVhjw.CsL8QLX5G79C0312tAuGIhWEhf1
packages: qemu-guest-agent
```

Do not forget to change passwd value with your copied hash.

### 4.4. Cloud-init Network Configuration
If a network configuration other than DHCP is needed, a network  configuration file is necessary.

Remember to change IP addresses as needed by your VM

```
sudo nano /srv/init/ubuntu-network-init.cfg
```

Fill as below:

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

### 4.5. Creating Cloud Seed Images
Now we will create image files cloud-init and network-init inside.

For Ubuntu server:

```
sudo cloud-localds --network-config /srv/init/ubuntu-network-init.cfg \
   /srv/kvm/ubuntu24-seed.qcow2 \
   /srv/init/ubuntu-cloud-init.cfg
```

For Debian server:

```
sudo cloud-localds --network-config /srv/init/debian-network-init.cfg \
   /srv/kvm/debian12-seed.qcow2 \
   /srv/init/debian-cloud-init.cfg
```

### 4.6. Start Our Images as a New VMs
Ubuntu Server:

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

Debian Server

```
virt-install --name debian12 \
  --connect qemu:///system \
  --virt-type kvm --memory 2048 --vcpus 2 \
  --boot hd,menu=on \
  --disk path=/srv/kvm/debian12-seed.qcow2,device=cdrom \
  --disk path=/srv/kvm/debiansrv-cloudimg.qcow2,device=disk \
  --graphics vnc,port=5903,listen=0.0.0.0 \
  --os-variant debian12 \
  --network bridge=br0 \
  --noautoconsole \
  --install no_install=yes
```

Ironically, on Debian 12, --os-variant debian12 gives an error. In that  case, try the following command:

```
virt-install --name debian12 \
  --connect qemu:///system \
  --virt-type kvm --memory 2048 --vcpus 2 \
  --boot hd,menu=on \
  --disk path=/srv/kvm/debian12-seed.qcow2,device=cdrom \
  --disk path=/srv/kvm/debiansrv-cloudimg.qcow2,device=disk \
  --graphics vnc,port=5903,listen=0.0.0.0 \
  --os-variant debian11 \
  --network bridge=br0 \
  --noautoconsole \
  --install no_install=yes
```

- It might take a few minutes for cloud-init to finish. You can connect to your VM from your workstation.

```
virt-viewer --connect qemu+ssh://exforge@elma/system ubuntu24
virt-viewer --connect qemu+ssh://exforge@elma/system debian12
```

### 4.7. Clean-up Tasks for Cloud-init
On your VMs run:

```
sudo touch /etc/cloud/cloud-init.disabled
```

If the file /etc/cloud/cloud-init.disabled exists, cloud-init does not run again.

### 4.8. The whole process except 4.7. can be automated by a python script. 

- Download latest focal current cloud image (or use an already downloaded  one) 4.1.
- A system call to run a command to create a new image 4.2.
   - Image size (and name) can be a parameter
- Create password hash and init files 4.3. and 4.4. 
   - User name can be a parameter
   - Password can be obtained at run time
   - Network properties (IP, GW etc) can be parameters
- A system call to run a command to create seed image 4.5.
- A system call to run a command to start the new image 4.6.
   - Memory size, vcpu count can be parameters.

<br>
</details>

<details markdown='1'>
<summary>
5. virsh: Shell Based VM Management
</summary>

---
virt-manager can only help with the basic management tasks. If you want  to dive deep, you need the old-style shell.

There are countless options to do with virsh command. I can only list a  handfull of most useful ones (IMHO) here.

For a complete list of virsh command usage, see the following web page:  
[www.libvirt.org](https://www.libvirt.org/manpages/virsh.html)

In all examples, NAME is the name of your VM.

### 5.0. Environment Variable Set
For Debian, in order to run virsh command without sudo, we need to set an environment variable.

```
export LIBVIRT_DEFAULT_URI='qemu:///system'
```

Instead of setting everytime, we can add it to the .bashrc file:

```
nano ~/.bashrc
```

```
export LIBVIRT_DEFAULT_URI='qemu:///system'
```

### 5.1. Info about host
```
virsh nodeinfo
```

### 5.2. List VMs and their states
Running VMs

```
virsh list
```

All VMs

```
virsh list --all
```

### 5.3. Start, shutdown, reboot, force shutdown, remove a VM
```
virsh start NAME
virsh shutdown NAME
virsh reboot NAME
virsh destroy NAME
virsh undefine NAME
virsh undefine NAME --remove-all-storage
virsh reboot ubuntu24
```

### 5.4. Pause and resume a VM
```
virsh suspend NAME
virsh resume NAME
```

### 5.5. Autostart a VM (starts when the host starts)
```
virsh autostart NAME
virsh autostart --disable NAME   # Disable autostart
```

### 5.6. Information about a VM
```
virsh dominfo NAME
virsh domid NAME
virsh domuuid NAME
virsh domstate NAME
```

Display VNC connection settings of VM
```
virsh domdisplay NAME
```

### 5.7. VM Memory Management
VMs have 2 memory parameters: Max Memory and Used Memory. 

Used memory is the amount of mem allocated to the VM.  
Max memory is the max amount of mem to be allocated to the VM.

See current memory allocation:

```
virsh dominfo NAME
```

Change Max memory (Activated after shutdown and start)

```
virsh setmaxmem NAME 2G --config
```

size could be something like 2G 1536M etc


Used memory can be changed when the VM is running (decreasing is not  advised).

Change memory for this session only (reverts after shutdown and start):

```
virsh setmem NAME 2536M
virsh setmem NAME 2536M --live
virsh setmem NAME 2536M --current
```

Change memory after the next shutdown and start

```
virsh setmem NAME 2536M --config
```

Activate immediately and keep the changes after the next shutdown and  start

```
virsh setmem NAME 1536M --live --config
virsh setmem ubuntu24 2536M --live --config
```

**Beware of Shutdown and Start. Reboots do not count.**
 
### 5.8. VM vCPU Management
Just like memory, VMs have 2 virtual CPU parameters. Maximum and Current.

**Current** is the number of vcpus that VM uses actively (on-line).  
**Maximum** is the max number of vcpus can be allocated to the VM.  

Also, there are 2 states. Config and Live.

**Config** is the permanent state, it will be active after shutdown and start.  
**Live** is the running VM's state, it may not be active after shutdown and start.

A cartesian product gives us 4 values:

**maximum config**: Max number of vcpus, valid after shutdown and start.  
**maximum live**: Max number of vcpus, valid now (while running).  
**current config**: Active number of vcpus, valid after shutdown and start.  
**current live**: Active number of vcpus, valid now (while running).

To see these values for your VM:

```
virsh vcpucount NAME
```

I keep saying shutdown and start instead of restart or reboot, because kvm, qemu or whatever it is, acts differently when you reboot or shutdown  and then start the VM. 

So when I say shutdown and start, I mean shutdown first, wait a while (from 0.001 miliseconds to as long as you want) and then start the VM.

There is no way (AFAIK) to change maximum live value, you can change  maximum config as:

```
virsh setvcpus NAME NUMBER --maximum --config
virsh setvcpus ubuntu24 3 --maximum --config
```

To change current vcpu count for the current state (all options are valid)

```
virsh setvcpus NAME NUMBER
virsh setvcpus NAME NUMBER --current
virsh setvcpus NAME NUMBER --live
virsh setvcpus ubuntu24 3 
virsh setvcpus ubuntu24 3 --current
virsh setvcpus ubuntu24 3 --live
```

To change current vcpu count for the config state

```
virsh setvcpus NAME NUMBER --config
virsh setvcpus ubuntu24 3 --config
```

To do it both together

```
virsh setvcpus NAME NUMBER --config --live
virsh setvcpus ubuntu24 3 --config --live
```

You can both increase and decrease the vcpu count. But beware that  decreasing vcpu count of a running VM could be dangerous.

When you increase the current live vcpu count, the increased vcpus becomes offline. That means you cannot use them right away. At least that is what happened to me. You can see online and offline vcpu  information of your VM with the following command (**run it on your VM**):

```
lscpu | head
```

To activate an offline cpu, first you have to know its number. cpu  numbering starts from 0, so if you had 2 vcpus and increased them by 1, the number for the 3rd vcpu will be 2. You need to edit the following file and change the 0 inside to 1:

```
sudo nano /sys/devices/system/cpu/cpu2/online
```

The number 2 after cpu means the cpu with number 2 i.e. 3rd cpu. When  you change the file, magically that vcpu will become online. For more vcpus, you have to change that file for each vcpu you added.

### 5.9. Snapshots
When you take a snapshot, current disk and memory state is saved.

Take a live snapshot

```
virsh snapshot-create-as VMNAME --name SNAPSHOTNAME --description DESCRIPTION
virsh snapshot-create-as ubuntu24 --name ss1-ubuntu24 --description "First Snapshot of Ubuntu24"
```

The snapshot becomes the current one and everything after is built onto  this snapshot. If you want to revert to that snapshot:

```
virsh snapshot-revert VMNAME --current
```

If you want to revert to a specific snapshot:

```
virsh snapshot-revert VMNAME --snapshotname SNAPSHOTNAME
```

To see which snapshot is current:

```
virsh snapshot-current VMNAME --name
```

To delete the current snapshot

```
virsh snapshot-delete VMNAME --current
```

To delete a specific snapshot

```
virsh snapshot-delete VMNAME --snapshotname SNAPSHOTNAME
```

To list all snapshots of a VM

```
virsh snapshot-list VMNAME
```

### 5.10. Attach Another Disk to a VM
Suppose that, for our ubuntu24 VM, we need another disk of 20GB size.  Because, we need to keep some data on another disk. 

We need to create a new image and attach it to the VM.

Create a 20GB image in qcow2 format:

```
sudo qemu-img create -f qcow2 /srv/kvm/ubuntu24-disk2.qcow2 20G
```

Now our image is ready to be attached to our VM. Before attaching it to  the VM, we have to decide its name on the VM.

VM disks are named as vda, vdb, vdc ... so on. We have to give it a name  that follows the last disk name. Because my ubuntu24 VM has only one  disk, name for the second one will be vdb. To see your disks on your VM, type the following command (On your VM):

```
lsblk -o name -d | grep vd
```

Most probably you will only have vda, in that case you can use the name  vdb. Otherwise use a name just after the last disk name.

Add the new image as a second disk to my ubuntu24 VM:

```
virsh attach-disk ubuntu24 /srv/kvm/ubuntu24-disk2.qcow2 vdb --persistent
```

The disk is added persistently, that is it is added alive and it will be there after shutdown and and start. If you want to add the disk for the session only, you can change --persistent to --live. Also, if you want to  add the disk after shutdown and start you can change --persistent to --config.

Needless to say that, you are going to have to mount the new disk before  using it.

In any case, if you want to detach the added disk, solution is easy:

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
</details>

<details markdown='1'>
<summary>
6. qemu-img: Shell Based Image Management
</summary>

---
qemu-img allows us to manipulate images. The command is expected to work  offline. That means, before you start using qemu-img, you have to shut  down the VM associated with it. 

**Do not use qemu-img with an image of running VM**

A full documentation can be found at the below site:
[www.qemu.org](https://www.qemu.org/docs/master/tools/qemu-img.html)

### 6.1. Get Basic Info About an Image
```
qemu-img info FILENAME
```

FILENAME is the name of the file which is the image for the VM.

For my ubuntu24 VM's image info:

```
qemu-img info /srv/kvm/ubuntusrv-cloudimg.qcow2
```

### 6.2. Creating an Image
```
qemu-img create -f FORMAT FILENAME SIZE
```

Remember, at 5.10. we created an empty disk image to add as another disk  to a VM:

```
sudo qemu-img create -f qcow2 /srv/kvm/ubuntu24-disk2.qcow2 20G
```

An image also can be created by backing from another image. In that way, we will have another image from an image, differentiating its format and size:

```
sudo qemu-img create -b BACKINGFILENAME -F BACKINGFILEFORMAT \
    -f OUTPUTFILEFORMAT OUTPUTFILENAME SIZE
```

Remember, at 4.2. we created a new cloud image from the cloud image we downloaded:

```
sudo qemu-img create -b /srv/isos/focal-server-cloudimg-amd64.img \
    -F qcow2 -f qcow2 /srv/kvm/ubuntusrv-cloudimg.qcow2 20G
```
 
### 6.3. Changing the Format of an Image
There are a lot of formats for images. For us, the 2 most important ones are raw and qcow2. 

- raw   : As the name implies. 
- qcow2 : Feature rich, allows snapshots, compression and encrytion.
- qcow  : Older version of qcow2.
- dmg   : Mac format.
- nbd   : Network block device, used to access remote storages
- vdi   : Virtualbox format
- vmdk  : VMW*re format
- vhdx  : Micros*ft HyperV format

```
qemu-img convert -f SOURCEFORMAT -O DESTINATIONFORMAT SOURCEFILE DESTFILE
```

I have Virtualbox installed on my workstation (Ubuntu 24.04 LTS). There  is a Windows 10 installed on it for testing purposes. I'll copy its image  (obviously in vdi format) to my server to /srv/kvm directory, convert it to qcow2 and run it on my server using KVM. 

Copy Windows 10 image to the server  
**Run on my workstation**

```
scp windows10.vdi exforge@elma:/tmp
```

On my server
Convert image to qcow2

```
sudo qemu-img convert -f vdi -O qcow2 /tmp/windows10.vdi \
   /srv/kvm/windows10.qcow2
```

If we want to display the progress percentage while converting the image, add -p option.

```
sudo qemu-img convert -p -f vdi -O qcow2 /tmp/windows10.vdi \
   /srv/kvm/windows10.qcow2
```

Now we can add it as a KVM image

```
virt-install --name windows10 \
  --connect qemu:///system \
  --virt-type kvm --memory 2048 --vcpus 2 \
  --boot hd,menu=on \
  --disk path=/srv/kvm/windows10.qcow2,device=disk \
  --graphics vnc,port=5904,listen=0.0.0.0 \
  --os-variant win10 \
  --network bridge=br0 \
  --noautoconsole
```
   
### 6.4. Resize a Disk Image.
If you need extra disk space for your VM, you can increase the size of the image file.

```
sudo qemu-img resize FILENAME +SIZE
```

Resize an image, FILENAME is the name of the file which is the image for the VM.

SIZE could be something like +10G. Image size will be increased by (not to) this amount. it is possible to shrink with -

You must use the parameter --shrink to shrink the image

You must use partitioning tools in the VM to resize the disk to shrinked  size before shrinking.

To increase the size of my ubuntu20 VM's image by 5GB:

```
sudo qemu-img resize /srv/kvm/ubuntusrv-cloudimg.qcow2 +5G
```

### 6.5. Check an Image For Errors
```
qemu-img check FILENAME
```

In any case if you suspect the integrity of the image file

<br>
</details>

<details markdown='1'>
<summary>
7. Export and Import of VMs
</summary>

---
If you want to move your VM to another host, or in a way you want to backup and restore your VM; there might be a lot of ways to do it. I'm  going to demonstrate a very simple  method which requires shutting down the VM (you can try while it is running, but with no success guaranteed).

### 7.1. Export
---
First of all, let's prepare a place for our backup files, /tmp/kvmbackup  would be fine.

```
mkdir /tmp/kvmbackup
```

We need the definition file of our VM and the image file it is using. "virsh dumpxml" command creates the definition file in xml format, we can  save it with the VM's name.

```
virsh dumpxml ubuntu24 > /tmp/kvmbackup/ubuntu24.xml
```

This file contains all the necessary metadata information about our VM.

If our VM was installed from the scratch as in 2.1. there will be only 1 image file. But if it was installed from a cloud image as we did in 4. or if another disk was added as in 5.10; there would be more than 1 images. 

We need to copy all the images. 

Images used by the VM is listed in the xml file. Let's find them:

```
grep "source file" /tmp/kvmbackup/ubuntu24.xml
```

For my ubuntu24 VM, output is listed below:

```
      <source file='/srv/kvm/ubuntu24-seed.qcow2'/>
      <source file='/srv/kvm/ubuntusrv-cloudimg.qcow2'/>
```

That means I need to prepare 2 files: /srv/kvm/ubuntu24-seed.qcow2 and /srv/kvm/ubuntusrv-cloudimg.qcow2 .

Lets copy them to our backup locations.

```
cp /srv/kvm/ubuntu24-seed.qcow2 /srv/kvm/ubuntusrv-cloudimg.qcow2 \
   /tmp/kvmbackup
```

**Beware:** You can copy the files while the VM is running, but it is  advised to shutdown (or at least suspend your VM) before copying. Continue at your own risk.

Let's package them

```
tar -cf /tmp/ubuntu24.tar -C /tmp/kvmbackup .
```

Now we have /tmp/ubuntu24.tar, it has all the necessary data to import our VM anywhere.

You have to copy this file to another server, before importing there.

### 7.2. Import
Assuming we have another virtualization server and we have copied  ubuntu20.tar there, we are going to import it and make it operational.

**Beware:** Before importing your VM to another server, you have to remove it on the original server, otherwise you would have 2 guests with the same IP and that may cause unexpected (and unpleasant) results.

ubuntu24.tar is copied to the server's /tmp directory as /tmp/ubuntu24.tar

Create a place for our import files

```
mkdir /tmp/import
```

Extract tar file there

```
tar -xf /tmp/ubuntu24.tar -C /tmp/import
```

Now we need to move our image files to their directories as in the original server. If you have a different directory structure on your new server, and you want to copy files to different directories you have to  edit the xml file and change directories there.

```
sudo cp /tmp/import/ubuntu24-seed.qcow2 \
    /tmp/import/ubuntusrv-cloudimg.qcow2 /srv/kvm
```
 
It is time to define our server. Remember the xml file? We will use it  to define our ubuntu24 server.

```
virsh define /tmp/import/ubuntu24.xml
```

Now we can start it

```
virsh start ubuntu24
```

<br>
</details>

<details markdown='1'>
<summary>
8. libguestfs: VM Disk Management
</summary>

---
A set of commands for managing VM disks. Full documentation:  
[libguestfs.org](https://libguestfs.org/)

Normally, as a system admin, you won't need to reach to VM's disks. But there may happen a need once in a while. 

I think you already understand that when you have a VPS on a cloud server, the administrators of that cloud environment can reach your VPS' data. 

There are many tools, I'm going to try to explain only mounting commands. 

### 8.1. Installation
```
sudo apt update
sudo apt-get --yes install libguestfs-tools
```

### 8.2. Mounting VM's Disks
Works online (While the VM is running) Mount my VMs disk on my host's /mnt directory:

```
sudo guestmount -d ubuntu24 -i --ro /mnt
```

/mnt directory holds all the files of my VM. If you remove --ro, you can mount it with write permissions. But be very careful.

Unmount it:

```
sudo guestunmount /mnt
```

I prefer mounting with readonly permissions just to be safe.

Details for guestmount and guestunmount commands:

```
guestmount --help
guestunmount --help
```

### 8.3. All Commands
guestfish(1) — interactive shell  
guestmount(1) — mount guest filesystem in host  
guestunmount(1) — unmount guest filesystem  
virt-alignment-scan(1) — check alignment of virtual machine partitions  
virt-builder(1) — quick image builder  
virt-builder-repository(1) — create virt-builder repositories  
virt-cat(1) — display a file  
virt-copy-in(1) — copy files and directories into a VM  
virt-copy-out(1) — copy files and directories out of a VM  
virt-customize(1) — customize virtual machines  
virt-df(1) — free space  
virt-dib(1) — safe diskimage-builder  
virt-diff(1) — differences  
virt-edit(1) — edit a file  
virt-filesystems(1) — display information about filesystems, devices, LVM  
virt-format(1) — erase and make blank disks  
virt-get-kernel(1) — get kernel from disk  
virt-inspector(1) — inspect VM images  
virt-list-filesystems(1) — list filesystems  
virt-list-partitions(1) — list partitions  
virt-log(1) — display log files  
virt-ls(1) — list files  
virt-make-fs(1) — make a filesystem  
virt-p2v(1) — convert physical machine to run on KVM  
virt-p2v-make-disk(1) — make P2V ISO  
virt-p2v-make-kickstart(1) — make P2V kickstart  
virt-rescue(1) — rescue shell  
virt-resize(1) — resize virtual machines  
virt-sparsify(1) — make virtual machines sparse (thin-provisioned)  
virt-sysprep(1) — unconfigure a virtual machine before cloning  
virt-tail(1) — follow log file  
virt-tar(1) — archive and upload files  
virt-tar-in(1) — archive and upload files  
virt-tar-out(1) — archive and download files  

</details>

