##### Etc Folder 
# /etc Folder on Debian and Ubuntu

<details markdown='1'>
<summary>
Specs
</summary>

---
### Info

The `/etc` directory is a crucial part of the filesystem hierarchy. Its name stands for "et cetera," and it stores system-wide configuration files and directories.

These configuration files control various aspects of the operating system, services, and installed applications—virtually everything—on a Linux system.

This guide attempts to cover all files and folders under `/etc` for a default installation of Debian 13 (without GUI) and Ubuntu 24.04 Server Edition. Some important packages are also included.


### Sources
- [ChatGPT](https://chatgpt.com)
- [Deepseek](https://www.deepseek.com/)
- [Debian](https://manpages.debian.org/) and [Ubuntu](https://manpages.ubuntu.com/) man pages 

<br>
</details>

<details markdown='1'>
<summary>
/etc/.pwd.lock
</summary>

---
This file exists in default Ubuntu and Debian installations.

It is used by the system to prevent multiple simultaneous changes to the system password database.

The `lckpwdf()` and `ulckpwdf()` functions manage modification access to the password databases via this lock file.

A process first calls `lckpwdf()` to lock the file, gaining exclusive rights to modify the `/etc/passwd` or `/etc/shadow` database.


<br>
</details>

<details markdown='1'>
<summary>
/etc/.updated
</summary>

---
This file exists in default Ubuntu and Debian installations.

It is updated by `systemd-update-done.service` when the `/usr` directory is updated, storing a timestamp.

Sample content on Debian:

```
# This file was created by systemd-update-done. Its only 
# purpose is to hold a timestamp of the time this directory
# was updated. See man:systemd-update-done.service(8).
TIMESTAMP_NSEC=1760517533879884038
```

<br>
</details>


<details markdown='1'>
<summary>
/etc/adduser.conf
</summary>

---
File exists in default Ubuntu & Debian installations.

It configures default settings for the `adduser` and `addgroup` commands, which create new users and groups on the system.

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
This file exists in default Debian installations.  
It does **not** exist in default Ubuntu installations.

It stores hardware clock (Real-Time Clock or RTC) time adjustment information.

The hardware clock is often inaccurate, but much of its inaccuracy is predictable—it gains or loses the same amount of time each day, known as **systematic drift**.

Sample content:

```
0.000000 1692481832 0.000000
1692481832
UTC
```
 
**Explanation:** 

- **First line:** Three numbers separated by spaces:
    - **Drift factor:** Systematic drift rate in seconds per day.
    - **Last adjust time:** Seconds since 1969 UTC of the most recent adjustment or calibration.
    - **Adjustment status:** 0.
- **Second line:** Last calibration time (seconds since 1969 UTC). Zero if no calibration has been performed.
- **Third line:** Clock mode: `UTC` or `LOCAL`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/aliases
</summary>

---
This file does **not** exist in default Ubuntu or Debian installations.

It is used with Postfix (or Sendmail) to define email aliases.

Changes require running the `newaliases` command to rebuild the alias database.

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
This folder exists in default Ubuntu and Debian installations.

It contains symbolic links pointing to the currently selected default version of a program or utility.

Administrators can use the `update-alternatives` command to manage these symbolic links and change the default version.

Excerpt from a directory listing:

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
This folder does **not** exist in default Ubuntu or Debian installations.  
It is created after installing the Apache2 package.

It contains configuration settings for the Apache2 web server.

Key files and folders:

- **`apache2.conf`:** The main configuration file for Apache. Contains global directives that apply to the entire server.
- **`ports.conf`:** Specifies the ports on which the server listens for incoming connections.
- **`envvar`:** A script that sets environment variables for the Apache HTTP Server process.
- **`magic`:** Contains definitions used by Apache to identify file types based on content (used by the `mod_mime_magic` module).
- **`conf-available/` and `conf-enabled/`:** Contain configuration files for various Apache components. Files in `conf-available/` can be enabled by creating symbolic links in `conf-enabled/`.
- **`mods-available/` and `mods-enabled/`:** Contain Apache modules. Modules in `mods-available/` can be enabled by creating symbolic links in `mods-enabled/`.
- **`sites-available/` and `sites-enabled/`:** Contain configuration files for Apache virtual hosts (websites). Virtual hosts in `sites-available/` can be enabled by creating symbolic links in `sites-enabled/`.

<br>
</details>



<details markdown='1'>
<summary>
/etc/apparmor/ Folder and /etc/apparmor.d/ Folder
</summary>

---
These folders exist in default Ubuntu and Debian installations.

- **`/etc/apparmor.d/`** contains configuration files that define access control policies for various applications and services.
- **`/etc/apparmor/`** contains configuration for AppArmor itself.

Excerpt from `/etc/apparmor/parser.conf`:

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
- **Debian:** This folder does **not** exist in default installations.
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **Apport**, a system crash and problem reporting tool.  
Apport automatically collects information about crashes and system errors, allowing users to report them to developers for analysis and debugging.

Key files and folders:

- **`apport.conf`:** Global configuration options for Apport.
- **`crashdb.conf`:** Configures Apport’s crash database behavior (e.g., database backend, authentication credentials).
- **`blacklist.d/`:** Contains configuration files specifying executables or packages excluded from Apport’s error reporting.

<br>
</details>

<details markdown='1'>
<summary>
/etc/apt/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and directories for the **Advanced Package Tool (APT)**.

Key files and folders:

- **`sources.list`:** Specifies package repositories from which APT retrieves packages. Each line represents a repository with its URL and additional options.
- **`auth.conf.d/`:** Contains authentication configuration (empty by default).
- **`apt.conf.d/`:** Contains configuration files that control APT’s behavior (e.g., proxy settings, package cache management, authentication).
- **`keyrings/`:** Contains the system’s default keyring files used to verify package authenticity.
- **`listchanges.d/`:** Configuration files for `apt-listchanges`, a tool that displays summaries of package changes before installation or upgrade.
- **`preferences.d/`:** Contains configuration files that control package installation preferences, influencing APT’s decisions on version selection and upgrades.
- **`sources.list.d/`:** Additional repository configuration files included alongside `sources.list`.
- **`trusted.gpg.d/`:** Contains additional trusted GPG keys added manually for package verification.

<br>
</details>

<details markdown='1'>
<summary>
/etc/bash_completion
</summary>

---
This file exists in default Debian and Ubuntu installations.

It contains the script used to configure Bash completion functionality for the Bash shell.

On Debian and Ubuntu, it typically includes the path to the main completion script.

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
This folder exists in default Debian and Ubuntu installations.

It contains additional scripts for Bash completion functionality.

Example script (`/etc/bash_completion.d/git-prompt`):

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
This file exists in default Debian and Ubuntu installations.

It is a system-wide initialization script for the Bash shell, executed whenever Bash starts an interactive login shell.

It contains global settings, aliases, shell options, and environment variables.

Excerpt:

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
This folder does **not** exist in default Ubuntu or Debian installations.  
It is created after installing the **BIND** package.

It contains configuration files and directories for the BIND DNS server, one of the most commonly used DNS servers on the internet.

Key files:

- **`bind.keys`:** Contains shared secrets used for DNSSEC operations and communication between DNS servers.
- **`db.*`:** Zone files used by BIND (e.g., `db.0`, `db.127`, `db.255`, `db.local`, `db.empty`).
- **`named.conf`:** The main configuration file for BIND; typically includes other configuration files.
- **`named.conf.default-zones`:** Contains default zone definitions provided by the BIND package.
- **`named.conf.local`:** Configures local zones specific to the server.
- **`named.conf.options`:** Contains global configuration options (e.g., listening addresses, logging, default query behavior).

<br>
</details>

<details markdown='1'>
<summary>
/etc/bindresvport.blacklist
</summary>

---
This file exists in default Debian and Ubuntu installations.

It specifies ports that should **not** be bound by privileged programs using "reserved ports" (ports below 1024).  
Traditionally, only privileged processes can bind to these ports.

Sample content:

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
This folder exists (and is empty) in default Debian and Ubuntu installations.

It is used to configure **Binary Format (binfmt) handlers**—a Linux kernel feature that enables execution of binary files in different formats by automatically invoking the appropriate interpreter or virtual machine.

Example configuration (`/etc/binfmt.d/wine.conf`):

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
This file does **not** exist in default Debian or Ubuntu installations.

It allows customization of the behavior of the `blkid` command.

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files and scripts related to **Byobu**, a terminal multiplexer that enhances GNU Screen or tmux functionality.

Example files:

**`/etc/byobu/backend`:**

```
# /etc/byobu/backend
# BYOBU_BACKEND can currently be "screen" or "tmux"
# Override this on a per-user basis by editing "$BYOBU_CONFIG_DIR/backend"
# or by launching either "byobu-screen" or "byobu-tmux" instead of "byobu".
BYOBU_BACKEND="tmu
```

**`/etc/byobu/socketdir`:**

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
These folders exist in default Debian and Ubuntu installations.

- **`/etc/ca-certificates/`** folder contains only an empty `update.d/` subdirectory by default.
- **`/etc/ca-certificates.conf`** lists certificates to be installed (or ignored) in `/etc/ssl/certs/`.
- Manually installed certificates are placed in `/etc/ca-certificates/`.

Example `/etc/ca-certificates.conf` content:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files and scripts for **cloud-init**, a tool for customizing cloud instances during initial boot.

Key contents:

- **`cloud.cfg`:** Top-level settings used as module and base configuration.
- **`ds-identify`:** Identifies the cloud platform.
- **`cloud.cfg.d/`:** Additional configuration snippets included in `cloud.cfg`.
- **`clean.d/`:** Cleanup scripts for third-party applications when `cloud-init clean` is invoked.
- **`templates/`:** Template files used by cloud-init to generate configuration files dynamically during boot.

<br>
</details>

<details markdown='1'>
<summary>
/etc/credstore/ and /etc/credstore.encrypted/ Folders
</summary>
---

These folders exist in default Debian and Ubuntu installations but are empty by default.

They are used by **systemd** to store and load credentials (including encrypted credentials) for systemd services.

<br>
</details>

<details markdown='1'>
<summary>
/etc/console-setup Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files for console font and keyboard layout settings on Debian-based systems, affecting the text-mode console (TTY) during system boot and when no graphical interface is available.

<br>
</details>

<details markdown='1'>
<summary>
/etc/crontab and /etc/cron.*/ Folders
</summary>

---
These files and folders exist in default Debian and Ubuntu installations.

**`/etc/crontab`** defines system-wide cron jobs that run at scheduled intervals.

Example content:

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

Each line in `/etc/crontab` follows the format:  
`minute hour day_of_month month day_of_week user command_to_run`

**Additional cron directories:**

- **`/etc/cron.d/`:** Contains additional cron tasks.
- **`/etc/cron.hourly/`, `/etc/cron.daily/`, `/etc/cron.weekly/`, `/etc/cron.monthly/`, `/etc/cron.yearly/`:** Contain scripts for hourly, daily, weekly, monthly, and yearly tasks, respectively.
- **`/etc/cron.deny`** (not present by default): Lists users prohibited from using the `cron` command.

<br>
</details>

<details markdown='1'>
<summary>
/etc/cryptsetup-initramfs/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the `cryptsetup` tool, specifically for setting up encrypted volumes during the initial ramdisk (initramfs) stage of boot.

It may include hooks, configuration options, and scripts.  
Ubuntu installations contain only the `conf-hook` file by default.

Excerpt from `/etc/cryptsetup-initramfs/conf-hook`:

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
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It describes encrypted block devices that are set up during system boot.

Example configuration:

```
# <name>       <source>         <keyfile>       <options>
encrypted_data /dev/sdb1        /etc/keys/encrypted_data.key   luks
```

In this example, the encrypted block device `/dev/sdb1` is configured to be unlocked during boot using LUKS encryption. The key is stored in `/etc/keys/encrypted_data.key`, and the mapped device is named `encrypted_data`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/cups/ Folder
</summary>

---
This folder does **not** exist in default Debian or Ubuntu installations.

It contains configuration files for **CUPS** (Common UNIX Printing System).

Key files and folders:

- **`cupsd.conf`:** Main configuration file for CUPS. Contains server settings such as network interfaces, access control, printer sharing, and logging.
- **`cups-files.conf`:** Configuration options for file and directory locations used by CUPS (e.g., spool directories, temporary files, error logs).
- **`cups-browsed.conf`:** Configuration for `cups-browsed`.
- **`snmp.conf`:** Configuration for SNMP support in CUPS.
- **`interfaces/`:** Configuration files for printer interfaces (USB, network, Bluetooth, etc.).
- **`ppd/`:** Contains Printer Description Files (PPDs) that describe printer capabilities and settings.
- **`ssl/`:** SSL/TLS certificates and keys for secure communication between CUPS clients and the server.

<br>
</details>

<details markdown='1'>
<summary>
/etc/dbus-1/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

- **Debian:** Contains two empty subfolders: `session.d` and `system.d`.
- **Ubuntu:** Contains the same two subfolders; `session.d` is empty.

It holds configuration files for **`dbus-daemon-1`** (Message Bus Daemon).  
D-Bus is a library that provides one-to-one communication between applications.  
`dbus-daemon-1` is an application that uses this library to implement a message bus daemon.

<br>
</details>

<details markdown='1'>
<summary>
/etc/debconf.conf
</summary>

---
This file exists in default Debian and Ubuntu installations.

It configures the behavior of the **debconf** package, a configuration management system for Debian packages.

Debconf handles configuration prompts and manages configuration files during package installation and upgrade.

Excerpt:


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
This file exists in default Debian and Ubuntu installations.

It contains the version number of the Debian operating system (or Ubuntu's base) installed on the system, providing a simple way to check the current version.

Example contents:

**Debian 13:**

```
13.1
```

**Ubuntu 24.04:**

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
This folder exists in default Debian and Ubuntu installations.

It contains configuration files for various system services and utilities, defining default settings, environment variables, and other options that control their behavior.

These files are often minimal (mostly comments) and are intended to be modified by system administrators as needed.

Example files:

**`/etc/default/ssh`:**

```
# Default settings for openssh-server. This file is sourced by /bin/sh from
# /etc/init.d/ssh.

# Options to pass to sshd
SSHD_OPTS=
```

**`/etc/default/keyboard`:**

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
This file exists in default Ubuntu and Debian installations.

It configures default settings for the `deluser` command.

Example content:

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

This folder exists in default Debian and Ubuntu installations.

It contains configuration files for **depmod**, a utility that generates `modules.dep` and map files for the kernel module loading system.

Linux kernel modules can provide services (called "symbols") for other modules. If a module uses a symbol from another module, it depends on that module.  
`depmod` reads each module under `/lib/modules/<version>/` to determine exported and needed symbols, then writes the dependency list to `modules.dep`.

- **Debian:** No files by default.
- **Ubuntu:** Contains one file, `ubuntu.conf`, with the following content:

```
search updates ubuntu built-in
```

The `search` keyword specifies the order in which `/lib/modules` subdirectories are processed by `depmod`.

<br>
</details>



<details markdown='1'>
<summary>
/etc/dhcp/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files for the DHCP daemon and client.

Key files and folders:

- **`dhclient.conf`:** DHCP client configuration.
- **`dhcpd.conf`:** DHCP server configuration.
- **`dhclient-enter-hooks.d/`:** Scripts executed when certain DHCP client events occur (e.g., obtaining a new lease).
- **`dhclient-exit-hooks.d/`:** Scripts executed when the DHCP client exits or releases a lease.

Example `dhcpd.conf`:

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

Example `dhclient.conf`:

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
This file exists in default Debian and Ubuntu installations.

It configures **`dhcpcd`**, a common DHCP client for Linux systems, defining how the service manages network interfaces and DHCP operations.

Example content:

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
- **Debian:** This folder exists in default installations.  
- **Ubuntu:** This folder does **not** exist in default installations.

It contains configuration files and symbolic links related to system-wide dictionary settings, used by spell checkers, word processors, text editors, and other applications.

Key files:

- **`words`:** Master list of valid words for spell-checking.
- **`ispell-default`:** Specifies the default dictionary for the Ispell spell-checking utility.
- **`default.aff`:** Provides essential language rules and affix definitions for spell-checking.

 
<br>
</details>



<details markdown='1'>
<summary>
/etc/dkms/ Folder
</summary>

---
This folder does **not** exist in default Debian or Ubuntu installations.

It contains configuration files for the **Dynamic Kernel Module Support (DKMS)** framework, which manages and recompiles out-of-tree kernel modules when the Linux kernel is upgraded.

The folder contains subdirectories named after DKMS-managed kernel modules.  
Each module directory holds configuration files specifying how the module should be built and installed for different kernel versions.

DKMS allows multiple versions of kernel modules to be managed simultaneously, with configuration files in `/etc/dkms/` determining how different module and kernel versions are handled.

<br>
</details>

<details markdown='1'>
<summary>
/etc/dovecot/ Folder
</summary>

---
This folder does **not** exist in default Debian or Ubuntu installations.  
It is created after installing the **Dovecot** package.

It contains configuration files and directories for the Dovecot IMAP and POP3 server.

Key files and folders:

- **`dovecot.conf`:** Main configuration file; includes other configuration files from `conf.d/` and other directories.
- **`dovecot-*.ext`:** Additional configuration files for specific Dovecot features.
- **`conf.d/`:** Additional configuration files for authentication, logging, protocol settings, etc.
- **`private/`:** Contains SSL certificates (or links to them) used by Dovecot.
- **`sieve/`:** Contains Sieve scripts for filtering and processing incoming email.

<br>
</details>

<details markdown='1'>
<summary>
/etc/dpkg
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files for **dpkg**, the low-level package management system.

Key files and folders:

- **`dpkg.cfg`:** Contains global configuration options for `dpkg` operations.
- **`dpkg.cfg.d/`:** Additional configuration snippets included in the main `dpkg.cfg`.
- **`origins/`:** Files describing package origins (distribution, repository, vendor) and associated cryptographic signatures.
- **`origins/default`:** Specifies the default origin for packages installed via `dpkg`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/e2scrub.conf
</summary>

---
This file exists in default Debian and Ubuntu installations.

It configures the **`e2scrub`** utility, which checks (but does not repair) all metadata in a mounted ext[234] filesystem if it resides on an LVM logical volume.

Example content:

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
- **Debian:** This folder exists in default installations.  
- **Ubuntu:** This folder does **not** exist in default installations.

It contains system-wide configuration files and directories for the **Emacs** text editor, known for its extensibility and support for various programming languages and modes.

Default Debian installations include a `site-start.d/` subfolder containing one file: `50dictionaries-common.el`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/environment
</summary>

---
This file exists in default Debian and Ubuntu installations.

It belongs to **PAM** (Pluggable Authentication Module) and is used by programs compiled with PAM support—primarily login systems, which then start the user’s shell or environment.

It sets environment variables for programs that are not typically started from a shell.

- **Debian:** Empty by default.
- **Ubuntu:** Contains the `PATH` environment variable.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ethertypes
</summary>

---
This file exists in default Debian and Ubuntu installations.

It lists Ethernet frame types (**EtherType** values), which identify the protocol encapsulated in an Ethernet frame.

It is used by tools like **tcpdump** or **Wireshark** to display EtherType values in human-readable format when analyzing network traffic.

Example content:

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
This folder does **not** exist in default Debian or Ubuntu installations.

It contains the **NFS server export table**—a list of local file systems accessible to NFS clients.

Example `exports` file:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **font system**. Even server editions may include it due to dependencies or for console/application font rendering.

Key files and folders:

- **`fonts.conf`:** Main configuration file defining font locations, default settings, and general parameters. Not intended for direct modification.
- **`local.conf`:** For local customizations without altering the main configuration.
- **`conf.d/`:** Additional configuration files included by `fonts.conf`.
- **`conf.avail/`:** Available configuration snippets that can be enabled by creating symbolic links in `conf.d/`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/fstab
</summary>

---
This file exists in default Debian and Ubuntu installations.

It defines how file systems are mounted and configured during system startup.

Example:

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
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It contains configuration for **FUSE** (Filesystem in Userspace), which allows userspace programs to export virtual filesystems to the Linux kernel.

FUSE provides a secure method for non-privileged users to create and mount their own filesystem implementations.

Example content:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration for **fwupd** (Firmware Update Daemon), a service that provides a standardized way to update firmware on Linux systems.

Key files and folders:

- **`daemon.conf`:** Global configuration options for the fwupd service.
- **`lvfs.conf`:** Configuration for the LVFS (Linux Vendor Firmware Service).
- **`vendor.conf`:** Firmware update settings for specific hardware vendors.
- **`remotes.d/`:** Configuration files for remote repositories providing firmware updates.


<br>
</details>

<details markdown='1'>
<summary>
/etc/gai.conf
</summary>

---
This file exists in default Debian and Ubuntu installations.

It contains configuration settings for the **`getaddrinfo`** system call, which performs hostname resolution and translates hostnames or service names into network addresses.

Network applications use `getaddrinfo` to determine IP addresses associated with domain names.

Both Debian and Ubuntu versions are fully commented by default.

<br>
</details>



<details markdown='1'>
<summary>
/etc/gnutls/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **GnuTLS** library, widely used for handling secure network protocols and part of the GNU project.

Default Ubuntu installations include one file, `config`, with the following content:

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
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and resources for the **GNU troff (groff)** typesetting system, which formats plain text into printable documents (e.g., technical documentation and manuals).

Debian and Ubuntu installations include two files: `man.local` and `mdoc.local`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/group and /etc/group-
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/group`:** Contains information about user groups on the system, used for managing group permissions and access control.
- **`/etc/group-`:** Contains the previous state of `/etc/group` for backup purposes.

Example `/etc/group` content:

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
This folder exists in default Debian and Ubuntu installations.

It contains scripts used during the generation of the **GRUB configuration file** (`grub.cfg`), which determines how the system boots and what options appear in the boot menu.

Scripts are typically numbered to specify the order of execution.  
After modifying scripts in `/etc/grub.d/`, run `grub-mkconfig` to regenerate `grub.cfg`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/gshadow and /etc/gshadow-
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/gshadow`:** Contains encrypted passwords for user groups. Readable only by the root user to prevent unauthorized access to password hashes.
- **`/etc/gshadow-`:** Contains the previous state of `/etc/gshadow` for backup.

<br>
</details>

<details markdown='1'>
<summary>
/etc/gss/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration settings for the **Generic Security Services (GSS) daemon**.  
The GSS API provides a uniform mechanism for applications to access security services (e.g., authentication) in distributed systems, independent of the underlying security mechanisms.

Default Debian and Ubuntu installations include an empty subfolder named `mech.d`.

<br>
</details>


<details markdown='1'>
<summary>
/etc/hdparm.conf
</summary>

---
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It contains configurations for the **`hdparm`** utility, a command-line tool for configuring and managing hard disk drives.  
The file allows users to set default parameters for hard drives.


<br>
</details>

<details markdown='1'>
<summary>
/etc/host.conf
</summary>

---
This file exists in default Debian and Ubuntu installations.

It configures the lookup order of hostname resolution methods, specifying how the system resolves hostnames into IP addresses.  
The system's DNS resolver library reads this file.

Example content:

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
This file exists in default Debian and Ubuntu installations.

It contains the system’s **hostname**—a unique identifier used on the network.  
The file consists of a single line with the hostname, which is set during boot or when network configuration is applied.

<br>
</details>

<details markdown='1'>
<summary>
/etc/hosts
</summary>

---
This file exists in default Debian and Ubuntu installations.

It maps hostnames to IP addresses locally, allowing hostname resolution without querying DNS servers. Useful for local network configurations and troubleshooting.

Example content:

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
These files exist in default Debian and Ubuntu installations.

They configure access control for network services using **TCP wrappers**:

- **`hosts.allow`:** Specifies which hosts are allowed to access network services.
- **`hosts.deny`:** Specifies which hosts are denied access unless explicitly allowed in `hosts.allow`.

**Evaluation order:**
1. If allowed in `hosts.allow`, access is granted.
2. If denied in `hosts.deny`, access is denied.
3. If neither file specifies a rule, access is allowed by default.

Example files:

**`/etc/hosts.allow`:**

```
# /etc/hosts.allow

# Allow SSH access from the local network
sshd: 192.168.1.0/255.255.255.0

# Allow FTP access from a specific IP address
vsftpd: 203.0.113.10

# Allow all services from localhost
ALL: 127.0.0.1
```

**`/etc/hosts.deny`:**

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
This folder exists in default Debian and Ubuntu installations.

It contains system startup scripts for the **System V init system**.  
Although both Debian and Ubuntu use **systemd** as their init system, this folder remains as a compatibility layer.

The scripts are used if the init system is switched to System V.


<br>
</details>

<details markdown='1'>
<summary>
/etc/initramfs-tools/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and scripts for generating the **initial RAM filesystem (initramfs)**.  
Initramfs is a temporary filesystem loaded into memory during boot, containing essential tools, modules, and scripts needed to initialize hardware and mount the root filesystem.

Key files and folders:

- **`initramfs.conf`:** Global configuration options for initramfs generation.
- **`modules`:** List of kernel modules to include in initramfs.
- **`update-initramfs.conf`:** Configuration for the `update-initramfs` utility.
- **`conf.d/`:** Additional configuration files that override settings in `initramfs.conf`.
- **`hooks/`:** Shell scripts executed during initramfs generation (e.g., adding custom files, configuring network interfaces, including kernel modules).
- **`scripts/`:** Shell scripts called from hooks or other scripts during initramfs generation (not executed automatically).

<br>
</details>

<details markdown='1'>
<summary>
/etc/inputrc
</summary>

---
This file exists in default Debian and Ubuntu installations.

It contains configuration settings for **Readline**, a library providing command-line editing for programs like Bash, Python, and MySQL.

Excerpt:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **iproute2** suite, used for managing networking aspects such as routing, traffic control, and network interfaces.

Key files:

- **`rt_tables`:** Defines additional routing tables for policy-based routing.
- **`rt_realms`:** Defines realms for policy-based routing.
- **`rt_dsfield`:** Definitions for Differentiated Services Field (DSField) values used in QoS and packet marking.
- **`rt_protos`:** Protocol identifiers for routing tables and cache entries.
- **`rt_scopes`:** Scope values for routing table entries.
- **`rt_tos`:** Type of Service (ToS) values for QoS and packet marking.
- **`rt_mark`:** Route marks for policy-based routing.

<br>
</details>

<details markdown='1'>
<summary>
/etc/iscsi/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **iSCSI** (Internet Small Computer System Interface) protocol, which transmits SCSI commands over IP networks for remote storage access.

Key files:

- **`initiatorname.iscsi`:** Contains the iSCSI initiator name that uniquely identifies the system on the network.
- **`iscsid.conf`:** Configuration for the `iscsid` daemon, which manages iSCSI connections.

<br>
</details>

<details markdown='1'>
<summary>
/etc/issue and /etc/issue.net
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/issue`:** Displays a pre-login message on local physical terminals (virtual consoles) before the login prompt.
- **`/etc/issue.net`:** Displays a pre-login message for remote users connecting via network services like SSH.  
  If `issue.net` is absent, `issue` is used for remote connections as well.

Example contents:

**Debian 13 `/etc/issue`:**

```
Debian GNU/Linux 13 \n \l
```

**Debian 13 `/etc/issue.net`:**

```
Debian GNU/Linux 13 
```

**Ubuntu 24.04 `/etc/issue`:**

```
Ubuntu 24.04 LTS \n \l
```

**Ubuntu 24.04 `/etc/issue.net`:**

```
Ubuntu 24.04 LTS 
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/kernel/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files related to kernel image and module management.

Default installations include four subfolders:

- **`install.d/`:** Scripts executed when a new kernel package is installed.
- **`preinst.d/`:** Scripts executed before a kernel package is installed or upgraded.
- **`postinst.d/`:** Scripts executed after a kernel package is installed or upgraded.
- **`postrm.d/`:** Scripts executed after a kernel package is removed.

<br>
</details>

<details markdown='1'>
<summary>
/etc/kernel-img.conf
</summary>

---
- **Debian:** This file exists in default installations.  
- **Ubuntu:** This file does **not** exist in default installations.

It is used during kernel package installation and removal to specify local options for handling kernel image packages.

Example content:

```
# Kernel image management overrides
# See kernel-img.conf(5) for details
do_symlinks = yes
do_bootloader = no
do_initrd = yes
link_in_boot = no
```

- **`do_symlinks`:** Whether to create symbolic links for kernel image files.
- **`do_bootloader`:** Whether to update bootloader configuration automatically.
- **`do_initrd`:** Whether to generate an initial RAM disk (initrd).
- **`link_in_boot`:** Whether to create symbolic links in `/boot`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/landscape/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists but is empty in default installations.

It contains configuration files for **Landscape**, a management tool for monitoring, managing, and updating multiple Ubuntu systems from a centralized interface.

Key features include system monitoring, software management, inventory management, security compliance, automation, multi-cloud support, and user authentication.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ld.so.conf, /etc/ld.so.conf.d Folder and /etc/ld.so.cache
</summary>

---
These files and folders exist in default Debian and Ubuntu installations.

- **`/etc/ld.so.conf`:** Configuration file for the dynamic linker/loader (`ld`). It specifies directories to search for shared libraries when executables run.
- **`/etc/ld.so.conf.d/`:** Additional configuration files included by `ld.so.conf`.
- **`/etc/ld.so.cache`:** Cache built from the configuration files for faster library lookup.

After modifying `ld.so.conf` or files in `ld.so.conf.d`, run `sudo ldconfig` to rebuild the cache.

<br>
</details>



<details markdown='1'>
<summary>
/etc/ldap/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **OpenLDAP** server and client utilities.  
OpenLDAP is an open-source implementation of the Lightweight Directory Access Protocol (LDAP), used for accessing and managing directory services.

Default Ubuntu includes only `ldap.conf`:

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

Key files and folders:

- **`ldap.conf`:** Global configuration for LDAP client utilities (`ldapsearch`, `ldapmodify`, etc.).
- **`slapd.conf`:** Main configuration for the OpenLDAP server (`slapd`), including database backend, access control, schema definitions, and logging.
- **`ldap.conf.d/`:** Additional configuration files included by `ldap.conf`.
- **`slapd.d/`:** Additional configuration files included by `slapd.conf`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/legal
</summary>

---
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It contains legal notices.

Default content:

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
This file exists in default Debian and Ubuntu installations.

It contains configuration for user-space applications linking to **libaudit**, a library that interacts with the Linux Audit framework for comprehensive system event logging and monitoring.

Example content:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **libblockdev** library, which provides a standardized, abstracted interface for managing block devices on Linux systems.  
Applications can use it to programmatically handle block devices without dealing with low-level storage details.

Example configuration (`/etc/libblockdevconf.d/00-default.cfg`):

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **libibverbs** library, a key component of the software stack for **Remote Direct Memory Access (RDMA)** technologies.  
RDMA enables high-performance, low-latency data transfers, commonly used in data centers, high-performance computing, and storage systems.

<br>
</details>


<details markdown='1'>
<summary>
/etc/libnl-3/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **libnl** (Network Link library), which provides an API for low-level communication with the kernel's networking stack.  
Applications use libnl to interact with network interfaces, routing tables, and other networking features.

Key files:

- **`classid`:** ClassID-to-name translation table.
- **`pktloc`:** Location definitions for packet matching.

<br>
</details>

<details markdown='1'>
<summary>
/etc/locale.alias and /etc/locale.gen
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/locale.alias`:** Contains alias definitions for locale names, mapping alternative names to canonical locale names.  
  Each line specifies an alias followed by the corresponding canonical locale name.

- **`/etc/locale.gen`:** Lists locale definitions to be generated or compiled on the system.  
  Each line defines a locale name and optional character encoding.  
  Uncomment a line to enable that locale, then run `locale-gen` to generate it.

Example excerpt from `/etc/locale.alias`:

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

Example excerpt from `/etc/locale.gen`:

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
This file exists in default Debian and Ubuntu installations.

It defines system-wide **locale settings**, which determine language, regional formats, and internationalization aspects of the operating system. These settings affect how dates, times, numbers, currencies, and other region-specific information are presented.

Example content:

```
LANG=en_US.UTF-8
LC_TIME=en_GB.UTF-8
LC_NUMERIC=de_DE.UTF-8
```

- **`LANG`:** Sets the default language and encoding for the system (primary locale setting).
- **`LC_*`:** Overrides specific locale categories (e.g., `LC_TIME` for time/date formats, `LC_NUMERIC` for numeric formats). If unspecified, they default to the `LANG` value.


<br>
</details>

<details markdown='1'>
<summary>
/etc/localtime
</summary>

---
This file exists in default Debian and Ubuntu installations.

It is a symbolic link or copy of the timezone data file used by the system’s C library to determine the local timezone.

It points to a timezone data file in `/usr/share/zoneinfo/`, which contains data for various regions and time zones worldwide.

<br>
</details>

<details markdown='1'>
<summary>
/etc/logcheck
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **Logcheck**, a log monitoring and analysis tool that scans system log files for suspicious or unusual activity and generates reports or alerts based on predefined rules.

Key files and folders:

- **`logcheck.conf`:** Global configuration settings (e.g., email recipient for reports, log directories to monitor, verbosity level).
- **`logcheck.logfiles`:** Lists log files to monitor.
- **`ignore.d.server/`:** Contains rules for ignoring certain log messages from specific services or applications.

<br>
</details>

<details markdown='1'>
<summary>
/etc/login.defs
</summary>

---
This file exists in default Debian and Ubuntu installations.

It provides default configuration for several user account parameters.  
Commands like `useradd`, `usermod`, `userdel`, and `groupadd` use values from this file.

Each line contains a directive name and its associated value, allowing system administrators to customize the login service’s default behavior according to security and operational needs.

Example excerpt:


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
These exist in default Debian and Ubuntu installations.

- **`/etc/logrotate.conf`:** Main configuration file for the **Logrotate** utility, which manages log file rotation and compression to prevent excessive disk usage.
- **`/etc/logrotate.d/`:** Contains additional configuration files for individual log files or sets.

Changes to `logrotate.conf` typically take effect immediately, with log rotation occurring according to the specified frequency and criteria.

Example `logrotate.conf`:

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
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It is a standard configuration file for systems adhering to the **Linux Standard Base (LSB)**.  
It provides distribution release, version, and other details in a standardized format, allowing applications and scripts to identify the Linux distribution and its characteristics.

Example content (Ubuntu):

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files and metadata for the **Logical Volume Manager (LVM)**, a disk management tool that allows administrators to create logical volumes from physical volumes for flexible and scalable storage management.

Key files and folders:

- **`lvm.conf`:** Main configuration file for LVM, controlling the behavior of LVM tools and daemons.
- **`lvmlocal.conf`:** Used for local customization of LVM settings.
- **`profiles/`:** Contains configuration files for LVM profiles.

<br>
</details>

<details markdown='1'>
<summary>
/etc/machine-id
</summary>

---
This file exists in default Debian and Ubuntu installations.

It contains the **unique machine ID** of the local system, set during installation or boot.  
The ID is a 32-character lowercase hexadecimal string (16 bytes/128 bits) terminated by a newline, and it must not be all zeros.

Example content:

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
These files exist in default Debian and Ubuntu installations.

- **`/etc/magic`:** Contains a database of "magic" numbers or patterns used to identify file types by examining their contents. Each entry describes a file type and includes rules or patterns matched against the beginning of the file.
- **`/etc/magic.mime`:** Similar to `/etc/magic` but specifically used for **MIME type detection**. It contains MIME type definitions and file format signatures used by utilities to determine the appropriate MIME type based on file contents.

System administrators or package managers may update or customize these files to add support for new file types and MIME types.

Example contents:

**`/etc/magic`:**

```
# /etc/magic
# Offset    Data type      Byte sequence    File type
# Example rule: Identify JPEG files
0      string     \xFF\xD8\xFF\xE0\x00\x10    JPEG image data
#
# Example rule: Identify PNG files
0      string     \x89\x50\x4E\x47\x0D\x0A\x1A\x0A    PNG image data
```

**`/etc/magic.mime`:**

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
These files do **not** exist in default Debian or Ubuntu installations.

- **`/etc/mailcap`:** Used by email clients and other applications to map MIME types to commands for displaying or handling files. It specifies which applications should be used for different file types.
- **`/etc/mailcap.order`:** Specifies the order in which entries from `/etc/mailcap` are processed when multiple entries match a given MIME type. Administrators can control the precedence of MIME type handlers.

Example `mailcap` content:

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

Example `mailcap.order` content:

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
This file exists in default Debian and Ubuntu installations.

It configures the system-wide manual page paths for the `man` command, defining the search paths used to locate and display manual pages.

Example content:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It is used by **mdadm** (multiple devices admin) for managing software RAID arrays, containing configuration files, metadata, and state information.

Key files and folders:

- **`array.state`:** Current state of RAID arrays managed by mdadm.
- **`conf.cache`:** Cache of RAID device metadata to improve performance by reducing metadata scans during initialization.
- **`mdadm.conf`:** Main configuration file for mdadm, containing settings and metadata for RAID arrays (device paths, RAID levels, etc.).
- **`mdadm.pid`:** Process ID (PID) of the running mdadm instance to prevent multiple instances and data corruption.
- **`mdadm.conf.d/`:** Additional configuration files included by `mdadm.conf` for custom RAID configuration snippets.


<br>
</details>

<details markdown='1'>
<summary>
/etc/mime.types
</summary>

---
This file exists in default Debian and Ubuntu installations.

It maps filename extensions to **MIME types**, allowing applications to determine the appropriate MIME type for a file based on its extension.

Example content:

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
This file exists in default Debian and Ubuntu installations.

It configures the **mke2fs** utility, controlling default parameters when creating ext2, ext3, or ext4 filesystems.

Example content:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **ModemManager** service, which manages mobile broadband (3G/4G/LTE) and other modem devices.

Default Ubuntu installations include two empty subfolders: `connection.d/` and `fcc-unlock.d/`.


<br>
</details>

<details markdown='1'>
<summary>
/etc/modprobe.d/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It configures the behavior of the **modprobe** command and the Linux kernel module loading process. Administrators can specify options, aliases, and other settings for individual kernel modules or for `modprobe` itself.

Example files:

**`/etc/modprobe.d/intel-microcode-blacklist.conf`:**

```
# /etc/modprobe.d/intel-microcode-blacklist.conf
#
# The microcode module attempts to apply a microcode update when
# it autoloads.  This is not always safe, so we block it by default.
blacklist microcode
```

**`/etc/modprobe.d/blacklist.conf`:**

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

**`/etc/modprobe.d/mdadm.conf`:**

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
These exist in default Debian and Ubuntu installations.

- **`/etc/modules`:** Specifies a list of kernel modules to be automatically loaded at boot. Each line corresponds to one module.

- **`/etc/modules-load.d/`:** Used by **systemd**; contains a symbolic link to `/etc/modules` as a compatibility layer.

Example `/etc/modules` content:

```
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
loop
lp
snd-usb-audio
```

<br>
</details>

<details markdown='1'>
<summary>
/etc/motd
</summary>

---
- **Debian:** This file exists in default installations.  
- **Ubuntu:** This file does **not** exist in default installations.

It contains a **Message of the Day (MOTD)** displayed to users upon login, often used for announcements, system status updates, or other important messages.

<br>
</details>

<details markdown='1'>
<summary>
/etc/mtab
</summary>

---
This file exists in default Debian and Ubuntu installations.

It is a symbolic link to `/proc/self/mounts` and provides real-time information about currently mounted filesystems.

<br>
</details>

<details markdown='1'>
<summary>
/etc/multipath.conf and /etc/multipath/ Folder
</summary>

---
- **Debian:** These do **not** exist in default installations.  
- **Ubuntu:** These exist in default installations.

They configure the **multipath daemon (`multipathd`)** and the `multipath` command-line utility for storage device redundancy and load balancing (e.g., via Fibre Channel, iSCSI, or SCSI).

Example `/etc/multipath.conf`:

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
This folder does **not** exist in default Debian or Ubuntu installations.  
It is created after installing `mysql-server` or `mariadb-server`.

It contains configuration files for **MySQL** and/or **MariaDB**.

Key files and folders:

- **`debian.cnf`:** Contains authentication credentials for MySQL utilities provided by the Debian packaging system. *Note: This file is obsolete and will be removed in future releases.*
- **`debian-start`:** Script run by the Debian packaging system when the MySQL/MariaDB server starts or restarts.
- **`mariadb.cnf`:** Additional configuration settings specific to MariaDB.
- **`my.cnf`:** Main configuration file for MySQL (global settings).
- **`my.cnf.fallback`:** Fallback configuration used if `my.cnf` is missing or unreadable.
- **`conf.d/`:** Additional configuration files included by `my.cnf` (and `mariadb.cnf`).
- **`mariadb.conf.d/`:** Additional configuration files included by `mariadb.cnf` (and `my.cnf`).


<br>
</details>

<details markdown='1'>
<summary>
/etc/nanorc
</summary>

---
This file exists in default Debian and Ubuntu installations.

It is the configuration (initialization) file for the **nano** text editor.

Excerpt:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **Needrestart** tool, which identifies running processes that need to be restarted after library or kernel updates to ensure changes take effect.

Key files and folders:

- **`needrestart.conf`:** Main configuration file (uses Perl syntax).
- **`notify.conf`:** Configures how Needrestart notifies users about processes requiring restart (e.g., email, syslog).
- **`iucode.sh`:** Checks whether CPU microcode needs updating (microcode updates address security vulnerabilities or improve performance).
- **`conf.d/`:** Additional configuration files for specific aspects of Needrestart's behavior.
- **`hook.d/`:** Scripts (hooks) executed at different stages of Needrestart's operation.
- **`notify.d/`:** Scripts or configuration files for notifying users/administrators about services needing restart.
- **`restart.d/`:** Configuration files defining conditions under which services or processes should be restarted.

<br>
</details>



<details markdown='1'>
<summary>
/etc/netconfig
</summary>

---
This file exists in default Debian and Ubuntu installations.

It defines a list of transport names describing their semantics and protocols.  
Currently, it is used only in conjunction with the TI-RPC code in the `libtirpc` library.

Example content:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains **Netplan** network configuration files.  
Netplan is a utility developed by Canonical for configuring network interfaces on Ubuntu.

Example configuration (`/etc/netplan/00-installer-config.yaml`):
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
This folder exists in default Debian and Ubuntu installations.

It contains network configuration files for Debian-based systems.

Key files and folders:

- **`interfaces`:** Main configuration file defining network interfaces, IP addresses, gateways, and other settings.
- **`interfaces.d/`:** Additional configuration files that can be included from the main `interfaces` file for modular organization.
- **`if-*.d/` directories:** Scripts executed during network interface state changes:
  - `if-down.d/`: When interfaces go down.
  - `if-post-down.d/`: After interfaces go down.
  - `if-pre-up.d/`: Before interfaces come up.
  - `if-up.d/`: After interfaces come up.

Example files:

**`/etc/network/interfaces.d/enp0s3`:**

```
# /etc/network/interfaces.d/enp0s3
auto enp0s3
iface enp0s3 inet static
  address 192.168.1.196/24
  broadcast 192.168.1.255
  network 192.168.1.0
  gateway 192.168.1.1
```

**`/etc/network/if-up.d/routes`:**

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **networkd-dispatcher** daemon, which works with `systemd-networkd` to handle network interface events.

Default Ubuntu installations include six empty subfolders:

- **`carrier.d/`:** Scripts executed when a network interface's carrier state changes (up/down).
- **`degraded.d/`:** Scripts executed when the network is in a degraded state.
- **`dormant.d/`:** Scripts executed when a network interface enters a dormant (deactivated) state.
- **`no-carrier.d/`:** Scripts executed when network interfaces lose carrier (go offline).
- **`off.d/`:** Scripts executed when a network interface is brought down or deactivated.
- **`routable.d/`:** Scripts executed when a network interface becomes routable (has an assigned IP address and can communicate).

<br>
</details>

<details markdown='1'>
<summary>
/etc/networks
</summary>

---
This file exists in default Debian and Ubuntu installations.

It is a simple text-based configuration file mapping network names to corresponding IP network addresses.  
Used by network-related utilities (e.g., `route`) to resolve network names to IP addresses when displaying routing information.

Example content:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **Newt** library, used for creating text-based user interfaces (TUI) in applications (e.g., installation programs, system configuration utilities).

Example configuration (`/etc/newt/palette.ubuntu`):

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
This file exists in default Debian and Ubuntu installations.

It configures the **nftables** firewall framework, a modern and flexible replacement for iptables for packet filtering and classification in the Linux kernel.

Example content (default Debian configuration):

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
This folder does **not** exist in default Debian or Ubuntu installations.  
It is created after installing the **nginx** package.

It contains configuration files and directories for the **Nginx** web server, known for its high performance, stability, and scalability.

Key files and folders:

- **`nginx.conf`:** Main configuration file for Nginx (global settings).
- **`fastcgi_params` & `scgi_params`:** Default configuration settings for FastCGI and SCGI, respectively.
- **`koi-utf` & `koi-win`:** Character conversion mappings for KOI8-U and KOI8-R character sets.
- **`mime.types`:** Mappings of file extensions to MIME types (determines the `Content-Type` HTTP header).
- **`conf.d/`:** Additional configuration files included by `nginx.conf` for modular configuration.
- **`modules-available/` & `modules-enabled/`:** Configuration files for Nginx modules. Enable modules by creating symbolic links from `modules-available/` to `modules-enabled/`.
- **`sites-available/` & `sites-enabled/`:** Configuration files for Nginx server blocks (virtual hosts). Enable virtual hosts by creating symbolic links from `sites-available/` to `sites-enabled/`.
- **`snippets/`:** Reusable configuration snippets to avoid duplication and simplify management.


<br>
</details>

<details markdown='1'>
<summary>
/etc/nsswitch.conf
</summary>

---
This file exists in default Debian and Ubuntu installations.

It configures the **Name Service Switch (NSS)** system, defining sources and their order for various system databases and services (e.g., user authentication, group membership, hostname resolution).

Example content:

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

**Explanation:**

- **`passwd`**, **`group`**, **`shadow`:** User account information, group membership, and password hashes. `files` indicates local files (`/etc/passwd`, `/etc/group`, `/etc/shadow`); `systemd` indicates consultation with systemd.
- **`hosts`:** Hostname resolution. `files` consults `/etc/hosts` first, then `dns` performs DNS resolution.
- **`networks`**, **`protocols`**, **`services`**, **`ethers`**, **`rpc`:** Network-related information. `db` indicates system databases (`/etc/networks`, `/etc/protocols`, etc.), followed by local `files`.
- **`netgroup`:** Network group information using the Network Information Service (`nis`) as the source.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ntp.conf
</summary>

---
This file does **not** exist in default Debian or Ubuntu installations.

It configures the **Network Time Protocol (NTP)** daemon, which synchronizes computer clocks over a network.

Example content:

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
This folder exists (and is empty) in default Debian and Ubuntu installations.

It is intended to store **global configuration files** for applications installed in `/opt/`.

While software in `/opt/` typically keeps its configuration within its own directory structure, `/etc/opt/` provides a standardized location for system-wide configuration files affecting multiple packages or requiring separation from software-specific files.

<br>
</details>

<details markdown='1'>
<summary>
/etc/os-release
</summary>

---
This file exists in default Debian and Ubuntu installations.

It is a symbolic link to `/usr/lib/os-release` and contains operating system identification data.

**Debian 13 example:**

```
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.1
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

**Ubuntu 24.04 example:**

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

- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists but is **disabled** by default.

It is used with systems that employ **overlay file systems**, commonly in LiveCDs, embedded systems, or diskless workstations, to keep the root filesystem read-only by overlaying a temporary writable filesystem on top.

<br>
</details>



<details markdown='1'>
<summary>
/etc/pam.conf and /etc/pam.d/ Folder
</summary>

---
These exist in default Debian and Ubuntu installations.

- **`/etc/pam.conf`:** Used only if `/etc/pam.d/` does not exist (for backward compatibility).
- **`/etc/pam.d/`:** Contains configuration files for the **Pluggable Authentication Modules (PAM)** framework, which provides flexible user authentication and authorization.

Key files in `/etc/pam.d/`:

- **`common-*`:** Shared PAM configurations included by service-specific files.
- **`login`:** Configuration for the login service.
- **`su`:** Configuration for the `su` command.
- **`sudo`:** Configuration for the `sudo` command.
- **`other`:** Default configuration for services without a specific file.


<br>
</details>

<details markdown='1'>
<summary>
/etc/passwd & /etc/passwd-
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/passwd`:** Stores user account information (one of the most essential system files).
- **`/etc/passwd-`:** Backup of the previous state of `/etc/passwd`.

Example `/etc/passwd` content:

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
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and directories for the **Perl** programming language, used to configure Perl itself and manage system-wide Perl modules.

Key contents:

- **`Errno.pm`:** Error code definitions used by Perl.
- **`CPAN/`:** Configuration files for the CPAN (Comprehensive Perl Archive Network) module installer (e.g., `Config.pm`).
- **`Net/`:** Configuration files for the Net module (e.g., `Config.pm`).

<br>
</details>

<details markdown='1'>
<summary>
/etc/php/ Folder
</summary>

---
This folder does **not** exist in default Debian or Ubuntu installations.  
It is created after installing a **PHP** package.

It contains configuration files and directories for PHP, a widely used server-side scripting language for web development.

Subfolders are named after PHP versions (e.g., `7.4/`, `8.2/`).  
Each version folder typically includes:

- **`apache2/`:** Configuration for PHP running as an Apache module.
- **`cli/`:** Configuration for the PHP command-line interface.
- **`mods-available/`:** Configuration files for specific PHP modules or extensions.

<br>
</details>

<details markdown='1'>
<summary>
/etc/pki/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains certificates (`fwupd/` subfolder) and metadata (`fwupd-metadata/` subfolder) used by **fwupd** (Firmware Update Daemon), a utility for managing firmware updates on Linux systems.

<br>
</details>

<details markdown='1'>
<summary>
/etc/plymouth/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists but is empty in default installations.

It is intended to contain configuration files, themes, and scripts for **Plymouth**, a boot splash screen system that provides a polished and visually consistent user experience during system startup/shutdown (common in Ubuntu, Fedora, etc.).

<br>
</details>

<details markdown='1'>
<summary>
/etc/pm/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files and scripts for **power management**.

Key subfolders:

- **`config.d/`:** Global power management settings (e.g., suspend, hibernate, screen dimming).
- **`power.d/`:** Scripts executed during power state transitions (e.g., entering/exiting suspend).
- **`sleep.d/`:** Scripts specifically executed during sleep transitions (suspend, hibernate, resume).

<br>
</details>

<details markdown='1'>
<summary>
/etc/polkit-1/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **PolicyKit**, a component for defining and enforcing fine-grained access control policies (e.g., mounting drives, changing system settings, administrative tasks).

<br>
</details>

<details markdown='1'>
<summary>
/etc/pollinate/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files and scripts for the **pollinate** utility, which gathers entropy (randomness) from external sources to improve the Linux kernel’s random number generator for cryptographic operations and security-sensitive processes.

<br>
</details>

<details markdown='1'>
<summary>
/etc/popularity-contest.conf
</summary>

---
- **Debian:** This file exists in default installations.  
- **Ubuntu:** This file does **not** exist in default installations.

It configures the **Popularity Contest** package for Debian, which collects anonymous data about the most used Debian packages to help developers prioritize maintenance.

Example content:

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
This folder does **not** exist in default Debian or Ubuntu installations.  
It is created after installing the **postfix** package.

It contains configuration files for **Postfix**, a popular open-source mail transfer agent (MTA) known for its security, performance, and ease of configuration.

Key files and folders:

- **`main.cf`:** Main configuration file (defines Postfix operation: hostname, domain, network interfaces, relay host, SMTP client options, etc.).
- **`master.cf`:** Master configuration file (defines mail transport services and their parameters).
- **`sasl/`:** Configuration for integrating Postfix with the Cyrus SASL (Simple Authentication and Security Layer) library (SMTP authentication mechanisms).
- **`postfix-files.d/`:** Miscellaneous configuration files and support scripts.

<br>
</details>




<details markdown='1'>
<summary>
/etc/profile & /etc/profile.d/ Folder
</summary>

---
These exist in default Debian and Ubuntu installations.

- **`/etc/profile`:** A system-wide configuration file that sets environment variables and initializes settings for Bourne shell and compatible shells (sh, bash, ksh, ash).
- **`/etc/profile.d/`:** Contains shell scripts automatically sourced by `/etc/profile`.

Example `/etc/profile` content:

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
This file exists in default Debian and Ubuntu installations.

It lists network protocols and their associated protocol numbers, mapping protocol names to numbers (with optional aliases).  
Used by networking utilities and applications for protocol identification.

Example content:

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
These folders exist in default Debian and Ubuntu installations.

- **`/etc/python3/`:** Contains `debian_config`, which holds Debian-specific packaging settings for Python.
- **`/etc/python3.*/`** (e.g., `python3.11/`, `python3.13/`): Contains `sitecustomize.py`, a script automatically imported during Python interpreter initialization to allow site-level customization.

Example files:

**`/etc/python3/debian_config`:**
```
[DEFAULT]
# how to byte-compile (comma separated: standard, optimize)
byte-compile = standard
```

**`/etc/python3.13/sitecustomize.py`:**

```
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
These folders exist in default Debian and Ubuntu installations.

Although both distributions use **systemd** as their init system, these folders are retained as a compatibility layer for **System V init**.  
They contain scripts that would be used if the init system were switched to System V, corresponding to different runlevels (e.g., `rc0.d/`, `rc1.d/`, etc.).


<br>
</details>

<details markdown='1'>
<summary>
/etc/reportbug.conf
</summary>

---

- **Debian:** This file exists in default installations.  
- **Ubuntu:** This file does **not** exist in default installations.

It configures the **reportbug** tool, which assists users in reporting bugs in Debian packages to the Debian Bug Tracking System (BTS).

Example excerpt:

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
This file exists in default Debian and Ubuntu installations.

It configures **DNS (Domain Name System)** resolver settings, translating domain names into IP addresses for network communication.

**Note:** In Ubuntu, it is a symbolic link to `/run/systemd/resolve/stub-resolv.conf` because Ubuntu uses `systemd-networkd` and `systemd-resolved`.

Example content:

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
This file exists in default Debian and Ubuntu installations.

It is a symbolic link to `/usr/sbin/rmt`, a utility for manipulating tape drives, retained for backward compatibility.

<br>
</details>

<details markdown='1'>
<summary>
/etc/rpc
</summary>

---
This file exists in default Debian and Ubuntu installations.

It defines **Remote Procedure Call (RPC)** program numbers and their associated service names.  
RPC allows programs to execute procedures on remote systems as if they were local.

Example content:

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
- **Debian:** These do **not** exist in default installations.  
- **Ubuntu:** These exist in default installations.

- **`/etc/rsyslog.conf`:** Main configuration file for the **rsyslog** daemon, a syslogd replacement with enhanced features and performance.  
  It handles receiving log messages and forwarding them to destinations (log files, remote servers, etc.).
- **`/etc/rsyslog.d/`:** Additional configuration files included by `rsyslog.conf`.

Excerpt from `/etc/rsyslog.conf`:

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
- **Debian:** This folder exists in default installations.  
- **Ubuntu:** This folder does **not** exist in default installations.

Although Debian uses **systemd** as its init system, this folder is retained as a compatibility layer for **Runit init**.  
Its scripts would be used if the init system were switched to Runit.

<br>
</details>

<details markdown='1'>
<summary>
/etc/screenrc
</summary>

---
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It configures **GNU Screen**, a terminal multiplexer that allows multiple terminal sessions within a single window for easier task management.

<br>
</details>

<details markdown='1'>
<summary>
/etc/security/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and scripts related to system security settings, policies, and authentication mechanisms.

Key files and folders:

- **`access.conf`:** Access control rules based on user, group, and terminal.
- **`capability.conf`:** Linux capabilities settings for fine-grained process privilege control.
- **`faillock.conf`:** Configuration for the `faillock` utility, managing user authentication failure records (e.g., lockouts, delays against brute-force attacks).
- **`group.conf`:** Group-based access control rules.
- **`limits.conf`:** System resource limits for users and processes (CPU time, processes, open files, etc.).
- **`namespace.conf`:** Configuration for process and namespace creation (affects security and resource isolation).
- **`namespace.init`:** Script initializing namespace support on system startup.
- **`opasswd`:** Stores hashed passwords of removed users to prevent reuse.
- **`pam_env.conf`:** Environment variable configuration for user sessions via PAM.
- **`time.conf`:** Time-based access control policies using the `pam_time` module.

<br>
</details>




<details markdown='1'>
<summary>
/etc/selinux/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

Although Debian and Ubuntu do not have **SELinux** enabled by default, this folder (containing `semanage.conf`) is present, likely due to dependency requirements.


<br>
</details>

<details markdown='1'>
<summary>
/etc/sensors3.conf and /etc/sensors.d/ Folder
</summary>

---
- **Debian:** These do **not** exist in default installations.  
- **Ubuntu:** These exist in default installations.

- **`/etc/sensors3.conf`:** Configuration file for the **libsensors** library (part of the `lm_sensors` package for hardware monitoring).
- **`/etc/sensors.d/`:** Additional configuration snippets included by `sensors3.conf`.


<br>
</details>

<details markdown='1'>
<summary>
/etc/services
</summary>

---
This file exists in default Debian and Ubuntu installations.

It maps well-known service names to their corresponding port numbers, used by network services and utilities to identify and communicate with services.

Example excerpt:

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains resources, configurations, and catalog files for **SGML** (Standard Generalized Markup Language), the basis for markup languages like XML and HTML.


<br>
</details>

<details markdown='1'>
<summary>
/etc/shadow & /etc/shadow-
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/shadow`:** Stores encrypted user passwords and related password information for authentication.
- **`/etc/shadow-`:** Backup of the previous state of `/etc/shadow`.

Example `/etc/shadow` content:

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

**Fields (per line):**

1. Username
2. Encrypted password
3. Days since last password change
4. Minimum password age
5. Maximum password age
6. Warning period before password expiration
7. Password inactivity period
8. Account expiration date
9. Reserved field

<br>
</details>

<details markdown='1'>
<summary>
/etc/shells
</summary>

---
This file exists in default Debian and Ubuntu installations.

It lists the available login shells on the system, with each line representing the path to a valid shell executable.  
Used by system utilities and administration tools to determine permissible login shells for user accounts.

Example content:

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
This folder exists in default Debian and Ubuntu installations.

It contains **template files and directories** copied to the home directory of each newly created user.

Default files in Debian/Ubuntu:

- **`.bash_logout`:** Executed when the user logs out (cleanup tasks, session saving).
- **`.bashrc`:** Bash shell configuration (environment variables, aliases, shell settings).
- **`.profile`:** Profile script executed at login (environment variables, commands/scripts).


<br>
</details>

<details markdown='1'>
<summary>
/etc/sos/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **sos report** tool, a command-line utility for collecting diagnostic information for troubleshooting.

Key contents:

- **`sos.conf`:** Main configuration for the `sos` utility.
- **`extras.d/`:** Configuration files for the `sos_extras` plugin.
- **`groups.d/`:** Host group configuration files for `sos collect`.
- **`presets.d/`:** Preset configuration files for `sos report`.

<br>
</details>



<details markdown='1'>
<summary>
/etc/ssh/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and keys for the **SSH (Secure Shell)** service.

Key files and folders:

- **`ssh_config`:** Client-side SSH configuration (applies to all users).
- **`sshd_config`:** Server-side SSH configuration (defines SSH server operation and security features).
- **`ssh_host_*_key` & `ssh_host_*_key.pub`:** Private and public keys for host authentication.
- **`moduli`:** Diffie-Hellman prime numbers for secure key exchange.
- **`ssh_config.d/` & `sshd_config.d/`:** Additional configuration snippets included by `ssh_config` and `sshd_config`, respectively.

Example excerpts:

**`/etc/ssh/ssh_config`:**

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

**`/etc/ssh/sshd_config`:**

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
This folder exists in default Debian and Ubuntu installations.

It contains **SSL/TLS-related configuration files and certificates**.

Key contents:

- **`openssl.cnf`:** OpenSSL configuration file (defines default settings for OpenSSL commands and libraries).
- **`certs/`:** Various SSL/TLS certificates, including Certificate Authority (CA) public keys and self-signed certificates.
- **`private/`:** Private keys used for SSL/TLS encryption.

Excerpt from `/etc/ssl/openssl.cnf`:

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
These files exist in default Debian and Ubuntu installations.

- **`/etc/subgid`:** Specifies **subordinate group IDs (subgids)** for user namespaces, allocating ranges of group IDs to non-root users.
- **`/etc/subgid-`:** Backup of the previous state of `/etc/subgid`.

Each line in `/etc/subgid` follows the format:  
`username:start_id:count`

- **`username`:** User to whom subordinate group IDs are allocated.
- **`start_id`:** Starting ID of the range.
- **`count`:** Number of subordinate group IDs in the range.

<br>
</details>

<details markdown='1'>
<summary>
/etc/subuid & /etc/subuid-
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/subuid`:** Specifies **subordinate user IDs (subuids)** for user namespaces, allocating ranges of user IDs to non-root users.
- **`/etc/subuid-`:** Backup of the previous state of `/etc/subuid`.

Each line in `/etc/subuid` follows the format:  
`username:start_id:count`

- **`username`:** User to whom subordinate user IDs are allocated.
- **`start_id`:** Starting ID of the range.
- **`count`:** Number of subordinate user IDs in the range.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sudo_logsrvd.conf & /etc/sudo.conf
</summary>

---
These files exist in default Debian and Ubuntu installations.

- **`/etc/sudo_logsrvd.conf`:** Configures sudo’s **logsrv daemon**.
- **`/etc/sudo.conf`:** Configures sudo’s behavior (authentication, logging, plugin settings).

Both files are fully commented by default.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sudoers and /etc/sudoers.d/ Folder
</summary>

---
These exist in default Debian and Ubuntu installations.

- **`/etc/sudoers`:** Defines which users or groups can execute commands with elevated privileges using **sudo**.  
  Edited via `visudo` to prevent syntax errors and ensure safe concurrent editing.
- **`/etc/sudoers.d/`:** Contains additional configuration files included by `/etc/sudoers`, allowing modular management of sudo rules without modifying the main file.


<br>
</details>

<details markdown='1'>
<summary>
/etc/supercat/ Folder
</summary>

---

This folder exists in default Debian and Ubuntu installations.

It contains configuration files for **supercat**, a tool that colorizes text based on regular expressions, strings, or characters.

Example configuration (`/etc/supercat/spcrc-crontab`):

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
- **Debian:** This folder exists in default installations.  
- **Ubuntu:** This folder does **not** exist in default installations.

Although Debian uses **systemd** as its init system, this folder is retained as a compatibility layer for **Runit init**.  
Its scripts would be used if the init system were switched to Runit.

<br>
</details>

<details markdown='1'>
<summary>
/etc/sysctl.conf & /etc/sysctl.d/ Folder
</summary>

---
These exist in default Debian and Ubuntu installations.

- **`/etc/sysctl.conf`:** Configures **kernel parameters** in the format `parameter = value`.
- **`/etc/sysctl.d/`:** Additional configuration files included by `sysctl.conf`.

Example `sysctl.conf`:

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

After modifying `sysctl.conf`, apply changes with:  
`sudo sysctl -p`

<br>
</details>

<details markdown='1'>
<summary>
/etc/sysstat/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **sysstat**, a collection of system performance monitoring tools for CPU, memory, disk, network, etc.

Example `/etc/sysstat/sysstat`:

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
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and directories for **systemd** (init system and services).

Key files and folders:

- **`journald.conf`:** Configuration for systemd's journal service (logging, rotation, storage).
- **`logind.conf`:** Configuration for systemd's login manager (user sessions, power management).
- **`resolved.conf`:** Configuration for systemd's DNS resolver (`systemd-resolved`).
- **`system.conf`:** Global systemd settings (resource limits, process priorities, cgroup hierarchy).
- **`timesyncd.conf`:** Configuration for systemd's network time synchronization (`systemd-timesyncd`).
- **`user.conf`:** Systemd configuration for user sessions.
- **`network/`:** Network configuration files for `systemd-networkd`.
- **`system/`:** System-specific unit files (services, sockets, devices, mounts, etc.).
- **`user/`:** User-specific unit files (services managed by systemd for individual users).

<br>
</details>

<details markdown='1'>
<summary>
/etc/terminfo/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

Default installations contain only a `README` file.  
Normally, it holds **terminal capability database files** used by terminal-related applications to define terminal characteristics and capabilities.

<br>
</details>

<details markdown='1'>
<summary>
/etc/thermald/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **Thermal Daemon (thermald)**, which monitors and controls thermal issues to prevent overheating (e.g., by adjusting CPU frequency).

Default Ubuntu installations include only `thermal-cpu-cdev-order.xml`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/timezone
</summary>

---
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It contains the **system timezone name**, used by utilities and applications to determine timezone settings.

Examples:

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
This folder exists in default Debian and Ubuntu installations.

- **Debian:** Empty by default.  
- **Ubuntu:** May contain files.

It holds configurations used by **systemd** to manage temporary files and directories at boot and during runtime (creation, deletion, modification).

<br>

</details>

<details markdown='1'>
<summary>
/etc/ubuntu-advantage/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **Ubuntu Advantage**, Canonical’s commercial support program for Ubuntu.

Example `/etc/ubuntu-advantage/uaclient.conf`:

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
This file exists in default Debian and Ubuntu installations.

It is associated with the **update configuration files (UCF)** utility, which handles configuration file updates during package installation or upgrade in a user-friendly, automated manner.

Example content:

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
This folder exists in default Debian and Ubuntu installations.

It contains configuration files for **udev**, the device manager subsystem that handles device nodes in `/dev` and manages device events (insertion, removal, hot-plugging).

Key files and folders:

- **`udev.conf`:** Global configuration options (logging verbosity, device naming, default behavior).
- **`hwdb.d/`:** Hardware database files for device matching (empty by default).
- **`rules.d/`:** Rule files specifying how udev handles devices and events (empty by default in Debian).

<br>
</details>

<details markdown='1'>
<summary>
/etc/udisks2/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **UDisks 2** service, which provides a standardized interface for managing storage devices (hard disks, SSDs, USB drives, optical drives).

Key files:

- **`udisks2.conf`:** Configuration options for UDisks 2 (device permissions, mount options, storage policies).
- **`mount_options.conf`:** Default mount options for filesystems managed by UDisks 2.

<br>
</details>

<details markdown='1'>
<summary>
/etc/ufw/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files and directories for the **Uncomplicated Firewall (UFW)**, a user-friendly interface for managing netfilter (Linux kernel firewall).

**Debian:** Includes only `applications.d/` by default.

Key files and folders:

- **`ufw.conf`:** Main UFW configuration (default policies, logging, boot enablement).
- **`before.rules` & `after.rules`:** Additional iptables rules applied before/after the main UFW ruleset (IPv4).
- **`before6.rules` & `after6.rules`:** Additional iptables rules for IPv6.
- **`before.init` & `after.init`:** Scripts executed before/after firewall rules are loaded during initialization.
- **`user.rules`:** User-defined firewall rules (IPv4).
- **`user6.rules`:** User-defined firewall rules (IPv6).
- **`applications.d/`:** Application profiles with predefined firewall rules for specific services.

<br>
</details>

<details markdown='1'>
<summary>
/etc/update-manager/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for the **Update Manager**, a tool for managing software updates.

Key files and folders:

- **`meta-release`:** Information about available Ubuntu releases and upgrade paths.
- **`release-upgrades`:** Configuration for release upgrades (e.g., LTS preferences, upgrade prompts).
- **`release-upgrades.d/`:** Additional configuration files for release upgrades.

Example files:

**`/etc/update-manager/meta-release`:**

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

**`/etc/update-manager/release-upgrades`:**

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
This folder exists in default Debian and Ubuntu installations.

It contains scripts that customize the **Message of the Day (MOTD)** displayed when users log in via SSH or on a virtual console.  
Scripts are executed in alphabetical order, and their output is concatenated to form the complete MOTD.

Example scripts:

**`/etc/update-motd.d/uname`:**

```
#!/bin/sh
uname -snrvm
```

**`/etc/update-motd.d/85-fwupd`:**

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
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists but is empty in default installations.

It contains configuration files and scripts for the **update-notifier** package, which provides notifications about available software updates.


<br>
</details>

<details markdown='1'>
<summary>
/etc/UPower/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **UPower**, a power management service that provides information about power sources and battery status.

Example `/etc/UPower/UPower.conf`:

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
- **Debian:** These do **not** exist in default installations.  
- **Ubuntu:** These exist in default installations.

- **`/etc/usb_modeswitch.conf`:** Configuration file for the **usb_modeswitch** package, evaluated by `/usr/sbin/usb_modeswitch_dispatcher`.  
  usb_modeswitch handles USB devices with multiple states/modes (e.g., devices presenting as USB storage but containing modem firmware).

- **`/etc/usb_modeswitch.d/`:** Additional configuration files included by `usb_modeswitch_dispatcher`.

<br>
</details>

<details markdown='1'>
<summary>
/etc/vconsole.conf
</summary>

---
This file exists in default Debian and Ubuntu installations.

It configures **virtual console settings**, including keyboard layout, font, and related parameters.

Example content (Ubuntu 24.04):

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
This folder exists in default Debian and Ubuntu installations.

It contains **system-wide Vim configuration files**, providing default settings for all users of the Vim text editor.

Key files:

- **`vimrc`:** Main system-wide Vim configuration (default options, key bindings).
- **`vimrc.tiny`:** Configuration for the "tiny" version of Vim (minimized feature set).

<br>
</details>

<details markdown='1'>
<summary>
/etc/vmware-tools/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It contains configuration files for **VMware Tools**, a suite of utilities that enhance performance and manageability of virtual machines on VMware platforms.

Example `/etc/vmware-tools/tools.conf` (Ubuntu):

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
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

It is a symbolic link to `/etc/alternatives/vtrgb`, which points to `/etc/console-setup/vtrgb`.  
Used as default input for the `setvtrgb` utility to set the color palette for virtual terminals.


<br>
</details>

<details markdown='1'>
<summary>
/etc/wgetrc
</summary>

---
This file exists in default Debian and Ubuntu installations.

It contains configuration settings for the **wget** utility, a command-line tool for downloading files via HTTP, HTTPS, FTP, etc.

<br>
</details>

<details markdown='1'>
<summary>
/etc/X11/ Folder
</summary>

---
This folder exists in default Debian and Ubuntu installations.

It contains configuration files for the **X Window System (X11)**, the windowing system providing a graphical user interface (GUI) in Unix-like systems.  
Even server installations (without GUI) may include this folder for compatibility or dependency reasons.

<br>
</details>

<details markdown='1'>
<summary>
/etc/xattr.conf
</summary>

---
This file exists in default Debian and Ubuntu installations.

It configures **extended attributes (xattrs)**, which associate metadata (e.g., ACLs, SELinux contexts, file capabilities) with files and directories beyond standard inode data.

Example content:

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
This folder exists in default Debian and Ubuntu installations.

It contains configuration files following the **XDG (X Desktop Group) Base Directory Specification**, which defines standard directories for user-specific configuration, cache, and data files for desktop applications.

Included in server installations for compatibility and dependency reasons.

<br>
</details>

<details markdown='1'>
<summary>
/etc/xml/ Folder
</summary>

---
- **Debian:** This folder does **not** exist in default installations.  
- **Ubuntu:** This folder exists in default installations.

It manages **XML-related configurations, catalogs, and resources**, defining how XML parsers and applications operate (e.g., catalog files, entities, namespaces).

<br>
</details>

<details markdown='1'>
<summary>
/etc/zsh_command_not_found
</summary>

---
- **Debian:** This file does **not** exist in default installations.  
- **Ubuntu:** This file exists in default installations.

Used by the **Zsh shell** to provide suggestions when a command is not found.  
If a user enters a command not in the system's `PATH`, Zsh executes this file with the original command as an argument.

</details>

