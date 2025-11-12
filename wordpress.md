##### Wordpress
# Install Wordpress On Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.1. The What

WordPress is a free and open-source content management system (CMS) that allows users to create and manage websites easily without needing extensive coding knowledge.

This tutorial demonstrates how to install WordPress on Debian and Ubuntu servers.

### 0.2. The Environment

- **Server Name:** `www.386387.xyz`
- **Server Distro:** Debian 12/13 or Ubuntu 22.04/24.04 LTS Server

**WordPress Configuration:**
- **MariaDB Database Name:** `wordpress`
- **MariaDB Database User:** `wordpressuser`
- **Database User Password:** `pAsswOrd1234`
- **Website Location:** `/var/www/wordpress`

**Prerequisite:** A LAMP stack (Linux, Apache, MySQL/MariaDB, PHP) must be installed. See the [LAMP Tutorial](lamp.html).

### 0.3. Sources

- [Brian Boucheron's Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lamp-on-ubuntu-18-04)
- [Deepseek](https://www.deepseek.com/)


<br>
</details>

<details markdown='1'>
<summary>
1. Configure a Website (If Not Already Done)
</summary>

---

Create the directory for your WordPress site:

```
sudo mkdir /var/www/wordpress
```

Create a virtual host configuration file for Apache:

```
sudo nano /etc/apache2/sites-available/386387.xyz.conf
```

Fill with the following content:

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

Enable the site and reload Apache:

```
sudo a2ensite 386387.xyz.conf
sudo systemctl reload apache2
```

<br>
</details>

<details markdown='1'>
<summary>
2. Create MariaDB Database and User for Wordpress
</summary>

---

Access the MariaDB shell:

```
sudo mariadb
```

Run the following commands in the MariaDB shell to create the database and user:

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

---

WordPress requires several PHP extensions for full functionality. Install them with:

```
sudo apt update
sudo apt install php-curl php-gd php-mbstring php-xml php-xmlrpc \
php-soap php-intl php-zip
```

Restart Apache to load the new PHP extensions:

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

To allow WordPress to use `.htaccess` files for URL rewriting and other directives, modify your site configuration:

```
sudo nano /etc/apache2/sites-available/386387.xyz.conf
```

Add the following `Directory` block just after the `DocumentRoot` line:

```
        <Directory /var/www/wordpress/>
            AllowOverride All
        </Directory>
```

Enable Apache's rewrite module:

```
sudo a2enmod rewrite
```

(Optional) Verify that your Apache configuration is valid:

```
sudo apache2ctl configtest
```

Restart Apache to apply the changes:

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

While WordPress is available via Debian packages, this guide uses the latest version from the official source for better compatibility and features.

Navigate to the temporary directory and download WordPress:

```
sudo apt update
sudo apt install --yes curl
cd /tmp
curl -O https://wordpress.org/latest.tar.gz
tar xzvf latest.tar.gz
```

Create a dummy `.htaccess` file and copy the sample configuration:

```
touch /tmp/wordpress/.htaccess
cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
```

Copy the WordPress files to your web directory:

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

Set ownership of all WordPress files to the web server user:

```
sudo chown -R www-data:www-data /var/www/wordpress
```

Set secure permissions (directories: 750, files: 640):

```
sudo find /var/www/wordpress/ -type d -exec chmod 750 {} \;
sudo find /var/www/wordpress/ -type f -exec chmod 640 {} \;
```

### 6.2. Setup wordpress config file

Generate secure authentication keys and salts:

```
curl -s https://api.wordpress.org/secret-key/1.1/salt/
```

This command will output a block of code similar to the following. **Copy the entire output** as you'll need to paste it in the next step:

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


Edit the WordPress configuration file:
```
sudo nano /var/www/wordpress/wp-config.php
```

**Locate the section with the placeholder authentication keys (around line 50)** that looks like this:

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

**Delete these placeholder lines and paste the keys you copied from the previous step in their place.**

**Next, locate the database configuration section** and update it with your actual database credentials:

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

**Finally, add the following line** to allow WordPress to directly manage its files (important for plugin/theme installations and updates):

```
define('FS_METHOD', 'direct');
```

Save and close the file.

<br>
</details>

<details markdown='1'>
<summary>
7. Complete the Installation via Web Browser
</summary>

---

Open your web browser and navigate to your domain:
`http://www.386387.xyz`

You should see the WordPress installation wizard. Follow the on-screen instructions to complete the setup.

**Recommended Next Step:** For security and SEO benefits, consider adding SSL/HTTPS to your site. Refer to the [Certbot Tutorial](certbot.html) for instructions on setting up free Let's Encrypt certificates.

</details>

