##### FHSOnDebianUbuntu 
# Filesystem Hierarchy Standard on Debian and Ubuntu
</details>

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.1. Introduction 

FHS (Filesystem Hierarchy Standard) is a set of guidelines and  specifications for organizing the structure and layout of directories in a Unix-like operating system. 

The goal of FHS is to create a consistent and predictable directory structure across different Unix and Unix-like systems, making it easier for software developers, system administrators, and users to understand where different types of files and data are located.

**Required Directories:**

- /bin: Essential command binaries
- /boot: Static files of the boot loader
- /dev: Device files
- /etc: Host-specific system configuration
- /lib: Essential shared libraries and kernel modules
- /media: Mount point for removable media
- /mnt: Mount point for mounting a filesystem temporarily
- /opt: Add-on application software packages
- /run: Data relevant to running processes
- /sbin: Essential system binaries
- /srv: Data for services provided by this system
- /tmp: Temporary files
- /usr: Secondary hierarchy
- /var: Variable data

**Optional Directories:**

- /home: User home directories
- /lib*: Alternate format essential shared libraries
- /root: Home directory for the root user

**Linux Specific Directories:**

- /proc: Kernel and process information virtual filesystem.
- /sys: Kernel and system information virtual filesystem.

In addition to the directory structure described in the FHS, the following directory can be found on Debian systems:

- /lost+found: File fragments that were recovered during the previous fsck


## 0.2. Quick Shot:
- **/bin:** Essential command binaries
- **/boot:** Static files of the boot loader
- **/dev:** Device files
- **/etc:** Host-specific system configuration
- **/etc/opt:** Configuration for /opt
- **/etc/X11:** Configuration for the X Window system (Optional)
- **/etc/sgml:** Configuration for SGML (Optional)
- **/etc/xml:** Configuration for XML (Optional)
- **/home:** User home directories
- **/lib:** Essential shared libraries and kernel modules
- **/lib/modules:** Loadable kernel modules (Optional)
- **/lib*:** Alternate format essential shared libraries
- **/media:** Mount point for removable media
- **/media/floppy:** Floppy drive (Optional)
- **/media/cdrom:** CD-ROM drive (Optional)
- **/media/cdrecorder:** CD writer (Optional)
- **/media/zip:** Zip drive (Optional)
- **/mnt:** Mount point for mounting a filesystem temporarily
- **/opt:** Add-on application software packages
- **/proc:** Kernel and process information virtual filesystem.
- **/root:** Home directory for the root user
- **/run:** Data relevant to running processes
- **/sbin:** Essential system binaries
- **/srv:** Data for services provided by this system
- **/sys:** Kernel and system information virtual filesystem.
- **/tmp:** Temporary files
- **/usr:** Secondary hierarchy
- **/usr/bin:** Most user commands
- **/usr/games:** Games and educational binaries (optional)
- **/usr/include:** Header files included by C programs
- **/usr/lib:** Libraries
- **/usr/libexec:** Binaries run by other programs (optional)
- **/usr/lib*:** Alternate Format Libraries (optional)
- **/usr/local:** Local hierarchy (empty after main installation)
- **/usr/local/bin:** Local binaries
- **/usr/local/etc:** Host-specific system configuration for local binaries
- **/usr/local/games:** Local game binaries
- **/usr/local/include:** Local C header files
- **/usr/local/lib:** Local libraries
- **/usr/local/man:** Local online manuals
- **/usr/local/sbin:** Local system binaries
- **/usr/local/share:** Local architecture-independent hierarchy
- **/usr/local/src:** Local source code
- **/usr/sbin:** Non-vital system binaries
- **/usr/share:** Architecture-independent data
- **/usr/share/color:** Color management information
- **/usr/share/dict:** Word lists
- **/usr/share/doc:** Miscellaneous documentation
- **/usr/share/games:** Static data files for /usr/games
- **/usr/share/info:** Primary directory for GNU Info system
- **/usr/share/locale:** Locale information
- **/usr/share/man:** Online manuals
- **/usr/share/misc:** Miscellaneous architecture-independent data
- **/usr/share/nls:** Message catalogs for Native language support
- **/usr/share/ppd:** Printer definitions
- **/usr/share/sgml:** SGML data
- **/usr/share/terminfo:** Directories for terminfo database
- **/usr/share/tmac:** troff macros not distributed with groff
- **/usr/share/xml:** XML data
- **/usr/share/zoneinfo:** Timezone information and configuration
- **/usr/src:** Source code (optional)
- **/var:** Variable data
- **/var/account:** Process accounting logs (Optional)
- **/var/cache:** Application cache data
- **/var/crash:** System crash dumps (Optional)
- **/var/games:** Variable game data (Optional)
- **/var/lib:** Variable state information
- **/var/local:** Variable data for /usr/local
- **/var/lock:** Lock files
- **/var/log:** Log files and directories
- **/var/mail:** User mailbox files (Optional)
- **/var/opt:**  Variable data for /opt
- **/var/run:**  Data relevant to running processes
- **/var/spool:** Application spool data
- **/var/tmp:** Temporary files preserved between system reboots
- **/var/yp:** Network Information Service (NIS) database files  

