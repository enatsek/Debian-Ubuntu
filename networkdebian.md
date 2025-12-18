##### Network On Debian 
# Network Configuration On Debian Servers 

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. The What
Network configuration examples for Debian 12 and 13.

Tried to be as thorough as possible: single NIC, multiple NICs, multiple networks, NIC bonding.

Debian and Ubuntu network configurations are very different, so there are separate tutorials for Debian and Ubuntu.

#### 0.1. Configuration Files
Debian 12 & 13 use ifupdown for network configuration.

The main configuration file is `/etc/network/interfaces`. This file includes all files in the `/etc/network/interfaces.d/` directory.

It is good practice to keep `/etc/network/interfaces` as shown below and create a separate configuration file for each NIC in the `/etc/network/interfaces.d/` directory.

```
sudo nano /etc/network/interfaces
```

```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
source /etc/network/interfaces.d/*
#
# The loopback network interface
auto lo
iface lo inet loopback
```

### 0.2. Name Server Configuration
The name server configuration file is `/etc/resolv.conf`. It can be as simple as:

```
nameserver 192.168.1.1
```

Or it may have more detailed configuration:

```
# /etc/resolv.conf
# Primary DNS server
nameserver 8.8.8.8
# Secondary DNS server
nameserver 8.8.4.4
# Tertiary DNS server (optional)
#nameserver 1.1.1.1
# Search domains (optional)
# If a domain name is provided without a fully qualified domain name (FQDN),
# the system appends these search domains to the provided domain to perform 
# DNS lookups.
# For example, if "example.com" is provided in a lookup, and "search 
# localdomain" is configured, the system will also try to resolve 
# example.com.localdomain".
search localdomain
```

### 0.3. Configuration Commands
Stop a NIC:

```
sudo ifdown enp0s3
```

Start a NIC:

```
sudo ifup enp0s3
```

To restart a NIC, stop it and start it again:

```
sudo ifdown enp0s3 && sudo ifup enp0s3
```

Restart networking (restarts all NICs and other networking services):

```
sudo systemctl restart networking
```

