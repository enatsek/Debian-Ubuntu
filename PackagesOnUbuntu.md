##### PackagesOnUbuntu 
# Ubuntu Software Packages

## 0. Specs
---
### 0.0. Info
We will explore the softare packages normally present in Ubuntu server editions (namely Ubuntu 24.04 Server LTS). 

Debian and Ubuntu has some differences in classifications, so there are 2 separate tutorials for them.

### 0.1. Debian Packages
Debian (and therefore Ubuntu) has around 60.000 software packages (a huge number). 

These packages can be classified in a lot of ways. But for this tutorial we are going to use the priority values for the classification.

The priority values range from "required" to "extra", and they are defined as follows:

**required:** Essential packages that are necessary for the proper functioning  of the system, such as the kernel, basic system utilities, and essential  libraries.

**important:** Important packages that are not strictly necessary for basic  system operation but are still considered essential for most users. These may include important system administration tools or libraries.

**standard:** Packages that provide a reasonably small but not essential subset of the Debian system. These packages are typically included in most installations.

**optional:** Additional packages that are not necessary for the basic system  operation but provide additional functionality or applications that many users may find useful.

**extra:** Packages that are not officially part of the Ubuntu distribution but  are available in the Debian repositories. These packages may include  experimental or third-party software. 

I have added 1 more category: necessary.

**necessary:** These packages are depended by required, important, and standard  packages, but don't exist in one of those groups.

We are going to explore required, important, standard, and necessary software packages.

### 0.2. Package Documentation Template
I prefer using the following template for my documentation
 
#### 0.2.1. Official Package Description
Debian's (and/or Ubuntu's) description of the package as in the package file.

#### 0.2.2. Depended Packages
The package is depended on these packages, that it, it requires them to install and work.

#### 0.2.3. Configuration Files
Configuration files supplied with the package, generally under /etc/ folder.

#### 0.2.4. Executable Files
Executable files supplied with the package, generally under /bin, /sbin, /usr/bin, /usr/sbin folders.

### 0.3. Sources
This tutorial is generated semi-automatically by using apt-cache, apt-file, and aptitude commands. And with a little help from ChatGPT.

List Required packages:

```
aptitude search '?priority(required)'
```

You may need to install the aptitude package:

```
sudo apt update
sudo apt install aptitude --yes
```

List Important packages:

```
aptitude search '?priority(important)'
```

List Standard packages:

```
aptitude search '?priority(standard)'
```

List details of a package (description, depended packages, etc):

```
apt-cache show base-files --no-all-versions
```

List files contained by a package

```
apt-file list base-files
```

You may need to install the apt-file package:

```
sudo apt update
sudo apt install apt-file --yes
```

You also need to update apt-file cache

```
sudo apt-file update
```

<br>

## 1. Required Packages
---
These are the (very) essential packages. You may expect them in every Ubuntu installation.

At my last check, the following packages are marked as required:

**apt-utils:** package management related utility programs  
**base-files:** Debian base system miscellaneous files  
**base-passwd:** Debian base system master password and group files  
**bash:** GNU Bourne Again SHell  
**bsdutils:** basic utilities from 4.4BSD-Lite  
**coreutils:** GNU core utilities  
**dash:** POSIX-compliant shell  
**debconf:** Debian configuration management system  
**debianutils:** Miscellaneous utilities specific to Debian  
**diffutils:** File comparison utilities  
**dpkg:** Debian package management system  
**e2fsprogs:** ext2/ext3/ext4 file system utilities  
**findutils:** utilities for finding files--find, xargs  
**gcc-14-base:** GCC, the GNU Compiler Collection (base package)  
**grep:** GNU grep, egrep and fgrep  
**gzip:** GNU compression utilities  
**hostname:** utility to set/show the host name or domain name  
**init-system-helpers:** helper tools for all init systems  
**libacl1:** access control list - shared library  
**libattr1:** extended attribute handling - shared library  
**libaudit-common:** Dynamic library for security auditing - common files  
**libaudit1:** Dynamic library for security auditing  
**libblkid1:** block device ID library  
**libbz2-1.0:** high-quality block-sorting file compressor library - runtime  
**libc-bin:** GNU C Library: Binaries  
**libc6:** GNU C Library: Shared libraries  
**libcap-ng0:** alternate POSIX capabilities library  
**libcap2:** POSIX 1003.1e capabilities (library)  
**libcom-err2:** common error description library  
**libcrypt1:** libcrypt shared library  
**libdb5.3:** Berkeley v5.3 Database Libraries [runtime]  
**libdebconfclient0:** Debian Configuration Management System (C-implementation library)  
**libext2fs2:** ext2/ext3/ext4 file system libraries  
**libext2fs2t64:** ext2/ext3/ext4 file system libraries  
**libgcc-s1:** GCC support library  
**libgcrypt20:** LGPL Crypto library - runtime library  
**libgmp10:** Multiprecision arithmetic library  
**libgpg-error0:** GnuPG development runtime library  
**liblz4-1:** Fast LZ compression algorithm library - runtime  
**liblzma5:** XZ-format compression library  
**libmd0:** message digest functions from BSD systems - shared library  
**libmount1:** device mounting library  
**libncursesw6:** shared libraries for terminal handling (wide character support)  
**libpam-modules:** Pluggable Authentication Modules for PAM  
**libpam-modules-bin:** Pluggable Authentication Modules for PAM - helper binaries  
**libpam-runtime:** Runtime support for the PAM library  
**libpam0g:** Pluggable Authentication Modules library  
**libpcre2-8-0:** New Perl Compatible Regular Expression Library- 8 bit runtime files  
**libproc2-0:** library for accessing process information from /proc  
**libselinux1:** SELinux runtime shared libraries  
**libsemanage-common:** Common files for SELinux policy management libraries  
**libsemanage2:** SELinux policy management library  
**libsepol2:** SELinux library for manipulating binary security policies  
**libsmartcols1:** smart column output alignment library  
**libss2:** command-line interface parsing library  
**libssl3:** Secure Sockets Layer toolkit - shared libraries  
**libssl3t64:** Secure Sockets Layer toolkit - shared libraries  
**libsystemd0:** systemd utility library  
**libtinfo6:** shared low-level terminfo library for terminal handling  
**libudev1:** libudev shared library  
**libuuid1:** Universally Unique ID library  
**libzstd1:** fast lossless compression algorithm  
**login:** system login tools  
**logsave:** save the output of a command in a log file  
**mawk:** Pattern scanning and text processing language  
**mount:** tools for mounting and manipulating filesystems  
**ncurses-base:** basic terminal type definitions  
**ncurses-bin:** terminal-related programs and man pages  
**passwd:** change and administer password and group data  
**perl-base:** minimal Perl system  
**procps:** /proc file system utilities  
**sed:** GNU stream editor for filtering/transforming text  
**sensible-utils:** Utilities for sensible alternative selection  
**sysvinit-utils:** System-V-like utilities  
**tar:** GNU version of the tar archiving utility  
**util-linux:** miscellaneous system utilities  
**zlib1g:** compression library - runtime  

<br>

### 1.1 apt-utils Package
#### 1.1.1. Official Package Description
package management related utility programs  
This package contains some less used commandline utilities related  
to package management with APT.  
.  
apt-extracttemplates is used by debconf to prompt for configuration  
questions before installation.  
apt-ftparchive is used to create Packages and other index files  
needed to publish an archive of Debian packages  
apt-sortpkgs is a Packages/Sources file normalizer.  

#### 1.1.2. Depended Packages
apt  
libapt-pkg6.0t64  
libc6  
libdb5.3t64  
libgcc-s1  
libstdc++6  

#### 1.1.3. Configuration Files
(None)

#### 1.1.4. Executable Files
/usr/bin/apt-extracttemplates  
/usr/bin/apt-ftparchive  
/usr/bin/apt-sortpkgs  

<br>

### 1.2 base-files Package
#### 1.2.1. Official Package Description
Debian base system miscellaneous files  
This package contains the basic filesystem hierarchy of a Debian system, and  
several important miscellaneous files, such as /etc/debian_version,  
/etc/host.conf, /etc/issue, /etc/motd, /etc/profile, and others,  
and the text of several common licenses in use on Debian systems.  

#### 1.2.2. Depended Packages
awk  
libc6  
libcrypt1  

#### 1.2.3. Configuration Files
/etc/debian_version  
/etc/dpkg/origins/debian  
/etc/dpkg/origins/ubuntu  
/etc/host.conf  
/etc/issue  
/etc/issue.net  
/etc/legal  
/etc/lsb-release  
/etc/os-release  
/etc/profile.d/01-locale-fix.sh  
/etc/update-motd.d/00-header  
/etc/update-motd.d/10-help-text  
/etc/update-motd.d/50-motd-news  

#### 1.2.4. Executable Files
/bin  
/sbin  
/usr/bin/locale-check  

<br>

### 1.3 base-passwd Package
#### 1.3.1. Official Package Description
Debian base system master password and group files  
These are the canonical master copies of the user database files  
(/etc/passwd and /etc/group), containing the Debian-allocated user and  
group IDs. The update-passwd tool is provided to keep the system databases  
synchronized with these master files.  

#### 1.3.2. Depended Packages
libc6  
libdebconfclient0  
libselinux1  

#### 1.3.3. Configuration Files
(None)

#### 1.3.4. Executable Files
/usr/sbin/update-passwd  

<br>

### 1.4 bash Package
#### 1.4.1. Official Package Description
GNU Bourne Again SHell  
Bash is an sh-compatible command language interpreter that executes  
commands read from the standard input or from a file.  Bash also  
incorporates useful features from the Korn and C shells (ksh and csh).  
.  
Bash is ultimately intended to be a conformant implementation of the  
IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).  
.  
The Programmable Completion Code, by Ian Macdonald, is now found in  
the bash-completion package.  

#### 1.4.2. Depended Packages
base-files  
debianutils  
libc6  
libtinfo6  

#### 1.4.3. Configuration Files
/etc/bash.bashrc  
/etc/skel/.bash_logout  
/etc/skel/.bashrc  
/etc/skel/.profile  

#### 1.4.4. Executable Files
/usr/bin/bash  
/usr/bin/bashbug  
/usr/bin/clear_console  
/usr/bin/rbash  

<br>

### 1.5 bsdutils Package
#### 1.5.1. Official Package Description
basic utilities from 4.4BSD-Lite  
This package contains the bare minimum of BSD utilities needed for a Debian  
system: logger, renice, script, scriptlive, scriptreplay and wall. The  
remaining standard BSD utilities are provided by bsdextrautils.  

#### 1.5.2. Depended Packages
libc6  
libsystemd0  

#### 1.5.3. Configuration Files
(None)

#### 1.5.4. Executable Files
/usr/bin/logger  
/usr/bin/renice  
/usr/bin/script  
/usr/bin/scriptlive  
/usr/bin/scriptreplay  
/usr/bin/wall  

<br>

### 1.6 coreutils Package
#### 1.6.1. Official Package Description
GNU core utilities  
This package contains the basic file, shell and text manipulation  
utilities which are expected to exist on every operating system.  
.  
Specifically, this package includes:  
arch base64 basename cat chcon chgrp chmod chown chroot cksum comm cp  
csplit cut date dd df dir dircolors dirname du echo env expand expr  
factor false flock fmt fold groups head hostid id install join link ln  
logname ls md5sum mkdir mkfifo mknod mktemp mv nice nl nohup nproc numfmt  
od paste pathchk pinky pr printenv printf ptx pwd readlink realpath rm  
rmdir runcon sha*sum seq shred sleep sort split stat stty sum sync tac  
tail tee test timeout touch tr true truncate tsort tty uname unexpand  
uniq unlink users vdir wc who whoami yes  

#### 1.6.2. Depended Packages
libacl1  
libattr1  
libc6  
libgmp10  
libselinux1  
libssl3t64  

#### 1.6.3. Configuration Files
(None)

