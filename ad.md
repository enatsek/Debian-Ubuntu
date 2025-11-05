##### Active Directory on Debian and Ubuntu  
# Simple Active Directory Configuration on Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. The What
We will install a single-domain Active Directory infrastructure using Debian or Ubuntu Servers.

- **2 Domain Controllers** and **1 File Server**.
- Windows workstations will be able to join the domain.
- **No license costs**, except for the Windows workstation licenses.

### 0.1. Environment

- **Domain Name:** `386387.XYZ`
- **Domain NetBIOS Name:** `386387`
- **First DC:**
    - `srv1.386387.xyz`
    - `192.168.1.201`
    - Debian 13/12 or Ubuntu 24.04/22.04 LTS Server
- **Second DC:**
    - `srv2.386387.xyz`
    - `192.168.1.202`
    - Debian 13/12 or Ubuntu 24.04/22.04 LTS Server
- **File Server:**
    - `filesrv.386387.xyz`
    - `192.168.1.203`
    - Debian 13/12 or Ubuntu 24.04/22.04 LTS Server
- Windows workstations will be able to connect to the domain.


- **Groups and Users:**
  - **Marketing:** mrk01, mrk02, mrk03
  - **Sales:** sls01, sls02, sls03
  - **Production:** prd01, prd02, prd03
  - **IT:** it01, it02, it03, support
  - **SysAdmin:** support
  - **All:** all of the above users


- **File Server Shares:**

```
//filesrv/Xmrk01    mrk01 (RW)
//filesrv/Xmrk02    mrk02 (RW)
//filesrv/Xmrk03    mrk03 (RW)
//filesrv/XMrk      Marketing (RW)
//filesrv/XMrkPub   Marketing (RW), All (R)
//filesrv/Xsls01    sls01 (RW)
//filesrv/Xsls02    sls02 (RW)
//filesrv/Xsls03    sls03 (RW)
//filesrv/XSls      Sales (RW)
//filesrv/XSlsPub   Sales (RW), All (R)
//filesrv/Xprd01    prd01 (RW)
//filesrv/Xprd02    prd02 (RW)
//filesrv/Xprd03    prd03 (RW)
//filesrv/XPrd      Production (RW)
//filesrv/XPrdPub   Production (RW), All (R)
//filesrv/Xit01     it01 (RW)
//filesrv/Xit02     it02 (RW)
//filesrv/Xit03     it03 (RW)
//filesrv/Xsupport  support (RW)
//filesrv/XIT       IT (RW)
//filesrv/XITPub    IT (RW), All (R)
//filesrv/XSys      SysAdmin (RW)
//filesrv/XSysPub   SysAdmin (RW), All (R)
//filesrv/XAll      All (RW)
```

In my tests, I used distributions uniformly (i.e., all servers were either Debian 12, Debian 13, Ubuntu 22.04, or Ubuntu 24.04). I believe the system would work with a mix of distributions, but this has not been tested.

### 0.3. Phases
- Add First DC (`srv1.386387.xyz`)
- Add Additional DC (`srv2.386387.xyz`)
- AD User Management
- Add a Linux File Server to the Domain (`filesrv.386387.xyz`)
- Add a Windows Computer to the Domain

### 0.4. Preliminary Tasks
There are some important considerations. Not complying with them can cause problems.

#### 0.4.1. Choosing Domain Name and Realm
The Realm is in the domain name format, and the Domain Name is a single word (the NetBIOS name of your domain).

If your company's internet domain name is `example.com`, you can choose your Realm and Domain Name as follows:
- **Realm:** `EXAMPLE.COM`
- **Domain Name:** `EXAMPLE`

Whenever you use them, they must be in **UPPERCASE**. This is due to a design choice in Microsoft's implementation.

#### 0.4.2. IP Address and Hostname for Domain Controllers and Domain Members

Domain Controllers and Domain Members should have static IP addresses.

While there might be ways to use DHCP, it is not recommended for Domain Controllers, and the method is beyond this guide's scope.

