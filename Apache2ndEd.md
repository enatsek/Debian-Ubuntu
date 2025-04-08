##### Apache2ndEd
# Apache Tutorial for Debian and Ubuntu, 2nd Edition

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What
[ApacheOnDebianUbuntu](ApacheOnDebianUbuntu.html) was my very first tutorial. I was new to Linux, and I wanted to document Apache HTTP server usage. The old document will be available for some time, in case you'd like to check it too.

After some years, I've grown older and I decided to revise it. So here is the result.

Apache HTTPD is a very powerful web server software. Some sources tell that it is the most used web server software with Nginx.

### 0.1. Environment
I used Debian and Ubuntu server editions, namely Debian 11 & 12, Ubuntu 22.04 & 24.04 LTS Servers.

I have a test domain name: 386387.xyz. I used it for my tests. 

Unless you want to run a totally static website, you would need PHP and a database server too. So we're going to touch them a bit.

### 0.3. Sources

- [Apache Documentation](https://httpd.apache.org/docs/)  
- [Debian](https://manpages.debian.org/) and [Ubuntu](https://manpages.ubuntu.com/) manpages.
- [Deepseek](https://www.deepseek.com/) (I tested everything she says)
- [ChatGPT](https://chatgpt.com/) (I tested everything he says)

I guess at this point you realized that I declared Deepseek as female and ChatGPT as male. That doesn't mean anything, I just didn't want to call them as "it".
<br>
</details>

<details markdown="1">
<summary>
1. Installation and Configuration Files
</summary>

---
### 1.1. Installation
Upgrade repositories and install apache2 package

```
sudo apt update
sudo apt install apache2 --yes
```

When installed on Debian and Ubuntu, apache (as the other daemon packages) starts automatically. You can check the service:

```
systemctl status apache2
```

Debian package managers prepared a sample page for the web server. You can check it:

```
sudo nano /var/www/html/index.html
```

### 1.2. Configuration Files

Debian and Ubuntu installations have the following files and directories at /etc/apache2:

- **apache2.conf**: Main configuration file for the Apache web server. Contains global server settings and typically includes other configuration files.

- **envvars**: Sets environment variables used by Apache, such as paths and user/group settings. It is sourced (included) when Apache starts.

- **magic**: Helps Apache identify file types based on their content rather than just their extensions. It's used for MIME type detection.

- **ports.conf**: Defines the ports on which Apache listens (like port 80 for HTTP and 443 for HTTPS).

- **conf-available/**: Contains additional configuration files that can be enabled or disabled as needed. These are typically non-essential but provide extra features.

- **conf-enabled/**: Symbolic links to configuration files in conf-available/ that are currently enabled. Files here are active and loaded by Apache.

- **mods-available/**: Contains configuration files for Apache modules that can be enabled or disabled. These modules extend Apache's functionality (like SSL or PHP).

- **mods-enabled/**: Symbolic links to enabled module configurations from mods-available/. Only modules listed here are active.

- **sites-available/**: Contains configuration files for individual websites (virtual hosts). Each file defines settings like the document root, domain name, and logging for a specific site.

- **sites-enabled/**: Symbolic links to enabled site configurations from sites-available/. Only sites listed here are active and accessible.

Normally, we do not need to edit configuration files other than the ones in sites-available/. 

### 1.3. Debian Specific Apache Commands

Debian makes available of 6 commands for easy Apache configuration. These commands are prepared by Debian package managers and they are available on Ubuntu servers too.

- **a2ensite**: Enables a site configuration by creating a symbolic link in sites-enabled/ from sites-available/.

- **a2dissite**: Disables a site configuration by removing its symbolic link from sites-enabled/.

- **a2enmod**: Enables an Apache module by creating a symbolic link in mods-enabled/ from mods-available/.

- **a2dismod**: Disables an Apache module by removing its symbolic link from mods-enabled/.

- **a2enconf**: Enables additional configuration files from conf-available/ by creating symbolic links in conf-enabled/.

- **a2disconf**: Disables additional configuration files by removing symbolic links from conf-enabled/.

After enabling or disabling a site we need to reload apache2:

```
sudo systemctl reload apache2
```

After enabling or disabling a conf or a mod, we need to restart apache2:

```
sudo systemctl restart apache2
```

<br>
</details>

<details markdown="1">
<summary>
2. Creating Our First Website
</summary>

---
### 2.0. Explanations

When Apache package is installed, it creates 2 configuration files in sites-available/ directory. ```000-default.conf``` and ```default-ssl.conf```. 

000-default.conf comes enabled, that is linked to sites-enabled/ directory. 

default-ssl.conf is not enabled and can be considered as a template for configuring SSL sites.

There are 4 steps to create a web site on Apache Web Server.

1. Prepare a place for the website contents and put the contents in there. Generally, a directory under /var/www is fine.
2. Create a configuration file for the site in /etc/apache2/sites-available/
3. Enable the site with a2ensite command.
4. Reload Apache daemon.

### 2.1. Configure the Website
#### 2.1.1. Prepare Website Home
Make a home for our website:

```
sudo mkdir /var/www/386387.xyz
```

Create a sample home page

```
sudo nano /var/www/386387.xyz/index.html
```

Fill as below:

```
<html>
<title>386387.xyz Test Page</title>
<body>
<h1>386387.xyz Test Page</h1>
<p>386387.xyz and www.386387.xyz land here.</p>
</body>
</html>
```

Make Apache daemon user own the directory and files:

```
sudo chown -R www-data:www-data /var/www/386387.xyz
```

Change all directory permissions to 755 and file permissions to 644

```
sudo find /var/www/386387.xyz -type d -exec chmod 755 {} \;
sudo find /var/www/386387.xyz -type f -exec chmod 644 {} \;
```

### 2.1.2. Create Website Configuration 

Disable the default site configuration, we don't need it anymore

```
sudo a2dissite 000-default.conf
```

Create the configuration file of the site

```
sudo nano /etc/apache2/sites-available/386387.xyz.conf
```

Fill as below:

```
<VirtualHost *:80>
   ServerAdmin webmaster@386387.xyz	
   ServerName 386387.xyz
   ServerAlias www.386387.xyz
   DocumentRoot /var/www/386387.xyz
   ErrorLog ${APACHE_LOG_DIR}/386387.xyz-error.log
   CustomLog ${APACHE_LOG_DIR}/386387.xyz-access.log combined
</VirtualHost>
```

Line by line explanation of the configuration file

- Start of the site configuration. Site listens from all IPs in the host at the port 80.
- Site is accessible by name 386387.xyz
- Site is also accessible by name www.386387.xyz
- Content of the site is in /var/www/386387.xyz
- File for error logs
- File for access logs
- End of the site configuration

### 2.1.3. Enable the Website
Enable the site and reload Apache daemon.

```
sudo a2ensite 386387.xyz.conf
sudo systemctl reload apache2
```

Our site is ready. Assuming 386387.xyz points to the IP of the server, we can reach our site by reaching to the following URL:

```
http://386387.xyz
```

### 2.2. Add SSL (TLS) Support
#### 2.2.1. Install Certbot

Thanks to [Let's Encrypt](https://letsencrypt.org/) we can get free certificates and let our site to be connected by HTTPS. We use [certbot](https://certbot.eff.org/) tool to automatically install and update the certificates.

Let's Encrypt certificates last 3 months, they have to be renewed periodically. Certbot tool handles acquiring and renewing tasks.

Install certbot:

```
sudo apt update
sudo apt install certbot --yes
```

#### 2.2.2. Install Necessary Apache Modules

To enable HTTPS and forward our HTTP site to HTTPS, we need to enable 2 Apache modules:

```
sudo a2enmod ssl
sudo a2enmod rewrite
sudo systemctl restart apache2
```

#### 2.2.3.Get the Certificates

Get the certificates with certbot:

```
sudo certbot certonly -d 386387.xyz,www.386387.xyz --agree-tos --webroot
```

- **certonly**: Get the certificates only, do not install them
- **-d ...**: Get a certificate for all these domains
- **--agree-tos**: Accept the terms of services
- **--webroot**: Put challenge (authentication) files to a webroot folder. If you don't have a web server installed, then certbot may span a temporary web server to authenticate. But we already have 1 so we don't need it.


It asks for your email to inform you if needed and asks to share your email address with EFF, you can answer Y if you want. 

Then asks for the webroot directory of the domain, you can enter yours, mine is ```/var/www/386387.xyz```.

If you are getting a certificate for more than 1 domains like me, it asks for other's webroot too, you can select 2 as the other webroot.

Our certificates are installed as following:

```
Certificate is saved at: /etc/letsencrypt/live/386387.xyz/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/386387.xyz/privkey.pem
```

#### 2.2.4. Create HTTPS Site Configuration

Now we need to prepare a configuration for the HTTPS site.

```
sudo nano /etc/apache2/sites-available/386387.xyz-ssl.conf
```

Fill as below:

```
<VirtualHost *:443>
   ServerName 386387.xyz
   ServerAlias www.386387.xyz
   DocumentRoot /var/www/386387.xyz
   ErrorLog ${APACHE_LOG_DIR}/386387.xyz-error.log
   CustomLog ${APACHE_LOG_DIR}/386387.xyz-access.log combined
   SSLEngine on
   SSLCertificateFile /etc/letsencrypt/live/386387.xyz/fullchain.pem
   SSLCertificateKeyFile /etc/letsencrypt/live/386387.xyz/privkey.pem
</VirtualHost>
```

There are 3 unfamiliar lines starting with SSL, they say SSL is working and certificates are at the given paths.

Our HTTPS site is ready at ```https://386387.xyz```after we enable the new configuration and reload the Apache daemon:

```
sudo a2ensite 386387.xyz-ssl.conf
sudo systemctl reload apache2
```

#### 2.2.5. HTTP to HTTPS Redirection

Our site works as HTTPS, but there is one more work to do.

Whenever someone tries to connect to https://386387.xyz, they meet our HTTPS site. But if someone tries to connect to https://386387.xyz, they get to our plain HTTP site. 

We can redirect our HTTP site to HTTPS site to overcome this little problem.

Edit our HTTP site configuration:

```
sudo nano /etc/apache2/sites-available/386387.xyz.conf
```

Change as below :

```
<VirtualHost *:80>
   ServerAdmin webmaster@386387.xyz	
   ServerName 386387.xyz
   ServerAlias www.386387.xyz
   DocumentRoot /var/www/386387.xyz
   # Redirection BEGIN
   # Force redirect to HTTPS unless the request is for Let's Encrypt
   RewriteEngine On
   RewriteCond %{REQUEST_URI} !^/.well-known/acme-challenge/
   RewriteCond %{HTTPS} off
   RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301]
   # Redirection END
   ErrorLog ${APACHE_LOG_DIR}/386387.xyz-error.log
   CustomLog ${APACHE_LOG_DIR}/386387.xyz-access.log combined
</VirtualHost>
```

Certbot puts some files on .well-know/acme-challenge/ directory to authenticate the server. The lines we added redirects the other requests to the HTTPS site.

Reload the Apache daemon and we are (almost) done.

```
sudo systemctl reload apache2
```

### 2.2.6. Certbot Hooks

When the time comes, certbot renews the certificates. But Apache doesn't know that and tries to use the old ones. That means our HTTPS site does not work anymore. 

To handle this situation, we need to find a way to reload Apache when certbot renews the certificates.

Certbot runs all scripts in the  /etc/letsencrypt/renewal-hooks/deploy directory after a successfull renewal. We'll put a script there.

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/reloadapache.sh
```

Fill as below:

```
#!/bin/bash
systemctl reload apache2
```

Make the script executable

```
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reloadapache.sh
```
<br>
</details>

<details markdown="1">
<summary>
3. Adding More Sites to Our Server
</summary>

---
### 3.0. Explanations

Apache server can host many sites. Actually there is no limit on the number of the sites, you can add sites as much as your server's CPU and RAM allows.

We're going to add some more sites with different properties

- Local access only
- Only Accessible by 2 IPs
- Reverse proxy configuration
- Custom error pages
- Listening on a different port
- No access logs

There will be only HTTP configurations for these sites, you can add HTTPS access to them as in step 2.2.

### 3.1. Local Access Only
Our site will allow access only from the server, no other IP's will be able to access it.

These type of sites can be used for management purposes.

Create a home for the site, a sample HTML, configure permissions and ownerships.

```
sudo mkdir /var/www/srv1
sudo touch /var/www/srv1/index.html
sudo chown -R www-data:www-data /var/www/srv1
sudo find /var/www/srv1 -type d -exec chmod 755 {} \;
sudo find /var/www/srv1 -type f -exec chmod 644 {} \;
```

Fill sample HTML

```
sudo nano /var/www/srv1/index.html
```

Fill as below:

```
<html>
<title>srv1.386387.xyz Test Page</title>
<body>
<h1>srv1.386387.xyz Test Page</h1>
<p>Local access only</p>
</body>
</html>
```

Create configuration for the site

```
sudo nano /etc/apache2/sites-available/srv1.conf
```

Fill as below:

```
<VirtualHost 127.0.0.1:80>
   ServerAdmin admin@386387.xyz	
   ServerName srv1.386387.xyz
   DocumentRoot /var/www/srv1
   ErrorLog ${APACHE_LOG_DIR}/srv1-error.log
   CustomLog ${APACHE_LOG_DIR}/srv1-access.log combined
</VirtualHost>
```

Enable the site and reload Apache daemon

```
sudo a2ensite srv1.conf
sudo systemctl reload apache2
```

You will not be able to reach to the site at ```http://srv1.386387.xyz```, but if you run the following command on the server, it will retrieve the HTML:

```
curl 127.0.0.1
```

### 3.2. Only Accessible by 2 IPs
Only 2 given IPs will be able to access this site.

These type of sites can be used to serve to only some selected persons.

Create a home for the site, a sample HTML, configure permissions and ownerships.

```
sudo mkdir /var/www/srv2
sudo touch /var/www/srv2/index.html
sudo chown -R www-data:www-data /var/www/srv2
sudo find /var/www/srv2 -type d -exec chmod 755 {} \;
sudo find /var/www/srv2 -type f -exec chmod 644 {} \;
```

Fill sample HTML

```
sudo nano /var/www/srv2/index.html
```

Fill as below:

```
<html>
<title>srv2.386387.xyz Test Page</title>
<body>
<h1>srv2.386387.xyz Test Page</h1>
<p>Only 2 IPs can access.</p>
</body>
</html>
```

Create configuration for the site

```
sudo nano /etc/apache2/sites-available/srv2.conf
```

Fill as below:

```
<VirtualHost *:80>
    <Directory "/var/www/srv2">
        Require ip 195.174.44.28
        Require ip 138.199.28.46
    </Directory>
    ServerAdmin admin@386387.xyz
    ServerName srv2.386387.xyz
    DocumentRoot /var/www/srv2
    ErrorLog ${APACHE_LOG_DIR}/srv2-error.log
    CustomLog ${APACHE_LOG_DIR}/srv2-access.log combined
</VirtualHost>
```

Enable the site and reload Apache daemon

```
sudo a2ensite srv2.conf
sudo systemctl reload apache2
```

Only 2 given IPs will be able to access to the site, the other will have Forbidden message.

You can add more IPs or even IP blocks as following:

```
        Require ip 195.174.44.0/24
```

### 3.3. Reverse Proxy Configuration

Some softwares supply locally running mini web servers. One of them is RSpamd. You can only access them from the server they are running.

Using Apache's Reverse Proxy module, we can access them from outside the server too.

We can simulate such a system, open another terminal window on your server and type the following commands, that terminal will stay busy:

```
mkdir /tmp/test
echo Test > /tmp/test/index.html
cd /tmp/test
python3 -m http.server 8080 --bind 127.0.0.1
```

Now if you run the following command on another terminal for your server:

```
curl 127.0.0.1:8080
```

You will see it is replying with Test

This mini server can be accessed from our server only, and we'll make it accessible from the world too.

First we need to enable proxy and proxy_http modules of Apache

```
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart apache2
```

Create a configuration for the site

```
sudo nano /etc/apache2/sites-available/srv3.conf
```

Fill as below:

```
<VirtualHost *:80>
   ServerAdmin admin@386387.xyz
   ServerName srv3.386387.xyz
   ProxyPreserveHost On
   ProxyPass "/reverse" "http://127.0.0.1:8080/"
   ProxyPassReverse "/reverse"  "http://127.0.0.1:8080/"
   ErrorLog ${APACHE_LOG_DIR}/srv3-error.log
   CustomLog ${APACHE_LOG_DIR}/srv3-access.log combined
</VirtualHost>
```

Enable the site and reload Apache daemon

```
sudo a2ensite srv3.conf
sudo systemctl reload apache2
```

Now, when you browse ```http://srv3.386387.xyz/reverse``` you will access to the local server.

Remember terminating the local server at the other terminal.

### 3.4. Custom Error Pages

When there is an error, Apache server inform us with an error page. The most occuring error is 404, page not found. But there are other errors too.

We can change the error pages as we like. Let's try it.

Create a home for the site, a sample HTML, 404 error page HTML, configure permissions and ownerships.

```
sudo mkdir /var/www/srv4
sudo touch /var/www/srv4/index.html
sudo touch /var/www/srv4/404.html
sudo chown -R www-data:www-data /var/www/srv4
sudo find /var/www/srv4 -type d -exec chmod 755 {} \;
sudo find /var/www/srv4 -type f -exec chmod 644 {} \;
```

Fill sample HTML

```
sudo nano /var/www/srv4/index.html
```

Fill as below:

```
<html>
<title>srv4.386387.xyz Test Page</title>
<body>
<h1>srv4.386387.xyz Test Page</h1>
<p>This site has a modified error 404 page.</p>
</body>
</html>
```

Fill error page HTML

```
sudo nano /var/www/srv4/404.html
```

Fill as below:

```
<html>
<title>I cannot find the page</title>
<body>
<h1>I cannot find the page</h1>
<p>May I ask you to change the address you're browsing?</p>
</body>
</html>
```

Create a configuration for the site

```
sudo nano /etc/apache2/sites-available/srv4.conf
```

Fill as below:

```
<VirtualHost *:80>
    ServerAdmin admin@386387.xyz
    ServerName srv4.386387.xyz
    DocumentRoot /var/www/srv4
    ErrorDocument 404 /404.html
    # You can add more error codes and HTMLs here
    ErrorLog ${APACHE_LOG_DIR}/srv4-error.log
    CustomLog ${APACHE_LOG_DIR}/srv4-access.log combined
</VirtualHost>
```

Enable the site and reload Apache daemon

```
sudo a2ensite srv4.conf
sudo systemctl reload apache2
```

When you visit ```http://srv4.386387.xyz``` you can see the main page, visit ```http://srv4.386387/test``` to see the custom error page.

### 3.5. Listening on a Different Port

Normally web servers listen on ports 80 (HTTP) and 443 (HTTPS). But sometimes it might be necessary to use the other ports.

We are going to configure our server to listen on port 8080.

Before everything we have to tell the Apache server to listen on port 8080 too.

```
sudo nano /etc/apache2/ports.conf
```

Add to the end of the file:

```
Listen 8080
```

Apache restart required

```
sudo systemctl restart apache2
```

Create a home for the site, a sample HTML, configure permissions and ownerships.

```
sudo mkdir /var/www/srv5
sudo touch /var/www/srv5/index.html
sudo chown -R www-data:www-data /var/www/srv5
sudo find /var/www/srv5 -type d -exec chmod 755 {} \;
sudo find /var/www/srv5 -type f -exec chmod 644 {} \;
```

Fill sample HTML

```
sudo nano /var/www/srv5/index.html
```

Fill as below:

```
<html>
<title>srv5.386387.xyz Test Page</title>
<body>
<h1>srv5.386387.xyz Test Page</h1>
<p>This site listens on port 8080.</p>
</body>
</html>
```

Create a configuration for the site

```
sudo nano /etc/apache2/sites-available/srv5.conf
```

Fill as below:

```
<VirtualHost *:8080>
    ServerAdmin admin@386387.xyz
    ServerName srv5.386387.xyz
    DocumentRoot /var/www/srv5
    ErrorLog ${APACHE_LOG_DIR}/srv5-error.log
    CustomLog ${APACHE_LOG_DIR}/srv4-access.log combined
</VirtualHost>
```

Enable the site and reload Apache daemon

```
sudo a2ensite srv5.conf
sudo systemctl reload apache2
```

Now you can visit ```http://srv5.386387.xyz:8080``` to see our new site.

### 3.6. No Access Logs

We want our site to have no access logs. There might be a lot of reason for that. One reason that comes to my mind is privacy. 

Create a home for the site, a sample HTML, configure permissions and ownerships.

```
sudo mkdir /var/www/srv6
sudo touch /var/www/srv6/index.html
sudo chown -R www-data:www-data /var/www/srv5
sudo find /var/www/srv6 -type d -exec chmod 755 {} \;
sudo find /var/www/srv6 -type f -exec chmod 644 {} \;
```

Fill sample HTML

```
sudo nano /var/www/srv6/index.html
```

Fill as below:

```
<html>
<title>srv6.386387.xyz Test Page</title>
<body>
<h1>srv6.386387.xyz Test Page</h1>
<p>We do not collect access logs.</p>
</body>
</html>
```

Create a configuration for the site

```
sudo nano /etc/apache2/sites-available/srv6.conf
```

Fill as below:

```
<VirtualHost *:80>
    ServerAdmin admin@386387.xyz
    ServerName srv6.386387.xyz
    DocumentRoot /var/www/srv6
    ErrorLog ${APACHE_LOG_DIR}/srv6-error.log
    CustomLog /dev/null combined
</VirtualHost>
```

Enable the site and reload Apache daemon

```
sudo a2ensite srv6.conf
sudo systemctl reload apache2
```

Now you can visit ```http://srv6.386387.xyz``` to see our new site.

If you want to disable error logs too, you can change the following line in the site config: 

```
    ErrorLog ${APACHE_LOG_DIR}/srv6-error.log
```

as

```
    ErrorLog /dev/null
```

<br>
</details>



<details markdown="1">
<summary>
4. Adding PHP Support to Apache
</summary>

---

### 4.1. Install PHP and Apache Dependencies

```
sudo apt update
sudo apt install php libapache2-mod-php --yes
```

Let's use our srv4 site to check PHP. We're going to add a page with PHP content and check if it is working.

```
sudo nano /var/www/srv4/info.php
```

Fill as below:

```
<?php phpinfo(); ?>
```

Now you can visit ```http://srv4.386387.xyz/info.php``` to see the PHP content.

### 4.2. PHP Configuration

You may want to make some changes to the PHP configuration. You can edit the configurations:

```
sudo nano /etc/php/*/apache2/php.ini
```

Common settings to adjust would be:

```
upload_max_filesize = 16M
post_max_size = 16M
memory_limit = 128M
display_errors = Off  # Set to On for development
```

After making changes you need to restart Apache:

```
sudo systemctl restart apache2
```

### 4.3. Additional PHP Packages

- php-mysql: Connect to MySQL/MariaDB databases
- php-pgsql: Connect to PostgreSQL databases
- php-sqlite3: Lightweight SQLite database support
- php-json: Encode/decode JSON data
- php-xml: Parse/generate XML
- php-mbstring: Handle non-English characters (e.g., UTF-8)
- php-curl: Make HTTP requests to APIs
- php-opcache: (Essential) Caches PHP code for faster execution
- php-zip: Create/extract ZIP files
- php-gd: Process images (resize, crop, add watermarks)

To install them all (and restart Apache afterwards):

```
sudo apt install php-mysql php-pgsql php-sqlite3 php-json \
   php-xml php-mbstring php-curl php-opcache php-zip php-gd
sudo systemctl restart apache2
```

<br>
</details>


