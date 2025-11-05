##### Certbot Tutorial
# Free Let's Encrypt SSL Certificates on Debian and Ubuntu Server

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.0. The What

Let's Encrypt is a free, automated, and open certificate authority (CA) that provides SSL/TLS certificates, enabling websites to use HTTPS. It's backed by the Internet Security Research Group (ISRG) and makes web encryption accessible to everyone.

Certbot, developed by the EFF (Electronic Frontier Foundation), is a command-line tool that automatically requests, installs, and renews Let's Encrypt certificates. It handles most of the setup, allowing you to enable HTTPS with just a few commands.

The certificates are free but need to be renewed every 90 days. This tutorial guides you through the installation and configuration of the auto-renewal process for both Apache2 and Nginx web servers.

### 0.1. Environment

- **Server Name:** `srv1.386387.xyz`
- **Server Distro:** Debian 13 or Ubuntu 24.04 Server
- **HTTP Server:** Apache2 or Nginx

**Remember to use your server's actual hostname instead of `srv1.386387.xyz` in your configurations.**


### 0.2. Sources

- [certbot.eff.org](https://certbot.eff.org/)
- [123qwe.com](https://123qwe.com/)

<br>
</details>

<details markdown='1'>
<summary>
1. Preliminary Work
</summary>

---

Depending on your choice of HTTP server, Apache2 or Nginx should be installed before.

### 1.1. Apache Server

Install Apache2

```
sudo apt update
sudo apt install apache2 -y
```

Create a configuration file:

```
sudo nano /etc/apache2/sites-available/srv1.386387.xyz.conf
```

Fill it with the following content:

```
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1.386387.xyz-access.log combined
</VirtualHost>
```

Enable the site and reload Apache:

```
sudo a2ensite srv1.386387.xyz.conf
sudo systemctl reload apache2
```

HTML files should be placed in `/var/www/srv1`. Enable the necessary Apache modules to allow SSL and redirection:

```
sudo a2enmod ssl
sudo a2enmod rewrite
sudo systemctl restart apache2
```

### 1.2. Nginx Server

Install Nginx

```
sudo apt update
sudo apt install nginx -y
```

Create a server block configuration file:

```
sudo nano /etc/nginx/sites-available/srv1.386387.xyz
```

Fill it with the following content:

```
server {
   listen 80;
   listen [::]:80;
   root /var/www/srv1;
   index index.html index.htm;
   server_name srv1.386387.xyz;
   access_log /var/log/nginx/srv1.386387.xyz.access.log;
   error_log /var/log/nginx/srv1.386387.xyz.error.log;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Enable the site by creating a symbolic link and reload Nginx:

```
sudo ln -s /etc/nginx/sites-available/srv1.386387.xyz \
    /etc/nginx/sites-enabled/srv1.386387.xyz
sudo systemctl reload nginx
```

HTML files should be placed in `/var/www/srv1`.

<br>
</details>

<details markdown='1'>
<summary>
2. Certbot
</summary>

---
### 2.1. Install Certbot
```
sudo apt update
sudo apt install certbot -y
```

### 2.2. Obtain Certificates

Run Certbot to obtain the certificates. When prompted:
1.  Select option **2** (Place files in webroot directory).
2.  Enter your email address.
3.  Accept the Terms of Service.
4.  Decide whether to share your email with the EFF.
5.  Enter the web root directory for your server (`/var/www/srv1` in this example).

```
sudo certbot certonly -d srv1.386387.xyz
```

Certificates are installed to /etc/letsencrypt/live/srv1.386387.xyz/

### 2.3. SSL Site Configuration for Apache2

Create an SSL configuration file for the site:

```
sudo nano /etc/apache2/sites-available/srv1.386387.xyz-ssl.conf
```

Fill it with the following content:

```
<VirtualHost *:443>
 ServerName srv1.386387.xyz
 DocumentRoot /var/www/srv1
 ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
 CustomLog ${APACHE_LOG_DIR}/srv1.386387.xyz-access.log combined
 SSLEngine on
 SSLCertificateFile /etc/letsencrypt/live/srv1.386387.xyz/fullchain.pem
 SSLCertificateKeyFile /etc/letsencrypt/live/srv1.386387.xyz/privkey.pem
</VirtualHost>
```

Enable the SSL site and reload Apache:

```
sudo a2ensite srv1.386387.xyz-ssl.conf
sudo systemctl reload apache2
```

Your SSL site is now accessible at `https://srv1.386387.xyz`. The next section covers important fine-tuning.

### 2.4. SSL Site Configuration for Nginx

Create an SSL server block configuration file:

```
sudo nano /etc/nginx/sites-available/srv1.386387.xyz-ssl
```

Fill it with the following content:

```
server {
   listen 443 ssl;
   listen [::]:443 ssl;
   root /var/www/srv1;
   index index.html index.htm;
   server_name srv1.386387.xyz;
   access_log /var/log/nginx/srv1.386387.xyz.access.log;
   error_log /var/log/nginx/srv1.386387.xyz.error.log;
   ssl_certificate /etc/letsencrypt/live/srv1.386387.xyz/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/srv1.386387.xyz/privkey.pem;
   ssl_session_timeout 5m;
   location / {
      try_files $uri $uri/ =404;
   }
   server_tokens off;
}
```

Enable the SSL site and reload Nginx:

```
sudo ln -s /etc/nginx/sites-available/srv1.386387.xyz-ssl \
    /etc/nginx/sites-enabled/srv1.386387.xyz-ssl
sudo systemctl reload nginx
```

Your SSL site is now accessible at `https://srv1.386387.xyz`. The next section covers important fine-tuning.


<br>
</details>

<details markdown='1'>
<summary>
3. Fine Tunings
</summary>

---
### 3.1. HTTP to HTTPS Redirect - Apache2

While `https://srv1.386387.xyz` now uses SSL, `http://srv1.386387.xyz` still does not.

We need to redirect all HTTP traffic to HTTPS, with one exception: Certbot's renewal process requires access to the `/.well-known/acme-challenge/` directory over HTTP. We must allow access to this path.

Edit the HTTP site configuration file:

```
sudo nano /etc/apache2/sites-available/srv1.386387.xyz.conf
```

Modify it as follows to include the redirection rules:

```
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    # Redirection BEGIN
    # Force redirect to HTTPS unless the request is for Let's Encrypt
    RewriteEngine On
    RewriteCond %{REQUEST_URI} !^/.well-known/acme-challenge/
    RewriteCond %{HTTPS} off
    RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
    # Redirection END
    ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1.386387.xyz-access.log combined
</VirtualHost>
```

Reload Apache to apply the changes:

```
sudo systemctl reload apache2
```

### 3.1. HTTP to HTTPS Redirect - Nginx

While `https://srv1.386387.xyz` now uses SSL, `http://srv1.386387.xyz` still does not.

We need to redirect all HTTP traffic to HTTPS, with one exception: Certbot's renewal process requires access to the `/.well-known/acme-challenge/` directory over HTTP. We must allow access to this path.

Edit the HTTP server block configuration file:

```
sudo nano /etc/nginx/sites-available/srv1.386387.xyz
```

```
server {
   listen 80;
   listen [::]:80;
   index index.html index.htm;
   server_name srv1.386387.xyz;
   access_log /var/log/nginx/srv1.386387.xyz.access.log;
   error_log /var/log/nginx/srv1.386387.xyz.error.log;
   # Serve Let's Encrypt validation requests normally
   location ^~ /.well-known/acme-challenge {
       allow all; 
       root /var/www/srv1;
   }
   # Redirect all other traffic to HTTPS
   location / {
      return 301 https://$host$request_uri;
   }
   server_tokens off;
}
```

Reload Nginx to apply the changes:

```
sudo systemctl reload nginx
```

### 3.3. Verification and Auto-Renewal

Test if the certificate renewal process works correctly with a dry run:

```
sudo certbot renew --dry-run
```

Certbot automatically installs a cron job or systemd timer to handle renewal. 
You can check the timers with:
```
systemctl list-timers
```

### 3.4. Certbot Renewal Hooks

When a certificate is automatically renewed, services using it (like Apache, Nginx, Postfix, or Dovecot) need to be reloaded to use the new certificate.


Certbot executes all scripts in the `/etc/letsencrypt/renewal-hooks/deploy/` directory after a successful renewal. We can create a script there to reload services.

Create the script:

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/reloadall.sh
```

Add the following content, including only the services you use:

```
#!/bin/bash
systemctl reload apache2     # If you have apache2
systemctl reload nginx       # If you have nginx
systemctl reload postfix     # If you have postfix
systemctl reload dovecot     # If you have dovecot
```

Make the script executable

```
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reloadall.sh
```
</details>