### 0.4. Sources
- [www.mybluelinux.com](https://www.mybluelinux.com/debian-permanent-static-routes/)
- [Debian Wiki](https://wiki.debian.org/NetworkConfiguration)
- [www.debian.org](https://www.debian.org/doc/manuals/debian-handbook/sect.network-config)
- [Deepseek](https://www.deepseek.com/)
- [ChatGPT](https://chatgpt.com/)

<br>
</details>

<details markdown='1'>
<summary>
1. Example Configurations
</summary>

---
### 1.1. DHCP Configuration
Our NIC is enp0s3.

```
sudo nano /etc/network/interfaces.d/enp0s3
```

Fill as below:

```
auto enp0s3
iface enp0s3 inet dhcp
```

Restart networking:

```
sudo systemctl restart networking
```

### 1.2. Static IP Configuration
Our NIC is enp0s3.

```
sudo nano /etc/network/interfaces.d/enp0s3
```

Fill as below:

```
auto enp0s3
iface enp0s3 inet static
  address 192.168.1.135/24
  broadcast 192.168.1.255
  network 192.168.1.0
  gateway 192.168.1.1
```

```
sudo systemctl restart networking
```

### 1.3. Static IP Configuration with 2 IPs
Our NIC is enp0s3.

```
sudo nano /etc/network/interfaces.d/enp0s3
```

Fill as below:

```
auto enp0s3
iface enp0s3 inet static
  address 192.168.1.196/24
  broadcast 192.168.1.255
  network 192.168.1.0
  gateway 192.168.1.1
iface enp0s3 inet static
  address 10.1.1.1/8
```

```
sudo systemctl restart networking
```

### 1.4. Static IP Configuration with 2 NICs
Our NICs are enp0s3 and enp0s8.

First NIC:

```
sudo nano /etc/network/interfaces.d/enp0s3
```

Fill as below:

```
auto enp0s3
iface enp0s3 inet static
  address 192.168.1.196/24
  broadcast 192.168.1.255
  network 192.168.1.0
  gateway 192.168.1.1
```

Second NIC:

```
sudo nano /etc/network/interfaces.d/enp0s8
```

Fill as below:

```
auto enp0s8
iface enp0s8 inet static
  address 10.1.1.1/8
  broadcast 10.255.255.255
  network 10.0.0.0
```

Restart networking:

```
sudo systemctl restart networking
```

<br>
</details>

<details markdown='1'>
<summary>
2. Case Study - Multiple Networks
</summary>

---
### 2.0. Specs
We have 2 separate networks (192.168.1.X and 10.X.X.X). Some hosts from one network need to reach hosts in the other network.

We will install a new host to act as a router between the networks.

The host will have 2 NICs (one in each network), and we'll enable IP routing on it.

This way, hosts in one network will be able to reach hosts in the other network. This will be possible by defining IP routes on the hosts to use the server with 2 NICs as a router to the other network.

Hosts in the 192.168.1.X network use 192.168.1.1 as the default gateway; hosts in the 10.X.X.X network use 10.1.1.1 as the default gateway.

Our router will have 2 NICs: one with IP 192.168.1.196 and the other with IP 10.1.1.196.

Hosts in the 192.168.1.X network will use 192.168.1.196 to reach the 10.X.X.X network. Hosts in the 10.X.X.X network will use 10.1.1.196 to reach the 192.168.1.X network.

We will configure:

- The router (192.168.1.196 & 10.1.1.196)
- The host in the first network (192.168.1.197)
- The host in the second network (10.1.1.198)

Then we'll check connectivity between them.


### 2.1. Configuration of the Router
We have 2 NICs (enp0s3 - 192.168.1.X network, and enp0s8 -10.X.X.X network).

Clean the `/etc/network/interfaces` file:

```
sudo nano /etc/network/interfaces
```

Set as below:

```
source /etc/network/interfaces.d/*
auto lo
iface lo inet loopback
```

Configure NICs:

**enp0s3 (192.168.1.196/24):**


```
sudo nano /etc/network/interfaces.d/enp0s3
```

Fill as below:

```
auto enp0s3
iface enp0s3 inet static
  address 192.168.1.196/24
  broadcast 192.168.1.255
  network 192.168.1.0
  gateway 192.168.1.1
```

**enp0s8 (10.1.1.196/8):**

```
sudo nano /etc/network/interfaces.d/enp0s8
```

Fill as below:

```
auto enp0s8
iface enp0s8 inet static
  address 10.1.1.196/8
  broadcast 10.255.255.255
  network 10.0.0.0
```


Restart networking (your SSH connection may break; reconnect if needed):

```
sudo systemctl restart networking
```

Enable IP Forwarding:

```
sudo nano /etc/sysctl.conf
```

Add the following line to the end:

```
net.ipv4.ip_forward = 1
```

Activate:

```
sudo sysctl -p
```

Set name server (if not already configured):

```
sudo nano /etc/resolv.conf
```

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

### 2.2. Configuration of the First Host
We have 1 NIC (enp0s3 - 192.168.1.X network).

Clear the `/etc/network/interfaces` file:

```
sudo nano /etc/network/interfaces
```

Set as below:

```
source /etc/network/interfaces.d/*
auto lo
iface lo inet loopback
```

Configure NIC:

**enp0s3 (192.168.1.197/24):**

```
sudo nano /etc/network/interfaces.d/enp0s3
```

```
auto enp0s3
iface enp0s3 inet static
  address 192.168.1.197/24
  broadcast 192.168.1.255
  network 192.168.1.0
  gateway 192.168.1.1
```

Define route:

Create a script file to add the route when the interface comes up:

```
sudo nano /etc/network/if-up.d/routes
```

Fill as below:

```
#!/bin/sh
if [ "$IFACE" = "enp0s3" ]; then
  ip route del 10.0.0.0/8 via 192.168.1.196 dev enp0s3 
  ip route add 10.0.0.0/8 via 192.168.1.196 dev enp0s3 
fi
```

Make the script executable:

```
sudo chmod 750 /etc/network/if-up.d/routes
```

Restart networking (your SSH connection may break; reconnect if needed):

```
sudo systemctl restart networking
```

Set name server (if not already configured):

```
sudo nano /etc/resolv.conf
```

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

### 2.3. Configuration of the Second Host
We have 1 NIC (enp0s3 - 10.X.X.X network).

Clear the `/etc/network/interfaces` file:

```
sudo nano /etc/network/interfaces
```

Set as below:

```
source /etc/network/interfaces.d/*
auto lo
iface lo inet loopback
```

Configure NIC:

**enp0s3 (10.1.1.198/8):**

```
sudo nano /etc/network/interfaces.d/enp0s3
```

```
auto enp0s3
iface enp0s3 inet static
  address 10.1.1.198/8
  broadcast 10.255.255.255
  network 10.0.0.0
  gateway 10.1.1.1
```

Define route:

Create a script file to add the route when the interface comes up:

```
sudo nano /etc/network/if-up.d/routes
```

Fill as below:

```
#!/bin/sh
if [ "$IFACE" = "enp0s3" ]; then
  ip route del 192.168.1.0/24 via 10.1.1.196 dev enp0s3 
  ip route add 192.168.1.0/24 via 10.1.1.196 dev enp0s3 
fi
```

Make the script executable:

```
sudo chmod 750 /etc/network/if-up.d/routes
```

Restart networking (your SSH connection may break; reconnect if needed):

```
sudo systemctl restart networking
```

Set name servers (if not already configured):

```
sudo nano /etc/resolv.conf
```

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

### 2.4. Notes
The host in the first network can ping the host in the other network now, and vice versa.

Try on the first host (192.168.1.197)

```
ping 10.1.1.198
```

Try on the second host (10.1.1.198)

```
ping 192.168.1.197
```

For a host to connect to another host on the other network, routing must be defined on both hosts.

<br>
</details>

<details markdown='1'>
<summary>
3. NIC Bonding
</summary>

---
Network Interface Card (NIC) bonding involves using two or more NICs together to achieve redundancy and/or increased throughput.

The most commonly used bonding modes are:

- **Active Backup:** Also known as failover mode. In this mode, one interface is active while the other interfaces remain in standby mode. If the active interface fails, one of the standby interfaces takes over. It provides redundancy but does not offer load balancing.

- **Balance-rr (Round-Robin):** Packets are transmitted sequentially across the bonded interfaces in a round-robin fashion. This provides load balancing and increased throughput, but does not provide fault tolerance.

- **Balance-xor:** Combines the MAC addresses of the interfaces and applies an XOR operation to determine the outgoing interface. It provides load balancing and fault tolerance, but requires switch support for optimal performance.

- **Broadcast:** All packets are sent on all interfaces. This mode is typically used when the switch does not support other bonding modes. It provides fault tolerance but not load balancing.

All examples below use 2 NICs (enp0s3 and enp0s8) on the same network (192.168.1.X).

### 3.0. Preliminary Steps
Before configuring bonding of any type, there are some necessary preliminary steps.

To use NIC bonding, the `ifenslave` package must be installed:

```
sudo apt update
sudo apt -y install ifenslave
```

Ensure the bonding kernel module is loaded:

```
sudo modprobe bonding
```

Ensure the kernel module loads at startup:

```
sudo nano /etc/modules
```

Add to the end of the file (if it doesn't already exist):

```
bonding
```

Clear the `/etc/network/interfaces` file:

```
sudo nano /etc/network/interfaces
```

Set as below:

```
source /etc/network/interfaces.d/*
auto lo
iface lo inet loopback
```

Set Name Servers (if not already)

```
sudo nano /etc/resolv.conf
```

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```


### 3.1. Active Backup Bonding
Configure the bond:

```
sudo nano /etc/network/interfaces.d/bond
```

Fill as below:

```
auto enp0s3
iface enp0s3 inet manual
    bond-master bond0

auto enp0s8
iface enp0s8 inet manual
    bond-master bond0

auto bond0
iface bond0 inet static
    address 192.168.1.196/24
    netmask 255.255.255.0
    network 192.168.1.0
    gateway 192.168.1.1
    slaves enp0s3 enp0s8
    bond-mode active-backup
    bond-primary enp0s3
```

Restart Networking:

```
sudo systemctl restart networking
```

Check the status of the bond

```
sudo cat /proc/net/bonding/bond0
```

### 3.2. Balance-RR Bonding
Configure the bond

```
sudo nano /etc/network/interfaces.d/bond
```

```
auto enp0s3
iface enp0s3 inet manual
    bond-master bond0

auto enp0s8
iface enp0s8 inet manual
    bond-master bond0

auto bond0
iface bond0 inet static
    address 192.168.1.196/24
    netmask 255.255.255.0
    network 192.168.1.0
    gateway 192.168.1.1
    bond-slaves enp0s3 enp0s8
    bond-mode balance-rr
```

Restart networking:

```
sudo systemctl restart networking
```

Check the status of the bond:

```
sudo cat /proc/net/bonding/bond0
```

### 3.3. Balance-XOR Bonding
Configure the bond

```
sudo nano /etc/network/interfaces.d/bond
```

```
auto enp0s3
iface enp0s3 inet manual
    bond-master bond0

auto enp0s8
iface enp0s8 inet manual
    bond-master bond0

auto bond0
iface bond0 inet static
    address 192.168.1.196/24
    netmask 255.255.255.0
    network 192.168.1.0
    gateway 192.168.1.1
    bond-slaves enp0s3 enp0s8
    bond-mode balance-xor
```

Restart networking:

```
sudo systemctl restart networking
```

Check the status of the bond:

```
sudo cat /proc/net/bonding/bond0
```

### 3.4. Broadcast Bonding
Configure the bond:

```
sudo nano /etc/network/interfaces.d/bond
```

```
auto enp0s3
iface enp0s3 inet manual
    bond-master bond0

auto enp0s8
iface enp0s8 inet manual
    bond-master bond0

auto bond0
iface bond0 inet static
    address 192.168.1.196/24
    netmask 255.255.255.0
    network 192.168.1.0
    gateway 192.168.1.1
    bond-slaves enp0s3 enp0s8
    bond-mode broadcast
```

Restart networking:

```
sudo systemctl restart networking
```

Check the status of the bond:

```
sudo cat /proc/net/bonding/bond0
```

</details>

