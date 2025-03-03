##### KVMOnDebianUbuntu2: 
# KVM Tutorial 2 On Debian and Ubuntu Server (KVM Networking)

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.0. Definition
KVM virtualization Tutorial 2 on Debian and Ubuntu Server. 

Please refer to [1st KVM tutorial](KVMOnDebianUbuntu1.html) before reading this one.

This tutorial specializes on KVM Networking.

### 0.1. Infrastructure
- Server (Host): Debian (12/11) or Ubuntu (24.04/22.04) Server
   - IP: 192.168.1.121 
   - Name: elma
   - NIC1: enp3s0f0
   - NIC2: enx00e04c534458
- Network1: 192.168.1.0/24 which is supplied by my internet modem (1st  interface)
- Network2: 10.1.1.0/24 with an external switch (2nd interface)
- Workstation: Debian 12 or Ubuntu 24.04 LTS Desktop

### 0.2. Resources
ISBN: 978-1-78829-467-6 **KVM Virtualization Cookbook** by Konstantin Ivanov

ISBN: 978-1-83882-871-4 **Mastering KVM Virtualization 2nd Ed.** by Vedran    Dakic, Humble Devassy Chirammal, Prasad Mukhedkar, Anil Vettathu

<br>
</details>

<details markdown='1'>
<summary>
1. KVM Networks - Configuration Commands
</summary>
---
Although it is possible to produce endless variations, there are 3 basic  network types in KVM: Bridged, NAT, and Isolated.

Before exploring KVM networking more, let's revise the commands for it.
 
### 1.1. Active Networks
List KVM Networks:

```
virsh net-list
```

We've already configured a bridged network on tutorial 1, so my server  gives the following output:

```
 Name           State    Autostart   Persistent
-------------------------------------------------
 host-bridge    active   yes         yes
```
 
To display information about a network, the following command can be used:

```
virsh net-info NETWORKNAME
virsh net-info host-bridge
```

Output on my server:

```
Name:           host-bridge
UUID:           a67dfcef-86e9-4e4c-832f-bc14443da475
Active:         yes
Persistent:     yes
Autostart:      yes
Bridge:         br0
```
 
We can display the information for the network as an XML file too:

```
virsh net-dumpxml NETWORKNAME
virsh net-dumpxml host-bridge
```

Output on my server:

```
<network>
  <name>host-bridge</name>
  <uuid>a67dfcef-86e9-4e4c-832f-bc14443da475</uuid>
  <forward mode='bridge'/>
  <bridge name='br0'/>
</network>
```

### 1.2. Adding a Network
To add a network, we must prepare the configuration in an XML file, and  use the name of the file as a parameter.

```
virsh net-define XMLFILE
```

As an example, I'm going to create another bridge on my 2nd interface and add that bridge to the KVM as another network.

Before creating a bridge on the KVM, we have to create it on the server. 

As Debian and Ubuntu have different ways of network configuration, we will do it for both of them.

**!!! Creating the Bridge on Ubuntu BEGIN !!!**

