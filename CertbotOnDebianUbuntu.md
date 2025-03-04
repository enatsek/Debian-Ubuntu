##### CertbotOnDebianUbuntu 
# Auto Free SSL Certificates for Apache2 Tutorial on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
Automation of SSL and certificate renewal for Apache 2 on Debian 11/12 and Ubuntu 22.04/24.04 servers.

My server's hostname is srv1.386387.xyz. You have to change it to yours.

Sources:  
[certbot.eff.org](https://certbot.eff.org/)  
[123qwe.com](https://123qwe.com/)

<br>
</details>

<details markdown='1'>
<summary>
1. Preliminary Work
</summary>

---
My server's name is srv1.386387.xyz and I have installed Apache2 and enabled the following site configuration:

```
sudo apt update
sudo apt install apache2 -y
sudo nano /etc/apache2/sites-available/srv1.386387.xyz.conf
```

Fill as below:

```
<VirtualHost *:80>
    ServerAdmin webmaster@386387.xyz	
    ServerName srv1.386387.xyz
    DocumentRoot /var/www/srv1
    ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1.386387.xyz-access.log combined
</VirtualHost>
```

```
sudo a2ensite srv1.386387.xyz.conf
sudo systemctl reload apache2
```

HTML files are placed to /var/www/srv1 and also some apache mods are  enabled to allow ssl and redirection.

```
sudo a2enmod ssl
sudo a2enmod rewrite
sudo systemctl restart apache2
```

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

### 2.2. Get Certificates 
Run certbot to get certificates. For authentication method question;  select the option 2 (Place files ...), and enter root directory (/var/www/srv1 for my server). Enter an email address and accept TOS.

```
sudo certbot certonly -d srv1.386387.xyz
```

Certificates are installed to /etc/letsencrypt/live/srv1.386387.xyz/

### 2.3. SSL Site Configuration
Create conf file for the SSL site

```
sudo nano /etc/apache2/sites-available/srv1.386387.xyz-ssl.conf
```

Fill as below:

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

Enable the SSL site

```
sudo a2ensite srv1.386387.xyz-ssl.conf
```

Reload Apache2

```
sudo systemctl reload apache2
```

Our SSL site is ready, and we can reach it by https://srv1.386387.xyz. But we need to do some fine tuning work, at the next section.

<br>
</details>

<details markdown='1'>
<summary>
3. Fine Tunings
</summary>

---
### 3.1. Redirect HTTP Site
https://srv1.386387.xyz goes to SSL site, but http://srv1.386387.xyz goes to  non-ssl site. 

We need to redirect every site access to http to https, with only 1  exception. Certbot tries to renew the certificate in every 2 months and  makes a challenge access to /.well-known/acme-challenge/ folder. So we # need to redirect everything except this folder.

Edit http site configuration and change as below:

```
sudo nano /etc/apache2/sites-available/srv1.386387.xyz.conf
```

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
    RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301]
    # Redirection END
    ErrorLog ${APACHE_LOG_DIR}/srv1.386387.xyz-error.log
    CustomLog ${APACHE_LOG_DIR}/srv1.386387.xyz-access.log combined
</VirtualHost>
```

Reload Apache

```
sudo systemctl reload apache2
```

We can have a check if certbot renewal works correctly.

```
sudo certbot renew --dry-run
```

Certbot adds a job to crontab for automatic renewal of the certificates.  
We can check it:

```
systemctl list-timers
```

### 3.2. Certbot Renewal Hooks
When your free certificate is automatically renewed, apache needs to be  restarted. Any other software using your certificate needs to be restarted also (like postfix and dovecot). 

Certbot runs all scripts in the  /etc/letsencrypt/renewal-hooks/deploy directory after a successfull renewal. We'll put a script there.

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/reloadall.sh
```

Fill as below:

```
#!/bin/bash
systemctl reload apache2
systemctl reload postfix
systemctl reload dovecot
```

Make the script executable

```
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reloadall.sh
```
</details>
