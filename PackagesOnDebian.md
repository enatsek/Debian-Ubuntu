##### PackagesOnDebian
# Debian Software Packages

## 0. Specs
---
### 0.0. Info
We will explore the softare packages normally present in Debian server  editions (namely Debian 12). 

Debian and Ubuntu has some differences in classifications, so there are 2 separate tutorials for them.

### 0.1. Debian Packages
Debian has around 60.000 software packages (a huge number). 

These packages can be classified in a lot of ways. But for this tutorial we are going to use the priority values for the classification.

The priority values range from "required" to "extra", and they are defined as follows:

**required:** Essential packages that are necessary for the proper functioning of the system, such as the kernel, basic system utilities, and essential libraries.

**important:** Important packages that are not strictly necessary for basic system operation but are still considered essential for most users. These  may include important system administration tools or libraries.

**standard:** Packages that provide a reasonably small but not essential subset of the Debian system. These packages are typically included in most  installations.

**optional:** Additional packages that are not necessary for the basic system  operation but provide additional functionality or applications that many users may find useful.

**extra:** Packages that are not officially part of the Debian distribution but  are available in the Debian repositories. These packages may include  experimental or third-party software. 

I have added 2 more categories; necessary and extra-necessary.
 
**necessary:** These packages are depended by required, important, and standard  packages, but don't exist in one of those groups.

**extra-necessary:** These packages are depended by necessary packages, but don't # exist in one of other 4 groups. Ubuntu does not have any extra-necessary packages.

We are going to explore required, important, standard, necessary and extra-necessary software packages.

### 0.2. Package Documentation Template
I prefer using the following template for my documentation
 
#### 0.2.1. Official Package Description
Debian's description of the package as in the package file.

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
These are the (very) essential packages. You may expect them in every Debian installation.

At my last check, the following packages are marked as required:

**apt:** commandline package manager  
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
**grep:** GNU grep, egrep and fgrep  
**gzip:** GNU compression utilities  
**hostname:** utility to set/show the host name or domain name  
**init-system-helpers:** helper tools for all init systems  
**libc-bin:** GNU C Library: Binaries  
**libpam-modules:** Pluggable Authentication Modules for PAM  
**libpam-modules-bin:** Pluggable Authentication Modules for PAM - helper binaries  
**libpam-runtime:** Runtime support for the PAM library  
**login:** system login tools  
**mawk:** Pattern scanning and text processing language  
**mount:** tools for mounting and manipulating filesystems  
**ncurses-base:** basic terminal type definitions  
**ncurses-bin:** terminal-related programs and man pages  
**passwd:** change and administer password and group data  
**perl-base:** minimal Perl system  
**sed:** GNU stream editor for filtering/transforming text  
**sysvinit-utils:** System-V-like utilities  
**tar:** GNU version of the tar archiving utility  
**tzdata:** time zone and daylight-saving time data  
**util-linux:** miscellaneous system utilities  

<br>

### 1.1 apt Package
#### 1.1.1. Official Package Description
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

#### 1.1.2. Depended Packages
adduser  
debian-archive-keyring  
gpgv  
libapt-pkg6.0  
libc6  
libgcc-s1  
libgnutls30  
libseccomp2  
libstdc++6  
libsystemd0  

#### 1.1.3. Configuration Files
/etc/apt/apt.conf.d/01autoremove  
/etc/cron.daily/apt-compat  
/etc/logrotate.d/apt  

#### 1.1.4. Executable Files
/usr/bin/apt  
/usr/bin/apt-cache  
/usr/bin/apt-cdrom  
/usr/bin/apt-config  
/usr/bin/apt-get  
/usr/bin/apt-key  
/usr/bin/apt-mark  

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

#### 1.2.3. Configuration Files
/etc/debian_version  
/etc/dpkg/origins/debian  
/etc/host.conf  
/etc/issue  
/etc/issue.net  
/etc/os-release  
/etc/update-motd.d/10-uname  

#### 1.2.4. Executable Files
(None)

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
/bin/bash  
/bin/rbash  
/usr/bin/bashbug  
/usr/bin/clear_console  

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

#### 1.6.3. Configuration Files
(None)

