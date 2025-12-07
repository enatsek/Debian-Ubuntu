##### Other Linuxes
# Other Linux Distributions for Debian and Ubuntu Admins

<details markdown='1'>
<summary>
0. Specs
</summary>

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
</details>

<details markdown='1'>
<summary>
1. Debian 13 & 12
</summary>

---
### 1.1. Package Management

Commands require root or sudo privileges.

#### 1.1.1. Update Cache

```
sudo apt update
```

#### 1.1.2. Upgrade Packages

```
sudo apt upgrade
```

#### 1.1.3. Install a Package

```
sudo apt install apache2
```

#### 1.1.4. Remove a Package

```
sudo apt remove apache2
```

#### 1.1.5. Search for a Package

```
sudo apt search apache2
```

#### 1.1.6. Clean Unused Packages

```
sudo apt autoremove
```

#### 1.1.7. Show Package Information

```
sudo apt show apache2
```

### 1.2. Network Configuration

#### 1.2.1. Identify Network Adapter Name

Network adapter names typically follow patterns like `enp0s3`. To find the exact name:

```
ls /sys/class/net
```

The interface with an `en*` format is usually your network adapter. If unsure, use:

```
ip a
```

#### 1.2.2. IP configuration. 

Edit the network interfaces file (replace `enp0s3` with your actual interface name):

```
sudo nano /etc/network/interfaces
```

**Static IP configuration:**

```
auto enp0s3
iface enp0s3 inet static
   address 192.168.1.135/24
   broadcast 192.168.1.255
   network 192.168.1.0
   gateway 192.168.1.1
```

**DHCP configuration:**

```
auto enp0s3
iface enp0s3 inet dhcp
```

#### 1.2.3. DNS Addresses

```
sudo nano /etc/resolv.conf
```

Add DNS servers:

```
nameserver 46.196.235.35
nameserver 178.233.140.110
nameserver 46.197.15.60
```

#### 1.2.4. Restart Network Adapter

Replace `enp0s3` with your interface name:

```
sudo ifdown enp0s3 && sudo ifup enp0s3
```

Alternatively:

```
sudo systemctl restart networking.service
```

**Note:** If connected via SSH, your connection will drop. Reconnect using the new IP address.

### 1.3. Installing LAMP Stack

#### 1.3.1. Install Packages

```
sudo apt update
sudo apt install --yes apache2 mariadb-server php \
   libapache2-mod-php php-mysql
```


#### 1.3.2. Test LAMP Stack

We'll create a test database, table, and PHP file to verify all components work together.

**Create test database and user:**

```
sudo mariadb
```

Run in MariaDB shell:

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

**Create test PHP file:**

```
sudo nano /var/www/html/test.php
```

Add the following content:

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

**Test:** Access `http://[your-server-ip]/test.php` from a browser to verify the LAMP stack is working.

### 1.4. Service Management

In Debian, services are typically enabled and started automatically upon installation.

#### 1.4.1. Check Service Status
```
systemctl status apache2
```
 
#### 1.4.2. Start/Stop a Service

```
sudo systemctl stop apache2
sudo systemctl start apache2
```

Force stop:

```
sudo systemctl kill apache2
```

#### 1.4.3. Reload a Service

Reloads configuration without stopping:

```
sudo systemctl reload apache2
```

#### 1.4.4. Restart a Service

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

Commands require root or sudo privileges.

#### 2.1.1. Update Cache

```
sudo apt update
```

#### 2.1.2. Upgrade Packages

```
sudo apt upgrade
```

#### 2.1.3. Install a Package

```
sudo install apache2
```

#### 2.1.4. Remove a Package

```
sudo remove apache2
```

#### 2.1.5. Search for a Package

```
sudo search apache2
```

#### 2.1.6. Clean Unused Packages

```
sudo autoremove
```

#### 2.1.7. Show Package Information

```
sudo show apache2
```
 
## 2.2. Network Configuration

#### 2.2.1. Get the name of the network adapter

Network adapter names typically follow patterns like `enp0s3`. To find the exact name:

```
ls /sys/class/net
```

The interface with an `en*` format is usually your network adapter. If unsure, use:

```
ip a
```

#### 2.2.2. Network configuration. 

