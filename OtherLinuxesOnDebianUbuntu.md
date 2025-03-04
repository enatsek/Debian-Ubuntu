##### OtherLinuxesOnDebianUbuntu  
# Other Linuxes for Debian and Ubuntu Admins

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. Information
Although my tutorials (and my learning curve) contain Debian and Ubuntu Linux distributions; Time to time, an admin may need to handle other Linuxes too. 

In this tutorial, my aim is to help with other linuxes,  namely Red Hat, Alpine and Devuan. 

In the previous versions, I used to include OpenSuse too; but I decided that I cannot concentrate on it anymore.

Main subjects are:

- Package Management
- Network Configuration
- Installing LAMP Stack
- Service Management

Main Distributions:

- Debian 12 and 11
- Ubuntu 24.04 and 22.04 LTS
- RHEL (Centos, Alma, Rocky) 9.x, 8.x
- Alpine 3.17, 3.18, 3.19
- Devuan 4, 5

### 0.2. Resources:
[access.redhat.com](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9)  
[wiki.alpinelinux.org](https://wiki.alpinelinux.org/wiki/Main_Page)  
[wiki.debian.org](https://wiki.debian.org/)  
[www.geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-retrieve-data-from-mysql-database-using-php/)  

<br>
</details>

<details markdown='1'>
<summary>
1. Debian 12 & 11
</summary>

---
### 1.1. Package Management
Commands require root or sudo.

#### 1.1.1. Update Cache
```
apt update
```
#### 1.1.2. Upgrade Packages
```
apt upgrade
```

#### 1.1.3. Install a Package
```
apt install apache2
```

#### 1.1.4. Remove a Package
```
apt remove apache2
```

#### 1.1.5. Search a Package
```
apt search apache2
```

#### 1.1.6. Clean Unused Packages
```
apt autoremove
```

#### 1.1.7. Show Package Info
```
apt show apache2
```

### 1.2. Network Configuration
#### 1.2.1. Get the name of the network adapter
The name of the network adapter will be something like enp0s3, but we  need the exact name. 

The following command lists the network interface name(s). The one in en* format should be the name of your network adapter.

```
ls /sys/class/net
```

In any case you cannot get the name, you can try to following command:

```
ip a
```

#### 1.2.2. IP configuration. 
```
sudo nano /etc/network/interfaces
```

I assume that your network adapter name is enp0s3, otherwise change it.

Fill the file like below (change to your IP addresses)

```
auto enp0s3
iface enp0s3 inet static
address 192.168.0.3/24
broadcast 192.168.0.255
network 192.168.0.0
gateway 192.168.0.1
```

If you want to use DHCP, fill the file as below

```
auto enp0s3
iface enp0s3 inet dhcp
```

#### 1.2.3. DNS Addresses
```
sudo nano /etc/resolv.conf
```

Add your DNS addresses as below

```
nameserver 46.196.235.35
nameserver 178.233.140.110
nameserver 46.197.15.60
```

#### 1.2.4. Restart Network Adapter
Assuming your network adapter name is enp0s3

```
sudo ifdown enp0s3 && sudo ifup enp0s3
```

or

```
sudo systemctl restart networking.service
```

If you are connecting through SSH, your connection would break up. You  need to connect with the new IP again.

### 1.3. Installing LAMP Stack
#### 1.3.1. Install packages
```
sudo apt update
sudo apt install --yes apache2 mariadb-server php \
   libapache2-mod-php php-mysql
```

This is all we need actually. But if you are like me, that is you have to see it to believe it; you are going to want to test it. So let's test it.

#### 1.3.2. Test LAMP
We'll create a test database on Mariadb, we'll create a table in that  database, add some rows to the table. We will also create a test PHP file  with the PHP code to retrieve the data from the database and display it as HTML. That way we'll be able to test the PHP-Mariadb and PHP-Apache  connections.

```
sudo mariadb
```
Create mysampledb database, connect to it, create a table, fill the  table, create a user with the access permission to that database and the  table.

Run on Mariadb shell:

```
CREATE DATABASE mysampledb;
USE mysampledb;
CREATE TABLE Employees (Name char(15), Age int(3), Occupation char(15));
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
INSERT INTO Employees VALUES ('John Doe', '33', 'Sleeper');
INSERT INTO Employees VALUES ('Mariadb Server', '14', 'RDBM');
GRANT ALL ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
exit
```

Create test PHP

```
sudo nano /var/www/html/test.php
```

Fill it as below

```
<?php
   $mycon = new mysqli("localhost", "appuser", "password", "mysampledb");
   if ($mycon->connect_errno)
   {
      echo "Connection Error";
      exit();
   }
   $mysql = "SELECT * FROM Employees";
   $result = ($mycon->query($mysql));
   $rows = [];
   if ($result->num_rows > 0)
    {
        $rows = $result->fetch_all(MYSQLI_ASSOC);
    }
?>
<!DOCTYPE html>
<html>
<body>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>Occupation</th>
            </tr>
        </thead>
        <tbody>
            <?php
               if(!empty($rows))
               foreach($rows as $row)
              {
            ?>
            <tr>
                <td><?php echo $row['Name']; ?></td>
                <td><?php echo $row['Age']; ?></td>
                <td><?php echo $row['Occupation']; ?></td>
            </tr>
            <?php } ?>
        </tbody>
    </table>
</body>
</html>
<?php
    mysqli_close($conn);
?>
```

Now, from your workstation's browser, load the page (replace srv with  your server's IP: 

http:/srv/test.php

You can use the same steps for testing LAMP stack on other distros too.

### 1.4. Service Management
Conventionally, when a package with a service is installed on Debian, it  is enabled and started by default.

#### 1.4.1. Status of a Service
```
systemctl status apache2
```
 
#### 1.4.2. Start/Stop a Service
```
sudo systemctl stop apache2
sudo systemctl start apache2
```

To force to stop

```
sudo systemctl kill apache2
```

#### 1.4.3. Reload a Service
Reads configuration file again

```
sudo systemctl reload apache2
```

#### 1.4.4. Restart a Service
Stops and Starts

```
sudo systemctl restart apache2
```

#### 1.4.5. Enable/Disable a Service
```
sudo systemctl enable apache2
sudo systemctl disable apache2
```

<br>
</details>

<details markdown='1'>
<summary>
2. Ubuntu 24.04 LTS & 22.04 LTS
</summary>

---
### 2.1. Package Management
Commands require root or sudo.

#### 2.1.1. Update Cache
```
apt update
```

#### 2.1.2. Upgrade Packages
```
apt upgrade
```

#### 2.1.3. Install a Package
```
apt install apache2
```

#### 2.1.4. Remove a Package
```
apt remove apache2
```

#### 2.1.5. Search a Package
```
apt search apache2
```

#### 2.1.6. Clean Unused Packages
```
apt autoremove
```

#### 2.1.7. Show Package Info
```
apt show apache2
```
 
## 2.2. Network Configuration
#### 2.2.1. Get the name of the network adapter
The name of the network adapter will be something like enp0s3, but we  need the exact name. 

The following command lists the network interface name(s). The one in en* format should be the name of your network adapter.

```
ls /sys/class/net
```

In any case you cannot get the name, you can try to following command:

```
ip a
```

#### 2.2.2. Network configuration. 
By default Ubuntu uses netplan for network configuration.

```
sudo nano /etc/netplan/00-installer-config.yaml
```

The file name might be different, in that case, use that file.

I assume that your network adapter name is enp0s3, otherwise change it.

Fill the file like below (change to your IP addresses)

```
network:
  ethernets:
    enp0s3:
      addresses:
      - 192.168.1.182/24
      routes:
      - to: default
        via: 192.168.1.1
      nameservers:
        addresses:
        - 8.8.8.8
        - 192.168.1.1
        search:
        - x11.xyz
  version: 2
```

#### 2.2.3. Restart Netplan
```
sudo netplan apply
```

If you are connecting through SSH, your connection would break up. You  need to connect with the new IP again.


### 2.3. Installing LAMP Stack
#### 2.3.1. Install packages
```
sudo apt update
sudo apt install --yes apache2 mariadb-server php \
    libapache2-mod-php php-mysql
```

#### 2.3.2. Test LAMP
You can use the test scenario at 1.3.2 to test RHEL LAMP stack.

### 2.4. Service Management
As Ubuntu being a derivative of Debian, when a package with a service is  installed, it is enabled and started by default.

#### 2.4.1. Status of a Service
```
systemctl status apache2
```

#### 2.4.2. Start/Stop a Service
```
sudo systemctl stop apache2
sudo systemctl start apache2
```

To force to stop

```
sudo systemctl kill apache2
```

#### 2.4.3. Reload a Service
Reads configuration file again

```
sudo systemctl reload apache2
```

#### 2.4.4. Restart a Service
Stops and Starts

```
sudo systemctl restart apache2
```

#### 2.4.5. Enable/Disable a Service
```
sudo systemctl enable apache2
sudo systemctl disable apache2
```

<br>
</details>

<details markdown='1'>
<summary>
3. RHEL (Centos, Alma, Rocky) 9.x, 8.x
</summary>

---
Centos (upto 8.x version), Alma and Rocky Linux are compatible  with Red Hat. That is, they are same other than brandings and names. So if something works in RHEL, it works in Centos, Alma, and Rocky too.

RHEL gives free licenses for testing purposes, I have 2 VMs running for testing purposes (versions 8.x and 9.x).

### 3.1. Package Management
Commands require root or sudo.

#### 3.1.1. Update Cache
```
dnf check-update   
```

It is always called when installing or updating packages.  
So it is not necessary

#### 3.1.2. Upgrade Packages
```
dnf upgrade
```

#### 3.1.3. Install a Package
```
dnf install httd
```

#### 3.1.4. Remove a Package
```
dnf remove httpd
```

#### 3.1.5. Search a Package
```
dnf search httpd
```

#### 3.1.6. Clean Unused Packages
```
dnf autoremove
```

#### 3.1.7. Show Package Info
```
dnf info httpd
```
 
### 3.2. Network Configuration
#### 3.2.1. Get the name of the network adapter
The name of the network adapter will be something like enp0s3, but we  need the exact name. 

The following command lists the network interface name(s). The one in en* format should be the name of your network adapter.

```
ls /sys/class/net
```

In any case you cannot get the name, you can try to following command:

```
ip a
```

#### 3.2.2. IP and DNS configuration. 
I assume that your network adapter name is enp0s3, otherwise change it.

Change IP and Gateway, change DNS

```
sudo nmcli con modify 'enp0s3' ifname enp0s3 ipv4.method manual \
   ipv4.addresses 192.168.0.210/24 gw4 192.168.0.1
sudo nmcli con modify 'enp0s3' ipv4.dns 8.8.8.8
```

#### 3.2.3. Restart Network Adapter
```
sudo nmcli con down 'enp0s3' && sudo nmcli con up 'enp0s3'
```

### 3.3. Installing LAMP Stack
As you might expect package names are different in RHEL (e.g. httpd  instead of apache2).

#### 3.3.1. Install packages
```
sudo dnf -y install httpd mariadb-server php php-mysqlnd
```

#### 3.3.2. Enable and Start Apache and Mariadb
```
sudo systemctl enable --now httpd
sudo systemctl start httpd
sudo systemctl enable --now mariadb
sudo systemctl start mariadb
```

#### 3.3.3. Opening Firewall Ports
RHEL activates firewall by default. We have to open http and https ports  permanently.

```
sudo firewall-cmd --add-service=http --add-service=https
sudo firewall-cmd --add-service=http --add-service=https --permanent
```

#### 3.3.4. Test
You can use the test scenario at 1.3.2 to test RHEL LAMP stack. For RHEL  8, you should run "sudo mysql" instead of "sudo mariadb".

### 3.4. Service Management
Unlike Debian and derivatives, RHEL and derivatives does not enable and start services by default.

#### 3.4.1. Status of a Service
```
systemctl status httpd
```
 
#### 3.4.2. Start/Stop a Service
```
sudo systemctl stop httpd
sudo systemctl start httpd
```

To force to stop

```
sudo systemctl kill httpd
```

#### 3.4.3. Reload a Service
Reads configuration file again

```
sudo systemctl reload httpd
```

#### 3.4.4. Restart a Service
Stops and Starts

```
sudo systemctl restart httpd
```

#### 3.4.5. Enable/Disable a Service
```
sudo systemctl enable httpd
sudo systemctl disable httpd
```

<br>
</details>

<details markdown='1'>
<summary>
4. Alpine Linux 3.17 3.18 & 3.19
</summary>

---
### 4.1. Package Management
Commands require root or sudo.

#### 4.1.1. Update Cache
```
apk update
```

#### 4.1.2. Upgrade Packages
```
apk upgrade
```

#### 4.1.3. Install a Package
```
apk add apache2
```

#### 4.1.4. Remove a Package
```
apt del apache2
```

#### 4.1.5. Search a Package
```
apk search apache2
```

#### 4.1.6. Clean Unused Packages
Not available as much as I know.

#### 4.1.7. Show Package Info
```
apk info apache2
```
 
### 4.2. Network Configuration
#### 4.2.1. Get the name of the network adapter
The name of the network adapter will be something like eth0, but we need  the exact name. 

The following command lists the network interface name(s). The one in  eth* format should be the name of your network adapter.

```
ls /sys/class/net
```

In any case you cannot get the name, you can try to following command:

```
ip a
```

#### 4.2.2. IP and DNS Configuration
I assume that your network adapter name is eth0, otherwise change it. 

Change IP address and Gateway:

```
sudo nano /etc/network/interfaces
```

File contents will be like below

```
auto lo
iface lo inet loopback
#auto eth0
#iface eth0 inet dhcp
auto eth0
iface eth0 inet static
        address 192.168.0.247/24
        gateway 192.168.0.1
        hostname alpine
```

Change DNS Addresses:

```
sudo nano /etc/resolv.conf
```

File contents will be like below

```
nameserver 192.168.0.1
nameserver 8.8.8.8
```


#### 4.2.3. Restart Network Adapter
```
sudo ifdown eth0 && sudo ifup eth0
```

### 4.3. Installing LAMP Stack
#### 4.3.1. Install Packages
```
sudo apk add apache2 php php-mysqli php-apache2 mariadb mariadb-client
```

#### 4.3.2. Enable Apache
```
sudo rc-update add apache2 default
sudo rc-service apache2 restart
```

#### 4.3.3. Initialize and Enable Mariadb
```
sudo mysql_install_db --user=mysql --datadir=/var/lib/mysql
sudo rc-update add mariadb default
sudo rc-service mariadb start
```

#### 4.3.4. Test
You can use the test scenario at 1.3.2 to test Alpine Linux LAMP stack. 

Just remember, default web site directory is /var/www/localhost/htdocs in  Alpine.

### 4.4. Service Management
Alpine Linux uses OpenRC as the init system. 

#### 4.4.1. Status of a Service
```
rc-service apache2 status
```
 
#### 4.4.2. Start/Stop a Service
```
sudo rc-service apache2 stop
sudo rc-service apache2 start
```

#### 4.4.3. Reload a Service
Reads configuration file again

```
sudo rc-service apache2 reload
```

#### 4.4.4. Restart a Service
Stops and Starts

```
sudo rc-service apache2 restart
```

#### 4.4.5. Enable/Disable a Service
```
sudo rc-update add apache2 default
sudo rc-update del apache2 default
```

<br>
</details>

<details markdown='1'>
<summary>
5. Devuan 5 & 4
</summary>

---
Devuan is a derivative of Debian without systemd. Devuan 5 & 4 are based  on Debian 12 & 11.

### 5.1. Package Management
Commands require root or sudo.

#### 5.1.1. Update Cache
```
apt update
```

#### 5.1.2. Upgrade Packages
```
apt upgrade
```

#### 5.1.3. Install a Package
```
apt install apache2
```

#### 5.1.4. Remove a Package
```
apt remove apache2
```

#### 5.1.5. Search a Package
```
apt search apache2
```

#### 5.1.6. Clean Unused Packages
```
apt autoremove
```

#### 5.1.7. Show Package Info
```
apt show apache2
```
 
### 5.2. Network Configuration
#### 5.2.1. Get the name of the network adapter
The name of the network adapter will be something like enp0s3, but we  need the exact name. 

The following command lists the network interface name(s). The one in  eth* format should be the name of your network adapter.

```
ls /sys/class/net
```

In any case you cannot get the name, you can try to following command:

```
ip a
```


#### 5.2.2. IP configuration. 
```
sudo nano /etc/network/interfaces
```

I assume that your network adapter name is eth0, otherwise change it.

Fill the file like below (change to your IP addresses)

```
auto eth0
iface eth0 inet static
address 192.168.0.3/24
broadcast 192.168.0.255
network 192.168.0.0
gateway 192.168.0.1
```

If you want to use DHCP, fill the file as below

```
auto eth0
iface eth0 inet dhcp
```
 
#### 5.2.3. DNS Addresses
```
sudo nano /etc/resolv.conf
```

Add your DNS addresses as below

```
nameserver 46.196.235.35
nameserver 178.233.140.110
nameserver 46.197.15.60
```


#### 5.2.4. Restart Network Adapter
Assuming your network adapter name is enp0s3

```
sudo ifdown eth0 && sudo ifup eth0
```

If you are connecting through SSH, your connection would break up. You  need to connect with the new IP again.


### 5.3. Installing LAMP Stack
#### 5.3.1. Install packages
```
sudo apt update
sudo apt install --yes apache2 mariadb-server php libapache2-mod-php php-mysql
```

#### 5.3.2. Test LAMP
You can use the test scenario at 1.3.2 to test Devuan Linux LAMP stack.

### 5.4. Service Management
Conventionally, when a package with a service is installed on Devuan, it is enabled and started by default.

At Devuan installation, user can choose from 3 init systems:

- sysvinit (default option)
- runit
- OpenRC

At this tutorial, I assume our Devuan server has sysvinit system.

#### 5.4.1. Status of a Service
```
sudo service apache2 status 
```
 

#### 5.4.2. Start/Stop a Service
```
sudo service apache2 stop
sudo service apache2 start
```


#### 5.4.3. Reload a Service
Reads configuration file again

```
sudo service apache2 reload
```


#### 5.4.4. Restart a Service
Stops and Starts

```
sudo service apache2 restart
```

#### 5.4.5. Enable/Disable a Service
```
sudo update-rc.d apache2 defaults
sudo update-rc.d apache2 remove
```

</details>

