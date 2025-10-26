##### Site-to-site VPN
# Site-to-site VPN Tutorial using wireguard for Debian and Ubuntu

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What

A Site-to-site VPN is a secure connection that links two or more separate networks over the internet, such as connecting a main office network to a branch office network. Think of it as creating a private, encrypted tunnel through the public internet. This allows employees at different physical locations to securely share resources and access shared files, printers, and applications as if they were all on the same local network.

It's different from the VPN you might use on your personal computer, which typically only connects a single device. A Site-to-site VPN connects entire networks to each other, automatically protecting all the data that travels between them without requiring individual users to turn anything on.

### 0.1. Environment

**Site 1**

- Name: net1
- Network: 192.168.56.0/24
- wireguard server (Debian 13 Server/Ubuntu 24.04 LTS Server): 
    - name: net1-1
    - Public IP: 192.168.1.251
    - Private IP: 192.168.56.1
- Hosts in the network (Linux/Mac/Wind*ws/etc): 
    - name: net1-2 Private IP: 192.168.56.2 


**Site 2**

- Name: net2
- Network: 192.168.57.0/24
- wireguard server (Debian 13 Server/Ubuntu 24.04 LTS Server): 
    - name: net2-1
    - Public IP: 192.168.1.252
    - Private IP: 192.168.57.1
- Hosts in the network (Linux/Mac/Wind*ws/etc): 
    - name: net2-2 Private IP: 192.168.57.2 

### 0.2. Sources