Ubuntu uses Netplan for network configuration. Edit the configuration file (filename may vary):

```
sudo nano /etc/netplan/00-installer-config.yaml
```

Replace `enp0s3` with your interface name and adjust IP settings:

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

#### 2.2.3. Apply Netplan Configuration

```
sudo netplan apply
```

**Note:** SSH connections may drop; reconnect using the new IP.


### 2.3. Installing LAMP Stack

#### 2.3.1. Install Packages

```
sudo apt update
sudo apt install --yes apache2 mariadb-server php \
    libapache2-mod-php php-mysql
```

#### 2.3.2. Test LAMP

Use the test scenario from section 1.3.2.

### 2.4. Service Management

As a Debian derivative, Ubuntu behaves similarly for service management.

#### 2.4.1. Check Service Status

```
systemctl status apache2
```

#### 2.4.2. Start/Stop a Service

```
sudo systemctl stop apache2
sudo systemctl start apache2
```

Force stop:

```
sudo systemctl kill apache2
```

#### 2.4.3. Reload a Service

Reads configuration file again

```
sudo systemctl reload apache2
```

#### 2.4.4. Restart a Service

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
3. RHEL (AlmaLinux, Rocky Linux) 10.x, 9.x
</summary>

---

AlmaLinux and Rocky Linux are RHEL-compatible distributions, meaning commands and configurations for RHEL work on these distributions as well.

### 3.1. Package Management

Commands require root or sudo privileges.

#### 3.1.1. Check for Updates

```
sudo dnf check-update
```

It is always called when installing or updating packages. So it is not necessary before installing or upgrading packages.

#### 3.1.2. Upgrade Packages

```
sudo dnf upgrade
```

#### 3.1.3. Install a Package

```
sudo dnf install httpd
```

#### 3.1.4. Remove a Package

```
sudo dnf remove httpd
```

#### 3.1.5. Search for a Package

```
sudo dnf search httpd
```

#### 3.1.6. Clean Unused Packages

```
sudo dnf autoremove
```

#### 3.1.7. Show Package Information

```
sudo dnf info httpd
```
 
### 3.2. Network Configuration

#### 3.2.1. Identify Network Adapter Name

Network adapter names typically follow patterns like `enp0s3`. To find the exact name:

```
ls /sys/class/net
```

The interface with an `en*` format is usually your network adapter. If unsure, use:

```
ip a
```

#### 3.2.2. IP and DNS Configuration

Replace `enp0s3` with your interface name:

```
sudo nmcli con modify 'enp0s3' ifname enp0s3 ipv4.method manual \
   ipv4.addresses 192.168.1.156/24 gw4 192.168.1.1
sudo nmcli con modify 'enp0s3' ipv4.dns 8.8.8.8
```

#### 3.2.3. Restart Network Connection

```
sudo nmcli con down 'enp0s3' && sudo nmcli con up 'enp0s3'
```

### 3.3. Installing LAMP Stack

Note: Package names differ from Debian/Ubuntu (e.g., `httpd` instead of `apache2`).

#### 3.3.1. Install Packages

```
sudo dnf -y install httpd mariadb-server php php-mysqlnd
```

#### 3.3.2. Enable and Start Services

```
sudo systemctl enable --now httpd
sudo systemctl enable --now mariadb
```

#### 3.3.3. Configure Firewall

RHEL enables the firewall by default. Open HTTP and HTTPS ports:

```
sudo firewall-cmd --add-service=http --add-service=https
sudo firewall-cmd --add-service=http --add-service=https --permanent
```

#### 3.3.4. Test

Use the test scenario from section 1.3.2. Note: For RHEL 9, use `sudo mysql` instead of `sudo mariadb`.

### 3.4. Service Management

Unlike Debian-based systems, RHEL does not automatically enable or start services after installation.

#### 3.4.1. Check Service Status

```
systemctl status httpd
```
 
#### 3.4.2. Start/Stop a Service

```
sudo systemctl stop httpd
sudo systemctl start httpd
```

Force stop:

```
sudo systemctl kill httpd
```

#### 3.4.3. Reload a Service

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
4. Alpine Linux 3.23
</summary>

---
### 4.1. Package Management

Commands require root or sudo privileges.

