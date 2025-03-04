##### UserAndGroupAdminOnDebianUbuntu 
# User and Group Administration on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
Aimed for Debian 12/11 and Ubuntu 24.04/22.04 Servers

But works fine on Debian, Ubuntu and derivatives' desktops (Ubuntu, Kubuntu, Xubuntu,  Lubuntu, MX, Mint etc) too.

Based on the book [Mastering Ubuntu Server 2nd Ed.](https://www.packtpub.com/networking-and-servers/mastering-ubuntu-server-second-edition) by Jay LaCroix. 

<br>
</details>

<details markdown='1'>
<summary>
1. User Add and Delete
</summary>

---
### 1.1. Add a new user jdoe and create home folder
```
sudo useradd -d /home/jdoe -m jdoe
```

### 1.2. Change a user's password
```
sudo passwd jdoe
```

### 1.3. Delete a user
```
sudo userdel jdoe
```

Remove home directory too

```
sudo userdel -r jdoe
```

<br>
</details>

<details markdown='1'>
<summary>
2. Files of User Information
</summary>

---
### 2.1. /etc/passwd file
```
exforge:x:1000:1000:Exforge,,,:/home/exforge:/bin/bash
username:pw:UID:GID:Name,Surname,XX:homefolder:shell
```

### 2.2. /etc/shadow file
Passwords are stored as hashed in shadow file

```
exforge:$6$z09H4l.6$h....A/tDL0:18221:0:99999:7:::
username:pwHash:DatesSinceLastPwChange:MinDaysToChangePw:
  MaxDaysToChangePw:DaysBeforeUserWarnedToChangePw:
  DaysToPwExpire:DaysToUserDisable
```

### 2.3. User pw information extracted from /etc/shadow
```
sudo passwd -S username
```

### 2.4. Default contents for home folders:
Contents of /etc/skel folder is distributed to created user's home directory

<br>
</details>

<details markdown='1'>
<summary>
3. root user
</summary>

---
### 3.1. root is locked by default in Ubuntu. It is optional in  Debian.
To give a pw to (and unlock) root

```
sudo passwd
```

### 3.2. switch to root account without unlocking it
```
sudo -i
```

### 3.3. switch to another user (if you know pw)
```
su - username
```

### 3.4. switch to another user (if you don't know pw)
```
sudo su - username
```

<br>
</details>

<details markdown='1'>
<summary>
4. Batch user add
</summary>

---
### 4.1. Create a text file for users
```
touch users.txt
```

### 4.2. Change the permissions of the file
```
chmod 600 users.txt
```

### 4.3. Add users information to the file
```
sudo nano users.txt
```

Fill as below:

```
user1:password:::User1:/home/user1:/bin/bash
user2:password:::User2:/home/user2:/bin/bash
user3:password:::User3:/home/user3:/bin/bash
#username:passwd:uid:gid:full name:home_dir:shell
```

### 4.4. Process file to add users
```
sudo newusers users.txt
```

You can check users from /etc/passwd


### 4.5. It is a good idea to change passwords of the users
```
sudo passwd user1
```
<br>
</details>

<details markdown='1'>
<summary>
5. Group Management
</summary>

---
### 5.1. List of groups
```
groups
```

or

```
cat /etc/group  
```

it is similar to /etc/password

### 5.2. Add a new group
```
sudo groupadd admins
```

### 5.3. Delete a group
```
sudo groupdel admins
```

### 5.4. List members of a group
```
getent group groupname
```

### 5.5. Add a user to a group
 -a append new group to groups of user  
 -G as a secondary group

```
sudo usermod -aG admins myuser
sudo usermod -a -G admins myuser
```

or

```
sudo gpasswd -a <username> <group>
```

### 5.6. Change a users primary group
```
sudo usermod -g admins myuser
```

### 5.7. Remove user from a group
```
sudo gpasswd -d <username> <grouptoremove>
```

<br>
</details>

<details markdown='1'>
<summary>
6. User manipulation
</summary>

---
## 6.1. Change username
First change home directory

```
sudo usermod -d /home/jsmith -m jdoe 
```

Then change username

```
sudo usermod -l jsmith jdoe
```

### 6.2. Lock a user
```
sudo passwd -l <username>
```

### 6.3. unlock
```
sudo passwd -u <username>
```

### 6.4. Password expiration info
```
sudo chage -l <username>
```

<br>
</details>

<details markdown='1'>
<summary>
7. sudo Group
</summary>

---
Members of sudo group can use sudo command

### 7.1. Configuration of sudo group members
```
sudo visudo
```

Opens the sudo configuration file in the default editor (Generally vim or nano)

Below is a sample file with explanations:

```
%sudo	ALL=(ALL:ALL) ALL
# sudo group members
#  can use sudo from any terminal
#  can use sudo to impersonate any user
#  can use sudo to impersonate any group
#  can use sudo for any command

charlie  ubuntu-server=(dscully:admins) /usr/bin/apt
#__________________________________
#  user charlie, 
#   can only use sudo on ubuntu_server
#   can only impersonate dscully user
#   can only impersonate admins group
#   can only run /usr/bin/apt

#  For a user to sudo without passwd
ansible ALL=(ALL) NOPASSWD: ALL
```

### 7.2. List granted sudo privileges
```
sudo -l
```

</details>

