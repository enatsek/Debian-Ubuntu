##### DebPackagingOnDebianUbuntu 
# Creating and Using .deb Packages On Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. Abstract
This tutorial deals with creating a .deb package. A .deb package is a  compressed collection of files for installing a software. Mainly used by  Debian GNU/Linux and Ubuntu. 

As Debian or Ubuntu users, we normally use apt command to install programs (or services), but in the background .deb files are used.

Our aim is to create and use a .deb package. Creating a new Debian package is another thing, actually a superset of this operation. It is a subject of another possible tutorial.

This tutorial is a simple one, it does not cover every detail. Its aim is to help you create a simple package.

### 0.1. Configuration
**Workstation:** Debian 12 or Ubuntu 24.04 LTS

**Test Servers:** Ubuntu 24.04 LTS, Ubuntu 22.04 LTS, Ubuntu 20.04 LTS, Debian 12, Debian 11, Debian 10, Debian 12

### 0.2. Sources
[www.debian.org](https://www.debian.org/doc/debian-policy/)  
[www.debian.org](https://www.debian.org/doc/manuals/maint-guide/dother.en.html)  
[tldp.org](https://tldp.org/HOWTO/html_single/Debian-Binary-Package-Building-HOWTO/)  
[github.com](https://github.com/rsm-gh/build-deb/blob/master/DEBIAN_BASICS.md)  


<br>
</details>

<details markdown='1'>
<summary>
1. Basic Information
</summary>

---
### 1.1. Package Types:
.deb packages may be source or binary packages. As their names imply,  they contain source or executable binaries (or scripts). 

As Debian Policy Manual states; A Debian source package contains the  source material used to construct one or more binary packages. 

At this tutorial, we are going to concentrate on binary packages.
 
### 1.2. Package Structure
A .deb package has the following naming format and contains 3 files.

packagename_version-revision_architecture.deb  
apache2_2.4.52-1debian4.4_amd64.deb

#### 1.2.1. debian-binary
.deb package version information. Mostly just contains 2.0.

#### 1.2.2. data.tar.zst
An archive of compressed files in directories. When the .deb file is installed, the files will be copied to the directories where they are.  The extension may be a different one if another compression type is used.

#### 1.2.3. control.tar.zst
An archive of compressed files. The extension may be a different one if  another compression type is used. The most used files are:

**control:** Metadata for the package, like package name, version, etc.

**conffiles:** A list of configuration files. These files are not overwritten when the package is upgraded. 

**preinst:** Scripts to run before unpacking the package, like stopping the services before upgrading.

**postinst:** Scripts to run after unpacking the package, like starting the  installed services.

**prerm:** Scripts to run before removing the package, like stopping the  services.

**postrm:** Scripts to run after removing the package, like removing created files.

### 1.3. .deb Package Manipulation
.deb packages can be installed with apt command too. 

install a package:

```
sudo apt install ./<package>
sudo apt install ./test.deb
```

remove a package:

```
sudo apt remove <appname>
sudo apt remove test
```

purge a package:

```
sudo apt purge <appname>
sudo apt purge test
```

<br>
</details>

<details markdown='1'>
<summary>
2. Package Control Files
</summary>

---
Control files exist in control.tar.zst archive. Some of the files are  listed in 1.2.3. A (nearly) full list is below with brief descriptions,  though some important ones have detailed descriptions.

### 2.1. control
This file contains the values that package managers use. It has fields  and values for the fields.

Most of the fields have single line values, but some may have multi line  values.

When entering multi line fields, the lines other than the first one must  start with a space or a tab.

The fields of a binary package are:
 
**Package:** Mandatory field. Name of the package. Can contain alphanumeric  characters and *,- and . (period). Ex: openssh-server

**Source:** Source package name. Ex: openssh

**Version:** Mandatory field. Version number. Format is: epoch:upstream_ver-debian_ver. Epoch can be omitted. Ex: 1:8.9p1-3

**Section:** Recommended field. Software category. For a Debian package,  there are many software categories like admin, database, httpd, java, etc. 

**Priority:** Recommended field. Could be one of the followings:  

- **required:** Necessary for the proper functioning of the system. 
- **important:** Packages that are expected to be in every Linux system.
- **standard**: Packages that are installed by default. Standard packages must not conflict with each other.
- **optional:** All others. Most of the packages fall into this category. Optional packages may conflict with each other.

**Architecture:** Mandatory field. Architecture that the package is prepared for. Examples: amd64, arm64, i386, powerpc, sparc, all

**Essential:** If set to yes, the package management software would refuse to remove this package. Normally you should set it as no, or skip this  field.

**Depends:** The packages that this package depends absolutely. This package # is not configured unless all the depended packages are configured. 

**Pre-Depends:** Not advised to use. Like Depends, but depended package should be configured before unpacking the package.

**Recommends:** Declares a strong but not absolute dependancy.

**Suggests:** Declares that this package would be more useful with the  listed packages.

**Enhances:** Opposite of Suggests. Declares that listed packages would be  more useful with this package.

**Breaks:** This package breaks the listed packages. They must be  unconfigured before this package can be installed.

**Conflicts:** Similar but stronger than Breaks. They must be unpacked before this package can be installed.

**Installed-Size:** An estimate of the total amount of disk space required to install the package.

**Maintainer:** Mandatory field. Name and email of the maintainer. Ex: Exforge <exforge@x386.org>

**Description:** Mandatory field. Description of the package. The first line is the short description, the others are the long version. 

**Homepage:** The url of the website of the package.

**Built-Using:** The list of packages that this package depended at build  time, but no more.

Also there might be some user defined fields. Ubuntu adds a field named 
**Original Maintainer** to keep Debian Maintainers info while giving theirs.

Contents of Ubuntu 22.04 LTS' apache2 package control file:

```
Package: apache2
Version: 2.4.52-1ubuntu4.4
Architecture: amd64
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Installed-Size: 533
Pre-Depends: init-system-helpers (>= 1.54~)
Depends: apache2-bin (= 2.4.52-1ubuntu4.4), apache2-data (= 2.4.52-1ubuntu4.4), apache2-utils (= 2.4.52-1ubuntu4.4), lsb-base, mime-support, perl:any, procps
Recommends: ssl-cert
Suggests: apache2-doc, apache2-suexec-pristine | apache2-suexec-custom, www-browser, ufw
Conflicts: apache2.2-bin, apache2.2-common
Replaces: apache2.2-bin, apache2.2-common
Provides: httpd, httpd-cgi
Section: httpd
Priority: optional
Homepage: https://httpd.apache.org/
Description: Apache HTTP Server
 The Apache HTTP Server Project's goal is to build a secure, efficient and
 extensible HTTP server as standards-compliant open source software. The
 result has long been the number one web server on the Internet.
 .
 Installing this package results in a full installation, including the
 configuration files, init scripts and support scripts.
Original-Maintainer: Debian Apache Maintainers <debian-apache@lists.debian.org>
```

Contents of Ubuntu 22.04 LTS' openssh package control file:

```
Package: openssh-server
Source: openssh
Version: 1:8.9p1-3
Architecture: amd64
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Debian OpenSSH Maintainers <debian-ssh@lists.debian.org>
Installed-Size: 1501
Pre-Depends: init-system-helpers (>= 1.54~)
Depends: adduser (>= 3.9), dpkg (>= 1.9.0), libpam-modules (>= 0.72-9), libpam-runtime (>= 0.76-14), lsb-base (>= 4.1+Debian3), openssh-client (= 1:8.9p1-3), openssh-sftp-server, procps, ucf (>= 0.28), debconf (>= 0.5) | debconf-2.0, libaudit1 (>= 1:2.2.1), libc6 (>= 2.34), libcom-err2 (>= 1.43.9), libcrypt1 (>= 1:4.1.0), libgssapi-krb5-2 (>= 1.17), libkrb5-3 (>= 1.13~alpha1+dfsg), libpam0g (>= 0.99.7.1), libselinux1 (>= 3.1~), libssl3 (>= 3.0.1), libsystemd0, libwrap0 (>= 7.6-4~), zlib1g (>= 1:1.1.4)
Recommends: default-logind | logind | libpam-systemd, ncurses-term, xauth, ssh-import-id
Suggests: molly-guard, monkeysphere, ssh-askpass, ufw
Conflicts: sftp, ssh-socks, ssh2
Replaces: openssh-client (<< 1:7.9p1-8), ssh, ssh-krb5
Provides: ssh-server
Section: net
Priority: optional
Multi-Arch: foreign
Homepage: http://www.openssh.com/
Description: secure shell (SSH) server, for secure access from remote machines
 This is the portable version of OpenSSH, a free implementation of
 the Secure Shell protocol as specified by the IETF secsh working
 group.
 .
 Ssh (Secure Shell) is a program for logging into a remote machine
 and for executing commands on a remote machine.
 It provides secure encrypted communications between two untrusted
 hosts over an insecure network. X11 connections and arbitrary TCP/IP
 ports can also be forwarded over the secure channel.
 It can be used to provide applications with a secure communication
 channel.
 .
 This package provides the sshd server.
 .
 In some countries it may be illegal to use any encryption at all
 without a special permit.
 .
 sshd replaces the insecure rshd program, which is obsolete for most
 purposes.
```

### 2.2. conffiles
This file contains the list of configuration files of the package. The  files listed here will be considered as conf files. If the user has  changed any of the conf files listed here, she/he will be warned by the  system.

Contents of Ubuntu 22.04 LTS' openssh package conffiles file:
```
/etc/default/ssh
/etc/init.d/ssh
/etc/pam.d/sshd
/etc/ssh/moduli
/etc/ufw/applications.d/openssh-server
```
 
### 2.3. preinst
This is the script (or program, but script is recommended) to run before  unpacking the package. 

The script can be called in the following ways:

- **new-preinst install:** Before the package is installed.
- **new-preinst install old-version new-version:** Before a removed package  is upgraded.
- **new-preinst upgrade old-version new-version:** Before the package is  upgraded.
- **old-preinst abort-upgrade new-version:** If postrm fails during upgrade or fails on failed upgrade.

This script must be idempotent, that is there mustn't be any problems if it runs more than 1 time. 

This script must start with #! 

Also this script must return 0 for success and nonzero for error conditions.

An excerpt from Ubuntu 22.04 LTS' apache2 package preinst file:

```
case "$1" in
    upgrade|install)
	if dpkg --compare-versions "$2" lt-nl "2.4.23-3~" ; then
		list_fixup_conffiles | replace_broken_conffiles
	fi
    ;;
    abort-upgrade)
		list_fixup_conffiles | revert_broken_conffiles
    ;;
    *)
	echo "preinst called with unknown argument \`$1'" >&2
	exit 1
    ;;
esac
```

### 2.4. postinst
This is the script (or program, but script is recommended) to run after  unpacking the package. 

The script can be called in the following ways:

- **postinst configure old-version:** After the package was installed.
- **old-postinst abort-upgrade new-version:** If prerm fails during upgrade or fails on failed-upgrade.
- **old-postinst abort-remove:** If prerm fails during remove.
- **postinst abort-deconfigure in-favour new-package new-version [ removing old-package old-version ]:** If prerm fails during deconfigure in-favour of a package.
- **postinst abort-remove:** If prerm fails during remove in-favour for replacement due to conflict.

This script must be idempotent, that is there mustn't be any problems if it runs more than 1 time. 

This script must start with #! 

Also this script must return 0 for success and nonzero for error conditions.
 
Two excerpts from Ubuntu 22.04 LTS' apache2 package postinst file:

```
is_fresh_install()
{
	if [ -z "$2" ] ; then
		return 0
	fi
	return 1
}
```

```
case "$1" in
	configure)
		enable_default_mpm $@
		install_default_files $@
		enable_default_modules $@
		enable_default_conf $@
		install_default_site $@
		execute_deferred_actions
	;;
	abort-upgrade)
	;;
	abort-remove|abort-deconfigure)
	;;
	*)
		echo "postinst called with unknown argument \`$1'" >&2
		exit 1
	;;
esac
```

### 2.5. prerm
This is the script (or program, but script is recommended) to run before  removing the package. 

The script can be called in the following ways:

- **prerm remove:** Before the package is removed.
- **old-prerm upgrade new-version:** Before an upgrade.
- **new-prerm failed-upgrade old-version new-version:** If the above upgrade fails.
- **prerm deconfigure in-favour new-package new-version:** Before package is deconfigured while dependency is replaced due to conflict.
- **prerm remove in-favour new-package new-version:** Before the package is replaced due to conflict.

This script must be idempotent, that is there mustn't be any problems if it runs more than 1 time. 

This script must start with #! 

Also this script must return 0 for success and nonzero for error  conditions.

Contents of Ubuntu 22.04 LTS' mariadb-server package prerm file:

```
#!/bin/sh
set -e
# Modified dh_systemd_start snippet that's not added automatically
if [ -d /run/systemd/system ]; then
	deb-systemd-invoke stop mariadb.service >/dev/null
# Modified dh_installinit snippet to only run with sysvinit
elif [ -x "/etc/init.d/mariadb" ]; then
	invoke-rc.d mariadb stop || exit $?
fi
```

### 2.6. postrm
This is the script (or program, but script is recommended) to run after  removing the package. 

The script can be called in the following ways:

- **postrm remove:** After the package was removed.
- **postrm purge:** After the package was purged.
- **old-postrm upgrade new-version:** After the package was upgraded.
- **new-postrm failed-upgrade old-version new-version:** If the above upgrade  call fails.
- **postrm disappear overwriter-package overwriter-version:** After all of the package files have been replaced.
- **new-postrm abort-install:** If preinst fails during install.
- **new-postrm abort-install old-version new-version:** If preinst fails  during install for an upgrade of a removed package.
- **new-postrm abort-upgrade old-version new-version:** If preinst fails during upgrade.

This script must be idempotent, that is there mustn't be any problems if it runs more than 1 time. 

This script must start with #! 

Also this script must return 0 for success and nonzero for error  conditions.

An excerpt of Ubuntu 22.04 LTS' openssh-server package postrm file:

```
if [ "$1" = "remove" ]; then
	if [ -x "/usr/bin/deb-systemd-helper" ]; then
		deb-systemd-helper mask 'ssh.service' >/dev/null || true
	fi
fi
if [ "$1" = "purge" ]; then
	if [ -x "/usr/bin/deb-systemd-helper" ]; then
		deb-systemd-helper purge 'ssh.service' >/dev/null || true
		deb-systemd-helper unmask 'ssh.service' >/dev/null || true
	fi
fi
```

### 2.7. config
**config** is an additional script that runs before preinst, before any  predependencies are satisfied. This script can be used for any information that should be prompted to the user.

Contents of Ubuntu 22.04 LTS' mariadb-server package prerm file:

```
#!/bin/bash
set -e
. /usr/share/debconf/confmodule
if [ -n "$DEBIAN_SCRIPT_DEBUG" ]; then set -v -x; DEBIAN_SCRIPT_TRACE=1; fi
${DEBIAN_SCRIPT_TRACE:+ echo "#42#DEBUG# RUNNING $0 $*" 1>&2 }
# Beware that there are two ypwhich one of them needs the 2>/dev/null!
if test -n "`which ypwhich 2>/dev/null`"  &&  ypwhich >/dev/null 2>&1; then
  db_input high mariadb-server-10.6/nis_warning || true
  db_go
fi
```

### 2.8. templates
This file contains templates for user prompting. 

An excerpt from Ubuntu 22.04 LTS' openssh-server package templates file:

```
Template: openssh-server/password-authentication
Type: boolean
Default: true
Description: Allow password authentication?
 By default, the SSH server will allow authenticating using a password.
 You may want to change this if all users on this system authenticate using
 a stronger authentication method, such as public keys.
```

### 2.9. md5sums
This file contains md5 hashes of files of the package.

Content Ubuntu 22.04 LTS' openssh-server package md5sums file:

```
8ec138e332aa1fbc3f081c17e81b62f9  lib/systemd/system/rescue-ssh.target
3841c38ccbff81c6bcab65bfd307c41c  lib/systemd/system/ssh.service
3f25171928b9546beb6a67bf51694eb3  lib/systemd/system/ssh.socket
bc5513f9fb433034b2986886e1af71df  lib/systemd/system/ssh@.service
4b50d38888a7c2093ea4928dca327287  usr/lib/openssh/ssh-session-cleanup
d9f4348145691919611bc60c3212d4a8  usr/sbin/sshd
f410eed89eecfb2bcf29440141a49d4f  usr/share/apport/package-hooks/openssh-server.py
77862d01cdeb1232790155687382fdad  usr/share/doc/openssh-client/examples/ssh-session...
b3cce9472de613cc6cb967aa63a7e28f  usr/share/man/man5/moduli.5.gz
d6f0d424d86f689708da000cfd8b9c0c  usr/share/man/man5/sshd_config.5.gz
ac7abad4e73226affab0c56e47cf8b68  usr/share/man/man8/sshd.8.gz
30e0fe758429c57d35a5e71dbd8dd2f8  usr/share/openssh/sshd_config
cb02155c6c0d5678ef2e827ebb983a3d  usr/share/openssh/sshd_config.md5sum
```

### 2.10. triggers
A package declares its relationship to some triggers by including a  triggers file.

There are the following trigger directives:

- **interest <trigger>:** The package is interested in the trigger.
- **interest-await <trigger>:** Puts the triggering package in awaited state.
- **interest-noawait <trigger>:** Does not put the triggering package in awaited state.
- **activate <trigger>:** Any change in this package activates the trigger
- **activate-await <trigger>:** Only puts the package in awaited state.
- **activate-noawait <trigger>:** Never puts the package in awaited state.

Contents of Ubuntu 22.04 LTS' mariadb-server package triggers file:

```
interest-noawait /etc/mysql
interest-noawait /etc/systemd/system/mariadb.service.d
```

### 2.11. symbols and shlibs
These files contain information about used shared libraries.

<https://man7.org/linux/man-pages/man5/deb-symbols.5.html>  
<https://man7.org/linux/man-pages/man5/deb-shlibs.5.html>

Contents of Ubuntu 22.04 LTS' slapd package shlibs file:

```
libslapi-2.5 0 libslapi-2.5-0
```

<br>
</details>

<details markdown='1'>
<summary>
3. Package Data Files
</summary>

---
### 3.1. Basics
Data files exist in data.tar.zst archive. The archive contains the files  in their corresponding directories. Every file in this archive is unpacked to its corresponding directory.
 
Files in Ubuntu 22.04 LTS' openssh-server package:

```
├── etc
│   ├── default
│   │   └── ssh
│   ├── init.d
│   │   └── ssh
│   ├── pam.d
│   │   └── sshd
│   ├── ssh
│   │   ├── moduli
│   │   └── sshd_config.d
│   └── ufw
│       └── applications.d
│           └── openssh-server
├── lib
│   └── systemd
│       └── system
│           ├── rescue-ssh.target
│           ├── ssh.service
│           ├── ssh@.service
│           └── ssh.socket
└── usr
    ├── lib
    │   └── openssh
    │       └── ssh-session-cleanup
    ├── sbin
    │   └── sshd
    └── share
        ├── apport
        │   └── package-hooks
        │       └── openssh-server.py
        ├── doc
        │   ├── openssh-client
        │   │   └── examples
        │   │       └── ssh-session-cleanup.service
        │   └── openssh-server -> openssh-client
        ├── man
        │   ├── man5
        │   │   ├── authorized_keys.5.gz -> ../man8/sshd.8.gz
        │   │   ├── moduli.5.gz
        │   │   └── sshd_config.5.gz
        │   └── man8
        │       └── sshd.8.gz
        └── openssh
            ├── sshd_config
            └── sshd_config.md5sum
```

### 3.2. File Locations
Data files consists binaries, static files, dynamic files, configurations, etc. 

Every file must be placed on an appropriate place. Some examples:

- Architecture-independent, application-specific files --> /usr/share
- User specific configuration files --> ~/.packagename. File or directory.
- Configuration files --> /etc/packagename
- Systemd unit files --> /lib/systemd/system
- Log files --> /var/log/packagename
- Cron jobs --> Regarding the time period, one of the following:
   - /etc/cron.hourly 
   - /etc/cron.daily 
   - /etc/cron.weekly 
   - /etc/cron.monthly
   - If the time period is different: /etc/cron.d

<br>
</details>

<details markdown='1'>
<summary>
4. Package Installation Process
</summary>

---
```
  If there is a previous version of the package:
    Call for the old package: "old-prerm upgrade new-version"
    If return status is not 0:
      Call for the current package: "new-prerm failed-upgrade old-version new-version"
      If return status is not 0:
        Call for the old package: "old-postinst abort-upgrade new-version"
          If return status is 0:
            Upgrade unsuccessfull, old version works
            Exit
          Else:
            Upgrade unsuccessfull, old version is broken too
            Exit
  If there are conflicting and/or broken packages
    For each of these packages run:
      # Unconfigure them
      deconfigured's-prerm deconfigure in-favour package-being-installed version
      If return status is not 0:
        deconfigured's-postinst abort-deconfigure in-favour \
            package-being-installed-but-failed version
      # Remove them
      conflictor's-prerm remove in-favour package new-version
      If return status is not 0:
        conflictor's-postinst abort-remove in-favour package new-version
      If there are any packages that depend of the conflicting or broken packages
        For each of these packages run:
          # Unconfigure them
          deconfigured's-prerm deconfigure in-favour package-being-installed \
              version removing conflicting-package version
          If return status is not 0:
            deconfigured's-postinst abort-deconfigure in-favour \
               package-being-installed-but-failed version \
               removing conflicting-package version
      # Prepare to remove conflicting packages
      conflictor's-prerm remove in-favour package new-version
      If return status is not 0:
        conflictor's-postinst abort-remove in-favour package new-version

  # Run the preinst of the new package
  If the package is being upgraded:
    new-preinst upgrade old-version new-version
    If return status is not 0:
      new-postrm abort-upgrade old-version new-version
        If return status is 0:
          Upgrade unsuccessfull, old version works
          Exit
        Else:
          Upgrade unsuccessfull, old version is broken too
          Exit
  Else if the package is new but there are old conf files:
    new-preinst install old-version new-version
    If return status is not 0:
      new-postrm abort-install old-version new-version
      Install unsuccessfull
      Exit
  Else:    # New install with no conf files
    new-preinst install
    If return status is not 0:
      new-postrm abort-install
      Install unsuccessfull
      Exit
  Unpack all the files
  # A package cannot write another package's file unless Replaces is used

  If the package is being upgraded:
    old-postrm upgrade new-version
    If return condition is not 0:
      new-postrm failed-upgrade old-version new-version
      If return condition is 0:
        Upgrade failed, old version works
        Exit
      Else
        # Upgrade failed, try to cover up
        old-preinst abort-upgrade new-version
        If return condition is 0:
          new-postrm abort-upgrade old-version new-version
          If return condition is 0:
            old-postinst abort-upgrade new-version
            Upgrade failed, old version works
            Exit
          Else:
            Upgrade failed, old version broken
            Exit
        Else:
          Upgrade failed, old version broken
          Exit
  Files in old version but not in new version removed
  New file list replaces the old one
  New scripts replaces the old ones
  For each package, whose files are overwritten and not required for dependencies:
    # Remove them
    disappearer's-postrm disappear overwriter overwriter-version
    Remove package scripts
    Update their status as "Not-Installed"
  If Any files of the new package is also listed in the other packages:
    Remove them
  Remove temporary and backup files made during installation
  Set the status of the package as "Unpacked"
  If there were conflicting packages:
    Remove them
```

<br>
</details>

<details markdown='1'>
<summary>
5. Package Removal/Purge Process
</summary>

---
```
  prerm remove
  If return status is not 0:
    If failure is due to conflict:
      conflictor's-postinst abort-remove in-favour package new-version
    Else: 
      postinst abort-remove
    If return status is 0:
      Remove aborted, package is still installed
      Exit
    Else:
      Remove aborted, package is broken
      Exit
  Remove package files (except conffiles)    
  Remove all scripts except postrm
  If Purge
    Remove conffiles and temporary and backup files made during process
    postrm purge
    Remove package's file list    
```

<br>
</details>

<details markdown='1'>
<summary>
6. .deb Package Preparation Checklist
</summary>

---
### 6.1. Create File and Folder Structure for the Package
A minimal set would include the following:

```
ProgramName-Version/
ProgramName-Version/DEBIAN
ProgramName-Version/DEBIAN/control
ProgramName-Version/usr/
ProgramName-Version/usr/bin/
ProgramName-Version/usr/bin/ProgramName
```

You may also need the following files/folder:

```
ProgramName-Version/DEBIAN/control
ProgramName-Version/DEBIAN/preinst
ProgramName-Version/DEBIAN/postinst
ProgramName-Version/DEBIAN/prerm
ProgramName-Version/DEBIAN/postrm
ProgramName-Version/etc/
ProgramName-Version/etc/ProgramName.conf
ProgramName-Version/etc/ProgramName/
ProgramName-Version/usr/share/applications/ProgramName.desktop
ProgramName-Version/usr/share/ProgramName/ProgramFiles
```

### 6.2. Copy Files
You need to copy program executable, control file, script files and  other files to their appropriate locations. 

- /usr/share/ProgramName/ is used if you have more than 1 files for the  program. 
- You can use /etc or /etc/ProgramName folders if you have 1 or more  configuration files respectively. 
- You can use /usr/share/applications/ folder for creating desktop  launchers.

### 6.3. Preparing and Building The Package
When all files are ready, you have to set permissions of the executable  files

```
chmod a+x ProgramName-Version/..
```

And build the package:

```
dpkg-deb -Z xz --build --root-owner-group ProgramName-Version
```
 
The resulting .deb file is your package.

<br>
</details>

<details markdown='1'>
<summary>
7. A Very Simple Package
</summary>

---
Now, we are going to create a very simple package, namely "distro". Our  package is a python script which displays the Unix distro name and the version information.

The package will only have the executable script and the control file. No configuration file or maintenance scripts are needed.

### 7.1. Create Folder Structure
We are going to create a packages folder at our home folder. All the  packages will reside on this folder with their own folders.

```
mkdir ~/packages
```

Remember a package has this format for its name:   
packagename_version-revision_architecture.deb

```
mkdir ~/packages/distro_1.0.0-1_all
```

/usr/bin folder to put the executable

```
mkdir -p ~/packages/distro_1.0.0-1_all/usr/bin
```

DEBIAN folder for control file

```
mkdir ~/packages/distro_1.0.0-1_all/DEBIAN
```

### 7.2. Executable File
Copy, or in our case, fill the executable file:

```
nano ~/packages/distro_1.0.0-1_all/usr/bin/distro
```

Fill as below:

```
#!/usr/bin/env python3
def distro_version():
    d = {}
    try:
        with open("/etc/os-release") as f:
            for line in f:
                line = line.replace('"', '')
                line = line.replace('\n', '')
                if line == "":
                    continue
                (key, val) = line.split("=")
                d[(key)] = val
        distro = d["NAME"]
        version = d["VERSION_ID"]
    except:
        distro = "Other"
        version = "Other"
    return distro, version
distro, version = distro_version()
print(distro, version)
```

make it executable

```
chmod +x ~/packages/distro_1.0.0-1_all/usr/bin/distro
```

### 7.3. control File
Copy, or in our case, fill the control file:

```
nano ~/packages/distro_1.0.0-1_all/DEBIAN/control
```

Fill as below:

```
Package: distro
Version: 1.0.0-1
Architecture: all
Maintainer: Exforge <exforge@x386.org>
Depends: python3
Homepage: https://github.com/enatsek/
Description: Prints Linux Distribution and Name
  A python script to print linux distro and version of the distro. I do not know what 
  it does on other OSs.
```

### 7.4. Build the package
```
cd ~/packages
dpkg-deb -Z xz --build --root-owner-group distro_1.0.0-1_all 
```

Your package distro_1.0.0-1_all.deb is in your ~/packages folder.

**A note:** dpkg-deb normally use zst compression, but we override it with -Z xz flag for xz compression. Because, the packages made in Ubuntu 22.04 with zst compression does not work on Debian distributions.

<br>
</details>

<details markdown='1'>
<summary>
8. A Bit More Complicated Package
</summary>

---
Our next package is named as **watchbox* and is a bit more complicated.

It is a python script too, but it is aimed to run as a service.

Our package must install it as a systemd service, enable and start it  after the installation. Also the service must be stopped before removing  or upgrading the package. 

As control files, beside the control file we will have conffiles,  postinst, and prerm.

As data files, we will have the script itself, configuration file, and  the service unit file.

### 8.0. About Watchbox
Watchbox is a service demonstration program, which allow periodic checks  for network connectivity for hosts, web pages, files, or services.

It has an application named watchbox, configuration file named  watchbox.conf, and a systemd service unit file named watchbox.service.

For more details, please see:

<https://github.com/enatsek/watchbox>

### 8.1. Copy Watchbox Files to a Temporary Place
Get watchbox files from github

```
wget https://raw.githubusercontent.com/enatsek/watchbox/main/watchbox \
     -P /tmp
wget https://raw.githubusercontent.com/enatsek/watchbox/main/watchbox.conf \
     -P /tmp
wget https://raw.githubusercontent.com/enatsek/watchbox/main/watchbox.service \
     -P /tmp
```

### 8.2. Folder Structure
Again we will use the folder ~/packages

```
~/packages/
~/packages/watchbox_0.9-1_all/
~/packages/watchbox_0.9-1_all/DEBIAN/
~/packages/watchbox_0.9-1_all/DEBIAN/control
~/packages/watchbox_0.9-1_all/DEBIAN/conffiles
~/packages/watchbox_0.9-1_all/DEBIAN/postinst
~/packages/watchbox_0.9-1_all/DEBIAN/prerm
~/packages/watchbox_0.9-1_all/etc/
~/packages/watchbox_0.9-1_all/etc/watchbox.conf
~/packages/watchbox_0.9-1_all/lib/
~/packages/watchbox_0.9-1_all/lib/systemd/
~/packages/watchbox_0.9-1_all/lib/systemd/system/
~/packages/watchbox_0.9-1_all/lib/systemd/system/watchbox.service
~/packages/watchbox_0.9-1_all/usr/
~/packages/watchbox_0.9-1_all/usr/bin/
~/packages/watchbox_0.9-1_all/usr/bin/watchbox
```

### 8.3. Create Folder Structure
```
mkdir -p ~/packages/watchbox_0.9-1_all/DEBIAN/
mkdir -p ~/packages/watchbox_0.9-1_all/etc
mkdir -p ~/packages/watchbox_0.9-1_all/lib/systemd/system/
mkdir -p ~/packages/watchbox_0.9-1_all/usr/bin/
```

### 8.4. Copy Watchbox Files to Their Places
```
cp /tmp/watchbox.conf ~/packages/watchbox_0.9-1_all/etc/
cp /tmp/watchbox.service ~/packages/watchbox_0.9-1_all/lib/systemd/system/
cp /tmp/watchbox -p ~/packages/watchbox_0.9-1_all/usr/bin/
```

Make it executable too:

```
chmod +x ~/packages/watchbox_0.9-1_all/usr/bin/watchbox
```

### 8.5. Create Control Files and Maintenance Scripts
control file (package metadata)

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/control
```

Fill as below

```
Package: watchbox
Version: 0.9-1
Architecture: amd64
Maintainer: Exforge <exforge@x386.org>
Homepage: https://github.com/enatsek/watchbox/
Depends: python3, python3-systemd
Description: Automated Service Checking Tool
  WatchBox (AKA watchbox) is planned to be a Systemd service for starting at the power-up and making periodic checks.
  Currently it has 6 types of checks:
  - IPPing: Checks if an IP address or hostname can be pinged
  - IPPort: Checks if an IP address or hostname can be connected through a TCP Port
  - Webpage: Checks if a webpage exists
  - WebpageContent: Checks if a webpage has a content
  - LocalPath: Checks if a path exists
  - LocalService: Checks if a systemd service is active
  Check status results can be collected to systemd journal, text file, and/or sqlite db file.
  Configuration file watchbox.conf is expected to be in /etc directory. It is well documented inside.
  Disclaimer: This program is far from being optimized, so it is not adviced to use it on production environments.
```

conffiles (Configuration files, stay after remove, removed at purge)

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/conffiles
```

Fill as below

```
/etc/watchbox.conf
```

postinst (script to run after installing)

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/postinst
```

Fill as below (Enables and runs watchbox service)

```
systemctl enable watchbox
systemctl start watchbox
```

Make it executable

```
chmod +x ~/packages/watchbox_0.9-1_all/DEBIAN/postinst
```

prerm (script to run before removing and upgrading)

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/prerm
```

Fill as below (Stops watchbox service)

```
systemctl stop watchbox
```

Make it executable

```
chmod +x ~/packages/watchbox_0.9-1_all/DEBIAN/prerm
```

### 8.6. Build the Package
```
cd ~/packages
dpkg-deb -Z xz --build --root-owner-group watchbox_0.9-1_all 
```

Your package watchbox_0.9-1_all.deb is in your ~/packages folder.

</details>

