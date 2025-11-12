##### DNS (BIND9)
# Installation and Configuration of DNS Servers on Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.0. The What

A DNS (Domain Name System) server translates human-readable domain names into numerical IP addresses, allowing users to access websites using easy-to-remember names instead of complex numbers. It acts like a phonebook for the internet, directing traffic to the correct locations.

This tutorial describes how to install and configure authoritative DNS servers for a domain on Debian and Ubuntu servers.

### 0.1. Notes

This setup will include 2 DNS Servers: 1 **Primary (Master)** and 1 **Replica (Slave)**.

For redundancy and reliability, every domain on the internet should have at least 2 DNS servers. Therefore, if you want to run your own DNS service, you need at least two servers.

For internal networks, it is also a good practice to install a secondary DNS server for redundancy.

While I personally prefer using services like [Cloudflare](https://www.cloudflare.com/dns/) for my domains due to their global network and DDoS protection, you may have reasons to run your own servers.

### 0.2. The Environment

**Example Specifications (Replace with your own values):**

- **Server OS:** Debian 13/12 or Ubuntu 24.04/22.04 Server (for both DNS servers)
- **Domain Name:** `386387.xyz`
- **Primary DNS Server:** `ns1.386387.xyz` at `192.168.1.201`
- **Replica DNS Server:** `ns2.386387.xyz` at `192.168.1.202`
- **Sample Host Records:**
   - `filesrv.386387.xyz`: `192.168.1.171`
   - `mail.386387.xyz`: `192.168.1.172`
   - `mailsrv.386387.xyz` (CNAME for `mail.386387.xyz`)
   - MX record pointing to `mail.386387.xyz`
- **DNS Forwarder:** Google's public DNS (`8.8.8.8`)

This tutorial has been tested with various combinations including Debian 12/13 and Ubuntu 22.04/24.04.

### 0.3. Sources  
- [www.linuxtechi.com](https://www.linuxtechi.com/install-configure-bind-9-dns-server-ubuntu-debian/)
- [Mastering Ubuntu Server](https://www.packtpub.com/networking-and-servers/mastering-ubuntu-server-second-edition)
- [https://bind9.readthedocs.io](https://bind9.readthedocs.io)

<br>
</details>

<details markdown='1'>
<summary>
1. Primary DNS Server Configuration
</summary>

---

Install BIND9 (the DNS server software):

```
sudo apt update
sudo apt -y install bind9
```

Edit the main configuration file to set global options:

```
sudo nano /etc/bind/named.conf.options
```

Modify the `options` block as follows:

```
options {
   # Cache Directory
   directory "/var/cache/bind";
   # Allow replica to transfer zone files
   allow-transfer { localhost; 192.168.1.202; };
   # Allow queries from any hosts
   allow-query { any; };
   # Use Google DNS as forwarder
   forwarders { 8.8.8.8; };
   # Automatic DNS Security validation
   dnssec-validation auto;
   # Listen on IP4 from all interfaces
   listen-on { any; };
   # Allow recursive queries
   recursion yes;
};
```

Define the forward and reverse zones by editing the local configuration file:

```
sudo nano /etc/bind/named.conf.local
```

Fill as below

```
// Forward zone
zone "386387.xyz" IN {
   type master;
   file "/etc/bind/forward.386387.xyz";
};

// Reverse zone
zone "1.168.192.in-addr.arpa" IN {
   type master;
   file "/etc/bind/reverse.386387.xyz";
};
```


Create and populate the forward zone file:

```
sudo nano /etc/bind/forward.386387.xyz
```

Add the following content:

```
$TTL 1D
@ IN SOA ns1.386387.xyz. hostmaster.386387.xyz. (
   2025111001 ; serial
   8H         ; refresh
   4H         ; retry
   4W         ; expire
   1D         ; minimum TTL
)

; Name Servers for the domain
@               IN      NS      ns1.386387.xyz.
@               IN      NS      ns2.386387.xyz.

; Mail Exchange record
@               IN      MX 10   mail.386387.xyz.

; A Records for Hosts
ns1             IN      A       192.168.1.201
ns2             IN      A       192.168.1.202
filesrv         IN      A       192.168.1.171
mail            IN      A       192.168.1.172

; CNAME Record (Alias)
mailsrv         IN      CNAME   mail.386387.xyz.
```


Create and populate the reverse zone file:

```
sudo nano /etc/bind/reverse.386387.xyz
```

Add the following content:

```
$TTL 1D
@    IN   SOA    ns1.386387.xyz. hostmaster.386387.xyz. (
   2025111001 ; Serial
   8H         ; Refresh
   4H         ; Retry
   4W         ; Expire
   1D         ; Minimum TTL
)

; Name Servers
@    IN    NS     ns1.386387.xyz.
@    IN    NS     ns2.386387.xyz.
ns1  IN    A      192.168.1.201
ns2  IN    A      192.168.1.202

; PTR Records (IP address to HostName)
201  IN    PTR    ns1.386387.xyz.
202  IN    PTR    ns2.386387.xyz.
171  IN    PTR    filesrv.386387.xyz.
172  IN    PTR    mail.386387.xyz.
```

Validate all configuration files for syntax errors:

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
2. Replica DNS Server Configuration
</summary>

---

Install BIND9 on the replica server:

```
sudo apt update
sudo apt -y install bind9
```

Edit the main configuration file:

```
sudo nano /etc/bind/named.conf.options
```

Use the same configuration as the primary server, but without the `allow-transfer` directive:

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
   # Allow recursive queries
   recursion yes;
};
```

Configure the replica zones to sync from the primary server:

```
sudo nano /etc/bind/named.conf.local
```

Fill as below

```
zone "386387.xyz" IN {
   type slave;
   masters { 192.168.1.201; };
   file "/var/lib/bind/forward.386387.xyz";
};
zone "1.168.192.in-addr.arpa" IN {
   type slave;
   masters { 192.168.1.201; };
   file "/var/lib/bind/reverse.386387.xyz";
};
```

Note that the zone files are located in `/var/lib/bind/` and will be automatically populated via zone transfers from the primary server.

Validate the configuration files:

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
### 3.1. Start the DNS Services

Restart BIND9 on both servers to apply the configuration:

```
sudo systemctl restart bind9
```

### 3.2. Test the DNS Servers

Your name servers should now be operational. You can test them using the `dig` command from any host on the network:

Test forward lookup (hostname to IP):
```
dig @192.168.1.201 mail.386387.xyz
dig @192.168.1.202 filesrv.386387.xyz
```

Test reverse lookup (IP to hostname):
```
dig @192.168.1.201 -x 192.168.1.171
dig @192.168.1.202 -x 192.168.1.172
```

Test zone transfer (should only work from replica to primary):
```
dig @192.168.1.201 386387.xyz AXFR
```


### 3.3. Important Notes

**Zone File Updates:**
- When you modify a zone file on the primary server, you **must** increment the **serial number** (the first number in the SOA record) for changes to propagate to the replica server.
- A common format is `YYYYMMDDNN` (e.g., `2025111001` for the first change on Nov 10, 2025).

**Client Configuration:**
- To use your new DNS servers, update the DNS settings on your client machines to point to `192.168.1.201` and `192.168.1.202`.
- You can also configure the DNS servers themselves to use each other as primary resolvers by editing `/etc/resolv.conf`.


</details>

