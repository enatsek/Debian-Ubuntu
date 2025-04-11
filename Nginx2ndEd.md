##### Nginx2ndEd
# Nginx Tutorial for Debian and Ubuntu, 2nd Edition

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What
It's been some time after I prepared [NginxOnDebianUbuntu](NginxOnDebianUbuntu.html) tutorial. I decided to revise it with a new perspective. The old document will be available for some time, in case you'd like to check it too.

Nginx is a very powerful web server software. Some sources tell that it is one of the most used web server software with Apache.

### 0.1. Environment
I used Debian and Ubuntu server editions, namely Debian 11 & 12, Ubuntu 22.04 & 24.04 LTS Servers.

I have a test domain name: 386387.xyz. I used it for my tests. 

Unless you want to run a totally static website, you would need PHP and a database server too. So we're going to touch them a bit.

All the following domain names points to my test server:

- 386387.xyz
- www.386387.xyz
- srv1.386387.xyz
- srv2.386387.xyz
- srv3.386387.xyz
- srv4.386387.xyz
- srv5.386387.xyz
- srv6.386387.xyz

### 0.2. Sources

- [nginx.org](https://nginx.org/en/docs/)  
- [www.geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-retrieve-data-from-mysql-database-using-php/)  
- [Deepseek](https://www.deepseek.com/)   
- [ChatGPT](https://chatgpt.com/) 

<br>
</details>

<details markdown="1">
<summary>
1. Installation and Configuration Files
</summary>

---
### 1.1. Installation
Upgrade repositories and install nginx package

```
sudo apt update
sudo apt install nginx --yes
```

When installed on Debian and Ubuntu, nginx (as the other daemon packages) starts automatically. You can check the service:

```
systemctl status nginx
```

Debian package maintainers prepared a sample page for the web server. You can check it:

```
sudo nano /var/www/html/index.nginx-debian.html
```

### 1.2. Configuration Files

Debian and Ubuntu installations have the following files and directories at /etc/nginx:

- **fastcgi.conf**: Contains default settings for FastCGI applications.
- **fastcgi_params**: Similar to fastcgi.conf, it defines FastCGI parameters but is more minimal. Some configurations use one or the other.
- **koi-utf**: Charset conversion maps for KOI8-R (Cyrillic encoding) to UTF-8. 
- **koi-win**: Charset conversion maps for KOI8-R (Cyrillic encoding) to Windows-1251.
- **mime.types**: Defines the mapping of file extensions to MIME types.
- **nginx.conf**: The main Nginx configuration file that includes global settings and loads other configurations.
- **proxy_params**: Contains default settings for reverse proxying requests to another server.
- **scgi_params**: Configuration parameters for handling SCGI (Simple Common Gateway Interface) requests.
- **uwsgi_params**: Defines parameters for uWSGI applications (commonly used for Python web apps).
- **win-utf**: Charset conversion map for Windows-1251 encoding.
- **conf.d/**: Stores additional Nginx configuration files that are automatically loaded. Empty on default installations.
- **modules-available/**: Contains configuration files for optional Nginx modules that can be enabled or disabled. Empty on default installations.
- **modules-enabled/**: Symbolic links to active modules from modules-available/. Empty on default installations.
- **sites-available/**: Stores virtual host configurations for different websites (like Apache’s sites-available).
- **sites-enabled/**: Contains symbolic links to active virtual host configurations from sites-available/.
- **snippets/**: Stores reusable configuration fragments that can be included in other config files (e.g., SSL settings).

Normally, we do not need to edit configuration files other than the ones in sites-available/.

### 1.3. Scripts for Enabling & Disabling Sites & Modules

If you used Apache Web Server you would remember there are commands like a2ensite, a2dissite, a2enmod, a2dismod. They are used to enable/disable sites and modules.

With the help of ChatGPT, I prepared Nginx counterparts of these commands as nxensite, nxdissite, nxenmod, and nxdismod.

#### 1.3.1. nxensite Enable a Site

This script is expected to enable a site configuration by creating a symbolic link in sites-enabled/ from sites-available/.

Let's create it:

```
sudo nano /usr/local/bin/nxensite
```

Fill as below:

```
#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: nxensite <site-name>"
    exit 1
fi

SITE="/etc/nginx/sites-available/$1"
LINK="/etc/nginx/sites-enabled/$1"

if [ ! -f "$SITE" ]; then
    echo "Site configuration '$1' does not exist in sites-available."
    exit 1
fi

ln -s "$SITE" "$LINK"
echo "Enabled site: $1"
```

Make it executable:

```
sudo chmod +x /usr/local/bin/nxensite
```

It is necessary to reload nginx after enabling a site:

```
sudo systemctl reload nginx
```

#### 1.3.2. nxdissite Disable a Site

This script is expected to disable a site configuration by removing its symbolic link from sites-enabled/.

Let's create it:

```
sudo nano /usr/local/bin/nxdissite
```

Fill as below:

```
#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: nxdissite <site-name>"
    exit 1
fi

LINK="/etc/nginx/sites-enabled/$1"

if [ ! -L "$LINK" ]; then
    echo "Site '$1' is not enabled."
    exit 1
fi

rm "$LINK"
echo "Disabled site: $1"
```


Make it executable:

```
sudo chmod +x /usr/local/bin/nxdissite
```

It is necessary to reload nginx after disabling a site:

```
sudo systemctl reload nginx
```

#### 1.3.3. nxenmod Enable a Module

This script is expected to enable a module by creating a symbolic link in mods-enabled/ from mods-available/.

Let's create it:

```
sudo nano /usr/local/bin/nxenmod
```

Fill as below:

```
#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: nxenmod <module-name>"
    exit 1
fi

MOD="/etc/nginx/modules-available/$1.conf"
LINK="/etc/nginx/modules-enabled/$1.conf"

if [ ! -f "$MOD" ]; then
    echo "Module configuration '$1.conf' does not exist in modules-available."
    exit 1
fi

ln -s "$MOD" "$LINK"
echo "Enabled module: $1"
```

Make it executable:

```
sudo chmod +x /usr/local/bin/nxenmod
```

It is necessary to restart nginx after enabling a module:

```
sudo systemctl restart nginx
```

#### 1.3.4. nxdismod Disable a Module

This script is expected to disable a module by removing its symbolic link from mods-enabled/.

Let's create it:

```
sudo nano /usr/local/bin/nxdismod
```

Fill as below:

```
#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: nxdismod <module-name>"
    exit 1
fi

LINK="/etc/nginx/modules-enabled/$1.conf"

if [ ! -L "$LINK" ]; then
    echo "Module '$1' is not enabled."
    exit 1
fi

rm "$LINK"
echo "Disabled module: $1"
```

Make it executable:

```
sudo chmod +x /usr/local/bin/nxdismod
```

It is necessary to restart nginx after disabling a module:

```
sudo systemctl restart nginx
```

<br>
</details>

<details markdown="1">
<summary>
2. Creating Our First Website
</summary>

---
### 2.0. Explanations

When Nginx is installed, it creates a configuraiton file in sites-available/ directory with the name default. 

Configuration file default comes enabled, that is linked to sites-enabled/ directory. 

Like Apache, there are 4 steps to create a web site on Nginx Web Server.

1. Prepare a place for the website contents and put the contents in there. Generally, a directory under /var/www is fine.
2. Create a configuration file for the site in /etc/nginx/sites-available/
3. Enable the site with nx2ensite command (or by just linking it to /etc/nginx/sites-enabled/ directory yourself).
4. Reload Nginx daemon.

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

Make Nginx daemon user own the directory and files:

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
sudo nxdissite default
```

Create the configuration file of the site

```
sudo nano /etc/nginx/sites-available/386387.xyz
```

Fill as below:

```
server {
   listen 80;
   listen [::]:80;
   root /var/www/386387.xyz;
   index index.html index.htm;
   server_name 386387.xyz www.386387.xyz;
   access_log /var/log/nginx/386387.xyz.access.log;
   error_log /var/log/nginx/386387.xyz.error.log;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Line by line explanation of the configuration file

- Start of the site configuration. 
- Listen IP version 4 at port 80.
- Listen IP version 6 at port 80.
- Root directory is /var/www/x386387.xyz.
- Index file (default file) is one of the followings in order.
- Server names are 386387.xyz and www.386387.xyz.
- Access log is: /var/log/nginx/386387.xyz.access.log
- Error log is: /var/log/nginx/386387.xyz.error.log
- For the location in root (and subfolders), try the given name as a file, then as a folder, if can't find, send 404 error message.
- Don't display server version at error (and other) messages.
- End of the site configuration.

### 2.1.3. Enable the Website
Enable the site and reload Nginx daemon.

```
sudo nxensite 386387.xyz
sudo systemctl reload nginx
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

#### 2.2.2.Get the Certificates

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

#### 2.2.3. Create HTTPS Site Configuration

Now we need to prepare a configuration for the HTTPS site.

```
sudo nano /etc/nginx/sites-available/386387.xyz-ssl
```

Fill as below:

```
server {
   listen 443 ssl;
   listen [::]:443 ssl;
   root /var/www/386387.xyz;
   index index.html index.htm;
   server_name 386387.xyz www.386387.xyz;
   access_log /var/log/nginx/386387.xyz.access.log;
   error_log /var/log/nginx/386387.xyz.error.log;
   ssl_certificate /etc/letsencrypt/live/386387.xyz/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/386387.xyz/privkey.pem;
   ssl_session_timeout 5m;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

There are 3 unfamiliar lines starting with ssl, they say SSL certificates are at the given paths and session timeout is 5 minutes.

Our HTTPS site is ready at ```https://386387.xyz```after we enable the new configuration and reload the Nginx daemon:

```
sudo nxensite 386387.xyz-ssl
sudo systemctl reload nginx
```

#### 2.2.4. HTTP to HTTPS Redirection

Our site works as HTTPS, but there is one more work to do.

Whenever someone tries to connect to https://386387.xyz, they meet our HTTPS site. But if someone tries to connect to http://386387.xyz, they get to our plain HTTP site. 

We can redirect our HTTP site to HTTPS site to overcome this little problem.

Edit our HTTP site configuration:

```
sudo nano /etc/nginx/sites-available/386387.xyz
```

Change as below :

```
server {
   listen 80;
   listen [::]:80;
   index index.html index.htm;
   server_name 386387.xyz www.386387.xyz;
   access_log /var/log/nginx/386387.xyz.access.log;
   error_log /var/log/nginx/386387.xyz.error.log;
   location ^~ /.well-known/acme-challenge {
       allow all; 
       root /var/www/386387.xyz;
   }
    location / {
       return 301 https://$host$request_uri;
    }   server_tokens off;
}
```

Certbot puts some files on .well-know/acme-challenge/ directory to authenticate the server. The lines we added redirects the other requests to the HTTPS site.

Reload the Nginx daemon and we are (almost) done.

```
sudo systemctl reload nginx
```


### 2.2.5. Certbot Hooks

When the time comes, certbot renews the certificates. But Nginx doesn't know that and tries to use the old ones. That means our HTTPS site does not work anymore. 

To handle this situation, we need to find a way to reload Nginx when certbot renews the certificates.

Certbot runs all scripts in the  /etc/letsencrypt/renewal-hooks/deploy directory after a successfull renewal. We'll put a script there.

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/reloadnginx.sh
```

Fill as below:

```
#!/bin/bash
systemctl reload nginx
```

Make the script executable

```
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reloadnginx.sh
```
<br>
</details>

<details markdown="1">
<summary>
3. Adding More Sites to Our Server
</summary>

---
### 3.0. Explanations

Nginx server can host many sites. Actually there is no limit on the number of the sites, you can add sites as much as your server's CPU and RAM allows.

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
sudo nano /etc/nginx/sites-available/srv1
```

```
server {
   listen 127.0.0.1:80;
   root /var/www/srv1;
   index index.html index.htm;
   server_name srv1.386387.xyz;
   access_log /var/log/nginx/srv1.access.log;
   error_log /var/log/nginx/srv1.error.log;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Enable the site and reload Nginx daemon

```
sudo nxensite srv1
sudo systemctl reload nginx
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
sudo nano /etc/nginx/sites-available/srv2
```

Fill as below:

```
server {
   listen 80;
   root /var/www/srv2;
   index index.html index.htm;
   server_name srv2.386387.xyz;
   allow 195.174.44.28;
   allow 138.199.28.46;
   deny all;
   location / {
      try_files $uri $uri/ =404;
   }
}
```

Enable the site and reload Nginx daemon

```
sudo nxensite srv2
sudo systemctl reload nginx
```

Only 2 given IPs will be able to access to the site ```http://srv2.386387.xyz```, the others will have Forbidden message.

You can add more IPs or even IP blocks as following:

```
      allow 195.174.44.0/24;
```

### 3.3. Reverse Proxy Configuration

Some software supplies locally running mini web servers. One of them is RSpamd. You can only access them from the server they are running.

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

Create a configuration for the site

```
sudo nano /etc/nginx/sites-available/srv3
```

Fill as below:

```
server {
   listen 80;
   server_name srv3.386387.xyz;
   access_log /var/log/nginx/srv3.access.log;
   error_log /var/log/nginx/srv3.error.log;
   location / {
        proxy_pass         http://127.0.0.1:8080;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
    }
}
```

Enable the site and reload Nginx daemon

```
sudo nxensite srv3
sudo systemctl reload nginx
```

Now, when you browse ```http://srv3.386387.xyz/``` you will access to the local server.

Remember terminating the local server at the other terminal.


### 3.4. Custom Error Pages

When there is an error, Nginx server inform us with an error page. The most occuring error is 404, page not found. But there are other errors too.

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
sudo nano /etc/nginx/sites-available/srv4
```

Fill as below:

```
server {
   listen 80;
   listen [::]:80;
   root /var/www/srv4;
   index index.html index.htm;
   server_name srv4.386387.xyz;
   access_log /var/log/nginx/srv4.access.log;
   error_log /var/log/nginx/srv4.error.log;
   error_page 404 /404.html;
   # internal directive makes those files can’t be accessed directly by users.
   location = /errors/404.html {
        internal;
   }
   server_tokens off;
}
```

Enable the site and reload Apache daemon

```
sudo nxensite srv4
sudo systemctl reload nginx
```

When you visit ```http://srv4.386387.xyz``` you can see the main page, visit ```http://srv4.386387/test``` to see the custom error page.

### 3.5. Listening on a Different Port

Normally web servers listen on ports 80 (HTTP) and 443 (HTTPS). But sometimes it might be necessary to use the other ports.

We are going to configure our server to listen on port 8080.

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
sudo nano /etc/nginx/sites-available/srv5
```

Fill as below:

```
server {
   listen 8080;
   root /var/www/srv5;
   index index.html index.htm;
   server_name srv5.386387.xyz;
   access_log /var/log/nginx/srv5.access.log;
   error_log /var/log/nginx/srv5.error.log;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Enable the site and reload Nginx daemon

```
sudo nxensite srv5
sudo systemctl reload nginx
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
sudo nano /etc/nginx/sites-available/srv6
```

Fill as below:

```
server {
   listen 80;
   root /var/www/srv6;
   index index.html index.htm;
   server_name srv6.386387.xyz;
   access_log off;
   error_log /var/log/nginx/srv6.error.log;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```


Enable the site and reload Nginx daemon

```
sudo nxensite srv6
sudo systemctl reload nginx
```

Now you can visit ```http://srv6.386387.xyz``` to see our new site.

If you want to disable error logs too, you can change the following line in the site config: 

```
   error_log /var/log/nginx/srv6.error.log;
```

as

```
   error_log /dev/null crit;
```

<br>
</details>

<details markdown='1'>
<summary>
4. LEMP Stack
</summary>

---
- L: Linux (Debian or Ubuntu in our case)
- E: Nginx (Enginx actually)
- M: Mariadb (or Mysql if you love Or*cle so much)
- P: PHP, Python, or Perl (PHP in our case)

So not a big deal, we'll install Mariadb and PHP and connect them with Nginx.

### 4.1. Install Mariadb, Php and Necessary Dependencies.

- php-cli   : PHP client package
- php-fpm   : To run php as a cgi, nginx doesn't have a native support for PHP 
- php-mysql : For php to connect to mariadb

```
sudo apt install --yes mariadb-server php-cli php-fpm php-mysql
```

### 4.2. Configure a Site for PHP

Let's use our srv6.386387.xyz site for LEMP testing.

```
sudo nano /etc/nginx/sites-available/srv6
```

Change as below:


```
server {
   listen 80;
   root /var/www/srv6;
   index index.html index.htm;
   server_name srv6.386387.xyz;
   access_log off;
   error_log /var/log/nginx/srv6.error.log;
   location / {
      try_files $uri $uri/ =404;
   }
   location ~ \.php$ {
      fastcgi_pass unix:/run/php/php-fpm.sock;
      include fastcgi.conf;
   }
   server_tokens off;
}
```

Reload nginx

```
sudo systemctl reload nginx
```
 
### 4.3. Test it

We'll create a test database, a table in that database, add some rows to the table on Mariadb. We will also create a test PHP file with the PHP code to retrieve the data from the database and display it as HTML. 

#### 4.3.1. DB Operations

Connect to Mariadb shell

```
sudo mariadb
```

Create mysampledb database, connect to it, create a table, fill the table, create a user with the access permission on that database and the table.

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

#### 4.3.2. Create Test PHP
```
sudo nano /var/www/srv6/test.php
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
```http://srv6.386387.xyz/test.php```

<br>
</details>

