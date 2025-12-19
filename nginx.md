##### Nginx Web Server
# Nginx Tutorial for Debian and Ubuntu

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What
Nginx is an open-source web server that also functions as a reverse proxy, load balancer, and HTTP cache. It is known for its high performance, low resource usage, and efficient handling of simultaneous connections.

### 0.1. Environment
I used Debian and Ubuntu server editions, specifically Debian 12 & 13, and Ubuntu 22.04 & 24.04 LTS Servers.

I have a test domain name: 386387.xyz, which I used for testing.

If you want to run more than a static website, you'll need PHP and a database server as well. We'll cover these components briefly.

All the following domain names point to my test server:

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
Update package repositories and install the Nginx package:

```
sudo apt update
sudo apt install nginx --yes
```

When installed on Debian and Ubuntu, Nginx (like other service packages) starts automatically. Check the service status:

```
systemctl status nginx
```

The Debian package maintainers include a sample page for the web server. You can view it:

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

Normally, you only need to edit configuration files in `sites-available/`.

### 1.3. Scripts for Enabling & Disabling Sites & Modules

If you've used Apache Web Server, you may recall commands like `a2ensite`, `a2dissite`, `a2enmod`, and `a2dismod` for enabling/disabling sites and modules.

With ChatGPT's assistance, I've created Nginx counterparts: `nxensite`, `nxdissite`, `nxenmod`, and `nxdismod`.

#### 1.3.1. nxensite - Enable a Site

This script enables a site configuration by creating a symbolic link in `sites-enabled/` from `sites-available/`.

Create the script:

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

After enabling a site, reload Nginx:

```
sudo systemctl reload nginx
```

#### 1.3.2. nxdissite - Disable a Site

This script disables a site configuration by removing its symbolic link from `sites-enabled/`.

Create the script:

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

After disabling a site, reload Nginx:

```
sudo systemctl reload nginx
```

#### 1.3.3. nxenmod - Enable a Module

This script enables a module by creating a symbolic link in `modules-enabled/` from `modules-available/`.

Create the script:

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

After enabling a module, restart Nginx:

```
sudo systemctl restart nginx
```

#### 1.3.4. nxdismod - Disable a Module

This script disables a module by removing its symbolic link from `modules-enabled/`.

Create the script:

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

After disabling a module, restart Nginx:

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

When Nginx is installed, it creates a configuration file named `default` in the `sites-available/` directory.

The `default` configuration file is enabled by default (linked to `sites-enabled/`).

Similar to Apache, there are four steps to create a website on Nginx:

1. Prepare a location for the website content and place the content there (typically a directory under `/var/www`).
2. Create a configuration file for the site in `/etc/nginx/sites-available/`.
3. Enable the site with the `nxensite` command (or manually create a symbolic link in `/etc/nginx/sites-enabled/`).
4. Reload the Nginx service.

### 2.1. Configure the Website
#### 2.1.1. Prepare Website Home

Create a home directory for our website:

```
sudo mkdir /var/www/386387.xyz
```

Create a sample home page:

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

Set proper ownership (Nginx runs as www-data):

```
sudo chown -R www-data:www-data /var/www/386387.xyz
```

Set directory permissions to 755 and file permissions to 644:

```
sudo find /var/www/386387.xyz -type d -exec chmod 755 {} \;
sudo find /var/www/386387.xyz -type f -exec chmod 644 {} \;
```

### 2.1.2. Create Website Configuration 

