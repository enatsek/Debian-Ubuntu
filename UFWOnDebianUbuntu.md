##### UFWOnDebianOnUbuntu
# Basic UFW (Uncomplicated Firewall) Tutorial On Ubuntu and Debian

<details markdown='1'>
<summary>
0. Specs
</summary>
---
Basic UFW (Uncomplicated Firewall) tutorial. Enabling, adding, deleting  rules, syntax etc.

Prepared for Debian 12/11 and Ubuntu 24.04/22.04 LTS Server

Sources:  
[www.netfilter.org](https://www.netfilter.org/)  
[www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04)  
[www.digitalocean.com](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)  
[help.ubuntu.com](https://help.ubuntu.com/community/UFW)  
[manpages.ubuntu.com](https://manpages.ubuntu.com/manpages/jammy/en/man8/ufw.8.html)  

<br>
</details>

<details markdown='1'>
<summary>
1. Firewall Architecture 
</summary>
---
### 1.1. Netfilter
Netfilter represents a set of hooks for network packets, it is integrated into the Linux kernel. It supplies a framework for packet filtering, NAT, and port translation.

It is the first (deepest) layer for Linux firewalls.

### 1.2. Nftables and Iptables
Nftables, which is the successor of Iptables, is the second layer of  Linux firewalls. It can be considered as a generic firewall. It allows  defining rulesets based on network packets.

We can use nftables (or iptables, at the older Linux distros) to supply firewall functionality, but because it is very complex; linux distros supply higher level firewall tools for easy manipulation.

### 1.3. Ufw
Ufw is the higher level firewall program supplied by Ubuntu (Canonical). Other distros can supply other higher level firewalls (like firewalld and  firewall-cmd from Red Hat).

<br>
</details>

<details markdown='1'>
<summary>
2. Ufw Basics
</summary>
---
### 2.1. Installation
ufw is installed and inactive by default on Ubuntu server. For Debian :

```
sudo apt update
sudo apt install ufw --yes
```

### 2.2. Status
Check ufw status (must be inactive)

```
sudo ufw status
```

in verbose mode:

```
sudo ufw status verbose
```

### 2.3. Enabling/Disabling
ufw is disabled by default. 

When you enable ufw, all incoming traffic is denied, and all outgoing  traffic is allowed.

So if you enable it while connected with ssh it may break your  connection. That means you have to allow ssh before enabling it.

Add ssh for everyone

```
sudo ufw allow ssh
```

Now we can enable it:

```
sudo ufw enable
```

Disable ufw

```
sudo ufw disable
```

Clear all rules and disable ufw

```
sudo ufw reset
```

Enable/disable logging

```
sudo ufw logging on
sudo ufw logging off
```
 
### 2.4. Simple Manipulation
Rule addition can be simple or complex

Both following commands are basically do the same thing and enables incoming HTTP.

```
sudo ufw allow 80
sudo ufw allow in proto tcp from any to any port 80
```

Remove added port 80

```
sudo ufw delete allow 80
```

List rules as numbered

```
sudo ufw status numbered
```

Rules can be deleted by referencing its number

```
sudo ufw delete 2
```

Show added rules

```
sudo ufw show added
```

Show in raw format

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

- **allow:** could be allow or deny
- **in:** could be in or out, specifies incoming or outgoing traffic
- **on:** if we want to specify the network interface card
- **enp0s3:** network interface card name, used with on
- **proto:** if we want to specify TCP or UDP protocol 
- **tcp:** used with proto, could be tcp or udp
- **from:** used to specify from address 
- **any:** means all IPs, could be IP address or network
- **to:** used to specify to address
- **port:** used to specify port number
- **22:** port number, could be any port number

### 3.2. Short Forms and Some Examples
Most of (if not all) the parameters can be omitted from the long format.

Some examples:

Allow/deny from an IP

```
sudo ufw deny from 192.168.1.11
sudo ufw allow from 192.168.1.11
```

Allow/deny from a network

```
sudo ufw allow from 192.168.0.0/24
sudo ufw deny from 192.168.0.0/24
```

Allow/deny incoming udp packets on port 53 

```
sudo ufw allow 53/udp
sudo ufw deny 53/udp
```

Allow all incoming HTTP and HTTPS (TCP)

```
sudo ufw allow proto tcp from any to any port 80,443
```

Allow from one IP to MySQL

```
sudo ufw allow from 192.168.1.11 to any port 3306
```

Allow from a network to Postgres

```
sudo ufw allow from 192.168.1.0/24 to any port 5432
```

Block outgoing SMTP

```
sudo ufw deny out 25
```

Allow a port range

```
sudo ufw allow 6000:6007/tcp
sudo ufw allow 6000:6007/udp
```

Allow incoming HTTP for an interface

```
sudo ufw allow in on enp0s3 to any port 80
```

### 3.3. Rule Order
Rules are processed from the top to the bottom. When an applicable rule  is is found, the remaining rules are skipped.

When you add a new rule, it is added to the bottom. 

Inserting a rule to the top

```
sudo ufw insert 1 deny from 192.168.1.0/24 to any
```

We can use service name instead of a port number. ufw reads services from /etc/services file.

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
### 4.0. Specs
- Allow SSH for 1 IP - 192.168.1.108
- Allow MariaDB for 1 network except 1 IP - 192.168.1.0/24 - 192.168.1.231
- Allow HTTP, HTTPS for everyone 
- Deny outgoing SMTP - Port 25 TCP
- Add one more IP for deny MariaDB exception  - 192.168.1.232

### 4.1. Always Add SSH First 
Allow incoming SSH (Port 22/TCP) from 192.168.1.108

```
sudo ufw allow in proto tcp from 192.168.1.108 to any port 22
```

Enable ufw

```
sudo ufw enable
```

Now we enabled our firewall, it only allows ssh, we're going to add the  other rules.

### 4.2. Add Mariadb Rules
Add MariaDB deny exception, it has to be before MariaDB allowing

```
sudo ufw deny in proto tcp from 192.168.1.231 to any port 3306
```

Add Mariadb allow network

```
sudo ufw allow in proto tcp from 192.168.1.0/24 to any port 3306
```

### 4.3. Add HTTP(S) Rules
Add allow HTTP and HTTPS

```
sudo ufw allow in proto tcp from any to any port 80
sudo ufw allow in proto tcp from any to any port 443
```

### 4.4. Outgoing SMTP
Deny outgoing SMTP

```
sudo ufw deny out proto tcp from any to any port 25
```

### 4.5. Additional Mariadb Exception
Add one more deny exception for Mariadb


Before going on let's see our rules

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

As you can see, rules are added to the end as you add them. First come  the TCP/IP version 4 rules, then come the version 6 rules. 

If we add another rule with the following command, rule list will be like 
the following:

```
sudo ufw deny in proto tcp from 192.168.1.232 to any port 3306
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
[ 7] 3306/tcp                   DENY IN     192.168.1.232             
[ 8] 80/tcp (v6)                ALLOW IN    Anywhere (v6)             
[ 9] 443/tcp (v6)               ALLOW IN    Anywhere (v6)             
[10] 25/tcp (v6)                DENY OUT    Anywhere (v6)              (out)
```

Because the rules are processed in order, our new rule (number 7) will  never be reached, because the rule number 3 will allow the connection.

Delete our useless new rule

```
sudo ufw delete 7
```

Now we insert our new rule to the 3rd place

```
sudo ufw insert 3 deny in proto tcp from 192.168.1.232 to any port 3306
```

Now our new rule is at the right place:

```
sudo ufw status numbered
```

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
### 5.0. Specs
- Two network interfaces - enp0s3 and enp0s8
- Allow SSH for 1 IP on interface 1 - port 22/TCP 192.168.1.108
- Allow SSH for all on interface 2 - port 22
- Allow HTTP, HTTPS for all on interface 1 - ports 80 and 443/TCP
 
### 5.1. First SSH Rule
Allow SSH for 1 IP for the 1st network interface enp0s3

```
sudo ufw allow in on enp0s3 proto tcp from 192.168.1.108 to any port 22
```

Enable ufw

```
sudo ufw enable
```

### 5.2. Second SSH Rule
Allow SSH for all for the 2nd network interface enp0s8

```
sudo ufw allow in on enp0s8 proto tcp from any to any port 22
```

### 5.3. HTTP(S) Rules
Allow HTTP and HTTPS for all for the 1st network interface enp0s3

```
sudo ufw allow in on enp0s3 proto tcp from any to any port 80
sudo ufw allow in on enp0s3 proto tcp from any to any port 443
```

See the rules

```
sudo ufw status numbered
```

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

