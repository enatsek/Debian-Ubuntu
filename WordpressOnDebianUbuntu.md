##### WordpressOnDebianUbuntu 
# Install Wordpress  On Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>
---
Based on [Brian Boucheron's Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lamp-on-ubuntu-18-04)

My server: www.386387.xyz  Debian 12 (or 11) and Ubuntu 24.04 Server (or 22.04)

Wordpress Mariadb Database Name: wordpress  
Wordpress Mariadb Database User: wordpressuser  
Password of wordpressuser: pAsswOrd1234  
Wordpress website location: /var/www/wordpress  

LAMP stack must be installed; see [LampOnDebianUbuntu](LampOnDebianUbuntu.html)  Tutorial

<br>
</details>

<details markdown='1'>
<summary>
1. Configure a Website (If you haven't done already)
</summary>
---
### 1.1. Make room for our website
```
sudo mkdir /var/www/wordpress
```

### 1.2. Create a configuration file for our web server
```
sudo nano /etc/apache2/sites-available/386387.xyz.conf
```

Fill as below:

```
<VirtualHost *:80>
        ServerAdmin postmaster@386387.xyz
        ServerName www.386387.xyz
        ServerAlias 386387.xyz
        DocumentRoot /var/www/wordpress
        ErrorLog ${APACHE_LOG_DIR}/386387.xyz-error.log
        CustomLog ${APACHE_LOG_DIR}/386387.xyz-access.log combined
</VirtualHost>
```

### 1.3. Enable the site
```
sudo a2ensite 386387.xyz.conf
```

### 1.4. Reload apache
```
sudo systemctl reload apache2
```

<br>
</details>

<details markdown='1'>
<summary>
2. Create MariaDB DB User for Wordpress
</summary>
---
### 2.1. Login to MariaDB
```
sudo mariadb
```

### 2.2. Create the Database
Create a database named as wordpress, create a user named as wordpressuser and give the user necessarry permissions for the database.

Run on Mariadb Shell:

```
CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'pAsswOrd1234';
GRANT ALL ON wordpress.* TO 'wordpressuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

<br>
</details>

<details markdown='1'>
<summary>
3. Install Additional PHP Extensions
</summary>
```
sudo apt update
sudo apt install php-curl php-gd php-mbstring php-xml php-xmlrpc \
php-soap php-intl php-zip
```

Restart apache

```
sudo systemctl restart apache2
```

<br>
</details>

<details markdown='1'>
<summary>
4. Adjust Apache for Wordpress
</summary>
---
### 4.1. Enable wordpress' .htaccess files
Edit our site config, adding folders to override

```
sudo nano /etc/apache2/sites-available/386387.xyz.conf
```
Add following lines to just after DocumentRoot line

```
        <Directory /var/www/wordpress/>
            AllowOverride All
        </Directory>
```

### 4.2. Enable Apache Rewrite module 
```
sudo a2enmod rewrite
```

### 4.3. (Optional) Check Status of Apache Configs
```
sudo apache2ctl configtest
```

### 4.4. Restart Apache
```
sudo systemctl restart apache2
```

<br>
</details>

<details markdown='1'>
<summary>
5. Download Wordpress
</summary>
---
Wordpress can be installed by Debian packages, but we prefer to download the latest version from the original source

### 5.1. Go to the temp directory, download wordpress, extract it
For Debian, you may need to install curl

```
sudo apt install --yes curl
cd /tmp
curl -O https://wordpress.org/latest.tar.gz
tar xzvf latest.tar.gz
```

### 5.2. Before copying to its home we need to make some additions
Create a dummy .htaccess file

```
touch /tmp/wordpress/.htaccess
```

Copy sample config file to real config file

```
cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
```

### 5.3. Copy wordpress files to their location
```
sudo cp -a /tmp/wordpress/. /var/www/wordpress
```

<br>
</details>

<details markdown='1'>
<summary>
6. Configure Wordpress Directory
</summary>
---
### 6.1. Set ownerships and permissions
Owned by www-data:www-data

```
sudo chown -R www-data:www-data /var/www/wordpress
```

All files 640, all dirs 750

```
sudo find /var/www/wordpress/ -type d -exec chmod 750 {} \;
sudo find /var/www/wordpress/ -type f -exec chmod 640 {} \;
```

### 6.2. Setup wordpress config file
#### 6.2.1. Generate secure phrases
WP requires some secure phrases for security, we will create them now

```
curl -s https://api.wordpress.org/secret-key/1.1/salt/
```

The output of this program will be something like following:  
Temporarily copy them into a text file, we'll use it later

```
define('AUTH_KEY',         'O`tLoX^0[pT24ty<YOByEP#}wBtd|7M!9^-az.W_v{`;+!*PX_9/A#^#}SL@I_wD');
define('SECURE_AUTH_KEY',  '-U]7Eu_Bbh!tA/5lk3.eDRzGrY<%i,:cn*yBOiE^*zZHK&RTbHmv]^+[[1v49=bq');
define('LOGGED_IN_KEY',    'VHYd-]>SDIsT_^-;>_0DBV:2}>u^wI;]T>IqXr}++h1sRjQM%U^I0ijVwAi? (yB');
define('NONCE_KEY',        'lui4^EuI3U-m8m!IUI%>;+)r[dJW`w2pl@g4JU==(,ipCi|EC)+vo,&2rAR Dm+-');
define('AUTH_SALT',        'W,>S!kG,KCPZ/`Y7;(hpL,1-M2lanZz(3)kdds-{;t9D(X&Qy:+0^H&3jE%WS:L4');
define('SECURE_AUTH_SALT', 'f*q%x{M6#GQ|L{U|!UoI~`8(71};e}Xm;4#e^J/b&DC<DO=Xv6$caAC<2q4gs}^0');
define('LOGGED_IN_SALT',   '=HN;=E:zl1-X:5w:MTw3LHV^?VP})Z}&T*P!zvAG|R=S>6;~Xz|rh@S#MrSH2FA)');
define('NONCE_SALT',       '`d)>*Ae)9g<Aaa1eQ*9HlqY-|__kE5,Nte2UAMJO3ro=9T#y=,|-/^D(&+XQ:,la');
```

#### 6.2.2. Add phrases to WP config file
```
sudo nano /var/www/wordpress/wp-config.php
```

Browse to the section with the following lines, replace them with the text you copied. (Around line 50)

```
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );
```

While in the same file, browse up to the section with the following lines:

```
/** The name of the database for WordPress */
define( 'DB_NAME', 'database_name_here' );
/** MySQL database username */
define( 'DB_USER', 'username_here' );
/** MySQL database password */
define( 'DB_PASSWORD', 'password_here' );
/** MySQL hostname */
define( 'DB_HOST', 'localhost' );
/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );
/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );
```

Change as specified:
- database_name_here : wordpress
- username_here : wordpressuser
- password : pAsswOrd1234

Add following line:

```
define('FS_METHOD', 'direct');
```

<br>
</details>

<details markdown='1'>
<summary>
7. Wordpress is ready, open in your browser
</summary>
---
`http://www.386387.xyz`

Of course it would be a good idea to add SSL to your site, refer to  [CertbotOnDebianUbuntu](CertbotOnDebianUbuntu.html) Tutorial.

</details>