Disable the default site configuration (we don't need it anymore):

```
sudo nxdissite default
```

Create the site configuration file:

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

Line-by-line explanation:

- `server {`: Start of server block configuration.
- `listen 80;`: Listen on IPv4 port 80.
- `listen [::]:80;`: Listen on IPv6 port 80.
- `root /var/www/386387.xyz;`: Root directory for the site.
- `index index.html index.htm;`: Default files to serve (in order).
- `server_name 386387.xyz www.386387.xyz;`: Domain names for this site.
- `access_log /var/log/nginx/386387.xyz.access.log;`: Access log location.
- `error_log /var/log/nginx/386387.xyz.error.log;`: Error log location.
- `location / {`: Configuration for all requests.
- `try_files $uri $uri/ =404;`: Try to serve the exact file, then directory, else return 404.
- `}`: End of location block.
- `server_tokens off;`: Hide Nginx version in headers and error pages.
- `}`: End of server block.

### 2.1.3. Enable the Website
Enable the site and reload Nginx:

```
sudo nxensite 386387.xyz
sudo systemctl reload nginx
```

Test the website (assuming 386387.xyz points to your server's IP):

```
http://386387.xyz
```

### 2.2. Add SSL (TLS) Support
#### 2.2.1. Install Certbot

Thanks to [Let's Encrypt](https://letsencrypt.org/), we can obtain free SSL certificates and enable HTTPS for our site. We'll use [Certbot](https://certbot.eff.org/) to automatically install and update certificates.

Let's Encrypt certificates are valid for 90 days and must be renewed periodically. Certbot handles both acquisition and renewal tasks.

Install Certbot:

```
sudo apt update
sudo apt install certbot --yes
```

#### 2.2.2.Get the Certificates

Obtain certificates with Certbot:

```
sudo certbot certonly -d 386387.xyz,www.386387.xyz --agree-tos --webroot
```

Parameters explained:
- `certonly`: Obtain certificates only; do not install them automatically.
- `-d ...`: Obtain certificates for all listed domains.
- `--agree-tos`: Accept the Terms of Service.
- `--webroot`: Place challenge (authentication) files in a webroot folder.

Certbot will:
1. Ask for your email address (for notifications and to share with EFF if you agree).
2. Request the webroot directory for the domain (enter `/var/www/386387.xyz`).
3. For multiple domains, request webroot directories for each (select option 2 for the alternative webroot).

Certificates are installed at:

```
Certificate is saved at: /etc/letsencrypt/live/386387.xyz/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/386387.xyz/privkey.pem
```

#### 2.2.3. Create HTTPS Site Configuration

Create a configuration for the HTTPS site:

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

SSL-specific directives:
- `ssl_certificate`: Path to the SSL certificate.
- `ssl_certificate_key`: Path to the SSL private key.
- `ssl_session_timeout`: SSL session timeout duration.

Enable the HTTPS configuration and reload Nginx:

```
sudo nxensite 386387.xyz-ssl
sudo systemctl reload nginx
```

#### 2.2.4. HTTP to HTTPS Redirection

While our HTTPS site works, users accessing `http://386387.xyz` still reach the plain HTTP site. To redirect all HTTP traffic to HTTPS, modify the HTTP site configuration:

```
sudo nano /etc/nginx/sites-available/386387.xyz
```

Update to include redirection rules:

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

The added rules:
- Allow Let's Encrypt challenge files (used for renewal) to be served via HTTP.
- Redirect all other HTTP requests to HTTPS with a 301 (permanent) redirect.

Reload Nginx:

```
sudo systemctl reload nginx
```


### 2.2.5. Certbot Hooks

Certbot automatically renews certificates before they expire, but Nginx continues using the old certificates until reloaded. To ensure Nginx uses renewed certificates, create a deployment hook script.

Certbot executes all scripts in `/etc/letsencrypt/renewal-hooks/deploy` after successful renewal. Create a script:

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/reloadnginx.sh
```

Fill as below:

```
#!/bin/bash
systemctl reload nginx
```

Make the script executable:

```
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reloadnginx.sh
```

Now Nginx will automatically reload whenever Certbot renews certificates.

<br>
</details>

<details markdown="1">
<summary>
3. Adding More Sites to Our Server
</summary>

---
### 3.0. Explanations

Nginx can host multiple websites simultaneously. There's no inherent limit to the number of sites you can host, constrained only by your server's CPU and RAM resources.

We'll add several sites with different configurations:

- Local access only
- Accessible only by specific IPs
- Reverse proxy configuration
- Custom error pages
- Listening on a non-standard port
- No access logs

These examples will use HTTP only; you can add HTTPS following the steps in section 2.2.

### 3.1. Local Access Only
This site will only allow access from the server itself, blocking all external IPs. Such configurations are useful for administrative or internal management interfaces.

Create the site directory and set proper permissions:

```
sudo mkdir /var/www/srv1
sudo touch /var/www/srv1/index.html
sudo chown -R www-data:www-data /var/www/srv1
sudo find /var/www/srv1 -type d -exec chmod 755 {} \;
sudo find /var/www/srv1 -type f -exec chmod 644 {} \;
```

Create the sample HTML content:

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

Create the site configuration:

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

Enable the site and reload Nginx:

```
sudo nxensite srv1
sudo systemctl reload nginx
```

You won't be able to access `http://srv1.386387.xyz` from external systems, but running this command on the server will retrieve the HTML:

```
curl 127.0.0.1
```

### 3.2. Only Accessible by Specific IPs
This site will only be accessible from two specified IP addresses. This configuration is useful for serving content to specific users or locations.

Create the site directory and set permissions:

```
sudo mkdir /var/www/srv2
sudo touch /var/www/srv2/index.html
sudo chown -R www-data:www-data /var/www/srv2
sudo find /var/www/srv2 -type d -exec chmod 755 {} \;
sudo find /var/www/srv2 -type f -exec chmod 644 {} \;
```

Create the sample HTML content:

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

Create the site configuration with IP restrictions:

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

Enable the site and reload Nginx:

```
sudo nxensite srv2
sudo systemctl reload nginx
```

Only the specified IPs can access `http://srv2.386387.xyz`; others will receive a "403 Forbidden" error.

You can add more IPs or entire subnets:

```
      allow 195.174.44.0/24;
```

### 3.3. Reverse Proxy Configuration

Some applications provide locally-running web servers (e.g., Rspamd). Using Nginx's reverse proxy capabilities, you can expose these internal services externally.

First, simulate a local web server. Open a terminal and run:

```
mkdir /tmp/test
echo Test > /tmp/test/index.html
cd /tmp/test
python3 -m http.server 8080 --bind 127.0.0.1
```

This Python server runs locally on port 8080. Test it in another terminal:

```
curl 127.0.0.1:8080
```

This Python server runs locally on port 8080. Test it in another terminal:

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

Key proxy directives:
- `proxy_pass`: Forward requests to the backend server.
- `proxy_set_header`: Preserve original request headers.

Enable the site and reload Nginx:

```
sudo nxensite srv3
sudo systemctl reload nginx
```

Now access `http://srv3.386387.xyz/` to reach the local Python server.

**Note:** Remember to stop the Python server (Ctrl+C in its terminal) when finished.


### 3.4. Custom Error Pages

Nginx serves default error pages, but you can customize them. The most common error is 404 (Page Not Found).

Create the site directory and files:

```
sudo mkdir /var/www/srv4
sudo touch /var/www/srv4/index.html
sudo touch /var/www/srv4/404.html
sudo chown -R www-data:www-data /var/www/srv4
sudo find /var/www/srv4 -type d -exec chmod 755 {} \;
sudo find /var/www/srv4 -type f -exec chmod 644 {} \;
```

Create the main page:

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

Create the custom 404 page:

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

Create the site configuration with custom error document:

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

The `internal` directive prevents direct access to the error page.

Enable the site and reload Nginx:

```
sudo nxensite srv4
sudo systemctl reload nginx
```

Visit `http://srv4.386387.xyz` for the main page, and `http://srv4.386387.xyz/nonexistent` to see the custom 404 page.

### 3.5. Listening on a Different Port

While web servers typically use ports 80 (HTTP) and 443 (HTTPS), you might need to use alternative ports.

Create the site directory and files:

```
sudo mkdir /var/www/srv5
sudo touch /var/www/srv5/index.html
sudo chown -R www-data:www-data /var/www/srv5
sudo find /var/www/srv5 -type d -exec chmod 755 {} \;
sudo find /var/www/srv5 -type f -exec chmod 644 {} \;
```

Create the sample HTML content:

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

Create the site configuration for port 8080:

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

Enable the site and reload Nginx:

```
sudo nxensite srv5
sudo systemctl reload nginx
```

Access the site at `http://srv5.386387.xyz:8080`.

### 3.6. No Access Logs

For privacy or performance reasons, you might want to disable access logging for a site.

Create the site directory and files:

```
sudo mkdir /var/www/srv6
sudo touch /var/www/srv6/index.html
sudo chown -R www-data:www-data /var/www/srv6
sudo find /var/www/srv6 -type d -exec chmod 755 {} \;
sudo find /var/www/srv6 -type f -exec chmod 644 {} \;
```

Create the sample HTML content:

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

Create the site configuration without access logs:

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


Enable the site and reload Nginx:

```
sudo nxensite srv6
sudo systemctl reload nginx
```

Access the site at `http://srv6.386387.xyz`. No access logs will be recorded.

To also disable error logging:

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
- **L**: Linux (Debian or Ubuntu in our case)
- **E**: Nginx (pronounced "Engine-X")
- **M**: MariaDB (or MySQL)
- **P**: PHP (also works with Python or Perl)

We'll install MariaDB and PHP, then configure Nginx to work with them.

### 4.1. Install Mariadb, PHP and Necessary Dependencies.
Install the required packages:

- `php-cli`: PHP command-line interface
- `php-fpm`: PHP FastCGI Process Manager (required for Nginx)
- `php-mysql`: PHP extension for MySQL/MariaDB connectivity

```
sudo apt install --yes mariadb-server php-cli php-fpm php-mysql
```

### 4.2. Configure a Site for PHP

Let's modify the srv6.386387.xyz site for PHP testing.

Edit the site configuration:

```
sudo nano /etc/nginx/sites-available/srv6
```

Update to include PHP processing:

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

Key additions:
- `index.php` added to the `index` directive
- PHP location block to process `.php` files via PHP-FPM

Reload Nginx:

```
sudo systemctl reload nginx
```
 
### 4.3. Test it

We'll create a test database, table, and PHP script to retrieve and display data.

#### 4.3.1. Database Setup

Connect to MariaDB:

```
sudo mariadb
```

Run the following SQL commands:

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

#### 4.3.2. Create Test PHP Script
```
sudo nano /var/www/srv6/test.php
```

Fill as below:

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

Access the test page at `http://srv6.386387.xyz/test.php` to verify the LEMP stack is working correctly.

<br>
</details>

