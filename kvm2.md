---
title: "KVM Virtualization (Networking)"
description: "Advanced KVM networking configurations"
next: false
prev: false
sidebar: 
   label: KVM Virtualization (Networking)
---

##### Advanced KVM networking configurations

## 0. Specs

---
### 0.0. Definition
KVM Virtualization Tutorial 2 for Debian and Ubuntu Server.

Please refer to the KVM Virtualization Beginner tutorial before reading this one.

This tutorial focuses on KVM networking configurations.

### 0.1. Infrastructure
- **Server (Host)**: Debian (13/12) or Ubuntu (24.04/22.04) Server
   - IP: 192.168.1.121
   - Name: elma
   - NIC1: enp3s0f0
   - NIC2: enx00e04c534458 (USB network adapter)
- **Network1**: 192.168.1.0/24 (internet modem/router, first interface)
- **Network2**: 10.1.1.0/24 (external switch, second interface)
- **Workstation**: Debian 13 or Ubuntu 24.04 LTS Desktop

### 0.2. Resources
- ISBN: 978-1-78829-467-6 **KVM Virtualization Cookbook** by Konstantin Ivanov
- ISBN: 978-1-83882-871-4 **Mastering KVM Virtualization 2nd Ed.** by Vedran Dakic, Humble Devassy Chirammal, Prasad Mukhedkar, Anil Vettathu

<br>

## 1. KVM Networks - Configuration Commands

---
While numerous variations exist, KVM supports three basic network types:
- **Bridged**: VMs appear as physical devices on the network
- **NAT**: VMs share host's IP with network address translation
- **Isolated**: VMs communicate only with each other and host

 
### 1.1. Active Networks
List KVM Networks:

```
virsh net-list
```

Example output (after Tutorial 1 bridge configuration):

```
 Name           State    Autostart   Persistent
-------------------------------------------------
 host-bridge    active   yes         yes
```
 
Display detailed network information:

```
virsh net-info NETWORKNAME
virsh net-info host-bridge
```

Example output:

```
Name:           host-bridge
UUID:           a67dfcef-86e9-4e4c-832f-bc14443da475
Active:         yes
Persistent:     yes
Autostart:      yes
Bridge:         br0
```
 
Display network configuration as XML:

```
virsh net-dumpxml NETWORKNAME
virsh net-dumpxml host-bridge
```

Example output:

```
<network>
  <name>host-bridge</name>
  <uuid>a67dfcef-86e9-4e4c-832f-bc14443da475</uuid>
  <forward mode='bridge'/>
  <bridge name='br0'/>
</network>
```

### 1.2. Adding a Network
To add a network, create an XML configuration file and define it:

```
virsh net-define XMLFILE
```

**Example**: Create a second bridge on the second interface.

First, create the bridge on the host system.

#### Ubuntu Bridge Configuration
Edit Netplan configuration:
 
```
sudo nano /etc/netplan/01-netcfg.yaml
```

RReplace content with (adjust interface names and IPs):

```
network:
  ethernets:
    enp3s0f0:
      dhcp4: false
      dhcp6: false
    enx00e04c534458:
      dhcp4: false
      dhcp6: false
  bridges:
    br0:
      interfaces: [ enp3s0f0 ]
      addresses: [192.168.1.121/24]
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
    br1:
      interfaces: [ enx00e04c534458 ]
      addresses: [10.1.1.1/24]
      routes:
      - to: 10.1.1.0/24
        via: 10.1.1.1
      mtu: 1500
      nameservers:
        addresses: [8.8.8.8,8.8.4.4]
      dhcp4: false
      dhcp6: false
  version: 2
```

Apply configuration:

```
sudo netplan apply
```

#### Debian Bridge Configuration
Edit network interfaces file:

```
sudo nano /etc/network/interfaces
```

Replace content with (adjust interface names and IPs):

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
auto br1
iface br1 inet static
        address 10.1.1.1
        netmask 255.255.255.0
        network 10.1.1.0
        broadcast 10.1.1.255
        bridge_ports enx00e04c534458
        bridge_stp off
        bridge_fd 0
        bridge_maxwait 0
```

Apply configuration (SSH may disconnect):

```
sudo systemctl restart networking.service
```

#### Add Bridge to KVM
Create XML configuration for the second bridge:


```
sudo nano host-bridge2.xml
```

Fill as below:

```
<network>
  <name>host-bridge2</name>
  <uuid>c723a80b-d496-460e-9235-9eced7b218cf</uuid>
  <forward mode='bridge'/>
  <bridge name='br1'/>
