##### DNSOnDebianUbuntu 
# Installation and Configuration of DNS Servers on Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>

---
There will be 2 DNS Servers, 1 Primary (Master) and 1 Replica (Slave). 

For every domain on the internet, at least 2 DNS Servers are needed. So if you want to run your own DNS Server, you need at least 2 servers.

If you need DNS Servers for your internal network, it might be a good idea to install a spare one.

I, myself prefer using www.cloudfare.com for DNS services of my domain. But you may prefer running on your servers.

My Specs: (Change the values to your ones)

- Both DNS Servers can be Debian 12/11 or Ubuntu 22.04/20.04 Server
- Domain Name: 386387.xyz (Change it to your domain name)
- Primary DNS Server: ns1.386387.xyz   192.168.1.221
- Replica DNS Server: ns2.386387.xyz   192.168.1.222
- Some sample servers to add as DNS records:
   - filesrv.386387.xyz: 192.168.1.171
   - mail.386387.xyz: 192.168.1.172
   - mailsrv as a canonical name for mail
   - mail as a mail server for the domain
- Google DNS server 8.8.8.8 is used as forwarder DNSs

I tested the tutorial with Debian 11, Debian 12, Ubuntu 20.04 and Ubuntu 22.04 pairs.

Sources:  
[www.linuxtechi.com](https://www.linuxtechi.com/install-configure-bind-9-dns-server-ubuntu-debian/)  
[Mastering Ubuntu Server](https://www.packtpub.com/networking-and-servers/mastering-ubuntu-server-second-edition)  
[https://bind9.readthedocs.io](https://bind9.readthedocs.io)

<br>
</details>

<details markdown='1'>
<summary>
1. Primary DNS Server
</summary>

---
### 1.1. Install bind9 (DNS Server)
```
sudo apt update
sudo apt -y install bind9
```

### 1.2. Edit main config file
```
sudo nano /etc/bind/named.conf.options
```

Change as below

```
options {
   # Cache Directory
   directory "/var/cache/bind";
   # Allow replica to transfer zone files
   allow-transfer { localhost; 192.168.1.222; };
   # Allow queries from any hosts
   allow-query { any; };
   # Use Google DNS as forwarder
   forwarders { 8.8.8.8; };
   # Automatic DNS Security validation
   dnssec-validation auto;
   # Listen on IP4 from all interfaces
   listen-on { any; };
   # Allow recursions
   recursion yes;
};
```

### 1.3. Add a Forward and a Reverse Zone.
```
sudo nano /etc/bind/named.conf.local
```

Fill as below

```
# Forward zone
zone "386387.xyz" IN {
   type master;
   file "/etc/bind/forward.386387.xyz";
};
# Reverse zone
zone "1.168.192.in-addr.arpa" IN {
   type master;
   file "/etc/bind/reverse.386387.xyz";
};
```

### 1.4. Fill the Forward File We Just Defined
```
sudo nano /etc/bind/forward.386387.xyz
```

Fill as below:

```
$TTL 1D
@ IN SOA ns1.386387.xyz hostmaster.386387.xyz (
   2022060501 ; serial
   8H ; Refresh
   4H ; Retry
   4W ; Expire
   1D ; Minimum TTL
)
; Name Server of the domain
@               IN NS     ns1.
; Mail server of the domain
@               IN MX 10  mail.386387.xyz.
; A Records for Hosts
ns1             IN A      192.168.1.221
ns2             IN A      192.168.1.222
filesrv         IN A      192.168.1.171
mail            IN A      192.168.1.172
# CNAME Record
mailsrv         IN CNAME  mail.386387.xyz.
```

### 1.5. Fill the Reverse File We Just Defined
```
sudo nano /etc/bind/reverse.386387.xyz
```

Fill as below

```
$TTL 1D
@    IN   SOA    386387.xyz hostmaster.386387.xyz (
   2022060501 ; Serial
   8H ; Refresh
   4H ; Retry
   4W ; Expire
   1D ; Minimum TTL
)
;Your Name Server Info
@    IN    NS     ns1.386387.xyz.
ns1  IN    A      192.168.1.221
;Reverse Lookup for Your DNS Server
224  IN    PTR    ns1.386387.xyz.
;PTR Records IP address to HostName
225  IN    PTR    ns2.386387.xyz.
171  IN    PTR    filesrv.386387.xyz.
172  IN    PTR    mail.386387.xyz.
```

### 1.6. Check Configuration Files
```
sudo named-checkconf /etc/bind/named.conf.options
sudo named-checkconf /etc/bind/named.conf.local
sudo named-checkzone 386387.xyz /etc/bind/forward.386387.xyz
sudo named-checkzone 386387.xyz /etc/bind/reverse.386387.xyz
```

<br>
</details>

<details markdown='1'>
<summary>
2. Replica DNS Server
</summary>

---
### 2.1. Install bind9 (DNS Server)
```
sudo apt update
sudo apt -y install bind9
```

### 2.2. Edit Main Config File
```
sudo nano /etc/bind/named.conf.options
```

Change as below

```
options {
   # Cache Directory
   directory "/var/cache/bind";
   # Allow queries from any hosts
   allow-query { any; };
   # Use Google DNS as forwarder
   forwarders { 8.8.8.8; };
   # Automatic DNS Security validation
   dnssec-validation auto;
   # Listen on IP4 from all interfaces
   listen-on { any; };
   # Allow recursions
   recursion yes;
};
```

### 2.3. Add the Local Zones
These zones will be replicated from the Primary DNS

```
sudo nano /etc/bind/named.conf.local
```

Fill as below

```
zone "386387.xyz" IN {
   type slave;
   masters { 192.168.1.221; };
   file "/var/lib/bind/forward.386387.xyz";
};
zone "1.168.192.in-addr.arpa" IN {
   type slave;
   masters { 192.168.1.221; };
   file "/var/lib/bind/reverse.386387.xyz";
};
```

This time local zone file is placed at /var/lib and it will be populated automatically

### 2.4. Check Configuration Files
```
sudo named-checkconf /etc/bind/named.conf.options
sudo named-checkconf /etc/bind/named.conf.local
```

<br>
</details>

<details markdown='1'>
<summary>
3. Final Touch
</summary>

---
### 3.1. Restart DNS on both primary and replica
```
sudo systemctl restart bind9
```

Your name servers must be working now. You can query them from any host  in the network with dig command:

```
dig @192.168.1.221 mail.386387.xyz
```

### 3.2. Notes
**Remember**

When you change the zone file on your primary server, remember to increase the number given before serial. 

You can change DNS server settings of your computers (including the DNS Servers) to the new DNS servers.

</details>