#### 1.6.4. Executable Files
/bin/cat  
/bin/chgrp  
/bin/chmod  
/bin/chown  
/bin/cp  
/bin/date  
/bin/dd  
/bin/df  
/bin/dir  
/bin/echo  
/bin/false  
/bin/ln  
/bin/ls  
/bin/mkdir  
/bin/mknod  
/bin/mktemp  
/bin/mv  
/bin/pwd  
/bin/readlink  
/bin/rm  
/bin/rmdir  
/bin/sleep  
/bin/stty  
/bin/sync  
/bin/touch  
/bin/true  
/bin/uname  
/bin/vdir  
/usr/bin/[  
/usr/bin/arch  
/usr/bin/b2sum  
/usr/bin/base32  
/usr/bin/base64  
/usr/bin/basename  
/usr/bin/basenc  
/usr/bin/chcon  
/usr/bin/cksum  
/usr/bin/comm  
/usr/bin/csplit  
/usr/bin/cut  
/usr/bin/dircolors  
/usr/bin/dirname  
/usr/bin/du  
/usr/bin/env  
/usr/bin/expand  
/usr/bin/expr  
/usr/bin/factor  
/usr/bin/fmt  
/usr/bin/fold  
/usr/bin/groups  
/usr/bin/head  
/usr/bin/hostid  
/usr/bin/id  
/usr/bin/install  
/usr/bin/join  
/usr/bin/link  
/usr/bin/logname  
/usr/bin/md5sum  
/usr/bin/md5sum.textutils  
/usr/bin/mkfifo  
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
/usr/bin/realpath  
/usr/bin/runcon  
/usr/bin/seq  
/usr/bin/sha1sum  
/usr/bin/sha224sum  
/usr/bin/sha256sum  
/usr/bin/sha384sum  
/usr/bin/sha512sum  
/usr/bin/shred  
/usr/bin/shuf  
/usr/bin/sort  
/usr/bin/split  
/usr/bin/stat  
/usr/bin/stdbuf  
/usr/bin/sum  
/usr/bin/tac  
/usr/bin/tail  
/usr/bin/tee  
/usr/bin/test  
/usr/bin/timeout  
/usr/bin/tr  
/usr/bin/truncate  
/usr/bin/tsort  
/usr/bin/tty  
/usr/bin/unexpand  
/usr/bin/uniq  
/usr/bin/unlink  
/usr/bin/users  
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
/bin/dash  
/bin/sh  

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
/bin/run-parts  
/bin/tempfile  
/sbin/installkernel  
/usr/bin/ischroot  
/usr/bin/savelog  
/usr/bin/which.debianutils  
/usr/sbin/add-shell  
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
/sbin/start-stop-daemon  
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
/usr/sbin/dpkg-fsys-usrunmess  

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
libext2fs2  
libss2  
libuuid1  
logsave  

#### 1.12.3. Configuration Files
/etc/cron.d/e2scrub_all  
/etc/e2scrub.conf  
/etc/mke2fs.conf  

#### 1.12.4. Executable Files
/sbin/badblocks  
/sbin/debugfs  
/sbin/dumpe2fs  
/sbin/e2fsck  
/sbin/e2image  
/sbin/e2label  
/sbin/e2mmpstatus  
/sbin/e2scrub  
/sbin/e2scrub_all  
/sbin/e2undo  
/sbin/fsck.ext2  
/sbin/fsck.ext3  
/sbin/fsck.ext4  
/sbin/mke2fs  
/sbin/mkfs.ext2  
/sbin/mkfs.ext3  
/sbin/mkfs.ext4  
/sbin/resize2fs  
/sbin/tune2fs  
/usr/bin/chattr  
/usr/bin/lsattr  
/usr/sbin/e2freefrag  
/usr/sbin/e4crypt  
/usr/sbin/e4defrag  
/usr/sbin/filefrag  
/usr/sbin/mklost+found  

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

### 1.14 grep Package
#### 1.14.1. Official Package Description
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

#### 1.14.2. Depended Packages
dpkg  
libc6  
libpcre2-8-0  

#### 1.14.3. Configuration Files
(None)

#### 1.14.4. Executable Files
/bin/egrep  
/bin/fgrep  
/bin/grep  
/usr/bin/rgrep  

<br>

### 1.15 gzip Package
#### 1.15.1. Official Package Description
GNU compression utilities  
This package provides the standard GNU file compression utilities, which  
are also the default compression tools for Debian.  They typically operate  
on files with names ending in '.gz', but can also decompress files ending  
in '.Z' created with 'compress'.  

#### 1.15.2. Depended Packages
dpkg  
libc6  

#### 1.15.3. Configuration Files
(None)

#### 1.15.4. Executable Files
/bin/gunzip  
/bin/gzexe  
/bin/gzip  
/bin/uncompress  
/bin/zcat  
/bin/zcmp  
/bin/zdiff  
/bin/zegrep  
/bin/zfgrep  
/bin/zforce  
/bin/zgrep  
/bin/zless  
/bin/zmore  
/bin/znew  

<br>

### 1.16 hostname Package
#### 1.16.1. Official Package Description
utility to set/show the host name or domain name  
This package provides commands which can be used to display the system's  
DNS name, and to display or set its hostname or NIS domain name.  

#### 1.16.2. Depended Packages
libc6  

#### 1.16.3. Configuration Files
(None)

#### 1.16.4. Executable Files
/bin/dnsdomainname  
/bin/domainname  
/bin/hostname  
/bin/nisdomainname  
/bin/ypdomainname  

<br>

### 1.17 init-system-helpers Package
#### 1.17.1. Official Package Description
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

#### 1.17.2. Depended Packages
usrmerge  

#### 1.17.3. Configuration Files
(None)

#### 1.17.4. Executable Files
/usr/bin/deb-systemd-helper  
/usr/bin/deb-systemd-invoke  
/usr/sbin/invoke-rc.d  
/usr/sbin/service  
/usr/sbin/update-rc.d  

<br>

### 1.18 libc-bin Package
#### 1.18.1. Official Package Description
GNU C Library: Binaries  
This package contains utility programs related to the GNU C Library.  
.  
getconf: query system configuration variables  
getent: get entries from administrative databases  
iconv, iconvconfig: convert between character encodings  
ldd, ldconfig: print/configure shared library dependencies  
locale, localedef: show/generate locale definitions  
tzselect, zdump, zic: select/dump/compile time zones  

#### 1.18.2. Depended Packages
libc6  

#### 1.18.3. Configuration Files
/etc/bindresvport.blacklist  
/etc/default/nss  
/etc/gai.conf  
/etc/ld.so.conf  
/etc/ld.so.conf.d/libc.conf  

#### 1.18.4. Executable Files
/sbin/ldconfig  
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
/usr/sbin/zic  

<br>

### 1.19 libpam-modules Package
#### 1.19.1. Official Package Description
Pluggable Authentication Modules for PAM  
This package completes the set of modules for PAM. It includes the  
pam_unix.so module as well as some specialty modules.  

#### 1.19.2. Depended Packages
debconf  
libaudit1  
libc6  
libcrypt1  
libdb5.3  
libpam-modules-bin  
libpam0g  
libselinux1  

#### 1.19.3. Configuration Files
/etc/security/access.conf  
/etc/security/faillock.conf  
/etc/security/group.conf  
/etc/security/limits.conf  
/etc/security/namespace.conf  
/etc/security/namespace.init  
/etc/security/pam_env.conf  
/etc/security/sepermit.conf  
/etc/security/time.conf  

#### 1.19.4. Executable Files
(None)

<br>

### 1.20 libpam-modules-bin Package
#### 1.20.1. Official Package Description
Pluggable Authentication Modules for PAM - helper binaries  
This package contains helper binaries used by the standard set of PAM  
modules in the libpam-modules package.  

#### 1.20.2. Depended Packages
libaudit1  
libc6  
libcrypt1  
libpam0g  
libselinux1  

#### 1.20.3. Configuration Files
(None)

#### 1.20.4. Executable Files
/sbin/mkhomedir_helper  
/sbin/pam_namespace_helper  
/sbin/pwhistory_helper  
/sbin/unix_chkpwd  
/sbin/unix_update  
/usr/sbin/faillock  
/usr/sbin/pam_timestamp_check  

<br>

### 1.21 libpam-runtime Package
#### 1.21.1. Official Package Description
Runtime support for the PAM library  
Contains configuration files and  directories required for  
authentication  to work on Debian systems.  This package is required  
on almost all installations.  

#### 1.21.2. Depended Packages
debconf  
libpam-modules  

#### 1.21.3. Configuration Files
/etc/pam.conf  
/etc/pam.d/other  

#### 1.21.4. Executable Files
/usr/sbin/pam-auth-update  
/usr/sbin/pam_getenv  

<br>

### 1.22 login Package
#### 1.22.1. Official Package Description
system login tools  
This package provides some required infrastructure for logins and for  
changing effective user or group IDs, including:  
login, the program that invokes a user shell on a virtual terminal;  
nologin, a dummy shell for disabled user accounts;  

#### 1.22.2. Depended Packages
libaudit1  
libc6  
libcrypt1  
libpam-modules  
libpam-runtime  
libpam0g  

#### 1.22.3. Configuration Files
/etc/login.defs  
/etc/pam.d/login  

#### 1.22.4. Executable Files
/bin/login  
/usr/bin/faillog  
/usr/bin/lastlog  
/usr/bin/newgrp  
/usr/bin/sg  
/usr/sbin/nologin  

<br>

### 1.23 mawk Package
#### 1.23.1. Official Package Description
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

#### 1.23.2. Depended Packages
libc6  

#### 1.23.3. Configuration Files
(None)

#### 1.23.4. Executable Files
/usr/bin/mawk  

<br>

### 1.24 mount Package
#### 1.24.1. Official Package Description
tools for mounting and manipulating filesystems  
This package provides the mount(8), umount(8), swapon(8),  
swapoff(8), and losetup(8) commands.  

#### 1.24.2. Depended Packages
libblkid1  
libc6  
libmount1  
libselinux1  
libsmartcols1  

#### 1.24.3. Configuration Files
(None)

#### 1.24.4. Executable Files
/bin/mount  
/bin/umount  
/sbin/losetup  
/sbin/swapoff  
/sbin/swapon  

<br>

### 1.25 ncurses-base Package
#### 1.25.1. Official Package Description
basic terminal type definitions  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains terminfo data files to support the most common types of  
terminal, including ansi, dumb, linux, rxvt, screen, sun, vt100, vt102, vt220,  
vt52, and xterm.  

#### 1.25.2. Depended Packages
(None)

#### 1.25.3. Configuration Files
/etc/terminfo/README  

#### 1.25.4. Executable Files
(None)

<br>

### 1.26 ncurses-bin Package
#### 1.26.1. Official Package Description
terminal-related programs and man pages  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains the programs used for manipulating the terminfo  
database and individual terminfo entries, as well as some programs for  
resetting terminals and such.  

#### 1.26.2. Depended Packages
libc6  
libtinfo6  

#### 1.26.3. Configuration Files
(None)

#### 1.26.4. Executable Files
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

### 1.27 passwd Package
#### 1.27.1. Official Package Description
change and administer password and group data  
This package includes passwd, chsh, chfn, and many other programs to  
maintain password and group data.  
.  
Shadow passwords are supported.  See /usr/share/doc/passwd/README.Debian  

#### 1.27.2. Depended Packages
libaudit1  
libc6  
libcrypt1  
libpam-modules  
libpam0g  
libselinux1  
libsemanage2  

#### 1.27.3. Configuration Files
/etc/default/useradd  
/etc/pam.d/chfn  
/etc/pam.d/chpasswd  
/etc/pam.d/chsh  
/etc/pam.d/newusers  
/etc/pam.d/passwd  

#### 1.27.4. Executable Files
/sbin/shadowconfig  
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
/usr/sbin/useradd  
/usr/sbin/userdel  
/usr/sbin/usermod  
/usr/sbin/vigr  
/usr/sbin/vipw  

<br>

### 1.28 perl-base Package
#### 1.28.1. Official Package Description
minimal Perl system  
Perl is a scripting language used in many system scripts and utilities.  
.  
This package provides a Perl interpreter and the small subset of the  
standard run-time library required to perform basic tasks. For a full  
Perl installation, install "perl" (and its dependencies, "perl-modules-5.36"  
and "perl-doc").  

#### 1.28.2. Depended Packages
dpkg  
libc6  
libcrypt1  

#### 1.28.3. Configuration Files
(None)

#### 1.28.4. Executable Files
/usr/bin/perl  
/usr/bin/perl5.36.0  

<br>

### 1.29 sed Package
#### 1.29.1. Official Package Description
GNU stream editor for filtering/transforming text  
sed reads the specified files or the standard input if no  
files are specified, makes editing changes according to a  
list of commands, and writes the results to the standard  
output.  

#### 1.29.2. Depended Packages
libacl1  
libc6  
libselinux1  

#### 1.29.3. Configuration Files
(None)

#### 1.29.4. Executable Files
/bin/sed  

<br>

### 1.30 sysvinit-utils Package
#### 1.30.1. Official Package Description
System-V-like utilities  
This package contains the important System-V-like utilities.  
.  
Specifically, this package includes:  
init-d-script, fstab-decode, killall5, pidof  
.  
It also contains the library scripts sourced by init-d-script and other  
initscripts that were formally in lsb-base.  

#### 1.30.2. Depended Packages
libc6  

#### 1.30.3. Configuration Files
(None)

#### 1.30.4. Executable Files
/bin/pidof  
/sbin/fstab-decode  
/sbin/killall5  

<br>

### 1.31 tar Package
#### 1.31.1. Official Package Description
GNU version of the tar archiving utility  
Tar is a program for packaging a set of files as a single archive in tar  
format.  The function it performs is conceptually similar to cpio, and to  
things like PKZIP in the DOS world.  It is heavily used by the Debian package  
management system, and is useful for performing system backups and exchanging  
sets of files with others.  

#### 1.31.2. Depended Packages
libacl1  
libc6  
libselinux1  

#### 1.31.3. Configuration Files
/etc/rmt  

#### 1.31.4. Executable Files
/bin/tar  
/usr/sbin/rmt-tar  
/usr/sbin/tarcat  

<br>

### 1.32 tzdata Package
#### 1.32.1. Official Package Description
time zone and daylight-saving time data  
This package contains data required for the implementation of  
standard local time for many representative locations around the  
globe. It is updated periodically to reflect changes made by  
political bodies to time zone boundaries, UTC offsets, and  
daylight-saving rules.  

#### 1.32.2. Depended Packages
debconf  

#### 1.32.3. Configuration Files
(None)

#### 1.32.4. Executable Files
(None)

<br>

### 1.33 util-linux Package
#### 1.33.1. Official Package Description
miscellaneous system utilities  
This package contains a number of important utilities, most of which  
are oriented towards maintenance of your system. Some of the more  
important utilities included in this package allow you to view kernel  
messages, create new filesystems, view block device information,  
interface with real time clock, etc.  

#### 1.33.2. Depended Packages
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
util-linux-extra  
zlib1g  

#### 1.33.3. Configuration Files
/etc/pam.d/runuser  
/etc/pam.d/runuser-l  
/etc/pam.d/su  
/etc/pam.d/su-l  

#### 1.33.4. Executable Files
/bin/dmesg  
/bin/findmnt  
/bin/lsblk  
/bin/more  
/bin/mountpoint  
/bin/su  
/bin/wdctl  
/sbin/agetty  
/sbin/blkdiscard  
/sbin/blkid  
/sbin/blkzone  
/sbin/blockdev  
/sbin/chcpu  
/sbin/ctrlaltdel  
/sbin/findfs  
/sbin/fsck  
/sbin/fsck.cramfs  
/sbin/fsck.minix  
/sbin/fsfreeze  
/sbin/fstrim  
/sbin/getty  
/sbin/isosize  
/sbin/mkfs  
/sbin/mkfs.bfs  
/sbin/mkfs.cramfs  
/sbin/mkfs.minix  
/sbin/mkswap  
/sbin/pivot_root  
/sbin/runuser  
/sbin/sulogin  
/sbin/swaplabel  
/sbin/switch_root  
/sbin/wipefs  
/sbin/zramctl  
/usr/bin/addpart  
/usr/bin/choom  
/usr/bin/chrt  
/usr/bin/delpart  
/usr/bin/fallocate  
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
/usr/bin/lscpu  
/usr/bin/lsipc  
/usr/bin/lslocks  
/usr/bin/lslogins  
/usr/bin/lsmem  
/usr/bin/lsns  
/usr/bin/mcookie  
/usr/bin/mesg  
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
/usr/bin/taskset  
/usr/bin/uclampset  
/usr/bin/unshare  
/usr/bin/utmpdump  
/usr/bin/whereis  
/usr/bin/x86_64  
/usr/sbin/chmem  
/usr/sbin/ldattach  
/usr/sbin/readprofile  
/usr/sbin/rtcwake  

<br>

## 2. Important Packages
---
These are the important packages. You may expect them in (almost) every Debian installation.

At my last check, the following packages are marked as important:

**adduser:** add and remove users and groups  
**apt-utils:** package management related utility programs  
**cpio:** GNU cpio -- a program to manage archives of files  
**cron:** process scheduling daemon  
**cron-daemon-common:** process scheduling daemon's configuration files  
**debconf-i18n:** full internationalization support for debconf  
**debian-archive-keyring:** GnuPG archive keys of the Debian archive  
**dmidecode:** SMBIOS/DMI table decoder  
**fdisk:** collection of partitioning utilities  
**gpgv:** GNU privacy guard - signature verification tool  
**ifupdown:** high level tools to configure network interfaces  
**init:** metapackage ensuring an init system is installed  
**iproute2:** networking and traffic control tools  
**iputils-ping:** Tools to test the reachability of network hosts  
**isc-dhcp-client:** DHCP client for automatically obtaining an IP address  
**isc-dhcp-common:** common manpages relevant to all of the isc-dhcp packages  
**kmod:** tools for managing Linux kernel modules  
**less:** pager program similar to more  
**logrotate:** Log rotation utility  
**nano:** small, friendly text editor inspired by Pico  
**netbase:** Basic TCP/IP networking system  
**nftables:** Program to control packet filtering rules by Netfilter project  
**procps:** /proc file system utilities  
**readline-common:** GNU readline and history libraries, common files  
**sensible-utils:** Utilities for sensible alternative selection  
**systemd:** system and service manager  
**systemd-sysv:** system and service manager - SysV compatibility symlinks  
**tasksel-data:** official tasks used for installation of Debian systems  
**udev:** /dev/ and hotplug management daemon  
**vim-common:** Vi IMproved - Common files  
**vim-tiny:** Vi IMproved - enhanced vi editor - compact version  
**whiptail:** Displays user-friendly dialog boxes from shell scripts  

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

### 2.2 apt-utils Package
#### 2.2.1. Official Package Description
package management related utility programs  
This package contains some less used commandline utilities related  
to package management with APT.  
.  
apt-extracttemplates is used by debconf to prompt for configuration  
questions before installation.  
apt-ftparchive is used to create Packages and other index files  
needed to publish an archive of Debian packages  
apt-sortpkgs is a Packages/Sources file normalizer.  

#### 2.2.2. Depended Packages
apt  
libapt-pkg6.0  
libc6  
libdb5.3  
libgcc-s1  
libstdc++6  

#### 2.2.3. Configuration Files
(None)

#### 2.2.4. Executable Files
/usr/bin/apt-extracttemplates  
/usr/bin/apt-ftparchive  
/usr/bin/apt-sortpkgs  

<br>

### 2.3 cpio Package
#### 2.3.1. Official Package Description
GNU cpio -- a program to manage archives of files  
GNU cpio is a tool for creating and extracting archives, or copying  
files from one place to another.  It handles a number of cpio formats  
as well as reading and writing tar files.  

#### 2.3.2. Depended Packages
libc6  

#### 2.3.3. Configuration Files
(None)

#### 2.3.4. Executable Files
/bin/cpio  
/bin/mt-gnu  

<br>

### 2.4 cron Package
#### 2.4.1. Official Package Description
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

#### 2.4.2. Depended Packages
cron-daemon-common  
init-system-helpers  
libc6  
libpam-runtime  
libpam0g  
libselinux1  
sensible-utils  

#### 2.4.3. Configuration Files
/etc/default/cron  
/etc/init.d/cron  
/etc/pam.d/cron  

#### 2.4.4. Executable Files
/usr/bin/crontab  
/usr/bin/crontab  
/usr/bin/crontab  
/usr/sbin/cron  

<br>

### 2.5 cron-daemon-common Package
#### 2.5.1. Official Package Description
process scheduling daemon's configuration files  
The cron daemon is a background process that runs particular programs at  
particular times (for example, every minute, day, week, or month), as  
specified in a crontab. By default, users may also create crontabs of  
their own so that processes are run on their behalf.  
.  
This package provides configuration files which must be there to  
define scheduled process sets.  

#### 2.5.2. Depended Packages
adduser  

#### 2.5.3. Configuration Files
/etc/cron.d/.placeholder  
/etc/cron.daily/.placeholder  
/etc/cron.hourly/.placeholder  
/etc/cron.monthly/.placeholder  
/etc/cron.weekly/.placeholder  
/etc/cron.yearly/.placeholder  
/etc/crontab  

#### 2.5.4. Executable Files
(None)

<br>

### 2.6 debconf-i18n Package
#### 2.6.1. Official Package Description
full internationalization support for debconf  
This package provides full internationalization for debconf, including  
translations into all available languages, support for using translated  
debconf templates, and support for proper display of multibyte character  
sets.  

#### 2.6.2. Depended Packages
debconf  
liblocale-gettext-perl  
libtext-charwidth-perl  
libtext-iconv-perl  
libtext-wrapi18n-perl  

#### 2.6.3. Configuration Files
(None)

#### 2.6.4. Executable Files
(None)

<br>

### 2.7 debian-archive-keyring Package
#### 2.7.1. Official Package Description
GnuPG archive keys of the Debian archive  
The Debian project digitally signs its Release files. This package  
contains the archive keys used for that.  

#### 2.7.2. Depended Packages
(None)

#### 2.7.3. Configuration Files
/etc/apt/trusted.gpg.d/debian-archive-bookworm-automatic.asc  
/etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.asc  
/etc/apt/trusted.gpg.d/debian-archive-bookworm-stable.asc  
/etc/apt/trusted.gpg.d/debian-archive-bullseye-automatic.asc  
/etc/apt/trusted.gpg.d/debian-archive-bullseye-security-automatic.asc  
/etc/apt/trusted.gpg.d/debian-archive-bullseye-stable.asc  
/etc/apt/trusted.gpg.d/debian-archive-buster-automatic.asc  
/etc/apt/trusted.gpg.d/debian-archive-buster-security-automatic.asc  
/etc/apt/trusted.gpg.d/debian-archive-buster-stable.asc  

#### 2.7.4. Executable Files
(None)

<br>

### 2.8 dmidecode Package
#### 2.8.1. Official Package Description
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

#### 2.8.2. Depended Packages
libc6  

#### 2.8.3. Configuration Files
(None)

#### 2.8.4. Executable Files
/usr/sbin/biosdecode  
/usr/sbin/dmidecode  
/usr/sbin/ownership  
/usr/sbin/vpddecode  

<br>

### 2.9 fdisk Package
#### 2.9.1. Official Package Description
collection of partitioning utilities  
This package contains the classic fdisk, sfdisk and cfdisk partitioning  
utilities from the util-linux suite.  
.  
The utilities included in this package allow you to partition  
your hard disk. The utilities supports both modern and legacy  
partition tables (eg. GPT, MBR, etc).  
.  
The fdisk utility is the classical text-mode utility.  
The cfdisk utilitity gives a more userfriendly curses based interface.  
The sfdisk utility is mostly for automation and scripting uses.  

#### 2.9.2. Depended Packages
libc6  
libfdisk1  
libmount1  
libncursesw6  
libreadline8  
libsmartcols1  
libtinfo6  

#### 2.9.3. Configuration Files
(None)

#### 2.9.4. Executable Files
/sbin/cfdisk  
/sbin/fdisk  
/sbin/sfdisk  

<br>

### 2.10 gpgv Package
#### 2.10.1. Official Package Description
GNU privacy guard - signature verification tool  
GnuPG is GNU's tool for secure communication and data storage.  
.  
gpgv is actually a stripped-down version of gpg which is only able  
to check signatures. It is somewhat smaller than the fully-blown gpg  
and uses a different (and simpler) way to check that the public keys  
used to make the signature are valid. There are no configuration  
files and only a few options are implemented.  

#### 2.10.2. Depended Packages
libbz2-1.0  
libc6  
libgcrypt20  
libgpg-error0  
zlib1g  

#### 2.10.3. Configuration Files
(None)

#### 2.10.4. Executable Files
/usr/bin/gpgv  

<br>

### 2.11 ifupdown Package
#### 2.11.1. Official Package Description
high level tools to configure network interfaces  
This package provides the tools ifup and ifdown which may be used to  
configure (or, respectively, deconfigure) network interfaces based on  
interface definitions in the file /etc/network/interfaces.  

#### 2.11.2. Depended Packages
adduser  
iproute2  
libc6  

#### 2.11.3. Configuration Files
/etc/default/networking  
/etc/default/networking  
/etc/init.d/networking  
/etc/network/if-down.d/resolved  
/etc/network/if-up.d/resolved  

#### 2.11.4. Executable Files
/sbin/ifdown  
/sbin/ifdown  
/sbin/ifquery  
/sbin/ifquery  
/sbin/ifup  
/sbin/ifup  

<br>

### 2.12 init Package
#### 2.12.1. Official Package Description
metapackage ensuring an init system is installed  
This package is a metapackage which allows you to select from the available  
init systems while ensuring that one of these is available on the system at  
all times.  

#### 2.12.2. Depended Packages
systemd-sysv  

#### 2.12.3. Configuration Files
(None)

#### 2.12.4. Executable Files
(None)

<br>

### 2.13 iproute2 Package
#### 2.13.1. Official Package Description
networking and traffic control tools  
The iproute2 suite is a collection of utilities for networking and  
traffic control.  
.  
These tools communicate with the Linux kernel via the (rt)netlink  
interface, providing advanced features not available through the  
legacy net-tools commands 'ifconfig' and 'route'.  

#### 2.13.2. Depended Packages
debconf  
libbpf1  
libbsd0  
libc6  
libcap2  
libcap2-bin  
libdb5.3  
libelf1  
libmnl0  
libselinux1  
libtirpc3  
libxtables12  

#### 2.13.3. Configuration Files
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

#### 2.13.4. Executable Files
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

### 2.14 iputils-ping Package
#### 2.14.1. Official Package Description
Tools to test the reachability of network hosts  
The ping command sends ICMP ECHO_REQUEST packets to a host in order to  
test if the host is reachable via the network.  
.  
This package includes a ping6 utility which supports IPv6 network  
connections.  

#### 2.14.2. Depended Packages
libc6  
libcap2  
libcap2-bin  
libidn2-0  

#### 2.14.3. Configuration Files
(None)

#### 2.14.4. Executable Files
/bin/ping  
/bin/ping4  
/bin/ping6  

<br>

### 2.15 isc-dhcp-client Package
#### 2.15.1. Official Package Description
DHCP client for automatically obtaining an IP address  
This is the Internet Software Consortiums DHCP client.  
.  
Dynamic Host Configuration Protocol (DHCP) is a protocol like BOOTP  
(actually dhcpd includes much of the functionality of bootpd). It  
gives client machines "leases" for IP addresses and can  
automatically set their network configuration. If your machine  
depends on DHCP (especially likely if its a workstation on a large  
network, or a laptop, or attached to a cable modem), keep this or  
another DHCP client installed.  
.  
Extra documentation can be found in the package isc-dhcp-common.  
.  
ISC has decided to stop maintaining the client and relay parts of isc-dhcp,  
and they will be removed after the 4.4.3 release, keeping only the server  
component. Please, consider using an alternative for isc-dhcp-client  
(dhclient).  
.  
More information can be found in the ISC official announcement:  
https://www.isc.org/blogs/dhcp-client-relay-eom/  

#### 2.15.2. Depended Packages
debianutils  
iproute2  
libc6  

#### 2.15.3. Configuration Files
/etc/apparmor.d/sbin.dhclient  
/etc/dhcp/debug  
/etc/dhcp/dhclient-enter-hooks.d/debug  
/etc/dhcp/dhclient-exit-hooks.d/debug  
/etc/dhcp/dhclient-exit-hooks.d/rfc3442-classless-routes  
/etc/dhcp/dhclient.conf  

#### 2.15.4. Executable Files
/sbin/dhclient  
/sbin/dhclient  
/sbin/dhclient-script  

<br>

### 2.16 isc-dhcp-common Package
#### 2.16.1. Official Package Description
common manpages relevant to all of the isc-dhcp packages  
This package includes manpages that are relevant to the various ISC DHCP  
packages.  
.  
The dhcp-options manpage describes available options for dhcpd and dhclient.  
The dhcp-eval manpage describes evaluation of conditional expressions.  

#### 2.16.2. Depended Packages
debianutils  

#### 2.16.3. Configuration Files
(None)

#### 2.16.4. Executable Files
(None)

<br>

### 2.17 kmod Package
#### 2.17.1. Official Package Description
tools for managing Linux kernel modules  
This package contains a set of programs for loading, inserting, and  
removing kernel modules for Linux.  
It replaces module-init-tools.  

#### 2.17.2. Depended Packages
libc6  
libkmod2  
liblzma5  
libssl3  
libzstd1  

#### 2.17.3. Configuration Files
/etc/init.d/kmod  

#### 2.17.4. Executable Files
/bin/kmod  
/bin/lsmod  
/sbin/depmod  
/sbin/insmod  
/sbin/lsmod  
/sbin/modinfo  
/sbin/modprobe  
/sbin/rmmod  

<br>

### 2.18 less Package
#### 2.18.1. Official Package Description
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

#### 2.18.2. Depended Packages
libc6  
libtinfo6  

#### 2.18.3. Configuration Files
(None)

#### 2.18.4. Executable Files
/usr/bin/less  
/usr/bin/lessecho  
/usr/bin/lessfile  
/usr/bin/lesskey  
/usr/bin/lesspipe  

<br>

### 2.19 logrotate Package
#### 2.19.1. Official Package Description
Log rotation utility  
The logrotate utility is designed to simplify the administration of  
log files on a system which generates a lot of log files.  Logrotate  
allows for the automatic rotation compression, removal and mailing of  
log files.  Logrotate can be set to handle a log file daily, weekly,  
monthly or when the log file gets to a certain size.  Normally, logrotate  
runs as a daily cron job.  

#### 2.19.2. Depended Packages
cron  
libacl1  
libc6  
libpopt0  
libselinux1  

#### 2.19.3. Configuration Files
/etc/cron.daily/logrotate  
/etc/logrotate.conf  
/etc/logrotate.d/btmp  
/etc/logrotate.d/wtmp  

#### 2.19.4. Executable Files
/usr/sbin/logrotate  

<br>

### 2.20 nano Package
#### 2.20.1. Official Package Description
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

#### 2.20.2. Depended Packages
libc6  
libncursesw6  
libtinfo6  

#### 2.20.3. Configuration Files
/etc/nanorc  

#### 2.20.4. Executable Files
/bin/nano  
/bin/rnano  

<br>

### 2.21 netbase Package
#### 2.21.1. Official Package Description
Basic TCP/IP networking system  
This package provides the necessary infrastructure for basic TCP/IP based  
networking.  
.  
In particular, it supplies common name-to-number mappings in /etc/services,  
/etc/rpc, /etc/protocols and /etc/ethertypes.  

#### 2.21.2. Depended Packages
(None)

#### 2.21.3. Configuration Files
/etc/ethertypes  
/etc/protocols  
/etc/rpc  
/etc/services  

#### 2.21.4. Executable Files
(None)

<br>

### 2.22 nftables Package
#### 2.22.1. Official Package Description
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

#### 2.22.2. Depended Packages
libc6  
libedit2  
libnftables1  

#### 2.22.3. Configuration Files
/etc/nftables.conf  

#### 2.22.4. Executable Files
/usr/sbin/nft  

<br>

### 2.23 procps Package
#### 2.23.1. Official Package Description
/proc file system utilities  
This package provides command line and full screen utilities for browsing  
procfs, a "pseudo" file system dynamically generated by the kernel to  
provide information about the status of entries in its process table  
(such as whether the process is running, stopped, or a "zombie").  
.  
It contains free, kill, pkill, pgrep, pmap, ps, pwdx, skill, slabtop,  
snice, sysctl, tload, top, uptime, vmstat, w, and watch.  

#### 2.23.2. Depended Packages
init-system-helpers  
libc6  
libncursesw6  
libproc2-0  
libtinfo6  

#### 2.23.3. Configuration Files
/etc/init.d/procps  
/etc/sysctl.conf  
/etc/sysctl.d/README.sysctl  

#### 2.23.4. Executable Files
/bin/kill  
/bin/ps  
/sbin/sysctl  
/usr/bin/free  
/usr/bin/pgrep  
/usr/bin/pidwait  
/usr/bin/pkill  
/usr/bin/pmap  
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

<br>

### 2.24 readline-common Package
#### 2.24.1. Official Package Description
GNU readline and history libraries, common files  
The GNU readline library aids in the consistency of user interface  
across discrete programs that need to provide a command line  
interface.  
.  
The GNU history library provides a consistent user interface for  
recalling lines of previously typed input.  

#### 2.24.2. Depended Packages
dpkg  

#### 2.24.3. Configuration Files
(None)

#### 2.24.4. Executable Files
(None)

<br>

### 2.25 sensible-utils Package
#### 2.25.1. Official Package Description
Utilities for sensible alternative selection  
This package provides a number of small utilities which are used  
by programs to sensibly select and spawn an appropriate browser,  
editor, or pager.  
.  
The specific utilities included are: sensible-browser sensible-editor  
sensible-pager  

#### 2.25.2. Depended Packages
(None)

#### 2.25.3. Configuration Files
(None)

#### 2.25.4. Executable Files
/usr/bin/select-editor  
/usr/bin/sensible-browser  
/usr/bin/sensible-editor  
/usr/bin/sensible-pager  

<br>

### 2.26 systemd Package
#### 2.26.1. Official Package Description
system and service manager  
systemd is a system and service manager for Linux. It provides aggressive  
parallelization capabilities, uses socket and D-Bus activation for starting  
services, offers on-demand starting of daemons, keeps track of processes using  
Linux control groups, maintains mount and automount points and implements an  
elaborate transactional dependency-based service control logic.  
.  
Installing the systemd package will not switch your init system unless you  
boot with init=/lib/systemd/systemd or install systemd-sysv in addition.  

#### 2.26.2. Depended Packages
libacl1  
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
libp11-kit0  
libseccomp2  
libselinux1  
libssl3  
libsystemd-shared  
libsystemd0  
libzstd1  
mount  

#### 2.26.3. Configuration Files
/etc/modules-load.d/modules.conf  
/etc/sysctl.d/99-sysctl.conf  
/etc/systemd/journald.conf  
/etc/systemd/logind.conf  
/etc/systemd/networkd.conf  
/etc/systemd/pstore.conf  
/etc/systemd/sleep.conf  
/etc/systemd/system.conf  
/etc/systemd/user.conf  
/etc/xdg/systemd/user  

#### 2.26.4. Executable Files
/bin/journalctl  
/bin/loginctl  
/bin/networkctl  
/bin/systemctl  
/bin/systemd  
/bin/systemd-ask-password  
/bin/systemd-creds  
/bin/systemd-escape  
/bin/systemd-firstboot  
/bin/systemd-inhibit  
/bin/systemd-machine-id-setup  
/bin/systemd-notify  
/bin/systemd-repart  
/bin/systemd-sysext  
/bin/systemd-sysusers  
/bin/systemd-sysusers  
/bin/systemd-tmpfiles  
/bin/systemd-tmpfiles  
/bin/systemd-tty-ask-password-agent  
/usr/bin/busctl  
/usr/bin/hostnamectl  
/usr/bin/kernel-install  
/usr/bin/localectl  
/usr/bin/systemd-analyze  
/usr/bin/systemd-cat  
/usr/bin/systemd-cgls  
/usr/bin/systemd-cgtop  
/usr/bin/systemd-cryptenroll  
/usr/bin/systemd-delta  
/usr/bin/systemd-detect-virt  
/usr/bin/systemd-id128  
/usr/bin/systemd-mount  
/usr/bin/systemd-path  
/usr/bin/systemd-run  
/usr/bin/systemd-socket-activate  
/usr/bin/systemd-stdio-bridge  
/usr/bin/systemd-umount  
/usr/bin/timedatectl  

<br>

### 2.27 systemd-sysv Package
#### 2.27.1. Official Package Description
system and service manager - SysV compatibility symlinks  
This package provides manual pages and compatibility symlinks needed for  
systemd to replace sysvinit.  
.  
Installing systemd-sysv will overwrite /sbin/init with a symlink to systemd.  

#### 2.27.2. Depended Packages
systemd  

#### 2.27.3. Configuration Files
(None)

#### 2.27.4. Executable Files
/sbin/halt  
/sbin/init  
/sbin/poweroff  
/sbin/reboot  
/sbin/runlevel  
/sbin/shutdown  
/sbin/telinit  

<br>

### 2.28 tasksel-data Package
#### 2.28.1. Official Package Description
official tasks used for installation of Debian systems  
This package contains data about the standard tasks available on a Debian  
system.  

#### 2.28.2. Depended Packages
tasksel  

#### 2.28.3. Configuration Files
(None)

#### 2.28.4. Executable Files
(None)

<br>

### 2.29 udev Package
#### 2.29.1. Official Package Description
/dev/ and hotplug management daemon  
udev is a daemon which dynamically creates and removes device nodes from  
/dev/, handles hotplug events and loads drivers at boot time.  

#### 2.29.2. Depended Packages
adduser  
libacl1  
libblkid1  
libc6  
libcap2  
libkmod2  
libselinux1  
libudev1  

#### 2.29.3. Configuration Files
/etc/init.d/udev  
/etc/udev/udev.conf  

#### 2.29.4. Executable Files
/bin/systemd-hwdb  
/bin/udevadm  

<br>

### 2.30 vim-common Package
#### 2.30.1. Official Package Description
Vi IMproved - Common files  
Vim is an almost compatible version of the UNIX editor Vi.  
.  
This package contains files shared by all non GUI-enabled vim variants  
available in Debian.  Examples of such shared files are: manpages and  
configuration files.  

#### 2.30.2. Depended Packages
(None)

#### 2.30.3. Configuration Files
/etc/vim/vimrc  

#### 2.30.4. Executable Files
/usr/bin/helpztags  

<br>

### 2.31 vim-tiny Package
#### 2.31.1. Official Package Description
Vi IMproved - enhanced vi editor - compact version  
Vim is an almost compatible version of the UNIX editor Vi.  
.  
This package contains a minimal version of Vim compiled with no GUI and  
a small subset of features. This package's sole purpose is to provide  
the vi binary for base installations.  
.  
If a vim binary is wanted, try one of the following more featureful  
packages: vim, vim-nox, vim-motif, or vim-gtk3.  

#### 2.31.2. Depended Packages
libacl1  
libc6  
libselinux1  
libtinfo6  
vim-common  

#### 2.31.3. Configuration Files
/etc/vim/vimrc.tiny  

#### 2.31.4. Executable Files
/usr/bin/vim.tiny  

<br>

### 2.32 whiptail Package
#### 2.32.1. Official Package Description
Displays user-friendly dialog boxes from shell scripts  
Whiptail is a "dialog" replacement using newt instead of ncurses. It  
provides a method of displaying several different types of dialog boxes  
from shell scripts. This allows a developer of a script to interact with  
the user in a much friendlier manner.  

#### 2.32.2. Depended Packages
libc6  
libnewt0.52  
libpopt0  
libslang2  

#### 2.32.3. Configuration Files
(None)

#### 2.32.4. Executable Files
/usr/bin/whiptail  

<br>

## 3. Standard Packages
---
These are the standard packages. They are normally expected in Debian  installations.

At my last check, the following packages are marked as standard:

**amd64-microcode:** Processor microcode firmware for AMD CPUs  
**apt-listchanges:** package change history notification tool  
**bash-completion:** programmable completion for the bash shell  
**bind9-dnsutils:** Clients provided with BIND 9  
**bind9-host:** DNS Lookup Utility  
**bzip2:** high-quality block-sorting file compressor - utilities  
**ca-certificates:** Common CA certificates  
**dbus:** simple interprocess messaging system (system message bus)  
**debian-faq:** Debian Frequently Asked Questions  
**doc-debian:** Debian Project documentation and other documents  
**file:** Recognize the type of data in a file using "magic" numbers  
**gettext-base:** GNU Internationalization utilities for the base system  
**groff-base:** GNU troff text-formatting system (base system components)  
**inetutils-telnet:** telnet client  
**intel-microcode:** Processor microcode firmware for Intel CPUs  
**krb5-locales:** internationalization support for MIT Kerberos  
**libc-l10n:** GNU C Library: localization files  
**liblockfile-bin:** support binaries for and cli utilities based on liblockfile  
**libnss-systemd:** nss module providing dynamic user and group name resolution  
**libpam-systemd:** system and service manager - PAM module  
**locales:** GNU C Library: National Language (locale) data [support]  
**lsof:** utility to list open files  
**man-db:** tools for reading manual pages  
**manpages:** Manual pages about using a GNU/Linux system  
**media-types:** List of standard media types and their usual file extension  
**mime-support:** transitional package  
**ncurses-term:** additional terminal type definitions  
**netcat-traditional:** TCP/IP swiss army knife  
**openssh-client:** secure shell (SSH) client, for secure access to remote machines  
**pciutils:** PCI utilities  
**perl:** Larry Wall's Practical Extraction and Report Language  
**python3-reportbug:** Python modules for interacting with bug tracking systems  
**reportbug:** reports bugs in the Debian distribution  
**systemd-timesyncd:** minimalistic service to synchronize local time with NTP servers  
**traceroute:** Traces the route taken by packets over an IPv4/IPv6 network  
**ucf:** Update Configuration File(s): preserve user changes to config files  
**util-linux-extra:** interactive login tools  
**wamerican:** American English dictionary words for /usr/share/dict  
**wget:** retrieves files from the web  
**xz-utils:** XZ-format compression utilities  

<br>

### 3.1 amd64-microcode Package
#### 3.1.1. Official Package Description
Processor microcode firmware for AMD CPUs  
This package contains microcode patches for all AMD AMD64  
processors.  AMD releases microcode patches to correct  
processor behavior as documented in the respective processor  
revision guides.  This package includes both AMD CPU microcode  
patches and AMD SEV firmware updates.  
.  
For Intel processors, please refer to the intel-microcode package.  

#### 3.1.2. Depended Packages
(None)

#### 3.1.3. Configuration Files
/etc/default/amd64-microcode  
/etc/modprobe.d/amd64-microcode-blacklist.conf  

#### 3.1.4. Executable Files
(None)

<br>

### 3.2 apt-listchanges Package
#### 3.2.1. Official Package Description
package change history notification tool  
The tool apt-listchanges can compare a new version of a  
package with the one currently installed and show what has been  
changed, by extracting the relevant entries from the Debian changelog  
and NEWS files.  
.  
It can be run on several .deb archives at a time to get a list of all  
changes that would be caused by installing or upgrading a group of  
packages. When configured as an APT plugin it will do this  
automatically during upgrades.  

#### 3.2.2. Depended Packages
apt  
debconf  
python3-apt  
python3-debconf  
python3:any  
sensible-utils  
ucf  

#### 3.2.3. Configuration Files
/etc/apt/apt.conf.d/20listchanges  

#### 3.2.4. Executable Files
/usr/bin/apt-listchanges  

<br>

### 3.3 bash-completion Package
#### 3.3.1. Official Package Description
programmable completion for the bash shell  
bash completion extends bash's standard completion behavior to achieve  
complex command lines with just a few keystrokes.  This project was  
conceived to produce programmable completion routines for the most  
common Linux/UNIX commands, reducing the amount of typing sysadmins  
and programmers need to do on a daily basis.  

#### 3.3.2. Depended Packages
(None)

#### 3.3.3. Configuration Files
/etc/bash_completion  
/etc/profile.d/bash_completion.sh  

#### 3.3.4. Executable Files
/usr/bin/dh_bash-completion  

<br>

### 3.4 bind9-dnsutils Package
#### 3.4.1. Official Package Description
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

#### 3.4.2. Depended Packages
bind9-host  
bind9-libs  
libc6  
libedit2  
libidn2-0  
libkrb5-3  
libprotobuf-c1  

#### 3.4.3. Configuration Files
(None)

#### 3.4.4. Executable Files
/usr/bin/delv  
/usr/bin/dig  
/usr/bin/dnstap-read  
/usr/bin/mdig  
/usr/bin/nslookup  
/usr/bin/nsupdate  

<br>

### 3.5 bind9-host Package
#### 3.5.1. Official Package Description
DNS Lookup Utility  
This package provides the 'host' DNS lookup utility in the form that  
is bundled with the BIND 9 sources.  

#### 3.5.2. Depended Packages
bind9-libs  
libc6  
libidn2-0  

#### 3.5.3. Configuration Files
(None)

#### 3.5.4. Executable Files
/usr/bin/host  

<br>

### 3.6 bzip2 Package
#### 3.6.1. Official Package Description
high-quality block-sorting file compressor - utilities  
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

#### 3.6.2. Depended Packages
libbz2-1.0  
libc6  

#### 3.6.3. Configuration Files
(None)

#### 3.6.4. Executable Files
/bin/bunzip2  
/bin/bzcat  
/bin/bzcmp  
/bin/bzdiff  
/bin/bzegrep  
/bin/bzexe  
/bin/bzfgrep  
/bin/bzgrep  
/bin/bzip2  
/bin/bzip2recover  
/bin/bzless  
/bin/bzmore  

<br>

### 3.7 ca-certificates Package
#### 3.7.1. Official Package Description
Common CA certificates  
Contains the certificate authorities shipped with Mozilla's browser to allow  
SSL-based applications to check for the authenticity of SSL connections.  
.  
Please note that Debian can neither confirm nor deny whether the  
certificate authorities whose certificates are included in this package  
have in any way been audited for trustworthiness or RFC 3647 compliance.  
Full responsibility to assess them belongs to the local system  
administrator.  

#### 3.7.2. Depended Packages
debconf  
openssl  

#### 3.7.3. Configuration Files
(None)

#### 3.7.4. Executable Files
/usr/sbin/update-ca-certificates  

<br>

### 3.8 dbus Package
#### 3.8.1. Official Package Description
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

#### 3.8.2. Depended Packages
dbus-bin  
dbus-daemon  
dbus-system-bus-common  
init-system-helpers  
libc6  
libdbus-1-3  
libexpat1  
libsystemd0  

#### 3.8.3. Configuration Files
/etc/default/dbus  
/etc/init.d/dbus  

#### 3.8.4. Executable Files
(None)

<br>

### 3.9 debian-faq Package
#### 3.9.1. Official Package Description
Debian Frequently Asked Questions  
In this package you will find the Debian GNU/Linux FAQ, which gives  
frequently asked questions (with their answers!) about the Debian distribution  
(Debian GNU/Linux and others) and about the Debian project.  
Some answers assume some knowledge of Unix-like operating systems.  
However, as little prior knowledge as possible is assumed: answers to general  
beginners questions will be kept simple.  
.  
This document is available at https://www.debian.org/doc/manuals/debian-faq/  
as well as from the Debian file server at https://deb.debian.org/debian/doc/FAQ  
and mirrors thereof.  
.  
The document is supplied in HTML, PDF, and plain text.  
.  
If you're new to Debian, and like to read documentation from your local system,  
without using the network, install this package.  

#### 3.9.2. Depended Packages
(None)

#### 3.9.3. Configuration Files
(None)

#### 3.9.4. Executable Files
(None)

<br>

### 3.10 doc-debian Package
#### 3.10.1. Official Package Description
Debian Project documentation and other documents  
The Debian Project is an association of individuals who have made  
common cause to create a free operating system.  
.  
In this package, you will find:  
Debian Linux Manifesto,  
Constitution for the Debian Project,  
Debian Social Contract,  
Debian Free Software Guidelines.  
.  
Additionally provided are:  
Debian Bug Tracking System documentation, and  
Introduction to the Debian mailing lists.  
.  
All of these files are available at http://ftp.debian.org/debian/doc/ and  
mirrors thereof.  

#### 3.10.2. Depended Packages
(None)

#### 3.10.3. Configuration Files
(None)

#### 3.10.4. Executable Files
(None)

<br>

### 3.11 file Package
#### 3.11.1. Official Package Description
Recognize the type of data in a file using "magic" numbers  
The file command is "a file type guesser", a command-line tool that  
tells you in words what kind of data a file contains.  
.  
This package contains the file program itself.  

#### 3.11.2. Depended Packages
libc6  
libmagic1  

#### 3.11.3. Configuration Files
(None)

#### 3.11.4. Executable Files
/usr/bin/file  

<br>

### 3.12 gettext-base Package
#### 3.12.1. Official Package Description
GNU Internationalization utilities for the base system  
This package includes the gettext and ngettext programs which allow  
other packages to internationalize the messages given by shell scripts.  

#### 3.12.2. Depended Packages
libc6  

#### 3.12.3. Configuration Files
(None)

#### 3.12.4. Executable Files
/usr/bin/envsubst  
/usr/bin/gettext  
/usr/bin/gettext.sh  
/usr/bin/ngettext  

<br>

### 3.13 groff-base Package
#### 3.13.1. Official Package Description
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

#### 3.13.2. Depended Packages
libc6  
libgcc-s1  
libstdc++6  
libuchardet0  

#### 3.13.3. Configuration Files
/etc/groff/man.local  
/etc/groff/mdoc.local  

#### 3.13.4. Executable Files
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

### 3.14 inetutils-telnet Package
#### 3.14.1. Official Package Description
telnet client  
The telnet command is used for interactive communication with another host  
using the TELNET protocol.  
.  
This implementation supports Kerberos, for authentication and encryption.  

#### 3.14.2. Depended Packages
libc6  
libcom-err2  
libk5crypto3  
libkrb5-3  
libtinfo6  
netbase  

#### 3.14.3. Configuration Files
(None)

#### 3.14.4. Executable Files
/usr/bin/inetutils-telnet  

<br>

### 3.15 intel-microcode Package
#### 3.15.1. Official Package Description
Processor microcode firmware for Intel CPUs  
This package contains updated system processor microcode for  
Intel i686 and Intel X86-64 processors.  Intel releases microcode  
updates to correct processor behavior as documented in the  
respective processor specification updates.  
.  
For AMD processors, please refer to the amd64-microcode package.  

#### 3.15.2. Depended Packages
iucode-tool  

#### 3.15.3. Configuration Files
/etc/default/intel-microcode  
/etc/kernel/preinst.d/intel-microcode  
/etc/modprobe.d/intel-microcode-blacklist.conf  

#### 3.15.4. Executable Files
(None)

<br>

### 3.16 krb5-locales Package
#### 3.16.1. Official Package Description
internationalization support for MIT Kerberos  
Kerberos is a system for authenticating users and services on a network.  
Kerberos is a trusted third-party service.  That means that there is a  
third party (the Kerberos server) that is trusted by all the entities on  
the network (users and services, usually called "principals").  
.  
This is the MIT reference implementation of Kerberos V5.  
.  
This package contains internationalized messages for MIT Kerberos.  

#### 3.16.2. Depended Packages
(None)

#### 3.16.3. Configuration Files
(None)

#### 3.16.4. Executable Files
(None)

<br>

### 3.17 libc-l10n Package
#### 3.17.1. Official Package Description
GNU C Library: localization files  
This package contains the translation files for the GNU C library and  
utility programs.  

#### 3.17.2. Depended Packages
(None)

#### 3.17.3. Configuration Files
(None)

#### 3.17.4. Executable Files
(None)

<br>

### 3.18 liblockfile-bin Package
#### 3.18.1. Official Package Description
support binaries for and cli utilities based on liblockfile  
This package contains support binaries for the liblockfile library,  
and the command-line utility dotlockfile''.  

#### 3.18.2. Depended Packages
libc6  

#### 3.18.3. Configuration Files
(None)

#### 3.18.4. Executable Files
/usr/bin/dotlockfile  

<br>

### 3.19 libnss-systemd Package
#### 3.19.1. Official Package Description
nss module providing dynamic user and group name resolution  
nss-systemd is a plug-in module for the GNU Name Service Switch (NSS)  
functionality of the GNU C Library (glibc), providing UNIX user and group name  
resolution for dynamic users and groups allocated through the DynamicUser=  
option in systemd unit files. See systemd.exec(5) for details on this  
option.  
.  
Installing this package automatically adds the module to /etc/nsswitch.conf.  

#### 3.19.2. Depended Packages
libc6  
libcap2  
systemd  

#### 3.19.3. Configuration Files
(None)

#### 3.19.4. Executable Files
(None)

<br>

### 3.20 libpam-systemd Package
#### 3.20.1. Official Package Description
system and service manager - PAM module  
This package contains the PAM module which registers user sessions in  
the systemd control group hierarchy for logind.  
.  
If in doubt, do install this package.  
.  
Packages that depend on logind functionality need to depend on libpam-systemd.  

#### 3.20.2. Depended Packages
default-dbus-system-bus  
libc6  
libcap2  
libpam-runtime  
libpam0g  
systemd  
systemd-sysv  

#### 3.20.3. Configuration Files
(None)

#### 3.20.4. Executable Files
(None)

<br>

### 3.21 locales Package
#### 3.21.1. Official Package Description
GNU C Library: National Language (locale) data [support]  
Machine-readable data files, shared objects and programs used by the  
C library for localization (l10n) and internationalization (i18n) support.  
.  
This package contains tools to generate locale definitions from source  
files (included in this package). It allows you to customize which  
definitions actually get generated. This is a space-saver over how this  
package used to be, with all locales generated by default. This created  
a package that unpacked to an excess of 30 megs.  

#### 3.21.2. Depended Packages
debconf  
libc-bin  
libc-l10n  

#### 3.21.3. Configuration Files
/etc/locale.alias  

#### 3.21.4. Executable Files
/usr/sbin/locale-gen  
/usr/sbin/update-locale  
/usr/sbin/validlocale  

<br>

### 3.22 lsof Package
#### 3.22.1. Official Package Description
utility to list open files  
Lsof is a Unix-specific diagnostic tool.  Its name stands  
for LiSt Open Files, and it does just that.  It lists  
information about any files that are open, by processes  
currently running on the system.  

#### 3.22.2. Depended Packages
libc6  
libselinux1  
libtirpc3  

#### 3.22.3. Configuration Files
(None)

#### 3.22.4. Executable Files
/usr/bin/lsof  

<br>

### 3.23 man-db Package
#### 3.23.1. Official Package Description
tools for reading manual pages  
This package provides the man command, the primary way of examining the  
system help files (manual pages). Other utilities provided include the  
whatis and apropos commands for searching the manual page database, the  
manpath utility for determining the manual page search path, and the  
maintenance utilities mandb, catman and zsoelim. man-db uses the groff  
suite of programs to format and display the manual pages.  

#### 3.23.2. Depended Packages
bsdextrautils  
debconf  
groff-base  
libc6  
libgdbm6  
libpipeline1  
libseccomp2  
zlib1g  

#### 3.23.3. Configuration Files
/etc/apparmor.d/usr.bin.man  
/etc/cron.daily/man-db  
/etc/cron.weekly/man-db  
/etc/manpath.config  

#### 3.23.4. Executable Files
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

### 3.24 manpages Package
#### 3.24.1. Official Package Description
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

#### 3.24.2. Depended Packages
(None)

#### 3.24.3. Configuration Files
(None)

#### 3.24.4. Executable Files
(None)

<br>

### 3.25 media-types Package
#### 3.25.1. Official Package Description
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

#### 3.25.2. Depended Packages
(None)

#### 3.25.3. Configuration Files
/etc/mime.types  

#### 3.25.4. Executable Files
(None)

<br>

### 3.26 mime-support Package
#### 3.26.1. Official Package Description
transitional package  
This is a transitional package. It will be possible to remove it  
safely once its dependency chain has adjusted to depend on mailcap  
or media-types directly.  

#### 3.26.2. Depended Packages
mailcap  
media-types  

#### 3.26.3. Configuration Files
(None)

#### 3.26.4. Executable Files
(None)

<br>

### 3.27 ncurses-term Package
#### 3.27.1. Official Package Description
additional terminal type definitions  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains all of the numerous terminal definitions not found in  
the ncurses-base package.  

#### 3.27.2. Depended Packages
ncurses-base  

#### 3.27.3. Configuration Files
(None)

#### 3.27.4. Executable Files
(None)

<br>

### 3.28 netcat-traditional Package
#### 3.28.1. Official Package Description
TCP/IP swiss army knife  
A simple Unix utility which reads and writes data across network  
connections using TCP or UDP protocol. It is designed to be a reliable  
"back-end" tool that can be used directly or easily driven by other  
programs and scripts. At the same time it is a feature-rich network  
debugging and exploration tool, since it can create almost any kind  
of connection you would need and has several interesting built-in  
capabilities.  
.  
This is the "classic" netcat, written by *Hobbit*. It lacks many  
features found in netcat-openbsd.  

#### 3.28.2. Depended Packages
libc6  

#### 3.28.3. Configuration Files
(None)

#### 3.28.4. Executable Files
/bin/nc.traditional  

<br>

### 3.29 openssh-client Package
#### 3.29.1. Official Package Description
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

#### 3.29.2. Depended Packages
adduser  
libc6  
libedit2  
libfido2-1  
libgssapi-krb5-2  
libselinux1  
libssl3  
passwd  
zlib1g  

#### 3.29.3. Configuration Files
/etc/ssh/ssh_config  

#### 3.29.4. Executable Files
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

### 3.30 pciutils Package
#### 3.30.1. Official Package Description
PCI utilities  
This package contains various utilities for inspecting and setting of  
devices connected to the PCI bus.  

#### 3.30.2. Depended Packages
libc6  
libkmod2  
libpci3  

#### 3.30.3. Configuration Files
(None)

#### 3.30.4. Executable Files
/usr/bin/lspci  
/usr/bin/setpci  
/usr/sbin/update-pciids  

<br>

### 3.31 perl Package
#### 3.31.1. Official Package Description
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

#### 3.31.2. Depended Packages
dpkg  
libperl5.36  
perl-base  
perl-modules-5.36  

#### 3.31.3. Configuration Files
/etc/perl/Net/libnet.cfg  

#### 3.31.4. Executable Files
/usr/bin/corelist  
/usr/bin/cpan  
/usr/bin/enc2xs  
/usr/bin/encguess  
/usr/bin/h2ph  
/usr/bin/h2xs  
/usr/bin/instmodsh  
/usr/bin/json_pp  
/usr/bin/libnetcfg  
/usr/bin/perlbug  
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
/usr/bin/ptar  
/usr/bin/ptardiff  
/usr/bin/ptargrep  
/usr/bin/shasum  
/usr/bin/shasum  
/usr/bin/splain  
/usr/bin/streamzip  
/usr/bin/xsubpp  
/usr/bin/zipdetails  

<br>

### 3.32 python3-reportbug Package
#### 3.32.1. Official Package Description
Python modules for interacting with bug tracking systems  
reportbug is a tool designed to make the reporting of bugs in Debian  
and derived distributions relatively painless.  
.  
This package includes Python modules which may be reusable by other  
tools that want to interact with the Debian bug tracking system.  
.  
To actually report a bug, install the reportbug package.  

#### 3.32.2. Depended Packages
apt  
file  
python3-apt  
python3-debian  
python3-debianbts  
python3-requests  
python3:any  
sensible-utils  

#### 3.32.3. Configuration Files
(None)

#### 3.32.4. Executable Files
(None)

<br>

### 3.33 reportbug Package
#### 3.33.1. Official Package Description
reports bugs in the Debian distribution  
reportbug is a tool designed to make the reporting of bugs in Debian  
and derived distributions relatively painless.  Its features include:  
.  
Integration with many mail user agents.  
Access to outstanding bug reports to make it easier to identify  
whether problems have already been reported.  
Automatic checking for newer versions of packages.  
Optional automatic verification of integrity of packages via debsums.  
Support for following-up on outstanding reports.  
Optional PGP/GnuPG integration.  
.  
Bug reporting in Debian relies on email; reportbug can use a local  
mail transport agent (like exim or sendmail), submit directly through  
an external mail server, or pass messages to an installed mail user  
agent (e.g., mutt) for submission.  
.  
This package also includes the "querybts" script for browsing the  
Debian bug tracking system.  

#### 3.33.2. Depended Packages
apt  
python3-reportbug  
python3:any  
sensible-utils  

#### 3.33.3. Configuration Files
/etc/reportbug.conf  

#### 3.33.4. Executable Files
/usr/bin/querybts  
/usr/bin/reportbug  

<br>

### 3.34 systemd-timesyncd Package
#### 3.34.1. Official Package Description
minimalistic service to synchronize local time with NTP servers  
The package contains the systemd-timesyncd system service that may be used to  
synchronize the local system clock with a remote Network Time Protocol server.  

#### 3.34.2. Depended Packages
libc6  
libsystemd-shared  
systemd  

#### 3.34.3. Configuration Files
/etc/dhcp/dhclient-exit-hooks.d/timesyncd  
/etc/systemd/timesyncd.conf  

#### 3.34.4. Executable Files
(None)

<br>

### 3.35 traceroute Package
#### 3.35.1. Official Package Description
Traces the route taken by packets over an IPv4/IPv6 network  
The traceroute utility displays the route used by IP packets on their way to a  
specified network (or Internet) host. Traceroute displays the IP number and  
host name (if possible) of the machines along the route taken by the packets.  
Traceroute is used as a network debugging tool. If you're having network  
connectivity problems, traceroute will show you where the trouble is coming  
from along the route.  
.  
Install traceroute if you need a tool for diagnosing network connectivity  
problems.  

#### 3.35.2. Depended Packages
libc6  

#### 3.35.3. Configuration Files
(None)

#### 3.35.4. Executable Files
/usr/bin/lft.db  
/usr/bin/traceproto.db  
/usr/bin/traceroute-nanog  
/usr/bin/traceroute.db  
/usr/bin/traceroute6.db  
/usr/sbin/tcptraceroute.db  

<br>

### 3.36 ucf Package
#### 3.36.1. Official Package Description
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

#### 3.36.2. Depended Packages
debconf  
sensible-utils  

#### 3.36.3. Configuration Files
/etc/ucf.conf  

#### 3.36.4. Executable Files
/usr/bin/lcf  
/usr/bin/ucf  
/usr/bin/ucfq  
/usr/bin/ucfr  

<br>

### 3.37 util-linux-extra Package
#### 3.37.1. Official Package Description
interactive login tools  
Tools commonly found on systems where humans login interactively,  
or are needed with non-standard system configurations.  

#### 3.37.2. Depended Packages
libaudit1  
libc6  
libsmartcols1  

#### 3.37.3. Configuration Files
/etc/default/hwclock  
/etc/init.d/hwclock.sh  

#### 3.37.4. Executable Files
/sbin/hwclock  
/usr/bin/fincore  
/usr/bin/lsfd  
/usr/bin/lsirq  

<br>

### 3.38 wamerican Package
#### 3.38.1. Official Package Description
American English dictionary words for /usr/share/dict  
This package provides the file /usr/share/dict/american-english  
containing a list of English words with American spellings.  
This list can be used by spelling checkers, and by programs such  
as look(1).  
.  
There are also -small, -large, and -huge versions of this word list,  
and there are wbritish* and wcanadian* packages as well.  

#### 3.38.2. Depended Packages
debconf  

#### 3.38.3. Configuration Files
(None)

#### 3.38.4. Executable Files
(None)

<br>

### 3.39 wget Package
#### 3.39.1. Official Package Description
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

#### 3.39.2. Depended Packages
libc6  
libgnutls30  
libidn2-0  
libnettle8  
libpcre2-8-0  
libpsl5  
libuuid1  
zlib1g  

#### 3.39.3. Configuration Files
/etc/wgetrc  

#### 3.39.4. Executable Files
/usr/bin/wget  

<br>

### 3.40 xz-utils Package
#### 3.40.1. Official Package Description
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

#### 3.40.2. Depended Packages
libc6  
liblzma5  

#### 3.40.3. Configuration Files
(None)

#### 3.40.4. Executable Files
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
There is no classification as necessary packages. These are the packages that are not classified as required, important, or standard; but some of the required, important, or standard packages are depended on these  packages. 

So you may expect these packages in Debian installations too.

Some packages listed here are virtual packages. 

Virtual packages are placeholders that represent a group of packages with  similar functionality. These virtual packages allow users to install any  package that provides the functionality specified by the virtual package name. They are particularly useful for creating dependencies between packages without tying them to specific implementations.

I mark the following packages as necessary:

**awk:** Virtual package provided by gawk, mawk, or original-awk  
**bind9-libs:** Shared Libraries used by BIND 9  
**bsdextrautils:** extra utilities from 4.4BSD-Lite  
**dbus-bin:** simple interprocess messaging system (command line utilities)  
**dbus-daemon:** simple interprocess messaging system (reference message bus)  
**dbus-system-bus-common:** simple interprocess messaging system (system bus configuration)  
**default-dbus-system-bus:** Virtual package provided by dbus package  
**iucode-tool:** Intel processor microcode tool  
**libacl1:** access control list - shared library  
**libapt-pkg6.0:** package management runtime library  
**libattr1:** extended attribute handling - shared library  
**libaudit1:** Dynamic library for security auditing  
**libblkid1:** block device ID library  
**libbpf1:** eBPF helper library (shared library)  
**libbsd0:** utility functions from BSD systems - shared library  
**libbz2-1.0:** high-quality block-sorting file compressor library - runtime  
**libc6:** GNU C Library: Shared libraries  
**libcap-ng0:** alternate POSIX capabilities library  
**libcap2:** POSIX 1003.1e capabilities (library)  
**libcap2-bin:** POSIX 1003.1e capabilities (utilities)  
**libcom-err2:** common error description library  
**libcrypt1:** libcrypt shared library  
**libcryptsetup12:** disk encryption support - shared library  
**libdb5.3:** Berkeley v5.3 Database Libraries [runtime]  
**libdbus-1-3:** simple interprocess messaging system (library)  
**libdebconfclient0:** Debian Configuration Management System (C-implementation library)  
**libedit2:** BSD editline and history libraries  
**libelf1:** library to read and write ELF files  
**libexpat1:** XML parsing C library - runtime library  
**libext2fs2:** ext2/ext3/ext4 file system libraries  
**libfdisk1:** fdisk partitioning library  
**libfido2-1:** library for generating and verifying FIDO 2.0 objects  
**libgcc-s1:** GCC support library  
**libgcrypt20:** LGPL Crypto library - runtime library  
**libgdbm6:** GNU dbm database routines (runtime version)  
**libgmp10:** Multiprecision arithmetic library  
**libgnutls30:** GNU TLS library - main runtime library  
**libgpg-error0:** GnuPG development runtime library  
**libgssapi-krb5-2:** MIT Kerberos runtime libraries - krb5 GSS-API Mechanism  
**libidn2-0:** Internationalized domain names (IDNA2008/TR46) library  
**libk5crypto3:** MIT Kerberos runtime libraries - Crypto Library  
**libkmod2:** libkmod shared library  
**libkrb5-3:** MIT Kerberos runtime libraries  
**liblocale-gettext-perl:** module using libc functions for internationalization in Perl  
**liblz4-1:** Fast LZ compression algorithm library - runtime  
**liblzma5:** XZ-format compression library  
**libmagic1:** Recognize the type of data in a file using "magic" numbers - library  
**libmd0:** message digest functions from BSD systems - shared library  
**libmnl0:** minimalistic Netlink communication library  
**libmount1:** device mounting library  
**libncursesw6:** shared libraries for terminal handling (wide character support)  
**libnettle8:** low level cryptographic library (symmetric and one-way cryptos)  
**libnewt0.52:** Not Erik's Windowing Toolkit - text mode windowing with slang  
**libnftables1:** Netfilter nftables high level userspace API library  
**libp11-kit0:** library for loading and coordinating access to PKCS#11 modules - runtime  
**libpam0g:** Pluggable Authentication Modules library  
**libpci3:** PCI utilities (shared library)  
**libpcre2-8-0:** New Perl Compatible Regular Expression Library- 8 bit runtime files  
**libperl5.36:** shared Perl library  
**libpipeline1:** Unix process pipeline manipulation library  
**libpopt0:** lib for parsing cmdline parameters  
**libproc2-0:** library for accessing process information from /proc  
**libprotobuf-c1:** Protocol Buffers C shared library (protobuf-c)  
**libpsl5:** Library for Public Suffix List (shared libraries)  
**libreadline8:** GNU readline and history libraries, run-time libraries  
**libseccomp2:** high level interface to Linux seccomp filter  
**libselinux1:** SELinux runtime shared libraries  
**libsemanage2:** SELinux policy management library  
**libslang2:** S-Lang programming library - runtime version  
**libsmartcols1:** smart column output alignment library  
**libss2:** command-line interface parsing library  
**libssl3:** Secure Sockets Layer toolkit - shared libraries  
**libstdc++6:** GNU Standard C++ Library v3  
**libsystemd-shared:** systemd shared private library  
**libsystemd0:** systemd utility library  
**libtext-charwidth-perl:** get display widths of characters on the terminal  
**libtext-iconv-perl:** module to convert between character sets in Perl  
**libtext-wrapi18n-perl:** internationalized substitute of Text::Wrap  
**libtinfo6:** shared low-level terminfo library for terminal handling  
**libtirpc3:** transport-independent RPC library  
**libuchardet0:** universal charset detection library - shared library  
**libudev1:** libudev shared library  
**libuuid1:** Universally Unique ID library  
**libxtables12:** netfilter xtables library  
**libzstd1:** fast lossless compression algorithm  
**logsave:** save the output of a command in a log file  
**mailcap:** Debians mailcap system, and support programs  
**openssl:** Secure Sockets Layer toolkit - cryptographic utility  
**perl-modules-5.36:** Core Perl modules  
**python3:** interactive high-level object-oriented language (default python3 version)  
**python3-apt:** Python 3 interface to libapt-pkg  
**python3-debconf:** interact with debconf from Python 3  
**python3-debian:** Python 3 modules to work with Debian-related data formats  
**python3-debianbts:** Python interface to Debian's Bug Tracking System  
**python3-requests:** elegant and simple HTTP library for Python3, built for human beings  
**tasksel:** tool for selecting tasks for installation on Debian systems  
**usrmerge:** Convert the system to the merged /usr directories scheme  
**zlib1g:** compression library - runtime  

<br>

### 4.1 awk Package
awk is a virtual package provided by gawk, mawk, or original-awk. If we install one of them, awk will be seen as installed too. 

As mawk being a required package and was documented at 1.23. we may consider  this package as documented too.

<br>

### 4.2 bind9-libs Package
#### 4.2.1. Official Package Description
Shared Libraries used by BIND 9  
The Berkeley Internet Name Domain (BIND 9) implements an Internet domain  
name server.  BIND 9 is the most widely-used name server software on the  
Internet, and is supported by the Internet Software Consortium, www.isc.org.  
.  
This package contains a bundle of shared libraries used by BIND 9.  

#### 4.2.2. Depended Packages
libc6  
libfstrm0  
libgssapi-krb5-2  
libjemalloc2  
libjson-c5  
libkrb5-3  
liblmdb0  
libmaxminddb0  
libnghttp2-14  
libprotobuf-c1  
libssl3  
libuv1  
libxml2  
zlib1g  

#### 4.2.3. Configuration Files
(None)

#### 4.2.4. Executable Files
(None)

<br>

### 4.3 bsdextrautils Package
#### 4.3.1. Official Package Description
extra utilities from 4.4BSD-Lite  
This package contains some extra BSD utilities: col, colcrt, colrm, column,  
hd, hexdump, look, ul and write.  
Other BSD utilities are provided by bsdutils and calendar.  

#### 4.3.2. Depended Packages
libc6  
libsmartcols1  
libtinfo6  

#### 4.3.3. Configuration Files
(None)

#### 4.3.4. Executable Files
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

### 4.4 dbus-bin Package
#### 4.4.1. Official Package Description
simple interprocess messaging system (command line utilities)  
D-Bus is a message bus, used for sending messages between applications.  
Conceptually, it fits somewhere in between raw sockets and CORBA in  
terms of complexity.  
.  
This package contains the D-Bus command-line utilities such as dbus-send  
and dbus-monitor.  

#### 4.4.2. Depended Packages
libc6  
libdbus-1-3  

#### 4.4.3. Configuration Files
(None)

#### 4.4.4. Executable Files
/usr/bin/dbus-cleanup-sockets  
/usr/bin/dbus-monitor  
/usr/bin/dbus-send  
/usr/bin/dbus-update-activation-environment  
/usr/bin/dbus-uuidgen  

<br>

### 4.5 dbus-daemon Package
#### 4.5.1. Official Package Description
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

#### 4.5.2. Depended Packages
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

#### 4.5.3. Configuration Files
(None)

#### 4.5.4. Executable Files
/usr/bin/dbus-daemon  
/usr/bin/dbus-run-session  

<br>

### 4.6 dbus-system-bus-common Package
#### 4.6.1. Official Package Description
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

#### 4.6.2. Depended Packages
adduser  

#### 4.6.3. Configuration Files
(None)

#### 4.6.4. Executable Files
(None)

<br>

### 4.7 default-dbus-system-bus Package
default-dbus-system-bus is a virtual package provided by dbus package. If  we install dbus, default-dbus-system-bus will be seen as installed too. 

As dbus being a standard package and was documented at 3.8. we may consider  this package as documented too.

<br>

### 4.8 iucode-tool Package
#### 4.8.1. Official Package Description
Intel processor microcode tool  
iucode_tool is a program to manipulate Intel\xc2\xae X86 and X86-64 processor  
microcode collections, and to use the kernel facilities to upgrade the  
microcode on Intel system processors.  
.  
It can load microcode data files in text and binary format, sort, list and  
filter the microcodes contained in these files, write selected microcodes to a  
new file in binary format, or upload them to the kernel.  
.  
It operates on non-free microcode data downloaded directly from Intel or  
installed by the intel-microcode package.  

#### 4.8.2. Depended Packages
libc6  

#### 4.8.3. Configuration Files
(None)

#### 4.8.4. Executable Files
/usr/sbin/iucode-tool  
/usr/sbin/iucode_tool  

<br>

### 4.9 libacl1 Package
#### 4.9.1. Official Package Description
access control list - shared library  
This package contains the shared library containing the POSIX 1003.1e  
draft standard 17 functions for manipulating access control lists.  

#### 4.9.2. Depended Packages
libc6  

#### 4.9.3. Configuration Files
(None)

#### 4.9.4. Executable Files
(None)

<br>

### 4.10 libapt-pkg6.0 Package
#### 4.10.1. Official Package Description
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

#### 4.10.2. Depended Packages
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

#### 4.10.3. Configuration Files
(None)

#### 4.10.4. Executable Files
(None)

<br>

### 4.11 libattr1 Package
#### 4.11.1. Official Package Description
extended attribute handling - shared library  
Contains the runtime environment required by programs that make use  
of extended attributes.  

#### 4.11.2. Depended Packages
libc6  

#### 4.11.3. Configuration Files
/etc/xattr.conf  

#### 4.11.4. Executable Files
(None)

<br>

### 4.12 libaudit1 Package
#### 4.12.1. Official Package Description
Dynamic library for security auditing  
The audit-libs package contains the dynamic libraries needed for  
applications to use the audit framework. It is used to monitor systems for  
security related events.  

#### 4.12.2. Depended Packages
libaudit-common  
libc6  
libcap-ng0  

#### 4.12.3. Configuration Files
(None)

#### 4.12.4. Executable Files
(None)

<br>

### 4.13 libblkid1 Package
#### 4.13.1. Official Package Description
block device ID library  
The blkid library allows system programs such as fsck and mount to  
quickly and easily find block devices by filesystem UUID or label.  
This allows system administrators to avoid specifying filesystems by  
hard-coded device names and use a logical naming system instead.  

#### 4.13.2. Depended Packages
libc6  

#### 4.13.3. Configuration Files
(None)

#### 4.13.4. Executable Files
(None)

<br>

### 4.14 libbpf1 Package
#### 4.14.1. Official Package Description
eBPF helper library (shared library)  
libbpf is a library for loading eBPF programs and reading and  
manipulating eBPF objects from user-space.  
.  
This package contains the shared library.  

#### 4.14.2. Depended Packages
libc6  
libelf1  
zlib1g  

#### 4.14.3. Configuration Files
(None)

#### 4.14.4. Executable Files
(None)

<br>

### 4.15 libbsd0 Package
#### 4.15.1. Official Package Description
utility functions from BSD systems - shared library  
This library provides some C functions such as strlcpy() that are commonly  
available on BSD systems but not on others like GNU systems.  
.  
For a detailed list of the provided functions, please see the libbsd-dev  
package description.  

#### 4.15.2. Depended Packages
libc6  
libmd0  

#### 4.15.3. Configuration Files
(None)

#### 4.15.4. Executable Files
(None)

<br>

### 4.16 libbz2-1.0 Package
#### 4.16.1. Official Package Description
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

#### 4.16.2. Depended Packages
libc6  

#### 4.16.3. Configuration Files
(None)

#### 4.16.4. Executable Files
(None)

<br>

### 4.17 libc6 Package
#### 4.17.1. Official Package Description
GNU C Library: Shared libraries  
Contains the standard libraries that are used by nearly all programs on  
the system. This package includes shared versions of the standard C library  
and the standard math library, as well as many others.  

#### 4.17.2. Depended Packages
libgcc-s1  

#### 4.17.3. Configuration Files
/etc/ld.so.conf.d/x86_64-linux-gnu.conf  

#### 4.17.4. Executable Files
(None)

<br>

### 4.18 libcap-ng0 Package
#### 4.18.1. Official Package Description
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

#### 4.18.2. Depended Packages
libc6  

#### 4.18.3. Configuration Files
(None)

#### 4.18.4. Executable Files
(None)

<br>

### 4.19 libcap2 Package
#### 4.19.1. Official Package Description
POSIX 1003.1e capabilities (library)  
Libcap implements the user-space interfaces to the POSIX 1003.1e capabilities  
available in Linux kernels. These capabilities are a partitioning of the all  
powerful root privilege into a set of distinct privileges.  
.  
This package contains the shared library.  

#### 4.19.2. Depended Packages
libc6  

#### 4.19.3. Configuration Files
(None)

#### 4.19.4. Executable Files
(None)

<br>

### 4.20 libcap2-bin Package
#### 4.20.1. Official Package Description
POSIX 1003.1e capabilities (utilities)  
Libcap implements the user-space interfaces to the POSIX 1003.1e capabilities  
available in Linux kernels. These capabilities are a partitioning of the all  
powerful root privilege into a set of distinct privileges.  
.  
This package contains additional utilities.  

#### 4.20.2. Depended Packages
libc6  
libcap2  

#### 4.20.3. Configuration Files
(None)

#### 4.20.4. Executable Files
/sbin/capsh  
/sbin/getcap  
/sbin/getpcaps  
/sbin/setcap  

<br>

### 4.21 libcom-err2 Package
#### 4.21.1. Official Package Description
common error description library  
libcomerr is an attempt to present a common error-handling mechanism to  
manipulate the most common form of error code in a fashion that does not  
have the problems identified with mechanisms commonly in use.  

#### 4.21.2. Depended Packages
libc6  

#### 4.21.3. Configuration Files
(None)

#### 4.21.4. Executable Files
(None)

<br>

### 4.22 libcrypt1 Package
#### 4.22.1. Official Package Description
libcrypt shared library  
libxcrypt is a modern library for one-way hashing of passwords.  
It supports DES, MD5, NTHASH, SUNMD5, SHA-2-256, SHA-2-512, and  
bcrypt-based password hashes  
It provides the traditional Unix 'crypt' and 'crypt_r' interfaces,  
as well as a set of extended interfaces like 'crypt_gensalt'.  

#### 4.22.2. Depended Packages
libc6  

#### 4.22.3. Configuration Files
(None)

#### 4.22.4. Executable Files
(None)

<br>

### 4.23 libcryptsetup12 Package
#### 4.23.1. Official Package Description
disk encryption support - shared library  
Cryptsetup provides an interface for configuring encryption on block  
devices (such as /home or swap partitions), using the Linux kernel  
device mapper target dm-crypt. It features integrated Linux Unified Key  
Setup (LUKS) support.  
.  
This package provides the libcryptsetup shared library.  

#### 4.23.2. Depended Packages
libargon2-1  
libblkid1  
libc6  
libdevmapper1.02.1  
libjson-c5  
libssl3  
libuuid1  

#### 4.23.3. Configuration Files
(None)

#### 4.23.4. Executable Files
(None)

<br>

### 4.24 libdb5.3 Package
#### 4.24.1. Official Package Description
Berkeley v5.3 Database Libraries [runtime]  
This is the runtime package for programs that use the v5.3 Berkeley  
database library.  

#### 4.24.2. Depended Packages
libc6  

#### 4.24.3. Configuration Files
(None)

#### 4.24.4. Executable Files
(None)

<br>

### 4.25 libdbus-1-3 Package
#### 4.25.1. Official Package Description
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

#### 4.25.2. Depended Packages
libc6  
libsystemd0  

#### 4.25.3. Configuration Files
(None)

#### 4.25.4. Executable Files
(None)

<br>

### 4.26 libdebconfclient0 Package
#### 4.26.1. Official Package Description
Debian Configuration Management System (C-implementation library)  
Debconf is a configuration management system for Debian packages. It is  
used by some packages to prompt you for information before they are  
installed. cdebconf is a reimplementation of the original debconf in C.  
.  
This library allows C programs to interface with cdebconf.  

#### 4.26.2. Depended Packages
libc6  

#### 4.26.3. Configuration Files
(None)

#### 4.26.4. Executable Files
(None)

<br>

### 4.27 libedit2 Package
#### 4.27.1. Official Package Description
BSD editline and history libraries  
Command line editor library provides generic line editing,  
history, and tokenization functions.  
.  
It slightly resembles GNU readline.  

#### 4.27.2. Depended Packages
libbsd0  
libc6  
libtinfo6  

#### 4.27.3. Configuration Files
(None)

#### 4.27.4. Executable Files
(None)

<br>

### 4.28 libelf1 Package
#### 4.28.1. Official Package Description
library to read and write ELF files  
The libelf1 package provides a shared library which allows reading and  
writing ELF files on a high level.  Third party programs depend on  
this package to read internals of ELF files.  The programs of the  
elfutils package use it also to generate new ELF files.  
.  
This library is part of elfutils.  

#### 4.28.2. Depended Packages
libc6  
zlib1g  

#### 4.28.3. Configuration Files
(None)

#### 4.28.4. Executable Files
(None)

<br>

### 4.29 libexpat1 Package
#### 4.29.1. Official Package Description
XML parsing C library - runtime library  
This package contains the runtime, shared library of expat, the C  
library for parsing XML. Expat is a stream-oriented parser in  
which an application registers handlers for things the parser  
might find in the XML document (like start tags).  

#### 4.29.2. Depended Packages
libc6  

#### 4.29.3. Configuration Files
(None)

#### 4.29.4. Executable Files
(None)

<br>

### 4.30 libext2fs2 Package
#### 4.30.1. Official Package Description
ext2/ext3/ext4 file system libraries  
The ext2, ext3 and ext4 file systems are successors of the original ext  
("extended") file system. They are the main file system types used for  
hard disks on Debian and other Linux systems.  
.  
This package provides the ext2fs and e2p libraries, for userspace software  
that directly accesses extended file systems. Programs that use libext2fs  
include e2fsck, mke2fs, and tune2fs. Programs that use libe2p include  
dumpe2fs, chattr, and lsattr.  

#### 4.30.2. Depended Packages
libc6  

#### 4.30.3. Configuration Files
(None)

#### 4.30.4. Executable Files
(None)

<br>

### 4.31 libfdisk1 Package
#### 4.31.1. Official Package Description
fdisk partitioning library  
The libfdisk library is used for manipulating partition tables. It is  
the core of the fdisk, cfdisk, and sfdisk tools.  

#### 4.31.2. Depended Packages
libblkid1  
libc6  
libuuid1  

#### 4.31.3. Configuration Files
(None)

#### 4.31.4. Executable Files
(None)

<br>

### 4.32 libfido2-1 Package
#### 4.32.1. Official Package Description
library for generating and verifying FIDO 2.0 objects  
A library for communicating with a FIDO device over USB or NFC, and for  
verifying attestation and assertion signatures. FIDO U2F (CTAP 1) and FIDO  
2.0 (CTAP 2) are supported.  
.  
This package contains the library.  

#### 4.32.2. Depended Packages
libc6  
libcbor0.8  
libssl3  
libudev1  
zlib1g  

#### 4.32.3. Configuration Files
(None)

#### 4.32.4. Executable Files
(None)

<br>

### 4.33 libgcc-s1 Package
#### 4.33.1. Official Package Description
GCC support library  
Shared version of the support library, a library of internal subroutines  
that GCC uses to overcome shortcomings of particular machines, or  
special needs for some languages.  

#### 4.33.2. Depended Packages
gcc-12-base  
libc6  

#### 4.33.3. Configuration Files
(None)

#### 4.33.4. Executable Files
(None)

<br>

### 4.34 libgcrypt20 Package
#### 4.34.1. Official Package Description
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

#### 4.34.2. Depended Packages
libc6  
libgpg-error0  

#### 4.34.3. Configuration Files
(None)

#### 4.34.4. Executable Files
(None)

<br>

### 4.35 libgdbm6 Package
#### 4.35.1. Official Package Description
GNU dbm database routines (runtime version)  
GNU dbm ('gdbm') is a library of database functions that use extendible  
hashing and works similarly to the standard UNIX 'dbm' functions.  
.  
The basic use of 'gdbm' is to store key/data pairs in a data file, thus  
providing a persistent version of the 'dictionary' Abstract Data Type  
('hash' to perl programmers).  

#### 4.35.2. Depended Packages
libc6  

#### 4.35.3. Configuration Files
(None)

#### 4.35.4. Executable Files
(None)

<br>

### 4.36 libgmp10 Package
#### 4.36.1. Official Package Description
Multiprecision arithmetic library  
GNU MP is a programmer's library for arbitrary precision  
arithmetic (ie, a bignum package).  It can operate on signed  
integer, rational, and floating point numeric types.  
.  
It has a rich set of functions, and the functions have a regular  
interface.  

#### 4.36.2. Depended Packages
libc6  

#### 4.36.3. Configuration Files
(None)

#### 4.36.4. Executable Files
(None)

<br>

### 4.37 libgnutls30 Package
#### 4.37.1. Official Package Description
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

#### 4.37.2. Depended Packages
libc6  
libgmp10  
libhogweed6  
libidn2-0  
libnettle8  
libp11-kit0  
libtasn1-6  
libunistring2  

#### 4.37.3. Configuration Files
(None)

#### 4.37.4. Executable Files
(None)

<br>

### 4.38 libgpg-error0 Package
#### 4.38.1. Official Package Description
GnuPG development runtime library  
Library that defines common error values, messages, and common  
runtime functionality for all GnuPG components.  Among these are GPG,  
GPGSM, GPGME, GPG-Agent, libgcrypt, pinentry, SmartCard Daemon and  
possibly more in the future.  
.  
It will likely be renamed "gpgrt" in the future.  

#### 4.38.2. Depended Packages
libc6  

#### 4.38.3. Configuration Files
(None)

#### 4.38.4. Executable Files
(None)

<br>

### 4.39 libgssapi-krb5-2 Package
#### 4.39.1. Official Package Description
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

#### 4.39.2. Depended Packages
libc6  
libcom-err2  
libk5crypto3  
libkrb5-3  
libkrb5support0  

#### 4.39.3. Configuration Files
(None)

#### 4.39.4. Executable Files
(None)

<br>

### 4.40 libidn2-0 Package
#### 4.40.1. Official Package Description
Internationalized domain names (IDNA2008/TR46) library  
Libidn2 implements the revised algorithm for internationalized domain  
names called IDNA2008/TR46.  
.  
This package contains runtime libraries.  

#### 4.40.2. Depended Packages
libc6  
libunistring2  

#### 4.40.3. Configuration Files
(None)

#### 4.40.4. Executable Files
(None)

<br>

### 4.41 libk5crypto3 Package
#### 4.41.1. Official Package Description
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

#### 4.41.2. Depended Packages
libc6  
libkrb5support0  

#### 4.41.3. Configuration Files
(None)

#### 4.41.4. Executable Files
(None)

<br>

### 4.42 libkmod2 Package
#### 4.42.1. Official Package Description
libkmod shared library  
This library provides an API for insertion, removal, configuration and  
listing of kernel modules.  

#### 4.42.2. Depended Packages
libc6  
liblzma5  
libssl3  
libzstd1  

#### 4.42.3. Configuration Files
(None)

#### 4.42.4. Executable Files
(None)

<br>

### 4.43 libkrb5-3 Package
#### 4.43.1. Official Package Description
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

#### 4.43.2. Depended Packages
libc6  
libcom-err2  
libk5crypto3  
libkeyutils1  
libkrb5support0  
libssl3  

#### 4.43.3. Configuration Files
(None)

#### 4.43.4. Executable Files
(None)

<br>

### 4.44 liblocale-gettext-perl Package
#### 4.44.1. Official Package Description
module using libc functions for internationalization in Perl  
The Locale::gettext module permits access from perl to the gettext() family of  
functions for retrieving message strings from databases constructed  
to internationalize software.  
.  
It provides gettext(), dgettext(), dcgettext(), textdomain(),  
bindtextdomain(), bind_textdomain_codeset(), ngettext(), dcngettext()  
and dngettext().  

#### 4.44.2. Depended Packages
libc6  
perl-base  
perlapi-5.36.0  

#### 4.44.3. Configuration Files
(None)

#### 4.44.4. Executable Files
(None)

<br>

### 4.45 liblz4-1 Package
#### 4.45.1. Official Package Description
Fast LZ compression algorithm library - runtime  
LZ4 is a very fast lossless compression algorithm, providing compression speed  
at 400 MB/s per core, scalable with multi-cores CPU. It also features an  
extremely fast decoder, with speed in multiple GB/s per core, typically  
reaching RAM speed limits on multi-core systems.  
.  
This package includes the shared library.  

#### 4.45.2. Depended Packages
libc6  

#### 4.45.3. Configuration Files
(None)

#### 4.45.4. Executable Files
(None)

<br>

### 4.46 liblzma5 Package
#### 4.46.1. Official Package Description
XZ-format compression library  
XZ is the successor to the Lempel-Ziv/Markov-chain Algorithm  
compression format, which provides memory-hungry but powerful  
compression (often better than bzip2) and fast, easy decompression.  
.  
The native format of liblzma is XZ; it also supports raw (headerless)  
streams and the older LZMA format used by lzma. (For 7-Zip's related  
format, use the p7zip package instead.)  

#### 4.46.2. Depended Packages
libc6  

#### 4.46.3. Configuration Files
(None)

#### 4.46.4. Executable Files
(None)

<br>

### 4.47 libmagic1 Package
#### 4.47.1. Official Package Description
Recognize the type of data in a file using "magic" numbers - library  
This library can be used to classify files according to magic number  
tests. It implements the core functionality of the file command.  

#### 4.47.2. Depended Packages
libbz2-1.0  
libc6  
liblzma5  
libmagic-mgc  
zlib1g  

#### 4.47.3. Configuration Files
/etc/magic  
/etc/magic.mime  

#### 4.47.4. Executable Files
(None)

<br>

### 4.48 libmd0 Package
#### 4.48.1. Official Package Description
message digest functions from BSD systems - shared library  
The libmd library provides various message digest ("hash") functions,  
as found on various BSDs on a library with the same name and with a  
compatible API.  

#### 4.48.2. Depended Packages
libc6  

#### 4.48.3. Configuration Files
(None)

#### 4.48.4. Executable Files
(None)

<br>

### 4.49 libmnl0 Package
#### 4.49.1. Official Package Description
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

#### 4.49.2. Depended Packages
libc6  

#### 4.49.3. Configuration Files
(None)

#### 4.49.4. Executable Files
(None)

<br>

### 4.50 libmount1 Package
#### 4.50.1. Official Package Description
device mounting library  
This device mounting library is used by mount and umount helpers.  

#### 4.50.2. Depended Packages
libblkid1  
libc6  
libselinux1  

#### 4.50.3. Configuration Files
(None)

#### 4.50.4. Executable Files
(None)

<br>

### 4.51 libncursesw6 Package
#### 4.51.1. Official Package Description
shared libraries for terminal handling (wide character support)  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains the shared libraries necessary to run programs  
compiled with ncursesw, which includes support for wide characters.  

#### 4.51.2. Depended Packages
libc6  
libtinfo6  

#### 4.51.3. Configuration Files
(None)

#### 4.51.4. Executable Files
(None)

<br>

### 4.52 libnettle8 Package
#### 4.52.1. Official Package Description
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

#### 4.52.2. Depended Packages
libc6  

#### 4.52.3. Configuration Files
(None)

#### 4.52.4. Executable Files
(None)

<br>

### 4.53 libnewt0.52 Package
#### 4.53.1. Official Package Description
Not Erik's Windowing Toolkit - text mode windowing with slang  
Newt is a windowing toolkit for text mode built from the slang library.  
It allows color text mode applications to easily use stackable windows,  
push buttons, check boxes, radio buttons, lists, entry fields, labels,  
and displayable text. Scrollbars are supported, and forms may be nested  
to provide extra functionality. This package contains the shared library  
for programs that have been built with newt.  

#### 4.53.2. Depended Packages
libc6  
libslang2  

#### 4.53.3. Configuration Files
(None)

#### 4.53.4. Executable Files
(None)

<br>

### 4.54 libnftables1 Package
#### 4.54.1. Official Package Description
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

#### 4.54.2. Depended Packages
libc6  
libgmp10  
libjansson4  
libmnl0  
libnftnl11  
libxtables12  

#### 4.54.3. Configuration Files
(None)

#### 4.54.4. Executable Files
(None)

<br>

### 4.55 libp11-kit0 Package
#### 4.55.1. Official Package Description
library for loading and coordinating access to PKCS#11 modules - runtime  
The p11-kit library provides a way to load and enumerate Public-Key  
Cryptography Standard #11 modules, along with a standard configuration  
setup for installing PKCS#11 modules so that they're discoverable. It  
also solves problems with coordinating the use of PKCS#11 by different  
components or libraries living in the same process.  
.  
This package contains the shared library required for applications loading  
and accessing PKCS#11 modules.  

#### 4.55.2. Depended Packages
libc6  
libffi8  

#### 4.55.3. Configuration Files
(None)

#### 4.55.4. Executable Files
(None)

<br>

### 4.56 libpam0g Package
#### 4.56.1. Official Package Description
Pluggable Authentication Modules library  
Contains the shared library for Linux-PAM, a library that enables the  
local system administrator to choose how applications authenticate users.  
In other words, without rewriting or recompiling a PAM-aware application,  
it is possible to switch between the authentication mechanism(s) it uses.  
One may entirely upgrade the local authentication system without touching  
the applications themselves.  

#### 4.56.2. Depended Packages
debconf  
libaudit1  
libc6  

#### 4.56.3. Configuration Files
(None)

#### 4.56.4. Executable Files
(None)

<br>

### 4.57 libpci3 Package
#### 4.57.1. Official Package Description
PCI utilities (shared library)  
This package contains the libpci shared library files.  
.  
The libpci library provides portable access to configuration  
registers of devices connected to the PCI bus.  

#### 4.57.2. Depended Packages
libc6  
libudev1  
pci.ids  
zlib1g  

#### 4.57.3. Configuration Files
(None)

#### 4.57.4. Executable Files
(None)

<br>

### 4.58 libpcre2-8-0 Package
#### 4.58.1. Official Package Description
New Perl Compatible Regular Expression Library- 8 bit runtime files  
This is PCRE2, the new implementation of PCRE, a library of functions  
to support regular expressions whose syntax and semantics are as  
close as possible to those of the Perl 5 language. New projects  
should use this library in preference to the older library,  
confusingly called pcre3 in Debian.  
.  
This package contains the 8 bit runtime library, which operates on  
ASCII and UTF-8 input.  

#### 4.58.2. Depended Packages
libc6  

#### 4.58.3. Configuration Files
(None)

#### 4.58.4. Executable Files
(None)

<br>

### 4.59 libperl5.36 Package
#### 4.59.1. Official Package Description
shared Perl library  
This package contains the shared Perl library, used by applications  
which embed a Perl interpreter.  
.  
It also contains the architecture-dependent parts of the standard  
library (and depends on perl-modules-5.36 which contains the  
architecture-independent parts).  

#### 4.59.2. Depended Packages
libbz2-1.0  
libc6  
libcrypt1  
libdb5.3  
libgdbm-compat4  
libgdbm6  
perl-modules-5.36  
zlib1g  

#### 4.59.3. Configuration Files
(None)

#### 4.59.4. Executable Files
/usr/bin/cpan5.36-x86_64-linux-gnu  
/usr/bin/perl5.36-x86_64-linux-gnu  

<br>

### 4.60 libpipeline1 Package
#### 4.60.1. Official Package Description
Unix process pipeline manipulation library  
This is a C library for setting up and running pipelines of processes,  
without needing to involve shell command-line parsing which is often  
error-prone and insecure.  

#### 4.60.2. Depended Packages
libc6  

#### 4.60.3. Configuration Files
(None)

#### 4.60.4. Executable Files
(None)

<br>

### 4.61 libpopt0 Package
#### 4.61.1. Official Package Description
lib for parsing cmdline parameters  
Popt was heavily influenced by the getopt() and getopt_long() functions,  
but it allows more powerful argument expansion. It can parse arbitrary  
argv[] style arrays and automatically set variables based on command  
line arguments. It also allows command line arguments to be aliased via  
configuration files and includes utility functions for parsing arbitrary  
strings into argv[] arrays using shell-like rules.  
.  
This package contains the runtime library and locale data.  

#### 4.61.2. Depended Packages
libc6  

#### 4.61.3. Configuration Files
(None)

#### 4.61.4. Executable Files
(None)

<br>

### 4.62 libproc2-0 Package
#### 4.62.1. Official Package Description
library for accessing process information from /proc  
The libproc2 library is a way of accessing information out of the /proc  
filesystem.  
.  
This package contains the shared libraries necessary to run programs  
compiled with libproc2.  

#### 4.62.2. Depended Packages
libc6  
libsystemd0  

#### 4.62.3. Configuration Files
(None)

#### 4.62.4. Executable Files
(None)

<br>

### 4.63 libprotobuf-c1 Package
#### 4.63.1. Official Package Description
Protocol Buffers C shared library (protobuf-c)  
Protocol Buffers are a flexible, efficient, automated mechanism for  
serializing structured data - similar to XML, but smaller, faster, and  
simpler. You define how you want your data to be structured once, then you can  
use special generated source code to easily write and read your structured  
data to and from a variety of data streams and using a variety of languages.  
You can even update your data structure without breaking deployed programs  
that are compiled against the "old" format.  
.  
This is the "protobuf-c" implementation of Protocol Buffers in C.  
.  
This package contains the shared library.  

#### 4.63.2. Depended Packages
libc6  

#### 4.63.3. Configuration Files
(None)

#### 4.63.4. Executable Files
(None)

<br>

### 4.64 libpsl5 Package
#### 4.64.1. Official Package Description
Library for Public Suffix List (shared libraries)  
Libpsl allows checking domains against the Public Suffix List.  
It can be used to avoid privacy-leaking 'super-cookies',  
'super domain' certificates, for domain highlighting purposes  
sorting domain lists by site and more.  
.  
Please see https://publicsuffix.org for more detailed information.  
.  
This package contains runtime libraries.  

#### 4.64.2. Depended Packages
libc6  
libidn2-0  
libunistring2  

#### 4.64.3. Configuration Files
(None)

#### 4.64.4. Executable Files
(None)

<br>

### 4.65 libreadline8 Package
#### 4.65.1. Official Package Description
GNU readline and history libraries, run-time libraries  
The GNU readline library aids in the consistency of user interface  
across discrete programs that need to provide a command line  
interface.  
.  
The GNU history library provides a consistent user interface for  
recalling lines of previously typed input.  

#### 4.65.2. Depended Packages
libc6  
libtinfo6  
readline-common  

#### 4.65.3. Configuration Files
(None)

#### 4.65.4. Executable Files
(None)

<br>

### 4.66 libseccomp2 Package
#### 4.66.1. Official Package Description
high level interface to Linux seccomp filter  
This library provides a high level interface to constructing, analyzing  
and installing seccomp filters via a BPF passed to the Linux Kernel's  
prctl() syscall.  

#### 4.66.2. Depended Packages
libc6  

#### 4.66.3. Configuration Files
(None)

#### 4.66.4. Executable Files
(None)

<br>

### 4.67 libselinux1 Package
#### 4.67.1. Official Package Description
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

#### 4.67.2. Depended Packages
libc6  
libpcre2-8-0  

#### 4.67.3. Configuration Files
(None)

#### 4.67.4. Executable Files
(None)

<br>

### 4.68 libsemanage2 Package
#### 4.68.1. Official Package Description
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

#### 4.68.2. Depended Packages
libaudit1  
libbz2-1.0  
libc6  
libselinux1  
libsemanage-common  
libsepol2  

#### 4.68.3. Configuration Files
(None)

#### 4.68.4. Executable Files
(None)

<br>

### 4.69 libslang2 Package
#### 4.69.1. Official Package Description
S-Lang programming library - runtime version  
S-Lang is a C programmer's library that includes routines for the rapid  
development of sophisticated, user friendly, multi-platform applications.  
.  
This package contains only the shared library libslang.so.* and copyright  
information. It is only necessary for programs that use this library (such  
as jed and slrn). If you plan on doing development with S-Lang, you will  
need the companion -dev package as well.  

#### 4.69.2. Depended Packages
libc6  

#### 4.69.3. Configuration Files
(None)

#### 4.69.4. Executable Files
(None)

<br>

### 4.70 libsmartcols1 Package
#### 4.70.1. Official Package Description
smart column output alignment library  
This smart column output alignment library is used by fdisk utilities.  

#### 4.70.2. Depended Packages
libc6  

#### 4.70.3. Configuration Files
(None)

#### 4.70.4. Executable Files
(None)

<br>

### 4.71 libss2 Package
#### 4.71.1. Official Package Description
command-line interface parsing library  
libss provides a simple command-line interface parser which will  
accept input from the user, parse the command into an argv argument  
vector, and then dispatch it to a handler function.  
.  
It was originally inspired by the Multics SubSystem library.  

#### 4.71.2. Depended Packages
libc6  
libcom-err2  

#### 4.71.3. Configuration Files
(None)

#### 4.71.4. Executable Files
(None)

<br>

### 4.72 libssl3 Package
#### 4.72.1. Official Package Description
Secure Sockets Layer toolkit - shared libraries  
This package is part of the OpenSSL project's implementation of the SSL  
and TLS cryptographic protocols for secure communication over the  
Internet.  
.  
It provides the libssl and libcrypto shared libraries.  

#### 4.72.2. Depended Packages
libc6  

#### 4.72.3. Configuration Files
(None)

#### 4.72.4. Executable Files
(None)

<br>

### 4.73 libstdc++6 Package
#### 4.73.1. Official Package Description
GNU Standard C++ Library v3  
This package contains an additional runtime library for C++ programs  
built with the GNU compiler.  
.  
libstdc++-v3 is a complete rewrite from the previous libstdc++-v2, which  
was included up to g++-2.95. The first version of libstdc++-v3 appeared  
in g++-3.0.  

#### 4.73.2. Depended Packages
gcc-12-base  
libc6  
libgcc-s1  

#### 4.73.3. Configuration Files
(None)

#### 4.73.4. Executable Files
(None)

<br>

### 4.74 libsystemd-shared Package
#### 4.74.1. Official Package Description
systemd shared private library  
This internal shared library provides common code used by various systemd  
components. It is supposed to decrease memory and disk footprint.  
The shared library is not meant for public use and is not API or ABI stable.  

#### 4.74.2. Depended Packages
libacl1  
libapparmor1  
libaudit1  
libblkid1  
libc6  
libcap2  
libcrypt1  
libgcrypt20  
libip4tc2  
libkmod2  
liblz4-1  
liblzma5  
libmount1  
libpam0g  
libseccomp2  
libselinux1  
libssl3  
libzstd1  

#### 4.74.3. Configuration Files
(None)

#### 4.74.4. Executable Files
(None)

<br>

### 4.75 libsystemd0 Package
#### 4.75.1. Official Package Description
systemd utility library  
This library provides APIs to interface with various system components such as  
the system journal, the system service manager, D-Bus and more.  

#### 4.75.2. Depended Packages
libc6  
libcap2  
libgcrypt20  
liblz4-1  
liblzma5  
libzstd1  

#### 4.75.3. Configuration Files
(None)

#### 4.75.4. Executable Files
(None)

<br>

### 4.76 libtext-charwidth-perl Package
#### 4.76.1. Official Package Description
get display widths of characters on the terminal  
Text::CharWidth permits one to get the display widths of characters  
and strings on the terminal, using wcwidth() and wcswidth() from libc.  
.  
It provides mbwidth(), mbswidth(), and mblen().  

#### 4.76.2. Depended Packages
libc6  
perl-base  
perlapi-5.36.0  

#### 4.76.3. Configuration Files
(None)

#### 4.76.4. Executable Files
(None)

<br>

### 4.77 libtext-iconv-perl Package
#### 4.77.1. Official Package Description
module to convert between character sets in Perl  
The iconv() family of functions from XPG4 defines an API for converting  
between character sets (e.g. UTF-8 to Latin1, EBCDIC to ASCII). They  
are provided by libc6.  
.  
This package allows access to them from Perl via the Text::Iconv  
package.  

#### 4.77.2. Depended Packages
libc6  
perl-base  
perlapi-5.36.0  

#### 4.77.3. Configuration Files
(None)

#### 4.77.4. Executable Files
(None)

<br>

### 4.78 libtext-wrapi18n-perl Package
#### 4.78.1. Official Package Description
internationalized substitute of Text::Wrap  
The Text::WrapI18N module is a substitution for Text::Wrap, supporting  
multibyte characters such as UTF-8, EUC-JP, and GB2312, fullwidth characters  
such as east Asian characters, combining characters such as diacritical marks  
and Thai, and languages which don't use whitespaces between words such as  
Chinese and Japanese.  
.  
It provides wrap().  

#### 4.78.2. Depended Packages
libtext-charwidth-perl  

#### 4.78.3. Configuration Files
(None)

#### 4.78.4. Executable Files
(None)

<br>

### 4.79 libtinfo6 Package
#### 4.79.1. Official Package Description
shared low-level terminfo library for terminal handling  
The ncurses library routines are a terminal-independent method of  
updating character screens with reasonable optimization.  
.  
This package contains the shared low-level terminfo library.  

#### 4.79.2. Depended Packages
libc6  

#### 4.79.3. Configuration Files
(None)

#### 4.79.4. Executable Files
(None)

<br>

### 4.80 libtirpc3 Package
#### 4.80.1. Official Package Description
transport-independent RPC library  
This package contains a port of Sun's transport-independent RPC library to  
Linux. The library is intended as a replacement for the RPC code in the GNU C  
library, providing among others support for RPC (and in turn, NFS) over IPv6.  

#### 4.80.2. Depended Packages
libc6  
libgssapi-krb5-2  
libtirpc-common  

#### 4.80.3. Configuration Files
(None)

#### 4.80.4. Executable Files
(None)

<br>

### 4.81 libuchardet0 Package
#### 4.81.1. Official Package Description
universal charset detection library - shared library  
uchardet is a C language binding of the original C++ implementation  
of the universal charset detection library by Mozilla.  
.  
uchardet is a encoding detector library, which takes a sequence of  
bytes in an unknown character encoding without any additional  
information, and attempts to determine the encoding of the text.  
.  
This package contains the shared library.  

#### 4.81.2. Depended Packages
libc6  
libgcc-s1  
libstdc++6  

#### 4.81.3. Configuration Files
(None)

#### 4.81.4. Executable Files
(None)

<br>

### 4.82 libudev1 Package
#### 4.82.1. Official Package Description
libudev shared library  
This library provides APIs to introspect and enumerate devices on the local  
system.  

#### 4.82.2. Depended Packages
libc6  

#### 4.82.3. Configuration Files
(None)

#### 4.82.4. Executable Files
(None)

<br>

### 4.83 libuuid1 Package
#### 4.83.1. Official Package Description
Universally Unique ID library  
The libuuid library generates and parses 128-bit Universally Unique  
IDs (UUIDs). A UUID is an identifier that is unique within the space  
of all such identifiers across both space and time. It can be used for  
multiple purposes, from tagging objects with an extremely short lifetime  
to reliably identifying very persistent objects across a network.  
.  
See RFC 4122 for more information.  

#### 4.83.2. Depended Packages
libc6  

#### 4.83.3. Configuration Files
(None)

#### 4.83.4. Executable Files
(None)

<br>

### 4.84 libxtables12 Package
#### 4.84.1. Official Package Description
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

#### 4.84.2. Depended Packages
libc6  

#### 4.84.3. Configuration Files
(None)

#### 4.84.4. Executable Files
(None)

<br>

### 4.85 libzstd1 Package
#### 4.85.1. Official Package Description
fast lossless compression algorithm  
Zstd, short for Zstandard, is a fast lossless compression algorithm, targeting  
real-time compression scenarios at zlib-level compression ratio.  
.  
This package contains the shared library.  

#### 4.85.2. Depended Packages
libc6  

#### 4.85.3. Configuration Files
(None)

#### 4.85.4. Executable Files
(None)

<br>

### 4.86 logsave Package
#### 4.86.1. Official Package Description
save the output of a command in a log file  
The logsave program will execute cmd_prog with the specified  
argument(s), and save a copy of its output to logfile.  If the  
containing directory for logfile does not exist, logsave will  
accumulate the output in memory until it can be written out.  A copy  
of the output will also be written to standard output.  

#### 4.86.2. Depended Packages
libc6  

#### 4.86.3. Configuration Files
(None)

#### 4.86.4. Executable Files
/sbin/logsave  

<br>

### 4.87 mailcap Package
#### 4.87.1. Official Package Description
Debians mailcap system, and support programs  
The mailcap system associates media types with programs that can handle them,  
using system and user configuration files.  A files media type is determined  
by its extension or by running the "file" command if available.  
.  
Other packages register their programs as viewers/editors/composers/etc by  
placing mailcap entry files or FreeDesktop menu entries in predetermined  
directories monitored by this packages dpkg triggers.  
.  
This package provides a "run-mailcap" program to open arbitrary files, and in  
addition the "see", "edit", "compose", and "print" aliases to display, alter,  
create, and print (respectively).  
.  
This package also provides the "debian-view" utility to handle Debian packages  
interactively.  

#### 4.87.2. Depended Packages
media-types  
perl  

#### 4.87.3. Configuration Files
/etc/mailcap.order  

#### 4.87.4. Executable Files
/usr/bin/compose  
/usr/bin/edit  
/usr/bin/print  
/usr/bin/run-mailcap  
/usr/bin/see  
/usr/sbin/update-mime  

<br>

### 4.88 openssl Package
#### 4.88.1. Official Package Description
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

#### 4.88.2. Depended Packages
libc6  
libssl3  

#### 4.88.3. Configuration Files
/etc/ssl/openssl.cnf  

#### 4.88.4. Executable Files
/usr/bin/c_rehash  
/usr/bin/openssl  

<br>

### 4.89 perl-modules-5.36 Package
#### 4.89.1. Official Package Description
Core Perl modules  
Architecture independent Perl modules.  These modules are part of Perl and  
required if the perl' package is installed.  
.  
Note that this package only exists to save archive space and should be  
considered an internal implementation detail of the perl' package.  
Other packages should not depend on perl-modules-5.36' directly, they  
should use perl' (which depends on perl-modules-5.36') instead.  

