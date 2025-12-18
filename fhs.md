##### FHS
# Filesystem Hierarchy Standard
</details>

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. Introduction 

The Filesystem Hierarchy Standard (FHS) is a set of guidelines and specifications for organizing the directory structure in Unix-like operating systems.

The goal of the FHS is to establish a consistent and predictable directory layout across different Unix and Unix-like systems. This consistency makes it easier for software developers, system administrators, and users to locate files and understand the system's organization.

**Required Directories:**

- `/bin`: Essential command binaries
- `/boot`: Static files of the boot loader
- `/dev`: Device files
- `/etc`: Host-specific system configuration
- `/lib`: Essential shared libraries and kernel modules
- `/media`: Mount point for removable media
- `/mnt`: Mount point for mounting a filesystem temporarily
- `/opt`: Add-on application software packages
- `/run`: Data relevant to running processes
- `/sbin`: Essential system binaries
- `/srv`: Data for services provided by this system
- `/tmp`: Temporary files
- `/usr`: Secondary hierarchy
- `/var`: Variable data

**Optional Directories:**

- `/home`: User home directories
- `/lib*`: Alternate format essential shared libraries
- `/root`: Home directory for the root user

**Linux Specific Directories:**

- `/proc`: Kernel and process information virtual filesystem
- `/sys`: Kernel and system information virtual filesystem

**Debian-Specific Directory:**

- `/lost+found`: File fragments recovered during previous `fsck` operations


### 0.2. Quick Reference

- **`/bin`**: Essential command binaries
- **`/boot`**: Static files of the boot loader
- **`/dev`**: Device files
- **`/etc`**: Host-specific system configuration
- **`/etc/opt`**: Configuration for `/opt`
- **`/etc/X11`**: Configuration for the X Window system (Optional)
- **`/etc/sgml`**: Configuration for SGML (Optional)
- **`/etc/xml`**: Configuration for XML (Optional)
- **`/home`**: User home directories
- **`/lib`**: Essential shared libraries and kernel modules
- **`/lib/modules`**: Loadable kernel modules (Optional)
- **`/lib*`**: Alternate format essential shared libraries
- **`/media`**: Mount point for removable media
- **`/media/floppy`**: Floppy drive (Optional)
- **`/media/cdrom`**: CD-ROM drive (Optional)
- **`/media/cdrecorder`**: CD writer (Optional)
- **`/media/zip`**: Zip drive (Optional)
- **`/mnt`**: Mount point for mounting a filesystem temporarily
- **`/opt`**: Add-on application software packages
- **`/proc`**: Kernel and process information virtual filesystem
- **`/root`**: Home directory for the root user
- **`/run`**: Data relevant to running processes
- **`/sbin`**: Essential system binaries
- **`/srv`**: Data for services provided by this system
- **`/sys`**: Kernel and system information virtual filesystem
- **`/tmp`**: Temporary files
- **`/usr`**: Secondary hierarchy
- **`/usr/bin`**: Most user commands
- **`/usr/games`**: Games and educational binaries (Optional)
- **`/usr/include`**: Header files included by C programs
- **`/usr/lib`**: Libraries
- **`/usr/libexec`**: Binaries run by other programs (Optional)
- **`/usr/lib*`**: Alternate Format Libraries (Optional)
- **`/usr/local`**: Local hierarchy (empty after main installation)
- **`/usr/local/bin`**: Local binaries
- **`/usr/local/etc`**: Host-specific system configuration for local binaries
- **`/usr/local/games`**: Local game binaries
- **`/usr/local/include`**: Local C header files
- **`/usr/local/lib`**: Local libraries
- **`/usr/local/man`**: Local online manuals
- **`/usr/local/sbin`**: Local system binaries
- **`/usr/local/share`**: Local architecture-independent hierarchy
- **`/usr/local/src`**: Local source code
- **`/usr/sbin`**: Non-vital system binaries
- **`/usr/share`**: Architecture-independent data
- **`/usr/share/color`**: Color management information
- **`/usr/share/dict`**: Word lists
- **`/usr/share/doc`**: Miscellaneous documentation
- **`/usr/share/games`**: Static data files for `/usr/games`
- **`/usr/share/info`**: Primary directory for GNU Info system
- **`/usr/share/locale`**: Locale information
- **`/usr/share/man`**: Online manuals
- **`/usr/share/misc`**: Miscellaneous architecture-independent data
- **`/usr/share/nls`**: Message catalogs for Native Language Support
- **`/usr/share/ppd`**: Printer definitions
- **`/usr/share/sgml`**: SGML data
- **`/usr/share/terminfo`**: Directories for terminfo database
- **`/usr/share/tmac`**: Troff macros not distributed with groff
- **`/usr/share/xml`**: XML data
- **`/usr/share/zoneinfo`**: Timezone information and configuration
- **`/usr/src`**: Source code (Optional)
- **`/var`**: Variable data
- **`/var/account`**: Process accounting logs (Optional)
- **`/var/cache`**: Application cache data
- **`/var/crash`**: System crash dumps (Optional)
- **`/var/games`**: Variable game data (Optional)
- **`/var/lib`**: Variable state information
- **`/var/local`**: Variable data for `/usr/local`
- **`/var/lock`**: Lock files
- **`/var/log`**: Log files and directories
- **`/var/mail`**: User mailbox files (Optional)
- **`/var/opt`**: Variable data for `/opt`
- **`/var/run`**: Data relevant to running processes
- **`/var/spool`**: Application spool data
- **`/var/tmp`**: Temporary files preserved between system reboots
- **`/var/yp`**: Network Information Service (NIS) database files

