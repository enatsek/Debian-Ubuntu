---
title: "Other Linux Distributions"
description: "Managing Debian, Ubuntu, Red Hat, Alpine, and Devuan systems"
sidebar: 
   label: Other Linux Distributions
---

#####  Managing Debian, Ubuntu, Red Hat, Alpine, and Devuan systems

## 0. Specs
---

### 0.1. The What

Although my tutorials (and my learning journey) focus on Debian and Ubuntu Linux distributions, administrators may occasionally need to work with other Linux distributions as well.

This tutorial aims to help Debian/Ubuntu administrators adapt to other Linux distributions, specifically Red Hat, Alpine, and Devuan.

Main topics covered:
- Package Management
- Network Configuration
- Installing LAMP Stack
- Service Management

Distributions covered:
- Debian 13 and 12
- Ubuntu 24.04 and 22.04 LTS
- RHEL (CentOS, AlmaLinux, Rocky Linux) 10.x, 9.x
- Alpine 3.23
- Devuan 6 and 5


### 0.2. Resources:

- [access.redhat.com](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9)
- [wiki.alpinelinux.org](https://wiki.alpinelinux.org/wiki/Main_Page)
- [wiki.debian.org](https://wiki.debian.org/)
- [www.geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-retrieve-data-from-mysql-database-using-php/)

<br>

## 1. Debian 13 & 12
---

### 1.1. Package Management

Commands require root or sudo privileges.

#### 1.1.1. Update Cache

```bash
sudo apt update
```

#### 1.1.2. Upgrade Packages

```bash
sudo apt upgrade
```

#### 1.1.3. Install a Package

```bash
sudo apt install apache2
```

#### 1.1.4. Remove a Package

```bash
sudo apt remove apache2
```

#### 1.1.5. Search for a Package

```bash
sudo apt search apache2
```

#### 1.1.6. Clean Unused Packages

```bash
sudo apt autoremove
```

#### 1.1.7. Show Package Information

```bash
sudo apt show apache2
```

### 1.2. Network Configuration

#### 1.2.1. Identify Network Adapter Name

Network adapter names typically follow patterns like `enp0s3`. To find the exact name:

```bash
ls /sys/class/net
```

The interface with an `en*` format is usually your network adapter. If unsure, use:

```bash
ip a
```

#### 1.2.2. IP configuration. 

Edit the network interfaces file (replace `enp0s3` with your actual interface name):

```bash
sudo nano /etc/network/interfaces
```

**Static IP configuration:**

```text
auto enp0s3
iface enp0s3 inet static
   address 192.168.1.135/24
   broadcast 192.168.1.255
   network 192.168.1.0
   gateway 192.168.1.1
```

**DHCP configuration:**

```text
auto enp0s3
iface enp0s3 inet dhcp
```

#### 1.2.3. DNS Addresses

```bash
sudo nano /etc/resolv.conf
```

Add DNS servers:

```text
nameserver 46.196.235.35
nameserver 178.233.140.110
nameserver 46.197.15.60
```

#### 1.2.4. Restart Network Adapter

Replace `enp0s3` with your interface name:

```bash
sudo ifdown enp0s3 && sudo ifup enp0s3
```

Alternatively:

```bash
sudo systemctl restart networking.service
```

**Note:** If connected via SSH, your connection will drop. Reconnect using the new IP address.

### 1.3. Installing LAMP Stack

#### 1.3.1. Install Packages

```bash
sudo apt update
sudo apt install --yes apache2 mariadb-server php \
   libapache2-mod-php php-mysql
```

#### 1.3.2. Test LAMP Stack

We'll create a test database, table, and PHP file to verify all components work together.

**Create test database and user:**

```bash
sudo mariadb
```

Run in MariaDB shell:

```sql
CREATE DATABASE mysampledb;
USE mysampledb;
CREATE TABLE Employees (Name char(15), Age int(3), Occupation char(15));
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
INSERT INTO Employees VALUES ('John Doe', '33', 'Sleeper');
INSERT INTO Employees VALUES ('Mariadb Server', '14', 'RDBM');
GRANT ALL ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
exit
```

**Create test PHP file:**

```bash
sudo nano /var/www/html/test.php
```

Add the following content:

```php
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

**Test:** Access `http://[your-server-ip]/test.php` from a browser to verify the LAMP stack is working.

### 1.4. Service Management

In Debian, services are typically enabled and started automatically upon installation.

#### 1.4.1. Check Service Status

```bash
systemctl status apache2
```
 
#### 1.4.2. Start/Stop a Service

```bash
sudo systemctl stop apache2
sudo systemctl start apache2
```

Force stop:

```bash
sudo systemctl kill apache2
```

#### 1.4.3. Reload a Service

Reloads configuration without stopping:

```bash
sudo systemctl reload apache2
```

#### 1.4.4. Restart a Service

```bash
sudo systemctl restart apache2
```

#### 1.4.5. Enable/Disable a Service

```bash
sudo systemctl enable apache2
sudo systemctl disable apache2
```

<br>

## 2. Ubuntu 24.04 LTS & 22.04 LTS

---

### 2.1. Package Management

Commands require root or sudo privileges.

#### 2.1.1. Update Cache

```bash
sudo apt update
```

#### 2.1.2. Upgrade Packages

```bash
sudo apt upgrade
```

#### 2.1.3. Install a Package

```bash
sudo install apache2
```

#### 2.1.4. Remove a Package

```bash
sudo remove apache2
```

#### 2.1.5. Search for a Package

```bash
sudo search apache2
```

#### 2.1.6. Clean Unused Packages

```bash
sudo autoremove
```

#### 2.1.7. Show Package Information

```bash
sudo show apache2
```
 
### 2.2. Network Configuration

#### 2.2.1. Get the name of the network adapter

Network adapter names typically follow patterns like `enp0s3`. To find the exact name:

```bash
ls /sys/class/net
```

The interface with an `en*` format is usually your network adapter. If unsure, use:

```bash
ip a
```

#### 2.2.2. Network configuration. 

Ubuntu uses Netplan for network configuration. Edit the configuration file (filename may vary):

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Replace `enp0s3` with your interface name and adjust IP settings:

```yaml
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

#### 2.2.3. Apply Netplan Configuration

```bash
sudo netplan apply
```

**Note:** SSH connections may drop; reconnect using the new IP.


### 2.3. Installing LAMP Stack

#### 2.3.1. Install Packages

```bash
sudo apt update
sudo apt install --yes apache2 mariadb-server php \
    libapache2-mod-php php-mysql
```

#### 2.3.2. Test LAMP

Use the test scenario from section 1.3.2.

### 2.4. Service Management

As a Debian derivative, Ubuntu behaves similarly for service management.

#### 2.4.1. Check Service Status

```bash
systemctl status apache2
```

#### 2.4.2. Start/Stop a Service

```bash
sudo systemctl stop apache2
sudo systemctl start apache2
```

Force stop:

```bash
sudo systemctl kill apache2
```

#### 2.4.3. Reload a Service

Reads configuration file again

```bash
sudo systemctl reload apache2
```

#### 2.4.4. Restart a Service

```bash
sudo systemctl restart apache2
```

#### 2.4.5. Enable/Disable a Service

```bash
sudo systemctl enable apache2
sudo systemctl disable apache2
```

<br>

## 3. RHEL (AlmaLinux, Rocky Linux) 10.x, 9.x
---

AlmaLinux and Rocky Linux are RHEL-compatible distributions, meaning commands and configurations for RHEL work on these distributions as well.

### 3.1. Package Management

Commands require root or sudo privileges.

#### 3.1.1. Check for Updates

```bash
sudo dnf check-update
```

It is always called when installing or updating packages. So it is not necessary before installing or upgrading packages.

#### 3.1.2. Upgrade Packages

```bash
sudo dnf upgrade
```

#### 3.1.3. Install a Package

```bash
sudo dnf install httpd
```

#### 3.1.4. Remove a Package

```bash
sudo dnf remove httpd
```

#### 3.1.5. Search for a Package

```bash
sudo dnf search httpd
```

#### 3.1.6. Clean Unused Packages

```bash
sudo dnf autoremove
```

#### 3.1.7. Show Package Information

```bash
sudo dnf info httpd
```
 
### 3.2. Network Configuration

#### 3.2.1. Identify Network Adapter Name

Network adapter names typically follow patterns like `enp0s3`. To find the exact name:

```bash
ls /sys/class/net
```

The interface with an `en*` format is usually your network adapter. If unsure, use:

```bash
ip a
```

#### 3.2.2. IP and DNS Configuration

Replace `enp0s3` with your interface name:

```bash
sudo nmcli con modify 'enp0s3' ifname enp0s3 ipv4.method manual \
   ipv4.addresses 192.168.1.156/24 gw4 192.168.1.1
sudo nmcli con modify 'enp0s3' ipv4.dns 8.8.8.8
```

#### 3.2.3. Restart Network Connection

```bash
sudo nmcli con down 'enp0s3' && sudo nmcli con up 'enp0s3'
```

### 3.3. Installing LAMP Stack

Note: Package names differ from Debian/Ubuntu (e.g., `httpd` instead of `apache2`).

#### 3.3.1. Install Packages

```bash
sudo dnf -y install httpd mariadb-server php php-mysqlnd
```

#### 3.3.2. Enable and Start Services

```bash
sudo systemctl enable --now httpd
sudo systemctl enable --now mariadb
```

#### 3.3.3. Configure Firewall

RHEL enables the firewall by default. Open HTTP and HTTPS ports:

```bash
sudo firewall-cmd --add-service=http --add-service=https
sudo firewall-cmd --add-service=http --add-service=https --permanent
```

#### 3.3.4. Test

Use the test scenario from section 1.3.2. Note: For RHEL 9, use `sudo mysql` instead of `sudo mariadb`.

### 3.4. Service Management

Unlike Debian-based systems, RHEL does not automatically enable or start services after installation.

#### 3.4.1. Check Service Status

```bash
systemctl status httpd
```
 
#### 3.4.2. Start/Stop a Service

```bash
sudo systemctl stop httpd
sudo systemctl start httpd
```

Force stop:

```bash
sudo systemctl kill httpd
```

#### 3.4.3. Reload a Service

```bash
sudo systemctl reload httpd
```

#### 3.4.4. Restart a Service

Stops and Starts

```bash
sudo systemctl restart httpd
```

#### 3.4.5. Enable/Disable a Service

```bash
sudo systemctl enable httpd
sudo systemctl disable httpd
```

<br>

## 4. Alpine Linux 3.23
---

### 4.1. Package Management

Commands require root or sudo privileges.

#### 4.1.1. Update Cache

```bash
sudo apk update
```

#### 4.1.2. Upgrade Packages

```bash
sudo apk upgrade
```

#### 4.1.3. Install a Package

```bash
sudo apk add apache2
```

#### 4.1.4. Remove a Package

```bash
sudo apk del apache2
```

#### 4.1.5. Search for a Package

```bash
sudo apk search apache2
```

#### 4.1.6. Clean Unused Packages

Not available in Alpine's package manager.

#### 4.1.7. Show Package Information

```bash
sudo apk info apache2
```
 
### 4.2. Network Configuration

#### 4.2.1. Identify Network Adapter Name

Alpine typically uses `eth0` style names:

```bash
ls /sys/class/net
```

or

```bash
ip a
```

#### 4.2.2. IP and DNS Configuration

Edit network interfaces (replace `eth0` with your interface name):

```bash
sudo nano /etc/network/interfaces
```

File contents will be like below

```text
auto lo
iface lo inet loopback

#auto eth0
#iface eth0 inet dhcp
auto eth0
iface eth0 inet static
        address 192.168.1.172/24
        gateway 192.168.1.1
        hostname alpine

```

Configure DNS:

```bash
sudo nano /etc/resolv.conf
```

```text
nameserver 192.168.0.1
nameserver 8.8.8.8
```


#### 4.2.3. Restart Network Adapter

```bash
sudo ifdown eth0 && sudo ifup eth0
```

### 4.3. Installing LAMP Stack

#### 4.3.1. Install Packages

```bash
sudo apk add apache2 php php-mysqli php-apache2 mariadb mariadb-client
```

#### 4.3.2. Enable and Start Apache

```bash
sudo rc-update add apache2 default
sudo rc-service apache2 start
```

#### 4.3.3. Initialize and Enable Mariadb

```bash
sudo mysql_install_db --user=mysql --datadir=/var/lib/mysql
sudo rc-update add mariadb default
sudo rc-service mariadb start
```

#### 4.3.4. Test

Use the test scenario from section 1.3.2. Note: Alpine's default web directory is `/var/www/localhost/htdocs`.

### 4.4. Service Management

Alpine uses OpenRC as its init system.

#### 4.4.1. Check Service Status

```bash
rc-service apache2 status
```
 
#### 4.4.2. Start/Stop a Service

```bash
sudo rc-service apache2 stop
sudo rc-service apache2 start
```

#### 4.4.3. Reload a Service

```bash
sudo rc-service apache2 reload
```

#### 4.4.4. Restart a Service

```bash
sudo rc-service apache2 restart
```

#### 4.4.5. Enable/Disable a Service

```bash
sudo rc-update add apache2 default
sudo rc-update del apache2 default
```

<br>

## 5. Devuan 6 & 5
---

Devuan is a Debian derivative without systemd. Devuan 6 & 5 are based on Debian 13 & 12.

### 5.1. Package Management

Commands require root or sudo privileges.

#### 5.1.1. Update Cache

```bash
sudo apt update
```

#### 5.1.2. Upgrade Packages

```bash
sudo apt upgrade
```

#### 5.1.3. Install a Package

```bash
sudo apt install apache2
```

#### 5.1.4. Remove a Package

```bash
sudo apt remove apache2
```

#### 5.1.5. Search for a Package

```bash
sudo apt search apache2
```

#### 5.1.6. Clean Unused Packages

```bash
sudo apt autoremove
```

#### 5.1.7. Show Package Information

```bash
sudo apt show apache2
```
 
### 5.2. Network Configuration

#### 5.2.1. Identify Network Adapter Name

Devuan typically uses `eth0` style names:

```bash
ls /sys/class/net
```

or

```bash
ip a
```

#### 5.2.2. IP configuration. 

Edit network interfaces (replace `eth0` with your interface name):

```bash
sudo nano /etc/network/interfaces
```

**Static IP:**

```text
auto eth0
iface eth0 inet static
   address 192.168.1.176/24
   broadcast 192.168.1.255
   network 192.168.1.0
   gateway 192.168.1.1
```

**DHCP:**

```text
auto eth0
iface eth0 inet dhcp
```
 
#### 5.2.3. DNS Configuration

```bash
sudo nano /etc/resolv.conf
```

```text
nameserver 46.196.235.35
nameserver 178.233.140.110
nameserver 46.197.15.60
```


#### 5.2.4. Restart Network Adapter

```bash
sudo ifdown eth0 && sudo ifup eth0
```

**Note:** SSH connections may drop; reconnect using the new IP.

### 5.3. Installing LAMP Stack

#### 5.3.1. Install Packages

```bash
sudo apt update
sudo apt install --yes apache2 mariadb-server php libapache2-mod-php php-mysql
```

#### 5.3.2. Test LAMP

Use the test scenario from section 1.3.2.

### 5.4. Service Management

Devuan services are typically enabled and started automatically. During installation, you can choose from three init systems:
- sysvinit (default)
- runit
- OpenRC

This tutorial assumes sysvinit.

#### 5.4.1. Check Service Status

```bash
sudo service apache2 status 
```
 

#### 5.4.2. Start/Stop a Service

```bash
sudo service apache2 stop
sudo service apache2 start
```


#### 5.4.3. Reload a Service

```bash
sudo service apache2 reload
```


#### 5.4.4. Restart a Service

```bash
sudo service apache2 restart
```

#### 5.4.5. Enable/Disable a Service

```bash
sudo update-rc.d apache2 defaults
sudo update-rc.d apache2 remove
```