The hostname must be in the format `name.example.com` (lowercase). Due to an incompatibility between Samba and Debian/Ubuntu (and other Debian-based distributions), you must remove the line starting with `127.0.1.1` (not `127.0.0.1`) from your `/etc/hosts` file and add the server's IP and hostname (both short and FQDN) as shown below.

**Example `/etc/hosts`:**
```
127.0.0.1       localhost
192.168.1.201   srv1.386387.xyz srv1
```

 
#### 0.4.3. Mixed Environment
You should have at least 2 Domain Controllers (DCs). You could use one Windows and one Linux DC to benefit from Microsoft's native AD management tools, but this is not necessary.

I recommend installing all DCs on Linux and using a Windows workstation with RSAT (Remote Server Administration Tools) installed to manage AD. This allows you to use the standard AD management programs (including for DNS) from a familiar environment.

#### 0.4.4. Default Values
Remember to replace all occurrences of `386387`, `386387.XYZ`, and `386387.xyz` with your own values, respecting the case.

### 0.5. Sources
- Based on the valuable documentation at: [Server-World](https://www.server-world.info/en/note?os=Ubuntu_18.04&p=samba&f=4)

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
IP:           192.168.1.201
```

### 1.1. Set Hostname
Set the hostname to the fully qualified domain name (if not done already):

```
sudo hostnamectl hostname srv1.386387.xyz
```

Update the /etc/hosts file

```
sudo nano /etc/hosts
```

Modify the beginning of the file as follows:

```
127.0.0.1       localhost
192.168.1.201   srv1.386387.xyz srv1 
```

### 1.2. Install required packages

```
sudo apt update
sudo apt -y install samba krb5-config winbind smbclient 
```

Provide the following answers to the configuration prompts:
- **Default Kerberos version 5 realm:** `386387.XYZ`
- **Kerberos servers for your realm:** `srv1.386387.xyz`
- **Administrative server for your Kerberos realm:** `srv1.386387.xyz`


### 1.3. Run Samba Configuration

Backup the original samba configuration:

```
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.original 
```

Run the domain provisioning tool:

```
sudo samba-tool domain provision
```

Provide the following answers:
- **Realm:** `386387.XYZ`
- **Domain:** `386387`
- **Server Role (dc, member, standalone) [dc]:** Press Enter
- **DNS backend (SAMBA_INTERNAL,...:** Press Enter
- **DNS forwarder IP address...:** Enter your DNS server (e.g., `8.8.8.8`)
- **Administrator password:** Enter a strong password

### 1.4. Copy Kerberos Config, Stop and Disable Services

```
sudo cp /var/lib/samba/private/krb5.conf /etc/
sudo systemctl stop smbd nmbd winbind systemd-resolved
sudo systemctl disable smbd nmbd winbind systemd-resolved
sudo systemctl unmask samba-ad-dc 
```

**Note:** On Debian 12, you may see an error `Failed to stop systemd-resolved.service: Unit systemd-resolved.service not loaded.` This can be safely ignored.

### 1.5. Recreate resolv.conf

```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Add the following lines:

```
domain 386387.xyz
nameserver 127.0.0.1
```

### 1.5. Start DC Services
```
sudo systemctl start samba-ad-dc
sudo systemctl enable samba-ad-dc 
```

Check the domain functional level:

```
sudo samba-tool domain level show
```

Create a test domain user:

```
sudo samba-tool user create exforge
```
<br>
</details>

<details markdown='1'>
<summary>
2. Add Additional Domain Controller
</summary>

---
## 2.0. Specs
```
Domain Name: 386387
Realm:       386387.XYZ	
Hostname:    srv2.386387.xyz
IP:          192.168.1.202
Original DC: srv1.386387.xyz (192.168.1.201)
```

### 2.1. Set Hostname
Set hostname as fully qualified (if you haven't done it before)

```
sudo hostnamectl hostname srv2.386387.xyz
```

Update the /etc/hosts file

```
sudo nano /etc/hosts
```

Modify the beginning of the file as follows:

```
127.0.0.1       localhost
192.168.1.202   srv2.386387.xyz srv2 
```

### 2.2. Install Kerberos and Edit Configuration

```
sudo apt update
sudo apt -y install krb5-user
```

(Press Enter through all prompts; we will configure manually.)

Edit the Kerberos configuration:
```
sudo nano /etc/krb5.conf 
```

Ensure the beginning of the file contains:

```
[libdefaults]
        default_realm = 386387.XYZ
        dns_lookup_realm = false
        dns_lookup_kdc = true
```

### 2.3. Stop and disable systemd.resolved
*This step is typically not necessary for Debian 12/13.*

```
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved 
```

### 2.4. Recreate resolv.conf

```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Add the following lines (pointing to the first DC):

```
domain 386387.xyz
nameserver 192.168.1.201
```

### 2.5. Obtain a Kerberos Ticket

You will be prompted for the Domain Administrator password (set during provisioning in section 1.3).

```
sudo kinit administrator
```

Verify the Kerberos ticket:

```
sudo klist
```

### 2.6. Add This DC to Existing AD

Install necessary packages:

```
sudo apt -y install samba winbind smbclient 
```

Back up and remove the default Samba config, then join the domain:

```
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.org 
sudo samba-tool domain join 386387.XYZ DC -U "srv1\administrator" \
   --dns-backend=SAMBA_INTERNAL 
```

### 2.7. Stop, Disable Old Services, and Enable Samba AD DC

```
sudo systemctl stop smbd nmbd winbind
sudo systemctl disable smbd nmbd winbind
sudo systemctl unmask samba-ad-dc
sudo systemctl start samba-ad-dc
sudo systemctl enable samba-ad-dc
```

### 2.8. Verification

Verify authentication locally:

```
sudo smbclient //127.0.0.1/netlogon -U Administrator -c 'ls'
```

Check replication status:

```
sudo samba-tool drs showrepl
```

**Note:** The warning `Warning: No NC replicated for Connection!` is not critical and can be ignored initially.

<br>
</details>

<details markdown='1'>
<summary>
3. AD User & Computer Management
</summary>

---

*These commands can be run on any Domain Controller.*

### 3.1. User Management

View all user-related commands:

```
sudo samba-tool user --help
```

List domain users:

```
sudo samba-tool user list
```

List users with full Distinguished Name (DN):

```
sudo samba-tool user list --full-dn
```

Create a domain user:

```
sudo samba-tool user create ubuntu
```

Create a user forced to change password at next login:

```
sudo samba-tool user create ubuntu2 --must-change-at-next-login
```
 
Delete a domain user:

```
sudo samba-tool user delete ubuntu2
```

Reset a user's password:

```
sudo samba-tool user setpassword ubuntu
```
 
Set an expiration date for a user account:

```
sudo samba-tool user setexpiry ubuntu --days=7
```

Remove expiration from a user account:

```
sudo samba-tool user setexpiry --noexpiry ubuntu
```
 
Disable/Enable a user account:

```
sudo samba-tool user disable ubuntu
sudo samba-tool user enable ubuntu
```

Show user details:

```
sudo samba-tool user show ubuntu
```
 
Edit user details (opens in a text editor):

```
sudo samba-tool user edit ubuntu
```
 
### 3.2. Group Management

View all group-related commands:

```
sudo samba-tool group --help
```

List domain groups:

```
sudo samba-tool group list
```

List members of a specific group:

```
sudo samba-tool group listmembers "Domain Users"
```
 
Create a new domain group:

```
sudo samba-tool group add TestUsers
sudo samba-tool group add TestUsers2
```
 
Delete a domain group:

```
sudo samba-tool group delete TestUsers2
```

Add/Remove a member to/from a group:

```
sudo samba-tool group addmembers TestUsers ubuntu
sudo samba-tool group removemembers TestUsers ubuntu
```

Show group details:

```
sudo samba-tool group show TestUsers
```

Edit group details (opens in a text editor):

```
sudo samba-tool group edit TestUsers
```

### 3.3. Computer Management

View all computer-related commands:

```
sudo samba-tool computer --help
```

List domain computers:

```
sudo samba-tool computer list
```

Show computer details:

```
sudo samba-tool computer show srv1
```

Edit computer details (opens in a text editor):

```
sudo samba-tool computer edit srv1
```

### 3.4. Other Important Management Subcommands

Check the local AD database for errors:

```
sudo samba-tool dbcheck --help
```

Manage delegation:

```
sudo samba-tool delegation --help
```

Manage DNS:

```
sudo samba-tool dns --help
```

Domain management:

```
sudo samba-tool domain --help
```

Manage Directory Replication Services (DRS):

```
sudo samba-tool drs --help
```

Forest management:

```
sudo samba-tool forest --help
```

Manage Flexible Single Master Operations (FSMO) roles:

```
sudo samba-tool fsmo --help
```

Manage Group Policy Objects (GPO):

```
sudo samba-tool gpo --help
```

Manage Organizational Units (OU):

```
sudo samba-tool ou --help
```

Schema querying and management:

```
sudo samba-tool schema --help
```

Sites management:

```
sudo samba-tool sites --help
```

Retrieve the time from a server:

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

Create all users with `Password1` as the default password. Users will be required to change their password at first logon.

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

Set the hostname:

```
sudo hostnamectl hostname filesrv.386387.xyz
```

Update `/etc/hosts`:

```
sudo nano /etc/hosts
```

Modify the beginning of the file:

```
127.0.0.1       localhost
192.168.1.203   filesrv.386387.xyz filesrv 
```
 
Recreate `/etc/resolv.conf`:

```
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
```

Add:

```
domain 386387.xyz
nameserver 192.168.1.201
nameserver 192.168.1.202
```

### 5.2. Install necessary packages
```
sudo apt update
sudo apt -y install winbind libpam-winbind libnss-winbind krb5-config \
   samba-dsdb-modules samba-vfs-modules 
```

Provide the following answers if prompted:
- **Default Kerberos version 5 realm:** `386387.XYZ`
- **Kerberos servers for your realm:** `srv1.386387.xyz`
- **Administrative server for your Kerberos realm:** `srv1.386387.xyz`

### 5.3. Configure Winbind

#### 5.3.1. Configure Samba

```
sudo nano /etc/samba/smb.conf 
```

Add/Modify the following lines in the `[global]` section:

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

#### 5.3.2. Configure PAM to Create Home Directories

```
sudo nano /etc/pam.d/common-session 
```

Add the following line:

```
session optional        pam_mkhomedir.so skel=/etc/skel umask=077
```

### 5.4. Join the AD Domain

Join the server to the domain:

```
sudo net ads join -U Administrator
```

Restart the winbind service:

```
sudo systemctl restart winbind
```

Verify domain users are visible:

```
sudo wbinfo -u
```

### 5.5. Configure the File Server

#### 5.5.0. Share Specifications

There will be 24 shares. Create the directory structure:

```
sudo mkdir -p /srv/shares/{Xmrk01,Xmrk02,Xmrk03,XMrk,XMrkPub,Xsls01,Xsls02,Xsls03,XSls,XSlsPub,Xprd01,Xprd02,Xprd03,XPrd,XPrdPub,Xit01,Xit02,Xit03,Xsupport,XIT,XITPub,XSys,XSysPub,XAll}
```

Set initial permissions (more specific permissions will be set via Samba):

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

Add the following lines to the `[global]` section:

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
   wins server = 192.168.1.201         
   wins proxy = no  
```

Add the following share definitions to the end of the file. **Remember to replace `386387` with your domain NetBIOS name if different.**

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

1.  On the Windows computer, configure its DNS settings to point to your Domain Controllers (e.g., `192.168.1.201` and `192.168.1.202`).
2.  Proceed with the standard "Join a Domain" process through System Properties, using the domain name (`386387`) and an administrative account.
3.  After joining, you can install **RSAT (Remote Server Administration Tools)** on the Windows workstation to manage AD, DNS, and other services.
4.  You can connect to the file shares using `\\filesrv\ShareName` (e.g., `\\filesrv\XMrk`) from any domain-joined Windows computer.

</details>

