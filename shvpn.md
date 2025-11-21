##### Self Hosted VPN Server
# VPN Server Configuration Tutorial using Wireguard for Debian and Ubuntu

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What

A VPN server for personal computers acts as a secure, private gateway between your device and the internet. When you connect to it using VPN software, it creates an encrypted tunnel that protects all your online activity. This process hides your real IP address, making it appear as if you are browsing from the server's location, which helps with privacy and accessing region-locked content. 

Essentially, it provides a safe and private connection for a single user, even when using public Wi-Fi networks.

### 0.1. Environment

- Server: 
    - IP: 192.227.167.142
    - OS: Debian 13 Server or Ubuntu 24.04 LTS Server
    - nic: eth0
- Client1: Debian 13 / Ubuntu 24.04 Desktop & Server, Linux Mint
- Client2: Windows 11
- Client3: Android


### 0.2. WireGuard Concepts

- WireGuard does not use a strict client-server model. In practice, all WireGuard nodes can act as servers and connect to each other in a peer-to-peer fashion.

- In our configuration, the central WireGuard server will connect to many clients, and each client will only connect to this central server.

- Connections can be initiated from either side. However, in our specific scenario, connections will always be initiated from the clients.

- Every host in a WireGuard network must have a public key and a private key. This key pair allows peers to identify and authorize each other.

### 0.3. Configuration Templates

Our central WireGuard server will use the following configuration template. You will need to replace the placeholder values with your server's private key and the clients' public keys. These keys are generated after installing WireGuard. Also, ensure you specify the correct name of your server's network interface (e.g., eth0) in the "NAT for clients" section.

Server Configuration (/etc/wireguard/wg0.conf):

```
[Interface]
Address = 10.100.0.100/24
ListenPort = 53
PrivateKey = serverprivkey

# NAT for clients
PostUp = iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
# Client 1
PublicKey = client1pubkey
AllowedIPs = 10.100.0.1/32

[Peer]
# Client 2
PublicKey = client2pubkey
AllowedIPs = 10.100.0.2/32

[Peer]
# Client 3
PublicKey = client3pubkey
AllowedIPs = 10.100.0.3/32

[Peer]
# Client 4
PublicKey = client4pubkey
AllowedIPs = 10.100.0.4/32
```

Notes on the server configuration:

- The network 10.100.0.0/24 is arbitrarily chosen for the WireGuard tunnel. You can use any private IP range, though 10.x.x.x is often a good choice.

- Port 53 is selected for WireGuard. It is the same port used for DNS, which may help obfuscate VPN traffic from ISPs that attempt to block it.

- We need to assign a unique IP address (e.g., 10.100.0.1, 10.100.0.2, ...) and a public/private key pair for the server and every client.



Our WireGuard clients will use the following configuration templates. Remember to replace the placeholders with the server's public key and each client's respective private key.


```
# Client1
[Interface]
PrivateKey = client1privkey
Address = 10.100.0.1/32
DNS = 1.1.1.1

[Peer]
PublicKey = serverpubkey
Endpoint = serverpublicip:53
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```

```
# Client2
[Interface]
PrivateKey = client2privkey
Address = 10.100.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = serverpubkey
Endpoint = serverpublicip:53
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```

```
# Client3
[Interface]
PrivateKey = client3privkey
Address = 10.100.0.3/32
DNS = 1.1.1.1

[Peer]
PublicKey = serverpubkey
Endpoint = serverpublicip:53
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```

Notes on the client configuration:

- Each client must have its own configuration file with a unique IP address and key pair.

- Specifying a DNS address (like 1.1.1.1) is necessary because your ISP's DNS might not resolve certain domain names correctly when the tunnel is active.

- The PersistentKeepalive option sends an empty packet every 25 seconds to maintain a connection state through NATs and firewalls.

### 0.4. Sources

