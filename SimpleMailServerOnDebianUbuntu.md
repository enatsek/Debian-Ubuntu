##### SimpleMailServerOnDebianUbuntu 
# Mail Server with SMTP and IMAP on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>
---
Based on the valuable documents at: [server-world.info](https://www.server-world.info/en/note?os=Ubuntu_18.04&p=mail&f=1)

SMTP: Postfix  
IMAP: Dovecot  
No virtual domains, only Linux users will have email accounts  
Tried to be as simple as possible

Hostname: mail.386387.xyz  
Mail Domain: 386387.xyz  
Operating System: Debian 12/11 or Ubuntu 24.04/22.04 LTS Server  
My User Name: exforge

An MX record must be created at the DNS Server with the value of  mail.386387.xyz

<br>
</details>

<details markdown='1'>
<summary>
1. Install and Configure Postfix
</summary>
---
### 1.0. Update Repositories
```
sudo apt update
```

### 1.1. Install Postfix and SASL (Simple Auth. & Security Layer)
```
sudo apt -y install postfix sasl2-bin 
```

Select No configuration at the install question, we will configure it manually.

### 1.2. Create a standart config file for postfix
```
sudo cp /usr/share/postfix/main.cf.dist /etc/postfix/main.cf
```

### 1.3. Edit postfix config file as described
```
sudo nano /etc/postfix/main.cf 
```

around line 78-82: uncomment

```
mail_owner = postfix
```

around line 94-98: uncomment and change hostname

```
myhostname = mail.386387.xyz
```

around line 102-106: uncomment and change domainname

```
mydomain = 386387.xyz
```

around line 123-127: uncomment

```
myorigin = $mydomain
```

around line 137-141: uncomment

```
inet_interfaces = all
```

around line 185-189: uncomment

```
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
```

around line 228-232: uncomment

```
local_recipient_maps = unix:passwd.byname $alias_maps
```

around line 270-277: uncomment

```
mynetworks_style = subnet
```

around line 287-294: add your local network

```
mynetworks = 127.0.0.0/8, 10.0.0.0/24
```

around line 407-416: uncomment

```
alias_maps = hash:/etc/aliases
```

around line 418-427: uncomment

```
alias_database = hash:/etc/aliases
```

around line 440-449: uncomment

```
home_mailbox = Maildir/
```

around line 576-585: change the line as below  
(remove `$mail_name (Ubuntu)  (Debian/GNU) for Debian`)

From:

```
#smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)
```

To:

```
smtpd_banner = $myhostname ESMTP
```

around line 650 - 659: add/change

```
sendmail_path = /usr/sbin/postfix
```

around line 655 - 664: add/change

```
newaliases_path = /usr/bin/newaliases
```

around line 660 - 669: add/change

```
mailq_path = /usr/bin/mailq
```

around line 666 - 675: add/change

```
setgid_group = postdrop
```

around line 670 - 679: comment out

```
#html_directory =
```

around line 674 - 683: comment out

```
#manpage_directory =
```

around line 679 - 688: comment out

```
#sample_directory =
```

around line 683 - 692: comment out

```
#readme_directory =
```

add to the end: 


```
# limit email size to 10MB
message_size_limit = 10485760
# limit mailbox size to 1GB
mailbox_size_limit = 1073741824
# SMTP-Auth setting
smtpd_sasl_type = dovecot
smtpd_sasl_path = private/auth
smtpd_sasl_auth_enable = yes
smtpd_sasl_security_options = noanonymous
smtpd_sasl_local_domain = $myhostname
smtpd_recipient_restrictions = permit_mynetworks, permit_auth_destination, permit_sasl_authenticated, reject
```

### 1.4. Activate Aliases (Will be explained at 5.2.) 
```
sudo newaliases
```

### 1.5. Restart Postfix
```
sudo systemctl restart postfix 
```

<br>
</details>

<details markdown='1'>
<summary>
2. Install and Configure Dovecot
</summary>
---
### 2.1. Install Dovecot core, pop3 and imap deamons
```
sudo apt -y install dovecot-core dovecot-pop3d dovecot-imapd 
```

### 2.2. Dovecot main config
```
sudo nano /etc/dovecot/dovecot.conf
```

around line 30: uncomment

```
listen = *, ::
```

### 2.3. Dovecot auth config
```
sudo nano /etc/dovecot/conf.d/10-auth.conf
```

around line 10: uncomment and change ( allow plain text auth )

```
disable_plaintext_auth = no
```

around line 100: add/change

```
auth_mechanisms = plain login
```

### 2.4. Dovecot mail config
```
sudo nano /etc/dovecot/conf.d/10-mail.conf
```

around line 30: change to Maildir

```
mail_location = maildir:~/Maildir
```

### 2.5. Dovecot master config
```
sudo nano /etc/dovecot/conf.d/10-master.conf
```

around line 107: uncomment and add

```
# Postfix smtp-auth
unix_listener /var/spool/postfix/private/auth {
    mode = 0666
    user = postfix
    group = postfix
}
```

### 2.6. Restart Dovecot
```
sudo systemctl restart dovecot 
```

<br>

---
</details>

<details markdown='1'>
<summary>
**Break Time**
</summary>

At this point we have a very basic mail config, all our linux users at  mail.386387.xyz have mail addresses. They can access smtp at port 25 and imap at port 143. But unfortunately there is no encryption. 

At the next step we will add SSL encrytpion and that will change our smtp  port to 587.

We will use Certbot tool of Let's Encrypt to have a free certificate

---

<br>
</details>

<details markdown='1'>
<summary>
3. Add SSL/TLS to Postfix and Dovecot
</summary>
---
### 3.1. Install Certbot to get TLS certificates
```
sudo apt -y install certbot
```

### 3.2. Run certbot to get certificates. 
Enter an email address and accept # TOS.

```
sudo certbot certonly --standalone -d mail.386387.xyz
```

Certificates are installed to /etc/letsencrypt/live/mail.386387.xyz/

### 3.3. Add certificates to Postfix main config
```
sudo nano /etc/postfix/main.cf 
```

Add to the end

```
smtpd_use_tls = yes
smtp_tls_mandatory_protocols = !SSLv2, !SSLv3
smtpd_tls_mandatory_protocols = !SSLv2, !SSLv3
smtpd_tls_cert_file = /etc/letsencrypt/live/mail.386387.xyz/fullchain.pem
smtpd_tls_key_file = /etc/letsencrypt/live/mail.386387.xyz/privkey.pem
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
```

### 3.4. Postfix master config
```
sudo nano /etc/postfix/master.cf
```

Around line 17 - 19 uncomment like below

```
submission inet n       -       y       -       -       smtpd
  -o syslog_name=postfix/submission
#  -o smtpd_tls_security_level=encrypt
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_tls_auth_only=yes
```

**For Ubuntu 22.04 and Debian 11**  
Around line 29-33: uncomment like below

```
smtps     inet  n       -       y       -       -       smtpd
  -o syslog_name=postfix/smtps
  -o smtpd_tls_wrappermode=yes
```

**For Ubuntu 24.04 and Debian 12** 
Around line 36: insert below lines

```
smtps     inet  n       -       y       -       -       smtpd
  -o syslog_name=postfix/smtps
  -o smtpd_tls_wrappermode=yes
```

### 3.5. Add certificates to Dovecot config
```
sudo nano /etc/dovecot/conf.d/10-ssl.conf
```

Around line 12: Specify certificates (change as below)  
Remember to change domain names to yours:  

```
ssl_cert = </etc/letsencrypt/live/mail.386387.xyz/fullchain.pem
ssl_key = </etc/letsencrypt/live/mail.386387.xyz/privkey.pem
```

### 3.6. Restart Postfix and Dovecot
```
sudo systemctl restart postfix dovecot 
```

<br>
</details>

<details markdown='1'>
<summary>
4. Client Mail Settings
</summary>
---
For Linux User exforge at mail.386387.xyz  

- Replace all occurences of:
   - exforge --> your user name
   - mail.386387.xyz --> your server name
   - 386387.xyz --> your domain

**Thunderbird Config:**

- Your name: Exforge
- Email address: exforge@386387.xyz
- Password: (Your Linux Password)
- Incoming: IMAP  mail.386387.xyz  	143  STARTTLS  Normal password
- Outgoing: SMTP  mail.386387.xyz  	465  SSL/TLS   Normal password
- Username: Incoming: exforge    	Outgoing: exforge
    


<br>
</details>

<details markdown='1'>
<summary>
5. Account Management
</summary>
---
### 5.1. Users
All Linux users already have mail accounts with their login names and passwords.

To add a new mail user, you need to add a user to your server

```
sudo useradd -d /home/exforge -m exforge
```

And you need to give her a password too

```
sudo passwd exforge
```

### 5.2. Aliases
If you want to use aliases, say postmaster and abuse for user exforge.

First create Linux users

```
sudo useradd -d /home/postmaster -m postmaster
sudo useradd -d /home/abuse -m abuse
sudo passwd postmaster
sudo passwd abuse
```

Add them to /etc/aliases file

```
sudo nano /etc/aliases
```

Fill as below:

```
# See man 5 aliases for format
postmaster: exforge
abuse: exforge
```

Activate aliases

```
sudo newaliases
```

### 5.3. Restart Postfix and Dovecot
```
sudo systemctl restart postfix dovecot
```
</details>