</network>
```

**Note**: Generate a unique UUID with `uuidgen` if needed.

Define, start, and enable autostart:

```
virsh net-define host-bridge2.xml
virsh net-start host-bridge2
virsh net-autostart host-bridge2
```

Now you have two bridges:
- `br0` for 192.168.1.0/24 network
- `br1` for 10.1.1.0/24 network

### 1.3. Stopping and Removing KVM Networks
Stop a KVM Network:

```
virsh net-destroy NETWORKNAME
virsh net-destroy host-bridge2
```

Disable autostart:

```
virsh net-autostart NETWORKNAME --disable
virsh net-autostart host-bridge2 --disable
```

Remove network definition:

```
virsh net-undefine NETWORKNAME
virsh net-undefine host-bridge2
```

<br>

## 2. KVM Networks - Network Types

---
When creating KVM network XML files, use unique UUID and MAC values for each network.

Generate a random UUID:

```
uuidgen
```

Generate a random MAC address (or use online tools like [Browserling Random MAC Generator](https://www.browserling.com/tools/random-mac)).


### 2.1. Bridged Networks
Bridged networks connect VMs directly to the host's physical network. VMs appear as separate devices on the same network segment as the host.

**Use cases**:
- Public-facing servers
- Services requiring direct network access
- Environments with existing DHCP infrastructure

**Requirements**:
1. Create a bridge in the host's network configuration
2. Define the bridge in KVM via XML

**Example XML configuration**:

```
<network>
  <name>host-bridge2</name>
  <uuid>c723a80b-d496-460e-9235-9eced7b218cf</uuid>
  <forward mode='bridge'/>
  <bridge name='br1'/>
</network>
```

**Customization**:
- Replace `host-bridge2` with your network name
- Replace UUID with a generated value
- Replace `br1` with your actual bridge interface name

**Network integration**:
- VMs receive IPs from the same DHCP server as the host
- VMs are directly accessible from the network
- No NAT translation occurs



### 2.2. NAT Network
NAT (Network Address Translation) networks allow VMs to access external networks while remaining hidden behind the host's IP address.

**Use cases**:
- Development and testing environments
- VMs requiring internet access but not public exposure
- Security-focused deployments

**Example XML configuration**:

```
<network>
  <name>nat</name>
  <uuid>d589efd6-7d61-4f92-976b-bde62956cca7</uuid>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='brnat' stp='on' delay='0'/>
  <mac address='4a:c3:6a:72:c2:30'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.101' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>
```

**Customization**:
- Replace `nat` with your network name
- Replace UUID with a generated value
- Replace `brnat` with your preferred bridge name
- Replace MAC address with a generated value
- Adjust IP subnet and DHCP range as needed

**Network behavior**:
- VMs can initiate connections to external networks
- External hosts cannot initiate connections to VMs
- Port forwarding can be configured for specific services
- Built-in DHCP server provides IP addresses


### 2.3. Isolated Network
Isolated networks create completely private segments where VMs can communicate only with each other and the host.

**Use cases**:
- Database backends
- Internal service communication
- Security-sensitive applications
- Testing environments requiring network isolation

**Example XML configuration**:

```
<network>
  <name>isolated</name>
  <uuid>a67bbbaf-81e9-4e4c-832f-bc14443da475</uuid>
  <bridge name='brisolated' stp='on' delay='0'/>
  <mac address='4a:c3:6a:72:c2:26'/>
  <domain name='myisolateddomain'/>
  <ip address='192.168.20.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.20.101' end='192.168.20.200'/>
    </dhcp>
  </ip>
</network>
```

**Customization**:
- Replace `isolated` with your network name
- Replace UUID with a generated value
- Replace `brisolated` with your preferred bridge name
- Replace MAC address with a generated value
- Adjust IP subnet and DHCP range as needed
- Set domain name for internal DNS

**Security architecture example**:
```
Internet ── [Web Server (dual NIC)] ── [Database Server]
             bridged:192.168.1.x/24    isolated:192.168.20.x/24
