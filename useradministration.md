---
title: "User and Group Administration"
description: "User and group management essentials"
sidebar: 
   label: User and Group Administration
---

##### User and group management essentials

## 0. Specs
---

### 0.1. The What

This tutorial covers basic user and group administration on Debian 13/12 and Ubuntu 24.04/22.04 Servers.

The commands and concepts also work on Debian, Ubuntu, and their derivatives' desktop environments (Ubuntu, Kubuntu, Xubuntu, Lubuntu, MX Linux, Mint, etc.).


### 0.2. Sources

- [Deepseek](https://www.deepseek.com/)
- [ChatGPT](https://chatgpt.com/)
- [Claude](https://claude.ai/)


<br>

## 1. User Add and Delete
---

Add two new users (`jdoe` and `jdoe2`) with home directories and bash as their default shell:

```bash
sudo useradd -m -s /bin/bash jdoe
sudo useradd -m -s /bin/bash jdoe2
```

Verify that the users were created successfully:

```bash
id jdoe
grep jdoe /etc/passwd
```


Change a user's password interactively:

```bash
sudo passwd jdoe
```

Change a user's password non-interactively (useful for scripts):

```bash
echo "jdoe:SecurePass123" | sudo chpasswd
```

Delete a user and their home directory:

```bash
sudo userdel -r jdoe
```

<br>

## 2. User Information Files
---

**/etc/passwd file:**
This file contains user account information. Each line represents one user with fields separated by colons.

```text
exforge:x:1000:1000:Exforge,,,:/home/exforge:/bin/bash
```

Format: `username:password:UID:GID:GECOS:home_directory:shell`

- **Username:** User login name
- **Password:** `x` indicates the password is stored in `/etc/shadow`
- **UID:** User ID number
- **GID:** Primary group ID number
- **GECOS:** Comment field (typically full name and contact information)
- **Home directory:** User's home directory path
- **Shell:** User's default shell


***/etc/shadow file:***

This secure file contains encrypted passwords and password aging information.

```text
exforge:$6$z09H4l.6$h....A/tDL0:18221:0:99999:7:::
```

Format: `username:password:last_change:min_age:max_age:warn:inactive:expire`

- **Username:** User login name
- **Password:** Encrypted password hash
- **last_change:** Days since Jan 1, 1970 that password was last changed
- **min_age:** Minimum days required between password changes
- **max_age:** Maximum days password is valid
- **warn:** Days before password expires that user is warned
- **inactive:** Days after password expires until account is disabled
- **expire:** Date when account will be disabled


**/etc/skel directory:**
The contents of this directory are copied to new users' home directories when their accounts are created. You can place default configuration files (like `.bashrc`, `.profile`) here.

<br>

## 3. Root user
---

The root account is locked by default in Ubuntu and optionally locked in Debian during installation.

To set a password for root (which unlocks the account):

```bash
sudo passwd
```

To switch to the root account temporarily without unlocking it (uses your sudo privileges):

```bash
sudo -i
```

To switch to another user (requires the target user's password):

```bash
su - username
```

To switch to another user using sudo privileges (doesn't require the target user's password):

```bash
sudo su - username
```

<br>

## 4. Batch User Creation
---

Create a text file for user data:

```bash
touch users.txt
```

Set secure permissions on the file:

```bash
chmod 600 users.txt
```

Add user information to the file:

```bash
sudo nano users.txt
```

Use the following format: `username:password:UID:GID:full_name:home_directory:shell`

```text
user1:password:::User1:/home/user1:/bin/bash
user2:password:::User2:/home/user2:/bin/bash
user3:password:::User3:/home/user3:/bin/bash
```

Process the file to create the users:

```bash
sudo newusers users.txt
```

Verify the users were created:

```bash
grep -E 'user1|user2|user3' /etc/passwd
```

**Security Note:** It's good practice to change the users' passwords after batch creation, as the plaintext passwords in the file may be a security risk:

```bash
sudo passwd user1
```
<br>

## 5. Group Management

---

View your current group memberships:

```bash
groups
```

Or view all groups on the system:

```bash
cat /etc/group  
```

The `/etc/group` file format is similar to `/etc/passwd`: `group_name:password:GID:user_list`


Create new groups:

```bash
sudo groupadd admins
sudo groupadd admins2
```

Delete a group:

```bash
sudo groupdel admins2
```

List members of a specific group:

```bash
getent group admins
```

Add a user to a group as a secondary group membership:

```bash
sudo usermod -aG admins jdoe
sudo usermod -a -G admins user1
```

Change a user's primary group:

```bash
sudo usermod -g admins jdoe
```

Remove a user from a group:

```bash
sudo gpasswd -d user1 admins
```

<br>

## 6. User Account Modifications
---

Change a user's home directory and move the contents:

```bash
sudo usermod -d /home/jsmith -m jdoe
```

Change a username:

```bash
sudo usermod -l jsmith jdoe
```

Lock a user account (prevents login):

```bash
sudo passwd -l user1
```

Unlock a user account:

```bash
sudo passwd -u user1
```

View password expiration information:

```bash
sudo chage -l user1
```

<br>

## 7. sudo Group

---

Members of the `sudo` group can use the `sudo` command to execute commands with elevated privileges.

Configure sudo privileges:

```bash
sudo visudo
```

This command safely edits the sudo configuration file (`/etc/sudoers`) in the default editor.

**Example sudoers configurations with explanations:**

Allow all members of the sudo group to run any command as any user:

```text
%sudo   ALL=(ALL:ALL) ALL
# %sudo  - All members of the 'sudo' group
# ALL    - From any terminal/host
# (ALL:ALL) - Can run commands as ANY user and ANY group
# ALL    - Can run ANY command
```

Specific user restriction - user `charlie` can only run `apt` as user `dscully` and group `admins` on host `ubuntu-server`:

```text
charlie  ubuntu-server=(dscully:admins) /usr/bin/apt
# charlie        - Username
# ubuntu-server  - Only on this specific host
# (dscully:admins) - Can run commands as user dscully and group admins
# /usr/bin/apt   - Only the apt command
```

Allow user `ansible` to run any command without a password prompt:

```bash
ansible ALL=(ALL) NOPASSWD: ALL
```

View your current sudo privileges:

```bash
sudo -l
```

