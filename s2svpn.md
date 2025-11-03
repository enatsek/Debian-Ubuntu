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

- **Name:** net1
- **Network:** 192.168.56.0/24
- **Wireguard Server (Debian 13 Server/Ubuntu 24.04 LTS Server):** 
    - **Name:** net1-1
    - **Public IP:** 192.168.1.251
    - **Private IP:** 192.168.56.1
- **Hosts in the network (Linux/Mac/Wind*ws/etc):** 
    - **Name:** net1-2 
    - **Private IP:** 192.168.56.2 


**Site 2**

- **Name:** net2
- **Network:** 192.168.57.0/24
- **Wireguard Server (Debian 13 Server/Ubuntu 24.04 LTS Server):** 
    - **Name:** net2-1
    - **Public IP:** 192.168.1.252
    - **Private IP:** 192.168.57.1
- **Hosts in the network (Linux/Mac/Wind*ws/etc):** 
    - **Name:** net2-2 
    - **Private IP:** 192.168.57.2 

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
Run on **net1-1** and **net2-1**:

```
echo 'net.ipv4.ip_forward=1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p                   # Activate the change
sudo sysctl net.ipv4.ip_forward  # Verify it's set to 1
```

Install wireguard
Run on **net1-1** and **net2-1**:

```
sudo apt update
sudo apt install wireguard -y
```

<br>
</details>

<details markdown="1">
<summary>
2. Generate Key Pairs
</summary>

---

We need to create public/private key pairs for both WireGuard servers.  
Take note of the generated keys, as we will use them in the configuration files.

You can delete or back up the key files after using them in the configurations.  

Run on **net1-1** and **net2-1**:

```
wg genkey | tee privatekey | wg pubkey > publickey
cat privatekey   # Check private key
cat publickey    # Check public key
```

My public and private keys for reference:

- net1-1 Public Key : ```fZjce9XED9g6LN0CJPjpeNueq7mzHFbIc9yIh/c+HVY=```
- net1-1 Private Key: ```8CKa3+nFCemn6ja0RH+soc9lZVzBRiIKjO4UKguYoFk=```
- net2-1 Public Key : ```8ZqdXWlcrJaYgOOrVZI3Aygz90CBnsQa1qtyL4/8LwU=```
- net2-1 Private Key: ```QE3DmQNIX4WePgJskO6oERq2toIqcrSVYRxONq+Fa0A=```

<br>
</details>





<details markdown="1">
<summary>
3. Wireguard Configuration
</summary>

---

### 3.0. Explanations

We need to configure WireGuard on both servers. The IP addresses for the WireGuard tunnel endpoints are chosen as `10.200.0.1/30` (net1-1) and `10.200.0.2/30` (net2-1). These are arbitrary and can be changed if desired.

**`[Interface]` Section**

- **Address:** The IP address assigned to this WireGuard interface in CIDR notation.
- **PrivateKey:** This server's generated private key.
- **ListenPort:** The port number used for the WireGuard tunnel.

**`[Peer]` Section**

- **PublicKey:** The generated public key of the other WireGuard server.
- **Endpoint:** The public IP address and port of the other server.
- **AllowedIPs:** The IP addresses on the remote network that are allowed to be reached through this tunnel.
- **PersistentKeepalive:** Sends an empty packet to the other side at the specified interval (in seconds) to maintain connection state, which is useful for traversing NATs/firewalls (Optional).


### 3.1. First Server Configuration

Create and edit the configuration file.  
Run on **net1-1**:

```
sudo nano /etc/wireguard/wg0.conf
```

Fill it as shown below (remember to replace the variables with your own):

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

Create and edit the configuration file.  
Run on **net2-1**:

```
sudo nano /etc/wireguard/wg0.conf
```

Fill it as shown below (remember to replace the variables with your own):

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

Enable the configuration (to run at startup) and start the tunnel.  
Run on **net1-1** and **net2-1**:

```
sudo systemctl enable wg-quick@wg0
sudo wg-quick up wg0
sudo wg show     # Verify the tunnel status
```

Test connectivity:

Run on **net1-1**:

```
ping 10.200.0.2             # Ping the other end of the VPN tunnel
ping 192.168.57.1           # Ping the other server's private IP
```

Run on net2-1

```
ping 10.200.0.1             # Ping the other end of the VPN tunnel
ping 192.168.56.1           # Ping the other server's private IP
```

If the pings receive replies, the VPN tunnel is established successfully. To enable communication with other hosts on the remote network, we need to add routes.

<br>
</details>



<details markdown="1">
<summary>
4. Adding Routes
</summary>

---

### 4.0. Explanations

**TL;DR:** Consult your network administrator for the best method in your environment.

If you have access to the default gateways (routers) in both networks, you can add the routes there. For net1, traffic to `192.168.57.0/24` should be routed via `192.168.56.1`. For net2, traffic to `192.168.56.0/24` should be routed via `192.168.57.1`.

It is also possible to configure these routes via DHCP, though the specific method is beyond the scope of this tutorial.

Otherwise, you must add the routes manually on each host.

For Windows hosts, it is straightforward. Use an elevated Command Prompt:

```
# Run on net1 hosts
route add -p 192.168.57.0 MASK 255.255.255.0 192.168.56.1
# Run on net2 hosts
route add -p 192.168.56.0 MASK 255.255.255.0 192.168.57.1
```

For Linux hosts, a similar temporary command exists:

```
# Run on net1 hosts
sudo ip route add 192.168.57.0/24 via 192.168.56.1
# Run on net2 hosts
sudo ip route add 192.168.56.0/24 via 192.168.57.1
```

However, this route is not persistent and will be lost after a reboot.

The method for adding persistent routes depends on the Linux distribution and its networking stack. Debian servers typically use `ifupdown`, Ubuntu servers use `netplan`, Red Hat derivatives use `systemd-networkd`, and most desktop editions (including Debian & Ubuntu) use `NetworkManager`.


### 4.1. ifupdown (Debian Server) Configuration

A sample configuration for **net1-2** could be as follows. Edit `/etc/network/interfaces`:

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

Similarly, a sample configuration for **net2-2**:

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

A sample configuration for **net1-2** could be as follows. Edit `/etc/netplan/01-netcfg.yaml`:

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


Similarly, a sample configuration for **net2-2**:

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

You can configure the route through the GUI Network Settings. It is also possible to do via the command line.

First, you need the name of the network connection. The following command will list them:

```
nmcli connection show
```

Add a route for **net1-2**:

```
# Use the appropriate connection name from the command above
sudo nmcli connection modify "Wired connection 1" +ipv4.routes "192.168.57.0/24 192.168.56.1"
```

Add a route for **net2-2**:

```
# Use the appropriate connection name from the command above
sudo nmcli connection modify "Wired connection 1" +ipv4.routes "192.168.56.0/24 192.168.57.1"
```


Apply the configuration:

```
# Use the appropriate connection name from the command above
sudo nmcli connection up "Wired connection 1"
```

<br>
</details>