```

**Implementation**:
1. Web server: One interface in bridged network, one in isolated network
2. Database server: Only isolated network interface
3. Result: Database accessible only via web server

**Network characteristics**:
- No external network access
- Built-in DHCP server
- Internal DNS resolution via domain name
- Complete isolation from external traffic

<br>

!!!


## 3. Case Study A: Bridged and Isolated Networks Together

---
### 3.1. Specifications
- **Network1**: Bridged network on 192.168.1.0/24 (existing)
- **Network2**: Isolated network on 192.168.20.0/24 (to create)
- **VM1**: Two network interfaces
  - Interface 1: Network1 (bridged)
  - Interface 2: Network2 (isolated)
- **VM2**: One network interface
  - Interface: Network2 (isolated)

**Architecture**:
- VM1: Accessible from all network devices (via Network1)
- VM2: Accessible only from VM1 (via Network2)
- VM1 acts as a gateway between the two networks

### 3.2. Create the Isolated Network
Create XML configuration file:

```
nano isolated.xml
```

Fill as below:

```
<network>
  <name>isolated</name>
  <uuid>a67bbbaf-81e9-4e4c-832f-bc14443da475</uuid>
  <bridge name='brisolated' stp='on' delay='0'/>
  <mac address='4a:c3:6a:72:c2:26'/>
  <domain name='myisolateddomain'/>
  <ip address='192.168.20.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.20.101' end='192.168.20.200'/>
    </dhcp>
  </ip>
</network>
```

Define and activate the network:

```
virsh net-define isolated.xml
virsh net-start isolated
virsh net-autostart isolated
```

Verify network creation:

```
virsh net-list --all
```

### 3.3. Create VMs with Dual Network Configuration
**Create VM1 (dual-homed)**:

```
sudo virt-install --name vm1 \
    --connect qemu:///system  --virt-type kvm \
    --memory 1024 --vcpus 1 \
    --disk /srv/kvm/vm1.qcow2,format=qcow2,size=10 \
    --cdrom /srv/isos/ubuntu-22.04.2-live-server-amd64.iso  \
    --network bridge=br0 \
    --network bridge=brisolated \
    --graphics vnc,port=5901,listen=0.0.0.0 \
    --os-variant ubuntu22.04 \
    --noautoconsole
```

**Create VM2 (isolated)**:

```
sudo virt-install --name vm2 \
    --connect qemu:///system  --virt-type kvm \
    --memory 1024 --vcpus 1 \
    --disk /srv/kvm/vm2.qcow2,format=qcow2,size=10 \
    --cdrom /srv/isos/ubuntu-22.04.2-live-server-amd64.iso  \
    --network bridge=brisolated \
    --graphics vnc,port=5902,listen=0.0.0.0 \
    --os-variant ubuntu22.04 \
    --noautoconsole
```

**Note for Debian 12 hosts**: Replace `--os-variant ubuntu24.04` with `--os-variant ubuntu22.04`.

Connect to VMs from your workstation to complete installation:

 
### 3.4. Network Configuration Considerations
**Isolated Network Limitations**:
- VM2 cannot access external networks (including internet)
- VM2 cannot receive updates or install packages directly
- VM1 can access both networks and act as a gateway

**Proxy Solution for Package Management**:
Install Squid proxy on the host to provide internet access for isolated VMs.

**Host Configuration (Simplified)**:
```
sudo apt update
sudo apt install squid --yes
sudo nano /etc/squid/squid.conf
```

Add to configuration:
```
http_port 192.168.20.1:3128
acl localnet src 192.168.20.0/24
http_access allow localnet
```

Restart Squid:
```
sudo systemctl restart squid
```

**VM Configuration (apt proxy)**:
On each isolated VM (VM2 in our case):

```
sudo nano /etc/apt/apt.conf
```

Add for unauthenticated proxy:
```
Acquire::http::Proxy "http://192.168.20.1:3128";
```

For authenticated proxy:
```
Acquire::http::Proxy "http://username:password@192.168.20.1:3128";
```

**Security Considerations**:
1. The proxy allows package downloads but maintains network isolation
2. Consider firewall rules to restrict proxy access
3. Monitor proxy logs for unusual activity
4. Use HTTPS proxy for additional security

**Testing Connectivity**:
From VM2:
```
ping 192.168.20.1                    # Should work (host isolated IP)
ping 192.168.1.1                     # Should fail (external network)
curl --proxy http://192.168.20.1:3128 http://example.com  # Should work
```

<br>

## 4. Case Study B: Separating Host and VM Access with 2 NICs

---
Separating host and VM network traffic is a recommended practice for improved security, performance, and management. We'll dedicate one interface for host access and another for VM traffic.

### 4.1. Specifications
- **Network**: 192.168.1.0/24 (single subnet)
- **Host Interfaces**:
  - NIC1 (enp3s0f0): VM traffic via bridge (192.168.1.121)
  - NIC2 (enx00e04c534458): Host management (192.168.1.122)
- **VM Configuration**: Single interface on bridged network

**Benefits**:
- Isolate host management traffic from VM traffic
- Prevent VM network issues from affecting host access
- Simplified firewall rules and monitoring
- Better performance isolation

### 4.2. Host Network Configuration
Configure the server's network interfaces before KVM setup.

#### Ubuntu Network Configuration
Edit Netplan configuration:

```
sudo nano /etc/netplan/01-netcfg.yaml
```

Change as below:

```
network:
  ethernets:
    enp3s0f0:
      dhcp4: false
      dhcp6: false
    enx00e04c534458:
      addresses: [192.168.1.122/24]
      routes:
      - to: 192.168.1.0/24
        via: 192.168.1.1
      nameservers:
        addresses: 
        - 8.8.8.8
        - 8.8.4.4
  bridges:
    br0:
      interfaces: [ enp3s0f0 ]
      addresses: [192.168.1.121/24]
      routes:
      - to: default
        via: 192.168.1.1
      mtu: 1500
      nameservers:
        addresses: 
        - 8.8.8.8
        - 8.8.4.4
      dhcp4: false
      dhcp6: false
  version: 2
