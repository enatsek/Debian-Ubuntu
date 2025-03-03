##### ADOnDebianUbuntu  
# Simple Active Directory Configuration on Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.1. Definition
- Single Domain Active Directory infrastructure with Debian or Ubuntu  Servers with 2 Domain Controllers and a file server.
- Windows workstations can join to AD.
- No license costs except Windows workstation licences.
- Based on the valuable documents at: [Server-World](https://www.server-world.info/en/note?os=Ubuntu_18.04&p=samba&f=4)

### 0.2. Configuration
- Domain Name: 386387.XYZ  
- Domain Netbios Name: 386387  
- First DC:  
    - srv1.386387.xyz   
    - 192.168.1.221   
    - Debian 12/11 or Ubuntu 24.04/22.04 LTS Server
- Second DC:    
    - srv2.386387.xyz 
    - 192.168.1.222 
    - Debian 12/11 or Ubuntu 24.04/22.04 LTS Server
- File Server: 
    - filesrv.386387.xyz 
    - 192.168.1.223 
    - Debian 12/11 or Ubuntu 24.04/22.04 LTS Server
- Windows workstations can connect to the domain


- Groups and Users:
  - Marketing:
     - mrk01, mrk02, mrk03
  - Sales:
     - sls01, sls02, sls03
  - Production:
     - prd01, prd02, prd03
  - IT:
     - it01, it02, it03, support
  - SysAdmin:
     - support
  - All:
     - all of the users


- File server shares:

```
//filesrv/Xmrk01    mrk01 RW
//filesrv/Xmrk02    mrk02 RW
//filesrv/Xmrk03    mrk03 RW
//filesrv/XMrk      Marketing RW
//filesrv/XMrkPub   Marketing RW, All R
//filesrv/Xsls01    sls01 RW
//filesrv/Xsls02    sls02 RW
//filesrv/Xsls03    sls03 RW
//filesrv/XSls      Sales RW
//filesrv/XSlsPub   Sales RW, All R
//filesrv/Xprd01    prd01 RW
//filesrv/Xprd02    prd02 RW
//filesrv/Xprd03    prd03 RW
//filesrv/XPrd      Production RW
//filesrv/XPrdPub   Production RW, All R
//filesrv/Xit01     it01 RW
//filesrv/Xit02     it02 RW
//filesrv/Xit03     it03 RW
//filesrv/Xsupport  support RW
//filesrv/XIT       IT RW
//filesrv/XITPub    IT RW, All R
//filesrv/XSys      SysAdmin RW
//filesrv/XSysPub   SysAdmin RW, All R
//filesrv/XAll      ALL RW
```

On my tests I used distros uniformly. That is all servers were Debian 11, Debian 12, Ubuntu 22.04, or Ubuntu 24.04. I believe the system would work with nonuniform distros too, but I haven't tested it.

### 0.3. Phases
- Add First DC (srv1.x36.org)
- Add Additional DC (srv2.386387.xyz)
- AD User Management
- Add a Linux File Server to the Domain (filesrv.386387.xyz)
- Add a Windows Computer to the Domain

### 0.4. Preliminary Tasks
There are some important matters to consider. Not complying them can  cause some problems.

#### 0.4.1. Choosing Domain Name and Realm
Realm is in the domain name format and Domain Name is a single  word (actually Netbios Name of your domain).

If your company's internet domain name is example.com, then you can  choose your Realm and Domain Name as following:

Realm : EXAMPLE.COM  
Domain Name : EXAMPLE

Whenever you use them, they must be UPPERCASE. Don't ask me why, that is  something about Micros*ft's bad design.

#### 0.4.2. IP Address and Host Name for Domain Controllers and Domain Members

Domain Controllers and Domain Members should have static IP addresses. 

There might be some ways to use DHCP but I don't know how and actually I don't see any reason to use DHCP for Domain Controllers.

Hostname must be in the format of name.example.com (lowercase this time)  and due to an incompatability with Samba and Debian/Ubuntu (Actually all  Debian based Linuxes) you have to erase the line starting with 127.0.1.1
(not 127.0.0.1) from your /etc/hosts file and add the IP and hostname  (short and long formats) in your /etc/hosts file as in below.

```
127.0.0.1       localhost
192.168.1.221	srv1.386387.xyz srv1
```
 
#### 0.4.3. Mixed Environment
You should have at least 2 DCs (Domain Controllers), you can use 1  Wind*ws and 1 Linux to benefit from Micros*ft's AD Management programs.  

But actually it is not necessary. 

I'd advice installing all DCs as Linux  and use any Windxws workstation to manage AD. You can install RSAT Management Tools to a Windxws workstation and use AD Manager programs (including DNS and WINS server) from there.

#### 0.4.4. Default Values 
Remember to replace all the occurences of 386387, x386, 386387.XYZ, and  386387.xyz with yours, regarding the cases. 

<br>
</details>

<details markdown='1'>
<summary>
1. Add First Domain Controller
</summary>
---
### 1.0. Specs
```
Domain Name:  386387
Realm:        386387.XYZ	
Hostname:     srv1.386387.xyz
IP:           192.168.1.221
```

### 1.1. Set Hostname
Set hostname as fully qualified (if you haven't done it before)

```
sudo hostnamectl set-hostname srv1.386387.xyz
```

Update /etc/hosts file

```
sudo nano /etc/hosts
```

Change the start of the file as below:

```
127.0.0.1       localhost
192.168.1.221   srv1.386387.xyz srv1 
```

### 1.2. Install required packages
```
sudo apt update
sudo apt -y install samba krb5-config winbind smbclient 
```

Answers to parameter questions:  

- Default Kerberos version 5 realm:
   - 386387.XYZ
- Kerberos servers for your realm:
   - srv1.386387.xyz
- Administrative server for your Kerberos realm:
   - srv1.386387.xyz

### 1.2. Run Samba Config

Backup original samba configuration

```
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.original 
```

Run provision tool to create the Domain

```
sudo samba-tool domain provision
```

Answers to parameter questions:

- Realm:
   - 386387.XYZ
- Domain: 
   - 386387
- Server Role (dc, member, standalone) [dc]: 
   - Just press enter
- DNS backend (SAMBA_INTERNAL,...
   - Just press enter
- DNS forwarder IP address...
   - Enter your DNS address, or you may enter 8.8.8.8
- Administrator password:
   - Enter a good password

### 1.3. Copy kerberos config file, stop and disable unnecessary services
```
sudo cp /var/lib/samba/private/krb5.conf /etc/
sudo systemctl stop smbd nmbd winbind systemd-resolved
sudo systemctl disable smbd nmbd winbind systemd-resolved
sudo systemctl unmask samba-ad-dc 
```

Debian 12 gives the following error, ignore it:

`Failed to stop systemd-resolved.service: Unit systemd-resolved.service not loaded.`

### 1.4. Remove resolv.conf and create a new one
```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Fill as below

```
domain 386387.xyz
nameserver 127.0.0.1
```

### 1.5. Start DC Services
```
sudo systemctl start samba-ad-dc
sudo systemctl enable samba-ad-dc 
```

Check domain level

```
sudo samba-tool domain level show
```

Create a domain user named exforge

```
sudo samba-tool user create exforge
```
<br>
</details>

<details markdown='1'>
<summary>
2. Add Additional DC
</summary>
---
## 2.0. Specs
```
Domain Name:      386387
Realm:            386387.XYZ	
Hostname:         srv2.386387.xyz
IP:               192.168.1.222
Org. DC Hostname: srv1.386387.xyz
Org. DC IP:       192.168.1.221
```

### 2.1. Set Hostname
Set hostname as fully qualified (if you haven't done it before)

```
sudo hostnamectl set-hostname srv2.386387.xyz
```

Update /etc/hosts file

```
sudo nano /etc/hosts
```

Change the start of the file as below:

```
127.0.0.1       localhost
192.168.1.222   srv2.386387.xyz srv2 
```

### 2.2. Install kerberos and edit configuration
```
sudo apt update
sudo apt -y install krb5-user
```

Pass all the questions with enter

```
sudo nano /etc/krb5.conf 
```

Change the beginning of the file as below

```
[libdefaults]
        default_realm = 386387.XYZ
        dns_lookup_realm = false
        dns_lookup_kdc = true
```

### 2.3. Stop and disable systemd.resolved
This step is not necessary for Debian 12

```
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved 
```

### 2.4. Remove resolv.conf and create a new one
```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Add following lines

```
domain 386387.xyz
nameserver 192.168.1.221
```

### 2.5. Get Kerberos ticket
Domain Admin password will be asked (Entered at 1.2.)

```
sudo kinit administrator
```

Check Kerberos ticket

```
sudo klist
```

### 2.6. Add This DC to Existing AD
Add necessary packages 

```
sudo apt -y install samba winbind smbclient 
```

Rename and remove default samba config, create a new one

```
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.org 
sudo samba-tool domain join 386387.XYZ DC -U "srv1\administrator" \
   --dns-backend=SAMBA_INTERNAL 
```

### 2.7. Close and disable unnecessary services and enable samba
```
sudo systemctl stop smbd nmbd winbind
sudo systemctl disable smbd nmbd winbind
sudo systemctl unmask samba-ad-dc
sudo systemctl start samba-ad-dc
sudo systemctl enable samba-ad-dc
```

### 2.8. Verify 
Verify authentication to localhost

```
sudo smbclient //127.0.0.1/netlogon -U Administrator -c 'ls'
```

Verify replication status with AD

```
sudo samba-tool drs showrepl
```

Following warning is not important, you can ignore it:  
       `Warning: No NC replicated for Connection!`

<br>
</details>

<details markdown='1'>
<summary>
3. AD User & Computer Management
</summary>
---

You can run on any DC
### 3.1. User Management
#### 3.1.0. See All Commands
```
sudo samba-tool user --help
```

#### 3.1.1. Display domain users list.
```
sudo samba-tool user list
```

Display DN info instead of user names

```
sudo samba-tool user list --full-dn
```

#### 3.1.2. Add a domain user.
```
sudo samba-tool user create ubuntu
```

Force to change password at next login

```
sudo samba-tool user create ubuntu2 --must-change-at-next-login
```
 
#### 3.1.3. Delete a domain user.
```
sudo samba-tool user delete ubuntu2
```

#### 3.1.4. Reset password of a user.
```
sudo samba-tool user setpassword ubuntu
```
 
#### 3.1.5. Set expiration for a user.
User will be disabled at expiration

```
sudo samba-tool user setexpiry ubuntu --days=7
```

Remove expiration

```
sudo samba-tool user setexpiry --noexpiry ubuntu
```
 
#### 3.1.6. Disable/Enable user account.
```
sudo samba-tool user disable ubuntu
sudo samba-tool user enable ubuntu
```

#### 3.1.7. Show information about a user
```
sudo samba-tool user show ubuntu
```
 
#### 3.1.8. Edit details of a user
```
sudo samba-tool user edit ubuntu
```

You can edit the details in an editor, be careful.
 
### 3.2. Group Management
#### 3.2.0. See All Commands
```
sudo samba-tool group --help
```

#### 3.2.1. Display domain group list.
```
sudo samba-tool group list
```

#### 3.2.2. Display members in a group.
```
sudo samba-tool group listmembers "Domain Users"
```
 
#### 3.2.3. Add a domain group.
```
sudo samba-tool group add TestUsers
sudo samba-tool group add TestUsers2
```
 
#### 3.2.4. Delete a domain group.
```
sudo samba-tool group delete TestUsers2
```

#### 3.2.5. Add/remove a member from a domain group.
```
sudo samba-tool group addmembers TestUsers ubuntu
sudo samba-tool group removemembers TestUsers ubuntu
```

#### 3.2.6. Show information about a group
```
sudo samba-tool group show TestUsers
```

#### 3.2.7. Edit details of a group
```
sudo samba-tool group edit TestUsers
```

### 3.3. Computer Management
#### 3.3.0. See All Commands
```
sudo samba-tool computer --help
```

#### 3.3.1. List Domain Computers
```
sudo samba-tool computer list
```

#### 3.3.2. Show details of a domain computer
```
sudo samba-tool computer show srv1
```

#### 3.3.2. Edit details of a domain computer
```
sudo samba-tool computer edit srv1
```

### 3.4. Other Important Management Subcommands
#### 3.4.1. Check local AD database for errors.
```
sudo samba-tool dbcheck --help
```

#### 3.4.2. Delegation management.
```
sudo samba-tool delegation --help
```

#### 3.4.3. Domain Name Service (DNS) management.
```
sudo samba-tool dns --help
```

#### 3.4.4. Domain management
```
sudo samba-tool domain --help
```

#### 3.4.5. Directory Replication Services (DRS) management.
```
sudo samba-tool drs --help
```

#### 3.4.6. Forest management
```
sudo samba-tool forest --help
```

#### 3.4.7. Flexible Single Master Operations (FSMO) roles management.
```
sudo samba-tool fsmo --help
```

#### 3.4.8. Group Policy Object (GPO) management.
```
sudo samba-tool gpo --help
```

#### 3.4.9. Organizational Units (OU) management.
```
sudo samba-tool ou --help
```

#### 3.4.10. Schema querying and management.
```
sudo samba-tool schema --help
```

#### 3.4.11. Sites management.
```
sudo samba-tool sites --help
```

#### 3.4.12. Retrieve the time on a server.
```
sudo samba-tool time --help
```

<br>
</details>

<details markdown='1'>
<summary>
4. Create Users and Groups
</summary>
---
### 4.1. Create Users
Create all users with Password1 as the default password. Users are going to have to change their password at their first logon.

```
sudo samba-tool user add mrk01 Password1 --given-name=Mrk --surname=01 \
    --must-change-at-next-login
sudo samba-tool user add mrk02 Password1 --given-name=Mrk --surname=02 \
    --must-change-at-next-login
sudo samba-tool user add mrk03 Password1 --given-name=Mrk --surname=03 \
    --must-change-at-next-login
sudo samba-tool user add sls01 Password1 --given-name=Sls --surname=01 \
    --must-change-at-next-login
sudo samba-tool user add sls02 Password1 --given-name=Sls --surname=02 \
    --must-change-at-next-login
sudo samba-tool user add sls03 Password1 --given-name=Sls --surname=03 \
    --must-change-at-next-login
sudo samba-tool user add prd01 Password1 --given-name=Prd --surname=01 \
    --must-change-at-next-login
sudo samba-tool user add prd02 Password1 --given-name=Prd --surname=02 \
    --must-change-at-next-login
sudo samba-tool user add prd03 Password1 --given-name=Prd --surname=03 \
    --must-change-at-next-login
sudo samba-tool user add it01 Password1 --given-name=IT --surname=01 \
    --must-change-at-next-login
sudo samba-tool user add it02 Password1 --given-name=IT --surname=02 \
    --must-change-at-next-login
sudo samba-tool user add it03 Password1 --given-name=IT --surname=03 \
    --must-change-at-next-login
sudo samba-tool user add support Password1 --given-name=Support --surname=User \
    --must-change-at-next-login
```

### 4.2. Create Groups
```
sudo samba-tool group add Marketing
sudo samba-tool group add Sales
sudo samba-tool group add Production
sudo samba-tool group add IT
sudo samba-tool group add SysAdmin
sudo samba-tool group add All
```

### 4.3. Add Users to the Corresponding Groups
```
sudo samba-tool group addmembers Marketing mrk01,mrk02,mrk03
sudo samba-tool group addmembers Sales sls01,sls02,sls03
sudo samba-tool group addmembers Production prd01,prd02,prd03
sudo samba-tool group addmembers IT it01,it02,it03,support
sudo samba-tool group addmembers SysAdmin support
sudo samba-tool group addmembers All Marketing,Sales,Production,IT,SysAdmin
```

<br>
</details>

<details markdown='1'>
<summary>
5. Install and Configure the File Server
</summary>
---
### 5.1. Set Hostname and DNS Information
Set hostname as fully qualified (if you haven't done it before)

```
sudo hostnamectl set-hostname filesrv.386387.xyz
```

Update /etc/hosts file

```
sudo nano /etc/hosts
```

Change the start of the file as below:

```
127.0.0.1       localhost
192.168.1.223   filesrv.386387.xyz filesrv 
```
 
Remove resolv.conf and create a new one

```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Add following lines

```
domain 386387.xyz
nameserver 192.168.1.221
nameserver 192.168.1.222
```

### 5.2. Install necessary packages
```
sudo apt update
sudo apt -y install winbind libpam-winbind libnss-winbind krb5-config \
   samba-dsdb-modules samba-vfs-modules 
```

Answers to parameter questions (if asked):

- Default Kerberos version 5 realm:
   - 386387.XYZ
- Kerberos servers for your realm:
   - srv1.386387.xyz
- Administrative server for your Kerberos realm:
   - srv1.386387.xyz

### 5.3. Configure Winbind
#### 5.3.1. Samba config
```
sudo nano /etc/samba/smb.conf 
```

Change/add following lines under [global] stanza

```
   workgroup = 386387
   realm = 386387.XYZ
   security = ads
   idmap config * : backend = tdb
   idmap config * : range = 3000-7999
   idmap config 386387 : backend = rid
   idmap config 386387 : range = 10000-999999
   template homedir = /home/%U
   template shell = /bin/bash
   winbind use default domain = true
   winbind offline logon = false
```

#### 5.3.2. pam config
```
sudo nano /etc/pam.d/common-session 
```

Add following line

```
session optional        pam_mkhomedir.so skel=/etc/skel umask=077
```

### 5.4. Join AD
#### 5.4.1. Add this server to AD 
```
sudo net ads join -U Administrator
```

Restart winbind
```
sudo systemctl restart winbind
```

#### 5.4.2. Show Domain Users
```
sudo wbinfo -u
```

### 5.5. Config File Server
#### 5.5.0. Specs
There will be 24 shares: 

```
/srv/shares/Xmrk01    mrk01 RW
/srv/shares/Xmrk02    mrk02 RW
/srv/shares/Xmrk03    mrk03 RW
/srv/shares/XMrk      Marketing RW
/srv/shares/XMrkPub   Marketing RW, All R
/srv/shares/Xsls01    sls01 RW
/srv/shares/Xsls02    sls02 RW
/srv/shares/Xsls03    sls03 RW
/srv/shares/XSls      Sales RW
/srv/shares/XSlsPub   Sales RW, All R
/srv/shares/Xprd01    prd01 RW
/srv/shares/Xprd02    prd02 RW
/srv/shares/Xprd03    prd03 RW
/srv/shares/XPrd      Production RW
/srv/shares/XPrdPub   Production RW, All R
/srv/shares/Xit01     it01 RW
/srv/shares/Xit02     it02 RW
/srv/shares/Xit03     it03 RW
/srv/shares/Xsupport  support RW
/srv/shares/XIT       IT RW
/srv/shares/XITPub    IT RW, All R
/srv/shares/XSys      SysAdmin RW
/srv/shares/XSysPub   SysAdmin RW, All R
/srv/shares/XAll      ALL RW
```

Create shared folders:

```
sudo mkdir -p /srv/shares/Xmrk01
sudo mkdir -p /srv/shares/Xmrk02
sudo mkdir -p /srv/shares/Xmrk03
sudo mkdir -p /srv/shares/XMrk
sudo mkdir -p /srv/shares/XMrkPub
sudo mkdir -p /srv/shares/Xsls01
sudo mkdir -p /srv/shares/Xsls02
sudo mkdir -p /srv/shares/Xsls03
sudo mkdir -p /srv/shares/XSls
sudo mkdir -p /srv/shares/XSlsPub
sudo mkdir -p /srv/shares/Xprd01
sudo mkdir -p /srv/shares/Xprd02
sudo mkdir -p /srv/shares/Xprd03
sudo mkdir -p /srv/shares/XPrd
sudo mkdir -p /srv/shares/XPrdPub
sudo mkdir -p /srv/shares/Xit01
sudo mkdir -p /srv/shares/Xit02
sudo mkdir -p /srv/shares/Xit03
sudo mkdir -p /srv/shares/Xsupport
sudo mkdir -p /srv/shares/XIT
sudo mkdir -p /srv/shares/XITPub
sudo mkdir -p /srv/shares/XSys
sudo mkdir -p /srv/shares/XSysPub
sudo mkdir -p /srv/shares/XAll
```

Set Permissions to full, we are going to set permissions on the shares too

```
sudo chmod -R 777 /srv/shares 
```

#### 5.5.1. Install Samba
```
sudo apt -y install samba
```
 
#### 5.5.2. Configure samba for AD file server
```
sudo nano /etc/samba/smb.conf
```

Add following lines under [global]  stanza

```
   netbios name = filesrv         
   socket options = TCP_NODELAY SO_RCVBUF=16384 SO_SNDBUF=16384         
   idmap uid = 10000-20000         
   winbind enum users = yes         
   winbind gid = 10000-20000         
   os level = 20         
   winbind enum groups = yes         
   password server = *         
   preferred master = no         
   winbind separator = +         
   encrypt passwords = yes         
   dns proxy = no         
   wins server = 192.168.1.221         
   wins proxy = no  
```

Add following lines at the end of the file  
!!! Remember to change them according to your shares !!!

```
# Marketing
[Xmrk01]
   comment = Xmrk01
   path = /srv/shares/Xmrk01         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = mrk01
   write list = mrk01
[Xmrk02]
   comment = Xmrk02
   path = /srv/shares/Xmrk02         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = mrk02
   write list = mrk02
[Xmrk03]
   comment = Xmrk03
   path = /srv/shares/Xmrk03         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = mrk03
   write list = mrk03
[XMrk]
   comment = XMrk
   path = /srv/shares/XMrk         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = @Marketing
   write list = @Marketing
[XMrkPub]         
   comment = XMrkPub         
   path = /srv/shares/XMrkPub         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770
   valid users = @Marketing, @All         
   read list = @All
   write list = @Marketing
# Sales
[Xsls01]
   comment = Xsls01
   path = /srv/shares/Xsls01         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = sls01
   write list = sls01
[Xsls02]
   comment = Xsls02
   path = /srv/shares/Xsls02         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = sls02
   write list = sls02
[Xsls03]
   comment = Xsls03
   path = /srv/shares/Xsls03         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = sls03
   write list = sls03
[XSls]
   comment = XSls
   path = /srv/shares/XSls         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = @Sales
   write list = @Sales
[XSlsPub]         
   comment = XSlsPub         
   path = /srv/shares/XSlsPub         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770
   valid users = @Sales, @All         
   read list = @All
   write list = @Sales
# Production
[Xprd01]
   comment = Xprd01
   path = /srv/shares/Xprd01         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = prd01
   write list = prd01
[Xprd02]
   comment = Xprd02
   path = /srv/shares/Xprd02         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = prd02
   write list = prd02
[Xprd03]
   comment = Xprd03
   path = /srv/shares/Xprd03         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = prd03
   write list = prd03
[XPrd]
   comment = XPrd
   path = /srv/shares/XPrd         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = @Production
   write list = @Production
[XPrdPub]         
   comment = XPrdPub         
   path = /srv/shares/XPrdPub         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770
   valid users = @Production, @All         
   read list = @All
   write list = @Production
# IT
[Xit01]
   comment = Xit01
   path = /srv/shares/Xit01         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = it01
   write list = it01
[Xit02]
   comment = Xit02
   path = /srv/shares/Xit02         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = it02
   write list = it02
[Xit03]
   comment = Xit03
   path = /srv/shares/Xit03         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = it03
   write list = it03
[Xsupport]
   comment = Xsupport
   path = /srv/shares/Xsupport         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = support
   write list = support
[XIT]
   comment = XIT
   path = /srv/shares/XIT         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = @IT
   write list = @IT
[XITPub]         
   comment = XITPub         
   path = /srv/shares/XITPub         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770
   valid users = @IT, @All         
   read list = @All
   write list = @IT
# All
[XAll]
   comment = XAll
   path = /srv/shares/XAll         
   browseable = yes         
   read only = no         
   create mask = 770         
   directory mask = 770         
   valid users = @All
   write list = @All
```

#### 5.5.3. Restart Samba
```
sudo systemctl restart smbd
```

<br>
</details>

<details markdown='1'>
<summary>
6. Add Windows Computers to the Domain 
</summary>
---
Change Windows computer's DNS setting to first DC and proceed as usual.

AD (including the DNS server on DC) could be managed through windows  workstation after installing RSAT management.

You can connect to the file server using \\srvf\share1 (share2,3,4) notation from your workstation.
</details>