#### 4.89.2. Depended Packages
dpkg  
perl-base  

#### 4.89.3. Configuration Files
(None)

#### 4.89.4. Executable Files
(None)

<br>

### 4.90 python3 Package
#### 4.90.1. Official Package Description
interactive high-level object-oriented language (default python3 version)  
Python, the high-level, interactive object oriented language,  
includes an extensive class library with lots of goodies for  
network programming, system administration, sounds and graphics.  
.  
This package is a dependency package, which depends on Debian's default  
Python 3 version (currently v3.11).  

#### 4.90.2. Depended Packages
libpython3-stdlib  
python3-minimal  
python3.11  

#### 4.90.3. Configuration Files
(None)

#### 4.90.4. Executable Files
/usr/bin/pdb3  
/usr/bin/pydoc3  
/usr/bin/pygettext3  

<br>

### 4.91 python3-apt Package
#### 4.91.1. Official Package Description
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

#### 4.91.2. Depended Packages
distro-info-data  
libapt-pkg6.0  
libc6  
libgcc-s1  
libstdc++6  
python-apt-common  
python3  
python3:any  

#### 4.91.3. Configuration Files
(None)

#### 4.91.4. Executable Files
(None)

<br>

### 4.92 python3-debconf Package
#### 4.92.1. Official Package Description
interact with debconf from Python 3  
Debconf is a configuration management system for debian packages. Packages  
use Debconf to ask questions when they are installed.  
.  
This package provides a debconf module to allow Python 3 programs to  
interact with a debconf frontend.  

