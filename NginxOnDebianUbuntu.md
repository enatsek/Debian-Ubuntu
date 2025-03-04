##### NginxOnDebianUbuntu 
# Basic Nginx Configuration On Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
Basic Nginx configuration, installation, SSL, LEMP stack, sample site  configurations, 

Server: Debian 12/11 or Ubuntu 24.04/22.04 LTS Server

srv1, srv2, srv3, srv4 all has the server's IP address.

Sources:
**Mastering Ubuntu Server 4th Ed.** by Jay LaCroix  
[nginx.org](https://nginx.org/en/docs/)  
[www.geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-retrieve-data-from-mysql-database-using-php/)

<br>
</details>

<details markdown='1'>
<summary>
1. Installation and Configuration Files
</summary>

---
### 1.1. Installation
Update repositories

```
sudo apt update
```

Install nginx

```
sudo apt install nginx --yes
```

A simple website is ready at http://srv1/

### 1.2. Configuration Files
Configuration files reside in /etc/nginx.

See main configuration file:

```
sudo nano /etc/nginx/nginx.conf
```
 
Available sites are in /etc/nginx/sites-available/

They must be enabled, that is linked to /etc/nginx/sites-enabled/ 

To enable a site conf named mysite in /etc/nginx/sites-available/ :

```
sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/mysite
```

And to disable it:

```
sudo rm /etc/nginx/sites-enabled/mysite
```

There is a default configuration which is already enabled

```
sudo nano /etc/nginx/sites-available/default
```

After enabling or disabling a site, we need to reload nginx:

```
sudo systemctl reload nginx
```
 
### 1.3. Site enable and disable scripts
You may remember Debian & Ubuntu Apache installations has a2ensite  and a2dissite scripts. We will create very (actually very very) simple  nginx scripts like them. 

#### 1.3.1. Create ~/bin Directory
This directory is in the search list of the executable files. You may  already have it. If it is so, skip this step.

```
mkdir ~/bin
```

You have to logoff and logon again.

#### 1.3.2. Scripts
Create site enable script

```
nano ~/bin/ngensite
```

Fill it as below

```
#/bin/bash
sudo ln -s /etc/nginx/sites-available/$1 /etc/nginx/sites-enabled/$1
```

Create site disable script

```
nano ~/bin/ngdissite
```

Fill it as below

```
#/bin/bash
sudo rm /etc/nginx/sites-enabled/$1
```

Make the scripts executable

```
chmod +x ~/bin/ngensite
chmod +x ~/bin/ngdissite
```

Now we can disable or enable a site with these scripts:

```
ngensite default
ngdissite default
```
 
### 1.4. Redesign Our Site
We will disable default configuration, leave it at sites-available as a  template, create a new conf with the name srv1 (my hostname) and enable  it.

#### 1.4.1. Disable default Conf
```
sudo rm /etc/nginx/sites-enabled/default
```

or simply

```
ngdissite default
```

#### 1.4.2. Create the New Conf
```
sudo nano /etc/nginx/sites-available/srv1
```

Fill it as below

```
server {
   listen 80;
   listen [::]:80;
   root /var/www/html;
   index index.html index.htm index.nginx-debian.html;
   server_name srv1;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Explanations:

- Listen IP version 4 at port 80
- Listen IP version 6 at port 80
- Root directory is /var/www/html
- Index file (default file) is one of the followings in order
- Server name is srv1 (can be more than 1 - after srv1)
- For the location in root (and subfolders), try the given name as a file, then as a folder, if can't find, send 404 error message.
- Don't display server version at error (and other) messages.

#### 1.4.3. Enable the New Conf
```
ngensite srv1
```

It is necessary to reload nginx

```
sudo systemctl reload nginx
```

<br>
</details>

<details markdown='1'>
<summary>
2. SSL Configuration
</summary>

---
We will test SSL configuration with self signed certificates. Later on  the tutorial, we are going to test getting certificates with certbot tool too.

### 2.1. Create a Self Signed Certificate
Create a place for the certificates

```
sudo mkdir /etc/nginx/certs
```

Create certificates

```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/nginx/certs/srv1.key -out /etc/nginx/certs/srv1.crt
```

You can give default answers to all the questions.

Key and certificate files are copied to /etc/nginx/certs/

### 2.1. Create SSL Conf
```
sudo nano /etc/nginx/sites-available/srv1-ssl
```

Fill it as below

```
server {
   listen 443 ssl;
   listen [::]:443 ssl;
   root /var/www/html;
   index index.html index.htm index.nginx-debian.html;
   server_name srv1;
   ssl_certificate /etc/nginx/certs/srv1.crt;
   ssl_certificate_key /etc/nginx/certs/srv1.key;
   ssl_session_timeout 5m;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Enable it

```
ngensite srv1-ssl
```

### 2.2. HTTPS Redirection
We have to add a redirection to srv1 conf to automatically redirect http://srv1/ to https://srv1/

```
sudo nano /etc/nginx/sites-available/srv1
```

Add the line below after the listen lines

```
   return 301 https://$host$request_uri;
```

Reload nginx

```
sudo systemctl reload nginx
```

### 2.3. SSL Site is Ready
`https://srv1/`

Your firefox will complain as "Warning: Potential Security Risk Ahead",  because our certificate is a self signed one. You can click "Advanced" and "Accept the Risk and Continue" to reach the SSL site.

<br>
</details>

<details markdown='1'>
<summary>
3. LEMP Stack
</summary>

---
- L: Linux (Debian or Ubuntu in our case)
- E: Nginx (Enginx actually)
- M: Mariadb (or Mysql if you love Or*cle so much)
- P: PHP, Python, or Perl (PHP in our case)

So not a big deal, we'll install Mariadb and PHP and connect them with  Nginx.

### 3.1. Install mariadb, php, and necessary dependancies.
- php-cli   : PHP client package
- php-fpm   : to run php as a cgi, nginx doesn't have a native support  
- php-mysql : for php to connect to mariadb

```
sudo apt install --yes mariadb-server php-cli php-fpm php-mysql
```

### 3.2. Update srv1-ssl Conf for PHP
```
sudo nano /etc/nginx/sites-available/srv1-ssl
```

Add the following part after the end of the location stanza.

```
   location ~ \.php$ {
      fastcgi_pass unix:/run/php/php-fpm.sock;
      include fastcgi.conf;
   }
```

Restart nginx

```
sudo systemctl restart nginx
```
 
### 3.3. Test it
We'll create a test database, a table in that database, add some rows to  the table on Mariadb. We will also create a test PHP file with the PHP  code to retrieve the data from the database and display it as HTML. 

#### 3.3.1. DB Operations
Connect to Mariadb shell

```
sudo mariadb
```

Create mysampledb database, connect to it, create a table, fill the  table, create a user with the access permission to that database and the  table.

**Run on Mariadb shell**

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

#### 3.3.2. Create Test PHP
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

Now go to below address to see if it is working:  
`https://srv1/test.php`

<br>
</details>

<details markdown='1'>
<summary>
4. Sample Configs
</summary>

---
### 4.1. Three Sites in One Conf File
srv2, srv3, and srv4 all have their directories and served in the same  server

```
server {
   listen 80;
   listen [::]:80;
   root /var/www/srv2;
   index index.html index.htm index.nginx-debian.html;
   server_name srv2;
   location / {
      try_files $uri $uri/ =404;
   }
}
server {
   listen 80;
   listen [::]:80;
   root /var/www/srv3;
   index index.html index.htm index.nginx-debian.html;
   server_name srv3;
   location / {
      try_files $uri $uri/ =404;
   }
}
server {
   listen 80;
   listen [::]:80;
   root /var/www/srv4;
   index index.html index.htm index.nginx-debian.html;
   server_name srv4;
   location / {
      try_files $uri $uri/ =404;
   }
}
```

### 4.2. Site Only Allowing 2 IPs to connect
```
server {
   listen 80;
   listen [::]:80;
   root /var/www/srv2;
   index index.html index.htm index.nginx-debian.html;
   server_name srv2;
   allow 192.168.1.108;
   allow 192.168.1.109;
   deny all;
   location / {
      try_files $uri $uri/ =404;
   }
}
```

### 4.3. IP Access Control on One Directory Only
Site is open to all IPs. Admin folder is restricted to 1 IP.

```
server {
   listen 80;
   listen [::]:80;
   root /var/www/srv2;
   index index.html index.htm index.nginx-debian.html;
   server_name srv2;
   deny all;
   location / {
      try_files $uri $uri/ =404;
   }
   location /admin {
      allow 192.168.1.108;
      deny all;
   }
}
```

### 4.4. Https Redirection with Certbot Access
Redirect to Https site except the certbot (Letsencrypt acme challenge)  accessing /.well-known/acme-challenge/. 

So that certbot can renew certificates by connecting to the Http site.

```
server {
   listen 80;
   listen [::]:80;
   index index.html index.htm index.nginx-debian.html;
   server_name srv1;
   location ^~ /.well-known/acme-challenge {
       allow all; 
       root /var/www/html;
   }
    location / {
       return 301 https://$host$request_uri;
    }
   server_tokens off;
}
```

<br>
</details>

<details markdown='1'>
<summary>
5. HTTPS With Free Let's Encrypt Certificates
</summary>

---
This section is performed on a VPS on internet. To get free Let's Encrypt certificates, our hostname must be in a DNS in internet. 

### 5.0. Specs
- Server   : Debian 12/11 or Ubuntu 24.04/22.04 LTS Server
- Hostname : 386387.xyz

Server is fresh install.

Remember to change all the occurences of 386387.xyz and www.386387.xyz with  your server names.

### 5.1. Install Nginx
```
sudo apt update
sudo apt install nginx --yes
```

### 5.2. Create ngensite and ngdissite scripts as in 1.3.
Refer to 1.3.

### 5.3. Disable default Site and Create a New One Named as x386387.xyz
```
ngdissite default
sudo nano /etc/nginx/sites-available/386387.xyz
```

Fill it as below

```
server {
   listen 80;
   listen [::]:80;
   root /var/www/386387.xyz;
   index index.html index.htm index.nginx-debian.html;
   server_name 386387.xyz www.386387.xyz;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Create /var/www/386387.xyz folder. Put some test HTMLs into it.

Enable the new conf

```
ngensite 386387.xyz
```

Reload nginx

```
sudo systemctl reload nginx
```

Your site is ready

### 5.4. Install certbot and Get a Free Certificate
Install certbot

```
sudo apt install certbot --yes
```

Run certbot to get certificates. For authentication method question;  select the option 2 (Place files ...), and enter root directory (/var/www/x11.xyz for my server).  Enter an email address and accept TOS.

```
sudo certbot certonly -d 386387.xyz -d www.386387.xyz
```

Certificates are installed to /etc/letsencrypt/live/386387.xyz/

Certificates will auto renew, you can check the process with:

```
sudo certbot renew --dry-run
```

### 5.5. Create a conf for the SSL site
```
sudo nano /etc/nginx/sites-available/386387.xyz-ssl
```

Fill as below:

```
server {
   listen 443 ssl;
   listen [::]:443 ssl;
   root /var/www/386387.xyz;
   index index.html index.htm index.nginx-debian.html;
   server_name x11.xyz www.x11.xyz;
   ssl_certificate /etc/letsencrypt/live/386387.xyz/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/386387.xyz/privkey.pem;
   ssl_session_timeout 5m;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Enable it

```
ngensite 386387.xyz-ssl
```

### 5.5. Update HTTP conf
Our http conf must redirect to https site with the exception of certbot  renew process

```
sudo nano /etc/nginx/sites-available/386387.xyz
```

Change as below

```
server {
   listen 80;
   listen [::]:80;
   index index.html index.htm index.nginx-debian.html;
   server_name 386387.xyz www.386387.xyz;
   location ^~ /.well-known/acme-challenge {
       allow all; 
       root /var/www/x11.xyz;
   }
    location / {
       return 301 https://$host$request_uri;
    }
   server_tokens off;
}
```

Reload Nginx

```
sudo systemctl reload nginx
```

Your HTTPS site is ready:

`https://386387.xyz/`

<br>
</details>

<details markdown='1'>
<summary>
6. Nginx and Apache Together
</summary>

---
**!!! This section starts with a fresh install server !!!**

Nginx is very good at static content, Apache is very good at dynamic  content. So we can use them together for the maximum performance.

### 6.0. Specs
- Nginx will run at port 80 and listen to the outside.
- Apache will run at port 8080 and listen to only inside. That is it can  be connected by only the localhost. So that only Nginx will listen to it.
- PHP and Mariadb will be connected to Apache only.
- All the HTML (and other static content) will be served by Nginx.
- All the PHP (and other dynamic content) will be served by Apache.

### 6.1. Install nginx And Reconfigure the Default Site
If you want, you may disable the default site and configure a new one too.

Install nginx

```
sudo apt update
sudo apt install nginx --yes
```

Backup default conf

```
sudo cp /etc/nginx/sites-available/{default,default.backup}
```

Update default conf

```
sudo nano /etc/nginx/sites-available/default
```

Fill as below

```
server {
   listen 80;
   listen [::]:80;
   server_name .386387.xyz;
   index index.html index.htm index.nginx-debian.html;
   root /var/www/html;
   location ~ \.php {
      proxy_pass http://127.0.0.1:8080;
   }
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Reload nginx

```
sudo systemctl reload nginx
```

### 6.2. Install apache2, php, mariadb, and dependencies
```
sudo apt install --yes apache2 php mariadb-server \
   libapache2-mod-php php-mysql
```

Apache doesn't start automatically, because port 80 is busy with nginx.

Change Apache's default listening port from 80 to 8080:

```
sudo nano /etc/apache2/ports.conf
```

Change the following line from: 

```
Listen 80
```

to as below:

```
Listen 8080
```

Update the default conf to listen to 8080 and only from local

```
sudo nano /etc/apache2/sites-available/000-default.conf
```

Change the first line from:

```
<VirtualHost *:80>
```

to as below:

```
<VirtualHost 127.0.0.1:8080>
```

Restart Apache

```
sudo systemctl restart apache2
```

You can test the combination using steps at 3.3.
</details>

