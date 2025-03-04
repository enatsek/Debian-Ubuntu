##### KeepalivedOnDebianUbuntu 
# keepalived Clustering on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
- Servers may be Debian 11/12 or Ubuntu 22.04/24.04
- Floating IP Address: 192.168.1.240
- Floating IP address will point to the first server
- SMTP server IP is 192.168.1.150 (optional)

If the first server goes off for any reason, then floating IP address will point to second server. It will return to the first server again when it goes back online.

This looks like clustering only at the network level.

All the necessary services on the first server must be installed on the second server too. (Web server, DB server, mail server etc)

The servers must be in the same network.

Based on the book [Mastering Ubuntu Server 2nd Ed.](https://www.packtpub.com/networking-and-servers/mastering-ubuntu-server-second-edition) by Jay LaCroix. 

I tested the tutorial with Debian 11, Debian 12, Ubuntu 22.04 and Ubuntu 24.04 pairs.


You may establish a full cluster of LAMP stack by:

1. Installing Apache on both servers
2. Configuring the apache and sites equally on the both server
3. Installing MariaDB on both server
4. Establishing Master-Master Replication for Mariadb on 1st and 2nd servers

<br>
</details>

<details markdown='1'>
<summary>
1. Install keepalived
</summary>

---
Install on both the first and the second servers

```
sudo apt update
sudo apt -y install keepalived
```

After the installation, tries to start but cannot because there is no config.

<br>
</details>

<details markdown='1'>
<summary>
2. First Server Config
</summary>

---
### 2.1. Config
Config file location is /etc/keepalived directory, initially empty

Create primary server conf file

```
sudo nano /etc/keepalived/keepalived.conf
```

Fill as below:

```
global_defs {
	notification_email {
	notify@x11.xyz
	}
	notification_email_from keepalived@x11.xyz
	smtp_server 192.168.1.150
	smtp_connect_timeout 30
	router_id mycompany_web_prod
}
vrrp_instance VI_1 {
	smtp_alert
	interface enp0s3
	virtual_router_id 51
	priority 100
	advert_int 5
	virtual_ipaddress {
	192.168.1.240
	}
}
```

### 2.2. Explanations
- global_defs
   - notification_email
      - email address to notify of cluster changes
      - replace notify@x11.xyz with your email
   - notification_email_from keepalived@x11.xyz
      - from address on the email, change as you wish
   - smtp_server
      - smtp server to send the mail through
   - smtp_connect_timeout
      - 30 seconds would be enough
   - router_id
      - Any value to distinguish
- vrrp_instance
   - interface xxxxx
      - the network interface to run keepalived
   - virtual_router_id xx
      - keepalived clusterid (0-255)
      - must be the same on all the cluster members
   - priority xx
      - must be different on each cluster member
      - highest will be master member of the cluster
   - virtual_ip_address
      - floating ip address of the cluster


</details>

<details markdown='1'>
<summary>
3. Second Server Config
</summary>

---
Almost the same as step 2. Just give a smaller number (say 90) for priority.

If you want to add more servers, give them numbers less then 90

<br>
</details>

<details markdown='1'>
<summary>
4. Start keepalived
</summary>

---
Run on both servers

```
sudo systemctl start keepalived
```

You can check the status of your cluster

```
systemctl status -l keepalived
```

</details>