#### 4.92.2. Depended Packages
debconf  
python3:any  

#### 4.92.3. Configuration Files
(None)

#### 4.92.4. Executable Files
(None)

<br>

### 4.93 python3-debian Package
#### 4.93.1. Official Package Description
Python 3 modules to work with Debian-related data formats  
This package provides Python 3 modules that abstract many formats of Debian  
related files. Currently handled are:  
Debtags information (debian.debtags module)  
debian/changelog (debian.changelog module)  
Packages files, pdiffs (debian.debian_support module)  
Control files of single or multiple RFC822-style paragraphs, e.g.  
debian/control, .changes, .dsc, Packages, Sources, Release, etc.  
(debian.deb822 module)  
Raw .deb and .ar files, with (read-only) access to contained  
files and meta-information  

#### 4.93.2. Depended Packages
python3-chardet  
python3:any  

#### 4.93.3. Configuration Files
(None)

#### 4.93.4. Executable Files
(None)

<br>

### 4.94 python3-debianbts Package
#### 4.94.1. Official Package Description
Python interface to Debian's Bug Tracking System  
This package provides the debianbts module, which allows one to query Debian's  
BTS via it's SOAP-interface and returns the answer in Python's native data  
types.  

#### 4.94.2. Depended Packages
python3-pysimplesoap  
python3:any  