## 0.3. Sources:
**Filesystem Hierarchy Standard** by LSB Workgroup, The Linux Foundation.  
ChatGPT

<br>
</details>

<details markdown='1'>
<summary>
1. /bin - Essential Command Binaries
</summary>
---
Contains commands for system administrators and users. These commands  must be required required when no other filesystems are mounted (e.g. in
single user mode). It may also contain commands which are used indirectly by scripts.

In Debian 12 and Ubuntu 24.04 /bin is a symbolic link to /usr/bin.

There must be no subdirectories in /bin.

Command binaries that are not essential enough to place into /bin must be placed in /usr/bin, instead.

**Some example commands:** cat, chgrp, chmod, chown, cp, date, dd, df, dmesg, echo, false, hostname, kill, ln, login, ls, mkdir, mknod, more, mount, mv, ps, pwd, rm, rmdir, sed, sh, stty, su, sync, true, umount, uname.

<br>
</details>

<details markdown='1'>
<summary>
2. /boot - Static Files of the Boot Loader
</summary>
---
Contains everything required for the boot process except configuration files not needed at boot time and the map installer. Stores data that is used before the kernel begins executing user-mode programs. This may include saved master boot sectors and sector map files.

Programs necessary to arrange for the boot loader to be able to boot a file must be placed in /sbin.

Configuration files for boot loaders that are not required at boot time must be placed in /etc.

The operating system kernel must be located in either / or /boot.

Certain architectures may have other requirements for /boot related to limitations or expectations specific to that architecture. 

<br>
</details>

<details markdown='1'>
<summary>
3. /dev - Device Files
</summary>
---
The /dev directory is the location of special or device files.

The devices in the /dev directory are created dynamically during the boot process or when new hardware is detected.

**Some examples:**

- /dev/tty0
- /dev/sda
- /dev/null

<br>
</details>

<details markdown='1'>
<summary>
4. /etc - Host-specific System Configuration
</summary>
---
The /etc hierarchy contains configuration files.

It is recommended that files be stored in subdirectories of /etc rather than directly in /etc.

No binaries may be located under /etc.

The following directory (or symbolic link to directory) is required:

- /etc/opt:   Configuration for /opt

The following directories (or symbolic links to directories) must be in /etc, if the corresponding subsystem is installed:

- /etc/X11: Configuration for the X Window system
- /etc/sgml: Configuration for SGML
- /etc/xml: Configuration for XML

The following files, or symbolic links to files, must be in /etc if the corresponding subsystem is installed:

- /etc/csh.login:   Systemwide initialization file for C shell logins
- /etc/exports:     NFS filesystem access control list
- /etc/fstab:       Static information about filesystems
- /etc/ftpusers:    FTP daemon user access control list
- /etc/gateways:    File which lists gateways for routed
- /etc/gettydefs:   Speed and terminal settings used by getty
- /etc/group:       User group file
- /etc/host.conf:   Resolver configuration file
- /etc/hosts:       Static information about host names
- /etc/hosts.allow: Host access file for TCP wrappers
- /etc/hosts.deny:  Host access file for TCP wrappers
- /etc/hosts.equiv: List of trusted hosts for rlogin, rsh, rcp
- /etc/hosts.lpd:   List of trusted hosts for lpd
- /etc/inetd.conf:  Configuration file for inetd
- /etc/inittab:     Configuration file for init
- /etc/issue:       Pre-login message and identification file
- /etc/ld.so.conf:  List of extra directories to search for shared libraries
- /etc/motd:        Post-login message of the day file
- /etc/mtab:        Dynamic information about filesystems
- /etc/mtools.conf: Configuration file for mtools
- /etc/networks:    Static information about network names
- /etc/passwd:      The password file
- /etc/printcap:    The lpd printer capability database
- /etc/profile:     Systemwide initialization file for sh shell logins
- /etc/protocols:   IP protocol listing
- /etc/resolv.conf: Resolver configuration file
- /etc/rpc:         RPC protocol listing
- /etc/securetty:   TTY access control for root login
- /etc/services:    Port names for network services
- /etc/shells:      Pathnames of valid login shells
- /etc/syslog.conf: Configuration file for syslogd


### 4.1. /etc/opt - Configuration for /opt
Host-specific configuration files for add-on application software packages must be installed within the directory /etc/opt/<subdir>, where <subdir> is the name of the subtree in /opt where the static data from that package is stored.

No structure is imposed on the internal arrangement of /etc/opt/<subdir>.

If a configuration file must reside in a different location in order for the package or system to function properly, it may be placed in a location other than /etc/opt/<subdir>.


### 4.2. /etc/X11 - Configuration for the X Window System
Location for all X11 host-specific configuration. This directory is necessary to allow local control if /usr is mounted read only.

The following files, or symbolic links to files, must be in /etc/X11 if the corresponding subsystem is installed:

- /etc/opt/xorg.conf: The configuration file for X.org
- /etc/opt/Xmodmap:   Global X11 keyboard modification file


### 4.3. /etc/sgml - Configuration for SGML
Generic configuration files defining high-level parameters of the SGML systems.

Files with names *.conf indicate generic configuration files. 

Files with names *.cat are the DTD-specific centralized catalogs,  containing references to all other catalogs needed to use the given DTD.


### 4.4. /etc/xml - Configuration for XML
Generic configuration files defining high-level parameters of the XML systems are installed here. 

Files with names *.conf indicate generic configuration files.

<br>
</details>

<details markdown='1'>
<summary>
5. /home - User Home Directories
</summary>
---
Home directories of users are stored here.

User specific configuration files for applications are stored in the user's home directory in a file that starts with the '.' character (a "dot file").
 
If an application needs to create more than one dot file then they should be placed in a subdirectory with a name starting with a '.' character, (a "dot directory"). In this case the configuration files should not start with the '.' character.

To find a user's home directory, use a library function such as getpwent, getpwent_r of fgetpwent rather than relying on /etc/passwd because user information may be stored remotely using systems such as NIS.

It is recommended that, apart from autosave and lock files, programs should refrain from creating non dot files or directories in a home directory without user consent.

<br>
</details>

<details markdown='1'>
<summary>
6. /lib - Essential Shared Libraries and Kernel Modules
</summary>
---
In Debian 12 and Ubuntu 24.04 /lib is a symbolic link to /usr/lib.

Contains shared library images needed to boot the system and run the commands in /bin and /sbin.

At least one of each of the following filename patterns are required (files or symbolic links):

- /lib/libc.so.*: The dynamically-linked C library
- /lib/ld*: The execution time linker/loader

If a C preprocessor is installed, /lib/cpp must be a reference to it, for historical reasons.

The following directory (or symbolic link to directory) must be in /lib, if the corresponding subsystem is installed:

- /lib/modules:    Loadable kernel modules

<br>
</details>

<details markdown='1'>
<summary>
7. /lib* - Alternate format essential shared libraries
</summary>
---
There may be one or more variants of the /lib directory on systems which  support more than one binary format requiring separate libraries.

By default; Debian 12 and Ubuntu 24.04 has the following directories:

- /lib32: symbolic link to /usr/lib32
- /lib64: symbolic link to /usr/lib64