#### 4.1.1. Update Cache

```
sudo apk update
```

#### 4.1.2. Upgrade Packages

```
sudo apk upgrade
```

#### 4.1.3. Install a Package

```
sudo apk add apache2
```

#### 4.1.4. Remove a Package

```
sudo apk del apache2
```

#### 4.1.5. Search for a Package

```
sudo apk search apache2
```

#### 4.1.6. Clean Unused Packages

Not available in Alpine's package manager.

#### 4.1.7. Show Package Information

```
sudo apk info apache2
```
 
### 4.2. Network Configuration

#### 4.2.1. Identify Network Adapter Name

Alpine typically uses `eth0` style names:

```
ls /sys/class/net
```

or

```
ip a
```

#### 4.2.2. IP and DNS Configuration

Edit network interfaces (replace `eth0` with your interface name):

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
        address 192.168.1.172/24
        gateway 192.168.1.1
        hostname alpine

```

Configure DNS:

```
sudo nano /etc/resolv.conf
```

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

#### 4.3.2. Enable and Start Apache

```
sudo rc-update add apache2 default
sudo rc-service apache2 start
```

#### 4.3.3. Initialize and Enable Mariadb

```
sudo mysql_install_db --user=mysql --datadir=/var/lib/mysql
sudo rc-update add mariadb default
sudo rc-service mariadb start
```

#### 4.3.4. Test

Use the test scenario from section 1.3.2. Note: Alpine's default web directory is `/var/www/localhost/htdocs`.

### 4.4. Service Management

Alpine uses OpenRC as its init system.

#### 4.4.1. Check Service Status

```
rc-service apache2 status
```
 
#### 4.4.2. Start/Stop a Service

```
sudo rc-service apache2 stop
sudo rc-service apache2 start
```

#### 4.4.3. Reload a Service

```
sudo rc-service apache2 reload
```

#### 4.4.4. Restart a Service

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
5. Devuan 6 & 5
</summary>

---

Devuan is a Debian derivative without systemd. Devuan 6 & 5 are based on Debian 13 & 12.

### 5.1. Package Management

Commands require root or sudo privileges.

#### 5.1.1. Update Cache

```
sudo apt update
```

#### 5.1.2. Upgrade Packages

```
sudo apt upgrade
```

#### 5.1.3. Install a Package

```
sudo apt install apache2
```

#### 5.1.4. Remove a Package

```
sudo apt remove apache2
```

#### 5.1.5. Search for a Package

```
sudo apt search apache2
```

#### 5.1.6. Clean Unused Packages

```
sudo apt autoremove
```

#### 5.1.7. Show Package Information

```
sudo apt show apache2
```
 
### 5.2. Network Configuration

#### 5.2.1. Identify Network Adapter Name

Devuan typically uses `eth0` style names:

```
ls /sys/class/net
```

or

```
ip a
```

#### 5.2.2. IP configuration. 

Edit network interfaces (replace `eth0` with your interface name):

```
sudo nano /etc/network/interfaces
```

**Static IP:**

```
auto eth0
iface eth0 inet static
   address 192.168.1.176/24
   broadcast 192.168.1.255
   network 192.168.1.0
   gateway 192.168.1.1
```

**DHCP:**

```
auto eth0
iface eth0 inet dhcp
```
 
#### 5.2.3. DNS Configuration

```
sudo nano /etc/resolv.conf
```

```
nameserver 46.196.235.35
nameserver 178.233.140.110
nameserver 46.197.15.60
```


#### 5.2.4. Restart Network Adapter

```
sudo ifdown eth0 && sudo ifup eth0
```

**Note:** SSH connections may drop; reconnect using the new IP.

### 5.3. Installing LAMP Stack

#### 5.3.1. Install Packages

```
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

```
sudo service apache2 status 
```
 

#### 5.4.2. Start/Stop a Service

```
sudo service apache2 stop
sudo service apache2 start
```


#### 5.4.3. Reload a Service

```
sudo service apache2 reload
```


#### 5.4.4. Restart a Service

```
sudo service apache2 restart
```

#### 5.4.5. Enable/Disable a Service
```
sudo update-rc.d apache2 defaults
sudo update-rc.d apache2 remove
```

</details>