#### 4.94.3. Configuration Files
(None)

#### 4.94.4. Executable Files
/usr/bin/debianbts  

<br>

### 4.95 python3-requests Package
#### 4.95.1. Official Package Description
elegant and simple HTTP library for Python3, built for human beings  
Requests allow you to send HTTP/1.1 requests. You can add headers, form data,  
multipart files, and parameters with simple Python dictionaries, and access  
the response data in the same way. It's powered by httplib and urllib3, but  
it does all the hard work and crazy hacks for you.  
.  
Features  
.  
International Domains and URLs  
Keep-Alive & Connection Pooling  
Sessions with Cookie Persistence  
Browser-style SSL Verification  
Basic/Digest Authentication  
Elegant Key/Value Cookies  
Automatic Decompression  
Unicode Response Bodies  
Multipart File Uploads  
Connection Timeouts  
.  
This package contains the Python 3 version of the library.  

#### 4.95.2. Depended Packages
ca-certificates  
python3-certifi  
python3-chardet  
python3-charset-normalizer  
python3-idna  
python3-urllib3  
python3:any  

#### 4.95.3. Configuration Files
(None)

#### 4.95.4. Executable Files
(None)

<br>

### 4.96 tasksel Package
#### 4.96.1. Official Package Description
tool for selecting tasks for installation on Debian systems  
This package provides 'tasksel', a simple interface for users who  
want to configure their system to perform a specific task.  

