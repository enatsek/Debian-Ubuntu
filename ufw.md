##### UFW (Uncomplicated Firewall)
# Basic UFW Tutorial for Ubuntu and Debian

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.1. The What

UFW (Uncomplicated Firewall), is a user-friendly command-line tool designed to simplify firewall management on Linux systems, particularly Ubuntu. It provides a straightforward way to configure firewall rules without requiring in-depth knowledge of iptables or nftables.

This is a basic UFW tutorial covering enabling/disabling, adding and deleting rules, syntax, and other fundamental operations.


### 0.2. Environment

Prepared for and tested on Debian 13/12 and Ubuntu 24.04/22.04 LTS Server.

### 0.3. Sources:

- [www.netfilter.org](https://www.netfilter.org/)
- [www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04)
- [www.digitalocean.com](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
- [help.ubuntu.com](https://help.ubuntu.com/community/UFW)
- [manpages.ubuntu.com](https://manpages.ubuntu.com/manpages/jammy/en/man8/ufw.8.html)

<br>
</details>

<details markdown='1'>
<summary>
1. Firewall Architecture 
</summary>

---

### 1.1. Netfilter

Netfilter is a set of hooks for network packets integrated into the Linux kernel. It provides a framework for packet filtering, NAT (Network Address Translation), and port translation.

This represents the deepest layer of Linux firewall functionality.

### 1.2. Nftables and Iptables

Nftables is the successor to iptables and serves as the second layer of Linux firewalls. It can be considered a generic firewall system that allows administrators to define rulesets based on network packets.

While nftables (or iptables on older distributions) can be used directly for firewall configuration, their complexity has led distributions to provide higher-level tools for easier management.

### 1.3. Ufw

UFW is the higher-level firewall program provided by Ubuntu (Canonical). Other distributions offer similar tools (such as firewalld and firewall-cmd from Red Hat).

<br>
</details>

<details markdown='1'>
<summary>
2. UFW Basics
</summary>

---

### 2.1. Installation

UFW is installed by default on Ubuntu Server (though initially inactive). On Debian, install it with:

```
sudo apt update
sudo apt install ufw --yes
```

### 2.2. Status

Check UFW's current status (should be inactive initially):

```
sudo ufw status
```

For more detailed information:

```
sudo ufw status verbose
```

### 2.3. Enabling/Disabling

UFW is disabled by default.

**Important:** When you enable UFW, all incoming traffic is denied while all outgoing traffic is allowed. If you enable it while connected via SSH without first allowing SSH traffic, you may lose your connection.

First, allow SSH:

```
sudo ufw allow ssh
```

Now enable UFW:

```
sudo ufw enable
```

To disable UFW:

```
sudo ufw disable
```

To clear all rules and disable UFW:

```
sudo ufw reset
```

Enable or disable logging:

```
sudo ufw logging on
sudo ufw logging off
```
 
### 2.4. Basic Rule Management

Rule addition can be done using simple or complex syntax. Both of the following commands achieve the same result: allowing incoming HTTP traffic.

```
sudo ufw allow 80
sudo ufw allow in proto tcp from any to any port 80
```

Remove a rule for port 80:

```
sudo ufw delete allow 80
```

List rules with numbers for easy reference:

```
sudo ufw status numbered
```

Delete a rule by its number:

```
sudo ufw delete 2
```

Show all added rules:

```
sudo ufw show added
```

Display rules in raw format:

```
sudo ufw show raw
```

<br>
</details>


<details markdown='1'>
<summary>
3. Allowing and Denying in Detail
</summary>

---
### 3.1. Long Format

```
sudo ufw allow in on enp0s3 proto tcp from any to any port 22
```

- **`allow`**: Could be `allow` or `deny`.
- **`in`**: Specifies incoming traffic; could be `in` or `out`.
- **`on`**: (Optional) Specifies the network interface.
- **`enp0s3`**: Network interface name; used with `on`.
- **`proto`**: (Optional) Specifies the protocol (TCP or UDP).
- **`tcp`**: Used with `proto`; could be `tcp` or `udp`.
- **`from`**: Specifies the source address.
- **`any`**: Means all IPs; could be an IP address or network range.
- **`to`**: Specifies the destination address.
- **`port`**: Specifies the port number.
- **`22`**: Port number; can be any valid port.

### 3.2. Short Forms and Some Examples

Most parameters from the long format can be omitted for simplicity.

**Examples:**

Allow or deny traffic from a specific IP:

```
sudo ufw deny from 192.168.1.11
sudo ufw allow from 192.168.1.11
```

Allow or deny traffic from a network:

```
sudo ufw allow from 192.168.0.0/24
sudo ufw deny from 192.168.0.0/24
```

Allow or deny incoming UDP packets on port 53 (DNS):

```
sudo ufw allow 53/udp
sudo ufw deny 53/udp
```

Allow all incoming HTTP and HTTPS (TCP):

```
sudo ufw allow proto tcp from any to any port 80,443
```

Allow access to MySQL from a specific IP:

```
sudo ufw allow from 192.168.1.11 to any port 3306
```

Allow access to PostgreSQL from a network:

```
sudo ufw allow from 192.168.1.0/24 to any port 5432
```

Block outgoing SMTP traffic:

```
sudo ufw deny out 25
```

Allow a range of ports:

```
sudo ufw allow 6000:6007/tcp
sudo ufw allow 6000:6007/udp
```

Allow incoming HTTP on a specific interface:

```
sudo ufw allow in on enp0s3 to any port 80
```

### 3.3. Rule Order

Rules are processed from top to bottom. When a matching rule is found, subsequent rules are skipped.

By default, new rules are appended to the bottom. To insert a rule at a specific position (e.g., at the top):

```
sudo ufw insert 1 deny from 192.168.1.0/24 to any
```

UFW can use service names instead of port numbers (read from `/etc/services`):

```
sudo ufw allow ssh
```

<br>
</details>

<details markdown='1'>
<summary>
4. Case Study 1
</summary>

---

### 4.0. Scenario

- Allow SSH for only one IP: `192.168.1.108`.
- Allow MariaDB for network `192.168.1.0/24`, except for IP `192.168.1.231`.
- Allow HTTP and HTTPS for everyone.
- Deny outgoing SMTP (port 25/TCP).
- Add an additional MariaDB exception for IP `192.168.1.232`.

### 4.1. Always Allow SSH First

Reset all previous configurations and disable UFW (Restart):

```
sudo ufw reset
```

Allow incoming SSH (port 22/TCP) from `192.168.1.108`:

```
sudo ufw allow in proto tcp from 192.168.1.108 to any port 22
```

Enable UFW:

```
sudo ufw enable
```

**Note:** After enabling, only SSH from the specified IP is allowed. Proceed to add the remaining rules.

### 4.2. Add MariaDB Rules

Add the MariaDB deny exception (must come before the allow rule):

```
sudo ufw deny in proto tcp from 192.168.1.231 to any port 3306
```

Allow MariaDB for the network:

```
sudo ufw allow in proto tcp from 192.168.1.0/24 to any port 3306
```

### 4.3. Add HTTP(S) Rules

Allow HTTP and HTTPS for all:

```
sudo ufw allow in proto tcp from any to any port 80
sudo ufw allow in proto tcp from any to any port 443
```

### 4.4. Outgoing SMTP

Block outgoing SMTP traffic:

```
sudo ufw deny out proto tcp from any to any port 25
```

### 4.5. Additional MariaDB Exception

Add another MariaDB exception for IP `192.168.1.232`.

First, check the current rules:

```
sudo ufw status numbered
```

```
Status: active
     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    192.168.1.108             
[ 2] 3306/tcp                   DENY IN     192.168.1.231             
[ 3] 3306/tcp                   ALLOW IN    192.168.1.0/24            
[ 4] 80/tcp                     ALLOW IN    Anywhere                  
[ 5] 443/tcp                    ALLOW IN    Anywhere                  
[ 6] 25/tcp                     DENY OUT    Anywhere                   (out)
[ 7] 80/tcp (v6)                ALLOW IN    Anywhere (v6)             
[ 8] 443/tcp (v6)               ALLOW IN    Anywhere (v6)             
[ 9] 25/tcp (v6)                DENY OUT    Anywhere (v6)              (out)
```

If we add the new rule with the default command:

```
sudo ufw deny in proto tcp from 192.168.1.232 to any port 3306
```

Verify the updated rules:

```
sudo ufw status numbered
```

Output:

```
Status: active
     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    192.168.1.108             
[ 2] 3306/tcp                   DENY IN     192.168.1.231             
[ 3] 3306/tcp                   ALLOW IN    192.168.1.0/24            
[ 4] 80/tcp                     ALLOW IN    Anywhere                  
[ 5] 443/tcp                    ALLOW IN    Anywhere                  
[ 6] 25/tcp                     DENY OUT    Anywhere                   (out)
[ 7] 3306/tcp                   DENY IN     192.168.1.232             
[ 8] 80/tcp (v6)                ALLOW IN    Anywhere (v6)             
[ 9] 443/tcp (v6)               ALLOW IN    Anywhere (v6)             
[10] 25/tcp (v6)                DENY OUT    Anywhere (v6)              (out)
```

It will be appended at the end (position 7 for IPv4), after the allow rule, making it ineffective because rule 3 will already permit the traffic.

Delete the useless rule:

```
sudo ufw delete 7
```

Insert the new rule at position 3 (before the network allow rule):

```
sudo ufw insert 3 deny in proto tcp from 192.168.1.232 to any port 3306
```

Verify the updated rules:

```
sudo ufw status numbered
```

Output:

```
Status: active
     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    192.168.1.108             
[ 2] 3306/tcp                   DENY IN     192.168.1.231             
[ 3] 3306/tcp                   DENY IN     192.168.1.232             
[ 4] 3306/tcp                   ALLOW IN    192.168.1.0/24            
[ 5] 80/tcp                     ALLOW IN    Anywhere                  
[ 6] 443/tcp                    ALLOW IN    Anywhere                  
[ 7] 25/tcp                     DENY OUT    Anywhere                   (out)
[ 8] 80/tcp (v6)                ALLOW IN    Anywhere (v6)             
[ 9] 443/tcp (v6)               ALLOW IN    Anywhere (v6)             
[10] 25/tcp (v6)                DENY OUT    Anywhere (v6)              (out)
```

<br>
</details>

<details markdown='1'>
<summary>
5. Case Study 2
</summary>

---

### 5.0. Scenario

- Two network interfaces: `enp0s3` and `enp0s8`.
- Allow SSH from IP `192.168.1.108` on interface `enp0s3`.
- Allow SSH from any IP on interface `enp0s8`.
- Allow HTTP and HTTPS from any IP on interface `enp0s3`.

### 5.1. First SSH Rule

Reset all previous configurations and disable UFW (Restart):

```
sudo ufw reset
```

Allow SSH from `192.168.1.108` on interface `enp0s3`:

```
sudo ufw allow in on enp0s3 proto tcp from 192.168.1.108 to any port 22
```

Enable UFW:

```
sudo ufw enable
```

### 5.2. Second SSH Rule

Allow SSH from any IP on interface `enp0s8`:

```
sudo ufw allow in on enp0s8 proto tcp from any to any port 22
```

### 5.3. HTTP(S) Rules

Allow HTTP and HTTPS from any IP on interface `enp0s3`:

```
sudo ufw allow in on enp0s3 proto tcp from any to any port 80
sudo ufw allow in on enp0s3 proto tcp from any to any port 443
```

View the configured rules:

```
sudo ufw status numbered
```

Output:

```
Status: active
     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp on enp0s3           ALLOW IN    192.168.1.108             
[ 2] 22/tcp on enp0s8           ALLOW IN    Anywhere                  
[ 3] 80/tcp on enp0s3           ALLOW IN    Anywhere                  
[ 4] 443/tcp on enp0s3          ALLOW IN    Anywhere                  
[ 5] 22/tcp (v6) on enp0s8      ALLOW IN    Anywhere (v6)             
[ 6] 80/tcp (v6) on enp0s3      ALLOW IN    Anywhere (v6)             
[ 7] 443/tcp (v6) on enp0s3     ALLOW IN    Anywhere (v6)                 
```

</details>