- [Deepseek](https://www.deepseek.com/)   
- [ChatGPT](https://chatgpt.com/)   
- [Claude](https://claude.ai/)  
- [Wireguard Documentation](https://www.wireguard.com/)


<br>
</details>

<details markdown="1">
<summary>
1. Server Configuration
</summary>

---

Enable IP Forwarding

The VPN server needs to forward traffic between its physical network interface and the WireGuard tunnel.

```
echo 'net.ipv4.ip_forward=1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p                    # Apply the change
sudo sysctl net.ipv4.ip_forward   # Verify it's set to 1
```

Free Port 53 (Ubuntu Systems)

On Ubuntu, port 53 is often used by the systemd-resolved service. We need to free it or choose a different port for WireGuard. To free port 53, edit the systemd-resolved configuration:


```
sudo nano /etc/systemd/resolved.conf
```

Find the line (around line 19) that says:

```
#DNSStubListener=yes
```

Change it to:

```
DNSStubListener=no
```

Save the file and restart the service:

```
sudo systemctl restart systemd-resolved
```


Install WireGuard and iptables

We need iptables to configure NAT, which allows clients to access the internet through the server.

```
sudo apt update
sudo apt install -y wireguard iptables
```

Generate Key Pairs

Create a directory for the keys and generate the key pairs for the server and clients.

```
mkdir wg && cd wg
wg genkey | tee serverprivkey | wg pubkey > serverpubkey
wg genkey | tee client1privkey | wg pubkey > client1pubkey
wg genkey | tee client2privkey | wg pubkey > client2pubkey
wg genkey | tee client3privkey | wg pubkey > client3pubkey
```

For reference, the generated keys in this example are:

Server: 

- Privkey: ```kAy+LgQ3EkJtTKyB1N0BnbXGZVJE/pX6SH2yCG2l1lI=```
- Pubkey:  ```OCtqLy2OkpuiBPhmXR0DbhbaVDhpuS4AVDm3yZDP1XU=```

Client1:

- Privkey: ```SJPFU+D5Eoa3cSseIjWNh44dUQfyyFYxw0m4qGRSrFc=``` 
- Pubkey:  ```KgjPrrOPamV81q76C0Cql2fU1K7sSiigqYXVlwkKyBA=```

Client2:

- Privkey: ```gCJE0PoqARqSnQgq1v87v7QcSzUn97d0abVM7BpqjFc=```
-  Pubkey: ```ZfZtUviU/jUAxEcIEXnf2d6rW0RcBFg+1Wt4kNnpTxg=```

Client3:

- Privkey: ```gLoXU+1aNQmcK/OtjSUJGnOXt28w/mRo1szjU+XO/XM=```
- Pubkey:  ```IG/wUYUGSDuZI0+DZsE6lq1OLNzx8aNIp8SUjllAwj8=```


Create and Activate the WireGuard Configuration

Create the WireGuard configuration file:

```
sudo nano /etc/wireguard/wg0.conf
```

Populate the file with the configuration below. Remember to use your actual server private key and client public keys. Also, verify your network interface name (e.g., eth0). You can add as many client ```[Peer]``` sections as needed.

```
[Interface]
Address = 10.100.0.100/24
ListenPort = 53
PrivateKey = kAy+LgQ3EkJtTKyB1N0BnbXGZVJE/pX6SH2yCG2l1lI=

# NAT for clients
PostUp = iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
# Client 1
PublicKey = KgjPrrOPamV81q76C0Cql2fU1K7sSiigqYXVlwkKyBA=
AllowedIPs = 10.100.0.1/32

[Peer]
# Client 2
PublicKey = ZfZtUviU/jUAxEcIEXnf2d6rW0RcBFg+1Wt4kNnpTxg=
AllowedIPs = 10.100.0.2/32

[Peer]
# Client 3
PublicKey = IG/wUYUGSDuZI0+DZsE6lq1OLNzx8aNIp8SUjllAwj8=
AllowedIPs = 10.100.0.3/32
```


Enable, start, verify the service.


```
sudo systemctl enable wg-quick@wg0
sudo systemctl start wg-quick@wg0
sudo wg show     # Verify the tunnel status and peers
```

<br>
</details>

<details markdown="1">
<summary>
2. Debian / Ubuntu & Derivatives Client Configuration
</summary>

---


This configuration should work on all Debian-based and Ubuntu-based systems, including Mint and MX Linux. It has been tested on Debian 13, Ubuntu 24.04, and Linux Mint 22.2.

Install WireGuard and resolvconf. The resolvconf package is needed to manage DNS settings for the WireGuard interface.

```
sudo apt update
sudo apt install -y wireguard resolvconf
```


Create the client configuration file:

```
sudo nano /etc/wireguard/wg0.conf
```


Populate the file with the configuration below, using the correct private key for this client, the server's public key, and the server's public IP address.


```
[Interface]
PrivateKey = SJPFU+D5Eoa3cSseIjWNh44dUQfyyFYxw0m4qGRSrFc=
Address = 10.100.0.1/32
DNS = 1.1.1.1

[Peer]
PublicKey = OCtqLy2OkpuiBPhmXR0DbhbaVDhpuS4AVDm3yZDP1XU=
Endpoint = 192.227.167.142:53
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```

Start the WireGuard tunnel and verify its status:

```
sudo wg-quick up wg0
sudo wg show     # Verify the tunnel
```

Ping the server's tunnel IP:

```
ping 10.100.0.100
```

Check your public IP address (it should match your server's IP)

```
curl https://ip.x386.org
```

If the displayed IP is your server's IP (in my case, 192.227.167.142), you are successfully routing your internet traffic through the WireGuard server.

To deactivate the VPN temporarily:

```
sudo wg-quick down wg0
```

To activate the VPN automatically at startup:

```
sudo systemctl enable wg-quick@wg0
```


<br>
</details>

<details markdown="1">
<summary>
3. Windows Client Configuration
</summary>

---

**Tested on Windows 11.**

Create a configuration file named wg0.conf and save it to a convenient location.

The file contents should be as follows. Remember to substitute the correct private key for this client, the server's public key, and the server's public IP address.


```
[Interface]
PrivateKey = gCJE0PoqARqSnQgq1v87v7QcSzUn97d0abVM7BpqjFc=
Address = 10.100.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = OCtqLy2OkpuiBPhmXR0DbhbaVDhpuS4AVDm3yZDP1XU=
Endpoint = 192.227.167.142:53
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```


Download and run the Windows installer from [Wireguard Install](https://www.wireguard.com/install/).

After installation, the WireGuard application will run. Click "Add Tunnel" at the bottom left and select "Import tunnel(s) from file." Choose the wg0.conf file you created. To activate the VPN, click the "Activate" button. To deactivate it, click "Deactivate."

<br>
</details>

<details markdown="1">
<summary>
4. Android Client Configuration
</summary>

---

Tested on my Samsung devices.

Create a configuration file named wg0.conf and transfer it to your Android device (e.g., via email, cloud storage, or a direct transfer).

The file contents should be as follows. Remember to substitute the correct private key for this client, the server's public key, and the server's public IP address.


```
[Interface]
PrivateKey = gLoXU+1aNQmcK/OtjSUJGnOXt28w/mRo1szjU+XO/XM=
Address = 10.100.0.3/32
DNS = 1.1.1.1

[Peer]
PublicKey = OCtqLy2OkpuiBPhmXR0DbhbaVDhpuS4AVDm3yZDP1XU=
Endpoint = 192.227.167.142:53
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```

Install the WireGuard app from the Google Play Store: <https://play.google.com/store/apps/details?id=com.wireguard.android&hl=en-US&pli=1>.

Open the WireGuard app, tap the "+" button, and select "Import from file or archive." Select your wg0.conf file. Once imported, tap the "Activate" switch to start the VPN connection.

<br>
</details>

<details markdown="1">
<summary>
5. Other Clients
</summary>

---

The process is similar for other operating systems like macOS and iOS. Download the official WireGuard application, import the configuration file (which has the same structure), and activate the tunnel.


<br>
</details>

<details markdown="1">
<summary>
6. Case Study - Configuring for 1,000 Clients
</summary>

---

As a case study, we will configure a server for 1,000 clients. We will use scripts to generate the key pairs, server configuration, and client configurations. You can modify these scripts for different numbers of clients.

Create and enter a temporary working directory:

```
mkdir /tmp/wg
cd /tmp/wg
```

### 6.1. Creating Keypairs

We will create 1,001 key pairs (one for the server and 1,000 for clients). Create the script:

```
nano keys.sh
```

Fill it with the following content. To create 10,000 key pairs, for example, you would change the first for loop to ```for i in {1..40}```.

```
#!/bin/bash
# Create wireguard public/private key pairs for the server and 1000 client
# Keys will be put on keys directory
# Server keys are named as serverprivkey and serverpubkey
# Client keys are named as 1-1privkey to 1-250privkey, 1-1pubkey to 1-250pubkey
# It goes for 2- 3- 4- and makes total 1,000 keypairs for clients
#
# So if you want to make 10.000 key pairs, change the first for line as:
# for i in {1..40}

mkdir -p keys
wg genkey | tee keys/serverprivkey | wg pubkey > keys/serverpubkey
for i in {1..4} 
do
  for j in {1..250}
  do
    wg genkey | tee keys/"$i"-"$j"privkey | wg pubkey > keys/"$i"-"$j"pubkey
  done
done
```

Make the script executable and run it:

```
chmod +x keys.sh
./keys.sh
```

The keys are now in the /tmp/wg/keys directory.

### 6.2. Creating Server Configuration

Create a script to generate the server configuration with 1,000 peers.

```
nano serverconf.sh
```

Fill it with the following content. This script uses the 10.100.0.0/16 network, which supports approximately 65,000 clients.

```
#!/bin/bash
# Create wireguard server configuration for 1,000 clients.
# Configuration is named as wg0.conf and put in conf directory
# You can directly put the conf file into /etc/wireguard directory
#
# 10.100.0.0/16 network is reserved for clients, that makes a total of 
#   about 65.000 client

mkdir -p confs
echo > confs/wg0.conf

echo '[Interface]' >> confs/wg0.conf
echo Address = 10.100.0.1/16 >> confs/wg0.conf
echo ListenPort = 53 >> confs/wg0.conf
echo PrivateKey = `cat keys/serverprivkey` >> confs/wg0.conf
echo >> confs/wg0.conf
echo "#" NAT for clients >> confs/wg0.conf
echo PostUp = iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE >> confs/wg0.conf
echo PostDown = iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE >> confs/wg0.conf

#!/bin/bash
for i in {1..4}
do
  for j in {1..250}
  do 
    echo >> confs/wg0.conf
    echo '[Peer]' >> confs/wg0.conf
    echo "#" Client "$i"-"$j" >> confs/wg0.conf
    echo PublicKey = `cat keys/"$i"-"$j"pubkey` >> confs/wg0.conf
    echo AllowedIPs = 10.100."$i"."$j"/32 >> confs/wg0.conf
  done
done
```

Make the script executable and run it:

```
chmod +x serverconf.sh
./serverconf.sh
```

The configuration file wg0.conf is now in the /tmp/wg/confs directory and can be copied to /etc/wireguard/ on the server.


### 6.3. Creating Client Configurations

Create a script to generate the 1,000 client configuration files.

```
nano clientconfs.sh
```

Fill it with the following content. Remember to set the serverip variable to your server's public IP address.

```
#!/bin/bash
# Create 1,000 wireguard client configurations.
# Configurations are put in confs directory and named as wg1-1.conf to 
#    wg1-250.conf.
# It goes for 2- 3- 4- and makes total 1,000 configurations for clients
# You can distribute the configurations to the clients as you wish.
# You have to edit serverip and change it to your wireguard servers.


serverip=192.227.167.142 # REPLACE WITH YOUR SERVER'S PUBLIC IP
for i in {1..4}
do
  for j in {1..250}
  do
    echo '[Interface]' > confs/wg"$i"-"$j".conf
    echo PrivateKey = `cat keys/"$i"-"$j"privkey` >> confs/wg"$i"-"$j".conf
    echo Address = 10.100."$i"."$j"/16 >> confs/wg"$i"-"$j".conf
    echo DNS = 1.1.1.1 >> confs/wg"$i"-"$j".conf
    echo >> confs/wg"$i"-"$j".conf
    echo '[Peer]' >> confs/wg"$i"-"$j".conf
    echo PublicKey = `cat keys/serverpubkey` >> confs/wg"$i"-"$j".conf
    echo Endpoint = "$serverip":53  >> confs/wg"$i"-"$j".conf
    echo AllowedIPs = 0.0.0.0/0, ::/0  >> confs/wg"$i"-"$j".conf
    echo PersistentKeepalive = 25  >> confs/wg"$i"-"$j".conf
  done
done
```

Make the script executable and run it:

```
chmod +x clientconfs.sh
./clientconfs.sh
```

The client configuration files are now in the /tmp/wg/confs directory and can be distributed to users.

### 6.4. Backup Backup

Do not forget to back up your key pairs and configuration files securely!


<br>
</details>