#### 4.96.2. Depended Packages
apt  
debconf  
liblocale-gettext-perl  
tasksel-data  

#### 4.96.3. Configuration Files
(None)

#### 4.96.4. Executable Files
/usr/bin/tasksel  

<br>

### 4.97 usrmerge Package
#### 4.97.1. Official Package Description
Convert the system to the merged /usr directories scheme  
This package will automatically convert the system to the merged  
/usr directory scheme, in which the /{bin,sbin,lib}/ directories are  
symlinked to their counterparts in /usr/.  
.  
There is no automatic method to restore the precedent configuration, so  
there is no going back once this package has been installed.  

#### 4.97.2. Depended Packages
libfile-find-rule-perl  
perl:any  

#### 4.97.3. Configuration Files
(None)

#### 4.97.4. Executable Files
(None)

<br>

### 4.98 zlib1g Package
#### 4.98.1. Official Package Description
compression library - runtime  
zlib is a library implementing the deflate compression method found  
in gzip and PKZIP.  This package includes the shared library.  

#### 4.98.2. Depended Packages
libc6  

#### 4.98.3. Configuration Files
(None)

#### 4.98.4. Executable Files
(None)

<br>

## 5. Extra Necessary Packages
---
There is no classification as extra necessary packages. These are the packages that are not classified as required, important, standard, or necessary; but some of the necessary packages are depended on these packages. 

