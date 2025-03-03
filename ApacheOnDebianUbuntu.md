##### ApacheOnDebianUbuntu
# Apache 2 Tutorial on Debian and Ubuntu 


<details markdown="1">
<summary>
0. Specs
</summary>
---
Apache 2 Installation, configuration, sample sites, enablement of PHP,  SSL etc on Ubuntu 24.04 (and 22.04) and Debian 12 (and 11) Servers 

Based on the book [Mastering Ubuntu Server 2nd Ed.](https://www.packtpub.com/networking-and-servers/mastering-ubuntu-server-second-edition) by Jay LaCroix. This book hes introduced me to Ubuntu Server and I have to thank him for this excellent book. 

srv1.386387.xyz, srv2.386387.xyz and srv3.386387.xyz all have the ip of my server
</details>

<details markdown="1">
<summary>
1. Apache Installation
</summary>
---
### 1.1. Install
```
sudo apt update
sudo apt install apache2 --yes
```

### 1.2. Check status

It must be working with the test page

```
systemctl status apache2
```

### 1.3. Default document root
```
sudo nano /var/www/html/index.html
```

### 1.4. Configuration Files

Configuration files for different sites exist as .conf files in /etc/apache2/sites-available directory

### 1.5. Main Apache2 config file
```
sudo nano /etc/apache2/apache2.conf
```

### 1.6. All available sites are in

/etc/apache2/sites-available

```
sudo nano /etc/apache2/sites-available/000-default.conf
```

### 1.7. Creating Virtual Hosts

For virtual hosts we need to create a new conf as say 000-virtual-hosts.conf

```
sudo nano /etc/apache2/sites-available/000-virtual-hosts.conf
```

Sample content for 2 virtual hosts

```
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv1.386387.xyz
    ServerAlias srv1
    DocumentRoot /var/www/srv1
    ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1.386387.xyz-access.log combined
</VirtualHost>
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv2.386387.xyz
    ServerAlias srv2
    DocumentRoot /var/www/srv2
    ErrorLog ${APACHE_LOG_DIR}/srv2.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv2.386387.xyz-access.log combined
</VirtualHost>
```

### 1.8. We need to enable the new conf to make it active
```
sudo a2ensite 000-virtual-hosts.conf
```

We can disable it again whenever we want

```
sudo a2dissite 000-virtual-hosts.conf
```

We need to reload Apache whenever we enable or disable a site

```
sudo systemctl reload apache2
```

Remember to copy sites' pages on DocumentRoot Directories: create /var/www/srv1 and /var/www/srv2 and fill them with htmls

<br>
</details>

<details markdown="1">
<summary>
2. Apache Additional Modules
</summary>
---
## 2.1. List of Apache modules
```
apt search libapache2-mod
```

### 2.2. Modules must be enabled by a2enmod after installing
then can be disabled by a2dismod

### 2.3. List of build-in modules of Apache2
```
sudo apache2 -l
```
Sudo is necessary for Debian

### 2.4. All installed and ready to be enabled modules
```
sudo a2enmod
```

### 2.5. Enable proxy module
```
sudo a2enmod proxy
```

### 2.6. Disable proxy module
```
sudo a2dismod proxy
```

### 2.7. Remember to restart Apache after enabling or disabling a module
```
sudo systemctl restart apache2
```

<br>
</details>

<details markdown="1">
<summary>
3. Adding SSL to Apache
</summary>
---
### 3.1. Enable ssl
```
sudo a2enmod ssl
```

### 3.2. Apache restart needed
```
sudo systemctl restart apache2
```

### 3.3. Makeup a place for certificates
```
sudo mkdir /etc/apache2/certs
```

### 3.4. Create self signed certificate files for srv1
```
sudo openssl req -x509 -nodes -days 730 -newkey rsa:2048 -keyout \
   /etc/apache2/certs/srv1.key -out /etc/apache2/certs/srv1.crt
```

You need to answer all the questions, default values OK for a test site

### 3.5. To get a formal certificate create a certificate signing request
```
sudo openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr
```

### 3.6. Create a conf file for the ssl site
```
sudo nano /etc/apache2/sites-available/000-virtual-ssl.conf
```

Fill as below:

```
<IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerName srv1.386387.xyz:443
        ServerAdmin webmaster@386387.xyz
        DocumentRoot /var/www/srv1
        ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
        CustomLog ${APACHE_LOG_DIR}/srv.386387.xyz-access.log combined
        SSLEngine on
        SSLCertificateFile	/etc/apache2/certs/srv1.crt
        SSLCertificateKeyFile	/etc/apache2/certs/srv1.key
        <FilesMatch ".(cgi|shtml|phtml|php)$">
            SSLOptions +StdEnvVars
    </FilesMatch>
    <Directory /usr/lib/cgi-bin>
        SSLOptions +StdEnvVars
    </Directory>
    </VirtualHost>
</IfModule>
```

### 3.7. Enable new ssl site
```
sudo a2ensite 000-virtual-ssl.conf
```

### 3.8. Reload apache - SSL Site is ready
Please consider, your browser will give an error/warning message because the certificate is self signed.

```
sudo systemctl reload apache2
```

<br>
</details>

<details markdown="1">
<summary>
4. Auto http-->https Redirect
</summary>
---
### 4.1. http://srv1.386387.xyz automatically redirects to https://srv1.386387.xyz

First we need to enable rewrite mode

```
sudo a2enmod rewrite.load
```

### 4.2. Modify conf file of the site to redirect 
```
sudo nano /etc/apache2/sites-available/000-virtual-hosts.conf
```

last 3 lines to be added

```
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    ErrorLog ${APACHE_LOG_DIR}/srv1-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1-access.log combined
    #redirection
    RewriteEngine on
    RewriteCond %{SERVER_NAME} =srv1.386387.xyz
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
```

### 4.3. Restart apache
```
sudo systemctl restart apache2
```

<br>
</details>

<details markdown="1">
<summary>
5. Enable PHP on Apache2
</summary>
---
### 5.1. Install php and apache php mod
```
sudo apt install php libapache2-mod-php
```

### 5.2. Install php extension if you have mysql - mariadb
```
sudo apt install php-mysql
```

Restart apache

```
sudo systemctl restart apache2
```

Create a test file for PHP

```
sudo nano /var/www/srv1/info.php
```

Fill as below:

```
<?php
phpinfo();
```

Test your page 
http://srv1.386387.xyz/info.php

<br>
</details>

<details markdown="1">
<summary>
6. Some Sample Apache Confs
</summary>
---
### 6.1. 3 different sites on 1 server in 1 conf file
```
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1.386387.xyz-access.log combined
</VirtualHost>

<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv2.386387.xyz
    DocumentRoot /var/www/srv2
    ErrorLog ${APACHE_LOG_DIR}/srv2.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv2.386387.xyz-access.log combined
</VirtualHost>

<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv3.386387.xyz
    DocumentRoot /var/www/srv3
    ErrorLog ${APACHE_LOG_DIR}/srv3.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv3.386387.xyz-access.log combined
</VirtualHost>
```

### 6.2. A server with only local access, to be used for configuration
```
<VirtualHost 127.0.0.1:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv3.386387.xyz
    DocumentRoot /var/www/localhost
    ErrorLog ${APACHE_LOG_DIR}/localhost-error.log
    CustomLog ${APACHE_LOG_DIR}/localhost-access.log combined
</VirtualHost>
```

### 6.3. This server allows letsencrypt's acme challenge
Otherwise redirects to https. You are going to need to enable rewrite module with:

```
sudo a2enmod rewrite
```

```
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    # Force redirect to HTTPS unless the request is for Let's Encrypt
    RewriteEngine On
    RewriteCond %{REQUEST_URI} !^/.well-known/acme-challenge/
    RewriteCond %{HTTPS} off
    RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301]
    <Directory "/var/www/srv1">
        Options None
        AllowOverride None
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/public_unencrypted.error.log
</VirtualHost>
```

### 6.4. A site with auto https redirection. 
Rewrite module is needed again.

```
<VirtualHost *:80>
   ServerAdmin webmaster@386387.xyz	
   ServerName srv1.386387.xyz
   ServerAlias www.386387.xyz
   DocumentRoot /var/www/srv1
   ErrorLog ${APACHE_LOG_DIR}/srv1-error.log
   CustomLog ${APACHE_LOG_DIR}/srv1-access.log combined
   RewriteEngine on
   RewriteCond %{SERVER_NAME} =srv1.386387.xyz [OR]
   RewriteCond %{SERVER_NAME} =www.386387.xyz
   RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
```

### 6.5. A site only allowing 2 IPs to connect, all others are refused
```
<VirtualHost *:80>
    <Directory "/var/www/srv1">
        Require ip 195.174.209.24
        Require ip 138.199.28.46
    </Directory>
    ServerAdmin postmaster@386387.xyz
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    ErrorLog ${APACHE_LOG_DIR}/srv1-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1-access.log combined
</VirtualHost>
```


### 6.6. Reverse Proxy Configuration
Assume that we have a program on server which runs a web server, serving   some content at some specific port and only allows connections from    localhost. That means, we cannot access it from other computers.

Apache allows us using it as a reverse proxy. That way we can connect that web server using apache.  
Rspamd is a good example of that kind of a program. It runs a web server at port 11334, and only allows connections from the computer itself.

We need to enable 2 Apache mods for the configuration:

```
a2enmod proxy_http
a2enmod rewrite
```

And our configuration:

```
<VirtualHost *:80>
    <Location /reverse>
        Require all granted
    </Location>
    RewriteEngine On
    RewriteRule ^/reverse$ /reverse/ [R,L]
    RewriteRule ^/reverse/(.*) http://localhost:11334/$1 [P,L]
    ServerAdmin webmaster@386387.xyz
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    ErrorLog ${APACHE_LOG_DIR}/srv1-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1-access.log combined
</VirtualHost>
```

<br>
</details>

<details markdown="1">
<summary>
7. Free SSL Certificates
</summary>
---
You can use free, autorenewing SSL certificates from <https://letsencrypt.org/> with Certbot tool from EFF. 

Check it out at my [CertbotOnDebianUbuntu](CertbotOnDebianUbuntu.html)  Tutorial.
</details>