Debian 12 also has the following directory:

- /libx32: symbolic link to /usr/libx32

If one or more of these directories exist, the requirements for their contents are the same as the normal /lib directory, except that /lib*/cpp is not required.

<br>
</details>

<details markdown='1'>
<summary>
8. /media - Mount Point for Removable Media
</summary>
---
Contains subdirectories which are used as mount points for removable media such as floppy disks, cdroms and zip disks.

The following directories, or symbolic links to directories, must be in  /media, if the corresponding subsystem is installed:

- /media/floppy:      Floppy drive
- /media/cdrom:       CD-ROM drive
- /media/cdrecorder:  CD writer
- /media/zip:         Zip drive

On systems where more than one device exists for mounting a certain type of media, mount directories can be created by appending a digit to the name of those available above starting with '0', but the unqualified name must also exist.

<br>
</details>

<details markdown='1'>
<summary>
9. /mnt - Mount Point for Mounting a Filesystem Temporarily
</summary>
---
System administrators may temporarily mount a filesystem here.

The content of this directory is a local issue and should not affect the manner in which any program is run.

This directory must not be used by installation programs: a suitable temporary directory not in use by the system must be used instead.

<br>
</details>

<details markdown='1'>
<summary>
10. /opt - Add-on Application Software Packages
</summary>
---
This folder is empty on default Debian 12 and Ubuntu 24.04 installations.

Reserved for the installations of add-on application software packages.

The purpose of the /opt directory is to provide a location where software  vendors can install their software and organize it in a way that is separate from the rest of the system's directory structure.

A package in /opt must locate its static files in a separate /opt/package or /opt/provider directory tree. package is a name that describes the software package; and provider is the provider's LANANA registered name.

The directories /opt/bin, /opt/doc, /opt/include, /opt/info, /opt/lib, and /opt/man are reserved for local system administrator use.

Package files that are variable (change in normal operation) must be installed in /var/opt.

Host-specific configuration files must be installed in /etc/opt.

<br>
</details>

<details markdown='1'>
<summary>
11. /root - Home directory for the root user
</summary>
---
Recommended home directory for the root user.

The root account's home directory may be determined by developer or local preference, but this is the recommended default location.

It is not recommended to use the root account for tasks that can be performed by an unprivileged user, and that it be used solely for system administration.

For this reason, it is recommended that subdirectories for mail and other applications not appear in the root account's home directory.

<br>
</details>

<details markdown='1'>
<summary>
12. /run - Data Relevant to Running Processes
</summary>
---
Contains system information data describing the system since it was booted.

Files under this directory must be cleared (removed or truncated as  appropriate) at the beginning of the boot process.

The purposes of this directory were once served by /var/run. In general,  programs may continue to use /var/run to fulfill the requirements set out for /run for the purposes of backwards compatibility.

Programs may have a subdirectory of /run; this is encouraged for programs that use more than one run-time file.

Process identifier (PID) files, which were originally placed in /etc, must be placed in /run. The naming convention for PID files is {program-name}.pid. For example, the crond PID file is named /run/crond.pid.

<br>
</details>

<details markdown='1'>
<summary>
13. /sbin - Essential System Binaries
</summary>
---
In Debian 12 and Ubuntu 24.04 /sbin is a symbolic link to /usr/bin.

Utilities used for system administration (and other root-only commands) are stored in /sbin, /usr/sbin, and /usr/local/sbin. 

/sbin contains binaries essential for booting, restoring, recovering, and/or repairing the system in addition to the binaries in /bin. 

There must be no subdirectories in /sbin.

If a normal user will ever run a command directly, then it must be placed in one of the "bin" directories. 

Ordinary users should not have to place any of the sbin directories in their path.

The following command (or symbolic link) is required in /sbin:

- /sbin/shutdown:  Command to bring the system down.

The following files (or symbolic links to files) must be in /sbin if the  corresponding subsystem is installed:

- /sbin/fastboot: Reboot the system without checking the disks
- /sbin/fasthalt: Stop the system without checking the disks
- /sbin/fdisk: Partition table manipulator
- /sbin/fsck: File system check and repair utility
- /sbin/fsck.*: File system check and repair utility for a specific filesystem
- /sbin/getty: The getty program
- /sbin/halt: Command to stop the system
- /sbin/ifconfig: Configure a network interface
- /sbin/init: Initial process
- /sbin/mkfs: Command to build a filesystem
- /sbin/mkfs.*: Command to build a specific filesystem
- /sbin/mkswap: Command to set up a swap area
- /sbin/reboot: Command to reboot the system
- /sbin/route: IP routing table utility
- /sbin/swapon: Enable paging and swapping
- /sbin/swapoff: Disable paging and swapping
- /sbin/update: Daemon to periodically flush filesystem buffers

<br>
</details>

<details markdown='1'>
<summary>
14. /srv - Data for Services Provided by This System
</summary>
---
This directory is empty on default installations of Debian 12 and Ubuntu 24.04.

Contains site-specific data that is served by the system. This directory  provides a location for data that is served by various services running on the system, separate from other files associated with the operating system.

Unlike directories such as /usr or /var, which may contain data related to installed packages, the /srv directory is not intended for distribution packages. It is for locally administered data associated with specific services.

<br>
</details>

<details markdown='1'>
<summary>
15. /tmp - Temporary Files
</summary>
---
Provides a location for temporary files that are used by programs and users during the course of their activities. 

It is recommended that files and directories located in /tmp be deleted whenever the system is booted.

Many applications and system processes use the /tmp directory for temporary file storage. For example, the system's package manager or various software installers may use /tmp to download and store temporary files before installation.

/tmp directory is typically world-writable, allowing any user on the system to create, modify, or delete files within it. This openness facilitates the sharing of temporary files among users and processes.

<br>
</details>

<details markdown='1'>
<summary>
16. /usr - Secondary hierarchy
</summary>
---
Stands for "Unix System Resources".

Contains various subdirectories with user-related programs, libraries, documentation, and other resources. 

Typically mounted as a separate partition and may be shared among multiple machines in a networked environment.

The following directories (or symbolic links to directories) are required: 

- /usr/bin:    Most user commands
- /usr/lib:    Libraries
- /usr/local:  Local hierarchy (empty after main installation)
- /usr/sbin:   Non-vital system binaries
- /usr/share:  Architecture-independent data

The following directories (or symbolic links to directories) are optional: 

- /usr/games:    Games and educational binaries
- /usr/include:  Header files included by C programs
- /usr/libexec:  Binaries run by other programs
- /usr/lib*:     Alternate Format Libraries
- /usr/src:      Source code

### 16.1. /usr/bin - Most User Commands
Primary directory of executable commands on the system.

There must be no subdirectories in /usr/bin.

The following files, or symbolic links to files, must be in /usr/bin, if  the corresponding subsystem is installed:

- /usr/bin/perl: The Practical Extraction and Report Language
- /usr/bin/python: The Python interpreted language
- /usr/bin/tclsh: Simple shell containing Tcl interpreter
- /usr/bin/wish: Simple Tcl/Tk windowing shell
- /usr/bin/expect: Program for interactive dialog

### 16.2. /usr/include - Header Files Included by C Programs
All of the system's general-use include files for the C programming language should be placed here.

The following directory (or symbolic link to directory) must be in /usr/include, if the corresponding subsystem is installed:

- /usr/include/bsd: BSD compatibility include files (optional)

### 16.3. /usr/lib - Libraries
Includes object files and libraries. On some systems, it may also include internal binaries that are not intended to be executed directly by users or shell scripts.

Applications may use a single subdirectory under /usr/lib. If so; all architecture-dependent data exclusively used by the application must be placed within that subdirectory. 

For historical reasons, /usr/lib/sendmail must be a symbolic link which resolves to the sendmail-compatible command provided by the system's mail transfer agent, if the latter exists.

### 16.4. /usr/libexec - Binaries Run by Other Programs

Includes internal binaries that are not intended to be executed directly by users or shell scripts. 

Applications may use a single subdirectory under /usr/libexec.

Applications which use /usr/libexec in this way must not also use /usr/lib  to store internal binaries, though they may use /usr/lib for the other purposes documented here.