So you may expect these packages in Debian installations too.

Some packages listed here are virtual packages. 

Virtual packages are placeholders that represent a group of packages with  similar functionality. These virtual packages allow users to install any  package that provides the functionality specified by the virtual package name. They are particularly useful for creating dependencies between packages without tying them to specific implementations.

I mark the following packages are marked as extra-necessary:

**dbus-session-bus-common:** simple interprocess messaging system (session bus configuration)  
**distro-info-data:** information about the distributions' releases (data files)  
**gcc-12-base:** GCC, the GNU Compiler Collection (base package)  
**libapparmor1:** changehat AppArmor library  
**libargon2-1:** memory-hard hashing function - runtime library  
**libaudit-common:** Dynamic library for security auditing - common files  
**libcbor0.8:** library for parsing and generating CBOR (RFC 7049)  
**libdevmapper1.02.1:** Linux Kernel Device Mapper userspace library  
**libffi8:** Foreign Function Interface library runtime  
**libfile-find-rule-perl:** module to search for files based on rules  
**libfstrm0:** Frame Streams (fstrm) library  
**libgdbm-compat4:** GNU dbm database routines (legacy support runtime version)  
**libhogweed6:** low level cryptographic library (public-key cryptos)  
**libip4tc2:** netfilter libip4tc library  
**libjansson4:** C library for encoding, decoding and manipulating JSON data  
**libjemalloc2:** general-purpose scalable concurrent malloc(3) implementation  
**libjson-c5:** JSON manipulation library - shared library  
**libkeyutils1:** Linux Key Management Utilities (library)  
**libkrb5support0:** MIT Kerberos runtime libraries - Support library  
**liblmdb0:** Lightning Memory-Mapped Database shared library  
**libmagic-mgc:** File type determination library using "magic" numbers (compiled magic file)  
**libmaxminddb0:** IP geolocation database library  
**libnftnl11:** Netfilter nftables userspace API library  
**libnghttp2-14:** library implementing HTTP/2 protocol (shared library)  
**libpython3-stdlib:** interactive high-level object-oriented language (default python3 version)  
**libsemanage-common:** Common files for SELinux policy management libraries  
**libsepol2:** SELinux library for manipulating binary security policies  
**libtasn1-6:** Manage ASN.1 structures (runtime)  
**libtirpc-common:** transport-independent RPC library - common files  
**libunistring2:** Unicode string library for C  
**libuv1:** asynchronous event notification library - runtime library  
**libxml2:** GNOME XML library  
**libxxhash0:** shared library for xxhash  
**pci.ids:** PCI ID Repository  
**perlapi-5.36.0:** Virtual package provided by perl-base  
**python-apt-common:** Python interface to libapt-pkg (locales)  
**python3-certifi:** root certificates for validating SSL certs and verifying TLS hosts (python3)  
**python3-chardet:** Universal Character Encoding Detector (Python3)  
**python3-charset-normalizer:** charset, encoding and language detection (Python 3)  
**python3-idna:** Python IDNA2008 (RFC 5891) handling (Python 3)  
**python3-minimal:** minimal subset of the Python language (default python3 version)  
**python3-pysimplesoap:** simple and lightweight SOAP Library (Python 3)  
**python3-urllib3:** HTTP library with thread-safe connection pooling for Python3  
**python3.11:** Interactive high-level object-oriented language (version 3.11)  

<br>

### 5.1 dbus-session-bus-common Package
#### 5.1.1. Official Package Description
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

#### 5.1.2. Depended Packages
(None)

#### 5.1.3. Configuration Files
(None)

#### 5.1.4. Executable Files
(None)

<br>

### 5.2 distro-info-data Package
#### 5.2.1. Official Package Description
information about the distributions' releases (data files)  
Information about all releases of Debian and Ubuntu. The distro-info script  
will give you the codename for e.g. the latest stable release of your  
distribution. To get information about a specific distribution there are the  
debian-distro-info and the ubuntu-distro-info scripts.  
.  
This package contains the data files.  

#### 5.2.2. Depended Packages
(None)

#### 5.2.3. Configuration Files
(None)

#### 5.2.4. Executable Files
(None)

<br>

### 5.3 gcc-12-base Package
#### 5.3.1. Official Package Description
GCC, the GNU Compiler Collection (base package)  
This package contains files common to all languages and libraries  
contained in the GNU Compiler Collection (GCC).  

#### 5.3.2. Depended Packages
(None)

#### 5.3.3. Configuration Files
(None)

#### 5.3.4. Executable Files
(None)

<br>

### 5.4 libapparmor1 Package
#### 5.4.1. Official Package Description
changehat AppArmor library  
libapparmor1 provides a shared library one can compile programs  
against in order to use various AppArmor functionality,  
such as transitioning to a different AppArmor profile or hat.  

#### 5.4.2. Depended Packages
libc6  

#### 5.4.3. Configuration Files
(None)

#### 5.4.4. Executable Files
(None)

<br>

### 5.5 libargon2-1 Package
#### 5.5.1. Official Package Description
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

#### 5.5.2. Depended Packages
libc6  

#### 5.5.3. Configuration Files
(None)

#### 5.5.4. Executable Files
(None)

<br>

### 5.6 libaudit-common Package
#### 5.6.1. Official Package Description
Dynamic library for security auditing - common files  
The audit-libs package contains the dynamic libraries needed for  
applications to use the audit framework. It is used to monitor systems for  
security related events.  
.  
This package contains the libaudit.conf configuration file and the associated  
manpage.  

#### 5.6.2. Depended Packages
(None)

#### 5.6.3. Configuration Files
/etc/libaudit.conf  

#### 5.6.4. Executable Files
(None)

<br>

### 5.7 libcbor0.8 Package
#### 5.7.1. Official Package Description
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

#### 5.7.2. Depended Packages
libc6  

#### 5.7.3. Configuration Files
(None)

#### 5.7.4. Executable Files
(None)

<br>

### 5.8 libdevmapper1.02.1 Package
#### 5.8.1. Official Package Description
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

#### 5.8.2. Depended Packages
dmsetup  
libc6  
libselinux1  
libudev1  

#### 5.8.3. Configuration Files
(None)

#### 5.8.4. Executable Files
(None)

<br>

### 5.9 libffi8 Package
#### 5.9.1. Official Package Description
Foreign Function Interface library runtime  
A foreign function interface is the popular name for the interface that  
allows code written in one language to call code written in another  
language.  

#### 5.9.2. Depended Packages
libc6  

#### 5.9.3. Configuration Files
(None)

#### 5.9.4. Executable Files
(None)

<br>

### 5.10 libfile-find-rule-perl Package
#### 5.10.1. Official Package Description
module to search for files based on rules  
File::Find::Rule is a Perl module which essentially provides an easy-to-use  
interface to the popular module, File::Find. It provides a way to build rules  
that specify desired file and directory names using a text-globbing syntax  
(provided by Text::Glob). This makes it useful for simple tasks, like finding  
all ".pm" files in a given directory.  