Edit netplan file to define the bridge. (If your netplan file is named as something else, change it below to that.
 
```
sudo nano /etc/netplan/01-netcfg.yaml
```

Remove its content , fill it as below, beware of changing enp3s0f0 and  enx00e04c534458 to your interfaces' names.

Also remember to change IP addresses as in your networks too.

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

Activate the new configuration

```
sudo netplan apply
```

**!!! Creating the Bridge on Ubuntu END !!!**

---

**!!! Creating the Bridge on Debian BEGIN !!!**

Edit your network config file
sudo nano /etc/network/interfaces

Remove its content , fill it as below, beware of changing enp3s0f0 and  enx00e04c534458 to your interfaces' names.

Also remember to change IP addresses as in your networks too.

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

Apply the changes. If you connect through ssh, you connection may break.  In this case, close the terminal and reconnect.

```
sudo systemctl restart networking.service
```

**!!! Creating the Bridge on Debian END !!!**

---


enp3s0f0 is my 1st interface, its name is a bit funny, but my 2nd  interface really has a weird name as enx00e04c534458. I guess that is  because it is an USB network adapter. 

Anyway, don't forget to change the names as your adapters'.

Now, it is time to create the XML file for the second bridge (namely br1).

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

Now we can define it

```
virsh net-define host-bridge2.xml
```

Start it:

```
virsh net-start host-bridge2
virsh net-start NETWORKNAME
```

Make it autostart (Starts when the server starts)

```
virsh net-autostart host-bridge2
virsh net-autostart NETWORKNAME
```

Now we have 2 bridges. If we want a VM in 192.168.1.0/24 network we use  br0, if we want it in 10.1.1.0/24 then we use br1.

### 1.3. Stopping and Removing KVM Networks
Stop a KVM Network

```
virsh net-destroy NETWORKNAME
virsh net-destroy host-bridge2
```

Disable autostart property of a KVM Network

```
virsh net-autostart NETWORKNAME --disable
virsh net-autostart host-bridge2 --disable
```

Remove a KVM Network

```
virsh net-undefine NETWORKNAME
virsh net-undefine host-bridge2
```

<br>
</details>

<details markdown='1'>
<summary>
2. KVM Networks - Network Types
</summary>
---
When preparing XML files for creating KVM networks, we use UUID and MAC  values. These UUID and MAC values must be unique for each network.  Remember to replace them with unique values.

Random UUID Generator:

```
uuidgen
```

Random MAC Address Generator:

[www.browserling.com](https://www.browserling.com/tools/random-mac)

### 2.1. Bridged Networks
I believe you already have an idea of bridged networks. It is like the  host is sharing its interface and network with the VM. VM is in the same network as the host. If there is a DHCP Server on the network the host  resides, the VM can use it to get an IP.

If you are going to use a server which directly serves information or a service to the users, most probably you'll use a Bridged Network.

To use a bridged network, first you need to create the bridge in the host machine's network configuration, and then prepare an XML file and add the network to the KVM with `virsh net-define` command, as we did in 1.2.

A sample Bridged Network XML File:

```
<network>
  <name>host-bridge2</name>
  <uuid>c723a80b-d496-460e-9235-9eced7b218cf</uuid>
  <forward mode='bridge'/>
  <bridge name='br1'/>
</network>
```

Considerations:

- Replace host-bridge2 with your chosen network name.
- Replace c723a80b-d496-460e-9235-9eced7b218cf with your generated uuid.
- Replace br1 with your bridge name in netplan file.


### 2.2. NAT Network
A NAT (Network Address Translation) Network is similar to (actually the same as) your home network behind your internet router. Your host's interface stands like your internet router and VMs are like your home devices. 

When VMs want to access to the network, they use host's IP address, but the other devices on the network cannot access to your VMs.

This type of network is useful when you don't want anyone to access your  VMs, but you want your VMs to access everywhere. 
 
An example of NAT Network XML File:

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

Considerations:

- Replace nat with your chosen network name.
- Replace d589efd6-7d61-4f92-976b-bde62956cca7 with your generated uuid.
- Replace brnat with your chosen bridge name.
- Replace 52:54:00:6e:a9:d8 with your generated MAC address.
- Our nat bridge will have 192.168.122.1/24 IP and a DHCP server will announce addresses between 192.168.122.101 and 192.168.10.254. Change these values as you like.


### 2.3. Isolated Network
An Isolated Network, as the name implies, is isolated. Noone can go out, noone can come in. 

The VMs in the isolated network cannot reach outside, and the devices outside cannot reach the VMs in the isolated network. Only the devices in the isolated network can reach to each other.

Although it is very useful for testing purposes, there might be some situations that isolated network could be very useful in the production. 

Consider you have a web server and a database server. The DB server can only be accessed by the web server and the web server will be accessed by everyone. You can put the DB server in an isolated network and define 2 interfaces for the web server as 1 in a bridged network and the other one in the isolated network. That way, noone other than the web server can access the DB server.

An example of Isolated Network XML File:

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

Considerations:

- Replace isolated with your chosen network name.
- Replace a67bbbaf-81e9-4e4c-832f-bc14443da475 with your generated uuid.
- Replace brisolated with your chosen bridge name.
- Replace 55:33:00:dd:dd:ee with your generated MAC address.
- Our nat bridge will have 192.168.20.1/24 IP and a DHCP server will  announce addresses between 192.168.20.101 and 192.168.20.200. Change these values as you like.

<br>
</details>

<details markdown='1'>
<summary>
3. Case Study A: Bridged and Isolated Networks Together
</summary>
---
### 3.1. Specs:
- Our host has a bridged network on 192.168.1.0/24 (Network 1)
- Our host has an isolated network on 192.168.20.0/24 (Network 2)
- Our VM1 has 2 interfaces, 1 in Network1 and 1 in Network2
- Our VM2 has 1 interface in Network2
- After the installations, VM2 will be accessed by VM1 only, but VM1 will  be accessed by all the devices on the network.

### 3.2. Create the Networks
We already have Network1, lets create Network2

Prepare XML File

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

Create the network

```
virsh net-define isolated.xml
```

Start it:

```
virsh net-start isolated
```

Make it autostart 

```
virsh net-autostart isolated
```

### 3.3. Create VM1 and VM2
VM1

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

VM2

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

On Debian 11, --os-variant ubuntu22.04 gives an error. In that case,  change it as --os-variant ubuntu20.04.

Now you can connect VM1 and VM2 from your workstation and install them. 
 
### 3.4. Considerations for Isolated Networks
If a VM is in an isolated network, and if it has no connections to the other networks, it cannot connect to the internet. That means, VM1 can connect  to the internet and VM2 cannot connect to the internet. 

Actually, when we put it in an isolated network, we accepted that it won't connect to other networks. But we need internet to install or update applications.

I have a not so bad solution for this situation. Install squid proxy to  the host, make it listen to Isolated Network IP of host (192.168.20.1),  allow all IPs to access it. Configure your VMs to use "apt" command  through a proxy.

I won't go in the details of installing and configuring squid proxy here, there are tons of materials on the internet about it. 

Configure your VM to use apt commands through a proxy:

**!!! Run on your VM !!!**

```
sudo nano /etc/apt/apt.conf
```

Add the following line:

```
Acquire::http::proxy "http://192.168.20.1:3128";
```

If you use username/password for the proxy, use the following format:

```
Acquire::http::proxy "http://user:pass@proxyserver:port";
```

<br>
</details>

<details markdown='1'>
<summary>
4. Case Study B: Separating Host and VM Access with 2 NICs
</summary>
---
I don't know if it would be a best practice but definitely it will be a  good practice to separate host's and VMs' network. That means, we will  connect our host to our network with 2 interfaces; 1 interface will be  used for accessing the host and the other will be used to access VMs.

### 4.1. Specs:
- Both interfaces of host are connected to my internet router.
- Our host has a bridged network on 192.168.1.0/24 (192.168.1.121-NIC 1)
- Our host has a standart network on 192.168.1.0/24 (192.168.1.122-NIC 2) 
- Our VM will have 1 interface on bridged network. 
- The first nic will be used by VMs and the second nic will be used to  access the host.

### 4.2. Host Network Configuration
Before the KVM network configuration, we need to configure the server's  network. 

- Again, Debian and Ubuntu have different steps:

---
**!!! Ubuntu Network Configuration BEGIN !!!**

Edit netplan file (change if your netplan file has a different name):

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

Apply the configuration, (You'd better restart the host)

```
sudo netplan apply
```

**!!! Ubuntu Network Configuration END !!!**

---
**!!! Debian Network Configuration BEGIN !!!**

Edit your network config file

```
sudo nano /etc/network/interfaces
```

Change as below:

```
auto lo
iface lo inet loopback
auto enp3s0f0
iface enp3s0f0 inet manual
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
auto enx00e04c534458
iface enx00e04c534458 inet static
        address 192.168.1.122
        netmask 255.255.255.0
        network 192.168.1.0
        gateway 192.168.1.1
```

Apply the changes. If you connect through ssh, your connection may break. In this case, close the terminal and reconnect.

```
sudo systemctl restart networking.service
```

**!!! Debian Network Configuration END !!!**

---

### 4.3. KVM Network Configuration
We already configured our br0 bridge on KVM. But in case you didn't do  it, or removed it.

If you already have it, skip this step.

```
nano host-bridge.xml

Fill as below:

```
<network>
  <name>host-bridge</name>
  <forward mode="bridge"/>
  <bridge name="br0"/>
</network>

Define the KVM Network

```
virsh net-define host-bridge.xml
```

Start and make it autostarted:

```
virsh net-start host-bridge
virsh net-autostart host-bridge
```

### 4.4. Create a VM on the Bridged Network
Now, if we create a VM on br0 bridge, it will use the first interface of # the host, and we will keep using the second interface at 192.168.1.202

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

<br>
</details>

<details markdown='1'>
<summary>
5. Case Study C: NAT KVM Network
</summary>
---
We will create a VM, in a NAT network.

### 5.1. Specs:
Server: 

-  Interface 1 is in bridged mode (as in 4.)
-  Interface 2 is in standard mode (as in 4.)
-  A NAT KVM network will be added.

VM (Named vmn):
-  An interface will be connected to the nat network

### 5.2. Host Network Configuration
There is no change needed if you applied 4.2. Otherwise do it now.

### 5.3. KVM NAT Network Configuration
Prepare XML File

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

Remember to generate a new uuid and a new MAC address

Define the KVM Network

```
virsh net-define nat.xml
```

Start and make it autostarted:

```
virsh net-start nat
virsh net-autostart nat
```

### 5.4. Create the VM
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

Your VM will be able to connect to your network, but the devices on your  network will not be able to connect to it.

<br>
</details>

<details markdown='1'>
<summary>
6. Adding and Removing Networks To/From a VM 
</summary>
---
I assume that we have bridged and isolated networks ready on our host.

### 6.1. Specs
- VM Name: vm
- Initial Network: host-bridge (bridge br0)
- Network to be added: nat (bridge brnat)
- Network to be removed: host-bridge (bridge br0)


We will create a VM with br0, then we will add it to the nat network, and then we will remove the br0 network.

### 6.2. Create a VM with Bridged Network
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

### 6.3. Add an Interface to the VM at the Isolated Network
Add an interface to the VM named vm, network type is bridge and bridge  name is brnat, interface name on the VM (--target) will be ens1 and it  will be active after shutdown and start again.

```
virsh attach-interface vmtest bridge brnat --target ens1 --config
```

Alternatively, you may add the network when the VM is off.

Restart the VM, either by logging into it, or using the following  commands at the host :

```
virsh destroy vmtest
virsh start vmtest
```

`virsh reboot` does not work, it restarts the VM but the interface does  not become active.

### 6.4. Configure the New Network at the VM
The new interface ens1 will become active at the VM but it won't start,  because it is not configured. We need to configure it using the netplan  file.

**!!! Run on the VM !!!**

Our VM is Ubuntu, if it were Debian, you should have configured the  network through /etc/network/interfaces file

```
sudo nano /etc/netplan/00-installer-config.yaml
```

Change it as below

```
network:
  ethernets:
    enp1s0:
      dhcp4: true
    ens1:
      dhcp4: true
  version: 2
```
 
Activate it

```
sudo netplan apply
```

Now the VM will have an IP from 192.168.122.0/24 (nat) network for the  2nd interface.

### 6.5. Remove the Bridged Network from the VM
We want to remove the Bridged Network from the VM, we will accomplish it  by removing its first interface (enp1s0). 

To do it, we need the MAC Address of the interface. Run the following command on the VM:

**!!! Run on the VM !!!**

ip link show

It will display something like below:

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 52:54:00:83:3c:a0 brd ff:ff:ff:ff:ff:ff
3: ens1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 52:54:00:70:55:cf brd ff:ff:ff:ff:ff:ff
```

My first interface is enp1s0, most probably yours will be the same, or  something like it.

At the line under the one starting with "2: enp1s0...", the part after # link/ether is the MAC Address. Mine is: 52:54:00:83:3c:a0

**Now we return back to our host:**

```
virsh detach-interface vmtest bridge --mac 52:54:00:83:3c:a0 --config
```

When you shutdown and start your VM, the interface will be gone.

</details>

