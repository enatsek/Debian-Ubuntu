##### Adminer
# Adminer Tutorial for Debian and Ubuntu Servers  

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.1. The What

Adminer is a lightweight database management tool written in PHP that allows users to manage databases like MySQL, PostgreSQL, and SQLite through a simple web interface. It is distributed as a single PHP file, making it easy to deploy on a server.

In this configuration, I wanted to bind Adminer to a specific site configuration on the server side and restrict access to only one client IP (though more can be added).

### 0.2. The Environment

- My Hostname: `adminer.386387.xyz`
- LAMP is already installed (See [LAMP Tutorial](lamp.html))
- My Client IP address: `192.168.1.56`
- MariaDB Admin User: `dbadmin` | Password: `PaSswOrD1234`
- Server Versions: Debian 13/12, Ubuntu 24.04/22.04 LTS Server

<br>
</details>

<details markdown='1'>
<summary>
1. Install Adminer
</summary>

---

While it's possible to download the Adminer PHP files directly, I prefer installing the package. This way, all upgrades will be managed by Debian/Ubuntu's package management system.

```
sudo apt update
sudo apt install adminer --yes
```

<br>
</details>

<details markdown='1'>
<summary>
2. DB Admin User
</summary>

---
We need to create a database admin user to log into Adminer and manage the databases.

```
sudo mariadb
```

Run the following in the MariaDB shell:

```
grant all on *.* to 'dbadmin'@'localhost' identified by 'PaSswOrD1234';
exit;
```

<br>
</details>

<details markdown='1'>
<summary>
3. Prepare a Web Site
</summary>

---
### 3.1. Create a Web Site Config File and Fill it
```
sudo nano /etc/apache2/sites-available/adminer.386387.xyz.conf
```

Add the following configuration. If you have more than one IP that needs access to Adminer, add them to the `Require ip` line. If you don't need IP-based access control, remove the entire `<Directory>` section (lines 2-4).

```
<VirtualHost *:80>
    <Directory /usr/share/adminer/adminer>
       Require ip 192.168.1.56
    </Directory>   
    Alias /adminer /usr/share/adminer/adminer
    ServerAdmin webmaster@386387.xyz	
    ServerName adminer.386387.xyz
    DocumentRoot /var/www/adminer
    ErrorLog ${APACHE_LOG_DIR}/adminer-error.log
    CustomLog ${APACHE_LOG_DIR}/adminer-access.log combined
</VirtualHost>
```

### 3.2. Create the Site Directory and Set Permissions

```
sudo mkdir /var/www/adminer
sudo chown www-data:www-data /var/www/adminer
sudo chmod 770 /var/www/adminer
```

You can optionally place an `index.html` file in the home directory, but I prefer leaving it empty and accessing Adminer directly through its subdirectory.

### 3.3. Enable the Site and Reload Apache
```
sudo a2ensite adminer.386387.xyz.conf
sudo systemctl reload apache2
```

<br>
</details>

<details markdown='1'>
<summary>
4. Run Adminer
</summary>

---

Your web-based database management tool is now ready:

**URL:** `http://adminer.386387.xyz/adminer`

**Login Information:**
- System: Select **MySQL** for MariaDB
- Server: `localhost` (default)
- Username: `dbadmin`
- Password: `PaSswOrD1234` (or whatever you set in the MariaDB script)
- Database: Leave empty to access all databases

<br>
</details>

<details markdown='1'>
<summary>
5. Security
</summary>

---

You should enable HTTPS, especially if you plan to expose your site to the internet. HTTPS is also recommended for local network sites for enhanced security.

Refer to the [Certbot Tutorial](certbot.html) for instructions on enabling HTTPS with free Let's Encrypt certificates.

</details>