- [Deepseek](https://www.deepseek.com/)   
- [ChatGPT](https://chatgpt.com/)   
- [Claude](https://claude.ai/)  
- [Wireguard Documentation](https://www.wireguard.com/)


<br>
</details>

<details markdown="1">
<summary>
1. Pre-Config and Wireguard Installation
</summary>

---

Enable IP Forwarding on both wireguard servers
Run on net1-1 and net2-1

```
echo 'net.ipv4.ip_forward=1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p    # Activate it
sudo sysctl net.ipv4.ip_forward  # Check it
```

Install wireguard
Run on net1-1 and net2-1

```
sudo apt update
sudo apt install wireguard -y
```

<br>
</details>

<details markdown="1">
<summary>
2. Generate Keypairs
</summary>

---

We need to create public/private keypairs for both wireguard servers.  
While installing take notes of them, we're going to use them on configuration files.

You can delete or backup them after using in configurations
Run on net1-1 and net2-1

```
wg genkey | tee privatekey | wg pubkey > publickey
cat privatekey   # Check private key
cat publickey    # Check public key
```

My public and private keys for reference:

net1-1 Public Key : ```fZjce9XED9g6LN0CJPjpeNueq7mzHFbIc9yIh/c+HVY=```  
net1-1 Private Key: ```8CKa3+nFCemn6ja0RH+soc9lZVzBRiIKjO4UKguYoFk=```  
net2-1 Public Key : ```8ZqdXWlcrJaYgOOrVZI3Aygz90CBnsQa1qtyL4/8LwU=```  
net2-2 Private Key: ```QE3DmQNIX4WePgJskO6oERq2toIqcrSVYRxONq+Fa0A=```

<br>
</details>





<details markdown="1">
<summary>
3. Wireguard Configuration
</summary>

---

### 3.0. Explanations

We need to configure wireguard on both servers. The IP addresses for wireguard endpoints are choosen as 10.200.0.1/30 (net1-1) and 10.200.0.2/30 (net2-1). They are arbitrary, you can change them if you want.

The keys and their explanations at the config file are as follows:

**Interface Section**

Address: Given IP address to wireguard in CIDR notation.  
PrivateKey: Produced Private Key of the server.  
ListenPort: The port number used for wireguard tunnel.  

**Peer Section**

PublicKey: Produced Public Key of the other wireguard server.  
Endpoint: IP:Port of the other server.  
AllowedIPs: IP addresses at the other network who can reach to this network.  
PersistentKeepalive: Send an empty packet to the other side every given second to keepalive the connection (Optional).  


### 3.1. First Server Configuration

We will create a configuration file and fill it as in the template.

Run on net1-1

```
sudo nano /etc/wireguard/wg0.conf
```

Fill as below (Remember changing variables as yours):

```
[Interface]
Address = 10.200.0.1/30
PrivateKey = 8CKa3+nFCemn6ja0RH+soc9lZVzBRiIKjO4UKguYoFk=
ListenPort = 51820

[Peer]
PublicKey = 8ZqdXWlcrJaYgOOrVZI3Aygz90CBnsQa1qtyL4/8LwU=
Endpoint = 192.168.1.252:51820
AllowedIPs = 10.200.0.2/32, 192.168.57.0/24
PersistentKeepalive = 25

```

### 3.2. Second Server Configuration

We will create a configuration file and fill it as in the template.

Run on net2-1

```
sudo nano /etc/wireguard/wg0.conf
```

Fill as below (Remember changing variables as yours):

```
[Interface]
Address = 10.200.0.2/30
PrivateKey = QE3DmQNIX4WePgJskO6oERq2toIqcrSVYRxONq+Fa0A=
ListenPort = 51820

[Peer]
PublicKey = fZjce9XED9g6LN0CJPjpeNueq7mzHFbIc9yIh/c+HVY=
Endpoint = 192.168.1.251:51820
AllowedIPs = 10.200.0.1/32, 192.168.56.0/24
PersistentKeepalive = 25
```

### 3.3. Enable and Start the Wireguard Tunnel

Enable our configuration (make it run at start-up) and start it.

Run on net1-1 and net2-1

```
sudo systemctl enable wg-quick@wg0
sudo wg-quick up wg0
sudo wg show     # Verify the tunnel
```

Test connectivity:

Run on net1-1

```
ping 10.200.0.2             # Ping other side of the VPN tunnel
ping 192.168.57.1           # Ping the other server's Private IP
```

Run on net2-1

```
ping 10.200.0.1             # Ping other side of the VPN tunnel
ping 192.168.56.1           # Ping the other server's Private IP
```

If the pings return the replies, it means the VPN tunnel is established. For connecting to the other hosts, we need to add routes to access to other network.

<br>
</details>



<details markdown="1">
<summary>
4. Adding Routes
</summary>

---

### 4.0. Explanations

TL;DR: Ask your network administrator.

If you have access to default gateways (routers) in the networks, you can add the routes there.  
For net1, 192.168.57.0/24 will be routed by 192.168.56.1. For net2, 192.168.56.0/24 will be routed by 192.168.57.1. 

If you are using DHCP, it is possible to add there. I really don't know how, but I know it is somehow possible.

Otherwise, you have to add it manually.

For windows hosts it is the easiest: 

```
route add -p 192.168.57.0 MASK 255.255.255.0 192.168.56.1   # For net1 hosts
route add -p 192.168.56.0 MASK 255.255.255.0 192.168.57.1   # For net2 hosts
```

For Linux hosts, there is a similar way:

```
sudo route add 192.168.57.0/24 via 192.168.56.1       # For net1 hosts
sudo route add 192.168.56.0/24 via 192.168.57.1       # For net2 hosts
```

But it is not persistent. Goes away when you reboot the host.

Method of adding persistent routes depends on the Linux distro and its networking stack. Debian servers use ifupdown, Ubuntu servers use netplan, Red-Hat servers (and derivatives) use systemd-networkd, most of the Desktop editions (including Debian & Ubuntu) use NetworkManager. 


### 4.1. ifupdown (Debian Server) Configuration

A sample configuration for net1-2 could be as below:

```
# /etc/network/interfaces
auto lo
iface lo inet loopback

# Primary interface
auto enp0s3
iface enp0s3 inet static
    address 192.168.56.2
    netmask 255.255.255.0
    gateway 192.168.56.101
    dns-nameservers 8.8.8.8 1.1.1.1
    
    # Secondary route to 192.168.57.0/24
    post-up ip route add 192.168.57.0/24 via 192.168.56.1
    post-down ip route del 192.168.57.0/24 via 192.168.56.1
```

Similarly a sample configuration for net2-2 could be as below:

```
# /etc/network/interfaces
auto lo
iface lo inet loopback

# Primary interface
auto enp0s3
iface enp0s3 inet static
    address 192.168.57.2
    netmask 255.255.255.0
    gateway 192.168.57.101
    dns-nameservers 8.8.8.8 1.1.1.1
    
    # Secondary route to 192.168.56.0/24
    post-up ip route add 192.168.56.0/24 via 192.168.57.1
    post-down ip route del 192.168.56.0/24 via 192.168.57.1
```

To apply the configuration:

```
sudo systemctl restart networking
```
or

```
sudo ifdown enp0s3 && sudo ifup enp0s3
```


### 4.2. netplan (Ubuntu Server) Configuration

A sample configuration for net1-2 could be as below:

```
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp0s3:
      addresses:
        - 192.168.56.2/24
      gateway4: 192.168.56.101
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
      routes:
      - to: 192.168.57.0/24
        via: 192.168.56.1
```


Similarly a sample configuration for net2-2 could be as below:

```
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp0s3:
      addresses:
        - 192.168.57.2/24
      gateway4: 192.168.57.101
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
      routes:
      - to: 192.168.56.0/24
        via: 192.168.57.1

```


To apply the configuration:

```
sudo netplan apply
```

### 4.3. NetworkManager (Debian & Ubuntu Desktop)

You can configure the route through Network Settings. But it is possible to perform it through terminal.

First you need the name of the network connection. For Debian desktop It is most probably "Wired connection 1", for Ubuntu desktop it is something like "netplan-enp0s3". The following command will give you a clue:

```
nmcli connection show
```

Add route for net1-2:

```
sudo nmcli connection modify "Wired connection 1" +ipv4.routes "192.168.57.0/24 192.168.56.1"
```

or

```
sudo nmcli connection modify "netplan-enp0s3" +ipv4.routes "192.168.57.0/24 192.168.56.1"
```

Add route for net2-2:

```
sudo nmcli connection modify "Wired connection 1" +ipv4.routes "192.168.56.0/24 192.168.57.1"
```

or

```
sudo nmcli connection modify "netplan-enp0s3" +ipv4.routes "192.168.56.0/24 192.168.57.1"
```



Apply the configuration:

```
sudo nmcli connection up "Wired connection 1"
```

or

```
sudo nmcli connection up "netplan-enp0s3"
```

<br>
</details>


