##### AdminerOnDebianUbuntu 
# Adminer on Debian and Ubuntu for MariaDB 

<details markdown='1'>
<summary>
0. Specs
</summary>
---
Adminer is a powerful web based management tool for Mysql, Mariadb and  more. You have to install it on the server which has the DB installed.

On my config I wanted to bind Adminer to a specific site config on the  server side and restrict it with only 1 client IP (might be more) to  reach.

My Hostname: adminer.386387.xyz  
Lamp is already installed (See [LampOnDebianUbuntu](LampOnDebianUbuntu.html) Tutorial)  
My Client IP address: 192.168.1.88  
MariaDB Admin User: dbadmin   Password: PaSswOrD1234  
Server Versions: Debian 12/11 Ubuntu 24.04/22.04 LTS Server

<br>
</details>

<details markdown='1'>
<summary>
1. Install Adminer
</summary>
---
It is possible to download Adminer php files and use them, but I prefer  installing its package, this way all the upgrades will be managed by  Debian/Ubuntu.

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
We are going to need a Database Admin user to log in Adminer and manage  the databases.

```
sudo mariadb
```

Run on Mariadb shell

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

If you have more than 1 IP to reach Adminer, add them to Require IP line  after the first IP.

If you don't need IP control, remove all the directory stanza (lines 2,3,4)

```
<VirtualHost *:80>
    <Directory /usr/share/adminer/adminer>
       Require ip 192.168.1.88
    </Directory>   
    Alias /adminer /usr/share/adminer/adminer
    ServerAdmin webmaster@386387.xyz	
    ServerName adminer.386387.xyz
    DocumentRoot /var/www/adminer
    ErrorLog ${APACHE_LOG_DIR}/adminer-error.log
    CustomLog ${APACHE_LOG_DIR}/adminer-access.log combined
</VirtualHost>
```

Create a home directory for the site and set permissions

```
sudo mkdir /var/www/adminer
sudo chown www-data:www-data /var/www/adminer
sudo chmod 770 /var/www/adminer
```

If you want, you can put an index.html file to the home directory, but I  prefer leaving the home directory empty and access to Adminer through its  directory.

### 3.2. Enable the Site and Reload Apache
```
sudo a2ensite adminer.386387.xyz.conf
sudo systemctl reload apache2
```

<br>
</details>

<details markdown='1'>
<summary>
4. Run it
</summary>
---
Your web based Database Management tool is ready:

`http://adminer.386387.xyz/adminer`

You need to select MySQL for MariaDB, server must be localhost (default), username: dbadmin, password: (whatever you gave at the Mariadb script, Database: leave empty to reach all the databases.

<br>
</details>

<details markdown='1'>
<summary>
5. Security
</summary>
---
You should enable https if you want to put your site on the internet. 

Actually https should be enabled on local network sites too. Refer to  [CertbotOnDebianUbuntu](CertbotOnDebianUbuntu.html) tutorial for enabling https with free certificates.

</details>