```

Apply configuration and reboot:

```
sudo netplan apply
sudo reboot
```

#### Debian Network Configuration
Edit network interfaces file:

```
sudo nano /etc/network/interfaces
```

```bash
auto lo
iface lo inet loopback

# VM traffic interface (bridged)
auto enp3s0f0
iface enp3s0f0 inet manual

# Bridge for VMs
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

# Host management interface
auto enx00e04c534458
iface enx00e04c534458 inet static
        address 192.168.1.122
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.1.255
        gateway 192.168.1.1
        dns-nameservers 8.8.8.8
```

Apply configuration (SSH may disconnect):

```
sudo systemctl restart networking.service
```

**Network Verification**:
```
ip addr show br0
ip addr show enx00e04c534458
ping -c 3 192.168.1.1
```


---

### 4.3. KVM Network Configuration
Define the bridged network in KVM:

Create XML configuration:
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

Define and activate network:

```
virsh net-define host-bridge.xml
virsh net-start host-bridge
virsh net-autostart host-bridge
```

Verify network creation:

```
virsh net-list --all
virsh net-info host-bridge
```

### 4.4. Create VM on the Bridged Network
Create a VM using the bridged interface:

```
sudo virt-install --name vm3 \
    --connect qemu:///system  --virt-type kvm \
    --memory 1024 --vcpus 1 \
    --disk /srv/kvm/vm3.qcow2,format=qcow2,size=10 \
    --cdrom /srv/isos/ubuntu-22.04.2-live-server-amd64.iso  \
    --network bridge=br0 \
    --graphics vnc,port=5901,listen=0.0.0.0 \
    --os-variant ubuntu22.04 \
    --noautoconsole
```

**Connect to VM**:
```
virt-viewer --connect qemu+ssh://exforge@elma/system vm3
```

**Network Verification**:
1. Host should be accessible at 192.168.1.122
2. VM should obtain an IP from 192.168.1.0/24 range
3. Both should have internet access via 192.168.1.1

**Firewall Considerations**:
Consider implementing firewall rules to:
- Restrict host management interface access
- Separate VM traffic rules
- Monitor traffic patterns


<br>

!!!

## 5. Case Study C: NAT KVM Network

---
We will create a VM, in a NAT network.

### 5.1. Specs:
Create a VM within a NAT (Network Address Translation) network for enhanced security and isolation.

### 5.1. Specifications
**Server Configuration**:
- Interface 1 (enp3s0f0): Bridged mode for VMs (as configured in Section 4)
- Interface 2 (enx00e04c534458): Standard mode for host management
- Additional NAT network for isolated VMs

**VM Configuration**:
- Name: `vmn` (VM-NAT)
- Single interface connected to NAT network
- Outbound internet access via NAT
- Inbound connections blocked (except port forwarding)


### 5.2. Host Network Configuration
No changes required if you completed Section 4.2. Verify existing configuration:

```
ip addr show br0
ip addr show enx00e04c534458
```

### 5.3. KVM NAT Network Configuration
Create XML configuration file:

```
nano nat.xml
```

Fill as below:

```
<network>
  <name>nat</name>
  <uuid>d589efd6-7d61-4f92-976b-bde62956cca7</uuid>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='brnat' stp='on' delay='0'/>
  <mac address='4a:c3:6a:72:c2:30'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.101' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>
```

**Important**: Generate unique values:
- UUID: `uuidgen`
- MAC address: Use a random generator or `openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'`

Define and activate the NAT network:

```
virsh net-define nat.xml
virsh net-start nat
virsh net-autostart nat
```

Verify network creation:

```
virsh net-list --all
virsh net-info nat
virsh net-dumpxml nat
```


### 5.4. Create VM on NAT Network
Create the NAT-connected VM:

```
sudo virt-install --name vmn \
    --connect qemu:///system  --virt-type kvm \
    --memory 1024 --vcpus 1 \
    --disk /srv/kvm/vmn.qcow2,format=qcow2,size=10 \
    --cdrom /srv/isos/ubuntu-22.04.2-live-server-amd64.iso  \
    --network bridge=brnat \
    --graphics vnc,port=5902,listen=0.0.0.0 \
    --os-variant ubuntu22.04 \
    --noautoconsole
```

**Note**: For Debian 12 hosts, use `--os-variant ubuntu22.04`.

### 5.5. NAT Network Behavior
**Outbound Access (VM → External)**:
- VM can initiate connections to external networks
- Source IP translated to host's IP (192.168.1.121)
- Source ports mapped to 1024-65535 range

**Inbound Access (External → VM)**:
- External devices cannot initiate connections to VM
- Port forwarding required for specific services
- VM remains hidden behind NAT

**Internal Network**:
- DHCP range: 192.168.122.101-254
- Gateway: 192.168.122.1 (host)
- DNS: Inherited from host configuration



<br>

## 6. Adding and Removing Networks To/From a VM 

---
Dynamically modify VM network interfaces without recreating the VM.

### 6.1. Specifications
- **VM Name**: `vmtest`
- **Initial Network**: `host-bridge` (bridge `br0`)
- **Network to Add**: `nat` (bridge `brnat`)
- **Network to Remove**: `host-bridge` (bridge `br0`)

**Process**:
1. Create VM with bridged network
2. Add NAT network interface
3. Configure new interface on VM
4. Remove original bridged interface


### 6.2. Create VM with Bridged Network
Create initial VM:

```
sudo virt-install --name vmtest \
    --connect qemu:///system  --virt-type kvm \
    --memory 1024 --vcpus 1 \
    --disk /srv/kvm/vm.qcow2,format=qcow2,size=10 \
    --cdrom /srv/isos/ubuntu-22.04.2-live-server-amd64.iso  \
    --network bridge=br0 \
    --graphics vnc,port=5902,listen=0.0.0.0 \
    --os-variant ubuntu22.04 \
    --noautoconsole
```

### 6.3. Add NAT Network Interface
Add a second network interface to the running VM:

```
virsh attach-interface vmtest \
    bridge brnat \
    --target ens1 \
    --config
```

**Parameters**:
- `bridge brnat`: Network type and bridge name
- `--target ens1`: Interface name inside VM
- `--config`: Persistent after shutdown/start

**Alternative for Powered-off VM**:
```
virsh attach-interface vmtest \
    bridge brnat \
    --target ens1 \
    --config \
    --persistent
```

**Restart VM** (required for interface activation):
```
virsh destroy vmtest
virsh start vmtest
```

**Important**: `virsh reboot` may not activate new interfaces; use shutdown/start cycle.

### 6.4. Configure New Network Interface on VM
Configure the new interface (`ens1`) on the Ubuntu VM.

**On the VM**:

Check available interfaces:
```
ip link show
```

Configure Netplan (Ubuntu):

```
sudo nano /etc/netplan/00-installer-config.yaml
```

```yaml
network:
  ethernets:
    enp1s0:
      dhcp4: true
    ens1:
      dhcp4: true
  version: 2
```

**For Debian VMs**, use `/etc/network/interfaces**:

```
sudo nano /etc/network/interfaces
```

```bash
auto lo
iface lo inet loopback

auto enp1s0
iface enp1s0 inet dhcp

auto ens1
iface ens1 inet dhcp
```

Apply configuration:

**Ubuntu**:
```
sudo netplan apply
```

**Debian**:
```
sudo systemctl restart networking
```

Verify network configuration:
```
ip addr show
ip route show
```


### 6.5. Remove Bridged Network Interface
Remove the original bridged interface (`enp1s0`).

**On the VM**:

Identify MAC address of interface to remove:
```
ip link show enp1s0
```

Example output:
```
2: enp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 52:54:00:83:3c:a0 brd ff:ff:ff:ff:ff:ff
```

**MAC Address**: `52:54:00:83:3c:a0`

**On the Host**:

Detach interface using MAC address:
```
virsh detach-interface vmtest \
    bridge \
    --mac 52:54:00:83:3c:a0 \
    --config
```

**Parameters**:
- `bridge`: Network type
- `--mac`: MAC address of interface to remove
- `--config`: Persistent after shutdown/start

**For immediate removal** (if VM is running):
```
virsh detach-interface vmtest \
    bridge \
    --mac 52:54:00:83:3c:a0 \
    --live \
    --config
```

**Shutdown and start VM** to complete removal:
```
virsh destroy vmtest
virsh start vmtest
```


<br>
