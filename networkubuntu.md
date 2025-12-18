##### Network On Ubuntu 
# Network Configuration On Ubuntu Server
</details>

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. Info
Network configuration examples on Ubuntu 22.04 LTS and 24.04 LTS Servers.

Tried to be as thorough as possible: single NIC, multiple NICs, multiple networks.

Debian and Ubuntu network configurations are very different, so there are separate tutorials for Debian and Ubuntu.

### 0.1. Configuration Files
Ubuntu 22.04 and 24.04 LTS Servers use Systemd-Networkd and Netplan for network configuration.

Configuration files reside as YAML files in the `/etc/netplan` directory. A good practice is to have one configuration file there.

This configuration file contains all network configurations, including name servers.

### 0.2. Sources
- [netplan.io](https://netplan.io/)
- [netplan.readthedocs.io](https://netplan.readthedocs.io/en/stable/)
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
sudo nano /etc/netplan/50-cloud-init.yaml
```

Fill as below:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: true
```

```
sudo netplan apply
```

### 1.2. Static IP Configuration
Our NIC is enp0s3.

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Fill as below:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 192.168.1.221/24
      nameservers:
        search:
          - "x386.org"
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      routes:
        - to: default
          via: 192.168.1.1
```

```
sudo netplan apply
```

### 1.3. Static IP Configuration with 2 IPs
Our NIC is enp0s3.

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Fill as below:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 192.168.1.221/24
        - 10.1.1.1/8
      nameservers:
        search:
          - "x386.org"
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      routes:
        - to: default
          via: 192.168.1.1
```

```
sudo netplan apply
```

### 1.4. Static IP Configuration with 2 NICs
Our NICs are enp0s3 and enp0s8.

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Fill as below:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 192.168.1.221/24
      nameservers:
        search:
          - "x386.org"
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      routes:
        - to: default
          via: 192.168.1.1
    enp0s8:
      addresses:
        - 10.1.1.1/8
```

```
sudo netplan apply
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

Our router will have 2 NICs: one with IP 192.168.1.216 and the other with IP 10.1.1.216.

Hosts in the 192.168.1.X network will use 192.168.1.216 to reach the 10.X.X.X network. Hosts in the 10.X.X.X network will use 10.1.1.216 to reach the 192.168.1.X network.

We will configure:

- The router (192.168.1.216 & 10.1.1.216)
- The host in the first network (192.168.1.217)
- The host in the second network (10.1.1.218)

Then we'll check connectivity between them.

### 2.1. Configuration of the Router
e have 2 NICs (enp0s3 - 192.168.1.X network, and enp0s8 - 10.X.X.X network).

Configure NICs:
- enp0s3: 192.168.1.216/24
- enp0s8: 10.1.1.216/8

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Fill as below:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 192.168.1.216/24
      nameservers:
        search:
          - "x386.org"
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      routes:
        - to: default
          via: 192.168.1.1
    enp0s8:
      addresses:
        - 10.1.1.216/8
```

Restart networking (your SSH connection may break; reconnect if needed):

```
sudo netplan apply
```

Enable IP forwarding:

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

### 2.2. Configuration of the First Host
We have 1 NIC (enp0s3 - 192.168.1.X network).

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Fill as below:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 192.168.1.217/24
      nameservers:
        search:
          - "x386.org"
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      routes:
        - to: default
          via: 192.168.1.1
        - to: 10.0.0.0/8
          via: 192.168.1.216
```

Restart networking (your SSH connection may break; reconnect if needed):

```
sudo netplan apply
```

### 2.3. Configuration of the Second Host
We have 1 NIC (enp0s3 - 192.168.1.X network).

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Fill as below:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 10.1.1.218/8
      nameservers:
        search:
          - "x386.org"
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      routes:
        - to: default
          via: 10.1.1.1
        - to: 192.168.1.0/24
          via: 10.1.1.216
```

Restart networking (your SSH connection may break; reconnect if needed):

```
sudo netplan apply
```

### 2.4. Notes
The host in the first network can ping the host in the other network now, and vice versa.

Try on the first host (192.168.1.217)

```
ping 10.1.1.218
```

Try on the second host (10.1.1.218)

```
ping 192.168.1.217
```

For a host to connect to another host on the other network, routing must be defined on both hosts.

<br>
</details>

<details markdown='1'>
<summary>
3. NIC Bonding
</summary>

---
I tried NIC bonding on Ubuntu, but unfortunately I wasn't successful.

This might be because of VirtualBox, Netplan, or Networkd. So I gave up. Maybe next time.

I was able to create the bond interface, and it got an IP address too, but it could not connect to anywhere on the network. Even working with Networkd directly didn't help.

</summary>