### 16.5. /usr/lib* - Alternate Format Libraries
By default; Debian 12 and Ubuntu 24.04 has the following directories:

- /usr/lib32: symbolic link to /usr/lib32
- /usr/lib64: symbolic link to /usr/lib64

Debian 12 also has the following directory:

- /usr/libx32: symbolic link to /usr/libx32

/usr/lib* performs the same role as /usr/lib for an alternate binary format, except that the symbolic links /usr/lib*/sendmail and /usr/lib*/X11 are not required.

The case where /usr/lib and /usr/lib<qual> are the same (one is a symbolic link to the other) these files and the per-application subdirectories will exist.

### 16.6. /usr/local - Local Hierarchy
For use by the system administrator when installing software locally. 

It needs to be safe from being overwritten when the system software is updated. 

The following directories (or symbolic links to directories), must be in /usr/local:

- /usr/local/bin:     Local binaries
- /usr/local/etc:     Host-specific system configuration for local binaries
- /usr/local/games:   Local game binaries
- /usr/local/include: Local C header files
- /usr/local/lib:     Local libraries
- /usr/local/man:     Local online manuals
- /usr/local/sbin:    Local system binaries
- /usr/local/share:   Local architecture-independent hierarchy
- /usr/local/src:     Local source code

If directories /lib* or /usr/lib* exist, the equivalent directories must also exist in /usr/local.

/usr/local/etc may be a symbolic link to /etc/local.

### 16.7. /usr/sbin - Non-vital System Binaries
Contains any non-essential binaries used exclusively by the system  administrator. 

System administration programs that are required for system repair, system
recovery, mounting /usr, or other essential functions must be placed in /sbin instead.
There must be no subdirectories in /usr/sbin.


### 16.8. /usr/share - Architecture-Independent Data
This hierarchy is for all read-only architecture independent data files.

This hierarchy is intended to be shareable among all architecture platforms of a given OS; thus, for example, a site with i386, Alpha, and PPC platforms might maintain a single /usr/share directory that is centrally-mounted. 

However, that /usr/share is generally not intended to be shared by different OSes or by different releases of the same OS.

Game data stored in /usr/share/games must be purely static data. Any  modifiable files, such as score files, game play logs, and so forth, should be placed in /var/games.

The following directories, or symbolic links to directories, must be in  /usr/share:

- /usr/share/man:   Online manuals
- /usr/share/misc:  Miscellaneous architecture-independent data

The following directories, or symbolic links to directories, must be in  /usr/share, if the corresponding subsystem is installed:

- /usr/share/color: Color management information
- /usr/share/dict: Word lists
- /usr/share/doc: Miscellaneous documentation
- /usr/share/games: Static data files for /usr/games
- /usr/share/info: Primary directory for GNU Info system
- /usr/share/locale: Locale information
- /usr/share/nls: Message catalogs for Native language support
- /usr/share/ppd: Printer definitions
- /usr/share/sgml: SGML data
- /usr/share/terminfo: Directories for terminfo database
- /usr/share/tmac: troff macros not distributed with groff
- /usr/share/xml: XML data
- /usr/share/zoneinfo: Timezone information and configuration


#### 16.8.1. /usr/share/color - Color Management Information
This directory is the home for ICC color management files installed by the system.

The following directory must be in /usr/share/color, if the corresponding  subsystem is installed:

- /usr/share/color/icc: ICC color profiles (optional)

The top-level directory /usr/share/color must not contain any files; all files should be in subdirectories.


#### 16.8.2. /usr/share/dict - Word Lists
Home for word lists on the system.

Traditionally this directory contains only the English words file, which is used by look(1) and various spelling programs. 

Words may use either American or British spelling.

The reason that only word lists are located here is that they are the only files common to all spell checkers.

The following file, or symbolic link to a file, must be in /usr/share/dict:

- /usr/share/dict/words: List of English words

Sites that require both American and British spelling may link words to  /usr/share/dict/american-english or /usr/share/dict/british-english.

Word lists for other languages may be added using the English name for that language, e.g., /usr/share/dict/french, /usr/share/dict/danish, etc. 

