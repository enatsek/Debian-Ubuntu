##### Apache Web Server
# Apache Tutorial for Debian and Ubuntu

<details markdown="1">
<summary>
0. Specs
</summary>

---

### 0.0. The What
Apache HTTP Server is a free and open-source web server software that facilitates the delivery of web content to users. It is one of the most popular web servers, known for its reliability, security, and extensive customization options.

### 0.1. Environment
I used Debian and Ubuntu server editions, specifically Debian 12 & 13, and Ubuntu 22.04 & 24.04 LTS Servers.

I have a test domain name: 386387.xyz, which I used for testing. The test hostnames used are:

- 386387.xyz
- www.386387.xyz
- srv1.386387.xyz
- srv2.386387.xyz
- srv3.386387.xyz
- srv4.386387.xyz
- srv5.386387.xyz
- srv6.386387.xyz

If you want to run more than a static website, you'll need PHP and a database server as well. We'll cover these components briefly.

### 0.3. Sources

- [Apache Documentation](https://httpd.apache.org/docs/)  
- [Debian](https://manpages.debian.org/) and [Ubuntu](https://manpages.ubuntu.com/) manpages.
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
Update package repositories and install the apache2 package:

```
sudo apt update
sudo apt install apache2 --yes
```

When installed on Debian and Ubuntu, Apache (like other service packages) starts automatically. You can check the service status:

```
systemctl status apache2
```

The Debian package managers include a sample page for the web server. You can view it:

```
sudo nano /var/www/html/index.html
```

### 1.2. Configuration Files

Debian and Ubuntu installations have the following files and directories at `/etc/apache2`:

- **apache2.conf**: The main configuration file for the Apache web server. Contains global server settings and typically includes other configuration files.

- **envvars**: Sets environment variables used by Apache, such as paths and user/group settings. It is sourced (included) when Apache starts.

- **magic**: Helps Apache identify file types based on their content rather than just their extensions. Used for MIME type detection.

- **ports.conf**: Defines the ports on which Apache listens (like port 80 for HTTP and 443 for HTTPS).

- **conf-available/**: Contains additional configuration files that can be enabled or disabled as needed. These are typically non-essential but provide extra features.

- **conf-enabled/**: Symbolic links to configuration files in `conf-available/` that are currently enabled. Files here are active and loaded by Apache.

- **mods-available/**: Contains configuration files for Apache modules that can be enabled or disabled. These modules extend Apache's functionality (like SSL or PHP).

- **mods-enabled/**: Symbolic links to enabled module configurations from `mods-available/`. Only modules listed here are active.

- **sites-available/**: Contains configuration files for individual websites (virtual hosts). Each file defines settings like the document root, domain name, and logging for a specific site.

- **sites-enabled/**: Symbolic links to enabled site configurations from `sites-available/`. Only sites listed here are active and accessible.

Normally, you only need to edit configuration files in `sites-available/`.

### 1.3. Debian (Ubuntu) Specific Apache Commands

Debian provides six commands for easy Apache configuration. These commands, prepared by Debian package managers, are also available on Ubuntu servers:

- **a2ensite**: Enables a site configuration by creating a symbolic link in `sites-enabled/` from `sites-available/`.
- **a2dissite**: Disables a site configuration by removing its symbolic link from `sites-enabled/`.
- **a2enmod**: Enables an Apache module by creating a symbolic link in `mods-enabled/` from `mods-available/`.
- **a2dismod**: Disables an Apache module by removing its symbolic link from `mods-enabled/`.
- **a2enconf**: Enables additional configuration files from `conf-available/` by creating symbolic links in `conf-enabled/`.
- **a2disconf**: Disables additional configuration files by removing symbolic links from `conf-enabled/`.

After enabling or disabling a site, reload Apache:

```
sudo systemctl reload apache2
```

After enabling or disabling a configuration or module, restart Apache:

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

When the Apache package is installed, it creates two configuration files in the `sites-available/` directory: `000-default.conf` and `default-ssl.conf`.

- `000-default.conf` is enabled by default (linked to `sites-enabled/`).
- `default-ssl.conf` is not enabled and can serve as a template for configuring SSL sites.

There are four steps to create a website on Apache Web Server:

1. Prepare a location for the website content and place the content there (typically a directory under `/var/www`).
2. Create a configuration file for the site in `/etc/apache2/sites-available/`.
3. Enable the site with the `a2ensite` command.
4. Reload the Apache service.

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

Make the Apache service user own the directory and files:

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
sudo a2dissite 000-default.conf
```

Create the configuration file for the site:

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

Line-by-line explanation of the configuration file:

- `<VirtualHost *:80>`: Start of site configuration. The site listens on all IP addresses of the host on port 80.
- `ServerAdmin`: Administrator email for the site.
- `ServerName`: Primary domain name for the site (386387.xyz).
- `ServerAlias`: Alternative domain name for the site (www.386387.xyz).
- `DocumentRoot`: Location of website content (/var/www/386387.xyz).
- `ErrorLog`: File for error logs.
- `CustomLog`: File for access logs with combined format.
- `</VirtualHost>`: End of site configuration.

### 2.1.3. Enable the Website
Enable the site and reload Apache:

```
sudo a2ensite 386387.xyz.conf
sudo systemctl reload apache2
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

#### 2.2.2. Install Necessary Apache Modules

To enable HTTPS and redirect HTTP to HTTPS, enable these Apache modules:

```
sudo a2enmod ssl
sudo a2enmod rewrite
sudo systemctl restart apache2
```

#### 2.2.3. Obtain Certificates

Obtain certificates with Certbot:

```
sudo certbot certonly -d 386387.xyz,www.386387.xyz --agree-tos --webroot
```

Parameters explained:

- `certonly`: Obtain certificates only; do not install them automatically.
- `-d ...`: Obtain certificates for all listed domains.
- `--agree-tos`: Accept the Terms of Service.
- `--webroot`: Place challenge (authentication) files in a webroot folder. Since we already have a web server, this method is appropriate.


Certbot will:
1. Ask for your email address (for notifications and to share with EFF if you agree).
2. Request the webroot directory for the domain (enter `/var/www/386387.xyz`).
3. For multiple domains, request webroot directories for each (select option 2 for the alternative webroot).

Certificates are installed at:

```
Certificate is saved at: /etc/letsencrypt/live/386387.xyz/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/386387.xyz/privkey.pem
```

#### 2.2.4. Create HTTPS Site Configuration

Create a configuration for the HTTPS site:

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

The SSL-specific lines:

- `SSLEngine on`: Enable SSL for this virtual host.
- `SSLCertificateFile`: Path to the SSL certificate.
- `SSLCertificateKeyFile`: Path to the SSL private key.

Enable the HTTPS configuration and restart Apache:

```
sudo a2ensite 386387.xyz-ssl.conf
sudo systemctl restart apache2
```

Our HTTPS site is now ready at `https://386387.xyz`.

#### 2.2.5. HTTP to HTTPS Redirection

While our HTTPS site works, users accessing `http://386387.xyz` still reach the plain HTTP site. To redirect all HTTP traffic to HTTPS, modify the HTTP site configuration:

```
sudo nano /etc/apache2/sites-available/386387.xyz.conf
```

Update to include redirection rules:

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

The added rules:

- Allow Let's Encrypt challenge files (used for renewal) to be served via HTTP.
- Redirect all other HTTP requests to HTTPS with a 301 (permanent) redirect.

Reload Apache:

```
sudo systemctl reload apache2
```

### 2.2.6. Certbot Hooks

When the time comes, certbot renews the certificates. But Apache doesn't know that and tries to use the old ones. That means our HTTPS site does not work anymore. 

Certbot automatically renews certificates before they expire, but Apache continues using the old certificates until reloaded. To ensure Apache uses renewed certificates, create a deployment hook script.

Certbot executes all scripts in `/etc/letsencrypt/renewal-hooks/deploy` after successful renewal. Create a script:

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/reloadapache.sh
```

Fill as below:

```
#!/bin/bash
systemctl reload apache2
```

Make the script executable:

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

Apache can host multiple websites simultaneously. There's no inherent limit to the number of sites you can host, constrained only by your server's CPU and RAM resources.

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

Create the site directory, sample HTML file, and set proper permissions:

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

Enable the site and reload Apache:

```
sudo a2ensite srv1.conf
sudo systemctl reload apache2
```

You won't be able to access `http://srv1.386387.xyz` from external systems, but running this command on the server will retrieve the HTML:

```
curl 127.0.0.1
```

### 3.2. Only Accessible by 2 IPs
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

Enable the site and reload Apache:

```
sudo a2ensite srv2.conf
sudo systemctl reload apache2
```

Only the specified IPs can access the site; others will receive a "403 Forbidden" error.

You can add more IPs or entire subnets:

```
        Require ip 195.174.44.0/24
```

### 3.3. Reverse Proxy Configuration

Some applications provide locally-running web servers (e.g., Rspamd). Using Apache's reverse proxy capabilities, you can expose these internal services externally.

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

Enable Apache's proxy modules:

```
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart apache2
```

Create the reverse proxy configuration:

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

Key directives:

- `ProxyPreserveHost On`: Preserve the original Host header.
- `ProxyPass`: Forward requests from `/reverse` to the local server.
- `ProxyPassReverse`: Adjust response headers from the backend server.

Enable the site and reload Apache:

Enable the site and reload Apache daemon

```
sudo a2ensite srv3.conf
sudo systemctl reload apache2
```

Now access `http://srv3.386387.xyz/reverse` to reach the local Python server.

**Note:** Remember to stop the Python server (Ctrl+C in its terminal) when finished.

### 3.4. Custom Error Pages

Apache serves default error pages, but you can customize them. The most common error is 404 (Page Not Found).

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

Enable the site and reload Apache:

```
sudo a2ensite srv4.conf
sudo systemctl reload apache2
```

Visit `http://srv4.386387.xyz` for the main page, and `http://srv4.386387.xyz/nonexistent` to see the custom 404 page.

### 3.5. Listening on a Non-Standard Port

While web servers typically use ports 80 (HTTP) and 443 (HTTPS), you might need to use alternative ports.

First, configure Apache to listen on port 8080:

```
sudo nano /etc/apache2/ports.conf
```

Add to the end of the file:

```
Listen 8080
```

Restart Apache (restart required, not reload):

```
sudo systemctl restart apache2
```

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

Enable the site and reload Apache:

```
sudo a2ensite srv5.conf
sudo systemctl reload apache2
```

Access the site at `http://srv5.386387.xyz:8080`.

### 3.6. No Access Logs

We want our site to have no access logs. There might be a lot of reason for that. One reason that comes to my mind is privacy. 

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

Enable the site and reload Apache:

```
sudo a2ensite srv6.conf
sudo systemctl reload apache2
```

Access the site at `http://srv6.386387.xyz`. No access logs will be recorded.

To also disable error logging, modify the configuration:

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
Install PHP and the Apache PHP module:

```
sudo apt update
sudo apt install php libapache2-mod-php --yes
```

Test PHP using the srv4 site. Create a PHP info page:

```
sudo nano /var/www/srv4/info.php
```

Fill as below:

```
<?php phpinfo(); ?>
```

Visit `http://srv4.386387.xyz/info.php` to see PHP configuration details.

### 4.2. PHP Configuration

Adjust PHP settings by editing the configuration file. The path varies by PHP version:

```
sudo nano /etc/php/*/apache2/php.ini
```

Common settings to adjust:

```
upload_max_filesize = 16M
post_max_size = 16M
memory_limit = 128M
display_errors = Off  # Set to On for development
```

After making changes you need to restart Apache:

```
After making changes, restart Apache:
```

### 4.3. Additional PHP Packages

- **php-mysql**: MySQL/MariaDB database connectivity
- **php-pgsql**: PostgreSQL database connectivity
- **php-sqlite3**: SQLite database support
- **php-json**: JSON encoding/decoding
- **php-xml**: XML parsing and generation
- **php-mbstring**: Multibyte string handling (UTF-8 support)
- **php-curl**: HTTP requests to external APIs
- **php-opcache**: Opcode cache for performance
- **php-zip**: ZIP archive manipulation
- **php-gd**: Image processing

Install all recommended packages:

```
sudo apt install php-mysql php-pgsql php-sqlite3 php-json \
   php-xml php-mbstring php-curl php-opcache php-zip php-gd
sudo systemctl restart apache2
```

<br>
</details>