#### 1.6.4. Executable Files
/usr/bin/[  
/usr/bin/arch  
/usr/bin/b2sum  
/usr/bin/base32  
/usr/bin/base64  
/usr/bin/basename  
/usr/bin/basenc  
/usr/bin/cat  
/usr/bin/chcon  
/usr/bin/chgrp  
/usr/bin/chmod  
/usr/bin/chown  
/usr/bin/cksum  
/usr/bin/comm  
/usr/bin/cp  
/usr/bin/csplit  
/usr/bin/cut  
/usr/bin/date  
/usr/bin/dd  
/usr/bin/df  
/usr/bin/dir  
/usr/bin/dircolors  
/usr/bin/dirname  
/usr/bin/du  
/usr/bin/echo  
/usr/bin/env  
/usr/bin/expand  
/usr/bin/expr  
/usr/bin/factor  
/usr/bin/false  
/usr/bin/fmt  
/usr/bin/fold  
/usr/bin/groups  
/usr/bin/head  
/usr/bin/hostid  
/usr/bin/id  
/usr/bin/install  
/usr/bin/join  
/usr/bin/link  
/usr/bin/ln  
/usr/bin/logname  
/usr/bin/ls  
/usr/bin/md5sum  
/usr/bin/md5sum.textutils  
/usr/bin/mkdir  
/usr/bin/mkfifo  
/usr/bin/mknod  
/usr/bin/mktemp  
/usr/bin/mv  
/usr/bin/nice  
/usr/bin/nl  
/usr/bin/nohup  
/usr/bin/nproc  
/usr/bin/numfmt  
/usr/bin/od  
/usr/bin/paste  
/usr/bin/pathchk  
/usr/bin/pinky  
/usr/bin/pr  
/usr/bin/printenv  
/usr/bin/printf  
/usr/bin/ptx  
/usr/bin/pwd  
/usr/bin/readlink  
/usr/bin/realpath  
/usr/bin/rm  
/usr/bin/rmdir  
/usr/bin/runcon  
/usr/bin/seq  
/usr/bin/sha1sum  
/usr/bin/sha224sum  
/usr/bin/sha256sum  
/usr/bin/sha384sum  
/usr/bin/sha512sum  
/usr/bin/shred  
/usr/bin/shuf  
/usr/bin/sleep  
/usr/bin/sort  
/usr/bin/split  
/usr/bin/stat  
/usr/bin/stdbuf  
/usr/bin/stty  
/usr/bin/sum  
/usr/bin/sync  
/usr/bin/tac  
/usr/bin/tail  
/usr/bin/tee  
/usr/bin/test  
/usr/bin/timeout  
/usr/bin/touch  
/usr/bin/tr  
/usr/bin/true  
/usr/bin/truncate  
/usr/bin/tsort  
/usr/bin/tty  
/usr/bin/uname  
/usr/bin/unexpand  
/usr/bin/uniq  
/usr/bin/unlink  
/usr/bin/users  
/usr/bin/vdir  
/usr/bin/wc  
/usr/bin/who  
/usr/bin/whoami  
/usr/bin/yes  
/usr/sbin/chroot  

<br>

### 1.7 dash Package
#### 1.7.1. Official Package Description
POSIX-compliant shell  
The Debian Almquist Shell (dash) is a POSIX-compliant shell derived  
from ash.  
.  
Since it executes scripts faster than bash, and has fewer library  
dependencies (making it more robust against software or hardware  
failures), it is used as the default system shell on Debian systems.  

#### 1.7.2. Depended Packages
debianutils  
dpkg  
libc6  

#### 1.7.3. Configuration Files
(None)

#### 1.7.4. Executable Files
/usr/bin/dash  
/usr/bin/sh  

<br>

### 1.8 debconf Package
#### 1.8.1. Official Package Description
Debian configuration management system  
Debconf is a configuration management system for debian packages. Packages  
use Debconf to ask questions when they are installed.  

#### 1.8.2. Depended Packages
(None)

#### 1.8.3. Configuration Files
/etc/apt/apt.conf.d/70debconf  
/etc/debconf.conf  

#### 1.8.4. Executable Files
/usr/bin/debconf  
/usr/bin/debconf-apt-progress  
/usr/bin/debconf-communicate  
/usr/bin/debconf-copydb  
/usr/bin/debconf-escape  
/usr/bin/debconf-set-selections  
/usr/bin/debconf-show  
/usr/sbin/dpkg-preconfigure  
/usr/sbin/dpkg-reconfigure  

<br>

### 1.9 debianutils Package
#### 1.9.1. Official Package Description
Miscellaneous utilities specific to Debian  
This package provides a number of small utilities which are used  
primarily by the installation scripts of Debian packages, although  
you may use them directly.  
.  
The specific utilities included are:  
add-shell installkernel ischroot remove-shell run-parts savelog  
update-shells which  

#### 1.9.2. Depended Packages
libc6  

#### 1.9.3. Configuration Files
(None)

#### 1.9.4. Executable Files
/usr/bin/ischroot  
/usr/bin/run-parts  
/usr/bin/savelog  
/usr/bin/tempfile  
/usr/bin/which.debianutils  
/usr/sbin/add-shell  
/usr/sbin/installkernel  
/usr/sbin/remove-shell  
/usr/sbin/update-shells  

<br>

### 1.10 diffutils Package
#### 1.10.1. Official Package Description
File comparison utilities  
The diffutils package provides the diff, diff3, sdiff, and cmp programs.  
.  
diff shows differences between two files, or each corresponding file  
in two directories.  cmp shows the offsets and line numbers where  
two files differ.  cmp can also show all the characters that  
differ between the two files, side by side.  diff3 shows differences  
among three files.  sdiff merges two files interactively.  
.  
The set of differences produced by diff can be used to distribute  
updates to text files (such as program source code) to other people.  
This method is especially useful when the differences are small compared  
to the complete files.  Given diff output, the patch program can  
update, or "patch", a copy of the file.  

#### 1.10.2. Depended Packages
libc6  

#### 1.10.3. Configuration Files
(None)

#### 1.10.4. Executable Files
/usr/bin/cmp  
/usr/bin/diff  
/usr/bin/diff3  
/usr/bin/sdiff  

<br>

### 1.11 dpkg Package
#### 1.11.1. Official Package Description
Debian package management system  
This package provides the low-level infrastructure for handling the  
installation and removal of Debian software packages.  
.  
For Debian package development tools, install dpkg-dev.  

#### 1.11.2. Depended Packages
libbz2-1.0  
libc6  
liblzma5  
libmd0  
libselinux1  
libzstd1  
tar  
zlib1g  

#### 1.11.3. Configuration Files
/etc/alternatives/README  
/etc/cron.daily/dpkg  
/etc/dpkg/dpkg.cfg  
/etc/logrotate.d/alternatives  
/etc/logrotate.d/dpkg  

#### 1.11.4. Executable Files
/usr/bin/dpkg  
/usr/bin/dpkg-deb  
/usr/bin/dpkg-divert  
/usr/bin/dpkg-maintscript-helper  
/usr/bin/dpkg-query  
/usr/bin/dpkg-realpath  
/usr/bin/dpkg-split  
/usr/bin/dpkg-statoverride  
/usr/bin/dpkg-trigger  
/usr/bin/update-alternatives  
/usr/sbin/start-stop-daemon  

<br>

### 1.12 e2fsprogs Package
#### 1.12.1. Official Package Description
ext2/ext3/ext4 file system utilities  
The ext2, ext3 and ext4 file systems are successors of the original ext  
("extended") file system. They are the main file system types used for  
hard disks on Debian and other Linux systems.  
.  
This package contains programs for creating, checking, and maintaining  
ext2/3/4-based file systems.  It also includes the "badblocks" program,  
which can be used to scan for bad blocks on a disk or other storage device.  

#### 1.12.2. Depended Packages
libblkid1  
libc6  
libcom-err2  
libext2fs2t64  
libss2  
libuuid1  
logsave  

#### 1.12.3. Configuration Files
/etc/cron.d/e2scrub_all  
/etc/e2scrub.conf  
/etc/mke2fs.conf  

#### 1.12.4. Executable Files
/usr/bin/chattr  
/usr/bin/lsattr  
/usr/sbin/badblocks  
/usr/sbin/debugfs  
/usr/sbin/dumpe2fs  
/usr/sbin/e2freefrag  
/usr/sbin/e2fsck  
/usr/sbin/e2image  
/usr/sbin/e2label  
/usr/sbin/e2mmpstatus  
/usr/sbin/e2scrub  
/usr/sbin/e2scrub_all  
/usr/sbin/e2undo  
/usr/sbin/e4crypt  
/usr/sbin/e4defrag  
/usr/sbin/filefrag  
/usr/sbin/fsck.ext2  
/usr/sbin/fsck.ext3  
/usr/sbin/fsck.ext4  
/usr/sbin/mke2fs  
/usr/sbin/mkfs.ext2  
/usr/sbin/mkfs.ext3  
/usr/sbin/mkfs.ext4  
/usr/sbin/mklost+found  
/usr/sbin/resize2fs  
/usr/sbin/tune2fs  

<br>

### 1.13 findutils Package
#### 1.13.1. Official Package Description
utilities for finding files--find, xargs  
GNU findutils provides utilities to find files meeting specified  
criteria and perform various actions on the files which are found.  
This package contains 'find' and 'xargs'; however, 'locate' has  
been split off into a separate package.  

#### 1.13.2. Depended Packages
libc6  
libselinux1  

#### 1.13.3. Configuration Files
(None)

#### 1.13.4. Executable Files
/usr/bin/find  
/usr/bin/xargs  

<br>

### 1.14 gcc-14-base Package
#### 1.14.1. Official Package Description
GCC, the GNU Compiler Collection (base package)  
This package contains files common to all languages and libraries  
contained in the GNU Compiler Collection (GCC).  

#### 1.14.2. Depended Packages
(None)

#### 1.14.3. Configuration Files
(None)

#### 1.14.4. Executable Files
(None)

<br>

### 1.15 grep Package
#### 1.15.1. Official Package Description
GNU grep, egrep and fgrep  
grep is a utility to search for text in files; it can be used from the  
command line or in scripts.  Even if you dont want to use it, other packages  
on your system probably will.  
.  
The GNU family of grep utilities may be the "fastest grep in the west".  
GNU grep is based on a fast lazy-state deterministic matcher (about  
twice as fast as stock Unix egrep) hybridized with a Boyer-Moore-Gosper  
search for a fixed string that eliminates impossible text from being  
considered by the full regexp matcher without necessarily having to  
look at every character. The result is typically many times faster  
than Unix grep or egrep. (Regular expressions containing backreferencing  
will run more slowly, however.)  

#### 1.15.2. Depended Packages
libc6  
libpcre2-8-0  

#### 1.15.3. Configuration Files
(None)

#### 1.15.4. Executable Files
/usr/bin/egrep  
/usr/bin/fgrep  
/usr/bin/grep  
/usr/bin/rgrep  

<br>

### 1.16 gzip Package
#### 1.16.1. Official Package Description
GNU compression utilities  
This package provides the standard GNU file compression utilities, which  
are also the default compression tools for Debian.  They typically operate  
on files with names ending in '.gz', but can also decompress files ending  
in '.Z' created with 'compress'.  

#### 1.16.2. Depended Packages
dpkg  
libc6  

#### 1.16.3. Configuration Files
(None)

#### 1.16.4. Executable Files
/usr/bin/gunzip  
/usr/bin/gzexe  
/usr/bin/gzip  
/usr/bin/uncompress  
/usr/bin/zcat  
/usr/bin/zcmp  
/usr/bin/zdiff  
/usr/bin/zegrep  
/usr/bin/zfgrep  
/usr/bin/zforce  
/usr/bin/zgrep  
/usr/bin/zless  
/usr/bin/zmore  
/usr/bin/znew  

<br>

### 1.17 hostname Package
#### 1.17.1. Official Package Description
utility to set/show the host name or domain name  
This package provides commands which can be used to display the system's  
DNS name, and to display or set its hostname or NIS domain name.  

#### 1.17.2. Depended Packages
libc6  

#### 1.17.3. Configuration Files
(None)

#### 1.17.4. Executable Files
/usr/bin/dnsdomainname  
/usr/bin/domainname  
/usr/bin/hostname  
/usr/bin/nisdomainname  
/usr/bin/ypdomainname  

<br>

### 1.18 init-system-helpers Package
#### 1.18.1. Official Package Description
helper tools for all init systems  
This package contains helper tools that are necessary for switching between  
the various init systems that Debian contains (e. g. sysvinit or  
systemd). An example is deb-systemd-helper, a script that enables systemd unit  
files without depending on a running systemd.  
.  
It also includes the "service", "invoke-rc.d", and "update-rc.d" scripts which  
provide an abstraction for enabling, disabling, starting, and stopping  
services for all supported Debian init systems as specified by the policy.  
.  
While this package is maintained by pkg-systemd-maintainers, it is NOT  
specific to systemd at all. Maintainers of other init systems are welcome to  
include their helpers in this package.  

#### 1.18.2. Depended Packages
(None)

#### 1.18.3. Configuration Files
(None)

#### 1.18.4. Executable Files
/usr/bin/deb-systemd-helper  
/usr/bin/deb-systemd-invoke  
/usr/sbin/invoke-rc.d  
/usr/sbin/service  
/usr/sbin/update-rc.d  

<br>

### 1.19 libacl1 Package
#### 1.19.1. Official Package Description
access control list - shared library  
This package contains the shared library containing the POSIX 1003.1e  
draft standard 17 functions for manipulating access control lists.  

#### 1.19.2. Depended Packages
libc6  

#### 1.19.3. Configuration Files
(None)

#### 1.19.4. Executable Files
(None)

<br>

### 1.20 libattr1 Package
#### 1.20.1. Official Package Description
extended attribute handling - shared library  
Contains the runtime environment required by programs that make use  
of extended attributes.  

#### 1.20.2. Depended Packages
libc6  

#### 1.20.3. Configuration Files
/etc/xattr.conf  

#### 1.20.4. Executable Files
(None)

<br>

### 1.21 libaudit-common Package
#### 1.21.1. Official Package Description
Dynamic library for security auditing - common files  
The audit-libs package contains the dynamic libraries needed for  
applications to use the audit framework. It is used to monitor systems for  
security related events.  
.  
This package contains the libaudit.conf configuration file and the associated  
manpage.  

#### 1.21.2. Depended Packages
(None)

#### 1.21.3. Configuration Files
/etc/libaudit.conf  

#### 1.21.4. Executable Files
(None)

<br>

### 1.22 libaudit1 Package
#### 1.22.1. Official Package Description
Dynamic library for security auditing  
The audit-libs package contains the dynamic libraries needed for  
applications to use the audit framework. It is used to monitor systems for  
security related events.  

#### 1.22.2. Depended Packages
libaudit-common  
libc6  
libcap-ng0  

#### 1.22.3. Configuration Files
(None)

#### 1.22.4. Executable Files
(None)

<br>

### 1.23 libblkid1 Package
#### 1.23.1. Official Package Description
block device ID library  
The blkid library allows system programs such as fsck and mount to  
quickly and easily find block devices by filesystem UUID or label.  
This allows system administrators to avoid specifying filesystems by  
hard-coded device names and use a logical naming system instead.  

#### 1.23.2. Depended Packages
libc6  

#### 1.23.3. Configuration Files
(None)

#### 1.23.4. Executable Files
(None)

<br>

### 1.24 libbz2-1.0 Package
#### 1.24.1. Official Package Description
high-quality block-sorting file compressor library - runtime  
This package contains libbzip2 which is used by the bzip2 compressor.  
.  
bzip2 is a freely available, patent free, data compressor.  
.  
bzip2 compresses files using the Burrows-Wheeler block-sorting text  
compression algorithm, and Huffman coding.  Compression is generally  
considerably better than that achieved by more conventional  
LZ77/LZ78-based compressors, and approaches the performance of the PPM  
family of statistical compressors.  
.  
The archive file format of bzip2 (.bz2) is incompatible with that of its  
predecessor, bzip (.bz).  

#### 1.24.2. Depended Packages
libc6  

#### 1.24.3. Configuration Files
(None)

#### 1.24.4. Executable Files
(None)

<br>

### 1.25 libc-bin Package
#### 1.25.1. Official Package Description
GNU C Library: Binaries  
This package contains utility programs related to the GNU C Library.  
.  
getconf: query system configuration variables  
getent: get entries from administrative databases  
iconv, iconvconfig: convert between character encodings  
ldd, ldconfig: print/configure shared library dependencies  
locale, localedef: show/generate locale definitions  
tzselect, zdump, zic: select/dump/compile time zones  

#### 1.25.2. Depended Packages
libc6  

#### 1.25.3. Configuration Files
/etc/bindresvport.blacklist  
/etc/gai.conf  
/etc/ld.so.conf  
/etc/ld.so.conf.d/libc.conf  

#### 1.25.4. Executable Files
/usr/bin/getconf  
/usr/bin/getent  
/usr/bin/iconv  
/usr/bin/ld.so  
/usr/bin/ldd  
/usr/bin/locale  
/usr/bin/localedef  
/usr/bin/pldd  
/usr/bin/tzselect  
/usr/bin/zdump  
/usr/sbin/iconvconfig  
/usr/sbin/ldconfig  
/usr/sbin/ldconfig.real  
/usr/sbin/zic  

<br>

### 1.26 libc6 Package
#### 1.26.1. Official Package Description
GNU C Library: Shared libraries  
Contains the standard libraries that are used by nearly all programs on  
the system. This package includes shared versions of the standard C library  
and the standard math library, as well as many others.  

#### 1.26.2. Depended Packages
libgcc-s1  

#### 1.26.3. Configuration Files
/etc/ld.so.conf.d/x86_64-linux-gnu.conf  

#### 1.26.4. Executable Files
(None)

<br>

### 1.27 libcap-ng0 Package
#### 1.27.1. Official Package Description
alternate POSIX capabilities library  
This library implements the user-space interfaces to the POSIX  
1003.1e capabilities available in Linux kernels.  These capabilities are  
a partitioning of the all powerful root privilege into a set of distinct  
privileges.  
.  
The libcap-ng library is intended to make programming with POSIX  
capabilities much easier than the traditional libcap library.  
.  
This package contains dynamic libraries for libcap-ng.  

#### 1.27.2. Depended Packages
libc6  

#### 1.27.3. Configuration Files
(None)

#### 1.27.4. Executable Files
(None)

<br>

### 1.28 libcap2 Package
#### 1.28.1. Official Package Description
POSIX 1003.1e capabilities (library)  
Libcap implements the user-space interfaces to the POSIX 1003.1e capabilities  
available in Linux kernels. These capabilities are a partitioning of the all  
powerful root privilege into a set of distinct privileges.  
.  
This package contains the shared library.  

#### 1.28.2. Depended Packages
libc6  

#### 1.28.3. Configuration Files
(None)

#### 1.28.4. Executable Files
(None)

<br>

### 1.29 libcom-err2 Package
#### 1.29.1. Official Package Description
common error description library  
libcomerr is an attempt to present a common error-handling mechanism to  
manipulate the most common form of error code in a fashion that does not  
have the problems identified with mechanisms commonly in use.  

#### 1.29.2. Depended Packages
libc6  

#### 1.29.3. Configuration Files
(None)

#### 1.29.4. Executable Files
(None)

<br>

### 1.30 libcrypt1 Package
#### 1.30.1. Official Package Description
libcrypt shared library  
libxcrypt is a modern library for one-way hashing of passwords.  
It supports DES, MD5, NTHASH, SUNMD5, SHA-2-256, SHA-2-512, and  
bcrypt-based password hashes  
It provides the traditional Unix 'crypt' and 'crypt_r' interfaces,  
as well as a set of extended interfaces like 'crypt_gensalt'.  

#### 1.30.2. Depended Packages
libc6  

#### 1.30.3. Configuration Files
(None)

#### 1.30.4. Executable Files
(None)

<br>

### 1.31 libdb5.3 Package
#### 1.31.1. Official Package Description
Berkeley v5.3 Database Libraries [runtime]
This is the runtime package for programs that use the v5.3 Berkeley  
database library.  

#### 1.31.2. Depended Packages
libc6  

#### 1.31.3. Configuration Files
(None)

#### 1.31.4. Executable Files
(None)

<br>

### 1.32 libdebconfclient0 Package
#### 1.32.1. Official Package Description
Debian Configuration Management System (C-implementation library)  
Debconf is a configuration management system for Debian packages. It is  
used by some packages to prompt you for information before they are  
installed. cdebconf is a reimplementation of the original debconf in C.  
.  
This library allows C programs to interface with cdebconf.  

#### 1.32.2. Depended Packages
libc6  

#### 1.32.3. Configuration Files
(None)

#### 1.32.4. Executable Files
(None)

<br>

### 1.33 libext2fs2 Package
#### 1.33.1. Official Package Description

#### 1.33.2. Depended Packages
libc6  

#### 1.33.3. Configuration Files
(None)

#### 1.33.4. Executable Files
(None)

<br>

### 1.34 libext2fs2t64 Package
#### 1.34.1. Official Package Description
ext2/ext3/ext4 file system libraries  
The ext2, ext3 and ext4 file systems are successors of the original ext  
("extended") file system. They are the main file system types used for  
hard disks on Debian and other Linux systems.  
.  
This package provides the ext2fs and e2p libraries, for userspace software  
that directly accesses extended file systems. Programs that use libext2fs  
include e2fsck, mke2fs, and tune2fs. Programs that use libe2p include  
dumpe2fs, chattr, and lsattr.  

#### 1.34.2. Depended Packages
libc6  

#### 1.34.3. Configuration Files
(None)

#### 1.34.4. Executable Files
(None)

<br>

### 1.35 libgcc-s1 Package
#### 1.35.1. Official Package Description
GCC support library  
Shared version of the support library, a library of internal subroutines  
that GCC uses to overcome shortcomings of particular machines, or  
special needs for some languages.  

#### 1.35.2. Depended Packages
gcc-14-base  
libc6  

#### 1.35.3. Configuration Files
(None)

#### 1.35.4. Executable Files
(None)

<br>

### 1.36 libgcrypt20 Package
#### 1.36.1. Official Package Description
LGPL Crypto library - runtime library  
libgcrypt contains cryptographic functions.  Many important free  
ciphers, hash algorithms and public key signing algorithms have been  
implemented:  
.  
Arcfour, Blowfish, CAST5, DES, AES, Twofish, Serpent, rfc2268 (rc2), SEED,  
Poly1305, Camellia, ChaCha20, IDEA, Salsa, SM4, Blake-2, CRC, MD2, MD4, MD5,  
RIPE-MD160, SM3, SHA-1, SHA-256, SHA-512, SHA3-224, SHA3-256, SHA3-384,  
SHA3-512, SHAKE128, SHAKE256, Tiger, Whirlpool, DSA, DSA2, ElGamal, RSA, ECC  
(Curve25519, sec256k1, GOST R 34.10-2001 and GOST R 34.10-2012, etc.)  

#### 1.36.2. Depended Packages
libc6  
libgpg-error0  

#### 1.36.3. Configuration Files
(None)

#### 1.36.4. Executable Files
(None)

<br>

### 1.37 libgmp10 Package
#### 1.37.1. Official Package Description
Multiprecision arithmetic library  
GNU MP is a programmer's library for arbitrary precision  
arithmetic (ie, a bignum package).  It can operate on signed  
integer, rational, and floating point numeric types.  
.  
It has a rich set of functions, and the functions have a regular  
interface.  

#### 1.37.2. Depended Packages
libc6  

#### 1.37.3. Configuration Files
(None)

#### 1.37.4. Executable Files
(None)

<br>

### 1.38 libgpg-error0 Package
#### 1.38.1. Official Package Description
GnuPG development runtime library  
Library that defines common error values, messages, and common  
runtime functionality for all GnuPG components.  Among these are GPG,  
GPGSM, GPGME, GPG-Agent, libgcrypt, pinentry, SmartCard Daemon and  
possibly more in the future.  
.  
It will likely be renamed "gpgrt" in the future.  

#### 1.38.2. Depended Packages
libc6  

#### 1.38.3. Configuration Files
(None)

#### 1.38.4. Executable Files
(None)

<br>

### 1.39 liblz4-1 Package
#### 1.39.1. Official Package Description
Fast LZ compression algorithm library - runtime  
LZ4 is a very fast lossless compression algorithm, providing compression speed  
at 400 MB/s per core, scalable with multi-cores CPU. It also features an  
extremely fast decoder, with speed in multiple GB/s per core, typically  
reaching RAM speed limits on multi-core systems.  
.  
This package includes the shared library.  

#### 1.39.2. Depended Packages
libc6  

#### 1.39.3. Configuration Files
(None)

#### 1.39.4. Executable Files
(None)

<br>

### 1.40 liblzma5 Package
#### 1.40.1. Official Package Description
XZ-format compression library  
XZ is the successor to the Lempel-Ziv/Markov-chain Algorithm  
compression format, which provides memory-hungry but powerful  
compression (often better than bzip2) and fast, easy decompression.  
.  
The native format of liblzma is XZ; it also supports raw (headerless)  
streams and the older LZMA format used by lzma. (For 7-Zip's related  
format, use the p7zip package instead.)  

#### 1.40.2. Depended Packages
libc6  

#### 1.40.3. Configuration Files
(None)

#### 1.40.4. Executable Files
(None)

<br>

### 1.41 libmd0 Package
#### 1.41.1. Official Package Description
message digest functions from BSD systems - shared library  
The libmd library provides various message digest ("hash") functions,  
as found on various BSDs on a library with the same name and with a  
compatible API.  

#### 1.41.2. Depended Packages
libc6  

#### 1.41.3. Configuration Files
(None)

#### 1.41.4. Executable Files
(None)

<br>

### 1.42 libmount1 Package
#### 1.42.1. Official Package Description
device mounting library  
This device mounting library is used by mount and umount helpers.  

#### 1.42.2. Depended Packages
libblkid1  
libc6  
libselinux1  

#### 1.42.3. Configuration Files
(None)

#### 1.42.4. Executable Files
(None)

<br>

### 1.43 libncursesw6 Package
#### 1.43.1. Official Package Description
shared libraries for terminal handling (wide character support)  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains the shared libraries necessary to run programs  
compiled with ncursesw, which includes support for wide characters.  

#### 1.43.2. Depended Packages
libc6  
libtinfo6  

#### 1.43.3. Configuration Files
(None)

#### 1.43.4. Executable Files
(None)

<br>

### 1.44 libpam-modules Package
#### 1.44.1. Official Package Description
Pluggable Authentication Modules for PAM  
This package completes the set of modules for PAM. It includes the  
pam_unix.so module as well as some specialty modules.  

#### 1.44.2. Depended Packages
debconf  
libaudit1  
libc6  
libcrypt1  
libpam-modules-bin  
libpam0g  
libselinux1  
libsystemd0  

#### 1.44.3. Configuration Files
/etc/security/access.conf  
/etc/security/faillock.conf  
/etc/security/group.conf  
/etc/security/limits.conf  
/etc/security/namespace.conf  
/etc/security/namespace.init  
/etc/security/pam_env.conf  
/etc/security/pwhistory.conf  
/etc/security/sepermit.conf  
/etc/security/time.conf  

#### 1.44.4. Executable Files
(None)

<br>

### 1.45 libpam-modules-bin Package
#### 1.45.1. Official Package Description
Pluggable Authentication Modules for PAM - helper binaries  
This package contains helper binaries used by the standard set of PAM  
modules in the libpam-modules package.  

#### 1.45.2. Depended Packages
libaudit1  
libc6  
libcrypt1  
libpam0g  
libselinux1  
libsystemd0  

#### 1.45.3. Configuration Files
(None)

#### 1.45.4. Executable Files
/usr/sbin/faillock  
/usr/sbin/mkhomedir_helper  
/usr/sbin/pam_extrausers_chkpwd  
/usr/sbin/pam_extrausers_update  
/usr/sbin/pam_namespace_helper  
/usr/sbin/pam_timestamp_check  
/usr/sbin/pwhistory_helper  
/usr/sbin/unix_chkpwd  
/usr/sbin/unix_update  

<br>

### 1.46 libpam-runtime Package
#### 1.46.1. Official Package Description
Runtime support for the PAM library  
Contains configuration files and  directories required for  
authentication  to work on Debian systems.  This package is required  
on almost all installations.  

#### 1.46.2. Depended Packages
debconf  
libpam-modules  

#### 1.46.3. Configuration Files
/etc/pam.conf  
/etc/pam.d/other  

#### 1.46.4. Executable Files
/usr/sbin/pam-auth-update  
/usr/sbin/pam_getenv  

<br>

### 1.47 libpam0g Package
#### 1.47.1. Official Package Description
Pluggable Authentication Modules library  
Contains the shared library for Linux-PAM, a library that enables the  
local system administrator to choose how applications authenticate users.  
In other words, without rewriting or recompiling a PAM-aware application,  
it is possible to switch between the authentication mechanism(s) it uses.  
One may entirely upgrade the local authentication system without touching  
the applications themselves.  

#### 1.47.2. Depended Packages
debconf  
libaudit1  
libc6  

#### 1.47.3. Configuration Files
(None)

#### 1.47.4. Executable Files
(None)

<br>

### 1.48 libpcre2-8-0 Package
#### 1.48.1. Official Package Description
New Perl Compatible Regular Expression Library- 8 bit runtime files  
This is PCRE2, the new implementation of PCRE, a library of functions  
to support regular expressions whose syntax and semantics are as  
close as possible to those of the Perl 5 language. New projects  
should use this library in preference to the older library,  
confusingly called pcre3 in Debian.  
.  
This package contains the 8 bit runtime library, which operates on  
ASCII and UTF-8 input.  

#### 1.48.2. Depended Packages
libc6  

#### 1.48.3. Configuration Files
(None)

#### 1.48.4. Executable Files
(None)

<br>

### 1.49 libproc2-0 Package
#### 1.49.1. Official Package Description
library for accessing process information from /proc  
The libproc2 library is a way of accessing information out of the /proc  
filesystem.  
.  
This package contains the shared libraries necessary to run programs  
compiled with libproc2.  

#### 1.49.2. Depended Packages
libc6  
libsystemd0  

#### 1.49.3. Configuration Files
(None)

#### 1.49.4. Executable Files
(None)

<br>

### 1.50 libselinux1 Package
#### 1.50.1. Official Package Description
SELinux runtime shared libraries  
This package provides the shared libraries for Security-enhanced  
Linux that provides interfaces (e.g. library functions for the  
SELinux kernel APIs like getcon(), other support functions like  
getseuserbyname()) to SELinux-aware applications. Security-enhanced  
Linux is a patch of the Linux kernel and a number of utilities with  
enhanced security functionality designed to add mandatory access  
controls to Linux.  The Security-enhanced Linux kernel contains new  
architectural components originally developed to improve the security  
of the Flask operating system. These architectural components provide  
general support for the enforcement of many kinds of mandatory access  
control policies, including those based on the concepts of Type  
Enforcement, Role-based Access Control, and Multi-level Security.  
.  
libselinux1 provides an API for SELinux applications to get and set  
process and file security contexts and to obtain security policy  
decisions.  Required for any applications that use the SELinux  
API. libselinux may use the shared libsepol to manipulate the binary  
policy if necessary (e.g. to downgrade the policy format to an older  
version supported by the kernel) when loading policy.  

#### 1.50.2. Depended Packages
libc6  
libpcre2-8-0  

#### 1.50.3. Configuration Files
(None)

#### 1.50.4. Executable Files
(None)

<br>

### 1.51 libsemanage-common Package
#### 1.51.1. Official Package Description
Common files for SELinux policy management libraries  
This package provides the common files used by the shared libraries  
for SELinux policy management.  
.  
Security-enhanced Linux is a patch of the Linux kernel and a  
number of utilities with enhanced security functionality designed to  
add mandatory access controls to Linux.  The Security-enhanced Linux  
kernel contains new architectural components originally developed to  
improve the security of the Flask operating system. These  
architectural components provide general support for the enforcement  
of many kinds of mandatory access control policies, including those  
based on the concepts of Type Enforcement, Role-based Access  
Control, and Multi-level Security.  

#### 1.51.2. Depended Packages
(None)

#### 1.51.3. Configuration Files
/etc/selinux/semanage.conf  

#### 1.51.4. Executable Files
(None)

<br>

### 1.52 libsemanage2 Package
#### 1.52.1. Official Package Description
SELinux policy management library  
This package provides the shared libraries for SELinux policy management.  
It uses libsepol for binary policy manipulation and libselinux for  
interacting with the SELinux system.  It also exec's helper programs  
for loading policy and for checking whether the file_contexts  
configuration is valid (load_policy and setfiles from  
policycoreutils) presently, although this may change at least for the  
bootstrapping case  
.  
Security-enhanced Linux is a patch of the Linux kernel and a  
number of utilities with enhanced security functionality designed to  
add mandatory access controls to Linux.  The Security-enhanced Linux  
kernel contains new architectural components originally developed to  
improve the security of the Flask operating system. These  
architectural components provide general support for the enforcement  
of many kinds of mandatory access control policies, including those  
based on the concepts of Type Enforcement, Role-based Access  
Control, and Multi-level Security.  

#### 1.52.2. Depended Packages
libaudit1  
libbz2-1.0  
libc6  
libselinux1  
libsemanage-common  
libsepol2  

#### 1.52.3. Configuration Files
(None)

#### 1.52.4. Executable Files
(None)

<br>

### 1.53 libsepol2 Package
#### 1.53.1. Official Package Description
SELinux library for manipulating binary security policies  
Security-enhanced Linux is a patch of the Linux kernel and a number  
of utilities with enhanced security functionality designed to add  
mandatory access controls to Linux.  The Security-enhanced Linux  
kernel contains new architectural components originally developed to  
improve the security of the Flask operating system. These  
architectural components provide general support for the enforcement  
of many kinds of mandatory access control policies, including those  
based on the concepts of Type Enforcement\xc2\xae, Role-based Access  
Control, and Multi-level Security.  
.  
libsepol provides an API for the manipulation of SELinux binary policies.  
It is used by checkpolicy (the policy compiler) and similar tools, as well  
as by programs like load_policy that need to perform specific transformations  
on binary policies such as customizing policy boolean settings.  

#### 1.53.2. Depended Packages
libc6  

#### 1.53.3. Configuration Files
(None)

#### 1.53.4. Executable Files
(None)

<br>

### 1.54 libsmartcols1 Package
#### 1.54.1. Official Package Description
smart column output alignment library  
This smart column output alignment library is used by fdisk utilities.  

#### 1.54.2. Depended Packages
libc6  

#### 1.54.3. Configuration Files
(None)

#### 1.54.4. Executable Files
(None)

<br>

### 1.55 libss2 Package
#### 1.55.1. Official Package Description
command-line interface parsing library  
libss provides a simple command-line interface parser which will  
accept input from the user, parse the command into an argv argument  
vector, and then dispatch it to a handler function.  
.  
It was originally inspired by the Multics SubSystem library.  

#### 1.55.2. Depended Packages
libc6  
libcom-err2  

#### 1.55.3. Configuration Files
(None)

#### 1.55.4. Executable Files
(None)

<br>

### 1.56 libssl3 Package
#### 1.56.1. Official Package Description
Secure Sockets Layer toolkit - shared libraries  
This package is part of the OpenSSL project's implementation of the SSL  
and TLS cryptographic protocols for secure communication over the  
Internet.  

#### 1.56.2. Depended Packages
libc6  

#### 1.56.3. Configuration Files
(None)

#### 1.56.4. Executable Files
(None)

<br>

### 1.57 libssl3t64 Package
#### 1.57.1. Official Package Description
Secure Sockets Layer toolkit - shared libraries  
This package is part of the OpenSSL project's implementation of the SSL  
and TLS cryptographic protocols for secure communication over the  
Internet.  
.  
It provides the libssl and libcrypto shared libraries.  

#### 1.57.2. Depended Packages
libc6  

#### 1.57.3. Configuration Files
(None)

#### 1.57.4. Executable Files
(None)

<br>

### 1.58 libsystemd0 Package
#### 1.58.1. Official Package Description
systemd utility library  
This library provides APIs to interface with various system components such as  
the system journal, the system service manager, D-Bus and more.  

#### 1.58.2. Depended Packages
libc6  
libcap2  
libgcrypt20  
liblz4-1  
liblzma5  
libzstd1  

#### 1.58.3. Configuration Files
(None)

#### 1.58.4. Executable Files
(None)

<br>

### 1.59 libtinfo6 Package
#### 1.59.1. Official Package Description
shared low-level terminfo library for terminal handling  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains the shared low-level terminfo library.  

#### 1.59.2. Depended Packages
libc6  

#### 1.59.3. Configuration Files
(None)

#### 1.59.4. Executable Files
(None)

<br>

### 1.60 libudev1 Package
#### 1.60.1. Official Package Description
libudev shared library  
This library provides APIs to introspect and enumerate devices on the local  
system.  

#### 1.60.2. Depended Packages
libc6  
libcap2  

#### 1.60.3. Configuration Files
(None)

#### 1.60.4. Executable Files
(None)

<br>

### 1.61 libuuid1 Package
#### 1.61.1. Official Package Description
Universally Unique ID library  
The libuuid library generates and parses 128-bit Universally Unique  
IDs (UUIDs). A UUID is an identifier that is unique within the space  
of all such identifiers across both space and time. It can be used for  
multiple purposes, from tagging objects with an extremely short lifetime  
to reliably identifying very persistent objects across a network.  
.  
See RFC 4122 for more information.  

#### 1.61.2. Depended Packages
libc6  

#### 1.61.3. Configuration Files
(None)

#### 1.61.4. Executable Files
(None)

<br>

### 1.62 libzstd1 Package
#### 1.62.1. Official Package Description
fast lossless compression algorithm  
Zstd, short for Zstandard, is a fast lossless compression algorithm, targeting  
real-time compression scenarios at zlib-level compression ratio.  
.  
This package contains the shared library.  

#### 1.62.2. Depended Packages
libc6  

#### 1.62.3. Configuration Files
(None)

#### 1.62.4. Executable Files
(None)

<br>

### 1.63 login Package
#### 1.63.1. Official Package Description
system login tools  
This package provides some required infrastructure for logins and for  
changing effective user or group IDs, including:  
login, the program that invokes a user shell on a virtual terminal;  
nologin, a dummy shell for disabled user accounts;  

#### 1.63.2. Depended Packages
libaudit1  
libc6  
libcrypt1  
libpam-modules  
libpam-runtime  
libpam0g  

#### 1.63.3. Configuration Files
/etc/login.defs  
/etc/pam.d/login  

#### 1.63.4. Executable Files
/usr/bin/faillog  
/usr/bin/lastlog  
/usr/bin/login  
/usr/bin/newgrp  
/usr/bin/sg  
/usr/sbin/nologin  

<br>

### 1.64 logsave Package
#### 1.64.1. Official Package Description
save the output of a command in a log file  
The logsave program will execute cmd_prog with the specified  
argument(s), and save a copy of its output to logfile.  If the  
containing directory for logfile does not exist, logsave will  
accumulate the output in memory until it can be written out.  A copy  
of the output will also be written to standard output.  

#### 1.64.2. Depended Packages
libc6  

#### 1.64.3. Configuration Files
(None)

#### 1.64.4. Executable Files
/usr/sbin/logsave  

<br>

### 1.65 mawk Package
#### 1.65.1. Official Package Description
Pattern scanning and text processing language  
Mawk is an interpreter for the AWK Programming Language. The AWK  
language is useful for manipulation of data files, text retrieval and  
processing, and for prototyping and experimenting with algorithms. Mawk  
is a new awk meaning it implements the AWK language as defined in Aho,  
Kernighan and Weinberger, The AWK Programming Language, Addison-Wesley  
Publishing, 1988. (Hereafter referred to as the AWK book.) Mawk conforms  
to the POSIX 1003.2 (draft 11.3) definition of the AWK language  
which contains a few features not described in the AWK book, and mawk  
provides a small number of extensions.  
.  
Mawk is smaller and much faster than gawk. It has some compile-time  
limits such as NF = 32767 and sprintf buffer = 1020.  

#### 1.65.2. Depended Packages
libc6  

#### 1.65.3. Configuration Files
(None)

#### 1.65.4. Executable Files
/usr/bin/mawk  

<br>

### 1.66 mount Package
#### 1.66.1. Official Package Description
tools for mounting and manipulating filesystems  
This package provides the mount(8), umount(8), swapon(8),  
swapoff(8), and losetup(8) commands.  

#### 1.66.2. Depended Packages
libblkid1  
libc6  
libmount1  
libselinux1  
libsmartcols1  

#### 1.66.3. Configuration Files
(None)

#### 1.66.4. Executable Files
/usr/bin/mount  
/usr/bin/umount  
/usr/sbin/losetup  
/usr/sbin/swapoff  
/usr/sbin/swapon  

<br>

### 1.67 ncurses-base Package
#### 1.67.1. Official Package Description
basic terminal type definitions  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains terminfo data files to support the most common types of  
terminal, including ansi, dumb, linux, rxvt, screen, sun, vt100, vt102, vt220,  
vt52, and xterm.  

#### 1.67.2. Depended Packages
(None)

#### 1.67.3. Configuration Files
/etc/terminfo/README  

#### 1.67.4. Executable Files
(None)

<br>

### 1.68 ncurses-bin Package
#### 1.68.1. Official Package Description
terminal-related programs and man pages  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains the programs used for manipulating the terminfo  
database and individual terminfo entries, as well as some programs for  
resetting terminals and such.  

#### 1.68.2. Depended Packages
libc6  
libtinfo6  

#### 1.68.3. Configuration Files
(None)

#### 1.68.4. Executable Files
/usr/bin/captoinfo  
/usr/bin/clear  
/usr/bin/infocmp  
/usr/bin/infotocap  
/usr/bin/reset  
/usr/bin/tabs  
/usr/bin/tic  
/usr/bin/toe  
/usr/bin/tput  
/usr/bin/tset  

<br>

### 1.69 passwd Package
#### 1.69.1. Official Package Description
change and administer password and group data  
This package includes passwd, chsh, chfn, and many other programs to  
maintain password and group data.  
.  
Shadow passwords are supported.  See /usr/share/doc/passwd/README.Debian  

#### 1.69.2. Depended Packages
libaudit1  
libc6  
libcrypt1  
libpam-modules  
libpam0g  
libselinux1  
libsemanage2  

#### 1.69.3. Configuration Files
/etc/default/useradd  
/etc/pam.d/chfn  
/etc/pam.d/chpasswd  
/etc/pam.d/chsh  
/etc/pam.d/newusers  
/etc/pam.d/passwd  

#### 1.69.4. Executable Files
/usr/bin/chage  
/usr/bin/chfn  
/usr/bin/chsh  
/usr/bin/expiry  
/usr/bin/gpasswd  
/usr/bin/passwd  
/usr/sbin/chgpasswd  
/usr/sbin/chpasswd  
/usr/sbin/cpgr  
/usr/sbin/cppw  
/usr/sbin/groupadd  
/usr/sbin/groupdel  
/usr/sbin/groupmems  
/usr/sbin/groupmod  
/usr/sbin/grpck  
/usr/sbin/grpconv  
/usr/sbin/grpunconv  
/usr/sbin/newusers  
/usr/sbin/pwck  
/usr/sbin/pwconv  
/usr/sbin/pwunconv  
/usr/sbin/shadowconfig  
/usr/sbin/useradd  
/usr/sbin/userdel  
/usr/sbin/usermod  
/usr/sbin/vigr  
/usr/sbin/vipw  

<br>

### 1.70 perl-base Package
#### 1.70.1. Official Package Description
minimal Perl system  
Perl is a scripting language used in many system scripts and utilities.  
.  
This package provides a Perl interpreter and the small subset of the  
standard run-time library required to perform basic tasks. For a full  
Perl installation, install "perl" (and its dependencies, "perl-modules-5.38"  
and "perl-doc").  

#### 1.70.2. Depended Packages
dpkg  
libc6  
libcrypt1  

#### 1.70.3. Configuration Files
(None)

#### 1.70.4. Executable Files
/usr/bin/perl  
/usr/bin/perl5.38.2  

<br>

### 1.71 procps Package
#### 1.71.1. Official Package Description
/proc file system utilities  
This package provides command line and full screen utilities for browsing  
procfs, a "pseudo" file system dynamically generated by the kernel to  
provide information about the status of entries in its process table  
(such as whether the process is running, stopped, or a "zombie").  
.  
It contains free, kill, pkill, pgrep, pmap, ps, pwdx, skill, slabtop,  
snice, sysctl, tload, top, uptime, vmstat, w, and watch.  

#### 1.71.2. Depended Packages
init-system-helpers  
libc6  
libncursesw6  
libproc2-0  
libsystemd0  
libtinfo6  

#### 1.71.3. Configuration Files
/etc/init.d/procps  
/etc/sysctl.conf  
/etc/sysctl.d/10-console-messages.conf  
/etc/sysctl.d/10-ipv6-privacy.conf  
/etc/sysctl.d/10-kernel-hardening.conf  
/etc/sysctl.d/10-magic-sysrq.conf  
/etc/sysctl.d/10-map-count.conf  
/etc/sysctl.d/10-network-security.conf  
/etc/sysctl.d/10-ptrace.conf  
/etc/sysctl.d/10-zeropage.conf  
/etc/sysctl.d/README.sysctl  

#### 1.71.4. Executable Files
/usr/bin/free  
/usr/bin/kill  
/usr/bin/pgrep  
/usr/bin/pidwait  
/usr/bin/pkill  
/usr/bin/pmap  
/usr/bin/ps  
/usr/bin/pwdx  
/usr/bin/skill  
/usr/bin/slabtop  
/usr/bin/snice  
/usr/bin/tload  
/usr/bin/top  
/usr/bin/uptime  
/usr/bin/vmstat  
/usr/bin/w  
/usr/bin/watch  
/usr/sbin/sysctl  

<br>

### 1.72 sed Package
#### 1.72.1. Official Package Description
GNU stream editor for filtering/transforming text  
sed reads the specified files or the standard input if no  
files are specified, makes editing changes according to a  
list of commands, and writes the results to the standard  
output.  

#### 1.72.2. Depended Packages
libacl1  
libc6  
libselinux1  

#### 1.72.3. Configuration Files
(None)

#### 1.72.4. Executable Files
/usr/bin/sed  

<br>

### 1.73 sensible-utils Package
#### 1.73.1. Official Package Description
Utilities for sensible alternative selection  
This package provides a number of small utilities which are used  
by programs to sensibly select and spawn an appropriate browser,  
editor, pager, or terminal emulator.  
.  
The specific utilities included are: sensible-browser sensible-editor  
sensible-pager sensible-terminal  

#### 1.73.2. Depended Packages
(None)

#### 1.73.3. Configuration Files
(None)

#### 1.73.4. Executable Files
/usr/bin/select-editor  
/usr/bin/sensible-browser  
/usr/bin/sensible-editor  
/usr/bin/sensible-pager  
/usr/bin/sensible-terminal  

<br>

### 1.74 sysvinit-utils Package
#### 1.74.1. Official Package Description
System-V-like utilities  
This package contains the important System-V-like utilities.  
.  
Specifically, this package includes:  
init-d-script, fstab-decode, killall5, pidof  
.  
It also contains the library scripts sourced by init-d-script and other  
initscripts that were formally in lsb-base.  

#### 1.74.2. Depended Packages
libc6  

#### 1.74.3. Configuration Files
(None)

#### 1.74.4. Executable Files
/usr/bin/pidof  
/usr/sbin/fstab-decode  
/usr/sbin/killall5  

<br>

### 1.75 tar Package
#### 1.75.1. Official Package Description
GNU version of the tar archiving utility  
Tar is a program for packaging a set of files as a single archive in tar  
format.  The function it performs is conceptually similar to cpio, and to  
things like PKZIP in the DOS world.  It is heavily used by the Debian package  
management system, and is useful for performing system backups and exchanging  
sets of files with others.  

#### 1.75.2. Depended Packages
libacl1  
libc6  
libselinux1  

#### 1.75.3. Configuration Files
/etc/rmt  

#### 1.75.4. Executable Files
/usr/bin/tar  
/usr/sbin/rmt-tar  
/usr/sbin/tarcat  

<br>

### 1.76 util-linux Package
#### 1.76.1. Official Package Description
miscellaneous system utilities  
This package contains a number of important utilities, most of which  
are oriented towards maintenance of your system. Some of the more  
important utilities included in this package allow you to view kernel  
messages, create new filesystems, view block device information,  
interface with real time clock, etc.  

#### 1.76.2. Depended Packages
libblkid1  
libc6  
libcap-ng0  
libcrypt1  
libmount1  
libpam0g  
libselinux1  
libsmartcols1  
libsystemd0  
libtinfo6  
libudev1  
libuuid1  
zlib1g  

#### 1.76.3. Configuration Files
/etc/pam.d/runuser  
/etc/pam.d/runuser-l  
/etc/pam.d/su  
/etc/pam.d/su-l  

#### 1.76.4. Executable Files
/usr/bin/addpart  
/usr/bin/choom  
/usr/bin/chrt  
/usr/bin/delpart  
/usr/bin/dmesg  
/usr/bin/fallocate  
/usr/bin/findmnt  
/usr/bin/flock  
/usr/bin/getopt  
/usr/bin/hardlink  
/usr/bin/i386  
/usr/bin/ionice  
/usr/bin/ipcmk  
/usr/bin/ipcrm  
/usr/bin/ipcs  
/usr/bin/last  
/usr/bin/lastb  
/usr/bin/linux32  
/usr/bin/linux64  
/usr/bin/lsblk  
/usr/bin/lscpu  
/usr/bin/lsipc  
/usr/bin/lslocks  
/usr/bin/lslogins  
/usr/bin/lsmem  
/usr/bin/lsns  
/usr/bin/mcookie  
/usr/bin/mesg  
/usr/bin/more  
/usr/bin/mountpoint  
/usr/bin/namei  
/usr/bin/nsenter  
/usr/bin/partx  
/usr/bin/prlimit  
/usr/bin/rename.ul  
/usr/bin/resizepart  
/usr/bin/rev  
/usr/bin/setarch  
/usr/bin/setpriv  
/usr/bin/setsid  
/usr/bin/setterm  
/usr/bin/su  
/usr/bin/taskset  
/usr/bin/uclampset  
/usr/bin/unshare  
/usr/bin/utmpdump  
/usr/bin/wdctl  
/usr/bin/whereis  
/usr/bin/x86_64  
/usr/sbin/agetty  
/usr/sbin/blkdiscard  
/usr/sbin/blkid  
/usr/sbin/blkzone  
/usr/sbin/blockdev  
/usr/sbin/chcpu  
/usr/sbin/chmem  
/usr/sbin/ctrlaltdel  
/usr/sbin/findfs  
/usr/sbin/fsck  
/usr/sbin/fsck.cramfs  
/usr/sbin/fsck.minix  
/usr/sbin/fsfreeze  
/usr/sbin/fstrim  
/usr/sbin/getty  
/usr/sbin/isosize  
/usr/sbin/ldattach  
/usr/sbin/mkfs  
/usr/sbin/mkfs.bfs  
/usr/sbin/mkfs.cramfs  
/usr/sbin/mkfs.minix  
/usr/sbin/mkswap  
/usr/sbin/pivot_root  
/usr/sbin/readprofile  
/usr/sbin/rtcwake  
/usr/sbin/runuser  
/usr/sbin/sulogin  
/usr/sbin/swaplabel  
/usr/sbin/switch_root  
/usr/sbin/wipefs  
/usr/sbin/zramctl  

<br>

### 1.77 zlib1g Package
#### 1.77.1. Official Package Description
compression library - runtime  
zlib is a library implementing the deflate compression method found  
in gzip and PKZIP.  This package includes the shared library.  

#### 1.77.2. Depended Packages
libc6  

#### 1.77.3. Configuration Files
(None)

#### 1.77.4. Executable Files
(None)

<br>

## 2. Important Packages
---
These are the important packages. You may expect them in (almost) every Ubuntu installation.

At my last check, the following packages are marked as important:

**adduser:** add and remove users and groups  
**apt:** commandline package manager  
**apt-utils:** package management related utility programs  
**ca-certificates:** Common CA certificates  
**console-setup:** console font and keymap setup program  
**console-setup-linux:** Linux specific part of console-setup  
**dbus:** simple interprocess messaging system (system message bus)  
**dbus-bin:** simple interprocess messaging system (command line utilities)  
**dbus-daemon:** simple interprocess messaging system (reference message bus)  
**dbus-session-bus-common:** simple interprocess messaging system (session bus configuration)  
**dbus-system-bus-common:** simple interprocess messaging system (system bus configuration)  
**dbus-user-session:** simple interprocess messaging system (systemd --user integration)  
**debconf-i18n:** full internationalization support for debconf  
**dhcpcd-base:** DHCPv4 and DHCPv6 dual-stack client (binaries and exit hooks)  
**distro-info:** provides information about the distributions' releases  
**distro-info-data:** information about the distributions' releases (data files)  
**dmsetup:** Linux Kernel Device Mapper userspace library  
**eject:** ejects CDs and operates CD-Changers under Linux  
**gir1.2-glib-2.0:** Introspection data for GLib, GObject, Gio and GModule  
**gpgv:** GNU privacy guard - signature verification tool  
**init:** metapackage ensuring an init system is installed  
**iproute2:** networking and traffic control tools  
**iputils-ping:** Tools to test the reachability of network hosts  
**iso-codes:** ISO language, territory, currency, script codes and their translations  
**kbd:** Linux console font and keytable utilities  
**keyboard-configuration:** system-wide keyboard preferences  
**kmod:** tools for managing Linux kernel modules  
**krb5-locales:** internationalization support for MIT Kerberos  
**less:** pager program similar to more  
**libapparmor1:** changehat AppArmor library  
**libapt-pkg6.0:**   
**libapt-pkg6.0t64:** package management runtime library  
**libargon2-1:** memory-hard hashing function - runtime library  
**libbpf1:** eBPF helper library (shared library)  
**libbsd0:** utility functions from BSD systems - shared library  
**libcap2-bin:** POSIX 1003.1e capabilities (utilities)  
**libcryptsetup12:** disk encryption support - shared library  
**libdb5.3t64:** Berkeley v5.3 Database Libraries [runtime]  
**libdbus-1-3:** simple interprocess messaging system (library)  
**libdevmapper1.02.1:** Linux Kernel Device Mapper userspace library  
**libelf1t64:** library to read and write ELF files  
**libestr0:** Helper functions for handling strings (lib)  
**libexpat1:** XML parsing C library - runtime library  
**libfastjson4:** fast json library for C  
**libfdisk1:** fdisk partitioning library  
**libffi8:** Foreign Function Interface library runtime  
**libfribidi0:** Free Implementation of the Unicode BiDi algorithm  
**libgirepository-1.0-1:** Library for handling GObject introspection data (runtime library)  
**libglib2.0-0t64:** GLib library of C routines  
**libglib2.0-data:** Common files for GLib library  
**libgnutls30:** GNU TLS library - main runtime library  
**libgnutls30t64:** GNU TLS library - main runtime library  
**libgssapi-krb5-2:** MIT Kerberos runtime libraries - krb5 GSS-API Mechanism  
**libhogweed6:** low level cryptographic library (public-key cryptos)  
**libhogweed6t64:** low level cryptographic library (public-key cryptos)  
**libicu74:** International Components for Unicode  
**libidn2-0:** Internationalized domain names (IDNA2008/TR46) library  
**libjson-c5:** JSON manipulation library - shared library  
**libk5crypto3:** MIT Kerberos runtime libraries - Crypto Library  
**libkeyutils1:** Linux Key Management Utilities (library)  
**libkmod2:** libkmod shared library  
**libkrb5-3:** MIT Kerberos runtime libraries  
**libkrb5support0:** MIT Kerberos runtime libraries - Support library  
**liblocale-gettext-perl:** module using libc functions for internationalization in Perl  
**libmnl0:** minimalistic Netlink communication library  
**libnetplan1:** Declarative network configuration runtime library  
**libnettle8:** low level cryptographic library (symmetric and one-way cryptos)  
**libnettle8t64:** low level cryptographic library (symmetric and one-way cryptos)  
**libnewt0.52:** Not Erik's Windowing Toolkit - text mode windowing with slang  
**libnss-systemd:** nss module providing dynamic user and group name resolution  
**libp11-kit0:** library for loading and coordinating access to PKCS#11 modules - runtime  
**libpam-cap:** POSIX 1003.1e capabilities (PAM module)  
**libpam-systemd:** system and service manager - PAM module  
**libpopt0:** lib for parsing cmdline parameters  
**libpython3-stdlib:** interactive high-level object-oriented language (default python3 version)  
**libpython3.12-minimal:** Minimal subset of the Python language (version 3.12)  
**libpython3.12-stdlib:** Interactive high-level object-oriented language (standard library, version 3.12)  
**libreadline8t64:** GNU readline and history libraries, run-time libraries  
**libseccomp2:** high level interface to Linux seccomp filter  
**libslang2:** S-Lang programming library - runtime version  
**libsqlite3-0:** SQLite 3 shared library  
**libstdc++6:** GNU Standard C++ Library v3  
**libsystemd-shared:** systemd shared private library  
**libtasn1-6:** Manage ASN.1 structures (runtime)  
**libtext-charwidth-perl:** get display widths of characters on the terminal  
**libtext-iconv-perl:** module to convert between character sets in Perl  
**libtext-wrapi18n-perl:** internationalized substitute of Text::Wrap  
**libtirpc-common:** transport-independent RPC library - common files  
**libtirpc3t64:** transport-independent RPC library  
**libunistring5:** Unicode string library for C  
**libxml2:** GNOME XML library  
**libxtables12:** netfilter xtables library  
**libxxhash0:** shared library for xxhash  
**libyaml-0-2:** Fast YAML 1.1 parser and emitter library  
**locales:** GNU C Library: National Language (locale) data [support]  
**logrotate:** Log rotation utility  
**lsb-release:** Linux Standard Base version reporting utility (minimal implementation)  
**media-types:** List of standard media types and their usual file extension  
**netbase:** Basic TCP/IP networking system  
**netcat-openbsd:** TCP/IP swiss army knife  
**netplan-generator:** Declarative network configuration systemd-generator  
**netplan.io:** Declarative network configuration for various backends  
**networkd-dispatcher:** Dispatcher service for systemd-networkd connection status changes  
**openssl:** Secure Sockets Layer toolkit - cryptographic utility  
**python-apt-common:** Python interface to libapt-pkg (locales)  
**python3:** interactive high-level object-oriented language (default python3 version)  
**python3-apt:** Python 3 interface to libapt-pkg  
**python3-cffi-backend:** Foreign Function Interface for Python 3 calling C code - runtime  
**python3-dbus:** simple interprocess messaging system (Python 3 interface)  
**python3-gi:** Python 3 bindings for gobject-introspection libraries  
**python3-markdown-it:** Python port of markdown-it and some its associated plugins  
**python3-mdurl:** Python port of the JavaScript mdurl package  
**python3-minimal:** minimal subset of the Python language (default python3 version)  
**python3-netifaces:** portable network interface information - Python 3.x  
**python3-netplan:** Declarative network configuration Python bindings  
**python3-pkg-resources:** Package Discovery and Resource Access using pkg_resources  
**python3-pygments:** syntax highlighting package written in Python 3  
**python3-rich:** render rich text, tables, progress bars, syntax highlighting, markdown and more  
**python3-yaml:** YAML parser and emitter for Python3  
**python3.12:** Interactive high-level object-oriented language (version 3.12)  
**python3.12-minimal:** Minimal subset of the Python language (version 3.12)  
**readline-common:** GNU readline and history libraries, common files  
**rsyslog:** reliable system and kernel logging daemon  
**shared-mime-info:** FreeDesktop.org shared MIME database and spec  
**sudo:** Provide limited super user privileges to specific users  
**systemd:** system and service manager  
**systemd-dev:** systemd development files  
**systemd-hwe-hwdb:** udev rules for hardware enablement (HWE)  
**systemd-resolved:** systemd DNS resolver  
**systemd-sysv:** system and service manager - SysV compatibility symlinks  
**systemd-timesyncd:** minimalistic service to synchronize local time with NTP servers  
**tzdata:** time zone and daylight-saving time data  
**ubuntu-keyring:** GnuPG keys of the Ubuntu archive  
**ubuntu-minimal:** Minimal core of Ubuntu  
**ubuntu-pro-client:** Management tools for Ubuntu Pro  
**ubuntu-pro-client-l10n:** Translations for Ubuntu Pro Client  
**ucf:** Update Configuration File(s): preserve user changes to config files  
**udev:** /dev/ and hotplug management daemon  
**vim-common:** Vi IMproved - Common files  
**vim-tiny:** Vi IMproved - enhanced vi editor - compact version  
**whiptail:** Displays user-friendly dialog boxes from shell scripts  
**xdg-user-dirs:** tool to manage well known user directories  
**xkb-data:** X Keyboard Extension (XKB) configuration data  
**xxd:** tool to make (or reverse) a hex dump  

<br>

### 2.1 adduser Package
#### 2.1.1. Official Package Description
add and remove users and groups  
This package includes the 'adduser' and 'deluser' commands for creating  
and removing users.  
.  
'adduser' creates new users and groups and adds existing users to  
existing groups;  
'deluser' removes users and groups and removes users from a given  
group.  
.  
Adding users with 'adduser' is much easier than adding them manually.  
'Adduser' will choose UID and GID values that conform to Debian policy,  
create a home directory, copy skeletal user configuration, and  
automate setting initial values for the user's password, real name  
and so on.  
.  
'Deluser' can back up and remove users' home directories  
and mail spool or all the files they own on the system.  
.  
A custom script can be executed after each of the commands.  
.  
'Adduser' and 'Deluser' are intended to be used by the local  
administrator in lieu of the tools from the 'useradd' suite, and  
they provide support for easy use from Debian package maintainer  
scripts, functioning as kind of a policy layer to make those scripts  
easier and more stable to write and maintain.  

#### 2.1.2. Depended Packages
passwd  

#### 2.1.3. Configuration Files
/etc/adduser.conf  
/etc/deluser.conf  

#### 2.1.4. Executable Files
/usr/sbin/addgroup  
/usr/sbin/adduser  
/usr/sbin/delgroup  
/usr/sbin/deluser  

<br>

### 2.2 apt Package
#### 2.2.1. Official Package Description
commandline package manager  
This package provides commandline tools for searching and  
managing as well as querying information about packages  
as a low-level access to all features of the libapt-pkg library.  
.  
These include:  
apt-get for retrieval of packages and information about them  
from authenticated sources and for installation, upgrade and  
removal of packages together with their dependencies  
apt-cache for querying available information about installed  
as well as installable packages  
apt-cdrom to use removable media as a source for packages  
apt-config as an interface to the configuration settings  
apt-key as an interface to manage authentication keys  

#### 2.2.2. Depended Packages
base-passwd  
gpgv  
libapt-pkg6.0t64  
libc6  
libgcc-s1  
libgnutls30t64  
libseccomp2  
libstdc++6  
libsystemd0  
ubuntu-keyring  

#### 2.2.3. Configuration Files
/etc/apt/apt.conf.d/01-vendor-ubuntu  
/etc/apt/apt.conf.d/01autoremove  
/etc/cron.daily/apt-compat  
/etc/logrotate.d/apt  

#### 2.2.4. Executable Files
/usr/bin/apt  
/usr/bin/apt-cache  
/usr/bin/apt-cdrom  
/usr/bin/apt-config  
/usr/bin/apt-get  
/usr/bin/apt-key  
/usr/bin/apt-mark  

<br>

### 2.3 apt-utils Package
#### 2.3.1. Official Package Description
package management related utility programs  
This package contains some less used commandline utilities related  
to package management with APT.  
.  
apt-extracttemplates is used by debconf to prompt for configuration  
questions before installation.  
apt-ftparchive is used to create Packages and other index files  
needed to publish an archive of Debian packages  
apt-sortpkgs is a Packages/Sources file normalizer.  

#### 2.3.2. Depended Packages
apt  
libapt-pkg6.0t64  
libc6  
libdb5.3t64  
libgcc-s1  
libstdc++6  

#### 2.3.3. Configuration Files
(None)

#### 2.3.4. Executable Files
/usr/bin/apt-extracttemplates  
/usr/bin/apt-ftparchive  
/usr/bin/apt-sortpkgs  

<br>

### 2.4 ca-certificates Package
#### 2.4.1. Official Package Description
Common CA certificates  
Contains the certificate authorities shipped with Mozilla's browser to allow  
SSL-based applications to check for the authenticity of SSL connections.  
.  
Please note that Debian can neither confirm nor deny whether the  
certificate authorities whose certificates are included in this package  
have in any way been audited for trustworthiness or RFC 3647 compliance.  
Full responsibility to assess them belongs to the local system  
administrator.  

#### 2.4.2. Depended Packages
debconf  
openssl  

#### 2.4.3. Configuration Files
(None)

#### 2.4.4. Executable Files
/usr/sbin/update-ca-certificates  

<br>

### 2.5 console-setup Package
#### 2.5.1. Official Package Description
console font and keymap setup program  
This package provides the console with the same keyboard  
configuration scheme as the X Window System. As a result, there is no  
need to duplicate or change the keyboard files just to make simple  
customizations such as the use of dead keys, the key functioning as  
AltGr or Compose key, the key(s) to switch between Latin and  
non-Latin mode, etc.  
.  
The package also installs console fonts supporting many of the  
world's languages.  It provides an unified set of font faces - the  
classic VGA, the simplistic Fixed, and the cleaned Terminus,  
TerminusBold and TerminusBoldVGA.  

#### 2.5.2. Depended Packages
console-setup-linux  
debconf  
keyboard-configuration  
xkb-data  

#### 2.5.3. Configuration Files
(None)

#### 2.5.4. Executable Files
/bin/setupcon  
/bin/setupcon  
/usr/bin/ckbcomp  
/usr/bin/ckbcomp  

<br>

### 2.6 console-setup-linux Package
#### 2.6.1. Official Package Description
Linux specific part of console-setup  
This package includes fonts in psf format and definitions of various  
8-bit charmaps.  

#### 2.6.2. Depended Packages
init-system-helpers  
kbd  
keyboard-configuration  

#### 2.6.3. Configuration Files
/etc/console-setup/compose.ARMSCII-8.inc  
/etc/console-setup/compose.CP1251.inc  
/etc/console-setup/compose.CP1255.inc  
/etc/console-setup/compose.CP1256.inc  
/etc/console-setup/compose.GEORGIAN-ACADEMY.inc  
/etc/console-setup/compose.GEORGIAN-PS.inc  
/etc/console-setup/compose.IBM1133.inc  
/etc/console-setup/compose.ISIRI-3342.inc  
/etc/console-setup/compose.ISO-8859-1.inc  
/etc/console-setup/compose.ISO-8859-10.inc  
/etc/console-setup/compose.ISO-8859-11.inc  
/etc/console-setup/compose.ISO-8859-13.inc  
/etc/console-setup/compose.ISO-8859-14.inc  
/etc/console-setup/compose.ISO-8859-15.inc  
/etc/console-setup/compose.ISO-8859-16.inc  
/etc/console-setup/compose.ISO-8859-2.inc  
/etc/console-setup/compose.ISO-8859-3.inc  
/etc/console-setup/compose.ISO-8859-4.inc  
/etc/console-setup/compose.ISO-8859-5.inc  
/etc/console-setup/compose.ISO-8859-6.inc  
/etc/console-setup/compose.ISO-8859-7.inc  
/etc/console-setup/compose.ISO-8859-8.inc  
/etc/console-setup/compose.ISO-8859-9.inc  
/etc/console-setup/compose.KOI8-R.inc  
/etc/console-setup/compose.KOI8-U.inc  
/etc/console-setup/compose.TIS-620.inc  
/etc/console-setup/compose.VISCII.inc  
/etc/console-setup/remap.inc  
/etc/console-setup/vtrgb  
/etc/console-setup/vtrgb.vga  
/etc/init.d/console-setup.sh  
/etc/init.d/keyboard-setup.sh  

#### 2.6.4. Executable Files
(None)

<br>

### 2.7 dbus Package
#### 2.7.1. Official Package Description
simple interprocess messaging system (system message bus)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
D-Bus supports broadcast messages, asynchronous messages (thus  
decreasing latency), authentication, and more. It is designed to be  
low-overhead; messages are sent using a binary protocol, not using  
XML. D-Bus also supports a method call mapping for its messages, but  
it is not required; this makes using the system quite simple.  
.  
It comes with several bindings, including GLib, Python, Qt and Java.  
.  
This package provides a fully-functional D-Bus system bus with activation  
support, used for communication between system services, and depends on  
most of the other components of the reference implementation of D-Bus.  
.  
To provide a complete D-Bus session bus, install one of the packages  
that implement the dbus-session-bus virtual package, such as  
dbus-user-session. The recommended implementation is indicated by  
the default-dbus-session-bus virtual package.  

#### 2.7.2. Depended Packages
dbus-bin  
dbus-daemon  
dbus-system-bus-common  
libc6  
libdbus-1-3  
libexpat1  
libsystemd0  

#### 2.7.3. Configuration Files
/etc/default/dbus  
/etc/init.d/dbus  

#### 2.7.4. Executable Files
(None)

<br>

### 2.8 dbus-bin Package
#### 2.8.1. Official Package Description
simple interprocess messaging system (command line utilities)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
This package contains the D-Bus command-line utilities such as dbus-send  
and dbus-monitor.  

#### 2.8.2. Depended Packages
libc6  
libdbus-1-3  

#### 2.8.3. Configuration Files
(None)

#### 2.8.4. Executable Files
/usr/bin/dbus-cleanup-sockets  
/usr/bin/dbus-monitor  
/usr/bin/dbus-send  
/usr/bin/dbus-update-activation-environment  
/usr/bin/dbus-uuidgen  

<br>

### 2.9 dbus-daemon Package
#### 2.9.1. Official Package Description
simple interprocess messaging system (reference message bus)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
This package contains dbus-daemon, the reference implementation of a  
D-Bus message bus, and dbus-run-session, a utility to start a temporary  
session dbus-daemon in a constrained environment or for automated tests.  
.  
To provide a complete D-Bus session bus, install one of the packages  
that implement the dbus-session-bus virtual package, such as  
dbus-user-session. The recommended implementation is indicated by  
the default-dbus-session-bus virtual package.  

#### 2.9.2. Depended Packages
dbus-bin  
dbus-session-bus-common  
libapparmor1  
libaudit1  
libc6  
libcap-ng0  
libdbus-1-3  
libexpat1  
libselinux1  
libsystemd0  

#### 2.9.3. Configuration Files
(None)

#### 2.9.4. Executable Files
/usr/bin/dbus-daemon  
/usr/bin/dbus-run-session  

<br>

### 2.10 dbus-session-bus-common Package
#### 2.10.1. Official Package Description
simple interprocess messaging system (session bus configuration)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
This package contains the configuration files defining the behaviour of  
the D-Bus session bus, used for applications and per-user services.  
These are used by the reference implementation in the dbus package,  
and by the reimplementation in the dbus-broker package.  
.  
To provide a complete D-Bus session bus, install one of the packages  
that implement the dbus-session-bus virtual package, such as  
dbus-user-session. The recommended implementation is indicated by  
the default-dbus-session-bus virtual package.  

#### 2.10.2. Depended Packages
(None)

#### 2.10.3. Configuration Files
(None)

#### 2.10.4. Executable Files
(None)

<br>

### 2.11 dbus-system-bus-common Package
#### 2.11.1. Official Package Description
simple interprocess messaging system (system bus configuration)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
This package contains the configuration files defining the behaviour of  
the D-Bus system bus, used for system services such as networking and  
storage management services. It is also responsible for creating the  
'messagebus' system user account used to run the system bus.  
These are used by the reference implementation in the dbus package,  
and by the reimplementation in the dbus-broker package.  
.  
To provide a complete D-Bus system bus, install one of the packages  
that implement the dbus-system-bus virtual package, such as dbus.  
The recommended implementation is indicated by the default-dbus-system-bus  
virtual package.  

#### 2.11.2. Depended Packages
adduser  

#### 2.11.3. Configuration Files
(None)

#### 2.11.4. Executable Files
(None)

<br>

### 2.12 dbus-user-session Package
#### 2.12.1. Official Package Description
simple interprocess messaging system (systemd --user integration)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
On systemd systems, this package opts in to the session model in which  
a users session starts the first time they log in, and does not end  
until all their login sessions have ended. This model merges all  
parallel non-graphical login sessions (text mode, ssh, cron, etc.), and up  
to one graphical session, into a single "user-session" or "super-session"  
within which all background D-Bus services are shared.  
.  
Multiple graphical sessions per user are not currently supported in this  
mode; as a result, it is particularly suitable for gdm, which responds to  
requests to open a parallel graphical session by switching to the existing  
graphical session and unlocking it.  
.  
To retain dbus traditional session semantics, in which login sessions  
are artificially isolated from each other, remove this package and install  
dbus-x11 instead.  
.  
See the dbus package description for more information about D-Bus in general.  

#### 2.12.2. Depended Packages
dbus-daemon  
dbus-session-bus-common  
libpam-systemd  
systemd  

#### 2.12.3. Configuration Files
/etc/X11/Xsession.d/20dbus_xdg-runtime  

#### 2.12.4. Executable Files
(None)

<br>

### 2.13 debconf-i18n Package
#### 2.13.1. Official Package Description
full internationalization support for debconf  
This package provides full internationalization for debconf, including  
translations into all available languages, support for using translated  
debconf templates, and support for proper display of multibyte character  
sets.  

#### 2.13.2. Depended Packages
debconf  
liblocale-gettext-perl  
libtext-charwidth-perl  
libtext-iconv-perl  
libtext-wrapi18n-perl  

#### 2.13.3. Configuration Files
(None)

#### 2.13.4. Executable Files
(None)

<br>

### 2.14 dhcpcd-base Package
#### 2.14.1. Official Package Description
DHCPv4 and DHCPv6 dual-stack client (binaries and exit hooks)  
dhcpcd provides seamless IPv4 and IPv6 auto-configuration:  
DHCPv4 client  
DHCPv6 client with Prefix Delegation (PD) support  
IPv4 LL support (ZeroConf)  
IPv6 SLAAC support  
ARP address conflict resolution  
ARP ping profiles  
Wireless SSID profiles  
.  
This package provides the binaries, exit hooks and manual pages.  
.  
It offers a dual-stack substitute for ISC DHCP Client (dhclient) on systems  
where interfaces are configured by ifupdown via </etc/network/interfaces>  
using the DHCP method.  
.  
The init.d script and systemd service required for systems without ifupdown  
are packaged separately as dhcpcd.  
.  
Since Debian 12 (Bookworm), dhcpcd uses Predictable Network Interface Names  
on Linux ports. See NEWS.Debian for more details.  

#### 2.14.2. Depended Packages
adduser  
libc6  
libssl3  
libudev1  

#### 2.14.3. Configuration Files
/etc/dhcpcd.conf  

#### 2.14.4. Executable Files
/usr/sbin/dhcpcd  

<br>

### 2.15 distro-info Package
#### 2.15.1. Official Package Description
provides information about the distributions' releases  
Information about all releases of Debian and Ubuntu. The distro-info script  
will give you the codename for e.g. the latest stable release of your  
distribution. To get information about a specific distribution there are the  
debian-distro-info and the ubuntu-distro-info scripts.  

#### 2.15.2. Depended Packages
distro-info-data  
libc6  

#### 2.15.3. Configuration Files
(None)

#### 2.15.4. Executable Files
/usr/bin/debian-distro-info  
/usr/bin/distro-info  
/usr/bin/ubuntu-distro-info  

<br>

### 2.16 distro-info-data Package
#### 2.16.1. Official Package Description
information about the distributions' releases (data files)  
Information about all releases of Debian and Ubuntu. The distro-info script  
will give you the codename for e.g. the latest stable release of your  
distribution. To get information about a specific distribution there are the  
debian-distro-info and the ubuntu-distro-info scripts.  
.  
This package contains the data files.  

#### 2.16.2. Depended Packages
(None)

#### 2.16.3. Configuration Files
(None)

#### 2.16.4. Executable Files
(None)

<br>

### 2.17 dmsetup Package
#### 2.17.1. Official Package Description
Linux Kernel Device Mapper userspace library  
The Linux Kernel Device Mapper is the LVM (Linux Logical Volume Management)  
Teams implementation of a minimalistic kernel-space driver that handles  
volume management, while keeping knowledge of the underlying device layout  
in user-space.  This makes it useful for not only LVM, but software raid,  
and other drivers that create "virtual" block devices.  
.  
This package contains a utility for modifying device mappings.  

#### 2.17.2. Depended Packages
libc6  
libdevmapper1.02.1  

#### 2.17.3. Configuration Files
(None)

#### 2.17.4. Executable Files
/usr/sbin/blkdeactivate  
/usr/sbin/dmsetup  
/usr/sbin/dmstats  

<br>

### 2.18 eject Package
#### 2.18.1. Official Package Description
ejects CDs and operates CD-Changers under Linux  
This program will eject CD-ROMs (assuming your drive supports the CDROMEJECT  
ioctl). It also allows setting the autoeject feature.  
.  
On supported ATAPI/IDE multi-disc CD-ROM changers, it allows changing  
the active disc.  
.  
You can also use eject to properly disconnect external mass-storage  
devices like digital cameras or portable music players.  

#### 2.18.2. Depended Packages
libc6  
libmount1  

#### 2.18.3. Configuration Files
(None)

#### 2.18.4. Executable Files
/usr/bin/eject  

<br>

### 2.19 gir1.2-glib-2.0 Package
#### 2.19.1. Official Package Description
Introspection data for GLib, GObject, Gio and GModule  
GObject Introspection is a project for providing machine readable  
introspection data of the API of C libraries. This introspection  
data can be used in several different use cases, for example  
automatic code generation for bindings, API verification and documentation  
generation.  
.  
This package contains the introspection data for the GLib, GObject,  
GModule and Gio libraries, in the typelib format used to generate  
bindings for dynamic languages like JavaScript and Python.  

#### 2.19.2. Depended Packages
libglib2.0-0t64  

#### 2.19.3. Configuration Files
(None)

#### 2.19.4. Executable Files
(None)

<br>

### 2.20 gpgv Package
#### 2.20.1. Official Package Description
GNU privacy guard - signature verification tool  
GnuPG is GNU's tool for secure communication and data storage.  
.  
gpgv is actually a stripped-down version of gpg which is only able  
to check signatures. It is somewhat smaller than the fully-blown gpg  
and uses a different (and simpler) way to check that the public keys  
used to make the signature are valid. There are no configuration  
files and only a few options are implemented.  

#### 2.20.2. Depended Packages
libassuan0  
libbz2-1.0  
libc6  
libgcrypt20  
libgpg-error0  
libnpth0t64  
zlib1g  

#### 2.20.3. Configuration Files
(None)

#### 2.20.4. Executable Files
/usr/bin/gpgv  

<br>

### 2.21 init Package
#### 2.21.1. Official Package Description
metapackage ensuring an init system is installed  
This package is a metapackage which allows you to select from the available  
init systems while ensuring that one of these is available on the system at  
all times.  

#### 2.21.2. Depended Packages
systemd-sysv  

#### 2.21.3. Configuration Files
(None)

#### 2.21.4. Executable Files
(None)

<br>

### 2.22 iproute2 Package
#### 2.22.1. Official Package Description
networking and traffic control tools  
The iproute2 suite is a collection of utilities for networking and  
traffic control.  
.  
These tools communicate with the Linux kernel via the (rt)netlink  
interface, providing advanced features not available through the  
legacy net-tools commands 'ifconfig' and 'route'.  

#### 2.22.2. Depended Packages
debconf  
libbpf1  
libc6  
libcap2  
libcap2-bin  
libdb5.3t64  
libelf1t64  
libmnl0  
libselinux1  
libtirpc3t64  
libxtables12  

#### 2.22.3. Configuration Files
/etc/iproute2/bpf_pinning  
/etc/iproute2/ematch_map  
/etc/iproute2/group  
/etc/iproute2/nl_protos  
/etc/iproute2/rt_dsfield  
/etc/iproute2/rt_protos  
/etc/iproute2/rt_protos.d/README  
/etc/iproute2/rt_realms  
/etc/iproute2/rt_scopes  
/etc/iproute2/rt_tables  
/etc/iproute2/rt_tables.d/README  

#### 2.22.4. Executable Files
/bin/ip  
/bin/ss  
/sbin/bridge  
/sbin/dcb  
/sbin/devlink  
/sbin/ip  
/sbin/rtacct  
/sbin/rtmon  
/sbin/tc  
/sbin/tipc  
/sbin/vdpa  
/usr/bin/ctstat  
/usr/bin/lnstat  
/usr/bin/nstat  
/usr/bin/rdma  
/usr/bin/routel  
/usr/bin/rtstat  
/usr/sbin/arpd  
/usr/sbin/genl  

<br>

### 2.23 iputils-ping Package
#### 2.23.1. Official Package Description
Tools to test the reachability of network hosts  
The ping command sends ICMP ECHO_REQUEST packets to a host in order to  
test if the host is reachable via the network.  
.  
This package includes a ping6 utility which supports IPv6 network  
connections.  

#### 2.23.2. Depended Packages
libc6  
libcap2  
libcap2-bin  
libidn2-0  

#### 2.23.3. Configuration Files
(None)

#### 2.23.4. Executable Files
/usr/bin/ping  
/usr/bin/ping4  
/usr/bin/ping6  

<br>

### 2.24 iso-codes Package
#### 2.24.1. Official Package Description
ISO language, territory, currency, script codes and their translations  
This package provides the ISO 639, ISO 639-3, and ISO 639-5 language  
code lists, the ISO 4217 currency code list, the ISO 3166 territory  
code list, the ISO 3166-2 sub-territory list, and the ISO 15924  
script code list as JSON files.  
.  
More importantly, it also provides their translations to be used by  
other programs.  

#### 2.24.2. Depended Packages
(None)

#### 2.24.3. Configuration Files
(None)

#### 2.24.4. Executable Files
(None)

<br>

### 2.25 kbd Package
#### 2.25.1. Official Package Description
Linux console font and keytable utilities  
This package allows you to set up the Linux console, change the font,  
resize text mode virtual consoles and remap the keyboard.  
.  
You will probably want to install the \xe2\x80\x9cconsole-setup\xe2\x80\x9d package which  
sets up console font and keymap data files.  

#### 2.25.2. Depended Packages
console-setup  
libc6  

#### 2.25.3. Configuration Files
(None)

#### 2.25.4. Executable Files
/usr/bin/chvt  
/usr/bin/codepage  
/usr/bin/deallocvt  
/usr/bin/dumpkeys  
/usr/bin/fgconsole  
/usr/bin/getkeycodes  
/usr/bin/kbd_mode  
/usr/bin/kbdinfo  
/usr/bin/loadkeys  
/usr/bin/loadunimap  
/usr/bin/mapscrn  
/usr/bin/mk_modmap  
/usr/bin/openvt  
/usr/bin/psfaddtable  
/usr/bin/psfgettable  
/usr/bin/psfstriptable  
/usr/bin/psfxtable  
/usr/bin/resizecons  
/usr/bin/screendump  
/usr/bin/setfont  
/usr/bin/setkeycodes  
/usr/bin/setleds  
/usr/bin/setlogcons  
/usr/bin/setmetamode  
/usr/bin/showconsolefont  
/usr/bin/showkey  
/usr/bin/splitfont  
/usr/bin/unicode_start  
/usr/bin/unicode_stop  
/usr/sbin/kbdrate  
/usr/sbin/setvesablank  
/usr/sbin/setvtrgb  
/usr/sbin/vcstime  

<br>

### 2.26 keyboard-configuration Package
#### 2.26.1. Official Package Description
system-wide keyboard preferences  
This package maintains the keyboard preferences in  
/etc/default/keyboard.  Other packages can use the information  
provided by this package in order to configure the keyboard on the  
console or in X Window.  

#### 2.26.2. Depended Packages
debconf  
liblocale-gettext-perl  
xkb-data  

#### 2.26.3. Configuration Files
(None)

#### 2.26.4. Executable Files
(None)

<br>

### 2.27 kmod Package
#### 2.27.1. Official Package Description
tools for managing Linux kernel modules  
This package contains a set of programs for loading, inserting, and  
removing kernel modules for Linux.  
It replaces module-init-tools.  

#### 2.27.2. Depended Packages
libc6  
libkmod2  
liblzma5  
libssl3  
libzstd1  

#### 2.27.3. Configuration Files
/etc/depmod.d/ubuntu.conf  
/etc/init.d/kmod  
/etc/modprobe.d/blacklist-ath_pci.conf  
/etc/modprobe.d/blacklist-firewire.conf  
/etc/modprobe.d/blacklist-framebuffer.conf  
/etc/modprobe.d/blacklist-rare-network.conf  
/etc/modprobe.d/blacklist.conf  
/etc/modprobe.d/iwlwifi.conf  

#### 2.27.4. Executable Files
/usr/bin/kmod  
/usr/bin/lsmod  
/usr/sbin/depmod  
/usr/sbin/insmod  
/usr/sbin/lsmod  
/usr/sbin/modinfo  
/usr/sbin/modprobe  
/usr/sbin/rmmod  

<br>

### 2.28 krb5-locales Package
#### 2.28.1. Official Package Description
internationalization support for MIT Kerberos  
Kerberos is a system for authenticating users and services on a network.  
Kerberos is a trusted third-party service.  That means that there is a  
third party (the Kerberos server) that is trusted by all the entities on  
the network (users and services, usually called "principals").  
.  
This is the MIT reference implementation of Kerberos V5.  
.  
This package contains internationalized messages for MIT Kerberos.  

#### 2.28.2. Depended Packages
(None)

#### 2.28.3. Configuration Files
(None)

#### 2.28.4. Executable Files
(None)

<br>

### 2.29 less Package
#### 2.29.1. Official Package Description
pager program similar to more  
This package provides "less", a file pager (that is, a memory-efficient  
utility for displaying text one screenful at a time). Less has many  
more features than the basic pager "more". As part of the GNU project,  
it is widely regarded as the standard pager on UNIX-derived systems.  
.  
Also provided are "lessecho", a simple utility for ensuring arguments  
with spaces are correctly quoted; "lesskey", a tool for modifying the  
standard (vi-like) keybindings; and "lesspipe", a filter for specific  
types of input, such as .doc or .txt.gz files.  

#### 2.29.2. Depended Packages
libc6  
libtinfo6  

#### 2.29.3. Configuration Files
(None)

#### 2.29.4. Executable Files
/usr/bin/less  
/usr/bin/lessecho  
/usr/bin/lessfile  
/usr/bin/lesskey  
/usr/bin/lesspipe  

<br>

### 2.30 libapparmor1 Package
#### 2.30.1. Official Package Description
changehat AppArmor library  
libapparmor1 provides a shared library one can compile programs  
against in order to use various AppArmor functionality,  
such as transitioning to a different AppArmor profile or hat.  

#### 2.30.2. Depended Packages
libc6  

#### 2.30.3. Configuration Files
(None)

#### 2.30.4. Executable Files
(None)

<br>

### 2.31 libapt-pkg6.0 Package
#### 2.31.1. Official Package Description

#### 2.31.2. Depended Packages
libbz2-1.0  
libc6  
libgcc-s1  
libgcrypt20  
liblz4-1  
liblzma5  
libstdc++6  
libsystemd0  
libudev1  
libxxhash0  
libzstd1  
zlib1g  

#### 2.31.3. Configuration Files
(None)

#### 2.31.4. Executable Files
(None)

<br>

### 2.32 libapt-pkg6.0t64 Package
#### 2.32.1. Official Package Description
package management runtime library  
This library provides the common functionality for searching and  
managing packages as well as information about packages.  
Higher-level package managers can depend upon this library.  
.  
This includes:  
retrieval of information about packages from multiple sources  
retrieval of packages and all dependent packages  
needed to satisfy a request either through an internal  
solver or by interfacing with an external one  
authenticating the sources and validating the retrieved data  
installation and removal of packages in the system  
providing different transports to retrieve data over cdrom, ftp,  
http(s), rsh as well as an interface to add more transports like  
tor+http(s) (apt-transport-tor).  

#### 2.32.2. Depended Packages
libbz2-1.0  
libc6  
libgcc-s1  
libgcrypt20  
liblz4-1  
liblzma5  
libstdc++6  
libsystemd0  
libudev1  
libxxhash0  
libzstd1  
zlib1g  

#### 2.32.3. Configuration Files
(None)

#### 2.32.4. Executable Files
(None)

<br>

### 2.33 libargon2-1 Package
#### 2.33.1. Official Package Description
memory-hard hashing function - runtime library  
Argon2 is a password-hashing function that can be used to hash passwords  
for credential storage, key derivation, or other applications.  
.  
There are two main versions of Argon2: Argon2i and Argon2d.  
Argon2i is the safest against side-channel attacks, while Argon2d provides  
the highest resistance against GPU cracking attacks.  
.  
Argon2i and Argon2d are parametrized by:  
A time cost, which defines the amount of computation realized and  
therefore the execution time, given in number of iterations  
A memory cost, which defines the memory usage, given in kibibytes  
A parallelism degree, which defines the number of parallel threads  
.  
This package includes the dynamic library against which programs are linked.  

#### 2.33.2. Depended Packages
libc6  

#### 2.33.3. Configuration Files
(None)

#### 2.33.4. Executable Files
(None)

<br>

### 2.34 libbpf1 Package
#### 2.34.1. Official Package Description
eBPF helper library (shared library)  
libbpf is a library for loading eBPF programs and reading and  
manipulating eBPF objects from user-space.  
.  
This package contains the shared library.  

#### 2.34.2. Depended Packages
libc6  
libelf1t64  
zlib1g  

#### 2.34.3. Configuration Files
(None)

#### 2.34.4. Executable Files
(None)

<br>

### 2.35 libbsd0 Package
#### 2.35.1. Official Package Description
utility functions from BSD systems - shared library  
This library provides some C functions such as strlcpy() that are commonly  
available on BSD systems but not on others like GNU systems.  
.  
For a detailed list of the provided functions, please see the libbsd-dev  
package description.  

#### 2.35.2. Depended Packages
libc6  
libmd0  

#### 2.35.3. Configuration Files
(None)

#### 2.35.4. Executable Files
(None)

<br>

### 2.36 libcap2-bin Package
#### 2.36.1. Official Package Description
POSIX 1003.1e capabilities (utilities)  
Libcap implements the user-space interfaces to the POSIX 1003.1e capabilities  
available in Linux kernels. These capabilities are a partitioning of the all  
powerful root privilege into a set of distinct privileges.  
.  
This package contains additional utilities.  

#### 2.36.2. Depended Packages
libc6  
libcap2  

#### 2.36.3. Configuration Files
(None)

#### 2.36.4. Executable Files
/usr/sbin/capsh  
/usr/sbin/getcap  
/usr/sbin/getpcaps  
/usr/sbin/setcap  

<br>

### 2.37 libcryptsetup12 Package
#### 2.37.1. Official Package Description
disk encryption support - shared library  
Cryptsetup provides an interface for configuring encryption on block  
devices (such as /home or swap partitions), using the Linux kernel  
device mapper target dm-crypt. It features integrated Linux Unified Key  
Setup (LUKS) support.  
.  
This package provides the libcryptsetup shared library.  

#### 2.37.2. Depended Packages
libargon2-1  
libblkid1  
libc6  
libdevmapper1.02.1  
libjson-c5  
libssl3  
libuuid1  

#### 2.37.3. Configuration Files
(None)

#### 2.37.4. Executable Files
(None)

<br>

### 2.38 libdb5.3t64 Package
#### 2.38.1. Official Package Description
Berkeley v5.3 Database Libraries [runtime]  
This is the runtime package for programs that use the v5.3 Berkeley  
database library.  

#### 2.38.2. Depended Packages
libc6  

#### 2.38.3. Configuration Files
(None)

#### 2.38.4. Executable Files
(None)

<br>

### 2.39 libdbus-1-3 Package
#### 2.39.1. Official Package Description
simple interprocess messaging system (library)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
D-Bus supports broadcast messages, asynchronous messages (thus  
decreasing latency), authentication, and more. It is designed to be  
low-overhead; messages are sent using a binary protocol, not using  
XML. D-Bus also supports a method call mapping for its messages, but  
it is not required; this makes using the system quite simple.  
.  
It comes with several bindings, including GLib, Python, Qt and Java.  
.  
The message bus daemon can be found in the dbus-daemon package.  

#### 2.39.2. Depended Packages
libc6  
libsystemd0  

#### 2.39.3. Configuration Files
(None)

#### 2.39.4. Executable Files
(None)

<br>

### 2.40 libdevmapper1.02.1 Package
#### 2.40.1. Official Package Description
Linux Kernel Device Mapper userspace library  
The Linux Kernel Device Mapper is the LVM (Linux Logical Volume Management)  
Teams implementation of a minimalistic kernel-space driver that handles  
volume management, while keeping knowledge of the underlying device layout  
in user-space.  This makes it useful for not only LVM, but software raid,  
and other drivers that create "virtual" block devices.  
.  
This package contains the (user-space) shared library for accessing the  
device-mapper; it allows usage of the device-mapper through a clean,  
consistent interface (as opposed to through kernel ioctls).  

#### 2.40.2. Depended Packages
libc6  
libselinux1  
libudev1  

#### 2.40.3. Configuration Files
(None)

#### 2.40.4. Executable Files
(None)

<br>

### 2.41 libelf1t64 Package
#### 2.41.1. Official Package Description
library to read and write ELF files  
The libelf1t64 package provides a shared library which allows reading and  
writing ELF files on a high level.  Third party programs depend on  
this package to read internals of ELF files.  The programs of the  
elfutils package use it also to generate new ELF files.  
.  
This library is part of elfutils.  

#### 2.41.2. Depended Packages
libc6  
libzstd1  
zlib1g  

#### 2.41.3. Configuration Files
(None)

#### 2.41.4. Executable Files
(None)

<br>

### 2.42 libestr0 Package
#### 2.42.1. Official Package Description
Helper functions for handling strings (lib)  
The 'libestr' library contains some essential string manipulation  
functions and more, like escaping special characters.  
.  
This package contains the shared library.  

#### 2.42.2. Depended Packages
libc6  

#### 2.42.3. Configuration Files
(None)

#### 2.42.4. Executable Files
(None)

<br>

### 2.43 libexpat1 Package
#### 2.43.1. Official Package Description
XML parsing C library - runtime library  
This package contains the runtime, shared library of expat, the C  
library for parsing XML. Expat is a stream-oriented parser in  
which an application registers handlers for things the parser  
might find in the XML document (like start tags).  

#### 2.43.2. Depended Packages
libc6  

#### 2.43.3. Configuration Files
(None)

#### 2.43.4. Executable Files
(None)

<br>

### 2.44 libfastjson4 Package
#### 2.44.1. Official Package Description
fast json library for C  
The libfastjson library is a fork from json-c with a focus on performance.  
.  
This package contains the shared library.  

#### 2.44.2. Depended Packages
libc6  

#### 2.44.3. Configuration Files
(None)

#### 2.44.4. Executable Files
(None)

<br>

### 2.45 libfdisk1 Package
#### 2.45.1. Official Package Description
fdisk partitioning library  
The libfdisk library is used for manipulating partition tables. It is  
the core of the fdisk, cfdisk, and sfdisk tools.  

#### 2.45.2. Depended Packages
libblkid1  
libc6  
libuuid1  

#### 2.45.3. Configuration Files
(None)

#### 2.45.4. Executable Files
(None)

<br>

### 2.46 libffi8 Package
#### 2.46.1. Official Package Description
Foreign Function Interface library runtime  
A foreign function interface is the popular name for the interface that  
allows code written in one language to call code written in another  
language.  

#### 2.46.2. Depended Packages
libc6  

#### 2.46.3. Configuration Files
(None)

#### 2.46.4. Executable Files
(None)

<br>

### 2.47 libfribidi0 Package
#### 2.47.1. Official Package Description
Free Implementation of the Unicode BiDi algorithm  
FriBiDi is a BiDi algorithm implementation for Hebrew and/or Arabic  
languages.  
This package contains the shared libraries.  

#### 2.47.2. Depended Packages
libc6  

#### 2.47.3. Configuration Files
(None)

#### 2.47.4. Executable Files
(None)

<br>

### 2.48 libgirepository-1.0-1 Package
#### 2.48.1. Official Package Description
Library for handling GObject introspection data (runtime library)  
GObject Introspection is a project for providing machine readable  
introspection data of the API of C libraries. This introspection  
data can be used in several different use cases, for example  
automatic code generation for bindings, API verification and documentation  
generation.  
.  
GObject Introspection contains tools to generate and handle the  
introspection data.  
.  
This package contains a C library for handling the introspection data.  

#### 2.48.2. Depended Packages
libc6  
libffi8  
libglib2.0-0t64  

#### 2.48.3. Configuration Files
(None)

#### 2.48.4. Executable Files
(None)

<br>

### 2.49 libglib2.0-0t64 Package
#### 2.49.1. Official Package Description
GLib library of C routines  
GLib is a library containing many useful C routines for things such  
as trees, hashes, lists, and strings.  It is a useful general-purpose  
C library used by projects such as GTK+, GIMP, and GNOME.  
.  
This package contains the shared libraries.  

#### 2.49.2. Depended Packages
libc6  
libffi8  
libmount1  
libpcre2-8-0  
libselinux1  
zlib1g  

#### 2.49.3. Configuration Files
(None)

#### 2.49.4. Executable Files
(None)

<br>

### 2.50 libglib2.0-data Package
#### 2.50.1. Official Package Description
Common files for GLib library  
GLib is a library containing many useful C routines for things such  
as trees, hashes, lists, and strings.  It is a useful general-purpose  
C library used by projects such as GTK+, GIMP, and GNOME.  
.  
This package is needed for the runtime libraries to display messages in  
languages other than English.  

#### 2.50.2. Depended Packages
(None)

#### 2.50.3. Configuration Files
(None)

#### 2.50.4. Executable Files
(None)

<br>

### 2.51 libgnutls30 Package
#### 2.51.1. Official Package Description
GNU TLS library - main runtime library  
GnuTLS is a portable library which implements the Transport Layer  
Security (TLS 1.0, 1.1, 1.2, 1.3) and Datagram  
Transport Layer Security (DTLS 1.0, 1.2) protocols.  
.  
GnuTLS features support for:  
- certificate path validation, as well as DANE and trust on first use.  
- the Online Certificate Status Protocol (OCSP).  
- public key methods, including RSA and Elliptic curves, as well as password  
and key authentication methods such as SRP and PSK protocols.  
- all the strong encryption algorithms, including AES and Camellia.  
- CPU-assisted cryptography with VIA padlock and AES-NI instruction sets.  
- HSMs and cryptographic tokens, via PKCS #11.  
.  
This package contains the main runtime library.  

#### 2.51.2. Depended Packages
libc6  
libgmp10  
libhogweed6  
libidn2-0  
libnettle8  
libp11-kit0  
libtasn1-6  
libunistring5  

#### 2.51.3. Configuration Files
(None)

#### 2.51.4. Executable Files
(None)

<br>

### 2.52 libgnutls30t64 Package
#### 2.52.1. Official Package Description
GNU TLS library - main runtime library  
GnuTLS is a portable library which implements the Transport Layer  
Security (TLS 1.0, 1.1, 1.2, 1.3) and Datagram  
Transport Layer Security (DTLS 1.0, 1.2) protocols.  
.  
GnuTLS features support for:  
certificate path validation, as well as DANE and trust on first use.  
the Online Certificate Status Protocol (OCSP).  
public key methods, including RSA and Elliptic curves, as well as password  
and key authentication methods such as SRP and PSK protocols.  
all the strong encryption algorithms, including AES and Camellia.  
CPU-assisted cryptography with VIA padlock and AES-NI instruction sets.  
HSMs and cryptographic tokens, via PKCS #11.  
.  
This package contains the main runtime library.  

#### 2.52.2. Depended Packages
libc6  
libgmp10  
libhogweed6t64  
libidn2-0  
libnettle8t64  
libp11-kit0  
libtasn1-6  
libunistring5  

#### 2.52.3. Configuration Files
/etc/gnutls/config  

#### 2.52.4. Executable Files
(None)

<br>

### 2.53 libgssapi-krb5-2 Package
#### 2.53.1. Official Package Description
MIT Kerberos runtime libraries - krb5 GSS-API Mechanism  
Kerberos is a system for authenticating users and services on a network.  
Kerberos is a trusted third-party service.  That means that there is a  
third party (the Kerberos server) that is trusted by all the entities on  
the network (users and services, usually called "principals").  
.  
This is the MIT reference implementation of Kerberos V5.  
.  
This package contains the runtime library for the MIT Kerberos  
implementation of GSS-API used by applications and Kerberos clients.  

#### 2.53.2. Depended Packages
libc6  
libcom-err2  
libk5crypto3  
libkrb5-3  
libkrb5support0  

#### 2.53.3. Configuration Files
(None)

#### 2.53.4. Executable Files
(None)

<br>

### 2.54 libhogweed6 Package
#### 2.54.1. Official Package Description
low level cryptographic library (public-key cryptos)  
Nettle is a cryptographic library that is designed to fit easily in more or  
less any context: In crypto toolkits for object-oriented languages (C++,  
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel  
space.  
.  
It tries to solve a problem of providing a common set of cryptographic  
algorithms for higher-level applications by implementing a  
context-independent set of cryptographic algorithms. In that light, Nettle  
doesn't do any memory allocation or I/O, it simply provides the  
cryptographic algorithms for the application to use in any environment and  
in any way it needs.  
.  
This package contains the asymmetric cryptographic algorithms, which,  
require the GNU multiple precision arithmetic library (libgmp) for  
their large integer computations.  

#### 2.54.2. Depended Packages
libc6  
libgmp10  
libnettle8  

#### 2.54.3. Configuration Files
(None)

#### 2.54.4. Executable Files
(None)

<br>

### 2.55 libhogweed6t64 Package
#### 2.55.1. Official Package Description
low level cryptographic library (public-key cryptos)  
Nettle is a cryptographic library that is designed to fit easily in more or  
less any context: In crypto toolkits for object-oriented languages (C++,  
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel  
space.  
.  
It tries to solve a problem of providing a common set of cryptographic  
algorithms for higher-level applications by implementing a  
context-independent set of cryptographic algorithms. In that light, Nettle  
doesn't do any memory allocation or I/O, it simply provides the  
cryptographic algorithms for the application to use in any environment and  
in any way it needs.  
.  
This package contains the asymmetric cryptographic algorithms, which,  
require the GNU multiple precision arithmetic library (libgmp) for  
their large integer computations.  

#### 2.55.2. Depended Packages
libc6  
libgmp10  
libnettle8t64  

#### 2.55.3. Configuration Files
(None)

#### 2.55.4. Executable Files
(None)

<br>

### 2.56 libicu74 Package
#### 2.56.1. Official Package Description
International Components for Unicode  
ICU is a C++ and C library that provides robust and full-featured  
Unicode and locale support.  This package contains the runtime  
libraries for ICU.  

#### 2.56.2. Depended Packages
libc6  
libgcc-s1  
libstdc++6  

#### 2.56.3. Configuration Files
(None)

#### 2.56.4. Executable Files
(None)

<br>

### 2.57 libidn2-0 Package
#### 2.57.1. Official Package Description
Internationalized domain names (IDNA2008/TR46) library  
Libidn2 implements the revised algorithm for internationalized domain  
names called IDNA2008/TR46.  
.  
This package contains runtime libraries.  

#### 2.57.2. Depended Packages
libc6  
libunistring5  

#### 2.57.3. Configuration Files
(None)

#### 2.57.4. Executable Files
(None)

<br>

### 2.58 libjson-c5 Package
#### 2.58.1. Official Package Description
JSON manipulation library - shared library  
This library allows you to easily construct JSON objects in C,  
output them as JSON formatted strings and parse JSON formatted  
strings back into the C representation of JSON objects.  

#### 2.58.2. Depended Packages
libc6  

#### 2.58.3. Configuration Files
(None)

#### 2.58.4. Executable Files
(None)

<br>

### 2.59 libk5crypto3 Package
#### 2.59.1. Official Package Description
MIT Kerberos runtime libraries - Crypto Library  
Kerberos is a system for authenticating users and services on a network.  
Kerberos is a trusted third-party service.  That means that there is a  
third party (the Kerberos server) that is trusted by all the entities on  
the network (users and services, usually called "principals").  
.  
This is the MIT reference implementation of Kerberos V5.  
.  
This package contains the runtime cryptography libraries used by  
applications and Kerberos clients.  

#### 2.59.2. Depended Packages
libc6  
libkrb5support0  

#### 2.59.3. Configuration Files
(None)

#### 2.59.4. Executable Files
(None)

<br>

### 2.60 libkeyutils1 Package
#### 2.60.1. Official Package Description
Linux Key Management Utilities (library)  
Keyutils is a set of utilities for managing the key retention facility in the  
kernel, which can be used by filesystems, block devices and more to gain and  
retain the authorization and encryption keys required to perform secure  
operations.  
.  
This package provides a wrapper library for the key management facility system  
calls.  

#### 2.60.2. Depended Packages
libc6  

#### 2.60.3. Configuration Files
(None)

#### 2.60.4. Executable Files
(None)

<br>

### 2.61 libkmod2 Package
#### 2.61.1. Official Package Description
libkmod shared library  
This library provides an API for insertion, removal, configuration and  
listing of kernel modules.  

#### 2.61.2. Depended Packages
libc6  
liblzma5  
libssl3  
libzstd1  

#### 2.61.3. Configuration Files
(None)

#### 2.61.4. Executable Files
(None)

<br>

### 2.62 libkrb5-3 Package
#### 2.62.1. Official Package Description
MIT Kerberos runtime libraries  
Kerberos is a system for authenticating users and services on a network.  
Kerberos is a trusted third-party service.  That means that there is a  
third party (the Kerberos server) that is trusted by all the entities on  
the network (users and services, usually called "principals").  
.  
This is the MIT reference implementation of Kerberos V5.  
.  
This package contains the runtime library for the main Kerberos v5 API  
used by applications and Kerberos clients.  

#### 2.62.2. Depended Packages
libc6  
libcom-err2  
libk5crypto3  
libkeyutils1  
libkrb5support0  
libssl3t64  

#### 2.62.3. Configuration Files
(None)

#### 2.62.4. Executable Files
(None)

<br>

### 2.63 libkrb5support0 Package
#### 2.63.1. Official Package Description
MIT Kerberos runtime libraries - Support library  
Kerberos is a system for authenticating users and services on a network.  
Kerberos is a trusted third-party service.  That means that there is a  
third party (the Kerberos server) that is trusted by all the entities on  
the network (users and services, usually called "principals").  
.  
This is the MIT reference implementation of Kerberos V5.  
.  
This package contains an internal runtime support library used by other  
Kerberos libraries.  

#### 2.63.2. Depended Packages
libc6  

#### 2.63.3. Configuration Files
(None)

#### 2.63.4. Executable Files
(None)

<br>

### 2.64 liblocale-gettext-perl Package
#### 2.64.1. Official Package Description
module using libc functions for internationalization in Perl  
The Locale::gettext module permits access from perl to the gettext() family of  
functions for retrieving message strings from databases constructed  
to internationalize software.  
.  
It provides gettext(), dgettext(), dcgettext(), textdomain(),  
bindtextdomain(), bind_textdomain_codeset(), ngettext(), dcngettext()  
and dngettext().  

#### 2.64.2. Depended Packages
libc6  
perl-base  
perlapi-5.38.2  

#### 2.64.3. Configuration Files
(None)

#### 2.64.4. Executable Files
(None)

<br>

### 2.65 libmnl0 Package
#### 2.65.1. Official Package Description
minimalistic Netlink communication library  
libmnl is a minimalistic user-space library oriented to Netlink developers.  
There are a lot of common tasks in parsing, validating, constructing of  
both the Netlink header and TLVs that are repetitive and easy to get wrong.  
This library aims to provide simple helpers that allows you to re-use code  
and to avoid re-inventing the wheel.  
.  
The main features of this library are:  
.  
Small: the shared library requires around 30KB for an x86-based computer.  
.  
Simple: this library avoids complexity and elaborated abstractions that  
tend to hide Netlink details.  
.  
Easy to use: the library simplifies the work for Netlink-wise developers.  
It provides functions to make socket handling, message building,  
validating, parsing and sequence tracking, easier.  
.  
Easy to re-use: you can use the library to build your own abstraction  
layer on top of this library.  
.  
Decoupling: the interdependency of the main bricks that compose the  
library is reduced, i.e. the library provides many helpers, but the  
programmer is not forced to use them.  
.  
This package contains the shared libraries needed to run programs that use  
the minimalistic Netlink communication library.  

#### 2.65.2. Depended Packages
libc6  

#### 2.65.3. Configuration Files
(None)

#### 2.65.4. Executable Files
(None)

<br>

### 2.66 libnetplan1 Package
#### 2.66.1. Official Package Description
Declarative network configuration runtime library  
netplan reads YAML network configuration files which are written  
by administrators, installers, cloud image instantiations, or other OS  
deployments. During early boot it then generates backend specific  
configuration files in /run to hand off control of devices to a particular  
networking daemon.  
.  
Currently supported backends are networkd and NetworkManager.  
.  
This package contains the necessary runtime library files.  

#### 2.66.2. Depended Packages
libc6  
libglib2.0-0t64  
libuuid1  
libyaml-0-2  

#### 2.66.3. Configuration Files
(None)

#### 2.66.4. Executable Files
(None)

<br>

### 2.67 libnettle8 Package
#### 2.67.1. Official Package Description
low level cryptographic library (symmetric and one-way cryptos)  
Nettle is a cryptographic library that is designed to fit easily in more or  
less any context: In crypto toolkits for object-oriented languages (C++,  
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel  
space.  
.  
It tries to solve a problem of providing a common set of cryptographic  
algorithms for higher-level applications by implementing a  
context-independent set of cryptographic algorithms. In that light, Nettle  
doesn't do any memory allocation or I/O, it simply provides the  
cryptographic algorithms for the application to use in any environment and  
in any way it needs.  
.  
This package contains the symmetric and one-way cryptographic  
algorithms. To avoid having this package depend on libgmp, the  
asymmetric cryptos reside in a separate library, libhogweed.  

#### 2.67.2. Depended Packages
libc6  

#### 2.67.3. Configuration Files
(None)

#### 2.67.4. Executable Files
(None)

<br>

### 2.68 libnettle8t64 Package
#### 2.68.1. Official Package Description
low level cryptographic library (symmetric and one-way cryptos)  
Nettle is a cryptographic library that is designed to fit easily in more or  
less any context: In crypto toolkits for object-oriented languages (C++,  
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel  
space.  
.  
It tries to solve a problem of providing a common set of cryptographic  
algorithms for higher-level applications by implementing a  
context-independent set of cryptographic algorithms. In that light, Nettle  
doesn't do any memory allocation or I/O, it simply provides the  
cryptographic algorithms for the application to use in any environment and  
in any way it needs.  
.  
This package contains the symmetric and one-way cryptographic  
algorithms. To avoid having this package depend on libgmp, the  
asymmetric cryptos reside in a separate library, libhogweed.  

#### 2.68.2. Depended Packages
libc6  

#### 2.68.3. Configuration Files
(None)

#### 2.68.4. Executable Files
(None)

<br>

### 2.69 libnewt0.52 Package
#### 2.69.1. Official Package Description
Not Erik's Windowing Toolkit - text mode windowing with slang  
Newt is a windowing toolkit for text mode built from the slang library.  
It allows color text mode applications to easily use stackable windows,  
push buttons, check boxes, radio buttons, lists, entry fields, labels,  
and displayable text. Scrollbars are supported, and forms may be nested  
to provide extra functionality. This package contains the shared library  
for programs that have been built with newt.  

#### 2.69.2. Depended Packages
libc6  
libslang2  

#### 2.69.3. Configuration Files
/etc/newt/palette.original  
/etc/newt/palette.ubuntu  

#### 2.69.4. Executable Files
(None)

<br>

### 2.70 libnss-systemd Package
#### 2.70.1. Official Package Description
nss module providing dynamic user and group name resolution  
nss-systemd is a plug-in module for the GNU Name Service Switch (NSS)  
functionality of the GNU C Library (glibc), providing UNIX user and group name  
resolution for dynamic users and groups allocated through the DynamicUser=  
option in systemd unit files. See systemd.exec(5) for details on this  
option.  
.  
Installing this package automatically adds the module to /etc/nsswitch.conf.  

#### 2.70.2. Depended Packages
libc6  
libcap2  
systemd  

#### 2.70.3. Configuration Files
(None)

#### 2.70.4. Executable Files
(None)

<br>

### 2.71 libp11-kit0 Package
#### 2.71.1. Official Package Description
library for loading and coordinating access to PKCS#11 modules - runtime  
The p11-kit library provides a way to load and enumerate Public-Key  
Cryptography Standard #11 modules, along with a standard configuration  
setup for installing PKCS#11 modules so that they're discoverable. It  
also solves problems with coordinating the use of PKCS#11 by different  
components or libraries living in the same process.  
.  
This package contains the shared library required for applications loading  
and accessing PKCS#11 modules.  

#### 2.71.2. Depended Packages
libc6  
libffi8  

#### 2.71.3. Configuration Files
(None)

#### 2.71.4. Executable Files
(None)

<br>

### 2.72 libpam-cap Package
#### 2.72.1. Official Package Description
POSIX 1003.1e capabilities (PAM module)  
Libcap implements the user-space interfaces to the POSIX 1003.1e capabilities  
available in Linux kernels. These capabilities are a partitioning of the all  
powerful root privilege into a set of distinct privileges.  
.  
This package contains the PAM module for enforcing capabilities on users and  
groups at PAM session start time.  

#### 2.72.2. Depended Packages
libc6  
libcap2  
libpam-runtime  
libpam0g  

#### 2.72.3. Configuration Files
/etc/security/capability.conf  

#### 2.72.4. Executable Files
(None)

<br>

### 2.73 libpam-systemd Package
#### 2.73.1. Official Package Description
system and service manager - PAM module  
This package contains the PAM module which registers user sessions in  
the systemd control group hierarchy for logind.  
.  
If in doubt, do install this package.  
.  
Packages that depend on logind functionality need to depend on libpam-systemd.  

#### 2.73.2. Depended Packages
default-dbus-system-bus  
libc6  
libcap2  
libpam-runtime  
libpam0g  
systemd  
systemd-sysv  

#### 2.73.3. Configuration Files
(None)

#### 2.73.4. Executable Files
(None)

<br>

### 2.74 libpopt0 Package
#### 2.74.1. Official Package Description
lib for parsing cmdline parameters  
Popt was heavily influenced by the getopt() and getopt_long() functions,  
but it allows more powerful argument expansion. It can parse arbitrary  
argv[] style arrays and automatically set variables based on command  
line arguments. It also allows command line arguments to be aliased via  
configuration files and includes utility functions for parsing arbitrary  
strings into argv[] arrays using shell-like rules.  
.  
This package contains the runtime library and locale data.  

#### 2.74.2. Depended Packages
libc6  

#### 2.74.3. Configuration Files
(None)

#### 2.74.4. Executable Files
(None)

<br>

### 2.75 libpython3-stdlib Package
#### 2.75.1. Official Package Description
interactive high-level object-oriented language (default python3 version)  
This package contains the majority of the standard library for the Python  
language (default python3 version).  
.  
This package is a dependency package, which depends on Debian's default  
Python 3 version's standard library (currently v3.12).  

#### 2.75.2. Depended Packages
libpython3.12-stdlib  

#### 2.75.3. Configuration Files
(None)

#### 2.75.4. Executable Files
(None)

<br>

### 2.76 libpython3.12-minimal Package
#### 2.76.1. Official Package Description
Minimal subset of the Python language (version 3.12)  
This package contains some essential modules. It is normally not  
used on it's own, but as a dependency of python3.12-minimal.  

#### 2.76.2. Depended Packages
libc6  
libssl3t64  

#### 2.76.3. Configuration Files
/etc/python3.12/sitecustomize.py  

#### 2.76.4. Executable Files
(None)

<br>

### 2.77 libpython3.12-stdlib Package
#### 2.77.1. Official Package Description
Interactive high-level object-oriented language (standard library, version 3.12)  
Python is a high-level, interactive, object-oriented language. Its 3.12 version  
includes an extensive class library with lots of goodies for  
network programming, system administration, sounds and graphics.  
.  
This package contains Python 3.12's standard library. It is normally not  
used on its own, but as a dependency of python3.12.  

#### 2.77.2. Depended Packages
libbz2-1.0  
libc6  
libcrypt1  
libdb5.3t64  
libffi8  
liblzma5  
libncursesw6  
libpython3.12-minimal  
libreadline8t64  
libsqlite3-0  
libtinfo6  
media-types  
netbase  
tzdata  

#### 2.77.3. Configuration Files
(None)

#### 2.77.4. Executable Files
(None)

<br>

### 2.78 libreadline8t64 Package
#### 2.78.1. Official Package Description
GNU readline and history libraries, run-time libraries  
The GNU readline library aids in the consistency of user interface  
across discrete programs that need to provide a command line  
interface.  
.  
The GNU history library provides a consistent user interface for  
recalling lines of previously typed input.  

#### 2.78.2. Depended Packages
libc6  
libtinfo6  
readline-common  

#### 2.78.3. Configuration Files
(None)

#### 2.78.4. Executable Files
(None)

<br>

### 2.79 libseccomp2 Package
#### 2.79.1. Official Package Description
high level interface to Linux seccomp filter  
This library provides a high level interface to constructing, analyzing  
and installing seccomp filters via a BPF passed to the Linux Kernel's  
prctl() syscall.  

#### 2.79.2. Depended Packages
libc6  

#### 2.79.3. Configuration Files
(None)

#### 2.79.4. Executable Files
(None)

<br>

### 2.80 libslang2 Package
#### 2.80.1. Official Package Description
S-Lang programming library - runtime version  
S-Lang is a C programmer's library that includes routines for the rapid  
development of sophisticated, user friendly, multi-platform applications.  
.  
This package contains only the shared library libslang.so.* and copyright  
information. It is only necessary for programs that use this library (such  
as jed and slrn). If you plan on doing development with S-Lang, you will  
need the companion -dev package as well.  

#### 2.80.2. Depended Packages
libc6  

#### 2.80.3. Configuration Files
(None)

#### 2.80.4. Executable Files
(None)

<br>

### 2.81 libsqlite3-0 Package
#### 2.81.1. Official Package Description
SQLite 3 shared library  
SQLite is a C library that implements an SQL database engine.  
Programs that link with the SQLite library can have SQL database  
access without running a separate RDBMS process.  

#### 2.81.2. Depended Packages
libc6  

#### 2.81.3. Configuration Files
(None)

#### 2.81.4. Executable Files
(None)

<br>

### 2.82 libstdc++6 Package
#### 2.82.1. Official Package Description
GNU Standard C++ Library v3  
This package contains an additional runtime library for C++ programs  
built with the GNU compiler.  
.  
libstdc++-v3 is a complete rewrite from the previous libstdc++-v2, which  
was included up to g++-2.95. The first version of libstdc++-v3 appeared  
in g++-3.0.  

#### 2.82.2. Depended Packages
gcc-14-base  
libc6  
libgcc-s1  

#### 2.82.3. Configuration Files
(None)

#### 2.82.4. Executable Files
(None)

<br>

### 2.83 libsystemd-shared Package
#### 2.83.1. Official Package Description
systemd shared private library  
This internal shared library provides common code used by various systemd  
components. It is supposed to decrease memory and disk footprint.  
The shared library is not meant for public use and is not API or ABI stable.  

#### 2.83.2. Depended Packages
libacl1  
libapparmor1  
libaudit1  
libblkid1  
libc6  
libcap2  
libcrypt1  
libgcrypt20  
libkmod2  
liblz4-1  
liblzma5  
libmount1  
libpam0g  
libseccomp2  
libselinux1  
libssl3t64  
libzstd1  

#### 2.83.3. Configuration Files
(None)

#### 2.83.4. Executable Files
(None)

<br>

### 2.84 libtasn1-6 Package
#### 2.84.1. Official Package Description
Manage ASN.1 structures (runtime)  
Manage ASN1 (Abstract Syntax Notation One) structures.  
The main features of this library are:  
on-line ASN1 structure management that doesn't require any C code  
file generation.  
off-line ASN1 structure management with C code file generation  
containing an array.  
DER (Distinguish Encoding Rules) encoding  
no limits for INTEGER and ENUMERATED values  
.  
This package contains runtime libraries.  

#### 2.84.2. Depended Packages
libc6  

#### 2.84.3. Configuration Files
(None)

#### 2.84.4. Executable Files
(None)

<br>

### 2.85 libtext-charwidth-perl Package
#### 2.85.1. Official Package Description
get display widths of characters on the terminal  
Text::CharWidth permits one to get the display widths of characters  
and strings on the terminal, using wcwidth() and wcswidth() from libc.  
.  
It provides mbwidth(), mbswidth(), and mblen().  

#### 2.85.2. Depended Packages
libc6  
perl-base  
perlapi-5.38.2  

#### 2.85.3. Configuration Files
(None)

#### 2.85.4. Executable Files
(None)

<br>

### 2.86 libtext-iconv-perl Package
#### 2.86.1. Official Package Description
module to convert between character sets in Perl  
The iconv() family of functions from XPG4 defines an API for converting  
between character sets (e.g. UTF-8 to Latin1, EBCDIC to ASCII). They  
are provided by libc6.  
.  
This package allows access to them from Perl via the Text::Iconv  
package.  

#### 2.86.2. Depended Packages
libc6  
perl-base  
perlapi-5.38.2  

#### 2.86.3. Configuration Files
(None)

#### 2.86.4. Executable Files
(None)

<br>

### 2.87 libtext-wrapi18n-perl Package
#### 2.87.1. Official Package Description
internationalized substitute of Text::Wrap  
The Text::WrapI18N module is a substitution for Text::Wrap, supporting  
multibyte characters such as UTF-8, EUC-JP, and GB2312, fullwidth characters  
such as east Asian characters, combining characters such as diacritical marks  
and Thai, and languages which don't use whitespaces between words such as  
Chinese and Japanese.  
.  
It provides wrap().  

#### 2.87.2. Depended Packages
libtext-charwidth-perl  

#### 2.87.3. Configuration Files
(None)

#### 2.87.4. Executable Files
(None)

<br>

### 2.88 libtirpc-common Package
#### 2.88.1. Official Package Description
transport-independent RPC library - common files  
This package contains a port of Sun's transport-independent RPC library to  
Linux. The library is intended as a replacement for the RPC code in the GNU C  
library, providing among others support for RPC (and in turn, NFS) over IPv6.  
.  
This package contains the netconfig configuration file as well as the  
associated manpage.  

#### 2.88.2. Depended Packages
(None)

#### 2.88.3. Configuration Files
/etc/netconfig  

#### 2.88.4. Executable Files
(None)

<br>

### 2.89 libtirpc3t64 Package
#### 2.89.1. Official Package Description
transport-independent RPC library  
This package contains a port of Sun's transport-independent RPC library to  
Linux. The library is intended as a replacement for the RPC code in the GNU C  
library, providing among others support for RPC (and in turn, NFS) over IPv6.  

#### 2.89.2. Depended Packages
libc6  
libgssapi-krb5-2  
libtirpc-common  

#### 2.89.3. Configuration Files
(None)

#### 2.89.4. Executable Files
(None)

<br>

### 2.90 libunistring5 Package
#### 2.90.1. Official Package Description
Unicode string library for C  
The 'libunistring' library implements Unicode strings (in the UTF-8,  
UTF-16, and UTF-32 encodings), together with functions for Unicode  
characters (character names, classifications, properties) and  
functions for string processing (formatted output, width, word  
breaks, line breaks, normalization, case folding, regular  
expressions).  
.  
This package contains the shared library.  

#### 2.90.2. Depended Packages
libc6  

#### 2.90.3. Configuration Files
(None)

#### 2.90.4. Executable Files
(None)

<br>

### 2.91 libxml2 Package
#### 2.91.1. Official Package Description
GNOME XML library  
XML is a metalanguage to let you design your own markup language.  
A regular markup language defines a way to describe information in  
a certain class of documents (eg HTML). XML lets you define your  
own customized markup languages for many classes of document. It  
can do this because it's written in SGML, the international standard  
metalanguage for markup languages.  
.  
This package provides a library providing an extensive API to handle  
such XML data files.  

#### 2.91.2. Depended Packages
libc6  
libicu74  
liblzma5  
zlib1g  

#### 2.91.3. Configuration Files
(None)

#### 2.91.4. Executable Files
(None)

<br>

### 2.92 libxtables12 Package
#### 2.92.1. Official Package Description
netfilter xtables library  
The iptables/xtables framework has been replaced by nftables. You should  
consider migrating now.  
.  
However, even if a given system may be fully running on native nftables,  
there are other reasons why libxtables might be installed. For one, nftables  
itself uses it to be able to display old rulesets that were created using  
xtables extensions (to help folks migrate). Other third-party software might  
also be linked to this library.  
.  
This library being installed in the system should be harmless in any case.  
.  
This package contains the user-space interface to the Netfilter xtables  
kernel framework.  

#### 2.92.2. Depended Packages
libc6  

#### 2.92.3. Configuration Files
(None)

#### 2.92.4. Executable Files
(None)

<br>

### 2.93 libxxhash0 Package
#### 2.93.1. Official Package Description
shared library for xxhash  
xxHash is an Extremely fast Hash algorithm, running at RAM speed limits.  
It successfully completes the SMHasher test suite which evaluates collision,  
dispersion and randomness qualities of hash functions. Code is highly portable,  
and hashes are identical on all platforms (little / big endian).  
.  
This package contains the shared library.  

#### 2.93.2. Depended Packages
libc6  

#### 2.93.3. Configuration Files
(None)

#### 2.93.4. Executable Files
(None)

<br>

### 2.94 libyaml-0-2 Package
#### 2.94.1. Official Package Description
Fast YAML 1.1 parser and emitter library  
LibYAML is a C library for parsing and emitting data in YAML 1.1, a  
human-readable data serialization format.  

#### 2.94.2. Depended Packages
libc6  

#### 2.94.3. Configuration Files
(None)

#### 2.94.4. Executable Files
(None)

<br>

### 2.95 locales Package
#### 2.95.1. Official Package Description
GNU C Library: National Language (locale) data [support]  
Machine-readable data files, shared objects and programs used by the  
C library for localization (l10n) and internationalization (i18n) support.  
.  
This package contains tools to generate locale definitions from source  
files (included in this package). It allows you to customize which  
definitions actually get generated. This is a space-saver over how this  
package used to be, with all locales generated by default. This created  
a package that unpacked to an excess of 30 megs.  

#### 2.95.2. Depended Packages
debconf  
libc-bin  

#### 2.95.3. Configuration Files
/etc/locale.alias  

#### 2.95.4. Executable Files
/usr/sbin/locale-gen  
/usr/sbin/update-locale  
/usr/sbin/validlocale  

<br>

### 2.96 logrotate Package
#### 2.96.1. Official Package Description
Log rotation utility  
The logrotate utility is designed to simplify the administration of  
log files on a system which generates a lot of log files.  Logrotate  
allows for the automatic rotation compression, removal and mailing of  
log files.  Logrotate can be set to handle a log file daily, weekly,  
monthly or when the log file gets to a certain size.  Normally, logrotate  
runs as a daily cron job.  

#### 2.96.2. Depended Packages
cron  
libacl1  
libc6  
libpopt0  
libselinux1  

#### 2.96.3. Configuration Files
/etc/cron.daily/logrotate  
/etc/logrotate.conf  
/etc/logrotate.d/btmp  
/etc/logrotate.d/wtmp  

#### 2.96.4. Executable Files
/usr/sbin/logrotate  

<br>

### 2.97 lsb-release Package
#### 2.97.1. Official Package Description
Linux Standard Base version reporting utility (minimal implementation)  
The Linux Standard Base (http://www.linuxbase.org/) is a standard  
core system that third-party applications written for Linux can  
depend upon.  
.  
The lsb_release command is a simple tool to help identify the Linux  
distribution being used and its compliance with the Linux Standard Base.  
.  
This package contains a bare-bones implementation that uses the  
information in /etc/os-release instead of relying on LSB packages.  

#### 2.97.2. Depended Packages
(None)

#### 2.97.3. Configuration Files
(None)

#### 2.97.4. Executable Files
/usr/bin/lsb_release  

<br>

### 2.98 media-types Package
#### 2.98.1. Official Package Description
List of standard media types and their usual file extension  
This package installs the configuration file /etc/mime.types, that lists  
standard media types (originally known as "MIME" types) and their usual file  
extension.  This provides a simple way for programs to have a first guess at a  
files content.  On standard Debian desktop systems, one will also find more  
sophisticated tools, for instance provided by the "file" and "xdg-utils"  
packages.  
.  
The /etc/mime.types file is compiled by hand using mostly information provided  
by the Internet Assigned Numbers Authority (IANA).  

#### 2.98.2. Depended Packages
(None)

#### 2.98.3. Configuration Files
/etc/mime.types  

#### 2.98.4. Executable Files
(None)

<br>

### 2.99 netbase Package
#### 2.99.1. Official Package Description
Basic TCP/IP networking system  
This package provides the necessary infrastructure for basic TCP/IP based  
networking.  
.  
In particular, it supplies common name-to-number mappings in /etc/services,  
/etc/rpc, /etc/protocols and /etc/ethertypes.  

#### 2.99.2. Depended Packages
(None)

#### 2.99.3. Configuration Files
/etc/ethertypes  
/etc/protocols  
/etc/rpc  
/etc/services  

#### 2.99.4. Executable Files
(None)

<br>

### 2.100 netcat-openbsd Package
#### 2.100.1. Official Package Description
TCP/IP swiss army knife  
A simple Unix utility which reads and writes data across network connections  
using TCP or UDP protocol. It is designed to be a reliable "back-end" tool  
that can be used directly or easily driven by other programs and scripts. At  
the same time it is a feature-rich network debugging and exploration tool,  
since it can create almost any kind of connection you would need and has  
several interesting built-in capabilities.  
.  
This package contains the OpenBSD rewrite of netcat, including support for  
IPv6, proxies, and Unix sockets.  

#### 2.100.2. Depended Packages
libbsd0  
libc6  

#### 2.100.3. Configuration Files
(None)

#### 2.100.4. Executable Files
/bin/nc.openbsd  

<br>

### 2.101 netplan-generator Package
#### 2.101.1. Official Package Description
Declarative network configuration systemd-generator  
netplan reads YAML network configuration files which are written  
by administrators, installers, cloud image instantiations, or other OS  
deployments. During early boot it then generates backend specific  
configuration files in /run to hand off control of devices to a particular  
networking daemon.  
.  
Currently supported backends are networkd and NetworkManager.  
.  
This package provides a systemd-generator to configure networking daemons  
at boot time.  

#### 2.101.2. Depended Packages
libc6  
libglib2.0-0t64  
libnetplan1  
systemd  

#### 2.101.3. Configuration Files
(None)

#### 2.101.4. Executable Files
(None)

<br>

### 2.102 netplan.io Package
#### 2.102.1. Official Package Description
Declarative network configuration for various backends  
netplan reads YAML network configuration files which are written  
by administrators, installers, cloud image instantiations, or other OS  
deployments. During early boot it then generates backend specific  
configuration files in /run to hand off control of devices to a particular  
networking daemon.  
.  
Currently supported backends are networkd and NetworkManager.  

#### 2.102.2. Depended Packages
iproute2  
libc6  
libglib2.0-0t64  
libnetplan1  
libsystemd0  
netplan-generator  
python3  
python3-dbus  
python3-netifaces  
python3-netplan  
python3-yaml  
systemd  

#### 2.102.3. Configuration Files
(None)

#### 2.102.4. Executable Files
/usr/sbin/netplan  

<br>

### 2.103 networkd-dispatcher Package
#### 2.103.1. Official Package Description
Dispatcher service for systemd-networkd connection status changes  
Networkd-dispatcher is a dispatcher daemon for systemd-networkd  
connection status changes. It is similar to NetworkManager-dispatcher,  
but is much more limited in the types of events it supports due to the  
limited nature of systemd-networkd.  

#### 2.103.2. Depended Packages
dbus  
gir1.2-glib-2.0  
python3-dbus  
python3-gi  
python3:any  

#### 2.103.3. Configuration Files
/etc/default/networkd-dispatcher  

#### 2.103.4. Executable Files
/usr/bin/networkd-dispatcher  

<br>

### 2.104 openssl Package
#### 2.104.1. Official Package Description
Secure Sockets Layer toolkit - cryptographic utility  
This package is part of the OpenSSL project's implementation of the SSL  
and TLS cryptographic protocols for secure communication over the  
Internet.  
.  
It contains the general-purpose command line binary /usr/bin/openssl,  
useful for cryptographic operations such as:  
creating RSA, DH, and DSA key parameters;  
creating X.509 certificates, CSRs, and CRLs;  
calculating message digests;  
encrypting and decrypting with ciphers;  
testing SSL/TLS clients and servers;  
handling S/MIME signed or encrypted mail.  

#### 2.104.2. Depended Packages
libc6  
libssl3t64  

#### 2.104.3. Configuration Files
/etc/ssl/openssl.cnf  

#### 2.104.4. Executable Files
/usr/bin/c_rehash  
/usr/bin/openssl  

<br>

### 2.105 python-apt-common Package
#### 2.105.1. Official Package Description
Python interface to libapt-pkg (locales)  
The apt_pkg Python interface will provide full access to the internal  
libapt-pkg structures allowing Python programs to easily perform a  
variety of functions.  
.  
This package contains locales.  

#### 2.105.2. Depended Packages
(None)

#### 2.105.3. Configuration Files
(None)

#### 2.105.4. Executable Files
(None)

<br>

### 2.106 python3 Package
#### 2.106.1. Official Package Description
interactive high-level object-oriented language (default python3 version)  
Python, the high-level, interactive object oriented language,  
includes an extensive class library with lots of goodies for  
network programming, system administration, sounds and graphics.  
.  
This package is a dependency package, which depends on Debian's default  
Python 3 version (currently v3.12).  

#### 2.106.2. Depended Packages
libpython3-stdlib  
python3-minimal  
python3.12  

#### 2.106.3. Configuration Files
(None)

#### 2.106.4. Executable Files
/usr/bin/pdb3  
/usr/bin/pydoc3  
/usr/bin/pygettext3  

<br>

### 2.107 python3-apt Package
#### 2.107.1. Official Package Description
Python 3 interface to libapt-pkg  
The apt_pkg Python 3 interface will provide full access to the internal  
libapt-pkg structures allowing Python 3 programs to easily perform a  
variety of functions, such as:  
.  
Access to the APT configuration system  
Access to the APT package information database  
Parsing of Debian package control files, and other files with a  
similar structure  
.  
The included 'aptsources' Python interface provides an abstraction of  
the sources.list configuration on the repository and the distro level.  

#### 2.107.2. Depended Packages
distro-info-data  
libapt-pkg6.0t64  
libc6  
libgcc-s1  
libstdc++6  
python-apt-common  
python3  
python3:any  

#### 2.107.3. Configuration Files
(None)

#### 2.107.4. Executable Files
(None)

<br>

### 2.108 python3-cffi-backend Package
#### 2.108.1. Official Package Description
Foreign Function Interface for Python 3 calling C code - runtime  
Convenient and reliable way of calling C code from Python 3.  
.  
The aim of this project is to provide a convenient and reliable way of calling  
C code from Python. It keeps Python logic in Python, and minimises the C  
required. It is able to work at either the C API or ABI level, unlike most  
other approaches, that only support the ABI level.  
.  
This package contains the runtime support for pre-built cffi modules.  

#### 2.108.2. Depended Packages
libc6  
libffi8  
python3  

#### 2.108.3. Configuration Files
(None)

#### 2.108.4. Executable Files
(None)

<br>

### 2.109 python3-dbus Package
#### 2.109.1. Official Package Description
simple interprocess messaging system (Python 3 interface)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
This package provides a Python 3 interface to D-Bus.  
.  
See the dbus description for more information about D-Bus in general.  

#### 2.109.2. Depended Packages
libc6  
libdbus-1-3  
libglib2.0-0t64  
python3  
python3:any  

#### 2.109.3. Configuration Files
(None)

#### 2.109.4. Executable Files
(None)

<br>

### 2.110 python3-gi Package
#### 2.110.1. Official Package Description
Python 3 bindings for gobject-introspection libraries  
GObject is an abstraction layer that allows programming with an object  
paradigm that is compatible with many languages. It is a part of Glib,  
the core library used to build GTK+ and GNOME.  
.  
This package contains the Python 3 binding generator for libraries that  
support gobject-introspection, i. e. which ship a gir1.2-<name>-<version>  
package. With these packages, the libraries can be used from Python 3.  

#### 2.110.2. Depended Packages
gir1.2-girepository-2.0  
gir1.2-glib-2.0  
libc6  
libffi8  
libgirepository-1.0-1  
libgirepository-1.0-1-with-libffi8  
libglib2.0-0t64  
python3  
python3:any  

#### 2.110.3. Configuration Files
(None)

#### 2.110.4. Executable Files
(None)

<br>

### 2.111 python3-markdown-it Package
#### 2.111.1. Official Package Description
Python port of markdown-it and some its associated plugins  
High speed Python markdown parser based in markdown-it. markdown-it-py  
follows the CommonMark spec for baseline parsing. Also, new syntax  
rules can be added and even replace existing ones. New syntax extensions  
can be added to extend the parser.  

#### 2.111.2. Depended Packages
python3-mdurl  
python3:any  

#### 2.111.3. Configuration Files
(None)

#### 2.111.4. Executable Files
/usr/bin/markdown-it  

<br>

### 2.112 python3-mdurl Package
#### 2.112.1. Official Package Description
Python port of the JavaScript mdurl package  
mdurl is a set of URL utilities for the markdown-it-py package. It  
provides a pure-Python implementation of several functions from the  
original JavaScript package, such as .decode(), .parse(), .encode().  

#### 2.112.2. Depended Packages
python3:any  

#### 2.112.3. Configuration Files
(None)

#### 2.112.4. Executable Files
(None)

<br>

### 2.113 python3-minimal Package
#### 2.113.1. Official Package Description
minimal subset of the Python language (default python3 version)  
This package contains the interpreter and some essential modules.  It's used  
in the boot process for some basic tasks.  
See /usr/share/doc/python3.12-minimal/README.Debian for a list of the modules  
contained in this package.  

#### 2.113.2. Depended Packages
dpkg  
python3.12-minimal  

#### 2.113.3. Configuration Files
(None)

#### 2.113.4. Executable Files
/usr/bin/py3clean  
/usr/bin/py3compile  
/usr/bin/py3versions  
/usr/bin/python3  

<br>

### 2.114 python3-netifaces Package
#### 2.114.1. Official Package Description
portable network interface information - Python 3.x  
netifaces provides a (hopefully portable-ish) way for Python programmers to  
get access to a list of the network interfaces on the local machine, and to  
obtain the addresses of those network interfaces.  
.  
This package contains the module for Python 3.x.  

#### 2.114.2. Depended Packages
libc6  
python3  

#### 2.114.3. Configuration Files
(None)

#### 2.114.4. Executable Files
(None)

<br>

### 2.115 python3-netplan Package
#### 2.115.1. Official Package Description
Declarative network configuration Python bindings  
netplan reads YAML network configuration files which are written  
by administrators, installers, cloud image instantiations, or other OS  
deployments. During early boot it then generates backend specific  
configuration files in /run to hand off control of devices to a particular  
networking daemon.  
.  
Currently supported backends are networkd and NetworkManager.  
.  
This package provides a CFFI based Python bindings to libnetplan.  

#### 2.115.2. Depended Packages
libc6  
libnetplan1  
python3  
python3-cffi-backend  

#### 2.115.3. Configuration Files
(None)

#### 2.115.4. Executable Files
(None)

<br>

### 2.116 python3-pkg-resources Package
#### 2.116.1. Official Package Description
Package Discovery and Resource Access using pkg_resources  
The pkg_resources module provides an API for Python libraries to  
access their resource files, and for extensible applications and  
frameworks to automatically discover plugins.  It also provides  
runtime support for using C extensions that are inside zipfile-format  
eggs, support for merging packages that have separately-distributed  
modules or subpackages, and APIs for managing Pythons current  
"working set" of active packages.  

#### 2.116.2. Depended Packages
python3:any  

#### 2.116.3. Configuration Files
(None)

#### 2.116.4. Executable Files
(None)

<br>

### 2.117 python3-pygments Package
#### 2.117.1. Official Package Description
syntax highlighting package written in Python 3  
Pygments aims to be a generic syntax highlighter for general use in all kinds  
of software such as forum systems, wikis or other applications that need to  
prettify source code.  
.  
Highlights are:  
a wide range of common languages and markup formats is supported  
special attention is paid to details, increasing quality by a fair amount  
support for new languages and formats are added easily  
a number of output formats, presently HTML, LaTeX and ANSI sequences  
it is usable as a command-line tool and as a library  

#### 2.117.2. Depended Packages
python3-pkg-resources  
python3:any  

#### 2.117.3. Configuration Files
(None)

#### 2.117.4. Executable Files
/usr/bin/pygmentize  

<br>

### 2.118 python3-rich Package
#### 2.118.1. Official Package Description
render rich text, tables, progress bars, syntax highlighting, markdown and more  
Rich is a Python library for rich text and beautiful formatting in the  
terminal.  
.  
The Rich API makes it easy to add color and style to terminal output. Rich can  
also render pretty tables, progress bars, markdown, syntax highlighted source  
code, tracebacks, and more \xe2\x80\x94 out of the box.  
.  
Here's a list of the core functionalities of rich:  
.  
to effortlessly add rich output to your application, you can import the rich  
print method, which has the same signature as the builtin Python function  
Rich can be installed in the Python REPL, so that any data structures will  
be pretty printed and highlighted  
for more control over rich terminal content, import and construct a Console  
object. The Console object has a print method which has an intentionally  
similar interface to the builtin print function  
to insert an emoji in to console output place the name between two colons  
Rich can render flexible tables with unicode box characters. There is a  
large variety of formatting options for borders, styles, cell alignment etc  
Rich can render multiple flicker-free progress bars to track long-running  
tasks.  
Rich can render content in neat columns with equal or optimal width.  
Rich can render markdown and does a reasonable job of translating the  
formatting to the terminal  
Rich can render beautiful tracebacks which are easier to read and show more  
code than standard Python tracebacks. You can set Rich as the default  
traceback handler so all uncaught exceptions will be rendered by Rich.  

#### 2.118.2. Depended Packages
python3-markdown-it  
python3-pygments  
python3-typing-extensions  
python3:any  

#### 2.118.3. Configuration Files
(None)

#### 2.118.4. Executable Files
(None)

<br>

### 2.119 python3-yaml Package
#### 2.119.1. Official Package Description
YAML parser and emitter for Python3  
Python3-yaml is a complete YAML 1.1 parser and emitter for Python3.  It can  
parse all examples from the specification. The parsing algorithm is simple  
enough to be a reference for YAML parser implementors. A simple extension API  
is also provided.  The package is built using libyaml for improved speed.  

#### 2.119.2. Depended Packages
libc6  
libyaml-0-2  
python3  
python3:any  

#### 2.119.3. Configuration Files
(None)

#### 2.119.4. Executable Files
(None)

<br>

### 2.120 python3.12 Package
#### 2.120.1. Official Package Description
Interactive high-level object-oriented language (version 3.12)  
Python is a high-level, interactive, object-oriented language. Its 3.12 version  
includes an extensive class library with lots of goodies for  
network programming, system administration, sounds and graphics.  

#### 2.120.2. Depended Packages
libpython3.12-stdlib  
media-types  
python3.12-minimal  
tzdata  

#### 2.120.3. Configuration Files
(None)

#### 2.120.4. Executable Files
/usr/bin/pdb3.12  
/usr/bin/pydoc3.12  
/usr/bin/pygettext3.12  

<br>

### 2.121 python3.12-minimal Package
#### 2.121.1. Official Package Description
Minimal subset of the Python language (version 3.12)  
This package contains the interpreter and some essential modules.  It can  
be used in the boot process for some basic tasks.  
See /usr/share/doc/python3.12-minimal/README.Debian for a list of the modules  
contained in this package.  

#### 2.121.2. Depended Packages
libc6  
libexpat1  
libpython3.12-minimal  
zlib1g  

#### 2.121.3. Configuration Files
(None)

#### 2.121.4. Executable Files
/usr/bin/python3.12  

<br>

### 2.122 readline-common Package
#### 2.122.1. Official Package Description
GNU readline and history libraries, common files  
The GNU readline library aids in the consistency of user interface  
across discrete programs that need to provide a command line  
interface.  
.  
The GNU history library provides a consistent user interface for  
recalling lines of previously typed input.  

#### 2.122.2. Depended Packages
(None)

#### 2.122.3. Configuration Files
(None)

#### 2.122.4. Executable Files
(None)

<br>

### 2.123 rsyslog Package
#### 2.123.1. Official Package Description
reliable system and kernel logging daemon  
Rsyslog is a multi-threaded implementation of syslogd (a system utility  
providing support for message logging), with features that include:  
reliable syslog over TCP, SSL/TLS and RELP  
on-demand disk buffering  
email alerting  
writing to MySQL or PostgreSQL databases (via separate output plugins)  
permitted sender lists  
filtering on any part of the syslog message  
on-the-wire message compression  
fine-grained output format control  
failover to backup destinations  
enterprise-class encrypted syslog relaying  
.  
It is the default syslogd on Debian systems.  

#### 2.123.2. Depended Packages
adduser  
libc6  
libestr0  
libfastjson4  
libsystemd0  
libuuid1  
libzstd1  
ucf  
zlib1g  

#### 2.123.3. Configuration Files
/etc/apparmor.d/rsyslog.d/README  
/etc/apparmor.d/usr.sbin.rsyslogd  
/etc/logcheck/ignore.d.server/rsyslog  
/etc/logrotate.d/rsyslog  
/etc/rsyslog.conf  

#### 2.123.4. Executable Files
/usr/sbin/rsyslogd  

<br>

### 2.124 shared-mime-info Package
#### 2.124.1. Official Package Description
FreeDesktop.org shared MIME database and spec  
This is the shared MIME-info database from the X Desktop Group. It is required  
by any program complying to the Shared MIME-Info Database spec, which is also  
included in this package.  
.  
At this time at least ROX, GNOME, KDE and Xfce use this database.  

#### 2.124.2. Depended Packages
libc6  
libgcc-s1  
libglib2.0-0t64  
libstdc++6  
libxml2  

#### 2.124.3. Configuration Files
(None)

#### 2.124.4. Executable Files
/usr/bin/update-mime-database  

<br>

### 2.125 sudo Package
#### 2.125.1. Official Package Description
Provide limited super user privileges to specific users  
Sudo is a program designed to allow a sysadmin to give limited root  
privileges to users and log root activity.  The basic philosophy is to give  
as few privileges as possible but still allow people to get their work done.  
.  
This version is built with minimal shared library dependencies, use the  
sudo-ldap package instead if you need LDAP support for sudoers.  

#### 2.125.2. Depended Packages
libapparmor1  
libaudit1  
libc6  
libpam-modules  
libpam0g  
libselinux1  
libssl3  
zlib1g  

#### 2.125.3. Configuration Files
/etc/pam.d/sudo  
/etc/pam.d/sudo  
/etc/pam.d/sudo-i  
/etc/pam.d/sudo-i  
/etc/sudo.conf  
/etc/sudo.conf  
/etc/sudo_logsrvd.conf  
/etc/sudo_logsrvd.conf  
/etc/sudoers  
/etc/sudoers  
/etc/sudoers.d/README  
/etc/sudoers.d/README  

#### 2.125.4. Executable Files
/usr/bin/cvtsudoers  
/usr/bin/cvtsudoers  
/usr/bin/sudo  
/usr/bin/sudo  
/usr/bin/sudoedit  
/usr/bin/sudoedit  
/usr/bin/sudoreplay  
/usr/bin/sudoreplay  
/usr/sbin/sudo_logsrvd  
/usr/sbin/sudo_logsrvd  
/usr/sbin/sudo_sendlog  
/usr/sbin/sudo_sendlog  
/usr/sbin/visudo  
/usr/sbin/visudo  

<br>

### 2.126 systemd Package
#### 2.126.1. Official Package Description
system and service manager  
systemd is a system and service manager for Linux. It provides aggressive  
parallelization capabilities, uses socket and D-Bus activation for starting  
services, offers on-demand starting of daemons, keeps track of processes using  
Linux control groups, maintains mount and automount points and implements an  
elaborate transactional dependency-based service control logic.  
.  
Installing the systemd package will not switch your init system unless you  
boot with init=/lib/systemd/systemd or install systemd-sysv in addition.  

#### 2.126.2. Depended Packages
libacl1  
libapparmor1  
libaudit1  
libblkid1  
libc6  
libcap2  
libcryptsetup12  
libfdisk1  
libgcrypt20  
libkmod2  
liblz4-1  
liblzma5  
libmount1  
libpam0g  
libseccomp2  
libselinux1  
libssl3t64  
libsystemd-shared  
libsystemd0  
libzstd1  
mount  
systemd-dev  

#### 2.126.3. Configuration Files
/etc/modules-load.d/modules.conf  
/etc/sysctl.d/99-sysctl.conf  
/etc/systemd/journald.conf  
/etc/systemd/logind.conf  
/etc/systemd/networkd.conf  
/etc/systemd/pstore.conf  
/etc/systemd/sleep.conf  
/etc/systemd/system-generators/systemd-gpt-auto-generator  
/etc/systemd/system.conf  
/etc/systemd/user.conf  
/etc/xdg/systemd/user  

#### 2.126.4. Executable Files
/usr/bin/busctl  
/usr/bin/hostnamectl  
/usr/bin/journalctl  
/usr/bin/kernel-install  
/usr/bin/localectl  
/usr/bin/loginctl  
/usr/bin/networkctl  
/usr/bin/systemctl  
/usr/bin/systemd  
/usr/bin/systemd-ac-power  
/usr/bin/systemd-analyze  
/usr/bin/systemd-ask-password  
/usr/bin/systemd-cat  
/usr/bin/systemd-cgls  
/usr/bin/systemd-cgtop  
/usr/bin/systemd-confext  
/usr/bin/systemd-creds  
/usr/bin/systemd-cryptenroll  
/usr/bin/systemd-cryptsetup  
/usr/bin/systemd-delta  
/usr/bin/systemd-detect-virt  
/usr/bin/systemd-escape  
/usr/bin/systemd-firstboot  
/usr/bin/systemd-id128  
/usr/bin/systemd-inhibit  
/usr/bin/systemd-machine-id-setup  
/usr/bin/systemd-mount  
/usr/bin/systemd-notify  
/usr/bin/systemd-path  
/usr/bin/systemd-repart  
/usr/bin/systemd-run  
/usr/bin/systemd-socket-activate  
/usr/bin/systemd-stdio-bridge  
/usr/bin/systemd-sysext  
/usr/bin/systemd-sysusers  
/usr/bin/systemd-sysusers  
/usr/bin/systemd-tmpfiles  
/usr/bin/systemd-tmpfiles  
/usr/bin/systemd-tty-ask-password-agent  
/usr/bin/systemd-umount  
/usr/bin/timedatectl  
/usr/bin/varlinkctl  

<br>

### 2.127 systemd-dev Package
#### 2.127.1. Official Package Description
systemd development files  
This package contains the systemd and udev pkg-config files. Note that these  
are different from the libsystemd's and libudev's pkg-config files, which can  
still be found in the respective dev packages, but instead provide data such as  
the installation directories for units, and more.  

#### 2.127.2. Depended Packages
(None)

#### 2.127.3. Configuration Files
(None)

#### 2.127.4. Executable Files
(None)

<br>

### 2.128 systemd-hwe-hwdb Package
#### 2.128.1. Official Package Description
udev rules for hardware enablement (HWE)  
systemd-hwe-hwdb contains hwdb rules for HWE on Ubuntu,  
which are not yet present in systemd.  

#### 2.128.2. Depended Packages
udev  

#### 2.128.3. Configuration Files
(None)

#### 2.128.4. Executable Files
(None)

<br>

### 2.129 systemd-resolved Package
#### 2.129.1. Official Package Description
systemd DNS resolver  
This package provides systemd's DNS resolver and the command line tool to  
manage it.  
.  
Installing this package automatically overwrites /etc/resolv.conf and switches  
it to be managed by systemd-resolved.  

#### 2.129.2. Depended Packages
default-dbus-system-bus  
libc6  
libssl3t64  
libsystemd-shared  
systemd  

#### 2.129.3. Configuration Files
/etc/systemd/resolved.conf  

#### 2.129.4. Executable Files
/usr/bin/resolvectl  
/usr/sbin/resolvconf  

<br>

### 2.130 systemd-sysv Package
#### 2.130.1. Official Package Description
system and service manager - SysV compatibility symlinks  
This package provides manual pages and compatibility symlinks needed for  
systemd to replace sysvinit.  
.  
Installing systemd-sysv will overwrite /sbin/init with a symlink to systemd.  

#### 2.130.2. Depended Packages
systemd  

#### 2.130.3. Configuration Files
(None)

#### 2.130.4. Executable Files
/usr/sbin/halt  
/usr/sbin/init  
/usr/sbin/poweroff  
/usr/sbin/reboot  
/usr/sbin/runlevel  
/usr/sbin/shutdown  
/usr/sbin/telinit  

<br>

### 2.131 systemd-timesyncd Package
#### 2.131.1. Official Package Description
minimalistic service to synchronize local time with NTP servers  
The package contains the systemd-timesyncd system service that may be used to  
synchronize the local system clock with a remote Network Time Protocol server.  

#### 2.131.2. Depended Packages
libc6  
libsystemd-shared  
systemd  

#### 2.131.3. Configuration Files
/etc/dhcp/dhclient-exit-hooks.d/timesyncd  
/etc/systemd/timesyncd.conf  

#### 2.131.4. Executable Files
(None)

<br>

### 2.132 tzdata Package
#### 2.132.1. Official Package Description
time zone and daylight-saving time data  
This package contains data required for the implementation of  
standard local time for many representative locations around the  
globe. It is updated periodically to reflect changes made by  
political bodies to time zone boundaries, UTC offsets, and  
daylight-saving rules.  

#### 2.132.2. Depended Packages
debconf  

#### 2.132.3. Configuration Files
(None)

#### 2.132.4. Executable Files
(None)

<br>

### 2.133 ubuntu-keyring Package
#### 2.133.1. Official Package Description
GnuPG keys of the Ubuntu archive  
The Ubuntu project digitally signs its Release files. This package  
contains the archive keys used for that.  

#### 2.133.2. Depended Packages
(None)

#### 2.133.3. Configuration Files
/etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg  
/etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg  

#### 2.133.4. Executable Files
(None)

<br>

### 2.134 ubuntu-minimal Package
#### 2.134.1. Official Package Description
Minimal core of Ubuntu  
This package depends on all of the packages in the Ubuntu minimal system,  
that is a functional command-line system with the following capabilities:  
.  
Boot  
Detect hardware  
Connect to a network  
Install packages  
Perform basic diagnostics  
.  
It is also used to help ensure proper upgrades, so it is recommended that  
it not be removed.  

#### 2.134.2. Depended Packages
adduser  
apt  
apt-utils  
console-setup  
debconf  
debconf-i18n  
dhcpcd-base  
e2fsprogs  
eject  
init  
iproute2  
iputils-ping  
kbd  
kmod  
less  
locales  
lsb-release  
mawk  
mount  
netbase  
netcat-openbsd  
netplan.io  
passwd  
procps  
python3  
sensible-utils  
sudo  
tzdata  
ubuntu-keyring  
ubuntu-pro-client  
udev  
vim-tiny  
whiptail  

#### 2.134.3. Configuration Files
(None)

#### 2.134.4. Executable Files
(None)

<br>

### 2.135 ubuntu-pro-client Package
#### 2.135.1. Official Package Description
Management tools for Ubuntu Pro  
Ubuntu Pro is a suite of additional services provided by Canonical on  
top of Ubuntu. Whether you're an enterprise customer deploying systems  
at scale or want security patching for your personal Ubuntu LTS  
at home, the Ubuntu Pro Client (pro) is the command-line tool that  
will help you manage the services you need.  

#### 2.135.2. Depended Packages
distro-info  
libapt-pkg6.0t64  
libc6  
libgcc-s1  
libjson-c5  
libstdc++6  
python3-apt  
python3-pkg-resources  
python3-yaml  
python3:any  

#### 2.135.3. Configuration Files
/etc/apparmor.d/ubuntu_pro_apt_news  
/etc/apt/apt.conf.d/20apt-esm-hook.conf  
/etc/apt/preferences.d/ubuntu-pro-esm-apps  
/etc/apt/preferences.d/ubuntu-pro-esm-infra  
/etc/logrotate.d/ubuntu-pro-client  
/etc/ubuntu-advantage/uaclient.conf  
/etc/update-manager/release-upgrades.d/ubuntu-advantage-upgrades.cfg  
/etc/update-motd.d/91-contract-ua-esm-status  

#### 2.135.4. Executable Files
/usr/bin/pro  
/usr/bin/ua  
/usr/bin/ubuntu-advantage  

<br>

### 2.136 ubuntu-pro-client-l10n Package
#### 2.136.1. Official Package Description
Translations for Ubuntu Pro Client  
This package delivers translations of Ubuntu Pro Client for various  
languages.  

#### 2.136.2. Depended Packages
ubuntu-pro-client  

#### 2.136.3. Configuration Files
(None)

#### 2.136.4. Executable Files
(None)

<br>

### 2.137 ucf Package
#### 2.137.1. Official Package Description
Update Configuration File(s): preserve user changes to config files  
Debian policy mandates that user changes to configuration files must be  
preserved during package upgrades. The easy way to achieve this behavior  
is to make the configuration file a 'conffile', in which case dpkg  
handles the file specially during upgrades, prompting the user as  
needed.  
.  
This is appropriate only if it is possible to distribute a default  
version that will work for most installations, although some system  
administrators may choose to modify it. This implies that the  
default version will be part of the package distribution, and must  
not be modified by the maintainer scripts during installation (or at  
any other time).  
.  
This script attempts to provide conffile-like handling for files that  
may not be labelled conffiles, and are not shipped in a Debian package,  
but handled by the postinst instead. This script allows one to  
maintain files in /etc, preserving user changes and in general  
offering the same facilities while upgrading that dpkg normally  
provides for 'conffiles'.  
.  
Additionally, this script provides facilities for transitioning a  
file that had not been provided with conffile-like protection to come  
under this schema, and attempts to minimize questions asked at  
installation time. Indeed, the transitioning facility is better than the  
one offered by dpkg while transitioning a file from a non-conffile to  
conffile status.  

#### 2.137.2. Depended Packages
debconf  
sensible-utils  

#### 2.137.3. Configuration Files
/etc/ucf.conf  

#### 2.137.4. Executable Files
/usr/bin/lcf  
/usr/bin/ucf  
/usr/bin/ucfq  
/usr/bin/ucfr  

<br>

### 2.138 udev Package
#### 2.138.1. Official Package Description
/dev/ and hotplug management daemon  
udev is a daemon which dynamically creates and removes device nodes from  
/dev/, handles hotplug events and loads drivers at boot time.  

#### 2.138.2. Depended Packages
libacl1  
libblkid1  
libc6  
libcap2  
libkmod2  
libselinux1  
libudev1  
systemd  
systemd-dev  

#### 2.138.3. Configuration Files
/etc/udev/iocost.conf  
/etc/udev/udev.conf  

#### 2.138.4. Executable Files
/usr/bin/systemd-hwdb  
/usr/bin/udevadm  

<br>

### 2.139 vim-common Package
#### 2.139.1. Official Package Description
Vi IMproved - Common files  
Vim is an almost compatible version of the UNIX editor Vi.  
.  
This package contains files shared by all non GUI-enabled vim variants  
available in Debian.  Examples of such shared files are: manpages and  
configuration files.  

#### 2.139.2. Depended Packages
(None)

#### 2.139.3. Configuration Files
/etc/vim/vimrc  

#### 2.139.4. Executable Files
/usr/bin/helpztags  

<br>

### 2.140 vim-tiny Package
#### 2.140.1. Official Package Description
Vi IMproved - enhanced vi editor - compact version  
Vim is an almost compatible version of the UNIX editor Vi.  
.  
This package contains a minimal version of Vim compiled with no GUI and  
a small subset of features. This package's sole purpose is to provide  
the vi binary for base installations.  
.  
If a vim binary is wanted, try one of the following more featureful  
packages: vim, vim-nox, vim-motif, or vim-gtk3.  

#### 2.140.2. Depended Packages
libacl1  
libc6  
libselinux1  
libtinfo6  
vim-common  

#### 2.140.3. Configuration Files
/etc/vim/vimrc.tiny  

#### 2.140.4. Executable Files
/usr/bin/vim.tiny  

<br>

### 2.141 whiptail Package
#### 2.141.1. Official Package Description
Displays user-friendly dialog boxes from shell scripts  
Whiptail is a "dialog" replacement using newt instead of ncurses. It  
provides a method of displaying several different types of dialog boxes  
from shell scripts. This allows a developer of a script to interact with  
the user in a much friendlier manner.  

#### 2.141.2. Depended Packages
libc6  
libnewt0.52  
libpopt0  
libslang2  

#### 2.141.3. Configuration Files
(None)

#### 2.141.4. Executable Files
/usr/bin/whiptail  

<br>

### 2.142 xdg-user-dirs Package
#### 2.142.1. Official Package Description
tool to manage well known user directories  
xdg-user-dirs is a tool to help manage "well known" user directories  
like the desktop folder and the music folder. It also handles  
localization (i.e. translation) of the filenames.  
.  
The way it works is that xdg-user-dirs-update is run very early in the  
login phase. This program reads a configuration file, and a set of  
default directories. It then creates localized versions of these  
directories in the users home directory and sets up a config file in  
$(XDG_CONFIG_HOME)/user-dirs.dirs (XDG_CONFIG_HOME defaults to  
~/.config) that applications can read to find these directories.  

#### 2.142.2. Depended Packages
libc6  

#### 2.142.3. Configuration Files
/etc/xdg/autostart/xdg-user-dirs.desktop  
/etc/xdg/user-dirs.conf  
/etc/xdg/user-dirs.defaults  

#### 2.142.4. Executable Files
/usr/bin/xdg-user-dir  
/usr/bin/xdg-user-dirs-update  

<br>

### 2.143 xkb-data Package
#### 2.143.1. Official Package Description
X Keyboard Extension (XKB) configuration data  
This package contains configuration data used by the X Keyboard  
Extension (XKB), which allows selection of keyboard layouts when  
using a graphical interface.  
.  
Every X11 vendor provides its own XKB data files, so keyboard layout  
designers have to send their layouts to several places.  The  
xkeyboard-config project has been launched at FreeDesktop in order  
to provide a central repository that could be used by all vendors.  

#### 2.143.2. Depended Packages
(None)

#### 2.143.3. Configuration Files
(None)

#### 2.143.4. Executable Files
(None)

<br>

### 2.144 xxd Package
#### 2.144.1. Official Package Description
tool to make (or reverse) a hex dump  
xxd creates a hex dump of a given file or standard input.  It can also convert  
a hex dump back to its original binary form.  

#### 2.144.2. Depended Packages
libc6  

#### 2.144.3. Configuration Files
(None)

#### 2.144.4. Executable Files
/usr/bin/xxd  

<br>

## 3. Standard Packages
---
These are the standard packages. They are normally expected in Debian installations.

At my last check, the following packages are marked as standard:

**apparmor:** user-space parser utility for AppArmor  
**bash-completion:** programmable completion for the bash shell  
**bind9-dnsutils:** Clients provided with BIND 9  
**bind9-host:** DNS Lookup Utility  
**bind9-libs:** Shared Libraries used by BIND 9  
**bsdextrautils:** extra utilities from 4.4BSD-Lite  
**busybox-static:** Standalone rescue shell with tons of builtin utilities  
**command-not-found:** Suggest installation of packages in interactive bash sessions  
**cpio:** GNU cpio -- a program to manage archives of files  
**cron:** process scheduling daemon  
**cron-daemon-common:** process scheduling daemon's configuration files  
**dmidecode:** SMBIOS/DMI table decoder  
**dosfstools:** utilities for making and checking MS-DOS FAT filesystems  
**ed:** classic UNIX line editor  
**file:** Recognize the type of data in a file using "magic" numbers  
**friendly-recovery:** Make recovery boot mode more user-friendly  
**ftp:** dummy transitional package for tnftp  
**fuse3:** Filesystem in Userspace (3.x version)  
**gettext-base:** GNU Internationalization utilities for the base system  
**groff-base:** GNU troff text-formatting system (base system components)  
**hdparm:** tune hard disk parameters for high performance  
**inetutils-telnet:** telnet client  
**info:** Standalone GNU Info documentation browser  
**install-info:** Manage installed documentation in info format  
**iptables:** administration tools for packet filtering and NAT  
**iputils-tracepath:** Tools to trace the network path to a remote host  
**libcbor0.10:** library for parsing and generating CBOR (RFC 7049)  
**libdrm-common:** Userspace interface to kernel DRM services -- common files  
**libdrm2:** Userspace interface to kernel DRM services -- runtime  
**libedit2:** BSD editline and history libraries  
**libfido2-1:** library for generating and verifying FIDO 2.0 objects  
**libfuse3-3:** Filesystem in Userspace (library) (3.x version)  
**libgdbm6t64:** GNU dbm database routines (runtime version)  
**libgpm2:** General Purpose Mouse - shared library  
**libip4tc2:** netfilter libip4tc library  
**libip6tc2:** netfilter libip6tc library  
**libjansson4:** C library for encoding, decoding and manipulating JSON data  
**liblmdb0:** Lightning Memory-Mapped Database shared library  
**libmagic-mgc:** File type determination library using "magic" numbers (compiled magic file)  
**libmaxminddb0:** IP geolocation database library  
**libncurses6:** shared libraries for terminal handling  
**libnetfilter-conntrack3:** Netfilter netlink-conntrack library  
**libnfnetlink0:** Netfilter netlink library  
**libnftables1:** Netfilter nftables high level userspace API library  
**libnftnl11:** Netfilter nftables userspace API library  
**libnghttp2-14:** library implementing HTTP/2 protocol (shared library)  
**libnss-systemd:** nss module providing dynamic user and group name resolution  
**libntfs-3g89t64:** read/write NTFS driver for FUSE (runtime library)  
**libnuma1:** Libraries for controlling NUMA policy  
**libpam-systemd:** system and service manager - PAM module  
**libparted2t64:** disk partition manipulator - shared library  
**libpci3:** PCI utilities (shared library)  
**libpipeline1:** Unix process pipeline manipulation library  
**libplymouth5:** graphical boot animation and logger - shared libraries  
**libpng16-16t64:** PNG library - runtime (version 1.6)  
**libpsl5t64:** Library for Public Suffix List (shared libraries)  
**libuchardet0:** universal charset detection library - shared library  
**libusb-1.0-0:** userspace USB programming library  
**libuv1t64:** asynchronous event notification library - runtime library  
**libx11-6:** X11 client-side library  
**libx11-data:** X11 client-side library  
**libxau6:** X11 authorisation library  
**libxcb1:** X C Binding  
**libxdmcp6:** X11 Display Manager Control Protocol library  
**libxext6:** X11 miscellaneous extension library  
**libxmuu1:** X11 miscellaneous micro-utility library  
**lshw:** information about hardware configuration  
**lsof:** utility to list open files  
**man-db:** tools for reading manual pages  
**manpages:** Manual pages about using a GNU/Linux system  
**mtr-tiny:** Full screen ncurses traceroute tool  
**nano:** small, friendly text editor inspired by Pico  
**nftables:** Program to control packet filtering rules by Netfilter project  
**ntfs-3g:** read/write NTFS driver for FUSE  
**openssh-client:** secure shell (SSH) client, for secure access to remote machines  
**parted:** disk partition manipulator  
**pci.ids:** PCI ID Repository  
**pciutils:** PCI utilities  
**perl:** Larry Wall's Practical Extraction and Report Language  
**plymouth:** boot animation, logger and I/O multiplexer  
**plymouth-theme-ubuntu-text:** boot animation, logger and I/O multiplexer - ubuntu text theme  
**powermgmt-base:** common utils for power management  
**psmisc:** utilities that use the proc file system  
**publicsuffix:** accurate, machine-readable list of domain name suffixes  
**python3-commandnotfound:** Python 3 bindings for command-not-found.  
**python3-distro-info:** information about distributions' releases (Python 3 module)  
**python3-distupgrade:** manage release upgrades  
**python3-gdbm:** GNU dbm database support for Python 3.x  
**python3-update-manager:** Python 3.x module for update-manager  
**rsync:** fast, versatile, remote (and local) file-copying tool  
**strace:** System call tracer  
**systemd-timesyncd:** minimalistic service to synchronize local time with NTP servers  
**tcpdump:** command-line network traffic analyzer  
**telnet:** transitional dummy package for inetutils-telnet default switch  
**time:** GNU time program for measuring CPU resource usage  
**tnftp:** enhanced ftp client  
**ubuntu-advantage-tools:** transitional dummy package for ubuntu-pro-client  
**ubuntu-release-upgrader-core:** manage release upgrades  
**ubuntu-standard:** Ubuntu standard system  
**ufw:** program for managing a Netfilter firewall  
**update-manager-core:** manage release upgrades  
**usb.ids:** USB ID Repository  
**usbutils:** Linux USB utilities  
**uuid-runtime:** runtime components for the Universally Unique ID library  
**wget:** retrieves files from the web  
**xauth:** X authentication utility  
**xz-utils:** XZ-format compression utilities  

<br>

### 3.1 apparmor Package
#### 3.1.1. Official Package Description
user-space parser utility for AppArmor  
apparmor provides the system initialization scripts needed to use the  
AppArmor Mandatory Access Control system, including the AppArmor Parser  
which is required to convert AppArmor text profiles into machine-readable  
policies that are loaded into the kernel for use with the AppArmor Linux  
Security Module.  

#### 3.1.2. Depended Packages
debconf  
libc6  
lsb-base  

#### 3.1.3. Configuration Files
/etc/apparmor.d/1password  
/etc/apparmor.d/Discord  
/etc/apparmor.d/MongoDB_Compass  
/etc/apparmor.d/QtWebEngineProcess  
/etc/apparmor.d/abi/3.0  
/etc/apparmor.d/abi/4.0  
/etc/apparmor.d/abi/kernel-5.4-outoftree-network  
/etc/apparmor.d/abi/kernel-5.4-vanilla  
/etc/apparmor.d/abstractions/X  
/etc/apparmor.d/abstractions/apache2-common  
/etc/apparmor.d/abstractions/apparmor_api/change_profile  
/etc/apparmor.d/abstractions/apparmor_api/examine  
/etc/apparmor.d/abstractions/apparmor_api/find_mountpoint  
/etc/apparmor.d/abstractions/apparmor_api/introspect  
/etc/apparmor.d/abstractions/apparmor_api/is_enabled  
/etc/apparmor.d/abstractions/aspell  
/etc/apparmor.d/abstractions/audio  
/etc/apparmor.d/abstractions/authentication  
/etc/apparmor.d/abstractions/base  
/etc/apparmor.d/abstractions/bash  
/etc/apparmor.d/abstractions/consoles  
/etc/apparmor.d/abstractions/crypto  
/etc/apparmor.d/abstractions/cups-client  
/etc/apparmor.d/abstractions/dbus  
/etc/apparmor.d/abstractions/dbus-accessibility  
/etc/apparmor.d/abstractions/dbus-accessibility-strict  
/etc/apparmor.d/abstractions/dbus-network-manager-strict  
/etc/apparmor.d/abstractions/dbus-session  
/etc/apparmor.d/abstractions/dbus-session-strict  
/etc/apparmor.d/abstractions/dbus-strict  
/etc/apparmor.d/abstractions/dconf  
/etc/apparmor.d/abstractions/dovecot-common  
/etc/apparmor.d/abstractions/dri-common  
/etc/apparmor.d/abstractions/dri-enumerate  
/etc/apparmor.d/abstractions/enchant  
/etc/apparmor.d/abstractions/exo-open  
/etc/apparmor.d/abstractions/fcitx  
/etc/apparmor.d/abstractions/fcitx-strict  
/etc/apparmor.d/abstractions/fonts  
/etc/apparmor.d/abstractions/freedesktop.org  
/etc/apparmor.d/abstractions/gio-open  
/etc/apparmor.d/abstractions/gnome  
/etc/apparmor.d/abstractions/gnupg  
/etc/apparmor.d/abstractions/groff  
/etc/apparmor.d/abstractions/gtk  
/etc/apparmor.d/abstractions/gvfs-open  
/etc/apparmor.d/abstractions/hosts_access  
/etc/apparmor.d/abstractions/ibus  
/etc/apparmor.d/abstractions/kde  
/etc/apparmor.d/abstractions/kde-globals-write  
/etc/apparmor.d/abstractions/kde-icon-cache-write  
/etc/apparmor.d/abstractions/kde-language-write  
/etc/apparmor.d/abstractions/kde-open5  
/etc/apparmor.d/abstractions/kerberosclient  
/etc/apparmor.d/abstractions/ldapclient  
/etc/apparmor.d/abstractions/libpam-systemd  
/etc/apparmor.d/abstractions/likewise  
/etc/apparmor.d/abstractions/mdns  
/etc/apparmor.d/abstractions/mesa  
/etc/apparmor.d/abstractions/mir  
/etc/apparmor.d/abstractions/mozc  
/etc/apparmor.d/abstractions/mysql  
/etc/apparmor.d/abstractions/nameservice  
/etc/apparmor.d/abstractions/nis  
/etc/apparmor.d/abstractions/nss-systemd  
/etc/apparmor.d/abstractions/nvidia  
/etc/apparmor.d/abstractions/opencl  
/etc/apparmor.d/abstractions/opencl-common  
/etc/apparmor.d/abstractions/opencl-intel  
/etc/apparmor.d/abstractions/opencl-mesa  
/etc/apparmor.d/abstractions/opencl-nvidia  
/etc/apparmor.d/abstractions/opencl-pocl  
/etc/apparmor.d/abstractions/openssl  
/etc/apparmor.d/abstractions/orbit2  
/etc/apparmor.d/abstractions/p11-kit  
/etc/apparmor.d/abstractions/perl  
/etc/apparmor.d/abstractions/php  
/etc/apparmor.d/abstractions/php-worker  
/etc/apparmor.d/abstractions/php5  
/etc/apparmor.d/abstractions/postfix-common  
/etc/apparmor.d/abstractions/private-files  
/etc/apparmor.d/abstractions/private-files-strict  
/etc/apparmor.d/abstractions/python  
/etc/apparmor.d/abstractions/qt5  
/etc/apparmor.d/abstractions/qt5-compose-cache-write  
/etc/apparmor.d/abstractions/qt5-settings-write  
/etc/apparmor.d/abstractions/recent-documents-write  
/etc/apparmor.d/abstractions/ruby  
/etc/apparmor.d/abstractions/samba  
/etc/apparmor.d/abstractions/samba-rpcd  
/etc/apparmor.d/abstractions/smbpass  
/etc/apparmor.d/abstractions/snap_browsers  
/etc/apparmor.d/abstractions/ssl_certs  
/etc/apparmor.d/abstractions/ssl_keys  
/etc/apparmor.d/abstractions/svn-repositories  
/etc/apparmor.d/abstractions/trash  
/etc/apparmor.d/abstractions/ubuntu-bittorrent-clients  
/etc/apparmor.d/abstractions/ubuntu-browsers  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/chromium-browser  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/java  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/kde  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/mailto  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/multimedia  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/plugins-common  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/productivity  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/text-editors  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/ubuntu-integration  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/ubuntu-integration-xul  
/etc/apparmor.d/abstractions/ubuntu-browsers.d/user-files  
/etc/apparmor.d/abstractions/ubuntu-console-browsers  
/etc/apparmor.d/abstractions/ubuntu-console-email  
/etc/apparmor.d/abstractions/ubuntu-email  
/etc/apparmor.d/abstractions/ubuntu-feed-readers  
/etc/apparmor.d/abstractions/ubuntu-gnome-terminal  
/etc/apparmor.d/abstractions/ubuntu-helpers  
/etc/apparmor.d/abstractions/ubuntu-konsole  
/etc/apparmor.d/abstractions/ubuntu-media-players  
/etc/apparmor.d/abstractions/ubuntu-unity7-base  
/etc/apparmor.d/abstractions/ubuntu-unity7-launcher  
/etc/apparmor.d/abstractions/ubuntu-unity7-messaging  
/etc/apparmor.d/abstractions/ubuntu-xterm  
/etc/apparmor.d/abstractions/user-download  
/etc/apparmor.d/abstractions/user-mail  
/etc/apparmor.d/abstractions/user-manpages  
/etc/apparmor.d/abstractions/user-tmp  
/etc/apparmor.d/abstractions/user-write  
/etc/apparmor.d/abstractions/video  
/etc/apparmor.d/abstractions/vulkan  
/etc/apparmor.d/abstractions/wayland  
/etc/apparmor.d/abstractions/web-data  
/etc/apparmor.d/abstractions/winbind  
/etc/apparmor.d/abstractions/wutmp  
/etc/apparmor.d/abstractions/xad  
/etc/apparmor.d/abstractions/xdg-desktop  
/etc/apparmor.d/abstractions/xdg-open  
/etc/apparmor.d/brave  
/etc/apparmor.d/buildah  
/etc/apparmor.d/busybox  
/etc/apparmor.d/cam  
/etc/apparmor.d/ch-checkns  
/etc/apparmor.d/ch-run  
/etc/apparmor.d/chrome  
/etc/apparmor.d/code  
/etc/apparmor.d/crun  
/etc/apparmor.d/devhelp  
/etc/apparmor.d/element-desktop  
/etc/apparmor.d/epiphany  
/etc/apparmor.d/evolution  
/etc/apparmor.d/firefox  
/etc/apparmor.d/flatpak  
/etc/apparmor.d/geary  
/etc/apparmor.d/github-desktop  
/etc/apparmor.d/goldendict  
/etc/apparmor.d/ipa_verify  
/etc/apparmor.d/kchmviewer  
/etc/apparmor.d/keybase  
/etc/apparmor.d/lc-compliance  
/etc/apparmor.d/libcamerify  
/etc/apparmor.d/linux-sandbox  
/etc/apparmor.d/local/README  
/etc/apparmor.d/loupe  
/etc/apparmor.d/lsb_release  
/etc/apparmor.d/lxc-attach  
/etc/apparmor.d/lxc-create  
/etc/apparmor.d/lxc-destroy  
/etc/apparmor.d/lxc-execute  
/etc/apparmor.d/lxc-stop  
/etc/apparmor.d/lxc-unshare  
/etc/apparmor.d/lxc-usernsexec  
/etc/apparmor.d/mmdebstrap  
/etc/apparmor.d/msedge  
/etc/apparmor.d/nautilus  
/etc/apparmor.d/notepadqq  
/etc/apparmor.d/nvidia_modprobe  
/etc/apparmor.d/obsidian  
/etc/apparmor.d/opam  
/etc/apparmor.d/opera  
/etc/apparmor.d/pageedit  
/etc/apparmor.d/plasmashell  
/etc/apparmor.d/podman  
/etc/apparmor.d/polypane  
/etc/apparmor.d/privacybrowser  
/etc/apparmor.d/qcam  
/etc/apparmor.d/qmapshack  
/etc/apparmor.d/qutebrowser  
/etc/apparmor.d/rootlesskit  
/etc/apparmor.d/rpm  
/etc/apparmor.d/rssguard  
/etc/apparmor.d/runc  
/etc/apparmor.d/sbuild  
/etc/apparmor.d/sbuild-abort  
/etc/apparmor.d/sbuild-adduser  
/etc/apparmor.d/sbuild-apt  
/etc/apparmor.d/sbuild-checkpackages  
/etc/apparmor.d/sbuild-clean  
/etc/apparmor.d/sbuild-createchroot  
/etc/apparmor.d/sbuild-destroychroot  
/etc/apparmor.d/sbuild-distupgrade  
/etc/apparmor.d/sbuild-hold  
/etc/apparmor.d/sbuild-shell  
/etc/apparmor.d/sbuild-unhold  
/etc/apparmor.d/sbuild-update  
/etc/apparmor.d/sbuild-upgrade  
/etc/apparmor.d/scide  
/etc/apparmor.d/signal-desktop  
/etc/apparmor.d/slack  
/etc/apparmor.d/slirp4netns  
/etc/apparmor.d/steam  
/etc/apparmor.d/stress-ng  
/etc/apparmor.d/surfshark  
/etc/apparmor.d/systemd-coredump  
/etc/apparmor.d/thunderbird  
/etc/apparmor.d/toybox  
/etc/apparmor.d/trinity  
/etc/apparmor.d/tunables/alias  
/etc/apparmor.d/tunables/apparmorfs  
/etc/apparmor.d/tunables/dovecot  
/etc/apparmor.d/tunables/etc  
/etc/apparmor.d/tunables/global  
/etc/apparmor.d/tunables/home  
/etc/apparmor.d/tunables/home.d/site.local  
/etc/apparmor.d/tunables/kernelvars  
/etc/apparmor.d/tunables/multiarch  
/etc/apparmor.d/tunables/multiarch.d/site.local  
/etc/apparmor.d/tunables/proc  
/etc/apparmor.d/tunables/run  
/etc/apparmor.d/tunables/securityfs  
/etc/apparmor.d/tunables/share  
/etc/apparmor.d/tunables/sys  
/etc/apparmor.d/tunables/xdg-user-dirs  
/etc/apparmor.d/tup  
/etc/apparmor.d/tuxedo-control-center  
/etc/apparmor.d/unix-chkpwd  
/etc/apparmor.d/unprivileged_userns  
/etc/apparmor.d/userbindmount  
/etc/apparmor.d/uwsgi-core  
/etc/apparmor.d/vdens  
/etc/apparmor.d/virtiofsd  
/etc/apparmor.d/vivaldi-bin  
/etc/apparmor.d/vpnns  
/etc/apparmor.d/wpcom  
/etc/apparmor/parser.conf  
/etc/init.d/apparmor  

#### 3.1.4. Executable Files
/sbin/apparmor_parser  
/usr/bin/aa-enabled  
/usr/bin/aa-exec  
/usr/bin/aa-features-abi  
/usr/sbin/aa-load  
/usr/sbin/aa-remove-unknown  
/usr/sbin/aa-status  
/usr/sbin/aa-teardown  
/usr/sbin/apparmor_status  

<br>

### 3.2 bash-completion Package
#### 3.2.1. Official Package Description
programmable completion for the bash shell  
bash completion extends bash's standard completion behavior to achieve  
complex command lines with just a few keystrokes.  This project was  
conceived to produce programmable completion routines for the most  
common Linux/UNIX commands, reducing the amount of typing sysadmins  
and programmers need to do on a daily basis.  

#### 3.2.2. Depended Packages
(None)

#### 3.2.3. Configuration Files
/etc/bash_completion  
/etc/profile.d/bash_completion.sh  

#### 3.2.4. Executable Files
/usr/bin/dh_bash-completion  

<br>

### 3.3 bind9-dnsutils Package
#### 3.3.1. Official Package Description
Clients provided with BIND 9  
The Berkeley Internet Name Domain (BIND 9) implements an Internet domain  
name server.  BIND 9 is the most widely-used name server software on the  
Internet, and is supported by the Internet Software Consortium, www.isc.org.  
.  
This package delivers various client programs related to DNS that are  
derived from the BIND 9 source tree.  
.  
dig - query the DNS in various ways  
nslookup - the older way to do it  
nsupdate - perform dynamic updates (See RFC2136)  

#### 3.3.2. Depended Packages
bind9-host  
bind9-libs  
libc6  
libedit2  
libidn2-0  
libkrb5-3  

#### 3.3.3. Configuration Files
(None)

#### 3.3.4. Executable Files
/usr/bin/delv  
/usr/bin/dig  
/usr/bin/mdig  
/usr/bin/nslookup  
/usr/bin/nsupdate  

<br>

### 3.4 bind9-host Package
#### 3.4.1. Official Package Description
DNS Lookup Utility  
This package provides the 'host' DNS lookup utility in the form that  
is bundled with the BIND 9 sources.  

#### 3.4.2. Depended Packages
bind9-libs  
libc6  
libidn2-0  

#### 3.4.3. Configuration Files
(None)

#### 3.4.4. Executable Files
/usr/bin/host  

<br>

### 3.5 bind9-libs Package
#### 3.5.1. Official Package Description
Shared Libraries used by BIND 9  
The Berkeley Internet Name Domain (BIND 9) implements an Internet domain  
name server.  BIND 9 is the most widely-used name server software on the  
Internet, and is supported by the Internet Software Consortium, www.isc.org.  
.  
This package contains a bundle of shared libraries used by BIND 9.  

#### 3.5.2. Depended Packages
libc6  
libgssapi-krb5-2  
libjson-c5  
libkrb5-3  
liblmdb0  
libmaxminddb0  
libnghttp2-14  
libssl3  
libuv1  
libuv1t64  
libxml2  
zlib1g  

#### 3.5.3. Configuration Files
(None)

#### 3.5.4. Executable Files
(None)

<br>

### 3.6 bsdextrautils Package
#### 3.6.1. Official Package Description
extra utilities from 4.4BSD-Lite  
This package contains some extra BSD utilities: col, colcrt, colrm, column,  
hd, hexdump, look, ul and write.  
Other BSD utilities are provided by bsdutils and calendar.  

#### 3.6.2. Depended Packages
libc6  
libsmartcols1  
libtinfo6  

#### 3.6.3. Configuration Files
(None)

#### 3.6.4. Executable Files
/usr/bin/col  
/usr/bin/colcrt  
/usr/bin/colrm  
/usr/bin/column  
/usr/bin/hd  
/usr/bin/hexdump  
/usr/bin/look  
/usr/bin/ul  
/usr/bin/write  

<br>

### 3.7 busybox-static Package
#### 3.7.1. Official Package Description
Standalone rescue shell with tons of builtin utilities  
BusyBox combines tiny versions of many common UNIX utilities into a single  
small executable. It provides minimalist replacements for the most common  
utilities you would usually find on your desktop system (i.e., ls, cp, mv,  
mount, tar, etc.).  The utilities in BusyBox generally have fewer options than  
their full-featured GNU cousins; however, the options that are included  
provide the expected functionality and behave very much like their GNU  
counterparts.  
.  
busybox-static provides you with a statically linked simple stand alone shell  
that provides all the utilities available in BusyBox. This package is  
intended to be used as a rescue shell, in the event that you screw up your  
system. Invoke "busybox sh" and you have a standalone shell ready to save  
your system from certain destruction. Invoke "busybox", and it will list the  
available builtin commands.  

#### 3.7.2. Depended Packages
(None)

#### 3.7.3. Configuration Files
(None)

#### 3.7.4. Executable Files
/bin/static-sh  
/usr/bin/busybox  

<br>

### 3.8 command-not-found Package
#### 3.8.1. Official Package Description
Suggest installation of packages in interactive bash sessions  
This package will install a handler for command_not_found that looks up  
programs not currently installed but available from the repositories.  

#### 3.8.2. Depended Packages
python3-commandnotfound  

#### 3.8.3. Configuration Files
/etc/apt/apt.conf.d/50command-not-found  
/etc/zsh_command_not_found  

#### 3.8.4. Executable Files
(None)

<br>

### 3.9 cpio Package
#### 3.9.1. Official Package Description
GNU cpio -- a program to manage archives of files  
GNU cpio is a tool for creating and extracting archives, or copying  
files from one place to another.  It handles a number of cpio formats  
as well as reading and writing tar files.  

#### 3.9.2. Depended Packages
libc6  

#### 3.9.3. Configuration Files
(None)

#### 3.9.4. Executable Files
/usr/bin/cpio  
/usr/bin/mt-gnu  

<br>

### 3.10 cron Package
#### 3.10.1. Official Package Description
process scheduling daemon  
The cron daemon is a background process that runs particular programs at  
particular times (for example, every minute, day, week, or month), as  
specified in a crontab. By default, users may also create crontabs of  
their own so that processes are run on their behalf.  
.  
Output from the commands is usually mailed to the system administrator  
(or to the user in question); you should probably install a mail system  
as well so that you can receive these messages.  
.  
This cron package does not provide any system maintenance tasks. Basic  
periodic maintenance tasks are provided by other packages, such  
as checksecurity.  

#### 3.10.2. Depended Packages
cron-daemon-common  
init-system-helpers  
libc6  
libpam-runtime  
libpam0g  
libselinux1  
sensible-utils  

#### 3.10.3. Configuration Files
/etc/default/cron  
/etc/init.d/cron  
/etc/pam.d/cron  
/etc/supercat/spcrc-crontab  
/etc/supercat/spcrc-crontab-light  

#### 3.10.4. Executable Files
/usr/bin/crontab  
/usr/bin/crontab  
/usr/bin/crontab  
/usr/bin/crontab  
/usr/sbin/cron  

<br>

### 3.11 cron-daemon-common Package
#### 3.11.1. Official Package Description
process scheduling daemon's configuration files  
The cron daemon is a background process that runs particular programs at  
particular times (for example, every minute, day, week, or month), as  
specified in a crontab. By default, users may also create crontabs of  
their own so that processes are run on their behalf.  
.  
This package provides configuration files which must be there to  
define scheduled process sets.  

#### 3.11.2. Depended Packages
adduser  
systemd  

#### 3.11.3. Configuration Files
/etc/cron.d/.placeholder  
/etc/cron.daily/.placeholder  
/etc/cron.hourly/.placeholder  
/etc/cron.monthly/.placeholder  
/etc/cron.weekly/.placeholder  
/etc/cron.yearly/.placeholder  
/etc/crontab  

#### 3.11.4. Executable Files
(None)

<br>

### 3.12 dmidecode Package
#### 3.12.1. Official Package Description
SMBIOS/DMI table decoder  
Dmidecode reports information about the system's hardware as described in the  
system BIOS according to the SMBIOS/DMI standard.  
.  
This information typically includes system manufacturer, model name, serial  
number, BIOS version, asset tag as well as a lot of other details of varying  
level of interest and reliability depending on the manufacturer. This will  
often include usage status for the CPU sockets, expansion slots (e.g. AGP, PCI,  
ISA) and memory module slots, and the list of I/O ports (e.g. serial, parallel,  
USB).  
.  
Beware that DMI data have proven to be too unreliable to be blindly trusted.  
Dmidecode does not scan the hardware, it only reports what the BIOS told it to.  

#### 3.12.2. Depended Packages
libc6  

#### 3.12.3. Configuration Files
(None)

#### 3.12.4. Executable Files
/usr/sbin/biosdecode  
/usr/sbin/dmidecode  
/usr/sbin/ownership  
/usr/sbin/vpddecode  

<br>

### 3.13 dosfstools Package
#### 3.13.1. Official Package Description
utilities for making and checking MS-DOS FAT filesystems  
The dosfstools package includes the mkfs.fat and fsck.fat utilities, which  
respectively make and check MS-DOS FAT filesystems.  

#### 3.13.2. Depended Packages
libc6  

#### 3.13.3. Configuration Files
(None)

#### 3.13.4. Executable Files
/usr/sbin/dosfsck  
/usr/sbin/dosfslabel  
/usr/sbin/fatlabel  
/usr/sbin/fsck.fat  
/usr/sbin/fsck.msdos  
/usr/sbin/fsck.vfat  
/usr/sbin/mkdosfs  
/usr/sbin/mkfs.fat  
/usr/sbin/mkfs.msdos  
/usr/sbin/mkfs.vfat  

<br>

### 3.14 ed Package
#### 3.14.1. Official Package Description
classic UNIX line editor  
ed is a line-oriented text editor.  It is used to  
create, display, modify and otherwise manipulate text  
files.  
.  
red is a restricted ed: it can only edit files in the  
current directory and cannot execute shell commands.  

#### 3.14.2. Depended Packages
libc6  

#### 3.14.3. Configuration Files
(None)

#### 3.14.4. Executable Files
/bin/ed  
/bin/red  

<br>

### 3.15 file Package
#### 3.15.1. Official Package Description
Recognize the type of data in a file using "magic" numbers  
The file command is "a file type guesser", a command-line tool that  
tells you in words what kind of data a file contains.  
.  
This package contains the file program itself.  

#### 3.15.2. Depended Packages
libc6  
libmagic1t64  

#### 3.15.3. Configuration Files
(None)

#### 3.15.4. Executable Files
/usr/bin/file  

<br>

### 3.16 friendly-recovery Package
#### 3.16.1. Official Package Description
Make recovery boot mode more user-friendly  
Make the recovery boot mode more user-friendly by providing a menu  
with pluggable options.  

#### 3.16.2. Depended Packages
systemd-sysv  
whiptail  

#### 3.16.3. Configuration Files
(None)

#### 3.16.4. Executable Files
(None)

<br>

### 3.17 ftp Package
#### 3.17.1. Official Package Description
dummy transitional package for tnftp  
This is a dummy transitional package transitioning ftp to tnftp.  

#### 3.17.2. Depended Packages
tnftp  

#### 3.17.3. Configuration Files
(None)

#### 3.17.4. Executable Files
(None)

<br>

### 3.18 fuse3 Package
#### 3.18.1. Official Package Description
Filesystem in Userspace (3.x version)  
Filesystem in Userspace (FUSE) is a simple interface for userspace programs to  
export a virtual filesystem to the Linux kernel. It also aims to provide a  
secure method for non privileged users to create and mount their own filesystem  
implementations.  

#### 3.18.2. Depended Packages
adduser  
libc6  
libfuse3-3  
mount  
sed  

#### 3.18.3. Configuration Files
/etc/fuse.conf  

#### 3.18.4. Executable Files
/bin/fusermount  
/bin/fusermount3  
/sbin/mount.fuse  
/sbin/mount.fuse3  

<br>

### 3.19 gettext-base Package
#### 3.19.1. Official Package Description
GNU Internationalization utilities for the base system  
This package includes the gettext and ngettext programs which allow  
other packages to internationalize the messages given by shell scripts.  

#### 3.19.2. Depended Packages
libc6  

#### 3.19.3. Configuration Files
(None)

#### 3.19.4. Executable Files
/usr/bin/envsubst  
/usr/bin/gettext  
/usr/bin/gettext.sh  
/usr/bin/ngettext  

<br>

### 3.20 groff-base Package
#### 3.20.1. Official Package Description
GNU troff text-formatting system (base system components)  
This package contains the traditional UN*X text formatting tools  
troff, nroff, tbl, eqn, and pic. These utilities, together with the  
man-db package, are essential for displaying the on-line manual pages.  
.  
groff-base is a stripped-down package containing the necessary components  
to read manual pages in ASCII, Latin-1, and UTF-8, plus the PostScript  
device (groff's default). Users who want a full groff installation, with  
the standard set of devices, fonts, macros, and documentation, should  
install the groff package.  

#### 3.20.2. Depended Packages
libc6  
libgcc-s1  
libstdc++6  
libuchardet0  

#### 3.20.3. Configuration Files
/etc/groff/man.local  
/etc/groff/mdoc.local  

#### 3.20.4. Executable Files
/usr/bin/eqn  
/usr/bin/geqn  
/usr/bin/gpic  
/usr/bin/groff  
/usr/bin/grog  
/usr/bin/grops  
/usr/bin/grotty  
/usr/bin/gtbl  
/usr/bin/neqn  
/usr/bin/nroff  
/usr/bin/pic  
/usr/bin/preconv  
/usr/bin/soelim  
/usr/bin/tbl  
/usr/bin/troff  

<br>

### 3.21 hdparm Package
#### 3.21.1. Official Package Description
tune hard disk parameters for high performance  
Get/set device parameters for Linux SATA/IDE drives.  
Provides a command line interface to various kernel interfaces supported by  
the Linux SATA/PATA/SAS "libata" subsystem and the older IDE driver subsystem.  
Many newer (2008 and later) USB drive enclosures now also support "SAT"  
(SCSI-ATA Command Translation) and therefore may also work with hdparm.  

#### 3.21.2. Depended Packages
libc6  
lsb-base  

#### 3.21.3. Configuration Files
/etc/hdparm.conf  

#### 3.21.4. Executable Files
/sbin/hdparm  

<br>

### 3.22 inetutils-telnet Package
#### 3.22.1. Official Package Description
telnet client  
The telnet command is used for interactive communication with another host  
using the TELNET protocol.  
.  
This implementation supports Kerberos, for authentication and encryption.  

#### 3.22.2. Depended Packages
libc6  
libcom-err2  
libk5crypto3  
libkrb5-3  
libtinfo6  
netbase  

#### 3.22.3. Configuration Files
(None)

#### 3.22.4. Executable Files
/usr/bin/inetutils-telnet  

<br>

### 3.23 info Package
#### 3.23.1. Official Package Description
Standalone GNU Info documentation browser  
The Info file format is an easily-parsable representation for online  
documents. This program allows you to view Info documents, like the  
ones stored in /usr/share/info.  
.  
Much of the software in Debian comes with its online documentation in  
the form of Info files, so it is most likely you will want to install it.  

#### 3.23.2. Depended Packages
install-info  
libc6  
libtinfo6  

#### 3.23.3. Configuration Files
(None)

#### 3.23.4. Executable Files
/usr/bin/info  

<br>

### 3.24 install-info Package
#### 3.24.1. Official Package Description
Manage installed documentation in info format  
The install-info utility creates the index of all installed documentation  
in info format and makes it available to info readers.  

#### 3.24.2. Depended Packages
libc6  

#### 3.24.3. Configuration Files
(None)

#### 3.24.4. Executable Files
/usr/bin/ginstall-info  
/usr/bin/install-info  
/usr/sbin/update-info-dir  

<br>

### 3.25 iptables Package
#### 3.25.1. Official Package Description
administration tools for packet filtering and NAT  
The iptables/xtables framework has been replaced by nftables. You should  
consider migrating now.  
.  
iptables is the userspace command line program used to configure  
the Linux packet filtering and NAT ruleset. It is targeted towards systems  
and networks administrators.  
.  
This package contains several different utilities, the most important ones:  
.  
iptables-nft, iptables-nft-save, iptables-nft-restore (nft-based version)  
.  
iptables-legacy, iptables-legacy-save, iptables-legacy-restore (legacy version)  
.  
ip6tables-nft, ip6tables-nft-save, ip6tables-nft-restore (nft-based version)  
.  
ip6tables-legacy, ip6tables-legacy-save, ip6tables-legacy-restore (legacy  
version)  
.  
arptables-nft, arptables-nft-save, arptables-nft-restore (nft-based version)  
.  
ebtables-nft, ebtables-nft-save, ebtables-nft-restore (nft-based version)  

#### 3.25.2. Depended Packages
libc6  
libip4tc2  
libip6tc2  
libmnl0  
libnetfilter-conntrack3  
libnfnetlink0  
libnftnl11  
libxtables12  
netbase  

#### 3.25.3. Configuration Files
(None)

#### 3.25.4. Executable Files
/usr/bin/iptables-xml  
/usr/sbin/arptables-nft  
/usr/sbin/arptables-nft-restore  
/usr/sbin/arptables-nft-save  
/usr/sbin/ebtables-nft  
/usr/sbin/ebtables-nft-restore  
/usr/sbin/ebtables-nft-save  
/usr/sbin/ebtables-translate  
/usr/sbin/ip6tables-apply  
/usr/sbin/ip6tables-legacy  
/usr/sbin/ip6tables-legacy-restore  
/usr/sbin/ip6tables-legacy-save  
/usr/sbin/ip6tables-nft  
/usr/sbin/ip6tables-nft-restore  
/usr/sbin/ip6tables-nft-save  
/usr/sbin/ip6tables-restore-translate  
/usr/sbin/ip6tables-translate  
/usr/sbin/iptables-apply  
/usr/sbin/iptables-legacy  
/usr/sbin/iptables-legacy-restore  
/usr/sbin/iptables-legacy-save  
/usr/sbin/iptables-nft  
/usr/sbin/iptables-nft-restore  
/usr/sbin/iptables-nft-save  
/usr/sbin/iptables-restore-translate  
/usr/sbin/iptables-translate  
/usr/sbin/nfnl_osf  
/usr/sbin/xtables-legacy-multi  
/usr/sbin/xtables-monitor  
/usr/sbin/xtables-nft-multi  

<br>

### 3.26 iputils-tracepath Package
#### 3.26.1. Official Package Description
Tools to trace the network path to a remote host  
The tracepath utility is similar to the traceroute utility, but also  
attempts to discover the MTU of the path. Supports IPv4 and IPv6.  

#### 3.26.2. Depended Packages
libc6  

#### 3.26.3. Configuration Files
(None)

#### 3.26.4. Executable Files
/usr/bin/tracepath  

<br>

### 3.27 libcbor0.10 Package
#### 3.27.1. Official Package Description
library for parsing and generating CBOR (RFC 7049)  
CBOR is a general-purpose schema-less binary data format, defined in  
RFC 7049. This package provides a C library for parsing and generating  
CBOR. The main features are:  
.  
Complete RFC conformance  
Robust C99 implementation  
Layered architecture offers both control and convenience  
Flexible memory management  
No shared global state - threading friendly  
Proper handling of UTF-8  
Full support for streams & incremental processing  
Extensive documentation and test suite  
No runtime dependencies, small footprint  
.  
This package contains the runtime library.  

#### 3.27.2. Depended Packages
libc6  

#### 3.27.3. Configuration Files
(None)

#### 3.27.4. Executable Files
(None)

<br>

### 3.28 libdrm-common Package
#### 3.28.1. Official Package Description
Userspace interface to kernel DRM services -- common files  
This library implements the userspace interface to the kernel DRM  
services.  DRM stands for "Direct Rendering Manager", which is the  
kernelspace portion of the "Direct Rendering Infrastructure" (DRI).  
The DRI is currently used on Linux to provide hardware-accelerated  
OpenGL drivers.  
.  
This package provides common files for libdrm.  

#### 3.28.2. Depended Packages
(None)

#### 3.28.3. Configuration Files
(None)

#### 3.28.4. Executable Files
(None)

<br>

### 3.29 libdrm2 Package
#### 3.29.1. Official Package Description
Userspace interface to kernel DRM services -- runtime  
This library implements the userspace interface to the kernel DRM  
services.  DRM stands for "Direct Rendering Manager", which is the  
kernelspace portion of the "Direct Rendering Infrastructure" (DRI).  
The DRI is currently used on Linux to provide hardware-accelerated  
OpenGL drivers.  
.  
This package provides the runtime environment for libdrm.  

#### 3.29.2. Depended Packages
libc6  
libdrm-common  

#### 3.29.3. Configuration Files
(None)

#### 3.29.4. Executable Files
(None)

<br>

### 3.30 libedit2 Package
#### 3.30.1. Official Package Description
BSD editline and history libraries  
Command line editor library provides generic line editing,  
history, and tokenization functions.  
.  
It slightly resembles GNU readline.  

#### 3.30.2. Depended Packages
libbsd0  
libc6  
libtinfo6  

#### 3.30.3. Configuration Files
(None)

#### 3.30.4. Executable Files
(None)

<br>

### 3.31 libfido2-1 Package
#### 3.31.1. Official Package Description
library for generating and verifying FIDO 2.0 objects  
A library for communicating with a FIDO device over USB or NFC, and for  
verifying attestation and assertion signatures. FIDO U2F (CTAP 1) and FIDO  
2.0 (CTAP 2) are supported.  
.  
This package contains the library.  

#### 3.31.2. Depended Packages
libc6  
libcbor0.10  
libssl3  
libudev1  
zlib1g  

#### 3.31.3. Configuration Files
(None)

#### 3.31.4. Executable Files
(None)

<br>

### 3.32 libfuse3-3 Package
#### 3.32.1. Official Package Description
Filesystem in Userspace (library) (3.x version)  
Filesystem in Userspace (FUSE) is a simple interface for userspace programs to  
export a virtual filesystem to the Linux kernel. It also aims to provide a  
secure method for non privileged users to create and mount their own filesystem  
implementations.  
.  
This package contains the shared library.  

#### 3.32.2. Depended Packages
libc6  

#### 3.32.3. Configuration Files
(None)

#### 3.32.4. Executable Files
(None)

<br>

### 3.33 libgdbm6t64 Package
#### 3.33.1. Official Package Description
GNU dbm database routines (runtime version)  
GNU dbm ('gdbm') is a library of database functions that use extendible  
hashing and works similarly to the standard UNIX 'dbm' functions.  
.  
The basic use of 'gdbm' is to store key/data pairs in a data file, thus  
providing a persistent version of the 'dictionary' Abstract Data Type  
('hash' to perl programmers).  

#### 3.33.2. Depended Packages
libc6  

#### 3.33.3. Configuration Files
(None)

#### 3.33.4. Executable Files
(None)

<br>

### 3.34 libgpm2 Package
#### 3.34.1. Official Package Description
General Purpose Mouse - shared library  
This package provides a library that handles mouse requests  
and delivers them to applications. See the description for the 'gpm'  
package for more information.  

#### 3.34.2. Depended Packages
libc6  

#### 3.34.3. Configuration Files
(None)

#### 3.34.4. Executable Files
(None)

<br>

### 3.35 libip4tc2 Package
#### 3.35.1. Official Package Description
netfilter libip4tc library  
The iptables/xtables framework has been replaced by nftables. You should  
consider migrating now.  
.  
This package contains the user-space iptables (IPv4) C library from the  
Netfilter xtables framework.  
.  
iptables IPv4 ruleset ADT and kernel interface.  
.  
This library has been considered private for years (and still is), in the  
sense of changing symbols and backward compatibility not guaranteed.  

#### 3.35.2. Depended Packages
libc6  

#### 3.35.3. Configuration Files
(None)

#### 3.35.4. Executable Files
(None)

<br>

### 3.36 libip6tc2 Package
#### 3.36.1. Official Package Description
netfilter libip6tc library  
The iptables/xtables framework has been replaced by nftables. You should  
consider migrating now.  
.  
This package contains the user-space iptables (IPv6) C library from the  
Netfilter xtables framework.  
.  
iptables IPv6 ruleset ADT and kernel interface.  
.  
This library has been considered private for years (and still is), in the  
sense of changing symbols and backward compatibility not guaranteed.  

#### 3.36.2. Depended Packages
libc6  

#### 3.36.3. Configuration Files
(None)

#### 3.36.4. Executable Files
(None)

<br>

### 3.37 libjansson4 Package
#### 3.37.1. Official Package Description
C library for encoding, decoding and manipulating JSON data  
Jansson is a C library for encoding, decoding and manipulating JSON data.  
.  
It features:  
Simple and intuitive API and data model  
Comprehensive documentation  
No dependencies on other libraries  
Full Unicode support (UTF-8)  
Extensive test suite  

#### 3.37.2. Depended Packages
libc6  

#### 3.37.3. Configuration Files
(None)

#### 3.37.4. Executable Files
(None)

<br>

### 3.38 liblmdb0 Package
#### 3.38.1. Official Package Description
Lightning Memory-Mapped Database shared library  
This package contains the LMDB shared library.  
.  
Lighting Memory-Mapped Database (LMDB) is an ultra-fast, ultra-compact  
key-value embedded data store developed for the OpenLDAP Project.  It uses  
memory-mapped files, so it has the read performance of a pure in-memory  
database while still offering the persistence of standard disk-based  
databases, and is only limited to the size of the virtual address space, (it  
is not limited to the size of physical RAM).  

#### 3.38.2. Depended Packages
libc6  

#### 3.38.3. Configuration Files
(None)

#### 3.38.4. Executable Files
(None)

<br>

### 3.39 libmagic-mgc Package
#### 3.39.1. Official Package Description
File type determination library using "magic" numbers (compiled magic file)  
This package provides the compiled magic file "magic.mgc". It has  
been separated from libmagic1t64 in order to meet the multiarch  
requirements without breaking applications that expect this file  
at its absolute path.  

#### 3.39.2. Depended Packages
(None)

#### 3.39.3. Configuration Files
(None)

#### 3.39.4. Executable Files
(None)

<br>

### 3.40 libmaxminddb0 Package
#### 3.40.1. Official Package Description
IP geolocation database library  
The libmaxminddb library provides a C library for reading MaxMind DB files,  
including the GeoIP2 databases from MaxMind. This is a custom binary format  
designed to facilitate fast lookups of IP addresses while allowing for great  
flexibility in the type of data associated with an address.  
.  
The MaxMind DB format is an open format. The spec is available at  
https://maxmind.github.io/MaxMind-DB/. This spec is licensed under the Creative  
Commons Attribution-ShareAlike 3.0 Unported License.  

#### 3.40.2. Depended Packages
libc6  

#### 3.40.3. Configuration Files
(None)

#### 3.40.4. Executable Files
(None)

<br>

### 3.41 libncurses6 Package
#### 3.41.1. Official Package Description
shared libraries for terminal handling  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains the shared libraries necessary to run programs  
compiled with ncurses.  

#### 3.41.2. Depended Packages
libc6  
libtinfo6  

#### 3.41.3. Configuration Files
(None)

#### 3.41.4. Executable Files
(None)

<br>

### 3.42 libnetfilter-conntrack3 Package
#### 3.42.1. Official Package Description
Netfilter netlink-conntrack library  
libnetfilter_conntrack is a userspace library providing a programming  
interface (API) to the in-kernel connection tracking state table.  

#### 3.42.2. Depended Packages
libc6  
libmnl0  
libnfnetlink0  

#### 3.42.3. Configuration Files
(None)

#### 3.42.4. Executable Files
(None)

<br>

### 3.43 libnfnetlink0 Package
#### 3.43.1. Official Package Description
Netfilter netlink library  
libnfnetlink is the low-level library for netfilter related  
kernel/userspace communication. It provides a generic messaging  
infrastructure for in-kernel netfilter subsystems (such as  
nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) and their  
respective users and/or management tools in userspace.  

#### 3.43.2. Depended Packages
libc6  

#### 3.43.3. Configuration Files
(None)

#### 3.43.4. Executable Files
(None)

<br>

### 3.44 libnftables1 Package
#### 3.44.1. Official Package Description
Netfilter nftables high level userspace API library  
This library provides high level semantics to interact with the nftables  
framework by Netfilter project.  
.  
nftables replaces the old popular iptables, ip6tables, arptables and ebtables.  
.  
Netfilter software and nftables in particular are used in applications such  
as Internet connection sharing, firewalls, IP accounting, transparent  
proxying, advanced routing and traffic control.  
.  
A Linux kernel >= 3.13 is required. However, >= 4.14 is recommended.  
.  
This package contains the libnftables library.  

#### 3.44.2. Depended Packages
libc6  
libgmp10  
libjansson4  
libmnl0  
libnftnl11  
libxtables12  

#### 3.44.3. Configuration Files
(None)

#### 3.44.4. Executable Files
(None)

<br>

### 3.45 libnftnl11 Package
#### 3.45.1. Official Package Description
Netfilter nftables userspace API library  
libnftnl is the low-level library for Netfilter 4th generation  
framework nftables.  
.  
Is the user-space library for low-level interaction with  
nftables Netlink's API over libmnl.  

#### 3.45.2. Depended Packages
libc6  
libmnl0  

#### 3.45.3. Configuration Files
(None)

#### 3.45.4. Executable Files
(None)

<br>

### 3.46 libnghttp2-14 Package
#### 3.46.1. Official Package Description
library implementing HTTP/2 protocol (shared library)  
This is an implementation of the Hypertext Transfer Protocol version  
2 in C. The framing layer of HTTP/2 is implemented as a reusable C  
library.  
.  
This package installs a shared library.  

#### 3.46.2. Depended Packages
libc6  

#### 3.46.3. Configuration Files
(None)

#### 3.46.4. Executable Files
(None)

<br>

### 3.47 libnss-systemd Package
#### 3.47.1. Official Package Description
nss module providing dynamic user and group name resolution  
nss-systemd is a plug-in module for the GNU Name Service Switch (NSS)  
functionality of the GNU C Library (glibc), providing UNIX user and group name  
resolution for dynamic users and groups allocated through the DynamicUser=  
option in systemd unit files. See systemd.exec(5) for details on this  
option.  
.  
Installing this package automatically adds the module to /etc/nsswitch.conf.  

#### 3.47.2. Depended Packages
libc6  
libcap2  
systemd  

#### 3.47.3. Configuration Files
(None)

#### 3.47.4. Executable Files
(None)

<br>

### 3.48 libntfs-3g89t64 Package
#### 3.48.1. Official Package Description
read/write NTFS driver for FUSE (runtime library)  
NTFS-3G uses FUSE (Filesystem in Userspace) to provide support for the NTFS  
filesystem used by Microsoft Windows.  
.  
This package contains the actual library.  

#### 3.48.2. Depended Packages
libc6  

#### 3.48.3. Configuration Files
(None)

#### 3.48.4. Executable Files
(None)

<br>

### 3.49 libnuma1 Package
#### 3.49.1. Official Package Description
Libraries for controlling NUMA policy  
Library to control specific NUMA (Non-Uniform Memory Architecture)  
scheduling or memory placement policies.  

#### 3.49.2. Depended Packages
libc6  

#### 3.49.3. Configuration Files
(None)

#### 3.49.4. Executable Files
(None)

<br>

### 3.50 libpam-systemd Package
#### 3.50.1. Official Package Description
system and service manager - PAM module  
This package contains the PAM module which registers user sessions in  
the systemd control group hierarchy for logind.  
.  
If in doubt, do install this package.  
.  
Packages that depend on logind functionality need to depend on libpam-systemd.  

#### 3.50.2. Depended Packages
default-dbus-system-bus  
libc6  
libcap2  
libpam-runtime  
libpam0g  
systemd  
systemd-sysv  

#### 3.50.3. Configuration Files
(None)

#### 3.50.4. Executable Files
(None)

<br>

### 3.51 libparted2t64 Package
#### 3.51.1. Official Package Description
disk partition manipulator - shared library  
GNU Parted is a program that allows you to create, destroy, resize,  
move, and copy disk partitions. This is useful for creating space  
for new operating systems, reorganizing disk usage, and copying data  
to new hard disks.  
.  
This package contains the shared library.  

#### 3.51.2. Depended Packages
dmidecode  
libblkid1  
libc6  
libdevmapper1.02.1  
libuuid1  

#### 3.51.3. Configuration Files
(None)

#### 3.51.4. Executable Files
(None)

<br>

### 3.52 libpci3 Package
#### 3.52.1. Official Package Description
PCI utilities (shared library)  
This package contains the libpci shared library files.  
.  
The libpci library provides portable access to configuration  
registers of devices connected to the PCI bus.  

#### 3.52.2. Depended Packages
libc6  
libudev1  
pci.ids  
zlib1g  

#### 3.52.3. Configuration Files
(None)

#### 3.52.4. Executable Files
(None)

<br>

### 3.53 libpipeline1 Package
#### 3.53.1. Official Package Description
Unix process pipeline manipulation library  
This is a C library for setting up and running pipelines of processes,  
without needing to involve shell command-line parsing which is often  
error-prone and insecure.  

#### 3.53.2. Depended Packages
libc6  

#### 3.53.3. Configuration Files
(None)

#### 3.53.4. Executable Files
(None)

<br>

### 3.54 libplymouth5 Package
#### 3.54.1. Official Package Description
graphical boot animation and logger - shared libraries  
Plymouth is an application that runs very early in the boot process  
(even before the root filesystem is mounted!) that provides a graphical  
boot animation while the boot process happens in the background.  
.  
This package contains the shared libraries.  

#### 3.54.2. Depended Packages
libc6  
libevdev2  
libpng16-16t64  
libudev1  
libxkbcommon0  

#### 3.54.3. Configuration Files
(None)

#### 3.54.4. Executable Files
(None)

<br>

### 3.55 libpng16-16t64 Package
#### 3.55.1. Official Package Description
PNG library - runtime (version 1.6)  
libpng is a library implementing an interface for reading and writing  
PNG (Portable Network Graphics) format files.  
.  
This package contains the runtime library files needed to run software  
using libpng.  

#### 3.55.2. Depended Packages
libc6  
zlib1g  

#### 3.55.3. Configuration Files
(None)

#### 3.55.4. Executable Files
(None)

<br>

### 3.56 libpsl5t64 Package
#### 3.56.1. Official Package Description
Library for Public Suffix List (shared libraries)  
Libpsl allows checking domains against the Public Suffix List.  
It can be used to avoid privacy-leaking 'super-cookies',  
'super domain' certificates, for domain highlighting purposes  
sorting domain lists by site and more.  
.  
Please see https://publicsuffix.org for more detailed information.  
.  
This package contains runtime libraries.  

#### 3.56.2. Depended Packages
libc6  
libidn2-0  
libunistring5  

#### 3.56.3. Configuration Files
(None)

#### 3.56.4. Executable Files
(None)

<br>

### 3.57 libuchardet0 Package
#### 3.57.1. Official Package Description
universal charset detection library - shared library  
uchardet is a C language binding of the original C++ implementation  
of the universal charset detection library by Mozilla.  
.  
uchardet is a encoding detector library, which takes a sequence of  
bytes in an unknown character encoding without any additional  
information, and attempts to determine the encoding of the text.  
.  
This package contains the shared library.  

#### 3.57.2. Depended Packages
libc6  
libgcc-s1  
libstdc++6  

#### 3.57.3. Configuration Files
(None)

#### 3.57.4. Executable Files
(None)

<br>

### 3.58 libusb-1.0-0 Package
#### 3.58.1. Official Package Description
userspace USB programming library  
Library for programming USB applications without the knowledge  
of Linux kernel internals.  
.  
This package contains what you need to run programs that use this  
library.  

#### 3.58.2. Depended Packages
libc6  
libudev1  

#### 3.58.3. Configuration Files
(None)

#### 3.58.4. Executable Files
(None)

<br>

### 3.59 libuv1t64 Package
#### 3.59.1. Official Package Description
asynchronous event notification library - runtime library  
Libuv is the asynchronous library behind Node.js. Very similar to libevent or  
libev, it provides the main elements for event driven systems: watching and  
waiting for availability in a set of sockets, and some other events like timers  
or asynchronous messages. However, libuv also comes with some other extras  
like:  
files watchers and asynchronous operations  
a portable TCP and UDP API, as well as asynchronous DNS resolution  
processes and threads management, and a portable inter-process  
communications mechanism, with pipes and work queues  
a plugins mechanism for loading libraries dynamically  
interface with external libraries that also need to access the I/O.  
.  
This package includes the dynamic library against which you can link  
your program.  

#### 3.59.2. Depended Packages
libc6  

#### 3.59.3. Configuration Files
(None)

#### 3.59.4. Executable Files
(None)

<br>

### 3.60 libx11-6 Package
#### 3.60.1. Official Package Description
X11 client-side library  
This package provides a client interface to the X Window System, otherwise  
known as 'Xlib'.  It provides a complete API for the basic functions of the  
window system.  
.  
More information about X.Org can be found at:  
<URL:https://www.X.org>  
.  
This module can be found at  
https://gitlab.freedesktop.org/xorg/lib/libX11  

#### 3.60.2. Depended Packages
libc6  
libx11-data  
libxcb1  

#### 3.60.3. Configuration Files
(None)

#### 3.60.4. Executable Files
(None)

<br>

### 3.61 libx11-data Package
#### 3.61.1. Official Package Description
X11 client-side library  
This package provides the locale data files for libx11.  
.  
More information about X.Org can be found at:  
<URL:https://www.X.org>  
.  
This module can be found at  
https://gitlab.freedesktop.org/xorg/lib/libX11  

#### 3.61.2. Depended Packages
(None)

#### 3.61.3. Configuration Files
(None)

#### 3.61.4. Executable Files
(None)

<br>

### 3.62 libxau6 Package
#### 3.62.1. Official Package Description
X11 authorisation library  
This package provides the main interface to the X11 authorisation handling,  
which controls authorisation for X connections, both client-side and  
server-side.  
.  
More information about X.Org can be found at:  
<URL:https://www.X.org>  
.  
This module can be found at  
https://gitlab.freedesktop.org/xorg/lib/libxau  

#### 3.62.2. Depended Packages
libc6  

#### 3.62.3. Configuration Files
(None)

#### 3.62.4. Executable Files
(None)

<br>

### 3.63 libxcb1 Package
#### 3.63.1. Official Package Description
X C Binding  
This package contains the library files needed to run software using libxcb,  
the X C Binding.  
.  
The XCB library provides an interface to the X Window System protocol,  
designed to replace the Xlib interface.  XCB provides several advantages over  
Xlib:  
.  
Size: small library and lower memory footprint  
Latency hiding: batch several requests and wait for the replies later  
Direct protocol access: one-to-one mapping between interface and protocol  
Thread support: access XCB from multiple threads, with no explicit locking  
Easy creation of new extensions: automatically generates interface from  
machine-parsable protocol descriptions  

#### 3.63.2. Depended Packages
libc6  
libxau6  
libxdmcp6  

#### 3.63.3. Configuration Files
(None)

#### 3.63.4. Executable Files
(None)

<br>

### 3.64 libxdmcp6 Package
#### 3.64.1. Official Package Description
X11 Display Manager Control Protocol library  
This package provides the main interface to the X11 display manager control  
protocol library, which allows for remote logins to display managers.  
.  
More information about X.Org can be found at:  
<URL:http://www.X.org>  
.  
This module can be found at  
git://anongit.freedesktop.org/git/xorg/lib/libXdmcp  

#### 3.64.2. Depended Packages
libbsd0  
libc6  

#### 3.64.3. Configuration Files
(None)

#### 3.64.4. Executable Files
(None)

<br>

### 3.65 libxext6 Package
#### 3.65.1. Official Package Description
X11 miscellaneous extension library  
libXext provides an X Window System client interface to several extensions to  
the X protocol.  
.  
The supported protocol extensions are:  
DOUBLE-BUFFER (DBE), the Double Buffer extension;  
DPMS, the VESA Display Power Management System extension;  
Extended-Visual-Information (EVI), an extension for gathering extra  
information about the X server's visuals;  
LBX, the Low Bandwidth X extension;  
MIT-SHM, the MIT X client/server shared memory extension;  
MIT-SUNDRY-NONSTANDARD, a miscellaneous extension by MIT;  
Multi-Buffering, the multi-buffering and stereo display extension;  
SECURITY, the X security extension;  
SHAPE, the non-rectangular shaped window extension;  
SYNC, the X synchronization extension;  
TOG-CUP, the Open Group's Colormap Utilization extension;  
XC-APPGROUP, the X Consortium's Application Group extension;  
XC-MISC, the X Consortium's resource ID querying extension;  
XTEST, the X test extension (this is one of two client-side  
implementations; the other is in the libXtst library, provided by the  
libxtst6 package);  
.  
libXext also provides a small set of utility functions to aid authors of  
client APIs for X protocol extensions.  
.  
More information about X.Org can be found at:  
<URL:http://www.X.org>  
.  
This module can be found at  
git://anongit.freedesktop.org/git/xorg/lib/libXext  

#### 3.65.2. Depended Packages
libc6  
libx11-6  

#### 3.65.3. Configuration Files
(None)

#### 3.65.4. Executable Files
(None)

<br>

### 3.66 libxmuu1 Package
#### 3.66.1. Official Package Description
X11 miscellaneous micro-utility library  
libXmuu provides a set of miscellaneous utility convenience functions for X  
libraries to use.  It is a lighter version of libXmu that does not depend  
on libXt or libXext; for more information on libXmu, see libxmu6.  
.  
More information about X.Org can be found at:  
<URL:http://www.X.org>  
.  
This module can be found at  
git://anongit.freedesktop.org/git/xorg/lib/libXmu  

#### 3.66.2. Depended Packages
libc6  
libx11-6  

#### 3.66.3. Configuration Files
(None)

#### 3.66.4. Executable Files
(None)

<br>

### 3.67 lshw Package
#### 3.67.1. Official Package Description
information about hardware configuration  
A small tool to provide detailed information on the hardware  
configuration of the machine. It can report exact memory  
configuration, firmware version, mainboard configuration, CPU version  
and speed, cache configuration, bus speed, etc. on DMI-capable x86  
systems, on some PowerPC machines (PowerMac G4 is known to work) and AMD64.  
.  
Information can be output in plain text, HTML or XML.  

#### 3.67.2. Depended Packages
libc6  
libgcc-s1  
libstdc++6  

#### 3.67.3. Configuration Files
(None)

#### 3.67.4. Executable Files
/usr/bin/lshw  

<br>

### 3.68 lsof Package
#### 3.68.1. Official Package Description
utility to list open files  
Lsof is a Unix-specific diagnostic tool.  Its name stands  
for LiSt Open Files, and it does just that.  It lists  
information about any files that are open, by processes  
currently running on the system.  

#### 3.68.2. Depended Packages
libc6  
libselinux1  
libtirpc3t64  

#### 3.68.3. Configuration Files
(None)

#### 3.68.4. Executable Files
/usr/bin/lsof  

<br>

### 3.69 man-db Package
#### 3.69.1. Official Package Description
tools for reading manual pages  
This package provides the man command, the primary way of examining the  
system help files (manual pages). Other utilities provided include the  
whatis and apropos commands for searching the manual page database, the  
manpath utility for determining the manual page search path, and the  
maintenance utilities mandb, catman and zsoelim. man-db uses the groff  
suite of programs to format and display the manual pages.  

#### 3.69.2. Depended Packages
bsdextrautils  
debconf  
groff-base  
libc6  
libgdbm6  
libpipeline1  
libseccomp2  
zlib1g  

#### 3.69.3. Configuration Files
/etc/apparmor.d/usr.bin.man  
/etc/cron.daily/man-db  
/etc/cron.weekly/man-db  
/etc/manpath.config  

#### 3.69.4. Executable Files
/usr/bin/apropos  
/usr/bin/catman  
/usr/bin/lexgrog  
/usr/bin/man  
/usr/bin/man-recode  
/usr/bin/mandb  
/usr/bin/manpath  
/usr/bin/whatis  
/usr/sbin/accessdb  

<br>

### 3.70 manpages Package
#### 3.70.1. Official Package Description
Manual pages about using a GNU/Linux system  
This package contains GNU/Linux manual pages for these sections:  
4 = Devices (e.g. hd, sd).  
5 = File formats and protocols, syntaxes of several system  
files (e.g. wtmp, /etc/passwd, nfs).  
7 = Conventions and standards, macro packages, etc.  
(e.g. nroff, ascii).  
.  
Beside the intro man page describing the section, a few manual  
pages from sections 1,6 and 8 are also provided.  
.  
The man pages describe syntaxes of several system files.  

#### 3.70.2. Depended Packages
(None)

#### 3.70.3. Configuration Files
(None)

#### 3.70.4. Executable Files
(None)

<br>

### 3.71 mtr-tiny Package
#### 3.71.1. Official Package Description
Full screen ncurses traceroute tool  
mtr combines the functionality of the 'traceroute' and 'ping' programs  
in a single network diagnostic tool.  
.  
As mtr starts, it investigates the network connection between the host  
mtr runs on and a user-specified destination host.  After it  
determines the address of each network hop between the machines,  
it sends a sequence of ICMP ECHO requests to each one to determine the  
quality of the link to each machine.  As it does this, it prints  
running statistics about each machine.  
.  
mtr-tiny is compiled without support for X and conserves disk space.  

#### 3.71.2. Depended Packages
libc6  
libjansson4  
libncurses6  
libtinfo6  

#### 3.71.3. Configuration Files
(None)

#### 3.71.4. Executable Files
/usr/bin/mtr  
/usr/bin/mtr-packet  

<br>

### 3.72 nano Package
#### 3.72.1. Official Package Description
small, friendly text editor inspired by Pico  
GNU nano is an easy-to-use text editor originally designed as a replacement  
for Pico, the ncurses-based editor from the non-free mailer package Pine  
(itself now available under the Apache License as Alpine).  
.  
However, GNU nano also implements many features missing in Pico, including:  
undo/redo  
line numbering  
syntax coloring  
soft-wrapping of overlong lines  
selecting text by holding Shift  
interactive search and replace (with regular expression support)  
a go-to line (and column) command  
support for multiple file buffers  
auto-indentation  
tab completion of filenames and search terms  
toggling features while running  
and full internationalization support  

#### 3.72.2. Depended Packages
libc6  
libncursesw6  
libtinfo6  

#### 3.72.3. Configuration Files
/etc/nanorc  

#### 3.72.4. Executable Files
/usr/bin/nano  
/usr/bin/rnano  

<br>

### 3.73 nftables Package
#### 3.73.1. Official Package Description
Program to control packet filtering rules by Netfilter project  
This software provides an in-kernel packet classification framework that is  
based on a network-specific Virtual Machine (VM) and the nft userspace  
command line tool. The nftables framework reuses the existing Netfilter  
subsystems such as the existing hook infrastructure, the connection tracking  
system, NAT, userspace queueing and logging subsystem.  
.  
nftables replaces the old popular iptables, ip6tables, arptables and ebtables.  
.  
Netfilter software and nftables in particular are used in applications such  
as Internet connection sharing, firewalls, IP accounting, transparent  
proxying, advanced routing and traffic control.  
.  
A Linux kernel >= 3.13 is required. However, >= 4.14 is recommended.  

#### 3.73.2. Depended Packages
libc6  
libedit2  
libnftables1  

#### 3.73.3. Configuration Files
/etc/nftables.conf  

#### 3.73.4. Executable Files
/usr/sbin/nft  

<br>

### 3.74 ntfs-3g Package
#### 3.74.1. Official Package Description
read/write NTFS driver for FUSE  
NTFS-3G uses FUSE (Filesystem in Userspace) to provide support for the NTFS  
filesystem used by Microsoft Windows.  

#### 3.74.2. Depended Packages
fuse3  
libc6  
libgcrypt20  
libgnutls30t64  
libntfs-3g89t64  

#### 3.74.3. Configuration Files
(None)

#### 3.74.4. Executable Files
/bin/lowntfs-3g  
/bin/ntfs-3g  
/bin/ntfs-3g.probe  
/bin/ntfscat  
/bin/ntfscluster  
/bin/ntfscmp  
/bin/ntfsfallocate  
/bin/ntfsfix  
/bin/ntfsinfo  
/bin/ntfsls  
/bin/ntfsmove  
/bin/ntfsrecover  
/bin/ntfssecaudit  
/bin/ntfstruncate  
/bin/ntfsusermap  
/bin/ntfswipe  
/sbin/mkfs.ntfs  
/sbin/mkntfs  
/sbin/mount.lowntfs-3g  
/sbin/mount.ntfs  
/sbin/mount.ntfs-3g  
/sbin/ntfsclone  
/sbin/ntfscp  
/sbin/ntfslabel  
/sbin/ntfsresize  
/sbin/ntfsundelete  
/usr/bin/ntfsdecrypt  

<br>

### 3.75 openssh-client Package
#### 3.75.1. Official Package Description
secure shell (SSH) client, for secure access to remote machines  
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
This package provides the ssh, scp and sftp clients, the ssh-agent  
and ssh-add programs to make public key authentication more convenient,  
and the ssh-keygen, ssh-keyscan, ssh-copy-id and ssh-argv0 utilities.  
.  
In some countries it may be illegal to use any encryption at all  
without a special permit.  
.  
ssh replaces the insecure rsh, rcp and rlogin programs, which are  
obsolete for most purposes.  

#### 3.75.2. Depended Packages
adduser  
libc6  
libedit2  
libfido2-1  
libgssapi-krb5-2  
libselinux1  
libssl3  
passwd  
zlib1g  

#### 3.75.3. Configuration Files
/etc/ssh/ssh_config  

#### 3.75.4. Executable Files
/usr/bin/scp  
/usr/bin/sftp  
/usr/bin/slogin  
/usr/bin/ssh  
/usr/bin/ssh-add  
/usr/bin/ssh-agent  
/usr/bin/ssh-argv0  
/usr/bin/ssh-copy-id  
/usr/bin/ssh-keygen  
/usr/bin/ssh-keyscan  

<br>

### 3.76 parted Package
#### 3.76.1. Official Package Description
disk partition manipulator  
GNU Parted is a program that allows you to create, destroy, resize,  
move, and copy disk partitions. This is useful for creating space  
for new operating systems, reorganizing disk usage, and copying data  
to new hard disks.  
.  
This package contains the binary and manual page. Further  
documentation is available in parted-doc.  
.  
Parted currently supports DOS, Mac, Sun, BSD, GPT, MIPS, and PC98  
partitioning formats, as well as a "loop" (raw disk) type which  
allows use on RAID/LVM. It can detect and remove ASFS/AFFS/APFS,  
Btrfs, ext2/3/4, FAT16/32, HFS, JFS, linux-swap, UFS, XFS, and ZFS  
file systems. Parted also has the ability to create and modify file  
systems of some of these types, but using it to perform file system  
operations is now deprecated.  
.  
The nature of this software means that any bugs could cause massive  
data loss. While there are no such bugs known at the moment, they  
could exist, so please back up all important files before running  
it, and do so at your own risk.  

#### 3.76.2. Depended Packages
libc6  
libparted2t64  
libreadline8t64  
libtinfo6  
libuuid1  

#### 3.76.3. Configuration Files
(None)

#### 3.76.4. Executable Files
/usr/sbin/parted  
/usr/sbin/partprobe  

<br>

### 3.77 pci.ids Package
#### 3.77.1. Official Package Description
PCI ID Repository  
This package contains the pci.ids file, a public repository of all known  
ID's used in PCI devices: ID's of vendors, devices, subsystems and device  
classes. It is used in various programs to display full human-readable  
names instead of cryptic numeric codes.  

#### 3.77.2. Depended Packages
(None)

#### 3.77.3. Configuration Files
(None)

#### 3.77.4. Executable Files
(None)

<br>

### 3.78 pciutils Package
#### 3.78.1. Official Package Description
PCI utilities  
This package contains various utilities for inspecting and setting of  
devices connected to the PCI bus.  

#### 3.78.2. Depended Packages
libc6  
libkmod2  
libpci3  

#### 3.78.3. Configuration Files
(None)

#### 3.78.4. Executable Files
/usr/bin/lspci  
/usr/bin/setpci  
/usr/sbin/update-pciids  

<br>

### 3.79 perl Package
#### 3.79.1. Official Package Description
Larry Wall's Practical Extraction and Report Language  
Perl is a highly capable, feature-rich programming language with over  
20 years of development. Perl 5 runs on over 100 platforms from  
portables to mainframes. Perl is suitable for both rapid prototyping  
and large scale development projects.  
.  
Perl 5 supports many programming styles, including procedural,  
functional, and object-oriented. In addition to this, it is supported  
by an ever-growing collection of reusable modules which accelerate  
development. Some of these modules include Web frameworks, database  
integration, networking protocols, and encryption. Perl provides  
interfaces to C and C++ for custom extension development.  

#### 3.79.2. Depended Packages
dpkg  
libperl5.38t64  
perl-base  
perl-modules-5.38  

#### 3.79.3. Configuration Files
/etc/perl/Net/libnet.cfg  

#### 3.79.4. Executable Files
/usr/bin/corelist  
/usr/bin/corelist  
/usr/bin/cpan  
/usr/bin/enc2xs  
/usr/bin/encguess  
/usr/bin/h2ph  
/usr/bin/h2xs  
/usr/bin/instmodsh  
/usr/bin/json_pp  
/usr/bin/json_pp  
/usr/bin/libnetcfg  
/usr/bin/perlbug  
/usr/bin/perldoc  
/usr/bin/perldoc  
/usr/bin/perlivp  
/usr/bin/perlthanks  
/usr/bin/piconv  
/usr/bin/pl2pm  
/usr/bin/pod2html  
/usr/bin/pod2man  
/usr/bin/pod2text  
/usr/bin/pod2usage  
/usr/bin/podchecker  
/usr/bin/prove  
/usr/bin/prove  
/usr/bin/ptar  
/usr/bin/ptardiff  
/usr/bin/ptargrep  
/usr/bin/shasum  
/usr/bin/shasum  
/usr/bin/splain  
/usr/bin/streamzip  
/usr/bin/streamzip  
/usr/bin/xsubpp  
/usr/bin/zipdetails  
/usr/bin/zipdetails  

<br>

### 3.80 plymouth Package
#### 3.80.1. Official Package Description
boot animation, logger and I/O multiplexer  
Plymouth provides a boot-time I/O multiplexing framework - the most obvious  
use for which is to provide an attractive graphical animation in place of  
the text messages that normally get shown during boot. (The messages are  
instead redirected to a logfile for later viewing.) However, in event-driven  
boot systems Plymouth can also usefully handle user interaction such as  
password prompts for encrypted file systems.  
.  
This package provides the basic framework, enabling a text-mode animation.  

#### 3.80.2. Depended Packages
init-system-helpers  
libc6  
libdrm2  
libplymouth5  
systemd  
sysvinit-utils  
udev  

#### 3.80.3. Configuration Files
/etc/init.d/plymouth  
/etc/init.d/plymouth-log  
/etc/logrotate.d/bootlog  

#### 3.80.4. Executable Files
/usr/bin/plymouth  
/usr/sbin/plymouthd  

<br>

### 3.81 plymouth-theme-ubuntu-text Package
#### 3.81.1. Official Package Description
boot animation, logger and I/O multiplexer - ubuntu text theme  
Plymouth provides a boot-time I/O multiplexing framework - the most obvious  
use for which is to provide an attractive graphical animation in place of  
the text messages that normally get shown during boot. (The messages are  
instead redirected to a logfile for later viewing.) However, in event-driven  
boot systems Plymouth can also usefully handle user interaction such as  
password prompts for encrypted file systems.  
.  
This package contains the default ubuntu-text text theme used when no  
support for a graphical theme is found on your system.  

#### 3.81.2. Depended Packages
libc6  
libplymouth5  
lsb-release  
plymouth  

#### 3.81.3. Configuration Files
(None)

#### 3.81.4. Executable Files
(None)

<br>

### 3.82 powermgmt-base Package
#### 3.82.1. Official Package Description
common utils for power management  
This package ships the following scripts:  
on_ac_power: determine whether the system is powered from battery or  
an abundant supply  
lspower: list power sources the system knows about, and their status  

#### 3.82.2. Depended Packages
(None)

#### 3.82.3. Configuration Files
(None)

#### 3.82.4. Executable Files
/sbin/on_ac_power  
/usr/bin/lspower  
/usr/bin/on_ac_power  

<br>

### 3.83 psmisc Package
#### 3.83.1. Official Package Description
utilities that use the proc file system  
This package contains miscellaneous utilities that use the proc FS:  
.  
fuser: identifies processes that are using files or sockets.  
killall: kills processes by name (e.g. "killall -HUP named").  
peekfd: shows the data traveling over a file descriptor.  
pstree: shows currently running processes as a tree.  
prtstat: print the contents of /proc/<pid>/stat  

#### 3.83.2. Depended Packages
libc6  
libtinfo6  

#### 3.83.3. Configuration Files
(None)

#### 3.83.4. Executable Files
/usr/bin/fuser  
/usr/bin/killall  
/usr/bin/peekfd  
/usr/bin/prtstat  
/usr/bin/pslog  
/usr/bin/pstree  
/usr/bin/pstree.x11  

<br>

### 3.84 publicsuffix Package
#### 3.84.1. Official Package Description
accurate, machine-readable list of domain name suffixes  
A machine-readable list of domain name suffixes that accept public  
registration.  Each suffix represents the part of a domain name which  
is not under the control of the individual registrant, which makes  
the list useful for grouping cookies, deciding same-origin policies,  
collating spam, and other activities.  

#### 3.84.2. Depended Packages
(None)

#### 3.84.3. Configuration Files
(None)

#### 3.84.4. Executable Files
(None)

<br>

### 3.85 python3-commandnotfound Package
#### 3.85.1. Official Package Description
Python 3 bindings for command-not-found.  
This package will install the Python 3 library for command_not_found tool.  

#### 3.85.2. Depended Packages
lsb-release  
python3-apt  
python3-gdbm  
python3:any  

#### 3.85.3. Configuration Files
(None)

#### 3.85.4. Executable Files
(None)

<br>

### 3.86 python3-distro-info Package
#### 3.86.1. Official Package Description
information about distributions' releases (Python 3 module)  
Information about all releases of Debian and Ubuntu.  
.  
This package contains a Python 3 module for parsing the data in  
distro-info-data. There is also a command line interface in the distro-info  
package.  

#### 3.86.2. Depended Packages
distro-info-data  
python3:any  

#### 3.86.3. Configuration Files
(None)

#### 3.86.4. Executable Files
(None)

<br>

### 3.87 python3-distupgrade Package
#### 3.87.1. Official Package Description
manage release upgrades  
This is the DistUpgrade Python 3 module  

#### 3.87.2. Depended Packages
gpgv  
lsb-release  
procps  
python3-apt  
python3-dbus  
python3-distro-info  
python3-update-manager  
python3:any  
sensible-utils  

#### 3.87.3. Configuration Files
(None)

#### 3.87.4. Executable Files
(None)

<br>

### 3.88 python3-gdbm Package
#### 3.88.1. Official Package Description
GNU dbm database support for Python 3.x  
GNU dbm database module for Python 3.x. Install this if you want to  
create or read GNU dbm database files with Python.  

#### 3.88.2. Depended Packages
libc6  
libgdbm6t64  
python3  

#### 3.88.3. Configuration Files
(None)

#### 3.88.4. Executable Files
(None)

<br>

### 3.89 python3-update-manager Package
#### 3.89.1. Official Package Description
Python 3.x module for update-manager  
Python module for update-manager (UpdateManager).  
.  
This package contains the Python 3.x version of this module.  

#### 3.89.2. Depended Packages
python3-apt  
python3-distro-info  
python3-distupgrade  
python3:any  

#### 3.89.3. Configuration Files
(None)

#### 3.89.4. Executable Files
(None)

<br>

### 3.90 rsync Package
#### 3.90.1. Official Package Description
fast, versatile, remote (and local) file-copying tool  
rsync is a fast and versatile file-copying tool which can copy locally  
and to/from a remote host. It offers many options to control its behavior,  
and its remote-update protocol can minimize network traffic to make  
transferring updates between machines fast and efficient.  
.  
It is widely used for backups and mirroring and as an improved copy  
command for everyday use.  
.  
This package provides both the rsync command line tool and optional  
daemon functionality.  

#### 3.90.2. Depended Packages
init-system-helpers  
libacl1  
libc6  
liblz4-1  
libpopt0  
libssl3  
libxxhash0  
libzstd1  
lsb-base  
zlib1g  

#### 3.90.3. Configuration Files
/etc/default/rsync  
/etc/init.d/rsync  

#### 3.90.4. Executable Files
/usr/bin/rrsync  
/usr/bin/rsync  
/usr/bin/rsync-ssl  

<br>

### 3.91 strace Package
#### 3.91.1. Official Package Description
System call tracer  
strace is a system call tracer: i.e. a debugging tool which prints out  
a trace of all the system calls made by another process/program.  
The program to be traced need not be recompiled for this, so you can  
use it on binaries for which you don't have source.  
.  
System calls and signals are events that happen at the user/kernel  
interface. A close examination of this boundary is very useful for bug  
isolation, sanity checking and attempting to capture race conditions.  

#### 3.91.2. Depended Packages
libc6  
libunwind8  

#### 3.91.3. Configuration Files
(None)

#### 3.91.4. Executable Files
/usr/bin/strace  
/usr/bin/strace-log-merge  

<br>

### 3.92 systemd-timesyncd Package
#### 3.92.1. Official Package Description
minimalistic service to synchronize local time with NTP servers  
The package contains the systemd-timesyncd system service that may be used to  
synchronize the local system clock with a remote Network Time Protocol server.  

#### 3.92.2. Depended Packages
libc6  
libsystemd-shared  
systemd  

#### 3.92.3. Configuration Files
/etc/dhcp/dhclient-exit-hooks.d/timesyncd  
/etc/systemd/timesyncd.conf  

#### 3.92.4. Executable Files
(None)

<br>

### 3.93 tcpdump Package
#### 3.93.1. Official Package Description
command-line network traffic analyzer  
This program allows you to dump the traffic on a network. tcpdump  
is able to examine IPv4, ICMPv4, IPv6, ICMPv6, UDP, TCP, SNMP, AFS  
BGP, RIP, PIM, DVMRP, IGMP, SMB, OSPF, NFS and many other packet  
types.  
.  
It can be used to print out the headers of packets on a network  
interface, filter packets that match a certain expression. You can  
use this tool to track down network problems, to detect attacks  
or to monitor network activities.  

#### 3.93.2. Depended Packages
adduser  
libc6  
libpcap0.8t64  
libssl3  

#### 3.93.3. Configuration Files
/etc/apparmor.d/usr.bin.tcpdump  

#### 3.93.4. Executable Files
/usr/bin/tcpdump  

<br>

### 3.94 telnet Package
#### 3.94.1. Official Package Description
transitional dummy package for inetutils-telnet default switch  
This package will force a switch from the old netkit telnet implementation  
to the inetutils-telnet one, which is an upstream maintained project.  
.  
This package can be safely removed once it has been upgraded, as  
inetutils-telnet provides a matching virtual package. It will stop being  
provided after Debian bookworm's release.  
.  
If you want to keep using the netkit implementation, then install  
telnet-ssl instead.  

#### 3.94.2. Depended Packages
inetutils-telnet  

#### 3.94.3. Configuration Files
(None)

#### 3.94.4. Executable Files
(None)

<br>

### 3.95 time Package
#### 3.95.1. Official Package Description
GNU time program for measuring CPU resource usage  
The 'time' command runs another program, then displays information  
about the resources used by that program, collected by the system while  
the program was running.  You can select which information is reported  
and the format in which it is shown, or have 'time' save the information  
in a file instead of display it on the screen.  
.  
The resources that 'time' can report on fall into the general  
categories of time, memory, I/O, and IPC calls.  
.  
The GNU version can format the output in arbitrary ways by using a  
printf-style format string to include various resource measurements.  

#### 3.95.2. Depended Packages
libc6  

#### 3.95.3. Configuration Files
(None)

#### 3.95.4. Executable Files
/usr/bin/time  

<br>

### 3.96 tnftp Package
#### 3.96.1. Official Package Description
enhanced ftp client  
tnftp is what many users affectionately call the enhanced ftp  
client in NetBSD (http://www.netbsd.org).  
.  
This package is a port' of the NetBSD ftp client to other systems.  
.  
The enhancements over the standard ftp client in 4.4BSD include:  
command-line editing within ftp  
command-line fetching of URLS, including support for:  
http proxies (c.f: $http_proxy, $ftp_proxy)  
authentication  
context sensitive command and filename completion  
dynamic progress bar  
IPv6 support (from the WIDE project)  
modification time preservation  
paging of local and remote files, and of directory listings  
(c.f: lpage', page', pdir')  
passive mode support, with fallback to active mode  
set option' override of ftp environment variables  
TIS Firewall Toolkit gate ftp proxy support (c.f: gate')  
transfer-rate throttling (c.f: -T', rate')  

#### 3.96.2. Depended Packages
libc6  
libedit2  
libssl3  

#### 3.96.3. Configuration Files
(None)

#### 3.96.4. Executable Files
/usr/bin/tnftp  

<br>

### 3.97 ubuntu-advantage-tools Package
#### 3.97.1. Official Package Description
transitional dummy package for ubuntu-pro-client  
This is a transitional dummy package for ubuntu-pro-client. It can safely be  
removed.  

#### 3.97.2. Depended Packages
debconf  
ubuntu-pro-client  

#### 3.97.3. Configuration Files
(None)

#### 3.97.4. Executable Files
(None)

<br>

### 3.98 ubuntu-release-upgrader-core Package
#### 3.98.1. Official Package Description
manage release upgrades  
This is the core of the Ubuntu Release Upgrader  

#### 3.98.2. Depended Packages
ca-certificates  
python3-distupgrade  
python3:any  

#### 3.98.3. Configuration Files
/etc/update-manager/meta-release  
/etc/update-manager/release-upgrades  
/etc/update-motd.d/91-release-upgrade  

#### 3.98.4. Executable Files
/usr/bin/do-release-upgrade  

<br>

### 3.99 ubuntu-standard Package
#### 3.99.1. Official Package Description
Ubuntu standard system  
This package depends on all of the packages in the Ubuntu standard system.  
This set of packages provides a comfortable command-line Unix-like  
environment.  
.  
It is also used to help ensure proper upgrades, so it is recommended that  
it not be removed.  

#### 3.99.2. Depended Packages
bind9-dnsutils  
busybox-static  
cpio  
cron  
dmidecode  
dosfstools  
ed  
file  
ftp  
hdparm  
info  
libpam-systemd  
logrotate  
lshw  
lsof  
man-db  
media-types  
nftables  
parted  
pciutils  
psmisc  
rsync  
strace  
time  
usbutils  
wget  
xz-utils  

#### 3.99.3. Configuration Files
(None)

#### 3.99.4. Executable Files
(None)

<br>

### 3.100 ufw Package
#### 3.100.1. Official Package Description
program for managing a Netfilter firewall  
The Uncomplicated FireWall is a front-end for iptables, to make managing a  
Netfilter firewall easier. It provides a command line interface with syntax  
similar to OpenBSD's Packet Filter. It is particularly well-suited as a  
host-based firewall.  

#### 3.100.2. Depended Packages
debconf  
iptables  
python3:any  
ucf  

#### 3.100.3. Configuration Files
/etc/default/ufw  
/etc/init.d/ufw  
/etc/logrotate.d/ufw  
/etc/rsyslog.d/20-ufw.conf  
/etc/ufw/sysctl.conf  

#### 3.100.4. Executable Files
/usr/sbin/ufw  

<br>

### 3.101 update-manager-core Package
#### 3.101.1. Official Package Description
manage release upgrades  
This is the core of update-manager and the release upgrader  

#### 3.101.2. Depended Packages
distro-info-data  
python3-distro-info  
python3-update-manager  
python3:any  
ubuntu-advantage-tools  
ubuntu-release-upgrader-core  

#### 3.101.3. Configuration Files
(None)

#### 3.101.4. Executable Files
/usr/bin/hwe-support-status  
/usr/bin/ubuntu-security-status  

<br>

### 3.102 usb.ids Package
#### 3.102.1. Official Package Description
USB ID Repository  
This package contains the usb.ids file, a public repository of all known  
ID's used in USB devices: ID's of vendors, devices, subsystems and device  
classes. It is used in various programs to display full human-readable  
names instead of cryptic numeric codes.  

#### 3.102.2. Depended Packages
(None)

#### 3.102.3. Configuration Files
(None)

#### 3.102.4. Executable Files
(None)

<br>

### 3.103 usbutils Package
#### 3.103.1. Official Package Description
Linux USB utilities  
This package contains the lsusb utility for inspecting the devices  
connected to the USB bus. It shows a graphical representation of the  
devices that are currently plugged in, showing the topology of the  
USB bus. It also displays information on each individual device on  
the bus.  
.  
lsusb, usb-devices, usbhid-dump, usbreset  

#### 3.103.2. Depended Packages
libc6  
libudev1  
libusb-1.0-0  

#### 3.103.3. Configuration Files
(None)

#### 3.103.4. Executable Files
/usr/bin/lsusb  
/usr/bin/usb-devices  
/usr/bin/usbhid-dump  
/usr/bin/usbreset  

<br>

### 3.104 uuid-runtime Package
#### 3.104.1. Official Package Description
runtime components for the Universally Unique ID library  
The libuuid library generates and parses 128-bit Universally Unique  
IDs (UUIDs). A UUID is an identifier that is unique within the space  
of all such identifiers across both space and time. It can be used for  
multiple purposes, from tagging objects with an extremely short lifetime  
to reliably identifying very persistent objects across a network.  
.  
See RFC 4122 for more information.  
.  
This package contains the uuidgen program and the uuidd daemon.  
.  
The uuidd daemon is used to generate UUIDs, especially time-based  
UUIDs, in a secure and guaranteed-unique fashion, even in the face of  
large numbers of threads trying to grab UUIDs running on different CPUs.  
It is used by libuuid as well as the uuidgen program.  

#### 3.104.2. Depended Packages
adduser  
init-system-helpers  
libc6  
libsmartcols1  
libsystemd0  
libuuid1  

#### 3.104.3. Configuration Files
/etc/init.d/uuidd  

#### 3.104.4. Executable Files
/usr/bin/uuidgen  
/usr/bin/uuidparse  
/usr/sbin/uuidd  

<br>

### 3.105 wget Package
#### 3.105.1. Official Package Description
retrieves files from the web  
Wget is a network utility to retrieve files from the web  
using HTTP(S) and FTP, the two most widely used internet  
protocols. It works non-interactively, so it will work in  
the background, after having logged off. The program supports  
recursive retrieval of web-authoring pages as well as FTP  
sites -- you can use Wget to make mirrors of archives and  
home pages or to travel the web like a WWW robot.  
.  
Wget works particularly well with slow or unstable connections  
by continuing to retrieve a document until the document is fully  
downloaded. Re-getting files from where it left off works on  
servers (both HTTP and FTP) that support it. Both HTTP and FTP  
retrievals can be time stamped, so Wget can see if the remote  
file has changed since the last retrieval and automatically  
retrieve the new version if it has.  
.  
Wget supports proxy servers; this can lighten the network load,  
speed up retrieval, and provide access behind firewalls.  

#### 3.105.2. Depended Packages
libc6  
libidn2-0  
libpcre2-8-0  
libpsl5t64  
libssl3  
libuuid1  
zlib1g  

#### 3.105.3. Configuration Files
/etc/wgetrc  

#### 3.105.4. Executable Files
/usr/bin/wget  

<br>

### 3.106 xauth Package
#### 3.106.1. Official Package Description
X authentication utility  
xauth is a small utility to read and manipulate Xauthority files, which  
are used by servers and clients alike to control authentication and access  
to X sessions.  

#### 3.106.2. Depended Packages
libc6  
libx11-6  
libxau6  
libxext6  
libxmuu1  

#### 3.106.3. Configuration Files
(None)

#### 3.106.4. Executable Files
/usr/bin/xauth  

<br>

### 3.107 xz-utils Package
#### 3.107.1. Official Package Description
XZ-format compression utilities  
XZ is the successor to the Lempel-Ziv/Markov-chain Algorithm  
compression format, which provides memory-hungry but powerful  
compression (often better than bzip2) and fast, easy decompression.  
.  
This package provides the command line tools for working with XZ  
compression, including xz, unxz, xzcat, xzgrep, and so on. They can  
also handle the older LZMA format, and if invoked via appropriate  
symlinks will emulate the behavior of the commands in the lzma  
package.  
.  
The XZ format is similar to the older LZMA format but includes some  
improvements for general use:  
.  
'file' magic for detecting XZ files;  
crc64 data integrity check;  
limited random-access reading support;  
improved support for multithreading (not used in xz-utils);  
support for flushing the encoder.  

#### 3.107.2. Depended Packages
libc6  
liblzma5  

#### 3.107.3. Configuration Files
(None)

#### 3.107.4. Executable Files
/usr/bin/lzmainfo  
/usr/bin/unxz  
/usr/bin/xz  
/usr/bin/xzcat  
/usr/bin/xzcmp  
/usr/bin/xzdiff  
/usr/bin/xzegrep  
/usr/bin/xzfgrep  
/usr/bin/xzgrep  
/usr/bin/xzless  
/usr/bin/xzmore  

<br>

## 4. Necessary Packages
---
**awk:** Virtual package provided by gawk, mawk, or original-awk  
**default-dbus-system-bus:** Virtual package provided by dbus package  
**gir1.2-girepository-2.0:** Introspection data for GIRepository library  
**libassuan0:** IPC library for the GnuPG components  
**libevdev2:** wrapper library for evdev devices  
**libgdbm6:** GNU dbm database routines (runtime version)  
**libgirepository-1.0-1-with-libffi8:**   
**libmagic1t64:** Recognize the type of data in a file using "magic" numbers - library  
**libnpth0t64:** replacement for GNU Pth using system threads  
**libpcap0.8t64:** system interface for user-level packet capture  
**libperl5.38t64:** shared Perl library  
**libunwind8:** library to determine the call-chain of a program - runtime  
**libuv1:** asynchronous event notification library - runtime library  
**libxkbcommon0:** library interface to the XKB compiler - shared library  
**lsb-base:** transitional package for Linux Standard Base init script functionality  
**perl-modules-5.38:** Core Perl modules  
**perlapi-5.38.2:** Virtual package provided by perl-base  
**python3-typing-extensions:** Backported and Experimental Type Hints for Python  

<br>

### 4.1 awk Package
awk is a virtual package provided by gawk, mawk, or original-awk. If we  install one of them, awk will be seen as installed too. 

As mawk being a required package and was documented at 1.65. we may consider  this package as documented too.

<br>

### 4.2 default-dbus-system-bus Package
default-dbus-system-bus is a virtual package provided by dbus package. If  we install dbus, default-dbus-system-bus will be seen as installed too. 

As dbus being an important package and was documented at 2.7. we may consider  this package as documented too.

<br>

### 4.3 gir1.2-girepository-2.0 Package
#### 4.3.1. Official Package Description
Introspection data for GIRepository library  
GObject Introspection is a project for providing machine readable  
introspection data of the API of C libraries. This introspection  
data can be used in several different use cases, for example  
automatic code generation for bindings, API verification and documentation  
generation.  
.  
This package contains the introspection data for the GIRepository library,  
which can be used to manipulate the search path used by language bindings  
and load introspection data.  

#### 4.3.2. Depended Packages
gir1.2-gobject-2.0  
libgirepository-1.0-1  

#### 4.3.3. Configuration Files
(None)

#### 4.3.4. Executable Files
(None)

<br>

### 4.4 libassuan0 Package
#### 4.4.1. Official Package Description
IPC library for the GnuPG components  
Libassuan is a small library implementing the so-called "Assuan  
protocol". This protocol is used for IPC between most newer GnuPG  
components. Both server and client side functions are provided.  

#### 4.4.2. Depended Packages
libc6  
libgpg-error0  

#### 4.4.3. Configuration Files
(None)

#### 4.4.4. Executable Files
(None)

<br>

### 4.5 libevdev2 Package
#### 4.5.1. Official Package Description
wrapper library for evdev devices  
libevdev is a wrapper library for evdev devices. It provides  
functions covering the common tasks when dealing with evdev devices,  
thus avoiding erroneous ioctls and other errors.  
.  
This package contains the files required to run software using  
libevdev.  

#### 4.5.2. Depended Packages
libc6  

#### 4.5.3. Configuration Files
(None)

#### 4.5.4. Executable Files
(None)

<br>

### 4.6 libgdbm6 Package
#### 4.6.1. Official Package Description
GNU dbm database routines (runtime version)  
GNU dbm ('gdbm') is a library of database functions that use extendible  
hashing and works similarly to the standard UNIX 'dbm' functions.  
.  
The basic use of 'gdbm' is to store key/data pairs in a data file, thus  
providing a persistent version of the 'dictionary' Abstract Data Type  
('hash' to perl programmers).  
#### 4.6.2. Depended Packages
libc6  

#### 4.6.3. Configuration Files
(None)

#### 4.6.4. Executable Files
(None)

<br>

### 4.7 libmagic1t64 Package
#### 4.7.1. Official Package Description
Recognize the type of data in a file using "magic" numbers - library  
This library can be used to classify files according to magic number  
tests. It implements the core functionality of the file command.  

#### 4.7.2. Depended Packages
libbz2-1.0  
libc6  
liblzma5  
libmagic-mgc  
zlib1g  

#### 4.7.3. Configuration Files
/etc/magic  
/etc/magic.mime  

#### 4.7.4. Executable Files
(None)

<br>

### 4.8 libnpth0t64 Package
#### 4.8.1. Official Package Description
replacement for GNU Pth using system threads  
nPth is a non-preemptive threads implementation using an API very  
similar to the one known from GNU Pth. It has been designed as a  
replacement of GNU Pth for non-ancient operating systems. In  
contrast to GNU Pth it is based on the system's standard threads  
implementation. Thus nPth allows the use of libraries which are not  
compatible to GNU Pth.  

#### 4.8.2. Depended Packages
libc6  

#### 4.8.3. Configuration Files
(None)

#### 4.8.4. Executable Files
(None)

<br>

### 4.9 libpcap0.8t64 Package
#### 4.9.1. Official Package Description
system interface for user-level packet capture  
libpcap (Packet CAPture) provides a portable framework for low-level  
network monitoring.  Applications include network statistics collection,  
security monitoring, network debugging, etc.  
.  
Since almost every system vendor provides a different interface for  
packet capture, and since there are several tools that require this  
functionality, the libpcap authors created this system-independent API  
to ease in porting and to alleviate the need for several  
system-dependent packet capture modules in each application.  

#### 4.9.2. Depended Packages
libc6  
libdbus-1-3  
libibverbs1  

#### 4.9.3. Configuration Files
(None)

#### 4.9.4. Executable Files
(None)

<br>

### 4.10 libperl5.38t64 Package
#### 4.10.1. Official Package Description
shared Perl library  
This package contains the shared Perl library, used by applications  
which embed a Perl interpreter.  
.  
It also contains the architecture-dependent parts of the standard  
library (and depends on perl-modules-5.38 which contains the  
architecture-independent parts).  

#### 4.10.2. Depended Packages
libbz2-1.0  
libc6  
libcrypt1  
libdb5.3t64  
libgdbm-compat4t64  
libgdbm6t64  
perl-modules-5.38  
zlib1g  

#### 4.10.3. Configuration Files
(None)

#### 4.10.4. Executable Files
/usr/bin/cpan5.38-x86_64-linux-gnu  
/usr/bin/perl5.38-x86_64-linux-gnu  

<br>

### 4.11 libunwind8 Package
#### 4.11.1. Official Package Description
library to determine the call-chain of a program - runtime  
The primary goal of this project is to define a portable and efficient C  
programming interface (API) to determine the call-chain of a program.  
The API additionally provides the means to manipulate the preserved  
(callee-saved) state of each call-frame and to resume execution at any  
point in the call-chain (non-local goto). The API supports both local  
(same-process) and remote (across-process) operation. As such, the API  
is useful in a number of applications.  
.  
This package includes the shared libraries  

#### 4.11.2. Depended Packages
libc6  
liblzma5  

#### 4.11.3. Configuration Files
(None)

#### 4.11.4. Executable Files
(None)

<br>

### 4.12 libuv1 Package
#### 4.12.1. Official Package Description
asynchronous event notification library - runtime library  
Libuv is the asynchronous library behind Node.js. Very similar to libevent or  
libev, it provides the main elements for event driven systems: watching and  
waiting for availability in a set of sockets, and some other events like timers  
or asynchronous messages. However, libuv also comes with some other extras  
like:  
files watchers and asynchronous operations  
a portable TCP and UDP API, as well as asynchronous DNS resolution  
processes and threads management, and a portable inter-process  
communications mechanism, with pipes and work queues  
a plugins mechanism for loading libraries dynamically  
interface with external libraries that also need to access the I/O.  
.  
This package includes the dynamic library against which you can link  
your program.  

#### 4.12.2. Depended Packages
libc6  

#### 4.12.3. Configuration Files
(None)

#### 4.12.4. Executable Files
(None)

<br>

### 4.13 libxkbcommon0 Package
#### 4.13.1. Official Package Description
library interface to the XKB compiler - shared library  
This package provides a library to handle keyboard descriptions, including  
loading them from disk, parsing them and handling their state. It's mainly  
meant for client toolkits, window systems, and other system applications;  
currently that includes Wayland, kmscon, GTK+, Clutter, and more.  
.  
More information about X.Org can be found at:  
<URL:http://www.X.org>  
.  
This module can be found at  
https://github.com/xkbcommon/libxkbcommon.git  

#### 4.13.2. Depended Packages
libc6  
xkb-data  

#### 4.13.3. Configuration Files
(None)

#### 4.13.4. Executable Files
(None)

<br>

### 4.14 lsb-base Package
#### 4.14.1. Official Package Description
transitional package for Linux Standard Base init script functionality  
This is an empty package; it's needed only because of Provides: not being  
supported in debootstrap.  It can be safely removed.  

#### 4.14.2. Depended Packages
sysvinit-utils  

#### 4.14.3. Configuration Files
(None)

#### 4.14.4. Executable Files
(None)

<br>

### 4.15 perl-modules-5.38 Package
#### 4.15.1. Official Package Description
Core Perl modules  
Architecture independent Perl modules.  These modules are part of Perl and  
required if the perl' package is installed.  
.  
Note that this package only exists to save archive space and should be  
considered an internal implementation detail of the perl' package.  
Other packages should not depend on perl-modules-5.38' directly, they  
should use perl' (which depends on perl-modules-5.38') instead.  

#### 4.15.2. Depended Packages
dpkg  
perl-base  

#### 4.15.3. Configuration Files
(None)

#### 4.15.4. Executable Files
(None)

<br>

### 4.16 perlapi-5.38.2 Package
perlapi-5.38.2 is a virtual package provided by perl-base. If we install perl-base, this package will be seen as installed too. 

As perl-base being a required package and was documented at 1.70. we may consider this package as documented too.

<br>

### 4.17 python3-typing-extensions Package
#### 4.17.1. Official Package Description
Backported and Experimental Type Hints for Python  
The "typing_extensions" module serves two related purposes:  
.  
1- Enable use of new type system features on older Python versions.  
2- Enable experimentation with new type system PEPs before they are accepted  
and added to the "typing" module.  
.  
"typing_extensions" is treated specially by static type checkers such as mypy  
and pyright. Objects defined in "typing_extensions" are treated the same  
way as equivalent forms in "typing".  

#### 4.17.2. Depended Packages
python3:any  

#### 4.17.3. Configuration Files
(None)

#### 4.17.4. Executable Files
(None)

<br>