#### 16.8.3. /usr/share/man - Online Manuals
The primary **mandir** of the system is /usr/share/man. /usr/share/man contains manual information for commands and data under the / and /usr filesystems.


#### 16.8.4. /usr/share/misc - Miscellaneous Architecture-independent Data
Contains miscellaneous architecture-independent files which don't require a separate subdirectory under /usr/share.

The following files, or symbolic links to files, must be in /usr/share/misc if the corresponding subsystem is installed:

- /usr/share/misc/ascii: ASCII character set table
- /usr/share/misc/termcap: Terminal capability database
- /usr/share/misc/termcap.db: Terminal capability database


#### 16.8.5. /usr/share/ppd - Printer Definitions
Contains PostScript Printer Definition (PPD) files, which are used as  descriptions of printer drivers by many print systems. 

PPD files may be placed in this directory, or in a subdirectory.

#### 16.8.6. /usr/share/sgml - SGML Data
Contains architecture-independent files used by SGML applications, such as ordinary catalogs (not the centralized ones, see /etc/sgml), DTDs, entities, or style sheets.

The following directories, or symbolic links to directories, must be in  /usr/share/sgml, if the corresponding subsystem is installed:

- /usr/share/sgml/docbook: docbook DTD
- /usr/share/sgml/tei: tei DTD
- /usr/share/sgml/html: html DTD
- /usr/share/sgml/mathml: mathml DTD

Other files that are not specific to a given DTD may reside in their own  subdirectory.

#### 16.8.7. /usr/share/xml - XML Data
Contains architecture-independent files used by XML applications, such as ordinary catalogs (not the centralized ones, see /etc/sgml), DTDs, entities, or style sheets.

The following directories (or symbolic links to directories) must be in  /usr/share/xml, if the corresponding subsystem is installed:

- /usr/share/xml/docbook: docbook XML DTD
- /usr/share/xml/xhtml: XHTML DTD
- /usr/share/xml/mathml: MathML DTD


### 16.9. /usr/src - Source Code
Source codes may be placed in this subdirectory, only for reference purposes.

Generally, source should not be built within this hierarchy.

<br>
</details>

<details markdown='1'>
<summary>
17. /var - Variable Data
</summary>
---
Contains variable data files. This includes spool directories and files,  administrative and logging data, and transient and temporary files.

Applications must generally not add directories to the top level of /var.

The following directories (or symbolic links to directories) are required in /var:

- /var/cache: Application cache data
- /var/lib: Variable state information
- /var/local: Variable data for /usr/local
- /var/lock: Lock files
- /var/log: Log files and directories
- /var/opt: Variable data for /opt
- /var/run: Data relevant to running processes
- /var/spool: Application spool data
- /var/tmp: Temporary files preserved between system reboots

Following directories are **reserved** and must not be used arbitrarily by some new application:

- /var/backups
- /var/cron
- /var/msgs
- /var/preserve

The following directories, or symbolic links to directories, must be in /var, if the corresponding subsystem is installed:

- /var/account: Process accounting logs
- /var/crash: System crash dumps
- /var/games: Variable game data
- /var/mail: User mailbox files
- /var/yp: Network Information Service (NIS) database files

<br>
</details>

<details markdown='1'>
<summary>
18. Special to Linux
</summary>
---
There are two more directory standarts specific to Linux:

- /proc
- /sys


### 18.1. /proc - Kernel and Process Information Virtual Filesystem
The proc filesystem is the de-facto standard Linux method for handling process and system information, rather than /dev/kmem and other similar methods. 

/proc is a virtual filesystem, which means that it doesn't exist on a physical storage device like a hard drive. Instead, it is dynamically generated by the kernel and provides a window into the current state of the running kernel and system.


### 18.2. /sys - Kernel and System Information Virtual Filesystem
The sys filesystem is the location where information about devices, drivers, and some kernel features are exposed.

The /sys directory exposes information about various kernel parameters and configurations. You can read and modify certain kernel parameters through the files in this directory.

/sys is a virtual filesystem, which means that it doesn't exist on a physical storage device like a hard drive.

</details>
</summary>