#### 5.10.2. Depended Packages
libnumber-compare-perl  
libtext-glob-perl  
perl:any  

#### 5.10.3. Configuration Files
(None)

#### 5.10.4. Executable Files
/usr/bin/findrule  

<br>

### 5.11 libfstrm0 Package
#### 5.11.1. Official Package Description
Frame Streams (fstrm) library  
Frame Streams is a light weight, binary clean protocol that allows for the  
transport of arbitrarily encoded data payload sequences with minimal framing  
overhead -- just four bytes per data frame. Frame Streams does not specify an  
encoding format for data frames and can be used with any data serialization  
format that produces byte sequences, such as Protocol Buffers, XML, JSON,  
MessagePack, YAML, etc. Frame Streams can be used as both a streaming  
transport over a reliable byte stream socket (TCP sockets, TLS connections,  
AF_UNIX sockets, etc.) for data in motion as well as a file format for data  
at rest. A "Content Type" header identifies the type of payload being carried  
over an individual Frame Stream and allows cooperating programs to determine  
how to interpret a given sequence of data payloads.  
.  
This is the "fstrm" implementation of Frame Streams in C.  
.  
This package contains the shared library.  

#### 5.11.2. Depended Packages
libc6  

#### 5.11.3. Configuration Files
(None)

#### 5.11.4. Executable Files
(None)

<br>

### 5.12 libgdbm-compat4 Package
#### 5.12.1. Official Package Description
GNU dbm database routines (legacy support runtime version)  
GNU dbm ('gdbm') is a library of database functions that use extendible  
hashing and works similarly to the standard UNIX 'dbm' functions.  
.  
The basic use of 'gdbm' is to store key/data pairs in a data file, thus  
providing a persistent version of the 'dictionary' Abstract Data Type  
('hash' to perl programmers).  
This package includes library files, required to run old programs,  
that use legacy 'dbm' interface. For new programs, please use modern  
interface, provided by libgdbm6 and libgdbm-dev.  

#### 5.12.2. Depended Packages
libc6  
libgdbm6  

#### 5.12.3. Configuration Files
(None)

#### 5.12.4. Executable Files
(None)

<br>

### 5.13 libhogweed6 Package
#### 5.13.1. Official Package Description
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

#### 5.13.2. Depended Packages
libc6  
libgmp10  
libnettle8  

#### 5.13.3. Configuration Files
(None)

#### 5.13.4. Executable Files
(None)

<br>

### 5.14 libip4tc2 Package
#### 5.14.1. Official Package Description
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

#### 5.14.2. Depended Packages
libc6  

#### 5.14.3. Configuration Files
(None)

#### 5.14.4. Executable Files
(None)

<br>

### 5.15 libjansson4 Package
#### 5.15.1. Official Package Description
C library for encoding, decoding and manipulating JSON data  
Jansson is a C library for encoding, decoding and manipulating JSON data.  
.  
It features:  
Simple and intuitive API and data model  
Comprehensive documentation  
No dependencies on other libraries  
Full Unicode support (UTF-8)  
Extensive test suite  

#### 5.15.2. Depended Packages
libc6  

#### 5.15.3. Configuration Files
(None)

#### 5.15.4. Executable Files
(None)

<br>

### 5.16 libjemalloc2 Package
#### 5.16.1. Official Package Description
general-purpose scalable concurrent malloc(3) implementation  
A library providing a malloc(3) implementation for multi-threaded processes on  
multi-processor systems.  
.  
Notable features are reduced lock contention, predictable low fragmentation,  
and introspection with heap profiling.  

#### 5.16.2. Depended Packages
libc6  
libgcc-s1  
libstdc++6  

#### 5.16.3. Configuration Files
(None)

#### 5.16.4. Executable Files
(None)

<br>

### 5.17 libjson-c5 Package
#### 5.17.1. Official Package Description
JSON manipulation library - shared library  
This library allows you to easily construct JSON objects in C,  
output them as JSON formatted strings and parse JSON formatted  
strings back into the C representation of JSON objects.  

#### 5.17.2. Depended Packages
libc6  

#### 5.17.3. Configuration Files
(None)

#### 5.17.4. Executable Files
(None)

<br>

### 5.18 libkeyutils1 Package
#### 5.18.1. Official Package Description
Linux Key Management Utilities (library)  
Keyutils is a set of utilities for managing the key retention facility in the  
kernel, which can be used by filesystems, block devices and more to gain and  
retain the authorization and encryption keys required to perform secure  
operations.  
.  
This package provides a wrapper library for the key management facility system  
calls.  

#### 5.18.2. Depended Packages
libc6  

#### 5.18.3. Configuration Files
(None)

#### 5.18.4. Executable Files
(None)

<br>

### 5.19 libkrb5support0 Package
#### 5.19.1. Official Package Description
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

#### 5.19.2. Depended Packages
libc6  

#### 5.19.3. Configuration Files
(None)

#### 5.19.4. Executable Files
(None)

<br>

### 5.20 liblmdb0 Package
#### 5.20.1. Official Package Description
Lightning Memory-Mapped Database shared library  
This package contains the LMDB shared library.  
.  
Lighting Memory-Mapped Database (LMDB) is an ultra-fast, ultra-compact  
key-value embedded data store developed for the OpenLDAP Project.  It uses  
memory-mapped files, so it has the read performance of a pure in-memory  
database while still offering the persistence of standard disk-based  
databases, and is only limited to the size of the virtual address space, (it  
is not limited to the size of physical RAM).  

#### 5.20.2. Depended Packages
libc6  

#### 5.20.3. Configuration Files
(None)

#### 5.20.4. Executable Files
(None)

<br>

### 5.21 libmagic-mgc Package
#### 5.21.1. Official Package Description
File type determination library using "magic" numbers (compiled magic file)  
This package provides the compiled magic file "magic.mgc". It has  
been separated from libmagic1 in order to meet the multiarch  
requirements without breaking applications that expect this file  
at its absolute path.  

#### 5.21.2. Depended Packages
(None)

#### 5.21.3. Configuration Files
(None)

#### 5.21.4. Executable Files
(None)

<br>

### 5.22 libmaxminddb0 Package
#### 5.22.1. Official Package Description
IP geolocation database library  
The libmaxminddb library provides a C library for reading MaxMind DB files,  
including the GeoIP2 databases from MaxMind. This is a custom binary format  
designed to facilitate fast lookups of IP addresses while allowing for great  
flexibility in the type of data associated with an address.  
.  
The MaxMind DB format is an open format. The spec is available at  
http://maxmind.github.io/MaxMind-DB/. This spec is licensed under the Creative  
Commons Attribution-ShareAlike 3.0 Unported License.  

#### 5.22.2. Depended Packages
libc6  

#### 5.22.3. Configuration Files
(None)

#### 5.22.4. Executable Files
(None)

<br>

### 5.23 libnftnl11 Package
#### 5.23.1. Official Package Description
Netfilter nftables userspace API library  
libnftnl is the low-level library for Netfilter 4th generation  
framework nftables.  
.  
Is the user-space library for low-level interaction with  
nftables Netlink's API over libmnl.  

#### 5.23.2. Depended Packages
libc6  
libmnl0  

#### 5.23.3. Configuration Files
(None)

#### 5.23.4. Executable Files
(None)

<br>

### 5.24 libnghttp2-14 Package
#### 5.24.1. Official Package Description
library implementing HTTP/2 protocol (shared library)  
This is an implementation of the Hypertext Transfer Protocol version  
2 in C. The framing layer of HTTP/2 is implemented as a reusable C  
library.  
.  
This package installs a shared library.  

#### 5.24.2. Depended Packages
libc6  

#### 5.24.3. Configuration Files
(None)

#### 5.24.4. Executable Files
(None)

<br>

### 5.25 libpython3-stdlib Package
#### 5.25.1. Official Package Description
interactive high-level object-oriented language (default python3 version)  
This package contains the majority of the standard library for the Python  
language (default python3 version).  
.  
This package is a dependency package, which depends on Debian's default  
Python 3 version's standard library (currently v3.11).  

#### 5.25.2. Depended Packages
libpython3.11-stdlib  

#### 5.25.3. Configuration Files
(None)

#### 5.25.4. Executable Files
(None)

<br>

### 5.26 libsemanage-common Package
#### 5.26.1. Official Package Description
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

#### 5.26.2. Depended Packages
(None)

#### 5.26.3. Configuration Files
/etc/selinux/semanage.conf  

#### 5.26.4. Executable Files
(None)

<br>

### 5.27 libsepol2 Package
#### 5.27.1. Official Package Description
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

#### 5.27.2. Depended Packages
libc6  

#### 5.27.3. Configuration Files
(None)

#### 5.27.4. Executable Files
(None)

<br>

### 5.28 libtasn1-6 Package
#### 5.28.1. Official Package Description
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

#### 5.28.2. Depended Packages
libc6  

#### 5.28.3. Configuration Files
(None)

#### 5.28.4. Executable Files
(None)

<br>

### 5.29 libtirpc-common Package
#### 5.29.1. Official Package Description
transport-independent RPC library - common files  
This package contains a port of Sun's transport-independent RPC library to  
Linux. The library is intended as a replacement for the RPC code in the GNU C  
library, providing among others support for RPC (and in turn, NFS) over IPv6.  
.  
This package contains the netconfig configuration file as well as the  
associated manpage.  

#### 5.29.2. Depended Packages
(None)

#### 5.29.3. Configuration Files
/etc/netconfig  

#### 5.29.4. Executable Files
(None)

<br>

### 5.30 libunistring2 Package
#### 5.30.1. Official Package Description
Unicode string library for C  
The 'libunistring' library implements Unicode strings (in the UTF-8,  
UTF-16, and UTF-32 encodings), together with functions for Unicode  
characters (character names, classifications, properties) and  
functions for string processing (formatted output, width, word  
breaks, line breaks, normalization, case folding, regular  
expressions).  
.  
This package contains the shared library.  

#### 5.30.2. Depended Packages
libc6  

#### 5.30.3. Configuration Files
(None)

#### 5.30.4. Executable Files
(None)

<br>

### 5.31 libuv1 Package
#### 5.31.1. Official Package Description
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

#### 5.31.2. Depended Packages
libc6  

#### 5.31.3. Configuration Files
(None)

#### 5.31.4. Executable Files
(None)

<br>

### 5.32 libxml2 Package
#### 5.32.1. Official Package Description
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

#### 5.32.2. Depended Packages
libc6  
libicu72  
liblzma5  
zlib1g  

#### 5.32.3. Configuration Files
(None)

#### 5.32.4. Executable Files
(None)

<br>

### 5.33 libxxhash0 Package
#### 5.33.1. Official Package Description
shared library for xxhash  
xxHash is an Extremely fast Hash algorithm, running at RAM speed limits.  
It successfully completes the SMHasher test suite which evaluates collision,  
dispersion and randomness qualities of hash functions. Code is highly portable,  
and hashes are identical on all platforms (little / big endian).  
.  
This package contains the shared library.  

#### 5.33.2. Depended Packages
libc6  

#### 5.33.3. Configuration Files
(None)

#### 5.33.4. Executable Files
(None)

<br>

### 5.34 pci.ids Package
#### 5.34.1. Official Package Description
PCI ID Repository  
This package contains the pci.ids file, a public repository of all known  
ID's used in PCI devices: ID's of vendors, devices, subsystems and device  
classes. It is used in various programs to display full human-readable  
names instead of cryptic numeric codes.  

#### 5.34.2. Depended Packages
(None)

#### 5.34.3. Configuration Files
(None)

#### 5.34.4. Executable Files
(None)

<br>

### 5.35 perlapi-5.36.0 Package
perlapi-5.36.0 is a virtual package provided by perl-base. If we install perl-base, this package will be seen as installed too. 

As perl-base being a required package and was documented at 1.28. we may consider this package as documented too.

<br>

### 5.36 python-apt-common Package
#### 5.36.1. Official Package Description
Python interface to libapt-pkg (locales)  
The apt_pkg Python interface will provide full access to the internal  
libapt-pkg structures allowing Python programs to easily perform a  
variety of functions.  
.  
This package contains locales.  

#### 5.36.2. Depended Packages
(None)

#### 5.36.3. Configuration Files
(None)

#### 5.36.4. Executable Files
(None)

<br>

### 5.37 python3-certifi Package
#### 5.37.1. Official Package Description
root certificates for validating SSL certs and verifying TLS hosts (python3)  
Certifi is a carefully curated collection of Root Certificates for  
validating the trustworthiness of SSL certificates while verifying  
the identity of TLS hosts. It has been extracted from the Requests  
project.  
.  
The version of certifi in this Debian package is patched to return  
the location of Debian-provided CA certificates, instead of those  
packaged by upstream.  
.  
This is the python3 package.  

#### 5.37.2. Depended Packages
ca-certificates  
python3:any  

#### 5.37.3. Configuration Files
(None)

#### 5.37.4. Executable Files
(None)

<br>

### 5.38 python3-chardet Package
#### 5.38.1. Official Package Description
Universal Character Encoding Detector (Python3)  
Chardet is a continuation of Mark Pilgrim's excellent original chardet port  
from C, and Ian Cordasco's charade Python 3-compatible fork.  
Chardet takes a sequence of bytes in an unknown character encoding, and  
attempts to determine the encoding.  
.  
Supported encodings:  
Big5, GB2312/GB18030, EUC-TW, HZ-GB-2312, and ISO-2022-CN (Traditional  
and Simplified Chinese)  
EUC-JP, SHIFT_JIS, and ISO-2022-JP (Japanese)  
EUC-KR and ISO-2022-KR (Korean)  
KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, and windows-1251 (Russian)  
ISO-8859-2 and windows-1250 (Hungarian)  
ISO-8859-5 and windows-1251 (Bulgarian)  
ISO-8859-1 and windows-1252 (Western European languages)  
ISO-8859-7 and windows-1253 (Greek)  
ISO-8859-8 and windows-1255 (Visual and Logical Hebrew)  
TIS-620 (Thai)  
UTF-32 BE, LE, 3412-ordered, or 2143-ordered (with a BOM)  
UTF-16 BE or LE (with a BOM)  
UTF-8 (with or without a BOM)  
ASCII  
.  
This library is a port of the auto-detection code in Mozilla.  
.  
This package contains the Python 3 version of the library.  

#### 5.38.2. Depended Packages
python3-pkg-resources  
python3:any  

#### 5.38.3. Configuration Files
(None)

#### 5.38.4. Executable Files
/usr/bin/chardet  
/usr/bin/chardetect  

<br>

### 5.39 python3-charset-normalizer Package
#### 5.39.1. Official Package Description
charset, encoding and language detection (Python 3)  
charset-normalizer is a library for detection of charsets, encodings,  
and languages in Python programs. It can be compared to chardet, with  
a different approach, which intends to make it faster and more reliable.  
charset-normalizer can also detect natural languages.  
.  
All IANA character set names for which the Python core library provides  
codecs are supported.  
.  
This package installs the library for Python 3.  

#### 5.39.2. Depended Packages
python3:any  

#### 5.39.3. Configuration Files
(None)

#### 5.39.4. Executable Files
/usr/bin/normalizer  

<br>

### 5.40 python3-idna Package
#### 5.40.1. Official Package Description
Python IDNA2008 (RFC 5891) handling (Python 3)  
A library to support the Internationalised Domain Names in Applications (IDNA)  
protocol as specified in RFC 5891. This version of the protocol is often  
referred to as \xe2\x80\x9cIDNA2008\xe2\x80\x9d and can produce different results from the earlier  
standard from 2003.  
.  
The library is also intended to act as a suitable drop-in replacement for the  
\xe2\x80\x9cencodings.idna\xe2\x80\x9d module that comes with the Python standard library but  
currently only supports the older 2003 specification.  
.  
This package contains the module for Python 3.  

#### 5.40.2. Depended Packages
python3:any  

#### 5.40.3. Configuration Files
(None)

#### 5.40.4. Executable Files
(None)

<br>

### 5.41 python3-minimal Package
#### 5.41.1. Official Package Description
minimal subset of the Python language (default python3 version)  
This package contains the interpreter and some essential modules.  It's used  
in the boot process for some basic tasks.  
See /usr/share/doc/python3.11-minimal/README.Debian for a list of the modules  
contained in this package.  

#### 5.41.2. Depended Packages
dpkg  
python3.11-minimal  

#### 5.41.3. Configuration Files
(None)

#### 5.41.4. Executable Files
/usr/bin/py3clean  
/usr/bin/py3compile  
/usr/bin/py3versions  
/usr/bin/python3  

<br>

### 5.42 python3-pysimplesoap Package
#### 5.42.1. Official Package Description
simple and lightweight SOAP Library (Python 3)  
Python simple and lightweight SOAP library for client and server webservices  
interfaces, aimed to be as small and easy as possible, supporting most common  
functionality. Initially it was inspired by PHP Soap Extension (mimicking its  
functionality, simplicity and ease of use), with many advanced features added.  
.  
This package contains the Python 3 version of pysimplesoap .  

#### 5.42.2. Depended Packages
python3-httplib2  
python3-pycurl  
python3:any  

#### 5.42.3. Configuration Files
(None)

#### 5.42.4. Executable Files
(None)

<br>

### 5.43 python3-urllib3 Package
#### 5.43.1. Official Package Description
HTTP library with thread-safe connection pooling for Python3  
urllib3 supports features left out of urllib and urllib2 libraries.  
.  
Re-use the same socket connection for multiple requests (HTTPConnectionPool  
and HTTPSConnectionPool) (with optional client-side certificate  
verification).  
File posting (encode_multipart_formdata).  
Built-in redirection and retries (optional).  
Supports gzip and deflate decoding.  
Thread-safe and sanity-safe.  
Small and easy to understand codebase perfect for extending and  
building upon.  
.  
This package contains the Python 3 version of the library.  

#### 5.43.2. Depended Packages
python3-six  
python3:any  

#### 5.43.3. Configuration Files
(None)

#### 5.43.4. Executable Files
(None)

<br>

### 5.44 python3.11 Package
#### 5.44.1. Official Package Description
Interactive high-level object-oriented language (version 3.11)  
Python is a high-level, interactive, object-oriented language. Its 3.11 version  
includes an extensive class library with lots of goodies for  
network programming, system administration, sounds and graphics.  

#### 5.44.2. Depended Packages
libpython3.11-stdlib  
media-types  
python3.11-minimal  

#### 5.44.3. Configuration Files
(None)

#### 5.44.4. Executable Files
/usr/bin/pdb3.11  
/usr/bin/pydoc3.11  
/usr/bin/pygettext3.11  

<br>