### 0.3. Sources:

- **Filesystem Hierarchy Standard** by LSB Workgroup, The Linux Foundation.
- [Deepseek](https://www.deepseek.com/)
- [ChatGPT](https://chatgpt.com/)

<br>
</details>

<details markdown='1'>
<summary>
1. /bin - Essential Command Binaries
</summary>

---

Contains essential command binaries for both system administrators and users. These commands must be available when no other filesystems are mounted (e.g., in single-user mode). It may also contain commands used indirectly by scripts.

In Debian 13 and Ubuntu 24.04, `/bin` is a symbolic link to `/usr/bin`.

**Rule:** There must be no subdirectories in `/bin`.

Command binaries that are not essential enough to reside in `/bin` should be placed in `/usr/bin` instead.

**Example commands:** `cat`, `chgrp`, `chmod`, `chown`, `cp`, `date`, `dd`, `df`, `dmesg`, `echo`, `false`, `hostname`, `kill`, `ln`, `login`, `ls`, `mkdir`, `mknod`, `more`, `mount`, `mv`, `ps`, `pwd`, `rm`, `rmdir`, `sed`, `sh`, `stty`, `su`, `sync`, `true`, `umount`, `uname`.

<br>
</details>

<details markdown='1'>
<summary>
2. /boot - Static Files of the Boot Loader
</summary>

---

Contains all files required for the boot process, except for configuration files not needed at boot time and the map installer. It stores data used before the kernel begins executing user-mode programs, which may include saved master boot sectors and sector map files.

**Rules:**

- Programs necessary to enable the boot loader to boot a file must be placed in `/sbin`.
- Configuration files for boot loaders that are not required at boot time must be placed in `/etc`.
- The operating system kernel must be located in either `/` or `/boot`.

**Note:** Certain architectures may have additional requirements for `/boot` due to limitations or expectations specific to that architecture.

<br>
</details>

<details markdown='1'>
<summary>
3. /dev - Device Files
</summary>

---

The /dev directory is the location of special or device files.

The devices in the /dev directory are created dynamically during the boot process or when new hardware is detected.

**Examples:**

- `/dev/tty0` – Terminal device
- `/dev/sda` – First SCSI/SATA disk
- `/dev/null` – Null device (discards all data written to it)

<br>
</details>



<details markdown='1'>
<summary>
4. /etc - Host-specific System Configuration
</summary>

---

The `/etc` hierarchy contains configuration files.

**Rules:**

- It is recommended that files be stored in subdirectories of `/etc` rather than directly in `/etc`.
- No binaries may be located under `/etc`.

**Required directory (or symbolic link):**

- `/etc/opt`: Configuration for `/opt`

**Required directories (if the corresponding subsystem is installed):**

- `/etc/X11`: Configuration for the X Window System
- `/etc/sgml`: Configuration for SGML
- `/etc/xml`: Configuration for XML

**Required files (if the corresponding subsystem is installed):**

- `/etc/csh.login`: Systemwide initialization file for C shell logins
- `/etc/exports`: NFS filesystem access control list
- `/etc/fstab`: Static information about filesystems
- `/etc/ftpusers`: FTP daemon user access control list
- `/etc/gateways`: File listing gateways for `routed`
- `/etc/gettydefs`: Speed and terminal settings used by `getty`
- `/etc/group`: User group file
- `/etc/host.conf`: Resolver configuration file
- `/etc/hosts`: Static information about hostnames
- `/etc/hosts.allow`: Host access file for TCP wrappers
- `/etc/hosts.deny`: Host access file for TCP wrappers
- `/etc/hosts.equiv`: List of trusted hosts for `rlogin`, `rsh`, `rcp`
- `/etc/hosts.lpd`: List of trusted hosts for `lpd`
- `/etc/inetd.conf`: Configuration file for `inetd`
- `/etc/inittab`: Configuration file for `init`
- `/etc/issue`: Pre-login message and identification file
- `/etc/ld.so.conf`: List of extra directories to search for shared libraries
- `/etc/motd`: Post-login message of the day file
- `/etc/mtab`: Dynamic information about filesystems
- `/etc/mtools.conf`: Configuration file for `mtools`
- `/etc/networks`: Static information about network names
- `/etc/passwd`: Password file
- `/etc/printcap`: LPD printer capability database
- `/etc/profile`: Systemwide initialization file for `sh` shell logins
- `/etc/protocols`: IP protocol listing
- `/etc/resolv.conf`: Resolver configuration file
- `/etc/rpc`: RPC protocol listing
- `/etc/securetty`: TTY access control for root login
- `/etc/services`: Port names for network services
- `/etc/shells`: Pathnames of valid login shells
- `/etc/syslog.conf`: Configuration file for `syslogd`


### 4.1. /etc/opt - Configuration for /opt

Host-specific configuration files for add-on application software packages must be installed in `/etc/opt/<subdir>`, where `<subdir>` matches the package's subtree in `/opt` where its static data resides.

No specific structure is imposed on `/etc/opt/<subdir>`.

If a configuration file must reside elsewhere for the package or system to function correctly, it may be placed outside `/etc/opt/<subdir>`.


### 4.2. /etc/X11 - Configuration for the X Window System

Location for all X11 host-specific configuration. This directory ensures local control when `/usr` is mounted read-only.

**Required files (if installed):**

- `/etc/X11/xorg.conf`: Configuration file for X.org
- `/etc/X11/Xmodmap`: Global X11 keyboard modification file


### 4.3. /etc/sgml - Configuration for SGML

Contains generic configuration files defining high-level parameters of SGML systems.

**File naming conventions:**

- `*.conf`: Generic configuration files
- `*.cat`: DTD-specific centralized catalogs containing references to other catalogs needed for a given DTD


### 4.4. /etc/xml - Configuration for XML

Contains generic configuration files defining high-level parameters of XML systems.

**File naming convention:**

- `*.conf`: Generic configuration files

<br>
</details>

<details markdown='1'>
<summary>
5. /home - User Home Directories
</summary>

---

User home directories are stored here.

**Configuration files:**

- User-specific application configuration files are stored as "dot files" (starting with `.`) in the user's home directory.
- If an application requires multiple configuration files, they should be placed in a "dot directory" (starting with `.`). Within such a directory, configuration files should not start with `.`.

**Finding home directories:**

- Use library functions (`getpwent`, `getpwent_r`, `fgetpwent`) rather than parsing `/etc/passwd`, as user information may be stored remotely (e.g., via NIS).

**Best practices:**

- Apart from autosave and lock files, programs should avoid creating non-dot files or directories in a home directory without user consent.

<br>
</details>

<details markdown='1'>
<summary>
6. /lib - Essential Shared Libraries and Kernel Modules
</summary>

---

In Debian 13 and Ubuntu 24.04, `/lib` is a symbolic link to `/usr/lib`.

Contains shared library images required to boot the system and run commands in `/bin` and `/sbin`.

**Required files (or symbolic links):**
- `/lib/libc.so.*`: Dynamically-linked C library
- `/lib/ld*`: Execution-time linker/loader

**Historical requirement:**
- If a C preprocessor is installed, `/lib/cpp` must reference it.

**Required directory (if installed):**
- `/lib/modules`: Loadable kernel modules

<br>
</details>

<details markdown='1'>
<summary>
7. /lib* - Alternate format essential shared libraries
</summary>

---

Systems supporting multiple binary formats requiring separate libraries may have one or more variants of `/lib`, such as `/lib64`.

**Example:**

- Debian 13 and Ubuntu 24.04 include `/lib64`, which is a symbolic link to `/usr/lib64`.

**Requirements:**

- The contents of these directories must meet the same requirements as `/lib`, except `/lib*/cpp` is not required.


<br>
</details>

<details markdown='1'>
<summary>
8. /media - Mount Point for Removable Media
</summary>

---

Contains subdirectories used as mount points for removable media such as floppy disks, CD-ROMs, and ZIP drives.

**Required directories (if installed):**

- `/media/floppy`: Floppy drive
- `/media/cdrom`: CD-ROM drive
- `/media/cdrecorder`: CD writer
- `/media/zip`: ZIP drive

**Multiple devices:**

- If multiple devices of the same type exist, mount directories can be created by appending a digit (starting with `0`) to the base name, but the unqualified name must also exist (e.g., `/media/cdrom0`, `/media/cdrom`).

<br>
</details>

<details markdown='1'>
<summary>
9. /mnt - Mount Point for Mounting a Filesystem Temporarily
</summary>

---

System administrators may temporarily mount filesystems here.

**Rules:**

- The contents of this directory are a local issue and should not affect program execution.
- Installation programs must not use this directory; they should use a suitable temporary directory not in use by the system.

<br>
</details>


<details markdown='1'>
<summary>
10. /opt - Add-on Application Software Packages
</summary>

---

This directory is empty in default Debian 13 and Ubuntu 24.04 installations.

Reserved for the installation of add-on application software packages. Its purpose is to provide a location where software vendors can install and organize their software separately from the core system's directory structure.

**Rules:**

- A package in `/opt` must locate its static files in a separate directory tree: either `/opt/<package>` or `/opt/<provider>`, where:
    - `<package>` is a descriptive name for the software package.
    - `<provider>` is the LANANA-registered name of the provider.
- The following directories are reserved for local system administrator use:
    - `/opt/bin`
    - `/opt/doc`
    - `/opt/include`
    - `/opt/info`
    - `/opt/lib`
    - `/opt/man`
- Variable package files (those that change during normal operation) must be installed in `/var/opt`.

- Host-specific configuration files must be installed in `/etc/opt`.

<br>
</details>

<details markdown='1'>
<summary>
11. /root - Home directory for the root user
</summary>

---

Recommended home directory for the root user.

**Guidelines:**

- While the root account's home directory may be determined by developer or local preference, this is the recommended default location.
- The root account should not be used for tasks that can be performed by an unprivileged user; it should be reserved for system administration only.
- For this reason, subdirectories for mail and other user applications are not recommended in `/root`.

<br>
</details>

<details markdown='1'>
<summary>
12. /run - Data Relevant to Running Processes
</summary>

---

Contains system information describing the system since it was booted.

**Rules:**

- Files under this directory must be cleared (removed or truncated as appropriate) at the beginning of the boot process.
- This directory replaces the functionality previously served by `/var/run`. Programs may continue to use `/var/run` for backward compatibility.
- Programs are encouraged to create subdirectories in `/run` if they use multiple runtime files.

**Process Identifier (PID) files:**

- PID files, originally placed in `/etc`, must now be placed in `/run`.
- Naming convention: `{program-name}.pid` (e.g., `/run/crond.pid`).

<br>
</details>

<details markdown='1'>
<summary>
13. /sbin - Essential System Binaries
</summary>

---

In Debian 13 and Ubuntu 24.04, `/sbin` is a symbolic link to `/usr/sbin`.

**Purpose:** Stores utilities used for system administration (root-only commands), including binaries essential for booting, restoring, recovering, or repairing the system.

**Rules:**

- There must be no subdirectories in `/sbin`.
- If a normal user will ever run a command directly, it must be placed in one of the "bin" directories (`/bin`, `/usr/bin`, `/usr/local/bin`).
- Ordinary users should not need `/sbin` directories in their `PATH`.

**Required command:**

- `/sbin/shutdown`: Command to bring the system down.

**Required files (if corresponding subsystem is installed):**

- `/sbin/fastboot`: Reboot without checking disks
- `/sbin/fasthalt`: Stop system without checking disks
- `/sbin/fdisk`: Partition table manipulator
- `/sbin/fsck`: Filesystem check and repair utility
- `/sbin/fsck.*`: Filesystem-specific check and repair utility
- `/sbin/getty`: Getty program
- `/sbin/halt`: Command to stop the system
- `/sbin/ifconfig`: Configure a network interface
- `/sbin/init`: Initial process
- `/sbin/mkfs`: Command to build a filesystem
- `/sbin/mkfs.*`: Command to build a specific filesystem
- `/sbin/mkswap`: Command to set up a swap area
- `/sbin/reboot`: Command to reboot the system
- `/sbin/route`: IP routing table utility
- `/sbin/swapon`: Enable paging and swapping
- `/sbin/swapoff`: Disable paging and swapping
- `/sbin/update`: Daemon to periodically flush filesystem buffers

<br>
</details>

<details markdown='1'>
<summary>
14. /srv - Data for Services Provided by This System
</summary>

---

This directory is empty in default Debian 13 and Ubuntu 24.04 installations.

**Purpose:** Contains site-specific data served by the system. It provides a location for service-specific data separate from operating system files.

**Key points:**

- Unlike `/usr` or `/var`, which may contain data related to distribution packages, `/srv` is not intended for package-managed data.
- It is reserved for locally administered data associated with specific services (e.g., web content, FTP files, version control repositories).

<br>
</details>

<details markdown='1'>
<summary>
15. /tmp - Temporary Files
</summary>

---

Provides a location for temporary files used by programs and users during their activities.

**Guidelines:**

- It is recommended that files and directories in `/tmp` be deleted when the system boots.
- Many applications and system processes use `/tmp` for temporary storage (e.g., package managers, installers, user sessions).
- The directory is typically world-writable, allowing any user to create, modify, or delete files, facilitating sharing of temporary data.

<br>
</details>

<details markdown='1'>
<summary>
16. /usr - Secondary hierarchy
</summary>

---

Stands for "Unix System Resources".

Contains user-related programs, libraries, documentation, and other resources. Typically mounted as a separate partition and may be shared among multiple machines in a networked environment.

**Required directories (or symbolic links):**

- `/usr/bin`: Most user commands
- `/usr/lib`: Libraries
- `/usr/local`: Local hierarchy (empty after main installation)
- `/usr/sbin`: Non-vital system binaries
- `/usr/share`: Architecture-independent data

**Optional directories (or symbolic links):**

- `/usr/games`: Games and educational binaries
- `/usr/include`: Header files included by C programs
- `/usr/libexec`: Binaries run by other programs
- `/usr/lib*`: Alternate Format Libraries
- `/usr/src`: Source code

### 16.1. /usr/bin - Most User Commands

Primary directory for executable commands.

**Rule:** No subdirectories in `/usr/bin`.

**Required files (if corresponding subsystem installed):**

- `/usr/bin/perl`: Practical Extraction and Report Language
- `/usr/bin/python`: Python interpreted language
- `/usr/bin/tclsh`: Simple shell containing Tcl interpreter
- `/usr/bin/wish`: Simple Tcl/Tk windowing shell
- `/usr/bin/expect`: Program for interactive dialog

### 16.2. /usr/include - Header Files Included by C Programs

Contains general-use C programming language include files.

**Required directory (if installed):**

- `/usr/include/bsd`: BSD compatibility include files (optional)

### 16.3. /usr/lib - Libraries

Contains object files and libraries. May also include internal binaries not intended for direct execution.

**Guidelines:**

- Applications may use a single subdirectory under `/usr/lib`. All architecture-dependent data exclusive to the application must reside there.
- For historical reasons, `/usr/lib/sendmail` must be a symbolic link to the system's sendmail-compatible command, if present.

### 16.4. /usr/libexec - Binaries Run by Other Programs

Contains internal binaries not intended for direct execution by users or shell scripts.

**Guidelines:**

- Applications may use a single subdirectory under `/usr/libexec`.
- Applications using `/usr/libexec` must not use `/usr/lib` for internal binaries (though they may use `/usr/lib` for other purposes).

### 16.5. /usr/lib* - Alternate Format Libraries

Serves the same role as `/usr/lib` for alternate binary formats, except:
- Symbolic links `/usr/lib*/sendmail` and `/usr/lib*/X11` are not required.

**Example:**

- Debian 13 and Ubuntu 24.04 include `/usr/lib64` (symbolic link to `/usr/lib64`).

**Note:** If `/usr/lib` and `/usr/lib<qual>` are the same (via symbolic link), per-application subdirectories may exist in both.


### 16.6. /usr/local - Local Hierarchy

Reserved for locally installed software by the system administrator. Should be safe from overwriting during system updates.

**Required directories:**

- `/usr/local/bin`: Local binaries
- `/usr/local/etc`: Host-specific configuration for local binaries
- `/usr/local/games`: Local game binaries
- `/usr/local/include`: Local C header files
- `/usr/local/lib`: Local libraries
- `/usr/local/man`: Local online manuals
- `/usr/local/sbin`: Local system binaries
- `/usr/local/share`: Local architecture-independent hierarchy
- `/usr/local/src`: Local source code

**Notes:**

- If `/lib*` or `/usr/lib*` exist, equivalent directories must exist in `/usr/local`.
- `/usr/local/etc` may be a symbolic link to `/etc/local`.

### 16.7. /usr/sbin - Non-vital System Binaries

Contains non-essential binaries used exclusively by the system administrator.

**Rules:**

- System administration programs required for repair, recovery, mounting `/usr`, or other essential functions must be in `/sbin`.
- No subdirectories in `/usr/sbin`.


### 16.8. /usr/share - Architecture-Independent Data

Contains all read-only, architecture-independent data files. Intended to be shareable across all architecture platforms of a given OS.

**Required directories:**

- `/usr/share/man`: Online manuals
- `/usr/share/misc`: Miscellaneous architecture-independent data

**Required directories (if corresponding subsystem installed):**

- `/usr/share/color`: Color management information
- `/usr/share/dict`: Word lists
- `/usr/share/doc`: Miscellaneous documentation
- `/usr/share/games`: Static data files for `/usr/games`
- `/usr/share/info`: Primary directory for GNU Info system
- `/usr/share/locale`: Locale information
- `/usr/share/nls`: Message catalogs for Native Language Support
- `/usr/share/ppd`: Printer definitions
- `/usr/share/sgml`: SGML data
- `/usr/share/terminfo`: Directories for terminfo database
- `/usr/share/tmac`: Troff macros not distributed with groff
- `/usr/share/xml`: XML data
- `/usr/share/zoneinfo`: Timezone information and configuration

**Game data note:** Data in `/usr/share/games` must be static. Modifiable files (e.g., score files, logs) belong in `/var/games`.


#### 16.8.1. /usr/share/color - Color Management Information

Home for ICC color management files. No files at the top level; all files must be in subdirectories.

**Required directory (if installed):**

- `/usr/share/color/icc`: ICC color profiles (optional)


#### 16.8.2. /usr/share/dict - Word Lists

Home for word lists, traditionally containing only the English words file.

**Required file:**

- `/usr/share/dict/words`: List of English words

**Notes:**

- Sites needing both American and British spelling may link `words` to `american-english` or `british-english`.
- Word lists for other languages use the English name (e.g., `/usr/share/dict/french`).

#### 16.8.3. /usr/share/man - Online Manuals

Primary `mandir` for manual information related to commands and data under `/` and `/usr`.

#### 16.8.4. /usr/share/misc - Miscellaneous Architecture-independent Data

Contains miscellaneous files that do not require separate subdirectories.

**Required files (if installed):**

- `/usr/share/misc/ascii`: ASCII character set table
- `/usr/share/misc/termcap`: Terminal capability database
- `/usr/share/misc/termcap.db`: Terminal capability database



#### 16.8.5. /usr/share/ppd - Printer Definitions

Contains PostScript Printer Definition (PPD) files used by print systems. Files may be placed directly here or in subdirectories.

#### 16.8.6. /usr/share/sgml - SGML Data

Contains architecture-independent files for SGML applications (catalogs, DTDs, entities, style sheets).

**Required directories (if installed):**

- `/usr/share/sgml/docbook`: DocBook DTD
- `/usr/share/sgml/tei`: TEI DTD
- `/usr/share/sgml/html`: HTML DTD
- `/usr/share/sgml/mathml`: MathML DTD

**Note:** Files not specific to a DTD may reside in their own subdirectory.

#### 16.8.7. /usr/share/xml - XML Data

Contains architecture-independent files for XML applications.

**Required directories (if installed):**

- `/usr/share/xml/docbook`: DocBook XML DTD
- `/usr/share/xml/xhtml`: XHTML DTD
- `/usr/share/xml/mathml`: MathML DTD


### 16.9. /usr/src - Source Code

May contain source code for reference purposes. Source should generally not be built within this hierarchy.


<br>
</details>

<details markdown='1'>
<summary>
17. /var - Variable Data
</summary>

---

Contains variable data files: spool directories, administrative and logging data, and transient/temporary files.

**Guideline:** Applications must generally not add directories to the top level of `/var`.


**Required directories:**

- `/var/cache`: Application cache data
- `/var/lib`: Variable state information
- `/var/local`: Variable data for `/usr/local`
- `/var/lock`: Lock files
- `/var/log`: Log files and directories
- `/var/opt`: Variable data for `/opt`
- `/var/run`: Data relevant to running processes
- `/var/spool`: Application spool data
- `/var/tmp`: Temporary files preserved between system reboots

**Reserved directories (must not be used arbitrarily by new applications):**

- `/var/backups`
- `/var/cron`
- `/var/msgs`
- `/var/preserve`

**Required directories (if corresponding subsystem installed):**

- `/var/account`: Process accounting logs
- `/var/crash`: System crash dumps
- `/var/games`: Variable game data
- `/var/mail`: User mailbox files
- `/var/yp`: Network Information Service (NIS) database files

<br>
</details>

<details markdown='1'>
<summary>
18. Special to Linux
</summary>

---

Two additional directory standards specific to Linux:


### 18.1. /proc - Kernel and Process Information Virtual Filesystem

The de-facto standard for handling process and system information in Linux.

- A virtual filesystem dynamically generated by the kernel.
- Provides a window into the current state of the running kernel and system.


### 18.2. /sys - Kernel and System Information Virtual Filesystem

Exposes information about devices, drivers, and kernel features.

- A virtual filesystem.
- Allows reading and modifying certain kernel parameters through its files.

</details>
</summary>

