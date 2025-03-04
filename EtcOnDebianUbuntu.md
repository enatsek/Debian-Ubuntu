##### EtcOnDebianUbuntu 
# /etc/ Folder on Debian and Ubuntu

<details markdown='1'>
<summary>
Specs
</summary>

---
### Info
/etc directory is a crucial part of the filesystem hierarchy. It stands for "et cetera" and is used to store system-wide configuration files and directories. 

These configuration files control various aspects of the operating system, services, and installed applications (virtually everything) on Linux.

I tried to cover all the files and folders under /etc/ for efault install Debian 12 (without GUI) and Ubuntu 24.04 Server edition. I added some (IMHO) important packages too. 

### Sources
[ChatGPT](https://chatgpt.com) (I tested everything that she says).  

[Debian](https://manpages.debian.org/) and [Ubuntu](https://manpages.ubuntu.com/) man pages 

<br>
</details>

<details markdown='1'>
<summary>
/etc/.pwd.lock
</summary>

---
File exists in default Ubuntu & Debian installations.

Used by the system to prevent multiple simultaneous changes to the system password database.

The lckpwdf() and ulckpwdf() functions enable modification access to the password databases through this lock file. 

A process first uses lckpwdf() to lock the lock file, thereby gaining exclusive rights to modify the /etc/passwd or /etc/shadow password database. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/.updated
</summary>

---
File does not exists in default Debian installations. 
File exists in default Ubuntu installations.

This file is updated by systemd-update-done.service when it updates /usr directory to place a timestamp.

Sample content on Ubuntu:

```
# This file was created by systemd-update-done. Its only 
# purpose is to hold a timestamp of the time this directory
# was updated. See man:systemd-update-done.service(8).
TIMESTAMP_NSEC=1713865027000000000
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/adduser.conf
</summary>

---
File exists in default Ubuntu & Debian installations.
Used to configure default settings for the adduser and addgroup commands which are used for creating new users and groups on the system.

Sample content:

```
# /etc/adduser.conf: `adduser' configuration.
# See adduser(8) and adduser.conf(5) for full documentation.
#
# A commented out setting indicates that this is the default in the
# code. If you need to change those settings, remove the comment and
# make your intended change.
#
# The login shell to be used for all new users.
# Default: DSHELL=/bin/bash
#DSHELL=/bin/bash
#
# The directory in which new home directories should  be  created.
# Default: DHOME=/home
# DHOME=/home
#
# The directory from which skeletal user configuration files
# will be copied.
# Default: SKEL=/etc/skel
#SKEL=/etc/skel
#
# Specify inclusive ranges of UIDs and GIDs from which UIDs and GIDs
# for system users, system groups, non-system users and non-system groups
# can be dynamically allocated.
# Default: FIRST_SYSTEM_UID=100, LAST_SYSTEM_UID=999
#FIRST_SYSTEM_UID=100
#LAST_SYSTEM_UID=999
#
# Default: FIRST_SYSTEM_GID=100, LAST_SYSTEM_GID=999
#FIRST_SYSTEM_GID=100
#LAST_SYSTEM_GID=999
#
# Default: FIRST_UID=1000, LAST_UID=59999
#FIRST_UID=1000
#LAST_UID=59999
#
# Default: FIRST_GID=1000, LAST_GID=59999
#FIRST_GID=1000
#LAST_GID=59999
#
# Specify a file or a directory containing UID and GID pool.
#UID_POOL=/etc/adduser-pool.conf
#UID_POOL=/etc/adduser-pool.d/
#GID_POOL=/etc/adduser-pool.conf
#GID_POOL=/etc/adduser-pool.d/
#
# Specify whether each created non-system user will be
# given their own group to use.
# Default: USERGROUPS=yes
#USERGROUPS=yes
#
# Defines the groupname or GID of the group all newly-created
# non-system users are placed into.
# It is a configuration error to define both variables
# even if the values are consistent.
# Default: USERS_GID=undefined, USERS_GROUP=users
#USERS_GID=100
#USERS_GROUP=users
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/adjtime
</summary>

---
File exist in default Debian installations.

File does not exist in default Ubuntu installations.

Used to store the hardware clock's (Real-Time Clock or RTC) time adjustment information.

The Hardware Clock is usually not very accurate. However, much of its inaccuracy is completely predictable - it gains or loses the same amount of time every day. This is called systematic drift.

Sample content:

```
0.000000 1692481832 0.000000
1692481832
UTC
```
 
Explanations:  

- First line: Three numbers, separated by blanks.
   - Drift factor: The systematic drift rate in seconds per day
   - Last adjust time: The resulting number of seconds since 1969 UTC of most recent adjustment or calibration.
   - Adjustment status: 0
- Second line : Last calibration time. The resulting number of seconds since 1969 UTC of most recent calibration. Zero if there has been no calibration yet.
- Third line: Clock mode: UTC or LOCAL.

<br>
</details>

<details markdown='1'>
<summary>
/etc/aliases
</summary>

---
File doesn't exist in default Ubuntu & Debian installations.

Used with Postfix (Sendmail), for defining email aliases. 

Require newaliases command to rebuild the alias database and apply the changes.

Sample content:

```
# alias: address1, address2, ...
root: admin@example.com
webmaster: admin@example.com
postmaster: admin@example.com
sales: sales@example.com, manager@example.com
support: support@example.com
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/alternatives/ Folder
</summary>

---
Folder exists in default Ubuntu & Debian installations.

In this folder there are symbolic links pointing to the currently selected default version of a particular program or utility.

Using the update-alternatives command, administrators can manage these symbolic links to change the default version of a program.

An excerpt from directory list:

```
lrwxrwxrwx  1 root root   13 Jun 17  2022 awk -> /usr/bin/mawk
lrwxrwxrwx  1 root root    9 Jan 18  2023 editor -> /bin/nano
lrwxrwxrwx  1 root root   17 May  4  2023 ex -> /usr/bin/vim.tiny
lrwxrwxrwx  1 root root   14 Feb 12  2023 lzcat -> /usr/bin/xzcat
lrwxrwxrwx  1 root root   14 Feb 12  2023 lzcmp -> /usr/bin/xzcmp
lrwxrwxrwx  1 root root   15 Feb 12  2023 lzdiff -> /usr/bin/xzdiff
lrwxrwxrwx  1 root root   16 Feb 12  2023 lzegrep -> /usr/bin/xzegrep
lrwxrwxrwx  1 root root   11 Feb 12  2023 lzma -> /usr/bin/xz
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/apache2/ Folder
</summary>

---
Folder doesn't exist in default Ubuntu & Debian installations. 

Created after installing Apache2 package. Contains Apache2 web server configuration settings.

Some files and folder:

- apache2.conf: The main configuration file for Apache. Contains global configuration directives that apply to the entire server.
- ports.conf: Specifies the ports on which the server listens for incoming connections. 
- envvar: Script used to set environment variables for the Apache HTTP Server process. 
- magic: contains definitions used by the Apache identify file types based on their content. This file is used by Apache's mod_mime_magic module.
- conf-available/ and conf-enabled/: Contains configuration files for various components of Apache. Configuration files placed in conf-available/ can be enabled by creating symbolic links to them in conf-enabled/.
- mods-available/ and mods-enabled/: Contains Apache modules. Modules in mods-available/ can be enabled by creating symbolic links to them in mods-enabled/.
- sites-available/ and sites-enabled/: Contains configuration files for Apache virtual hosts (websites). Virtual hosts defined in sites-available/ can be enabled by creating symbolic links to them in sites-enabled/.

<br>
</details>

<details markdown='1'>
<summary>
/etc/apparmor/ Folder and /etc/apparmor.d/ Folder
</summary>

---
Folders exist in default Ubuntu & Debian installations.

/etc/apparmor.d/ contains configuration files that define the access control policies for various applications and services running on the system.

/etc/apparmor/ folder contains the configuration for apparmor itself.

Excerpt from /etc/apparmor/parser.conf

```
# parser.conf is a global AppArmor config file for the apparmor_parser

# It can be used to specify the default options for the parser, which
# can then be overriden by options passed on the command line.
#
# Leading whitespace is ignored and lines that begin with # are treated
# as comments.

# Config options are specified one per line using the same format as the
# longform command line options (without the preceding --).

# If a value is specified twice the last version to appear is used.

## Suppress Warnings
#quiet
#
## Be verbose
#verbose
## Set additional include path
#Include /etc/apparmor.d/
# or
#Include /usr/share/apparmor
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/apport/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for Apport, a system crash and problem reporting tool. 

Apport is designed to automatically collect information about crashes and other system errors, allowing users to report them to developers or package maintainers for analysis and debugging.

Some files and folders:

- apport.conf: Global options for apport.
- crashdb.conf: Behavior of Apport's crash database, such as the database backend to use, authentication credentials, and other database options.
- blacklist.d/ : Contains configuration files that specify which executables or packages should be excluded from Apport's error reporting. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/apt/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and directories related to the Advanced Package Tool (APT).

Some files and folders:

- sources.list: Specifies package repositories from which APT retrieves packages. Each line in these files typically represents a repository, including its URL and additional options. 
- auth.conf.d/: Contains authentication configuration. This folder is empty by default.
- apt.conf.d/: Contains configuration files that control various aspects of APT's behavior. These files allow you to configure options such as proxy # settings, package cache management, authentication settings, and more.
- keyrings/: Contains the system's default keyring files used by APT to verify the authenticity of packages retrieved from repositories.
- listchanges.d/: Configuration files for the apt-listchanges tool. apt-listchanges is a utility that displays a summary of package changes or release notes before installing or upgrading packages using APT.
- preferences.d/: Contains configuration files that control package installation preferences. Allows to specify preferences for certain packages versions, influencing APT's decision-making process when resolving package  dependencies and upgrades.
- sources.list.d/: Additional repository configurations that are included alongside the main sources.list file.
- trusted.gpg.d/: Contains additional trusted GPG keys that users or administrators have manually added to the system for package verification.

<br>
</details>

<details markdown='1'>
<summary>
/etc/bash_completion
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains the script used to configure bash completion functionality for the Bash shell.

In Debian and Ubuntu contains the path of the script.

Sample content:

```
. /usr/share/bash-completion/bash_completion
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/bash_completion.d/ Folder
</summary>

---
Folder does not exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains additional scripts for bash completion functionality. 

Sample content:

```
# /etc/bash_completion.d/git-prompt
# In git versions < 1.7.12, this shell library was part of the
# git completion script.

# Some users rely on the __git_ps1 function becoming available
# when bash-completion is loaded.  Continue to load this library
# at bash-completion startup for now, to ease the transition to a
# world order where the prompt function is requested separately.

if [[ -e /usr/lib/git-core/git-sh-prompt ]]; then
        . /usr/lib/git-core/git-sh-prompt
fi
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/bash.bashrc
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains system-wide initialization script for the Bash shell. 

Executed whenever Bash is started for interactive login shells.

Contains global settings, aliases, shell options and environment variables.

Excerpt from contents:

```
# If not running interactively, don't do anything
[ -z "$PS1" ] && return
# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize
# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/bind/ Folder
</summary>

---
Folder doesn't exist in default Ubuntu & Debian installations. 

Created after installing bind package. Contains DNS server settings.

Contains configuration files and related directories for the BIND DNS server. 

Bind is one of the most commonly used DNS (Domain Name System) servers on the internet.

Some files:

- bind.keys: This file contains the shared secrets used for DNSSEC (Domain Name System Security Extensions) operations and communication between DNS servers.
- db.*: Zone files used by BIND for various purposes, such as mapping IP addresses to domain names (db.0, db.127, db.255), specifying local network configuration (db.local), and providing responses for nonexistent domains (db.empty).
- named.conf: Main configuration file for BIND. It typically includes other configuration files such as named.conf.options, named.conf.local, and named.conf.default-zones.
- named.conf.default-zones: Contains default zone definitions provided by the BIND package.
- named.conf.local: Used for configuring local zones specific to the server. It often includes zone definitions for domains hosted on the local BIND server.
- named.conf.options: Contains global configuration options for BIND, such as listening addresses, logging settings, and default query behavior.

<br>
</details>

<details markdown='1'>
<summary>
/etc/bindresvport.blacklist
</summary>

---
File exists in default Debian & Ubuntu installations.

Specifies ports that should not be bound to by privileged programs using "reserved ports". 

Reserved ports are typically below 1024, and traditionally, only privileged processes could bind to these ports.

Sample Content

```
# This file contains a list of port numbers between 600 and 1024,
# which should not be used by bindresvport. bindresvport is mostly
# called by RPC services. This mostly solves the problem, that a
# RPC service uses a well known port of another service.

631     # cups
636     # ldaps
655     # tinc
774     # rpasswd
783     # spamd
873     # rsync
921     # lwresd
993     # imaps
995     # pops
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/binfmt.d Folder
</summary>

---
Folder exists and is empty in default Debian & Ubuntu installations.

Used to configure Binary Format (binfmt) handlers. 

Binfmt is a feature of the Linux kernel that allows execution of binary  files in different formats by automatically invoking the appropriate  interpreter or virtual machine.

Sample content:

```
# /etc/binfmt.d/wine.conf
# Start WINE on Windows executables
:DOSWin:M::MZ::/usr/bin/wine:
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/blkid.conf
</summary>

---
File doesn't exist in default Debian & Ubuntu installations.

Allows for customization of the behavior of blkid.

Sample content:
```
# Configuration file for blkid(8)

# How to encode whitespace characters in LABEL/UUID. 'b' uses backslash,
# 'h' uses C-style hexadecimal notation, 'e' uses '\040'.
WHITESPACE_ENCODING=b

# How to print whitespace characters in LABEL/UUID. 'b' uses backslash,
# 'h' uses C-style hexadecimal notation, 'e' uses '\040'.
WHITESPACE_PRINT=b

# Whether to use chattr to protect the UUID of filesystems.
PROTECT_UUID=1

# Whether to use fs-cache file.
USE_FS_CACHE=1

# How to escape special characters in LABEL/UUID. 'b' uses backslash,
# 'h' uses C-style hexadecimal notation.
ESCAPE_CHARACTERS=b
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/byobu/ Folder
</summary>

---
Folder does not exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files and scripts related to Byobu.

Byobu is a terminal multiplexer that enhances the functionality of the GNU Screen or tmux utilities.

Sample Contents

```
# /etc/byobu/backend
# BYOBU_BACKEND can currently be "screen" or "tmux"
# Override this on a per-user basis by editing "$BYOBU_CONFIG_DIR/backend"
# or by launching either "byobu-screen" or "byobu-tmux" instead of "byobu".
BYOBU_BACKEND="tmu
```


```
# /etc/byobu/socketdir
# Set the location of the socket directory that byobu will use.
# On Debian/Ubuntu systems, this is in /var/run/screen, but on
# other distros, it might be elsewhere, such as /tmp/screens
# depending on your compilation.

# This file will be sourced by both shell scripts and python code,
# so please ensure that:
#  * the variable name is SOCKETDIR
#  * there is no space around the "="
#  * and that the path value is quoted
SOCKETDIR="/var/run/screen"
```

<br>

</details>

<details markdown='1'>
<summary>
/etc/ca-certificates.conf and /etc/ca-certificates/ Folder
</summary>

---
File and Folder exist in in default Debian & Ubuntu installations.

/etc/ca-certificates/ folder includes only an empty update.d Folder.

/etc/ca-certificates.conf list the certificates to use or ignore to be installed in /etc/ssl/certs.

/etc/ca-certificates/ folder contains the certificates installed manually.
 
Sample /etc/ca-certificates.conf content:

```
# This file lists certificates that you wish to use or to ignore to be
# installed in /etc/ssl/certs.
# update-ca-certificates(8) will update /etc/ssl/certs by reading this file.

# This is autogenerated by dpkg-reconfigure ca-certificates.
# Certificates should be installed under /usr/share/ca-certificates
# and files with extension '.crt' is recognized as available certs.

# line begins with # is comment.
# line begins with ! is certificate filename to be deselected.

mozilla/ACCVRAIZ1.crt
mozilla/AC_RAIZ_FNMT-RCM.crt
mozilla/AC_RAIZ_FNMT-RCM_SERVIDORES_SEGUROS.crt
mozilla/Actalis_Authentication_Root_CA.crt
mozilla/AffirmTrust_Commercial.crt
mozilla/AffirmTrust_Networking.crt
mozilla/AffirmTrust_Premium.crt
mozilla/AffirmTrust_Premium_ECC.crt
mozilla/Amazon_Root_CA_1.crt
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/cloud/ Folder
</summary>

---
Folder does not exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files and scripts related to cloud-init.

Cloud-init is a widely used tool for customizing cloud instances during the initial boot process.

Folders and files in the folder:

- cloud.cfg: The top level settings are used as module and base configuration.
- ds-identify: Used to identify the cloud platform.
- cloud.cfg.d/: Additional configuration snippets that can be included in cloud.cfg.
- clean.d/: Additional clean up scripts for the third party applications when the command `cloud-init clean` is invoked.
- templates/: Template files used by cloud-init to generate configuration files dynamically during the boot process. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/credstore/ and /etc/credstore.encrypted/ Folders
</summary>

---
Folders do not exist in default Debian installations. 
Folders exist in default Ubuntu installations. 
Folders are empty in default Ubuntu installations.

Used by systemd to store and load credentials (and encrypted credentials) of systemd services. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/console-setup Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files for the console font and keyboard layout settings on Debian-based systems. 
These settings affect the text mode console (TTY) during system boot and when accessing the system without a graphical user interface.

<br>
</details>

<details markdown='1'>
<summary>
/etc/crontab and /etc/cron.*/ Folders
</summary>

---
File and folders exist in default Debian & Ubuntu installations.

/etc/crontab file defines system-wide cron jobs that run at specified  intervals according to a predefined schedule.

Sample content:

```
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
```

Each line in /etc/crontab represents a cron job and follows the format:
- minute hour day_of_month month day_of_week user command_to_run

/etc/cron.d/ Folder contains additional cron tasks.

The folders /etc/cron.hourly/, /etc/cron.daily/, /etc/cron.weekly/, /etc/cron.monthly/, and /etc/cron.yearly/ includes additional hourly, daily, weekly, monthly, and yearly cron tasks respectively.

/etc/cron.deny file, which does not exist in default Debian and Ubuntu installations is used to include users who are not allowed to use cron command.

<br>
</details>

<details markdown='1'>
<summary>
/etc/cryptsetup-initramfs/ Folder
</summary>

---
Folder does not exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files of the cryptsetup tool, particularly for setting up encrypted volumes during the initial ramdisk (initramfs) stage of the boot process.

Can contain hooks, configuration options and scripts.

Ubuntu installation includes only conf-hook file.

Excerpt from /etc/cryptsetup-initramfs/conf-hook

```
# Configuration file for the cryptroot initramfs hook.

# KEYFILE_PATTERN: ...

# The value of this variable is interpreted as a shell pattern.
# Matching key files from the crypttab(5) are included in the initramfs
# image.  The associated devices can then be unlocked without manual
# intervention.  (For instance if /etc/crypttab lists two key files
# /etc/keys/{root,swap}.key, you can set KEYFILE_PATTERN="/etc/keys/*.key"
# to add them to the initrd.)

# If KEYFILE_PATTERN if null or unset (default) then no key file is
# copied to the initramfs image.

# Note that the glob(7) is not expanded for crypttab(5) entries with a
# 'keyscript=' option.  In that case, the field is not treated as a file
# name but given as argument to the keyscript.
#KEYFILE_PATTERN=

# ASKPASS: [ y | n ]

# Whether to include the askpass binary to the initramfs image.  askpass
# is required for interactive passphrase prompts, and ASKPASS=y (the
# default) is implied when the hook detects that same device needs to be
# unlocked interactively (i.e., not via keyfile nor keyscript) at
# initramfs stage.  Setting ASKPASS=n also skips `cryptroot-unlock`
# inclusion as it requires the askpass executable.

#ASKPASS=y
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/crypttab
</summary>

---
File does not exist in default Debian installations.  
File exists in default Ubuntu installations.

Describes encrypted block devices that are set up during system boot.

Sample config file

```
# <name>       <source>         <keyfile>       <options>
encrypted_data /dev/sdb1        /etc/keys/encrypted_data.key   luks
```

The encrypted block device /dev/sdb1 is configured to be unlocked during boot using the LUKS encryption format. The encryption key is stored in /etc/keys/encrypted_data.key, and the mapped device is named encrypted_data.

<br>
</details>

<details markdown='1'>
<summary>
/etc/cups/ Folder
</summary>

---
Folder does not exist in default Debian & Ubuntu installations.

Contains configuration files for CUPS (Common UNIX Printing System).

Some files and folders:

- cupsd.conf: Main configuration file for the CUPS printing system. Contains settings related to the CUPS server, such as network interfaces to listen on, access control, printer sharing options, logging settings, etc.
- cup-files.conf: Contains configuration options related to file and directory locations used by CUPS, such as the location of spool directories, temporary files, error logs, and more.
- cups-browsed.conf: Configuration for cups-browsed.
- snmp.conf: Contains configuration options for SNMP support in CUPS.
- interfaces/: Contains configuration files for printer interfaces, such as USB, network, and Bluetooth connections. 
- ppd/: Contains Printer Description Files (PPDs) used by CUPS to describe printer capabilities and settings.
- ssl/: Contains SSL/TLS certificates and keys used for secure communication between CUPS clients and the CUPS server. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/dbus-1/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

In Debian, it has 2 subfolders session.d and system.d both are empy.

In Ubuntu it has 2 same subfolders; session.d is empty.

Contains configuration files for dbus-deamon-1 (Message Bus Deamon).

D-Bus is a library that provides one-to-one communication between any two applications.

dbus-daemon-1 is an application that uses this library to implement a message bus daemon. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/debconf.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Used to configure the behavior of the debconf package, which is a configuration management system for Debian packages. 

Debconf is responsible for handling configuration prompts and managing configuration files during the installation and upgrade of Debian packages.

Excerpt from contents:

```
# Debconf will use this database to store the data you enter into it,
# and some other dynamic data.
Config: configdb
# Debconf will use this database to store static template data.
Templates: templatedb

# World-readable, and accepts everything but passwords.
Name: config
Driver: File
Mode: 644
Reject-Type: password
Filename: /var/cache/debconf/config.dat

# Not world readable (the default), and accepts only passwords.
Name: passwords
Driver: File
Mode: 600
Backup: false
Required: false
Accept-Type: password
Filename: /var/cache/debconf/passwords.dat
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/debian_version
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains the version number of the Debian operating system installed on a system. 

It's a simple way to check which version of Debian is currently running on a machine.

File contents on Debian 12

```
12.4
```

File contents on Ubuntu 24.04

```
trixie/sid
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/default/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files for various system services and utilities.

These configuration files often define default settings, environment variables, and other options that control the behavior of the associated services or utilities.

These files are generally empty (containing only the comments). System admins are expected to change these files based on their needs.

Sample content for /etc/default/ssh

```
# Default settings for openssh-server. This file is sourced by /bin/sh from
# /etc/init.d/ssh.

# Options to pass to sshd
SSHD_OPTS=
```

Sample content for /etc/default/keyboard

```
# KEYBOARD CONFIGURATION FILE
# Consult the keyboard(5) manual page.
XKBMODEL="pc105"
XKBLAYOUT="tr"
XKBVARIANT=""
XKBOPTIONS=""
BACKSPACE="guess"
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/deluser.conf
</summary>

---
File exists in default Ubuntu & Debian installations.

Used to configure default settings for the deluser command.

Sample content:

```
# /etc/deluser.conf: `deluser' configuration.
# See deluser(8) and deluser.conf(5) for full documentation.

# A commented out setting indicates that this is the default in the
# code. If you need to change those settings, remove the comment and
# make your intended change.

# Remove home directory and mail spool when user is removed
# Default: REMOVE_HOME = 0
#REMOVE_HOME = 0

# Remove all files on the system owned by the user to be removed
# Default: REMOVE_ALL_FILES = 0
#REMOVE_ALL_FILES = 0

# Backup files before removing them. This options has only an effect if
# REMOVE_HOME or REMOVE_ALL_FILES is set.
# Default: BACKUP = 0
#BACKUP = 0

# Target directory for the backup file
# Default: BACKUP_TO = "."
#BACKUP_TO = "."
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/depmod.d/ Folder
</summary>

---
Folder does not exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for depmod, a utility that generates modules.dep and map files used by the kernel module loading system.

Linux kernel modules can provide services (called "symbols") for other modules to use If a second module uses this symbol, that second module clearly depends on the first module.

depmod creates a list of module dependencies by reading each module under /lib/modules/version and determining what symbols it exports and what symbols it needs. By default, this list is written to modules.dep.

Default Ubuntu installations has only 1 file named as ubuntu.conf with the following content:

```
search updates ubuntu built-in
```

search keyword allows you to specify the order in which /lib/modules subdirectories will be processed by depmod.

<br>
</details>

<details markdown='1'>
<summary>
/etc/dhcp/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files for DHCP daemon and client.
 
Some files and folders are:

- dhclient.conf: DHCP client configuration.
- dhcpd.conf: DHCP server configuration.
- dhclient-enter-hooks.d/: Scripts to run when certain events occur (such as getting a new DCHP lease).
- dhclient-exit-hooks.d/: Scripts to run when certain events occur (such as exiting DCHP clients).

Sample dhcpd.conf file contents:

```
# /etc/dhcp/dhcpd.conf

# Set the domain name for the DHCP clients
option domain-name "example.com";

# Set the DNS servers to be used by DHCP clients
option domain-name-servers 8.8.8.8, 8.8.4.4;

# Set the default lease time for IP addresses
default-lease-time 600;
# Set the maximum lease time for IP addresses
max-lease-time 7200;

# Define a subnet for the DHCP server to manage
subnet 192.168.1.0 netmask 255.255.255.0 {
    # Specify the range of IP addresses to lease to clients
    range 192.168.1.100 192.168.1.200;
    # Set the gateway (router) for the subnet
    option routers 192.168.1.1;
    # Set the subnet mask
    option subnet-mask 255.255.255.0;
}
```

Sample dhclient.conf file contents:

```
# /etc/dhcp/dhclient.conf

# Request specific DHCP options
request subnet-mask, broadcast-address, routers, domain-name-servers;

# Set a timeout for DHCP requests
timeout 30;

# Use a specific interface for DHCP requests
interface eth0;

# Send a hostname to the DHCP server
send host-name "my-computer";

# Send a domain name to the DHCP server
send domain-name "example.com";

# Set the default route metric
default route metric 100;
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/dhcpcd.conf
</summary>

---
File does not exist in default Debian installations.  
File exists in default Ubuntu installations.

Configuration file used by dhcpcd, a common DHCP (Dynamic Host Configuration Protocol) client for Linux systems. This file is where you configure how the dhcpcd service manages DHCP on your system. 

Sample Contents:

```
# A sample configuration for dhcpcd.
# See dhcpcd.conf(5) for details.

# Allow users of this group to interact with dhcpcd via the control socket.
#controlgroup wheel

# Inform the DHCP server of our hostname for DDNS.
#hostname

# Use the hardware address of the interface for the Client ID.
#clientid
# or
# Use the same DUID + IAID as set in DHCPv6 for DHCPv4 ClientID as per RFC4361.
# Some non-RFC compliant DHCP servers do not reply with this set.
# In this case, comment out duid and enable clientid above.
duid

# Persist interface configuration when dhcpcd exits.
persistent

# vendorclassid is set to blank to avoid sending the default of
# dhcpcd-<version>:<os>:<machine>:<platform>
vendorclassid

# A list of options to request from the DHCP server.
option domain_name_servers, domain_name, domain_search
option classless_static_routes
# Respect the network MTU. This is applied to DHCP routes.
option interface_mtu

# Request a hostname from the network
option host_name

# Most distributions have NTP support.
#option ntp_servers

# Rapid commit support.
# Safe to enable by default because it requires the equivalent option set
# on the server to actually work.
option rapid_commit


# A ServerID is required by RFC2131.
require dhcp_server_identifier

# Generate SLAAC address using the Hardware Address of the interface
#slaac hwaddr
# OR generate Stable Private IPv6 Addresses based from the DUID
slaac private
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/dictionaries-common/ Folder
</summary>

---
Folder exists in default Debian installations.  
Folder does not exist in default Ubuntu installations.

Contains configuration files and symbolic links related to system-wide dictionary settings. 

These settings are used by various programs and utilities that rely on dictionaries, such as spell checkers, word processors, and text editors.

Some files:

- words: Contains a master list of words that are considered valid for spell-checking purposes. 
- ispell-default: Specifies the default dictionary for the Ispell spell-checking utility.
- default.aff: Provides the essential language rules and affix definitions necessary for spell-checking in various applications and utilities.
 
<br>
</details>

<details markdown='1'>
<summary>
/etc/discover-modprobe.conf
</summary>

---
File exists in default Debian installations.  
File does not exist in default Ubuntu installations.

Configuration  file  for  discover-modprobe,  which  is responsible for retrieving and loading kernel modules.

This file allows users to define options that should be passed to modprobe when loading specific modules.

Sample content:

```
# $Progeny$

# Load modules for the following device types. Specify "all"
# to detect all device types.
types="all"

# Don't ever load the foo, bar, or baz modules.
#skip="foo bar baz"

# Lines below this point have been automatically added by
# discover-modprobe(8) to disable the loading of modules that have
# previously crashed the machine:
```

<br>

</details>

<details markdown='1'>
<summary>
/etc/discover.conf.d/ Folder
</summary>

---
Folder exists in default Debian installations.  
Folder does not exist in default Ubuntu installations.

Contains configuration files that control the default behavior for both the discover tool and the Discover library. 

Default Debian installation has the file 00discover with the following content:

```
<?xml version="1.0"?>
<!-- $Progeny$ -->
<!DOCTYPE conffile SYSTEM "conffile.dtd">
<conffile>
  <busscan scan="default">
    <bus name="ata"/>
    <bus name="pci"/>
    <bus name="pcmcia"/>
    <bus name="scsi"/>
    <bus name="usb"/>
  </busscan>
</conffile>
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/dkms/ Folder
</summary>

---
Folder does not exist in default Debian & Ubuntu installations.

Contains configuration files used by the Dynamic Kernel Module Support (DKMS) framework. 

DKMS is a system that helps manage and recompile out-of-tree kernel modules when the Linux kernel is upgraded.

Contains subdirectories named after DKMS-managed kernel modules. 

Inside each module directory, there are configuration files that specify how the module should be built and installed for different kernel versions.

DKMS allows for managing multiple versions of kernel modules simultaneously. 

Configuration files in /etc/dkms help DKMS determine how to handle different module versions and kernel versions.

<br>
</details>

<details markdown='1'>
<summary>
/etc/dovecot/ Folder
</summary>

---
Folder does not exist in default Debian & Ubuntu installations.

Created after installing Dovecot package. 

Contains configuration files and related directories for the Dovecot IMAP and POP3 server

Some files and folders:

- dovecot.conf: Main configuration file for Dovecot. Includes other configuration files located in the conf.d/ and other directories.
- dovecot-*.ext: Additional configuration files for specific Dovecot features.
- conf.d/: Contains additional configuration files that are included in the main dovecot.conf file. Each file in this directory corresponds to a specific aspect of Dovecot's configuration, such as authentication, logging, and protocol settings.
- private/: Contains SSL certificates (or links to them) used by Dovecot.
- sieve/: Contains Sieve scripts for filtering and processing incoming email messages.

<br>
</details>

<details markdown='1'>
<summary>
/etc/dpkg
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files for dpkg low level package management system.

Some files and folder:

- dpkg.cfg: Contains configuration options for dpkg. Allows administrators to specify global options for dpkg operations.
- dpkg.cfg.d/: Contains additional configuration snippets that are included in the main dpkg.cfg file.
- origins/: Contains files describing the origin of packages (e.g., distribution, repository, vendor) and their associated cryptographic signatures. 
- origins/default: This file specifies the default origin for packages installed via dpkg. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/e2scrub.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Configuration file for e2scrub utility.

e2scrub attempts to check (but not repair) all metadata in a mounted ext[234] file system if the file system resides on an LVM logical volume.

Sample file content:

```
# e2scrub configuration file

# Uncomment to enable automatic periodic runs of e2scrub_all
# (either via cron or via a systemd timer)
# periodic_e2scrub=1

# e-mail destination used by e2scrub_fail when problems are found with
# the file system.
# recipient=root

# e-mail sender used by e2scrub_fail when problems are found with
# the file system.
# sender=e2scrub@host.domain.name

# Snapshots will be created to run fsck; the snapshot will be of this size.
# snap_size_mb=256

# Set this to 1 to enable fstrim for everyone.
# fstrim=0

# Arguments passed into e2fsck.
# e2fsck_opts="-vtt"

# Set this to 1 to have e2scrub_all scrub all LVs, not just the mounted ones.
# scrub_all=0
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/emacs/ Folder
</summary>

---
Folder exists in default Debian installations.  
Folder does not exist in default Ubuntu installations.

Contains system-wide configuration files and directories for the Emacs text editor. 

Emacs is a powerful and extensible text editor known for its extensive customization options and support for various programming languages and modes.

Default Debian installation contains one folder named site-start.d, which contains one file named 50dictionaries-common.el

<br>
</details>

<details markdown='1'>
<summary>
/etc/environment
</summary>

---
File exists in default Debian & Ubuntu installations.

Belongs to PAM (Pluggable Authentication Module), and only programs compiled with PAM support are able to use it (primarily login systems, which subsequently start the shell or user environment).

Used for setting variables for programs which are usually not started from a shell.

Default Debian file is empty, default Ubuntu file contains PATH environment variable.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ethertypes
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains ethernet frame types.

EtherType values are used in Ethernet frames to identify the type of protocol encapsulated in the frame.

It is typically used by tools like tcpdump or wireshark to display EtherType values in a human-readable format when analyzing network traffic.

Sample content:

```
# Ethernet frame types

# The EtherType is a two-octet field of Ethernet frames used to indicate
# which protocol is contained in their payload.

# More entries, mostly historical, can be found on:
#	https://www.iana.org/assignments/ieee-802-numbers/
#	http://standards-oui.ieee.org/ethertype/eth.txt

# <name>	<hexnumber> <alias1>...<alias35> # Comment

IPv4		0800	ip ip4	# IP (IPv4)
X25		0805
ARP		0806	ether-arp # Address Resolution Protocol
FR_ARP		0808		# Frame Relay ARP [RFC1701]
BPQ		08FF		# G8BPQ AX.25 over Ethernet
TRILL		22F3		# TRILL [RFC6325]
L2-IS-IS	22F4		# TRILL IS-IS [RFC6325]
TEB		6558		# Transparent Ethernet Bridging [RFC1701]
RAW_FR		6559		# Raw Frame Relay [RFC1701]
RARP		8035		# Reverse ARP [RFC903]
ATALK		809B		# Appletalk
AARP		80F3		# Appletalk Address Resolution Protocol
802_1Q		8100	8021q 1q 802.1q	dot1q # VLAN tagged frame [802.1q]
IPX		8137		# Novell IPX
NetBEUI		8191		# NetBEUI
IPv6		86DD	ip6	# IP version 6
PPP		880B		# Point-to-Point Protocol
MPLS		8847		# MPLS [RFC5332]
MPLS_MULTI	8848		# MPLS with upstream-assigned label [RFC5332]
ATMMPOA		884C		# MultiProtocol over ATM
PPP_DISC	8863		# PPP over Ethernet discovery stage
PPP_SES		8864		# PPP over Ethernet session stage
ATMFATE		8884		# Frame-based ATM Transport over Ethernet
EAPOL		888E		# EAP over LAN [802.1x]
S-TAG		88A8		# QinQ Service VLAN tag identifier [802.1q]
EAP_PREAUTH	88C7		# EAPOL Pre-Authentication [802.11i]
LLDP		88CC		# Link Layer Discovery Protocol [802.1ab]
MACSEC		88E5		# Media Access Control Security [802.1ae]
PBB		88E7	macinmac # Provider Backbone Bridging [802.1ah]
MVRP		88F5		# Multiple VLAN Registration Protocol [802.1q]
PTP		88F7		# Precision Time Protocol
FCOE		8906		# Fibre Channel over Ethernet
FIP		8914		# FCoE Initialization Protocol
ROCE		8915		# RDMA over Converged Ethernet
LoWPAN		A0ED		# LoWPAN encapsulation
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/exports/ Folder
</summary>

---
Folder does not exist in default Debian & Ubuntu installations.

NFS server export table

Contains a table of local physical file systems on an NFS server that are accessible to NFS clients.

Sample content:

```
/               master(rw) trusty(rw,no_root_squash)
/projects       proj*.local.domain(rw)
/usr            *.local.domain(ro) @trusted(rw)
/home/joe       pc001(rw,all_squash,anonuid=150,anongid=100)
/pub            *(ro,insecure,all_squash)
/srv/www        -sync,rw server @trusted @external(ro)
/foo            2001:db8:9:e54::/64(rw) 192.0.2.0/24(rw)
/build          buildhost[0-9].local.domain(rw)
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/fonts/ Folder
</summary>

---
Folder does not exist in default Debian installations. 
Folder exists in default Debian installations.

Contains configuration files for the font system. As much as I know, server editions do not need fonts, but I guess Ubuntu needs it for some dependency issues.

Some files and folders:

- fonts.conf: This file defines basic configurations, such as where to find fonts, default font settings, and other general font-related parameters. You are not expected to modify this file.
- local.conf: Configuration file for local changes at /etc/fonts/local.conf. This allows users to customize font settings without modifying the main configuration file.
- conf.d/: Included by fonts.conf to allow additional configurations.
- conf.avail/: Represents a set of potential configurations that can be enabled or disabled based on system or user preferences. These configurations become active when they are linked from /etc/fonts/conf.d. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/fstab
</summary>

---
File exists in default Debian & Ubuntu installations.

Defines how file systems are mounted and configured during system startup.

Sample content:

```
# /etc/fstab: static file system information.

# Use 'blkid' to print the universally unique identifier for a device; this 
# may be used with UUID= as a more robust way to name devices that works even 
# if disks are added and removed. See fstab(5).

# <file system> <mount point>   <type>  <options>       <dump>  <pass>
/dev/sda1       /               ext4    errors=remount-ro 0       1
/dev/sda2       /home           ext4    defaults        0       2
/dev/sda3       none            swap    sw              0       0
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/fuse.conf
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Contains FUSE configurations.

FUSE  (Filesystem  in  Userspace) is a simple interface for userspace programs to export a virtual filesystem to the Linux kernel. 

FUSE also aims to provide a secure method for non privileged users to create and mount their own filesystem implementations.

Sample content: 
```
# The file /etc/fuse.conf allows for the following parameters:
#
# user_allow_other - Using the allow_other mount option works fine as root, in
# order to have it work as user you need user_allow_other in /etc/fuse.conf as
# well. (This option allows users to use the allow_other option.) You need
# allow_other if you want users other than the owner to access a mounted fuse.
# This option must appear on a line by itself. There is no value, just the
# presence of the option.

#user_allow_other

# mount_max = n - this option sets the maximum number of mounts.
# Currently (2014) it must be typed exactly as shown
# (with a single space before and after the equals sign).

#mount_max = 1000
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/fwupd/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration options for fwupd utility.

fwupd (Firmware Update Daemon) is a firmware update service which aims to provide a standardized way to update firmware on Linux systems.

Some files and folders:

- daemon.conf: This file contains global configuration options for the fwupd service. 
- lvfs.conf: Configuration settings for LVFS (Linux Vendor Firmware Service).
- vendor.conf: Contains configuration settings related to firmware updates for specific hardware vendors.
- remotes.d/: This directory contains configuration files for remote repositories where firmware updates can be obtained. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/gai.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains configuration settings for getaddrinfo system call.

The getaddrinfo function is used in programming to perform hostname resolution. 

It is used to translate a hostname or service name into a set of network addresses. This function is often used when writing network applications to determine the IP addresses associated with a domain name.

Both config files (in Debian & Ubuntu) are fully commented.

<br>
</details>

<details markdown='1'>
<summary>
/etc/gnutls/ Folder
</summary>

---
File does not exist in default Debian installations. 
File exists in default Ubuntu installations.

Contains configuration files for GnuTLS library. GnuTLS is widely used in Linux systems for handling secure network protocols and is part of the broader GNU project.

Default Ubuntu installations has only 1 file named `config` with the following content:

```
[overrides]
disabled-version = tls1.0
disabled-version = tls1.1
disabled-version = dtls0.9
disabled-version = dtls1.0
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/groff/ Folder
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains configuration files and resources used by the GNU troff (groff) typesetting system. 

Groff is a Unix-based typesetting system that formats plain text into printable documents, typically used for producing technical documentation, manuals, and other printed material.

Debian & Ubuntu installations include 2 files: man.local and mdoc.local.

<br>
</details>

<details markdown='1'>
<summary>
/etc/group and /etc/group-
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/group contains information about user groups on the system.

/etc/group- contains the previous state of /etc/group for backup purposes.

/etc/group file is typically used by the system to manage group permissions and access control. 

Sample content:

```
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:exforge
floppy:x:25:exforge
tape:x:26:
staff:x:50:
games:x:60:
users:x:100:exforge
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:101:
input:x:102:
sgx:x:103:
kvm:x:104:
render:x:105:
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/grub.d/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains scripts that are used during the generation of the GRUB configuration file, which determines how the system boots and which options are available in the boot menu.

The scripts in the folder are typically numbered to specify the order in which they are executed during the generation of grub.cfg.

After modifying scripts in /etc/grub.d, the grub-mkconfig command is typically used to regenerate the grub.cfg file based on the updated scripts. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/gshadow and /etc/gshadow-
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/gshadow contains encrypted passwords for user groups on the system.

/etc/gshadow- contains the previous state of /etc/gshadow for backup purposes.

/etc/gshadow file is readable only by the root user to prevent unauthorized access to group password hashes.

<br>
</details>

<details markdown='1'>
<summary>
/etc/gss/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration settings for Generic Security Services (GSS) daemon.

The GSS API provides a mechanism for applications to access security services in a generic and uniform way, regardless of the underlying security mechanisms being used. 

It is commonly used for authentication and security-related operations in distributed systems.

In Default Debian & Ubuntu installations, this folder has an empty folder named mech.d

<br>
</details>

<details markdown='1'>
<summary>
/etc/hdparm.conf
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Contains configurations used by the hdparm utility.

hdparm is a command-line tool used to configure and manage hard disk drives. 

Allows users to set default parameters for hard drives.

<br>
</details>

<details markdown='1'>
<summary>
/etc/host.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Used to configure the lookup order of host name resolution methods. It specifies how the system should resolve hostnames into IP addresses. 

This file is read by the system's DNS resolver library.

Sample content:

```
# Configuration file for host name resolution

# Order of host name resolution methods
order hosts,bind

# Enable IPv6 support
multi on
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/hostname
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains the hostname of the system, which is the unique identifier used to identify the system on a network.

Contains only one line with the hostname of the system. 

The hostname specified in this file is used to set the system's hostname during the boot process or when the network configuration is applied.

<br>
</details>

<details markdown='1'>
<summary>
/etc/hosts
</summary>

---
File exists in default Debian & Ubuntu installations.

Used to map hostnames to IP addresses locally on the system. 

Often used to resolve hostnames without querying DNS servers, making it useful for local network configurations and troubleshooting.

Sample content:

```
# /etc/hosts

# Static table lookup for hostnames.

# IPv4 addresses
127.0.0.1   localhost
192.168.1.100  mycomputer
192.168.1.101  myrouter

# IPv6 addresses
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/hosts.allow and /etc/hosts.deny
</summary>

---
Files exist in default Debian & Ubuntu installations.

Used to configure access control for network services.

hosts.allow specifies which hosts are allowed to access network services on the system.

hosts.deny specifies which hosts are denied access to network services on the system if they are not explicitly allowed in hosts.allow.

The order of evaluation between hosts.allow and hosts.deny:

1. If allowed in hosts.allow, access is granted.
2. If denied in hosts.deny, access is denied.
3. If neither file specifies anything about a service or client, access is allowed by default.

Sample contents

```
# /etc/hosts.allow

# Allow SSH access from the local network
sshd: 192.168.1.0/255.255.255.0

# Allow FTP access from a specific IP address
vsftpd: 203.0.113.10

# Allow all services from localhost
ALL: 127.0.0.1
```

```
# /etc/hosts.deny

# Deny all services from all hosts by default
ALL: ALL
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/init.d/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains system startup scripts for System V init system.

Although both Debian & Ubuntu uses systemd for their init systems, it is possible to convert to System V init.

The scripts in the folder will be used if init system is changed to System V. That is, the folder exists as a compatability layer.

<br>
</details>

<details markdown='1'>
<summary>
/etc/initramfs-tools/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and scripts related to the generation of the initial RAM filesystem (initramfs). 

The initramfs is a temporary filesystem that is loaded into memory during the boot process before the actual root filesystem is mounted. 

It contains essential tools, modules, and scripts required to boot the system and initialize hardware.

Some files and folders:

- initramfs.conf: Contains global configuration options for the initramfs generation process.
- modules: List of modules to be included in initramfs.
- update-initramfs.conf: Contains configuration options for update-initramfs utility.
- conf.d/: Contains additional configuration files that can override settings in initramfs.conf. Files placed here specify environment variables or other options that affect the initramfs generation process.
- hooks/: Contains shell scripts (hooks) that are executed during the initramfs generation process. Hooks are used to perform tasks such as adding custom files, configuring network interfaces, or including additional kernel modules.
- scripts/ : Contains shell scripts to be executed during the initramfs generation process. Unlike hooks, scripts in this directory are not executed automatically during the initramfs generation process. Instead, they are called from other hooks or scripts.

<br>
</details>

<details markdown='1'>
<summary>
/etc/inputrc
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains configuration settings for Readline.

Readline is a library used to provide command-line editing for many programs, including Bash, Python, and MySQL, among others.

Excerpt from /etc/inputrc

```
# allow the use of the Home/End keys
"\e[1~": beginning-of-line
"\e[4~": end-of-line

# allow the use of the Delete/Insert keys
"\e[3~": delete-char
"\e[2~": quoted-insert

# mappings for "page up" and "page down" to step to the beginning/end
# of the history
# "\e[5~": beginning-of-history
# "\e[6~": end-of-history

# alternate mappings for "page up" and "page down" to search the history
# "\e[5~": history-search-backward
# "\e[6~": history-search-forward
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/iproute2/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and settings related to the iproute2 suite.

iproute2 suite is used for managing various aspects of networking, including routing, traffic control, and network interfaces. 

Some files:

- rt_tables: Defines additional routing tables used by the kernel for policy-based routing.
- rt_realms: Similar to rt_tables, this file defines realms used for policy-based routing. Realms provide a way to group routes for policy-based routing purposes.
- rt_dsfield: Contains definitions for the Differentiated Services Field (DSField) values used in Quality of Service (QoS) and packet marking configurations.
- rt_protos: Defines protocol identifiers used in routing tables and routing cache entries.
- rt_scopes: Defines the scope values used in routing table entries. Scopes are used to determine the scope of a route.
- rt_tos: Contains definitions for the Type of Service (ToS) values used in QoS configurations and packet marking.
- rt_mark: Contains definitions for route marks used in policy-based routing.

<br>
</details>

<details markdown='1'>
<summary>
/etc/iscsi/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files and settings related to the iSCSI (Internet Small Computer System Interface) protocol. 

iSCSI is a protocol used to transmit SCSI commands over IP networks,allowing storage devices to be shared and accessed remotely over a network.

Some files:

- initiatorname.iscsi: Contains the iSCSI initiator name for the system. The initiator name uniquely identifies the iSCSI initiator on the network.
- iscsid.conf: Contains configuration settings for the iscsid daemon, which manages iSCSI connections on the system. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/issue and /etc/issue.net
</summary>

---
Files exist in default Debian & Ubuntu installations.  

/etc/issue contains the pre-login message that is displayed on the local system's physical terminals (virtual consoles) before the login prompt.

/etc/issue.net is similar to /etc/issue, but it is used specifically for displaying pre-login messages to remote users connecting via network services like SSH.

If /etc/issue.net is not present, /etc/issue is used for remote users too.

Sample contents:

Debian 12 /etc/issue

```
Debian GNU/Linux 12 \n \l
```

Debian 12 /etc/issue.net

```
Debian GNU/Linux 12 
```

Ubuntu 24.04 /etc/issue

```
Ubuntu 24.04 LTS \n \l
```

Ubuntu 24.04 /etc/issue.net

```
Ubuntu 22.04 LTS 
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/kernel/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files related to the management of kernel images and modules.

Default Debian & Ubuntu installations has 4 folders:

- install.d/: Contains scripts that are executed when a new kernel package is installed on the system.
- preinst.d/: Contains scripts that are executed before a kernel package is installed or upgraded.
- postinst.d/: Contains scripts that are executed after a kernel package is installed or upgraded.
- postrm.d/: Contains scripts that are executed after a kernel package is removed from the system. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/kernel-img.conf
</summary>

---
File exists in default Debian installations.  
File doesn't exist in default Ubuntu installations.

Used by the kernel package installation and removal process to allow local options for handling some aspects of the installation. 

Most configuration variables apply only to kernel image packages.

Sample content:

```
# Kernel image management overrides
# See kernel-img.conf(5) for details
do_symlinks = yes
do_bootloader = no
do_initrd = yes
link_in_boot = no
```

- do_symlinks: Specifies whether symbolic links should be created for kernel image files. 
- do_bootloader: Specifies whether to automatically update the bootloader configuration during kernel installation. 
- do_initrd: Specifies whether to generate an initial RAM disk (initrd) during kernel installation. 
- link_in_boot: Specifies whether to create symbolic links in the /boot directory.

<br>
</details>

<details markdown='1'>
<summary>
/etc/landscape/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.  
Folder is empty in default Ubuntu installations.

Contains configuration files and settings for the Landscape management tool, which is used for managing multiple Ubuntu systems. 

Landscape allows administrators to monitor, manage, and update Ubuntu systems from a centralized interface.

Key features of Ubuntu Landscape include: System Monitoring, Software Management, Inventory Management, Security Compliance, Automation & Orchestration, Multi-Cloud Support, and User Authentication & Access  Control.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ld.so.conf, /etc/ld.so.conf.d Folder and /etc/ld.so.cache
</summary>

---
Files and folder exists in default Debian & Ubuntu installations.

/etc/ld.so.conf is a configuration file used by the dynamic linker/loader (ld). It specifies directories in which the linker should search for shared libraries when an executable is run.

Each line in the file typically represents a directory path where shared libraries (.so files) are located. 

The dynamic linker uses this information to locate and load the required libraries at runtime when an executable is executed.

/etc/ld.so.conf.d Folder is included by /etc/ld.so.conf, it allows additional configurations in different files.

After modifying the /etc/ld.so.conf file, ldconfig command must be run to update the cache used by the dynamic linker:

```
sudo ldconfig
```

This command rebuilds the cache (/etc/ld.so.cache) based on the paths specified in the configuration file.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ldap/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for the OpenLDAP server and client utilities.

OpenLDAP is an open-source implementation of the Lightweight Directory Access Protocol (LDAP), which is used for accessing and managing directory services.

Default Ubuntu configurations consist only ldap.conf file with the following content:

```
# /etc/ldap/ldap.conf

# LDAP Defaults

# See ldap.conf(5) for details
# This file should be world readable but not world writable.

#BASE   dc=example,dc=com
#URI    ldap://ldap.example.com ldap://ldap-provider.example.com:666

#SIZELIMIT      12
#TIMELIMIT      15
#DEREF          never

# TLS certificates (needed for GnuTLS)
TLS_CACERT      /etc/ssl/certs/ca-certificates.crt
```

Some files and folders:
- ldap.conf: This file contains global configuration options for the LDAP client utilities (ldapsearch, ldapmodify, etc.).
- slapd.conf: Main configuration file for the OpenLDAP server (slapd). It defines settings such as database backend configuration, access control rules, schema definitions, and logging options.
- ldap.conf.d/: Additional configuration files included by ldap.conf.
- slapd.d/: Additional configuration files included by slapd.conf.

<br>
</details>

<details markdown='1'>
<summary>
/etc/legal
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Contains legal notices.

Default Ubuntu installations has the following content:

```
The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/libaudit.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains configuration information for user space applications that link to libaudit. 

libaudit is a library in Linux systems used for interacting with the Linux Audit framework. 

The Audit framework provides a comprehensive logging and monitoring mechanism for system events.

Sample content:

```
# This is the configuration file for libaudit tunables.
# It is currently only used for the failure_action tunable.

# failure_action can be: log, ignore, terminate
failure_action = ignore
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/libblockdev/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for the libblockdev library.

Libblockdev is a library that provides a standard and abstracted way to access block devices on Linux systems. 

Allows applications to manage block devices programmatically without needing to know the low-level details of the underlying storage technology.

Sample file:

```
# /etc/libblockdevconf.d/00-default.cfg
# This is the default configuration for the libblockdev library. For
# each supported technology/plugin there is a separate section/group
# with the 'sonames' key. The value of the key has to be a list of
# sonames of shared objects that should be attempted to be loaded for
# the plugin falling back to the next one in the list.

# So this example:
# [lvm]
# sonames=libbd_lvm-dbus.so.0;libbd_lvm.so.0
#
# would result in the libbd_lvm-dbus.so.0 shared object attempted to
# be loaded and if that failed, the libbd_lvm.so.0 would be attempted
# to be loaded.

[btrfs]
sonames=libbd_btrfs.so.2

[crypto]
sonames=libbd_crypto.so.2

[dm]
sonames=libbd_dm.so.2

[fs]
sonames=libbd_fs.so.2

[kbd]
sonames=libbd_kbd.so.2

[loop]
sonames=libbd_loop.so.2

[lvm]
sonames=libbd_lvm.so.2

[mdraid]
sonames=libbd_mdraid.so.2

[mpath]
sonames=libbd_mpath.so.2

[nvdimm]
sonames=libbd_nvdimm.so.2

[swap]
sonames=libbd_swap.so.2

[s390]
sonames=libbd_s390.so.2
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/libibverbs.d/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for the libibverbs library. The libibverbs library is a key component of the software stack used to interact with Remote Direct Memory Access (RDMA) technologies. It provides an interface for applications to use RDMA capabilities, enabling high-performance data transfers with low latency, often used in data centers, high-performance computing, and storage systems.

<br>
</details>

<details markdown='1'>
<summary>
/etc/libnl-3/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for the libnl (Network Link library). 

libnl is a library used for low-level communication with the kernel's networking stack, providing an API for applications to interact with network interfaces, routing tables, and other networking-related features.

Some files:

- classid: Contains ClassID to Name Translation Table conversions.
- pktloc: Contains location definitions for packet matching.

<br>
</details>

<details markdown='1'>
<summary>
/etc/locale.alias and /etc/locale.gen
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/local.alias contains alias definitions for locale names. 

It provides a mapping between different locale names, allowing users and applications to refer to locales using different aliases.

Each line in the file typically contains an alias followed by the corresponding canonical locale name.

/etc/locale.gen is used to generate locale definitions. 

It contains a list of locale definitions to be generated or compiled on the system.

Each line in the file typically represents a locale definition, specifying the locale name and optionally the character encoding.

Excerpt from /etc/locale.alias

```
catalan         ca_ES.ISO-8859-1
croatian        hr_HR.ISO-8859-2
czech           cs_CZ.ISO-8859-2
danish          da_DK.ISO-8859-1
dansk           da_DK.ISO-8859-1
deutsch         de_DE.ISO-8859-1
dutch           nl_NL.ISO-8859-1
eesti           et_EE.ISO-8859-15
estonian        et_EE.ISO-8859-15
finnish         fi_FI.ISO-8859-1
french          fr_FR.ISO-8859-1
galego          gl_ES.ISO-8859-1
galician        gl_ES.ISO-8859-1
german          de_DE.ISO-8859-1
greek           el_GR.ISO-8859-7
hebrew          he_IL.ISO-8859-8
hrvatski        hr_HR.ISO-8859-2
```

- Excerpt from /etc/locale.gen

```
# en_SG.UTF-8 UTF-8
# en_US ISO-8859-1
# en_US.ISO-8859-15 ISO-8859-15
en_US.UTF-8 UTF-8
# en_ZA ISO-8859-1
# en_ZA.UTF-8 UTF-8
# en_ZM UTF-8
# en_ZW ISO-8859-1
# en_ZW.UTF-8 UTF-8
# eo UTF-8
# es_AR ISO-8859-1
# es_AR.UTF-8 UTF-8
# es_BO ISO-8859-1
# es_BO.UTF-8 UTF-8
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/locale.conf
</summary>

---
File does not exist in default Debian installations. 
File exists in default Ubuntu installations.

Defines system-wide locale settings. Locale settings determine the language, regional formats, and other internationalization aspects of the operating system, affecting how dates, times, numbers, currencies, and other regional-specific information are presented.

Sample contents:

```
LANG=en_US.UTF-8
LC_TIME=en_GB.UTF-8
LC_NUMERIC=de_DE.UTF-8
```

- LANG: This sets the default language and encoding for the system. It is the primary locale setting.
- LC_*: These override specific categories of locale, like LC_TIME for time and date formats, LC_NUMERIC for numeric formats, etc. If not specified, these default to the value of LANG.

<br>
</details>

<details markdown='1'>
<summary>
/etc/localtime
</summary>

---
File exists in default Debian & Ubuntu installations.

It is a symbolic link or a copy of the timezone data file used by the system's C library to determine the local timezone. 

It points to a timezone data file located in the /usr/share/zoneinfo directory. 

The timezone data files in this directory represent different regions and time zones around the world.

<br>
</details>

<details markdown='1'>
<summary>
/etc/logcheck
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for the Logcheck utility on Linux systems.

Logcheck is a log monitoring and analysis tool that scans system log files for suspicious or unusual activities and generates reports or alerts based on predefined rules.

Some files and folders:

- logcheck.conf: Global configuration settings for Logcheck, such as the email address to which reports should be sent, the log file directories to monitor, and the verbosity level of the output.
- logcheck.logfiles: Lists the log files that Logcheck should monitor. 
- ignore.d.server/: Contains rules for ignoring certain log messages from specific services or applications. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/login.defs
</summary>

---
File exists in default Debian & Ubuntu installations.

Provides default configuration information for several user account parameters. 

The useradd, usermod, userdel, and groupadd commands, and other user and group utilities take default values from this file. 

Each line consists of a directive name and associated value. 

Allows system administrators to customize the default behavior of the login service according to their security and operational requirements.

Excerpt from contents:

```
# REQUIRED for useradd/userdel/usermod
#   Directory where mailboxes reside, _or_ name of file, relative to the
#   home directory.  If you _do_ define MAIL_DIR and MAIL_FILE,
#   MAIL_DIR takes precedence.

#   Essentially:
#      - MAIL_DIR defines the location of users mail spool files
#        (for mbox use) by appending the username to MAIL_DIR as defined
#        below.
#      - MAIL_FILE defines the location of the users mail spool files as the
#        fully-qualified filename obtained by prepending the user home
#        directory before $MAIL_FILE
#
# NOTE: This is no more used for setting up users MAIL environment variable
#       which is, starting from shadow 4.0.12-1 in Debian, entirely the
#       job of the pam_mail PAM modules
#       See default PAM configuration files provided for
#       login, su, etc.

# This is a temporary situation: setting these variables will soon
# move to /etc/default/useradd and the variables will then be
# no more supported
MAIL_DIR        /var/mail
#MAIL_FILE      .mail
#
# Enable logging of successful logins
#
LOG_OK_LOGINS		no
#
# Enable "syslog" logging of su activity - in addition to sulog file logging.
# SYSLOG_SG_ENAB does the same for newgrp and sg.

SYSLOG_SU_ENAB		yes
SYSLOG_SG_ENAB		yes
#
# If defined, all su activity is logged to this file.
#
#SULOG_FILE	/var/log/sulog
#
# If defined, file which maps tty line to TERM environment parameter.
# Each line of the file is in a format something like "vt100  tty01".
#
#TTYTYPE_FILE	/etc/ttytype
#
# If defined, login failures will be logged here in a utmp format
# last, when invoked as lastb, will read /var/log/btmp, so...
#
FTMP_FILE	/var/log/btmp
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/logrotate.conf and /etc/logrotate.d/ Folder
</summary>

---
File & Folder exist in default Debian & Ubuntu installations.

/etc/logrotate.conf is the Main configuration file for the Logrotate utility. 

Logrotate is a system utility that manages the rotation and compression of log files to prevent them from consuming too much disk space.

/etc/logrotate.conf file provides a centralized location for configuring global settings for log rotation. 

Individual log files or sets of log files can be further configured for rotation in separate configuration files located in the /etc/logrotate.d directory. 

Changes made to /etc/logrotate.conf typically take effect immediately, and log rotation occurs according to the specified frequency and criteria.

Sample content:

```
# /etc/logrotate.conf
# Global options
# Rotate log files weekly
weekly

# Rotate log files only if they are larger than 1 MB
size 1M

# Rotate log files keeping up to 4 old versions
rotate 4

# Compress rotated log files using gzip
compress

# Specify where to store rotated log files
# Uncomment and specify a directory if needed
# rotate /var/log/oldlogs

# Include additional configuration files from the /etc/logrotate.d directory
include /etc/logrotate.d
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/lsb-release
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

A standard configuration file found on Linux systems that adhere to the Linux Standard Base (LSB). 

Contains information about the distribution's release, version, and certain other details in a standardized format, allowing applications and scripts to identify the Linux distribution and its characteristics.

Sample content from Ubuntu:

```
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04 LTS"
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/lvm/ Folder
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Contains configuration files and metadata related to Logical Volume Manager (LVM). 

LVM is a disk management tool that allows administrators to create logical volumes from physical volumes, providing flexibility and scalability in managing storage.

Some files and folders:

- lvm.conf: Main configuration file for LVM. Contains settings and options that control the behavior of the LVM tools and daemons.
- lvmlocal.conf: Used for local customization of LVM 
- profiles/: Contains configuration files for LVM profiles.

<br>
</details>

<details markdown='1'>
<summary>
/etc/machine-id
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains the unique machine ID of the local system that is set during installation or boot. 

The machine ID is a single newline-terminated, hexadecimal, 32-character, lowercase ID. 

When decoded from hexadecimal, this corresponds to a 16-byte/128-bit value. This ID may not be all zeros. 

Sample content:

```
4d7f0b0c161e4e729b6c2f1d8e9b37a2
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/magic and /etc/magic.mime
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/magic file contains a database of "magic" numbers or patterns that are used to identify the type of files by examining their contents.

Each entry in the file describes a particular file type or format and includes a set of rules or patterns that are matched against the beginning of the file's contents.

The /etc/magic.mime file is similar to /etc/magic but is specifically used for MIME type detection.

It contains MIME type definitions and file format signatures that are used by MIME type detection utilities to determine the appropriate MIME type for a file based on its contents.

System administrators or package managers may update or customize /etc/magic and /etc/magic.mime to add support for new file types and MIME types.

Sample contents

```
# /etc/magic
# Offset    Data type      Byte sequence    File type
# Example rule: Identify JPEG files
0      string     \xFF\xD8\xFF\xE0\x00\x10    JPEG image data
#
# Example rule: Identify PNG files
0      string     \x89\x50\x4E\x47\x0D\x0A\x1A\x0A    PNG image data
```

```
# /etc/magic.mime
# MIME type definitions for file type detection
# This file is used by MIME type detection utilities to determine
# the appropriate MIME type for a file based on its contents.
# Offset    Data type      Byte sequence    File type
# Images
0       string          \x89\x50\x4e\x47\x0d\x0a\x1a\x0a    image/png
0       string          \xff\xd8\xff\xe0\x00\x10\x4a\x46    image/jpeg
0       string          \x47\x49\x46\x38\x37\x61             image/gif
0       string          \x47\x49\x46\x38\x39\x61             image/gif
#
# Audio
0       string          RIFF\x00\x00\x00\x00WAVE             audio/x-wav
0       string          OggS                                    audio/ogg
#
# Video
0       string          OggS                                    video/ogg
#
# Text
0       string          #!/bin/sh                               text/x-shellscript
0       string          <?xml                                   application/xml
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/mailcap and /etc/mailcap.order
</summary>

---
Files exist in default Debian installations.  
Files don't exist in default Ubuntu installations.

/etc/mailcap file is used by email clients and other applications to map MIME types to commands that can be used to display or handle files of those types. 

It allows users to specify which applications should be used to view or handle different types of files.

/etc/mailcap.order file is used to specify the order in which entries from the /etc/mailcap file are processed by applications. 

This file allows administrators to control the precedence of MIME type handlers defined in /etc/mailcap when multiple entries match a given MIME type.

Sample /etc/mailcap content:

```
text/plain; more %s; needsterminal
text/english; vim %s; needsterminal
text/plain; vim %s; needsterminal
text/x-makefile; vim %s; needsterminal
text/x-c++hdr; vim %s; needsterminal
text/x-c++src; vim %s; needsterminal
text/x-chdr; vim %s; needsterminal
text/x-csrc; vim %s; needsterminal
text/x-java; vim %s; needsterminal
text/x-moc; vim %s; needsterminal
text/x-pascal; vim %s; needsterminal
text/x-tcl; vim %s; needsterminal
```

Sample /etc/mailcap.order content:

```
text/html
text/plain
image/jpeg
audio/mpeg
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/manpath.config
</summary>

---
File exists in default Debian & Ubuntu installations.

Used to configure the system-wide manual page paths for the man command.

It defines the search paths that the man command will use to locate and display manual pages when invoked by users.

Sample content:

```
# There are three mappings allowed in this file:
# --------------------------------------------------------
# MANDATORY_MANPATH                     manpath_element
# MANPATH_MAP           path_element    manpath_element
# MANDB_MAP             global_manpath  [relative_catpath]
# ---------------------------------------------------------
# every automatically generated MANPATH includes these fields
#
#MANDATORY_MANPATH                      /usr/src/pvm3/man

MANDATORY_MANPATH                       /usr/man
MANDATORY_MANPATH                       /usr/share/man
MANDATORY_MANPATH                       /usr/local/share/man
# ---------------------------------------------------------
# set up PATH to MANPATH mapping
# ie. what man tree holds man pages for what binary directory.
#
#               *PATH*        ->        *MANPATH*
#
MANPATH_MAP     /bin                    /usr/share/man
MANPATH_MAP     /usr/bin                /usr/share/man
MANPATH_MAP     /sbin                   /usr/share/man
MANPATH_MAP     /usr/sbin               /usr/share/man
MANPATH_MAP     /usr/local/bin          /usr/local/man
MANPATH_MAP     /usr/local/bin          /usr/local/share/man
MANPATH_MAP     /usr/local/sbin         /usr/local/man
MANPATH_MAP     /usr/local/sbin         /usr/local/share/man
MANPATH_MAP     /usr/X11R6/bin          /usr/X11R6/man
MANPATH_MAP     /usr/bin/X11            /usr/X11R6/man
MANPATH_MAP     /usr/games              /usr/share/man
MANPATH_MAP     /opt/bin                /opt/man
# Any manpaths that are subdirectories of other manpaths must be mentioned
# *before* the containing manpath. E.g. /usr/man/preformat must be listed
# before /usr/man.

#               *MANPATH*     ->        *CATPATH*
#
MANDB_MAP       /usr/man                /var/cache/man/fsstnd
MANDB_MAP       /usr/share/man          /var/cache/man
MANDB_MAP       /usr/local/man          /var/cache/man/oldlocal
MANDB_MAP       /usr/local/share/man    /var/cache/man/local
MANDB_MAP       /usr/X11R6/man          /var/cache/man/X11R6
MANDB_MAP       /opt/man                /var/cache/man/opt
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/mdadm/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Used by the mdadm (multiple devices admin) utility for managing software RAID arrays. 

Contains configuration files, metadata, and state information related to software RAID devices.

Some files and folders:

- array.state: Contains the current state of RAID arrays managed by mdadm. 
- conf.cache: Contains a cache of RAID device metadata. It is used to improve the performance of mdadm by reducing the need to scan RAID devices for  metadata during initialization.
- mdadm.conf: Main configuration file for mdadm. It contains configuration settings and metadata for RAID arrays, including device paths, RAID levels, and other array properties.
- mdadm.pid: Contains the process ID (PID) of the currently running mdadm process. It is used to ensure that only one instance of mdadm is running at a time to prevent conflicts and data corruption.
- mdadm.conf.d/: Contains additional configuration files that can be included by mdadm.conf. Administrators can place custom configuration snippets in this directory to organize and manage RAID configurations more effectively.

<br>
</details>

<details markdown='1'>
<summary>
/etc/mime.types
</summary>

---
File exists in default Debian & Ubuntu installations.

Used to map filename extensions to MIME (Multipurpose Internet Mail Extensions) types.
Provides a mapping between file types and their corresponding MIME types, allowing applications to determine the appropriate MIME type for a given file based on its filename extension.

Sample content:

```
application/octet-stream       bin dms lha lrf lzh exe class so dll img iso dmg
application/pdf                pdf
application/zip                zip
application/x-gzip             gz tgz
audio/mpeg                     mp3
image/jpeg                     jpeg jpg jpe
image/png                      png
text/plain                     txt
text/html                      html htm
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/mke2fs.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Configuration file for mke2fs utility.

It controls the default parameters used by mke2fs when it is creating ext2, ext3, or ext4 file systems.

Sample content:

```
[defaults]
	base_features = sparse_super,large_file,filetype,resize_inode,dir_index,ext_attr
	default_mntopts = acl,user_xattr
	enable_periodic_fsck = 0
	blocksize = 4096
	inode_size = 256
	inode_ratio = 16384
[fs_types]
	ext3 = {
		features = has_journal
	}
	ext4 = {
		features = has_journal,extent,huge_file,flex_bg,metadata_csum,64bit,dir_nlink,extra_isize
	}
	small = {
		blocksize = 1024
		inode_ratio = 4096
	}
	floppy = {
		blocksize = 1024
		inode_ratio = 8192
	}
	big = {
		inode_ratio = 32768
	}
	huge = {
		inode_ratio = 65536
	}
	news = {
		inode_ratio = 4096
	}
	largefile = {
		inode_ratio = 1048576
		blocksize = -1
	}
	largefile4 = {
		inode_ratio = 4194304
		blocksize = -1
	}
	hurd = {
	     blocksize = 4096
	     inode_size = 128
	     warn_y2038_dates = 0
	}
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/ModemManager/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for ModemManager service.

ModemManager service manages mobile broadband (3G/4G/LTE) and other modem devices. 

Default Ubuntu installations contain 2 empty folder; named as; connection.d/ and fcc-unlock.d/

<br>
</details>

<details markdown='1'>
<summary>
/etc/modprobe.d/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Used to configure the behavior of the modprobe command and the Linux kernel module loading process. 

It allows system administrators to specify options, aliases, and other settings for individual kernel modules or for the modprobe command itself.

Sample contents:

```
# /etc/modprobe.d/intel-microcode-blacklist.conf
#
# The microcode module attempts to apply a microcode update when
# it autoloads.  This is not always safe, so we block it by default.
blacklist microcode
```

```
# /etc/modprobe.d/blacklist.conf
#
# This file lists those modules which we don't want to be loaded by
# alias expansion, usually so some other driver will be loaded for the
# device instead.
#
# evbug is a debug tool that should be loaded explicitly
blacklist evbug

# these drivers are very simple, the HID drivers are usually preferred
blacklist usbmouse
blacklist usbkbd

# replaced by e100
blacklist eepro100

# replaced by tulip
blacklist de4x5

# causes no end of confusion by creating unexpected network interfaces
blacklist eth1394
```

```
# /etc/modprobe.d/mdadm.conf

# mdadm module configuration file
# set start_ro=1 to make newly assembled arrays read-only initially,
# to prevent metadata writes.  This is needed in order to allow
# resume-from-disk to work - new boot should not perform writes
# because it will be done behind the back of the system being
# resumed.  See http://bugs.debian.org/415441 for details.

options md_mod start_ro=1
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/modules and /etc/modules-load.d/ Folder
</summary>

---
File and folder exist in default Debian & Ubuntu installations.

Specifies a list of kernel modules to be automatically loaded at boot time on.

Each line in the file corresponds to a single kernel module that the system should load during the boot process.

Sample content:

```
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
loop
lp
snd-usb-audio
```

/etc/modules-load.d folder is used by systemd and contains a symbolic link to /etc/modules. It is used as a compatability layer.

<br>
</details>

<details markdown='1'>
<summary>
/etc/motd
</summary>

---
File exists in default Debian installations.  
File doesn't exist in default Ubuntu installations.

Contains a message or information that is displayed to users when they log in to the system. 

It's often used to convey important announcements, system status updates, or other messages to users.

<br>
</details>

<details markdown='1'>
<summary>
/etc/mtab
</summary>

---
File exists in default Debian & Ubuntu installations.

It is a symbolic link to /proc/self/mounts.

Provides information about currently mounted filesystems. 

It is a dynamic file that is updated in real-time to reflect the current state of mounted filesystems.

<br>
</details>

<details markdown='1'>
<summary>
/etc/multipath.conf and /etc/multipath/ Folder
</summary>

---
File and folder don't exist in default Debian installations.  
File and folder exist in default Ubuntu installations.

Configuration file and additional configurations folder for multipath daemon (multipathd) and the multipath command-line utility.

Multipathing is a technique used to provide redundancy and load balancing for storage devices connected to a system via multiple paths, such as Fibre Channel (FC), iSCSI, or SCSI.

Sample content:

```
# /etc/multipath.conf
#
# Multipath configuration file
#
# See the multipath.conf(5) man page for details

defaults {
        user_friendly_names yes
}
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/mysql/
</summary>

---
Folder doesn't exist in default Debian & Ubuntu installations.

Created after installing mysql-server or mariadb-server package. Contains MySql and/or Mariadb configuration settings.

Some files and folders:

- debian.cnf: Contains authentication credentials used by the MySQL utilities (such as mysql, mysqldump, etc.) provided by the Debian packaging system. This configuration file is obsolete and will be removed in future releases.
- debian-start: A script that is run by the Debian packaging system when the MySQL or Mariadb server is started or restarted.
- mariadb.cnf: Provided by the MariaDB fork of MySQL. It contains additional configuration settings specific to MariaDB.
- my.cnf: Main configuration file for MySQL. Contains global configuration settings for the MySQL server. 
- my.cnf.fallback: A fallback configuration file that is used if the main my.cnf file is missing or unreadable.
- conf.d/: Included by my.cnf (also by mariadb.cnf), contains additional configuration files for MySQL. 
- mariadb.conf.d/: Included by mariadb.cnf (also by my.cnf), contains additional configuration files for MariaDB. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/nanorc
</summary>

---
File exists in default Debian & Ubuntu installations.

Configuration (initialization) file for nano text editor utility.

Excerpt from contents:
```
## Sample initialization file for GNU nano.
##
## For the options that take parameters, the default value is shown.
## Other options are unset by default.  To make sure that an option
## is disabled, you can use "unset <option>".
##
## Characters that are special in a shell should not be escaped here.
## Inside string parameters, quotes should not be escaped -- the last
## double quote on the line will be seen as the closing quote.
#
## Make 'nextword' (Ctrl+Right) and 'chopwordright' (Ctrl+Delete)
## stop at word ends instead of at beginnings.
# set afterends
#
## When soft line wrapping is enabled, make it wrap lines at blanks
## (tabs and spaces) instead of always at the edge of the screen.
# set atblanks
#
## Automatically indent a newly created line to the same number of
## tabs and/or spaces as the preceding line -- or as the next line
## if the preceding line is the beginning of a paragraph.
# set autoindent
#
## Back up files to the current filename plus a tilde.
# set backup
#
## The directory to put unique backup files in.
# set backupdir ""
#
## Use bold text instead of reverse video text.
# set boldtext
#
## Treat any line with leading whitespace as the beginning of a paragraph.
# set bookstyle
#
## The characters treated as closing brackets when justifying paragraphs.
## This may not include any blank characters.  Only closing punctuation,
## optionally followed by these closing brackets, can end sentences.
# set brackets ""')>]}"
#
## Automatically hard-wrap the current line when it becomes overlong.
# set breaklonglines
#
## Do case-sensitive searches by default.
# set casesensitive
#
## Constantly display the cursor position in the status bar or minibar.
# set constantshow
#
## Use cut-from-cursor-to-end-of-line by default.
# set cutfromcursor
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/needrestart/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files used by the Needrestart tool. 

Needrestart is a utility that identifies running processes that need to be restarted after library or kernel updates to ensure that the changes take effect.

Some files and folders:

- needrestart.conf: Main configuration file. Uses Perl syntax.
- notify.conf: Configures how Needrestart notifies users about processes that need to be restarted. It allows customization of notifications, such as the format or destination (e.g., email, syslog).
- iucode.sh: Related to checking whether the microcode of the CPU needs to be updated. Microcode updates for CPUs are provided by the CPU manufacturer (e.g., Intel or AMD) and may address security vulnerabilities or improve  performance.
- conf.d/: This directory contains additional configuration files for Needrestart. Each file represents a specific aspect of Needrestart's behavior, such as which types of processes to consider or # exclude.
- hook.d/: Contain scripts (or hooks) that can be executed by Needrestart at different stages of its operation.
- notify.d/: Contains scripts or configuration files to notify users or administrators about services that need to be restarted.
- restart.d/: Contains configuration files that define conditions under which certain services or processes need to be restarted. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/netconfig
</summary>

---
File exists in default Debian & Ubuntu installations.

Defines a list of transport names describing their semantics and protocol.

Currently only used in conjunction with the TI-RPC code in the libtirpc library.

Sample content:

```
#
# The network configuration file. This file is currently only used in
# conjunction with the TI-RPC code in the libtirpc library.
#
# Entries consist of:
#
#       <network_id> <semantics> <flags> <protofamily> <protoname> \
#               <device> <nametoaddr_libs>
#
# The <device> and <nametoaddr_libs> fields are always empty in this
# implementation.

udp        tpi_clts      v     inet     udp     -       -
tcp        tpi_cots_ord  v     inet     tcp     -       -
udp6       tpi_clts      v     inet6    udp     -       -
tcp6       tpi_cots_ord  v     inet6    tcp     -       -
rawip      tpi_raw       -     inet      -      -       -
local      tpi_cots_ord  -     loopback  -      -       -
unix       tpi_cots_ord  -     loopback  -      -       -
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/netplan/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains Netplan network configuration files.

Netplan is a utility for configuring network interfaces. It is developed by Canonical and used in Ubuntu. 

Sample content:

```
# /etc/netplan/00-installer-config.yaml
network:
  ethernets:
    enp0s3:
      addresses:
      - 192.168.1.216/24
      nameservers:
        addresses:
        - 192.168.1.1
        - 8.8.8.8
        search:
        - x386.org
      routes:
      - to: default
        via: 192.168.1.1
  version: 2
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/network/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains network configuration files for Debian Linux. 

Some files and folders:

- interfaces: Configuration file to define network interfaces, IP addresses, gateways, and other network-related settings.
- interfaces.d/: Contains additional configuration files that could be included from the main interfaces file. It allows for modular organization of network configuration settings.
- if-*.d/: These directories contain scripts that are executed when network interfaces go down (if-down.d), after they go down (if-post-down.d), before they come up (if-pre-up.d), and after they come up (if-up.d).

Sample contents:

```
# /etc/network/interfaces.d/enp0s3
auto enp0s3
iface enp0s3 inet static
  address 192.168.1.196/24
  broadcast 192.168.1.255
  network 192.168.1.0
  gateway 192.168.1.1
```

```
sudo nano /etc/network/if-up.d/routes
```

```
#!/bin/sh
if [ "$IFACE" = "enp0s3" ]; then
  ip route del 10.0.0.0/8 via 192.168.1.196 dev enp0s3 
  ip route add 10.0.0.0/8 via 192.168.1.196 dev enp0s3 
fi
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/networkd-dispatcher/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for networkd-dispatcher daemon. 

networkd-dispatcher is a service that works in conjunction with systemd-networkd to handle events related to network interfaces.

Contains 6 empty folders in default Ubuntu installations:

- carrier.d/: Scripts placed here are executed when the carrier state of a network interface changes from down to up or from up to down. 
- degraded.d/: Scripts placed here are executed when the network is considered to be in a degraded state.
- dormant.d/: Scripts placed here are executed when a network interface enters the dormant state. The dormant state indicates that the network interface has been deactivated or is no longer actively transmitting or receiving data.
- no-carrier.d/: Scripts placed here are executed when network interfaces lose carrier, meaning they go offline or lose connectivity. 
- off.d/: Scripts placed here are executed when a network interface is brought down or deactivated. 
- routable.d/: Scripts placed here are executed when a network interface becomes routable, that is it has an IP address assigned and can communicate with other devices on the network.

<br>
</details>

<details markdown='1'>
<summary>
/etc/networks
</summary>

---
File exists in default Debian & Ubuntu installations.

A simple text-based configuration file to map network names to their corresponding IP network addresses. 

Primarily used by various network-related utilities and commands to resolve network names to IP addresses. For instance, the route command may use this file to look up network addresses by their names when displaying routing information.

Sample content:

```
default         0.0.0.0
loopback        127.0.0.0
link-local      169.254.0.0
localnet        192.168.1.0
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/newt/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for Newt library. 

Newt is a programming library for creating text-based user interfaces (TUI) in applications. It is commonly used in installation programs, system configuration utilities, and other text-mode applications where a graphical user interface (GUI) is not available or practical.

Sample content:

```
# /etc/newt/palette.ubuntu
root=,magenta
checkbox=,magenta
entry=,magenta
label=magenta,
actlistbox=,magenta
helpline=,magenta
roottext=,magenta
emptyscale=magenta
disabledentry=magenta,
```

<br> 
</details>

<details markdown='1'>
<summary>
/etc/nftables.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Configuration file for nftables firewall.

nftables is a framework for packet filtering and classification that is available in the Linux kernel. 

It provides a more modern and flexible replacement for the older iptables firewall.

Sample content (default content for Debian):

```
#!/usr/sbin/nft -f
flush ruleset
table inet filter {
        chain input {
                type filter hook input priority filter;
        }
        chain forward {
                type filter hook forward priority filter;
        }
        chain output {
                type filter hook output priority filter;
        }
}
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/nginx/ Folder
</summary>

---
Folder doesn't exist in default Debian & Ubuntu installations.

Created after installing nginx package. 

Contains configuration files and related directories for the Nginx web server. 

Nginx is a popular open-source web server known for its high performance, stability, and scalability.

Some files and folders:

- nginx.conf: The main configuration file for Nginx. Contains global configuration settings for the Nginx server.
- fastcgi_params & scgi_params: Contain default configuration settings for FastCGI and SCGI, respectively.
- koi-utf & koi-win: Provide character conversion mappings for the KOI8-U and KOI8-R character sets, respectively.
- mime.types: Contains mappings of file extensions to MIME types. It is used by Nginx to determine the appropriate Content-Type HTTP header to send for each requested file.
- conf.d/: Contains additional configuration files for Nginx. Included by nginx.conf to allow administrators to modularize their Nginx configuration.
- modules-available/ & modules-enabled/: Contain configuration files for Nginx modules. Modules in modules-available/ can be enabled by creating symbolic links to them in modules-enabled/.
- sites-available/ & sites-enabled/: Contain configuration files for Nginx server blocks (virtual hosts). Server blocks defined in sites-available/ can be enabled by creating symbolic links to them in sites-enabled/.
- snippets/: Contains reusable configuration snippets for the Nginx web server. Snippets are small pieces of configuration that can be included in other Nginx configuration files to avoid duplication and simplify  management.

<br>
</details>

<details markdown='1'>
<summary>
/etc/nsswitch.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Configuration file used by the Name Service Switch (NSS) system.

Defines the sources and order of sources for various system databases and services, such as user authentication, group membership, hostname resolution, and more.

Sample content:

```
# /etc/nsswitch.conf
#
# Example configuration of GNU Name Service Switch functionality.
# If you have the `glibc-doc-reference' and `info' packages installed, try:
# `info libc "Name Service Switch"' for information about this file.

passwd:         files systemd
group:          files systemd
shadow:         files

hosts:          files dns
networks:       files

protocols:      db files
services:       db files
ethers:         db files
rpc:            db files

netgroup:       nis
```

- passwd, group, and shadow: Define user account information, group membership, and password hashes, respectively. files source indicates that the information is stored in local files like /etc/passwd, /etc/group,  and /etc/shadow, while systemd indicates that systemd should be consulted for these databases.
- hosts: Defines hostname resolution. The files source indicates that the local /etc/hosts file is consulted first, followed by DNS resolution dns.
- networks, protocols, services, ethers, rpc: Define various network-related information. In this example, the db source indicates that the information is stored in system databases (/etc/networks, /etc/protocols, /etc/services, /etc/ethers, /etc/rpc), followed by local files.
- netgroup: Defines network group information and is configured to use the Network Information Service (NIS) as the source.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ntp.conf
</summary>

---
File doesn't exist in default Debian & Ubuntu installations.

Configuration file for the Network Time Protocol (NTP) daemon.

NTP is a protocol used to synchronize the clocks of computers over a network.

Sample content:

```
# /etc/ntp.conf
# Configuration file for ntpd

# Use default NTP servers provided by ntpd pool
server 0.pool.ntp.org
server 1.pool.ntp.org
server 2.pool.ntp.org
server 3.pool.ntp.org

# Specify the drift file location
driftfile /var/lib/ntp/ntp.drift

# Log settings
logfile /var/log/ntp.log

# Restrict NTP queries
restrict default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/opt/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Folder is empty in default Debian & Ubuntu installations.

Contain global configuration for applications installed inside /opt/.

Softwares installed in the /opt/ directory typically have their own directory structure, and configuration files may be stored within that structure.

But, sometimes it's desirable to separate configuration files that affect multiple software packages or system-wide configurations from software-specific files. In such cases, the /etc/opt/ directory provides a standardized location for these system-wide configuration files related to  software installed in /opt/.

<br>
</details>

<details markdown='1'>
<summary>
/etc/os-release
</summary>

---
File exists in default Debian & Ubuntu installations.

It is a symbolic link to usr/lib/os-release.

Contains operating system identification data.

Sample content for Debian 12

```
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

Sample content for Ubuntu 24.04

```
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo

```

<br>
</details>

<details markdown='1'>
<summary>
/etc/overlayroot.conf
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Default configuration of Ubuntu is in a disabled state.

Used with systems that utilize overlay file systems, often used in LiveCDs, embedded systems, or diskless workstations to keep the root filesystem read-only by overlaying a temporary writable filesystem on top of it.

<br>
</details>

<details markdown='1'>
<summary>
/etc/pam.conf and /etc/pam.d/ Folder
</summary>

---
File & folder exist in default Debian & Ubuntu installations.

pam.conf is only used if /etc/pam.d folder does not exists. We may consider it for backward compatability.

/etc/pam.d/ contains configuration files for the Pluggable Authentication Modules (PAM) framework. 

PAM provides a flexible mechanism for authenticating users and authorizing their access to system resources.

Some files:

- common-*: These files contain common PAM configurations that are shared among multiple services. They are typically included by other service specific configuration files.
- login: Configuration file for the login service, which handles user authentication during login sessions.
- su: Configuration file for the su command, which allows users to switch to another user account.
- sudo: Configuration file for the sudo command, which allows users to execute commands as another user (usually root).
- other: This file is used for services that do not have a specific configuration file.

<br>
</details>

<details markdown='1'>
<summary>
/etc/passwd & /etc/passwd-
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/passwd stores user account information. It is one of the most essential system files and contains details about each user account registered on the system.

/etc/passwd- contains the previous state of /etc/passwd for backup purposes.

Sample content:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/perl/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and directories related to the Perl programming language. 

Used to configure Perl itself and manage Perl modules installed system wide.

Some files & folders:

- Errno.pm: Contains error code definitions used by Perl.
- CPAN/: Contains configuration files related to the CPAN (Comprehensive Perl Archive Network) module installer. The Config.pm file within this directory is used to configure CPAN settings.
- Net/: Contains configuration files related to the Net module. The Config.pm file within this directory is used to configure settings for the Net module.

<br>
</details>

<details markdown='1'>
<summary>
/etc/php/ Folder
</summary>

---
Folder doesn't exist in default Ubuntu & Debian installations. 

Created after installing PHP package. 

Contains configuration files and directories related to the PHP programming language. 

PHP is a widely used server-side scripting language that is particularly popular for web development.

Folder has subfolders with the version number of installed PHP versions, like 7.4, 8.2, etc.

Under these folder, normally there are 3 folders:
- apache2/: Contains configuration files for PHP running as an Apache module.
- cli: Contains configuration files for PHP command-line interface.
- mods-available: Contains configuration files for specific PHP modules or extensions.

<br>
</details>

<details markdown='1'>
<summary>
/etc/pki/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains certificates (fwupd/ folder) and metadata (fwupd-metadata folder) used by the fwupd (Firmware Update Daemon) utility

fwupd is a utility for managing firmware updates on Linux systems.

<br>
</details>

<details markdown='1'>
<summary>
/etc/plymouth/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations. 
Folder is empty in default Ubuntu installations. 

Its purpose is to contain configuration files, themes, and scripts for Plymouth project, which is a boot splash screen system for Linux distributions. 

Plymouth is often used in distributions like Ubuntu, Fedora, and others to give a more polished and visually consistent user experience when starting or shutting down the system.

<br>
</details>

<details markdown='1'>
<summary>
/etc/pm/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files and scripts related to power management settings. 

May contain the following folders:

- config.d/: Contains configuration files that define global settings for power management. These settings apply system-wide and can affect the behavior of power management features such as suspend, hibernate, and screen dimming.
- power.d/: Contains power management scripts that are executed when the system transitions between different power states, such as when it enters or exits suspend mode.
- sleep.d/: Similar to the power.d/, contains scripts that are executed when the system enters or exits suspend mode. However, scripts in this directory are specifically executed during the system's sleep transitions (suspend, hibernate, or resume). 

<br>
</details>

<details markdown='1'>
<summary>
/etc/polkit-1/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for PolicyKit. 

PolicyKit is a component used for defining and enforcing fine-grained access control policies. 
These policies determine what actions users can perform on the system, such as mounting drives, changing system settings, or performing administrative tasks.

<br>
</details>

<details markdown='1'>
<summary>
/etc/pollinate/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files and scripts for the pollinate utility.

pollinate is a tool used to gather entropy (randomness) from external sources and feed it into the Linux kernel's random number generator. 

This helps to improve the quality of randomness available to cryptographic operations and other security-sensitive processes on the system.

<br>
</details>

<details markdown='1'>
<summary>
/etc/popularity-contest.conf
</summary>

---
File exists in default Debian installations.  
File doesn't exist in default Ubuntu installations.

Configuration file for the Popularity Contest package for Debian. 

Popularity Contest is a tool that collects anonymous information about the most used Debian packages on a system. 

This data helps Debian developers make informed decisions about which packages to prioritize and maintain.

Sample content:

```
# Config file for Debian's popularity-contest package.
#
# To change this file, use:
#        dpkg-reconfigure popularity-contest
#
# You can also edit it by hand, if you so choose.
#
# See /usr/share/popularity-contest/default.conf for more info
# on the options.

MY_HOSTID="31fe0edc362341265545f660dfdd1d77"
PARTICIPATE="yes"
USEHTTP="yes"
DAY="6"
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/postfix/ Folder
</summary>

---
Folder doesn't exist in default Ubuntu & Debian installations. 

Created after installing postfix package. 

Contains configuration files and settings for the Postfix mail transfer agent (MTA). 

Postfix is a popular open-source MTA known for its security, performance, and ease of configuration.

Some files and folders:

- main.cf: Main configuration file for Postfix. Contains settings that define how Postfix operates, including parameters such as the mail server hostname, domain name, network interfaces to listen on, relay host configuration, SMTP client options, and more.
- master.cf: Master configuration file for Postfix. It defines the various mail transport services and their configuration parameters. Each service corresponds to a particular aspect of mail handling, such as receiving  incoming messages, delivering messages to local mailboxes, relaying messages to other mail servers, and so on.
- sasl/: Contains configuration files for integrating Postfix with the Cyrus SASL (Simple Authentication and Security Layer) library. SASL provides mechanisms for authenticating clients and servers during SMTP sessions, such # as PLAIN, LOGIN, and CRAM-MD5. 
- postfix-files.d/: This directory contains miscellaneous configuration files and support scripts used by Postfix.

<br>
</details>

<details markdown='1'>
<summary>
/etc/profile & /etc/profile.d/ Folder
</summary>

---
File & folder exist in default Debian & Ubuntu installations.

/etc/profile is a system wide configuration file that sets environment variables and initializes settings for Bourne shell and compatible shells (sh, bash, ksh, ash).

/etc/profile.d/ contains shell scripts that are automatically sourced by the system-wide shell profile script /etc/profile. 

Sample content:

```
# /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
# and Bourne compatible shells (bash(1), ksh(1), ash(1), ...).
if [ "$(id -u)" -eq 0 ]; then
  PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
else
  PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"
fi
export PATH

if [ "${PS1-}" ]; then
  if [ "${BASH-}" ] && [ "$BASH" != "/bin/sh" ]; then
    # The file bash.bashrc already sets the default PS1.
    # PS1='\h:\w\$ '
    if [ -f /etc/bash.bashrc ]; then
      . /etc/bash.bashrc
    fi
  else
    if [ "$(id -u)" -eq 0 ]; then
      PS1='# '
    else
      PS1='$ '
    fi
  fi
fi

if [ -d /etc/profile.d ]; then
  for i in /etc/profile.d/*.sh; do
    if [ -r $i ]; then
      . $i
    fi
  done
  unset i
fi
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/protocols
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains a list of network protocols and their associated protocol numbers. 

Each entry in this file defines a protocol name, its corresponding protocol number, and optionally, aliases for the protocol.

Used by various networking utilities and applications to map between protocol names and their corresponding protocol numbers. 

Sample content:

```
# Internet (IP) protocols

# Updated from http://www.iana.org/assignments/protocol-numbers and other
# sources.
# New protocols will be added on request if they have been officially
# assigned by IANA and are not historical.
# If you need a huge list of used numbers please install the nmap package.

ip	0	IP		# internet protocol, pseudo protocol number
hopopt	0	HOPOPT		# IPv6 Hop-by-Hop Option [RFC1883]
icmp	1	ICMP		# internet control message protocol
igmp	2	IGMP		# Internet Group Management
ggp	3	GGP		# gateway-gateway protocol
ipencap	4	IP-ENCAP	# IP encapsulated in IP (officially ``IP'')
st	5	ST		# ST datagram mode
tcp	6	TCP		# transmission control protocol
egp	8	EGP		# exterior gateway protocol
igp	9	IGP		# any private interior gateway (Cisco)
pup	12	PUP		# PARC universal packet protocol
udp	17	UDP		# user datagram protocol
hmp	20	HMP		# host monitoring protocol
xns-idp	22	XNS-IDP		# Xerox NS IDP
rdp	27	RDP		# "reliable datagram" protocol
iso-tp4	29	ISO-TP4		# ISO Transport Protocol class 4 [RFC905]
dccp	33	DCCP		# Datagram Congestion Control Prot. [RFC4340]
xtp	36	XTP		# Xpress Transfer Protocol
ddp	37	DDP		# Datagram Delivery Protocol
idpr-cmtp 38	IDPR-CMTP	# IDPR Control Message Transport
ipv6	41	IPv6		# Internet Protocol, version 6
ipv6-route 43	IPv6-Route	# Routing Header for IPv6
ipv6-frag 44	IPv6-Frag	# Fragment Header for IPv6
idrp	45	IDRP		# Inter-Domain Routing Protocol
rsvp	46	RSVP		# Reservation Protocol
gre	47	GRE		# General Routing Encapsulation
esp	50	IPSEC-ESP	# Encap Security Payload [RFC2406]
ah	51	IPSEC-AH	# Authentication Header [RFC2402]
skip	57	SKIP		# SKIP
ipv6-icmp 58	IPv6-ICMP	# ICMP for IPv6
ipv6-nonxt 59	IPv6-NoNxt	# No Next Header for IPv6
ipv6-opts 60	IPv6-Opts	# Destination Options for IPv6
rspf	73	RSPF CPHB	# Radio Shortest Path First (officially CPHB)
vmtp	81	VMTP		# Versatile Message Transport
eigrp	88	EIGRP		# Enhanced Interior Routing Protocol (Cisco)
ospf	89	OSPFIGP		# Open Shortest Path First IGP
ax.25	93	AX.25		# AX.25 frames
ipip	94	IPIP		# IP-within-IP Encapsulation Protocol
etherip	97	ETHERIP		# Ethernet-within-IP Encapsulation [RFC3378]
encap	98	ENCAP		# Yet Another IP encapsulation [RFC1241]
#	99			# any private encryption scheme
pim	103	PIM		# Protocol Independent Multicast
ipcomp	108	IPCOMP		# IP Payload Compression Protocol
vrrp	112	VRRP		# Virtual Router Redundancy Protocol [RFC5798]
l2tp	115	L2TP		# Layer Two Tunneling Protocol [RFC2661]
isis	124	ISIS		# IS-IS over IPv4
sctp	132	SCTP		# Stream Control Transmission Protocol
fc	133	FC		# Fibre Channel
mobility-header 135 Mobility-Header # Mobility Support for IPv6 [RFC3775]
udplite	136	UDPLite		# UDP-Lite [RFC3828]
mpls-in-ip 137	MPLS-in-IP	# MPLS-in-IP [RFC4023]
manet	138			# MANET Protocols [RFC5498]
hip	139	HIP		# Host Identity Protocol
shim6	140	Shim6		# Shim6 Protocol [RFC5533]
wesp	141	WESP		# Wrapped Encapsulating Security Payload
rohc	142	ROHC		# Robust Header Compression
ethernet 143	Ethernet	# Ethernet encapsulation for SRv6 [RFC8986]
# The following entries have not been assigned by IANA but are used
# internally by the Linux kernel.
mptcp	262	MPTCP		# Multipath TCP connection
```

<br>	
</details>

<details markdown='1'>
<summary>
/etc/python3/ and /etc/python3.*/ Folders:
</summary>

---
Folders exist in default Debian & Ubuntu installations.

/etc/python3/ contains debian_config file which contains settings related to the Debian-specific packaging of Python.

/etc/python3.*/: Depending on the Python version could be python3.10, python3.11 etc. Contains sitecustomize.py. This Python script is automatically imported during the initialization of the Python interpreter.

It allows administrators to customize the behavior of Python 3.* at the site level by adding their own customizations.

Sample contents:

```
# /etc/python3/debian_config
[DEFAULT]
# how to byte-compile (comma separated: standard, optimize)
byte-compile = standard
```

```
# /etc/python3.11/sitecustomize.py
# install the apport exception handler if available
try:
    import apport_python_hook
except ImportError:
    pass
else:
    apport_python_hook.install()
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/rc*.d/ Folders
</summary>

---
Folders exist in default Debian & Ubuntu installations.

Although both Debian & Ubuntu uses systemd for their init systems, it is possible to convert to System V init.

The scripts in these folders will be used if init system is changed to System V. That is, the folders exist as a compatability layer.

The purpose of these folders is to have the scripts when init goes to a runlevel.

<br>
</details>

<details markdown='1'>
<summary>
/etc/reportbug.conf
</summary>

---
File exists in default Debian installations.  
File doesn't exist in default Ubuntu installations.

Contains configuration settings for the reportbug tool, which is used to report bugs in Debian packages. This tool assists users in submitting bug reports to the Debian Bug Tracking System (BTS).

Excerpt from content:

```
# Example configuration file for reportbug(1)
# Options can be specified in any order
# usually, no-OPTION will disable OPTION if OPTION is boolean

# Default severity level; will bypass prompt in reportbug, so disabled
# severity normal

# BTS to use
# See 'reportbug --bts help' for a current list of supported BTSes
# bts debian

# Submission address: default is 'submit'
# Can also be 'quiet' or 'maintonly'; see --report-quiet and --maintonly
# entries on man page
submit

# Mailer to use (default is empty, to use internal mailer). One of:
# mutt
# mh
# nmh

# You can also use 'mua'; it takes an argument like that to --mua
# mua 'mutt'
#
# Additional headers to add:
# header "X-Silly-Header: I haven't edited my /etc/reportbug.conf"
# header "X-Debbugs-No-Ack: please" # to suppress acknowledgments

# The following boolean options can be disabled by adding 'no-'
# Should I query the BTS?
query-bts
#
# Should I check for newer releases of the package
# check-available
#
# Should I CC the reporter?
cc
#
# Should I ever include modified config files?
config-files
#
# Should I strip down modified config files?
compress
#
# Specify one of the following to digitally sign bug reports automatically.
# sign gpg
# sign pgp
# sign gnupg
# sign none #to disable signing
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/resolv.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Used to configure DNS (Domain Name System) resolver settings. 

DNS resolvers are responsible for translating domain names (e.g., www.example.com) into IP addresses that computers can use to communicate over a network.

In Ubuntu it is a symbolic link to /run/systemd/resolve/stub-resolv.conf. 

That is because Ubuntu uses systemd-networkd and systemd-resolvd.

Sample content:
```
# Nameservers
nameserver 192.168.1.1
nameserver 8.8.8.8
nameserver 8.8.4.4
#
# Search domain
search example.com
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/rmt
</summary>

---
File exists in default Debian & Ubuntu installations.

This file is a symbolic link to /usr/sbin/rmt	

rmt is used to manipulate tape drives.

Used for backward compatability.

<br>
</details>

<details markdown='1'>
<summary>
/etc/rpc
</summary>

---
File exists in default Debian & Ubuntu installations.

Used to define remote procedure call (RPC) program numbers and their associated service names. 

RPC is a protocol used by networked systems to allow programs to execute procedures or functions on remote systems as if they were local.

Sample content:

```
# This file contains user readable names that can be used in place of rpc
# program numbers.
#
portmapper	100000	portmap sunrpc rpcbind
rstatd		100001	rstat rstat_svc rup perfmeter
rusersd		100002	rusers
nfs		100003	nfsprog
ypserv		100004	ypprog
mountd		100005	mount showmount
ypbind		100007
walld		100008	rwall shutdown
yppasswdd	100009	yppasswd
etherstatd	100010	etherstat
rquotad		100011	rquotaprog quota rquota
sprayd		100012	spray
3270_mapper	100013
rje_mapper	100014
selection_svc	100015	selnsvc
database_svc	100016
rexd		100017	rex
alis		100018
sched		100019
llockmgr	100020
nlockmgr	100021
x25.inr		100022
statmon		100023
status		100024
bootparam	100026
ypupdated	100028	ypupdate
keyserv		100029	keyserver
tfsd		100037 
nsed		100038
nsemntd		100039
ypxfrd		100069
nfs_acl		100227
pcnfsd		150001
amd		300019	amq
sgi_fam		391002
ugidd		545580417
fypxfrd		600100069	freebsd-ypxfrd
bwnfsd          788585389
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/rsyslog.conf & /etc/rsyslog.d/ Folder
</summary>

---
File & folder don't exist in default Debian installations.  
File & folder exist in default Ubuntu installations.

/etc/rsyslog.conf is the main configuration file for the rsyslog daemon.

rsyslogd is a syslogd replacement that offers more features and performance. 

The rsyslog daemon is responsible for receiving log messages from various system components and forwarding them to the appropriate destinations, such as log files, remote syslog servers, or other logging services.

/etc/rsyslog.d/ folder contains additional configuration files which are included by rsyslog.conf.

Excerpt from /etc/rsyslog.conf

```
# /etc/rsyslog.conf configuration file for rsyslog
#
# For more information install rsyslog-doc and see
# /usr/share/doc/rsyslog-doc/html/configuration/index.html

# Default logging rules can be found in /etc/rsyslog.d/50-default.conf

#################
#### MODULES ####
#################

module(load="imuxsock") # provides support for local system logging
#module(load="immark")  # provides --MARK-- message capability

# provides UDP syslog reception
#module(load="imudp")
#input(type="imudp" port="514")

# provides UDP syslog reception
#module(load="imudp")
#input(type="imudp" port="514")

# provides TCP syslog reception
#module(load="imtcp")
#input(type="imtcp" port="514")

# provides kernel logging support and enable non-kernel klog messages
module(load="imklog" permitnonkernelfacility="on")

###########################
#### GLOBAL DIRECTIVES ####
###########################


# Use traditional timestamp format.
# To enable high precision timestamps, comment out the following line.

$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

# Filter duplicated messages
$RepeatedMsgReduction on


# Set the default permissions for all log files.
#
$FileOwner syslog
$FileGroup adm
$FileCreateMode 0640
$DirCreateMode 0755
```
 
<br>
</details>

<details markdown='1'>
<summary>
/etc/runit/ Folder
</summary>

---
Folder exists in default Debian installations.  
Folder doesn't exist in default Ubuntu installations.

Although Debian uses systemd for their init systems, it is  possible to convert to Runit init.

The scripts in the folder will be used if init system is changed to Runit. That is, the folder exists as a compatability layer.

<br>
</details>

<details markdown='1'>
<summary>
/etc/screenrc
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Configuration file for the GNU Screen utility. 

GNU Screen is a terminal multiplexer that allows users to run multiple terminal sessions within a single window or terminal emulator, making it easier to manage multiple tasks simultaneously.

<br>
</details>

<details markdown='1'>
<summary>
/etc/security/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and scripts related to system security settings, policies, and authentication mechanisms.

Some files and folders:

- access.conf: Used to configure access control rules based on user, group, and terminal. It defines which users or groups are allowed or denied access to specific system resources.
- capability.conf: Used to configure Linux capabilities settings. Linux capabilities are a feature that allows fine-grained control over the privileges of a process beyond the traditional user and group permissions.
- faillock.conf: Contains configuration settings for the faillock utility, which is used to manage user authentication failure records. These records track unsuccessful login attempts and enforce policies such as lockouts or delays to protect against brute-force attacks and unauthorized access.
- group.conf: Used to define group-based access control rules, such as granting or denying access to certain resources based on group membership.
- limits.conf: Used to set limits on system resources for users and processes. It can control limits such as maximum CPU time, maximum number of processes, maximum number of open files, and more.
- namespace.conf: Contains configuration settings for controlling process and namespace creation, which can affect system security and resource isolation.
- namespace.init: This script initializes namespace support on system startup. It may contain commands to set up namespace configurations and prepare the system for namespace-based isolation.
- opasswd: Stores hashed passwords of removed users. Used by utilities like passwd to prevent reuse of old passwords.
- pam_env.conf: Used to configure environment variables for users' sessions managed by the Pluggable Authentication Modules (PAM) subsystem. It allows system administrators to define custom environment variables that are set for users during login.
- time.conf: Used to configure time-based access control policies using the pam_time module. This module allows system administrators to restrict user access to certain services based on the time of day or day of the week.

<br>
</details>

<details markdown='1'>
<summary>
/etc/selinux/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Although Debian & Ubuntu doesn't have SELinux by default; they have the configuration folder and 1 file (semanage.conf) in that folder.

It is possible that this folder exists because of a dependency issue.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sensors3.conf and /etc/sensors.d/ Folder
</summary>

---
File and folder don't exist in default Debian installations.  
File and folder exist in default Ubuntu installations.

/etc/sensors3.conf is the configuration file for the libsensors library. /etc/sensors.d/ folder is used for including additional configuration snippets. Files placed in theis directory will be read as part of the main sensors3.d file.

The libsensors library is a core component of the lm_sensors package, which is widely used in Linux systems for hardware monitoring.

<br>
</details>

<details markdown='1'>
<summary>
/etc/services
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains a mapping of well-known service names to their corresponding port numbers. 

These service names and port numbers are used by various network services and utilities to identify and communicate with network services running on a system.

Excerpt from content:

```
# Network services, Internet style
#
# Updated from https://www.iana.org/assignments/service-names-port-numbers/
# service-names-port-numbers.xhtml .

# New ports will be added on request if they have been officially assigned
# by IANA and used in the real-world or are needed by a debian package.
# If you need a huge list of used numbers please install the nmap package.
tcpmux		1/tcp				# TCP port service multiplexer
echo		7/tcp
echo		7/udp
discard		9/tcp		sink null
discard		9/udp		sink null
systat		11/tcp		users
daytime		13/tcp
daytime		13/udp
netstat		15/tcp
qotd		17/tcp		quote
chargen		19/tcp		ttytst source
chargen		19/udp		ttytst source
ftp-data	20/tcp
ftp		21/tcp
fsp		21/udp		fspd
ssh		22/tcp				# SSH Remote Login Protocol
telnet		23/tcp
smtp		25/tcp		mail
time		37/tcp		timserver
time		37/udp		timserver
whois		43/tcp		nicname
tacacs		49/tcp				# Login Host Protocol (TACACS)
tacacs		49/udp
domain		53/tcp				# Domain Name Server
domain		53/udp
bootps		67/udp
bootpc		68/udp
tftp		69/udp
gopher		70/tcp				# Internet Gopher
finger		79/tcp
http		80/tcp		www		# WorldWideWeb HTTP
kerberos	88/tcp		kerberos5 krb5 kerberos-sec	# Kerberos v5
kerberos	88/udp		kerberos5 krb5 kerberos-sec	# Kerberos v5
iso-tsap	102/tcp		tsap		# part of ISODE
acr-nema	104/tcp		dicom		# Digital Imag. & Comm. 300
pop3		110/tcp		pop-3		# POP version 3
sunrpc		111/tcp		portmapper	# RPC 4.0 portmapper
sunrpc		111/udp		portmapper
auth		113/tcp		authentication tap ident
```

<br>

</details>

<details markdown='1'>
<summary>
/etc/sgml Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains resources, configurations, and catalog files for SGML (Standard Generalized Markup Language). SGML is a standardized markup language that serves as the basis for other markup languages like XML (eXtensible Markup Language) and HTML (HyperText Markup Language).

<br>
</details>

<details markdown='1'>
<summary>
/etc/shadow & /etc/shadow-
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/shadow file stores encrypted user passwords and related password information. It is used for authentication purposes to verify the identity of users attempting to log in to the system.

/etc/shadow- contains the previous state of /etc/shadow for backup purposes.

Sample content:

```
root:!:19588:0:99999:7:::
daemon:*:19588:0:99999:7:::
bin:*:19588:0:99999:7:::
sys:*:19588:0:99999:7:::
sync:*:19588:0:99999:7:::
games:*:19588:0:99999:7:::
man:*:19588:0:99999:7:::
lp:*:19588:0:99999:7:::
mail:*:19588:0:99999:7:::
news:*:19588:0:99999:7:::
uucp:*:19588:0:99999:7:::
proxy:*:19588:0:99999:7:::
www-data:*:19588:0:99999:7:::
backup:*:19588:0:99999:7:::
list:*:19588:0:99999:7:::
irc:*:19588:0:99999:7:::
_apt:*:19588:0:99999:7:::
nobody:*:19588:0:99999:7:::
systemd-network:!*:19588::::::
systemd-timesync:!*:19588::::::
```

Fields:

- Username
- Encrypted password
- Days from last password change
- Minimum password age
- Maximum password age
- Number of days before password expiration to warn
- Password inactivity period
- Account expiration date
- Reserved field

<br>
</details>

<details markdown='1'>
<summary>
/etc/shells
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains the available login shells on the system. 

Each line in the file represents the pathname of a shell executable that can be used as a valid login shell for user accounts.

Serves as a reference for system utilities and administration tools to determine which shells are valid for use as login shells. 

Sample content:

```
# /etc/shells: valid login shells
/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/sh
/bin/dash
/usr/bin/dash
/usr/bin/tmux
/usr/bin/screen
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/skel/	Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains template files and directories that are automatically copied to the home directory of a newly created user. 

Contains default configuration files, sample scripts, and directories commonly found in user home directories. 

Debian & Ubuntu default files:

- .bash_logout: Executed when the user logs out, typically used to perform cleanup tasks or save session information.
- .bashrc: Bash shell configuration file that sets environment variables, aliases, and other shell settings.
- .profile: Profile script that is executed when the user logs in, typically used to set environment variables and execute commands or scripts.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sos/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for sos report tool in Ubuntu.

Sos is a command-line tool used for collecting diagnostic information from a system for troubleshooting purposes.

Some files and folders:

- sos.conf: Contains main configuration settings for the "sos" utility.
- extras.d/: Stores configuration files used by the sos_extras plugin.
- groups.d/: Stores host group configuration files for sos collect.
- presets.d/: Stores preset configuration files for sos report.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ssh/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and keys related to the SSH (Secure Shell) service. 

Some files and folders:

- ssh_config: Contains client-side SSH configuration options. Applies to all users on the system.
- sshd_config: Contains server-side SSH configuration options. It determines how the SSH server operates and what security features are enforced.
- ssh_host_\*_key & ssh_host_\*_key.pub: Contain private and public keys used by the SSH server for host authentication.
- moduli: Contains Diffie-Hellman prime numbers used for key exchange. It is used to enhance the security of SSH connections.
- ssh_config.d/ & sshd_config.d/: Used for including additional configuration snippets. Files placed in these directories will be read as part of the main ssh_config or sshd_config files respectively.

Excerp from contents:

```
# /etc/ssh/ssh_config
# This is the ssh client system-wide configuration file.  See
# ssh_config(5) for more information.  This file provides defaults for
# users, and the values can be changed in per-user configuration files
# or on the command line.

# Configuration data is parsed as follows:
#  1. command line options
#  2. user-specific file
#  3. system-wide file
# Any configuration value is only changed the first time it is set.
# Thus, host-specific definitions should be at the beginning of the
# configuration file, and defaults at the end.

# Site-wide defaults for some commonly used options.  For a comprehensive
# list of available options, their meanings and defaults, please see the
# ssh_config(5) man page.
#
Include /etc/ssh/ssh_config.d/*.conf

Host *
#   ForwardAgent no
#   ForwardX11 no
#   ForwardX11Trusted yes
#   PasswordAuthentication yes
#   HostbasedAuthentication no
#   GSSAPIAuthentication no
#   GSSAPIDelegateCredentials no
#   GSSAPIKeyExchange no
#   GSSAPITrustDNS no
#   BatchMode no
#   CheckHostIP yes
#   AddressFamily any
#   ConnectTimeout 0
#   StrictHostKeyChecking ask
#   IdentityFile ~/.ssh/id_rsa
#   IdentityFile ~/.ssh/id_dsa
#   IdentityFile ~/.ssh/id_ecdsa
#   IdentityFile ~/.ssh/id_ed25519
#   Port 22
```

```
# /etc/ssh/sshd_config
# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.
# This sshd was compiled with PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/us>
# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.
#
Include /etc/ssh/sshd_config.d/*.conf

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
# Ciphers and keying
#RekeyLimit default none

# Logging
#SyslogFacility AUTH
#LogLevel INFO
#
# Authentication:
#
#LoginGraceTime 2m
#PermitRootLogin prohibit-password
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10
#
#PubkeyAuthentication yes
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/ssl/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains SSL/TLS-related configuration files and certificates. 

Some files and folders:

- openssl.cnf: OpenSSL configuration file. Defines default settings and behavior for OpenSSL commands and libraries.
- certs/: Contains various SSL/TLS certificates. Includes public keys of Certificate Authorities (CAs) or self-signed certificates.
- private/: Contains private keys used for SSL/TLS encryption. 

Excerpt from /etc/ssl/openssl.conf

```
# OpenSSL example configuration file.
# See doc/man5/config.pod for more info.

# This is mostly being used for generation of certificate requests,
# but may be used for auto loading of providers

# Note that you can include other files from the main configuration
# file using the .include directive.
#.include filename

# This definition stops the following lines choking if HOME isn't
# defined.
HOME                    = .

# Use this in order to automatically load providers.
openssl_conf = openssl_init

# Comment out the next line to ignore configuration errors
config_diagnostics = 1

# Extra OBJECT IDENTIFIER info:
# oid_file       = $ENV::HOME/.oid
oid_section = new_oids

# To use this configuration file with the "-extfile" option of the
# "openssl x509" utility, name here the section containing the
# X.509v3 extensions to use:
# extensions            =
# (Alternatively, use a configuration file that has only
# X.509v3 extensions in its main [= default] section.)
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/subgid & /etc/subgid- 
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/subgid specifies subordinate group IDs (subgids). These IDs are used for user namespaces.

/etc/subgid file defines ranges of subordinate group IDs that are allocated to non-root users.

Each line in the /etc/subgid file typically follows this format:

```
username:start_id:count
```

- username: Name of the user for whom the subordinate group IDs are being defined.
- start_id: The starting ID of the range of subordinate group IDs allocated to the user.
- count: The number of subordinate group IDs in the range.

/etc/subgid- contains the previous state of /etc/subgid for backup purposes.

<br>
</details>

<details markdown='1'>
<summary>
/etc/subuid & /etc/subuid-
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/subuid specifies subordinate user IDs (subuids). These IDs are used for user namespaces.

/etc/subuid file defines ranges of subordinate user IDs that are allocated to non-root users.

Each line in the /etc/subuid file typically follows this format:

```
username:start_id:count
```

- username: Name of the user for whom the subordinate user IDs are being defined.
- start_id: The starting ID of the range of subordinate user IDs allocated to the user.
- count: The number of subordinate user IDs in the range.

- /etc/subuid- contains the previous state of /etc/subuid for backup purposes.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sudo_logsrvd.conf & /etc/sudo.conf
</summary>

---
Files exist in default Debian & Ubuntu installations.

/etc/sudo_logsrvd.conf contains configurations for sudo's logsrv daemon.

/etc/sudo.conf contains configurations for sudo's behavior, such as settings related to authentication, logging, and plugin configuration.

Both Debian & Ubuntu files are fully commented.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sudoers and /etc/sudoers.d/ Folder
</summary>

---
File & folder exist in default Debian & Ubuntu installations.

/etc/sudoers is used to specify which users or groups are allowed to execute commands with elevated privileges using the sudo command.

The file is edited using the visudo command, which ensures that only one user can edit the file at a time and performs syntax checking before saving changes to prevent syntax errors that could lock users out of administrative access.

/etc/sudoers.d/ folder is included by /etc/suoders. 

Thus, instead of modifying the main /etc/sudoers file directly, administrators can place individual configuration files in this directory, and sudo will include them when parsing sudoers rules.

<br>
</details>

<details markdown='1'>
<summary>
/etc/supercat/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for supercat tool.

Supercat is a program that colorizes text based on matching regular expressions/strings/characters.

Sample contents for /etc/supercat/spcrc-crontab

```
# ============ this file is to colorize crontabs ==========
#        1         2         3         4         5
#2345678901234567890123456789012345678901234567890123456789
# HTML COLOR         COL A N T STRING or REGULAR EXPRESSION
#################### ### # # # ############################
#Where:
#  HTML COLOR - Standard HTML Color name for HTML output
#  COL        - Console color name from the list
#                 red, yel, cya, grn, mag, blk, whi, blu
#  A          - Attribute from the list
#                 ' ' : normal
#                 'b' : bold
#                 'u' : underline
#                 'r' : reverse video
#                 'k' : blink
#  N          - number of matches
#                 ' ' : all
#                 '0' : all
#                 '1' - '9' : number of matches
#  T          - type of matching to perform
#                 'c' : characters
#                 's' : string
#                 'r' : regex - case   sensitive
#                 'R' : regex - case insensitive
#                 't' : regex with Unix time conversion
#                 ' ' : default ('r' regex)
#        1         2         3         4         5
#2345678901234567890123456789012345678901234567890123456789
# HTML COLOR         COL A N T STRING or REGULAR EXPRESSION
#################### ### # # # ############################
#                                        dom is blue + bold
Blue                 blu b 5   \s+(\S+)
#                                     month is green + bold
Green                grn b 4   \s+(\S+)
#                              dow is green + reverse video
Green                grn r 3   \s+(\S+)
#                                        hour is red + bold
Red                  red b 2   \s+(\S+)
#                             minute is red + reverse video
Red                  red r 1   \s*(\S+)
#                                      comments are magenta
Magenta              mag       (^#.*)
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/sv/ Folder
</summary>

---
Folder exists in default Debian installations.  
Folder doesn't exist in default Ubuntu installations.

Although Debian uses systemd for their init systems, it is  possible to convert to Runit init.

The scripts in the folder will be used if init system is changed to Runit. That is, the folder exists as a compatability layer.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sysctl.conf & /etc/sysctl.d/ Folder
</summary>

---
File & folder exists in default Debian & Ubuntu installations.

/etc/sysctl.conf is used to configure kernel parameters

Each parameter is specified in the format parameter = value.

Sample /etc/sysctl.conf

```
# Disable source routing
net.ipv4.conf.default.accept_source_route = 0
net.ipv4.conf.all.accept_source_route = 0

# Enable TCP SYN Cookie Protection
net.ipv4.tcp_syncookies = 1

# Disable ICMP Redirect Acceptance
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0

# Disable IP Forwarding
net.ipv4.ip_forward = 0

# Disable IP Spoofing Protection
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Enable TCP Keepalive
net.ipv4.tcp_keepalive_time = 300
net.ipv4.tcp_keepalive_intvl = 60
net.ipv4.tcp_keepalive_probes = 9

# Set maximum number of SYN Backlog Queue
net.ipv4.tcp_max_syn_backlog = 2048

# Increase system file descriptor limit
fs.file-max = 65535

# Increase system IP port range
net.ipv4.ip_local_port_range = 1024 65535

# Set maximum number of allowed PIDs
kernel.pid_max = 65536

# Disable IPv6
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
```

After changing sysctl.conf parameters, you can use the following command to activate them:

```
sudo sysctl -p
```

/etc/sysctl.d/ folder is used for including additional configuration parameters. Files placed in this directory will be read as part of the main sysctl.conf file.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sysstat/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for sysstat tool. Sysstat is a collection of system performance monitoring tool which is  designed to monitor various aspects of system performance, such as CPU usage, memory usage, disk activity, network traffic, and more. 

Sample contents for /etc/sysstat/sysstat:

```
# sysstat configuration file. See sysstat(5) manual page.

# How long to keep log files (in days).
# Used by sa2(8) script
# If value is greater than 28, then use sadc's option -D to prevent older
# data files from being overwritten. See sadc(8) and sysstat(5) manual pages.
HISTORY=7

# Compress (using xz, gzip or bzip2) sa and sar files older than (in days):
COMPRESSAFTER=10

# Parameters for the system activity data collector (see sadc(8) manual page)
# which are used for the generation of log files.
# By default contains the `-S DISK' option responsible for generating disk
# statisitcs. Use `-S XALL' to collect all available statistics.
SADC_OPTIONS="-S DISK"

# Directory where sa and sar files are saved. The directory must exist.
SA_DIR=/var/log/sysstat

# Compression program to use.
ZIP="xz"

# By default sa2 script generates yesterday's summary, since the cron job
# usually runs right after midnight. If you want sa2 to generate the summary
# of the same day (for example when cron job runs at 23:53) set this variable.
#YESTERDAY=no

# By default sa2 script generates reports files (the so called sarDD files).
# Set this variable to false to disable reports generation.
#REPORTS=false

# Tell sa2 to wait for a random delay in the range 0 .. ${DELAY_RANGE} before
# executing. This delay is expressed in seconds, and is aimed at preventing
# a massive I/O burst at the same time on VM sharing the same storage area.
# Set this variable to 0 to make sa2 generate reports files immediately.
DELAY_RANGE=0

# The sa1 and sa2 scripts generate system activity data and report files in
# the /var/log/sysstat directory. By default the files are created with umask 0>
# and are therefore readable for all users. Change this variable to restrict
# the permissions on the files (e.g. use 0027 to adhere to more strict
# security standards).
UMASK=0022
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/systemd/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and directories related to the systemd init system and its other services.

Some files and folders:

- journald.conf: Configurations of for systemd's journal service (journald). Allows configuring settings related to system logging, including log rotation, storage options, and log levels.
- logind.conf: Configurations of systemd's login manager (logind). Allows configuring settings related to user sessions, power management, and other login-related behavior.
- resolved.conf: Configuration file for systemd's resolved, a system service that provides DNS name resolution to local applications. This file allows you to configure DNS-related settings such as DNS server addresses and DNSSEC validation.
- system.conf: Contains global systemd settings. Allows configuring various global settings related to systemd's behavior, such as default resource limits, process priorities, and cgroup hierarchy settings.
- timesyncd.conf: Configuration file for systemd's  timesyncd, which provides network time synchronization services.
- user.conf: Similar to system.conf, contains configuration options specifically for user sessions managed by systemd.
- network/: Contains network configuration files for systemd-networkd, a system service responsible for network configuration and management.
- system/: Contains system-specific unit files. Unit files describe how systemd should manage system services, sockets, devices, mounts, and other system resources.
- user/: Similar to /etc/systemd/system/, but contains unit files for user specific services. These services are started and managed by systemd on behalf of individual users.

<br>
</details>

<details markdown='1'>
<summary>
/etc/terminfo/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Default Debian and Ubuntu installation only has a README file in this folder.

Normally, contains terminal capability database files used by various terminal-related applications. 

These files define the capabilities and characteristics of different types of terminals, allowing programs to interact with them appropriately.

<br>
</details>

<details markdown='1'>
<summary>
/etc/thermald/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for the Thermal Daemon (thermald).

thermald is a system daemon designed to monitor and control thermal related issues in the system. It helps in managing thermal throttling and preventing overheating of the system by dynamically adjusting the CPU frequency and other parameters based on thermal sensor readings.

thermal-cpu-cdev-order.xml is the only file in default Ubuntu installations. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/timezone
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains the name of the timezone configured for the system. 

It is used by various system utilities and applications to determine the timezone settings.

Sample contents:

```
America/New_York
```

```
Europe/Istanbul
```

```
Etc/UTC
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/tmpfiles.d/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.  
Folder is empty in default Debian installations.

Contains configurations used by systemd to manage temporary files and directories at boot time and during runtime. 

Allows administrators to create configuration files to specify the creation, deletion, and modification of temporary files and directories.

<br>

</details>

<details markdown='1'>
<summary>
/etc/ubuntu-advantage/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files related to the Ubuntu Advantage service, which is Canonical's commercial support program for Ubuntu. 

Sample content:

```
# /etc/ubuntu-advantage/uaclient.conf
contract_url: https://contracts.canonical.com
log_level: debug
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/ucf.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Associated with the "update configuration files" (UCF) utility.

UCF is a tool used during package installation or upgrade to handle configuration file updates in a more user-friendly and automated manner.

Sample content:

```
# This file is a bourne shell snippet, and is sourced by the
# ucf script for configuration.
#
#
# Debugging information: The default value is 0 (no debugging
# information is printed). To change the default behavior, uncomment
# the following line and set the value to 1.
#
# DEBUG=0
#
# Verbosity: The default value is 0 (quiet). To change the default
# behavior, uncomment the following line and set the value to 1.
#
# VERBOSE=0
#
#
# The src directory. This is the directory where the historical
# md5sums for a file are looked for.  Specifically, the historical
# md5sums are looked for in the subdirectory ${filename}.md5sum.d/
#
# conf_source_dir=/some/path/
#
# Force the installed file to be retained. The default is have this
# variable unset, which makes the script ask in case of doubt. To
# change the default behavior, uncomment the following line and set
# the value to YES
#
# conf_force_conffold=YES
#
# Force the installed file to be overridden. The default is have this
# variable unset, which makes the script ask in case of doubt. To
# change the default behavior, uncomment the following line and set
# the value to YES
#
# conf_force_conffnew=YES
#
# Please note that only one of conf_force_conffold and
# conf_force_conffnew should be set.
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/udev/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files for the udev (device manager) subsystem.

udev is responsible for managing device nodes in the /dev directory and handling device events, such as device insertion, removal, and hot-plugging.

Some files and folders:

- udev.conf: Contains global configuration options for udev. Allows administrators to specify settings such as logging verbosity, device naming conventions, and default behavior for device events.
- hwdb.d/: Contains hardware database files used by udev to match devices based on their hardware properties. This folder is empty on default Debian & Ubuntu installations.
- rules.d/: Contains rule files that specify how udev should handle devices and device events. This folder is empty on default Debian installations.

<br>
</details>

<details markdown='1'>
<summary>
/etc/udisks2/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for UDisks 2 service.

UDisks 2 is a system service that provides a standardized interface for managing storage devices such as hard disks, solid-state drives, USB drives, and optical drives.

Some files:

- udisks2.conf: Configuration options for the UDisks 2 service. Allows administrators to specify settings such as device permissions, mount options, and storage policies.
- mount_options.conf: Configuration file specifying default mount options for filesystems managed by UDisks 2. Administrators can define options such as read/write permissions, filesystem type, and other mount-related settings.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ufw/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files and directories for the Uncomplicated Firewall (UFW). 

UFW provides a user-friendly interface for managing netfilter, the Linux kernel's firewall subsystem, by simplifying the process of creating and maintaining firewall rules.

Default Debian installations only has application.d folder.

Some files and folders:

- ufw.conf: Contains main configuration settings for UFW. Allows administrators to specify general options such as default policies, logging settings, and whether UFW should be enabled at boot.
- before.rules & after.rules: Contain additional iptables rules that are applied before and after the main UFW ruleset, respectively. You can use these files to add custom iptables rules that UFW does not directly support.
- before6.rules & after6.rules: Similar to after.rules and before.rules, contain additional IPv6 iptables rules that are applied before and after the main UFW ruleset.
- before.init & after.init: Scripts that are executed by UFW during its initialization process, specifically before and after the firewall rules are loaded.
- user.rules: Contains the user-defined firewall rules managed by UFW. Any custom rules added by the administrator using the ufw command-line tool are stored in this file.
- user6.rules: Similar to user.rules, this file contains user-defined IPv6 firewall rules managed by UFW.
- applications.d/: Contains application profiles that define predefined firewall rules for specific applications or services. 

<br>
</details>

<details markdown='1'>
<summary>
/etc/update-manager/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for the Update Manager, which is a  tool used for managing software updates on the system.

Some files and folders:

- meta-release: Contains information about available Ubuntu releases and their upgrade paths. It's used by the Update Manager to determine which releases are available for upgrade and to provide information about the upgrade process.
- release-upgrades: Contains configuration options for the release upgrade process, allowing administrators to specify settings such as whether to allow non-LTS (Long Term Support) releases, whether to prompt for release upgrades, and the default behavior for release upgrades.
- release-upgrades.d/: Contains additional configuration files for release upgrades. Administrators can place custom configuration files here to override or extend the default behavior specified in /etc/update-manager  /release-upgrades.

Sample contents:

```
# /etc/update-manager/meta-release
# default location for the meta-release file
#
[METARELEASE]
URI = https://changelogs.ubuntu.com/meta-release
URI_LTS = https://changelogs.ubuntu.com/meta-release-lts
URI_UNSTABLE_POSTFIX = -development
URI_PROPOSED_POSTFIX = -proposed
```

```
# /etc/update-manager/release-upgrades
# Default behavior for the release upgrader.
#
[DEFAULT]
# Default prompting and upgrade behavior, valid options:
#
#  never  - Never check for, or allow upgrading to, a new release.
#  normal - Check to see if a new release is available.  If more than one new
#           release is found, the release upgrader will attempt to upgrade to
#           the supported release that immediately succeeds the
#           currently-running release.
#  lts    - Check to see if a new LTS release is available.  The upgrader
#           will attempt to upgrade to the first LTS release available after
#           the currently-running one.  Note that if this option is used and
#           the currently-running release is not itself an LTS release the
#           upgrader will assume prompt was meant to be normal.
Prompt=lts
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/update-motd.d/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains scripts to customize the Message of the Day (motd) displayed to users when they log in via SSH or on a virtual console. 

The Message of the Day typically provides system information, such as available updates, system status, or important notifications, to users upon login.

The scripts are executed in alphabetical order, and their output is concatenated to form the complete motd message presented to users.

Sample contents:

/etc/update-motd.d/uname

```
#!/bin/sh
uname -snrvm
```

/etc/update-motd.d/85-fwupd

```
#!/bin/sh
if [ -f /run/motd.d/85-fwupd ]; then
        cat /run/motd.d/85-fwupd
fi
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/update-notifier/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.  
Folder is empty in default Ubuntu installations.

Contains configuration files and scripts for the update-notifier package. 

update-notifier package provides notifications and reminders about available software updates to the system administrator and regular users.

<br>
</details>

<details markdown='1'>
<summary>
/etc/UPower/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for UPower utility.

UPower is a power management service that provides information about power sources and battery status.

Sample content:

```
# /etc/UPower/Upower.conf
[UPower]

# Enable the Watts Up Pro device.
#
# The Watts Up Pro contains a generic FTDI USB device without a specific
# vendor and product ID. When we probe for WUP devices, we can cause
# the user to get a perplexing "Device or resource busy" error when
# attempting to use their non-WUP device.
#
# The generic FTDI device is known to also be used on:
#
# - Sparkfun FT232 breakout board
# - Parallax Propeller
#
# default=false
EnableWattsUpPro=false
#
# Don't poll the kernel for battery level changes.
#
# Some hardware will send us battery level changes through
# events, rather than us having to poll for it. This option
# allows disabling polling for hardware that sends out events.
#
# default=false
NoPollBatteries=false
#
# Do we ignore the lid state
#
# Some laptops are broken. The lid state is either inverted, or stuck
# on or off. We can't do much to fix these problems, but this is a way
# for users to make the laptop panel vanish, a state that might be used
# by a couple of user-space daemons. On Linux systems, see also
# logind.conf(5).
#
# default=false
IgnoreLid=false
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/usb_modeswitch.conf & /etc/usb_modeswitch.d/ Folder
</summary>

---
File & folder don't exist in default Debian installations.  
File & folder exist in default Ubuntu installations.

/etc/usb_modeswitch.conf is the configuration file for the usb_modeswitch package

It is evaluated by the wrapper script /usr/sbin/usb_modeswitch_dispatcher.

usb_modeswitch is a mode switching tool for USB devices providing multiple states or modes. It is used to handle USB devices that present themselves as USB storage but actually contain modem firmware.

/etc/usb_modeswitch.d/ contains additional configuration files that are included in /usr/sbin/usb_modeswitch_dispatcher.

<br>
</details>

<details markdown='1'>
<summary>
/etc/vconsole.conf
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Used to configure the virtual console settings, specifically for managing the console's keyboard layout, font, and other related settings.

Sample contents on Ubuntu 24.04:

```
# KEYBOARD CONFIGURATION FILE

# Consult the keyboard(5) manual page.

XKBMODEL="pc105"
XKBLAYOUT="tr"
XKBVARIANT=""
XKBOPTIONS=""

BACKSPACE="guess"
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/vim/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains system-wide Vim configuration files. 

Vim is a highly configurable text editor, and these files provide default settings and configurations that apply to all users on the system.

Some files:

- vimrc: Main system-wide Vim configuration file. Sets default options and key bindings for all users of Vim on the system.
- vimrc.tiny: Configuration options specifically for the "tiny" version of Vim, which is a minimized version of Vim with fewer features.

<br>
</details>

<details markdown='1'>
<summary>
/etc/vmware-tools/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Contains configuration files for VMware Tools.

VMware Tools is a suite of utilities and services designed to enhance the performance and manageability of virtual machines (VMs) running on VMware platforms.

The folder contains configuration files, scripts, logging and debugging information.

Sample contents for /etc/vmware-tools/tools.conf file on Ubuntu:

```
[logging]
# Turns on logging globally. It can still be disabled for each domain.
# log = true

# Disables core dumps on fatal errors; they're enabled by default.
# enableCoreDump = false

# Defines the "vmsvc" domain, logging to file
# vmsvc.level = message
vmsvc.handler = file
# Setup file rotation - keep 3 files
vmsvc.maxOldLogFiles = 3
# Max log file size kept: 1 MB
vmsvc.maxLogSize = 1

# Defines the "vmtoolsd" domain, and disable logging for it.
# vmtoolsd.level = none
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/vtrgb
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

This file is a symbolic link to /etc/alternatives/vtrgb, which is a symbolic link to /etc/console-setup/vtrgb

Used as a default input for the setvtrgb utility, which uses these values to set the color palette for virtual terminals.

<br>
</details>

<details markdown='1'>
<summary>
/etc/wgetrc
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains configuration settings for the wget utility. 

Wget is a command-line tool used for downloading files from the internet using various protocols like HTTP, HTTPS, and FTP.

<br>
</details>

<details markdown='1'>
<summary>
/etc/X11/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files related to the X Window System (X11).

X11 is the windowing system used to provide a graphical user interface (GUI) in Unix-like operating systems.

Although Debian and Ubuntu server installations don't have GUI by default, it seems that they need this folder for compatibility or dependancy issues.

<br>
</details>

<details markdown='1'>
<summary>
/etc/xattr.conf
</summary>

---
File exists in default Debian & Ubuntu installations.

Contains configurations of extended attributes (xattrs). 

Extended attributes allow to associate metadata with files and directories beyond typical inode. 

This metadata can include things like access control lists (ACLs), SELinux security contexts, file capabilities, etc.

Sample content:

```
# /etc/xattr.conf
#
# Format:
# <pattern> <action>
#
# Actions:
#   permissions - copy when trying to preserve permissions.
#   skip - do not copy.
system.nfs4_acl                 permissions
system.nfs4acl                  permissions
system.posix_acl_access         permissions
system.posix_acl_default        permissions
trusted.SGI_ACL_DEFAULT         skip            # xfs specific
trusted.SGI_ACL_FILE            skip            # xfs specific
trusted.SGI_CAP_FILE            skip            # xfs specific
trusted.SGI_DMI_*               skip            # xfs specific
trusted.SGI_MAC_FILE            skip            # xfs specific
xfsroot.*                       skip            # xfs specific; obsolete
user.Beagle.*                   skip            # ignore Beagle index data
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/xdg/ Folder
</summary>

---
Folder exists in default Debian & Ubuntu installations.

Contains configuration files for XDG (X Desktop Group) Base Directory Specification. 

This specification defines a set of standard directories for storing user specific configuration, cache, and data files for desktop applications.

Although Debian and Ubuntu server installations don't have GUI (and hence X Desktop) by default, it seems that they need this folder for compatibility and dependancy issues.

<br>
</details>

<details markdown='1'>
<summary>
/etc/xml/ Folder
</summary>

---
Folder doesn't exist in default Debian installations.  
Folder exists in default Ubuntu installations.

Used to manage XML-related configurations, catalogs, and resources. It's often associated with the system-wide setup for XML parsers and applications that deal with XML files. 

This folder plays a significant role in defining how XML-related software operates, specifying catalog files, and defining XML entities and namespaces.

<br>
</details>

<details markdown='1'>
<summary>
/etc/zsh_command_not_found
</summary>

---
File doesn't exist in default Debian installations.  
File exists in default Ubuntu installations.

Used by the Zsh shell to provide suggestions when a command is not found.

When a user types a command that does not exist in the system's PATH, Zsh will check if the /etc/zsh_command_not_found file exists and is executable.

If it is, Zsh will execute this file with the original command as an argument.
</details>

