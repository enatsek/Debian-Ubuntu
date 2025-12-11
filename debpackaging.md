##### Deb Packaging 
# Creating and Using .deb Packages

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.1. The What

This tutorial covers the creation of a `.deb` package. A `.deb` package is a compressed archive of files used to install software on Debian GNU/Linux and Ubuntu systems.

As Debian or Ubuntu users, we typically use the `apt` command to install programs or services. In the background, `.deb` files are the actual packages being installed.

Our goal is to create and use a `.deb` package. Note that creating a completely new Debian package from scratch is a broader topic—a superset of what we’ll cover here—and could be the subject of a separate tutorial.

This tutorial is introductory and does not cover every detail. Its purpose is to help you create a simple package.

### 0.2. The Environment

**Workstation:** Debian 13 or Ubuntu 24.04 LTS  
**Test Servers:** Ubuntu 24.04 LTS, Ubuntu 22.04 LTS, Debian 13, Debian 12.

### 0.3. Sources

- [www.debian.org](https://www.debian.org/doc/debian-policy/)  
- [www.debian.org](https://www.debian.org/doc/manuals/maint-guide/dother.en.html)  
- [tldp.org](https://tldp.org/HOWTO/html_single/Debian-Binary-Package-Building-HOWTO/)  
- [github.com](https://github.com/rsm-gh/build-deb/blob/master/DEBIAN_BASICS.md)  


<br>
</details>

<details markdown='1'>
<summary>
1. Basic Information
</summary>

---

### 1.1. Package Types:

`.deb` packages can be either **source packages** or **binary packages**. As the names suggest, source packages contain source code, while binary packages contain compiled executables or scripts.

According to the Debian Policy Manual: *A Debian source package contains the source material used to construct one or more binary packages.*

In this tutorial, we will focus on **binary packages**.
 
### 1.2. Package Structure

A `.deb` package follows a specific naming format and contains three main files:

**Format:** `packagename_version-revision_architecture.deb`  
**Example:** `apache2_2.4.52-1debian4.4_amd64.deb`

**Internal files:**

1. **`debian-binary`**  
   Contains the Debian package format version, typically just `2.0`.

2. **`data.tar.zst`**  
   A compressed archive of files organized in directory structure. When the package is installed, these files are extracted to their corresponding locations in the filesystem. The extension may vary if a different compression method is used (e.g., `.gz`, `.xz`).

3. **`control.tar.zst`**  
   A compressed archive of control and maintenance scripts. Common files include:
   - **`control`**: Metadata about the package (name, version, dependencies, etc.)
   - **`conffiles`**: A list of configuration files that should be preserved during upgrades
   - **`preinst`**: Scripts executed **before** the package is unpacked (e.g., stopping services before an upgrade)
   - **`postinst`**: Scripts executed **after** the package is unpacked (e.g., starting services, updating system caches)
   - **`prerm`**: Scripts executed **before** the package is removed (e.g., stopping services)
   - **`postrm`**: Scripts executed **after** the package is removed (e.g., cleaning up temporary files)

### 1.3. .deb Package Manipulation

`.deb` packages can be installed directly using `apt`:

**Install a package:**

```
sudo apt install ./<package>
sudo apt install ./test.deb
```

**Remove a package:**

```
sudo apt remove <appname>
sudo apt remove test
```

**Purge a package** (removes configuration files as well):

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

Control files are located in the `control.tar.zst` archive. Some key files were listed in Section 1.2. Below is a more comprehensive list with brief descriptions; important files are covered in greater detail.

### 2.1. `control`

This file contains metadata used by package managers. It consists of fields and their corresponding values.

Most fields have single-line values, but some support multiple lines. For multi-line fields, each line after the first must begin with a space or tab.

**Fields in a binary package:**

- **`Package`** (Mandatory): Name of the package. May contain alphanumeric characters, hyphens (`-`), and periods (`.`).  
  Example: `openssh-server`

- **`Source`**: Name of the source package.  
  Example: `openssh`

- **`Version`** (Mandatory): Package version. Format: `[epoch:]upstream_version-debian_revision`. The epoch is optional.  
  Example: `1:8.9p1-3`

- **`Section`** (Recommended): Software category (e.g., `admin`, `database`, `httpd`, `java`).

- **`Priority`** (Recommended): Indicates the importance of the package:
    - **`required`**: Essential for system functionality.
    - **`important`**: Expected on every Linux system.
    - **`standard`**: Installed by default; must not conflict with other standard packages.
    - **`optional`**: Most packages fall here; may conflict with others.

- **`Architecture`** (Mandatory): Target architecture (e.g., `amd64`, `arm64`, `i386`, `powerpc`, `sparc`, `all`).

- **`Essential`**: If set to `yes`, the package manager will refuse to remove it. Usually set to `no` or omitted.

- **`Depends`**: Absolute dependencies; this package will not be configured unless all listed packages are configured.

- **`Pre-Depends`**: Like `Depends`, but dependencies must be configured **before** unpacking this package (use sparingly).

- **`Recommends`**: Strong but optional dependencies.

- **`Suggests`**: Suggested packages that enhance functionality.

- **`Enhances`**: Inverse of `Suggests`; indicates that other packages are more useful with this package.

- **`Breaks`**: This package breaks listed packages; they must be unconfigured before installation.

- **`Conflicts`**: Stronger than `Breaks`; conflicting packages must be removed before installation.

- **`Installed-Size`**: Estimated disk space (in kilobytes) required after installation.

- **`Maintainer`** (Mandatory): Name and email of the maintainer.  
  Example: `Exforge <exforge@x386.org>`

- **`Description`** (Mandatory): Package description. The first line is a short summary; subsequent lines provide detailed information.

- **`Homepage`**: URL of the package's website.

- **`Built-Using`**: Packages required during build but not runtime.

- **User-defined fields** may also appear. Ubuntu adds `Original-Maintainer` to preserve Debian maintainer information.

**Example: `apache2` control file (Debian 13):**

```
Package: apache2
Version: 2.4.65-2
Architecture: amd64
Maintainer: Debian Apache Maintainers <debian-apache@lists.debian.org>
Installed-Size: 576
Pre-Depends: init-system-helpers (>= 1.54~)
Depends: apache2-bin (= 2.4.65-2), apache2-data (= 2.4.65-2), apache2-utils (= 2.4.65-2), media-types, procps, perl:any
Recommends: ssl-cert
Suggests: apache2-doc, apache2-suexec-pristine | apache2-suexec-custom, ufw, www-browser
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
```

**Example: `openssh-server` control file (Debian 13):**

```
Package: openssh-server
Source: openssh
Version: 1:10.0p1-7
Architecture: amd64
Maintainer: Debian OpenSSH Maintainers <debian-ssh@lists.debian.org>
Installed-Size: 3429
Pre-Depends: init-system-helpers (>= 1.54~)
Depends: libpam-modules, libpam-runtime, lsb-base, openssh-client (= 1:10.0p1-7), openssh-sftp-server, procps, ucf, debconf (>= 0.5) | debconf-2.0, runit-helper (>= 2.14.0~), systemd | systemd-standalone-sysusers | systemd-sysusers, libaudit1 (>= 1:2.2.1), libc6 (>= 2.38), libcom-err2 (>= 1.43.9), libcrypt1 (>= 1:4.1.0), libgssapi-krb5-2 (>= 1.17), libkrb5-3 (>= 1.13~alpha1+dfsg), libpam0g (>= 0.99.7.1), libselinux1 (>= 3.1~), libssl3t64 (>= 3.0.0), libwrap0 (>= 7.6-4~), libwtmpdb0 (>= 0.13.0), zlib1g (>= 1:1.1.4)
Recommends: default-logind | logind | libpam-systemd, ncurses-term, xauth
Suggests: molly-guard, monkeysphere, ssh-askpass, ufw
Conflicts: sftp, ssh-socks, ssh2
Breaks: runit (<< 2.1.2-51~)
Replaces: openssh-client (<< 1:7.9p1-8), ssh, ssh-krb5
Provides: ssh-server
Section: net
Priority: optional
Multi-Arch: foreign
Homepage: https://www.openssh.com/
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

### 2.2. `conffiles`

Lists configuration files that should be preserved during upgrades. Users are warned if they have modified these files.

**Example from `openssh-server` (Ubuntu 22.04 LTS):**

```
/etc/default/ssh
/etc/init.d/ssh
/etc/pam.d/sshd
/etc/ssh/moduli
/etc/sv/ssh/.meta/installed
/etc/sv/ssh/finish
/etc/sv/ssh/log/run
/etc/sv/ssh/run
/etc/ufw/applications.d/openssh-server
```
 
### 2.3. preinst

Script executed **before** unpacking the package. Must be idempotent (can run more than once without any problems), start with a shebang (`#!`), and return `0` on success.

**Call scenarios:**

- `new-preinst install` – Before initial installation.
- `new-preinst install old-version new-version` – Before upgrading a removed package.
- `new-preinst upgrade old-version new-version` – Before package upgrade.
- `old-preinst abort-upgrade new-version` – If `postrm` fails during upgrade.

**Excerpt from `apache2` `preinst`:**

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

### 2.4. `postinst`

Script executed **after** unpacking the package. Must be idempotent, start with a shebang, and return `0` on success.

**Call scenarios:**

- `postinst configure old-version` – After installation.
- `old-postinst abort-upgrade new-version` – If `prerm` fails during upgrade.
- `old-postinst abort-remove` – If `prerm` fails during removal.
- `postinst abort-deconfigure in-favour new-package new-version [...]` – If `prerm` fails during deconfiguration due to conflict.


**Excerpt from `apache2` `postinst`:**

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

### 2.5. `prerm`

Script executed **before** removing a package. Must be idempotent, start with a shebang, and return `0` on success.

**Call scenarios:**

- `prerm remove` – Before removal.
- `old-prerm upgrade new-version` – Before upgrade.
- `new-prerm failed-upgrade old-version new-version` – If upgrade fails.
- `prerm deconfigure in-favour new-package new-version` – Before deconfiguration due to conflict.
- `prerm remove in-favour new-package new-version` – Before replacement due to conflict.

**Example from `mariadb-server` `prerm`:**

```
#!/bin/sh
set -e
# Automatically added by dh_installsystemd/13.24.2
if [ -z "$DPKG_ROOT" ] && [ "$1" = remove ] && [ -d /run/systemd/system ] ; then
	deb-systemd-invoke stop 'mariadb.service' >/dev/null || true
fi
# End automatically added section
# Automatically added by dh_installinit/13.24.2
if [ -z "$DPKG_ROOT" ] && [ "$1" = remove ] && [ -x "/etc/init.d/mariadb" ] ; then
	invoke-rc.d --skip-systemd-native mariadb stop || exit 1
fi
# End automatically added section
```

### 2.6. postrm

Script executed **after** removing a package. Must be idempotent, start with a shebang, and return `0` on success.

**Call scenarios:**

- `postrm remove` – After removal.
- `postrm purge` – After purging.
- `old-postrm upgrade new-version` – After upgrade.
- `new-postrm failed-upgrade old-version new-version` – If upgrade fails.
- `postrm disappear overwriter-package overwriter-version` – After files are overwritten.
- `new-postrm abort-install` – If `preinst` fails during installation.

**Excerpt from `openssh-server` `postrm`:**

```
if [ "$1" = remove ] && [ -d /run/systemd/system ] ; then
	systemctl --system daemon-reload >/dev/null || true
fi
if [ "$1" = "purge" ]; then
	if [ -x "/usr/bin/deb-systemd-helper" ]; then
		deb-systemd-helper purge 'sshd-keygen.service' >/dev/null || true
	fi
fi
```

### 2.7. `config`

Script run **before** `preinst`, before any pre-dependencies are satisfied. Used to prompt the user for configuration decisions.

**Example from `mariadb-server` `config`:**

```
#!/bin/bash

set -e

# shellcheck source=/dev/null
. /usr/share/debconf/confmodule

if [ -n "$DEBIAN_SCRIPT_DEBUG" ]
then
  set -v -x; DEBIAN_SCRIPT_TRACE=1
fi

${DEBIAN_SCRIPT_TRACE:+ echo "#42#DEBUG# RUNNING $0 $*" 1>&2}

# Beware that there are two ypwhich one of them needs the 2>/dev/null!
if test -n "$(command -v ypwhich 2>/dev/null)" && ypwhich > /dev/null 2>&1
then
  db_input high mariadb-server/nis_warning || true
  db_go
fi
```

### 2.8. `templates`

Contains templates for user prompts (used with `debconf`).

**Excerpt from `openssh-server` `templates`:**

```
Template: openssh-server/password-authentication
Type: boolean
Default: true
Description: Allow password authentication?
 By default, the SSH server will allow authenticating using a password.
 You may want to change this if all users on this system authenticate using
 a stronger authentication method, such as public keys.
```

### 2.9. `md5sums`

MD5 hashes of package files for integrity verification.

**Excerpt from `openssh-server` `md5sums`:**

```
4b50d38888a7c2093ea4928dca327287  usr/lib/openssh/ssh-session-cleanup
36b4eaabb3472c543e7e9e7c0c80a014  usr/lib/openssh/sshd-auth
269cc6f51c160b60b0f714ee2f1f434d  usr/lib/openssh/sshd-session
8ec138e332aa1fbc3f081c17e81b62f9  usr/lib/systemd/system/rescue-ssh.target
0cbed0c937f53a8d3e9372faa6c23e4c  usr/lib/systemd/system/ssh.service
144e44ecb5dfaa27337b7e5d6348e9fa  usr/lib/systemd/system/ssh.socket
a09b0c24335b507ec5c9f100f9ba3b15  usr/lib/systemd/system/sshd-keygen.service
09582565e7d6ab3f1f15293d0bc9ab97  usr/lib/systemd/system/sshd@.service
3890b397321c96e14ef5627d1ea251d0  usr/lib/sysusers.d/openssh-server.conf
550889177dce3b36aa2717e88c9bf7e1  usr/lib/tmpfiles.d/openssh-server.conf
283a135db1d5bf7fbe7483fe56269dfc  usr/sbin/sshd
f410eed89eecfb2bcf29440141a49d4f  usr/share/apport/package-hooks/openssh-server.py
77862d01cdeb1232790155687382fdad  usr/share/doc/openssh-client/examples/ssh-session-cleanup.service
931ec2a78f8e7e9b8971416497aecc5b  usr/share/lintian/overrides/openssh-server
58d232b99ab4d6c8fde0c12a98b8841c  usr/share/man/man5/moduli.5.gz
18f27d1ef2de5f84a601ffefa20568d2  usr/share/man/man5/sshd_config.5.gz
5a9a2a3ffa3b98bb9bfb77f057fada68  usr/share/man/man8/sshd.8.gz
0382ac8785a147d5a10f3fa0cdfd8eb5  usr/share/openssh/sshd_config
07e75bae4aeca2bbf7bb42ba6af88a7d  usr/share/openssh/sshd_config.md5sum
d41d8cd98f00b204e9800998ecf8427e  usr/share/runit/meta/ssh/installed
```

### 2.10. `triggers`

Declares package relationships with system triggers.

**Trigger directives:**

- `interest <trigger>` – Package is interested in the trigger.
- `interest-await <trigger>` – Puts triggering package in "awaited" state.
- `interest-noawait <trigger>` – Does not await the trigger.
- `activate <trigger>` – Any change activates the trigger.
- `activate-await <trigger>` – Only puts package in "awaited" state.
- `activate-noawait <trigger>` – Never puts package in "awaited" state.

**Example from `mariadb-server` `triggers`:**

```
interest-noawait /etc/mysql
interest-noawait /etc/systemd/system/mariadb.service.d
```

### 2.11. `symbols` and `shlibs`

Contain shared library information.

**Reference:**  
<https://man7.org/linux/man-pages/man5/deb-symbols.5.html>  
<https://man7.org/linux/man-pages/man5/deb-shlibs.5.html>

**Example from `slapd` `shlibs`:**

```
libslapi 2 slapd (>= 2.6.10+dfsg)
```

<br>
</details>


<details markdown='1'>
<summary>
3. Package Data Files
</summary>

---
### 3.1. Basics

Data files reside in the `data.tar.zst` archive. This archive contains files organized in their corresponding directory structure. During installation, each file is extracted to its appropriate location in the filesystem.

**Example: Directory structure of the `openssh-server` package (Ubuntu 22.04 LTS):**

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

Data files include binaries, static files, dynamic files, configurations, and more. Each file must be placed in an appropriate directory.

**Common locations:**

- **Architecture-independent, application-specific files** → `/usr/share`
- **User-specific configuration files** → `~/.packagename` (file or directory)
- **System-wide configuration files** → `/etc/packagename`
- **Systemd unit files** → `/lib/systemd/system`
- **Log files** → `/var/log/packagename`
- **Cron jobs** (depending on frequency):
    - `/etc/cron.hourly`
    - `/etc/cron.daily`
    - `/etc/cron.weekly`
    - `/etc/cron.monthly`
    - For custom schedules → `/etc/cron.d`

<br>
</details>

<details markdown='1'>
<summary>
4. Package Installation Process
</summary>

---

The installation process of a `.deb` package involves multiple steps, including script execution and dependency management. Below is a simplified overview of the flow:

```
If there is a previous version of the package:
  Call for the old package: "old-prerm upgrade new-version"
  If return status is not 0:
    Call for the current package: "new-prerm failed-upgrade old-version new-version"
    If return status is not 0:
      Call for the old package: "old-postinst abort-upgrade new-version"
        If return status is 0:
          Upgrade unsuccessful, old version remains functional
          Exit
        Else:
          Upgrade unsuccessful, old version is broken
          Exit

If there are conflicting and/or broken packages:
  For each conflicting/broken package:
    # Unconfigure them
    deconfigured's-prerm deconfigure in-favour package-being-installed version
    If return status is not 0:
      deconfigured's-postinst abort-deconfigure in-favour \
          package-being-installed-but-failed version
    # Remove them
    conflictor's-prerm remove in-favour package new-version
    If return status is not 0:
      conflictor's-postinst abort-remove in-favour package new-version
    If any packages depend on the conflicting/broken packages:
      For each dependent package:
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

# Run the preinst script of the new package
If the package is being upgraded:
  new-preinst upgrade old-version new-version
  If return status is not 0:
    new-postrm abort-upgrade old-version new-version
      If return status is 0:
        Upgrade unsuccessful, old version remains functional
        Exit
      Else:
        Upgrade unsuccessful, old version is broken
        Exit
Else if the package is new but old configuration files exist:
  new-preinst install old-version new-version
  If return status is not 0:
    new-postrm abort-install old-version new-version
    Installation unsuccessful
    Exit
Else:  # Fresh installation with no existing configuration files
  new-preinst install
  If return status is not 0:
    new-postrm abort-install
    Installation unsuccessful
    Exit

Unpack all files from the data archive
# A package cannot overwrite another package's files unless specified with "Replaces"

If the package is being upgraded:
  old-postrm upgrade new-version
  If return condition is not 0:
    new-postrm failed-upgrade old-version new-version
    If return condition is 0:
      Upgrade failed, old version remains functional
      Exit
    Else:
      # Upgrade failed; attempt to recover
      old-preinst abort-upgrade new-version
      If return condition is 0:
        new-postrm abort-upgrade old-version new-version
        If return condition is 0:
          old-postinst abort-upgrade new-version
          Upgrade failed, old version remains functional
          Exit
        Else:
          Upgrade failed, old version broken
          Exit
      Else:
        Upgrade failed, old version broken
        Exit

Files present in the old version but not in the new version are removed
The new file list replaces the old one
New maintenance scripts replace the old ones
For each package whose files were overwritten and is no longer required for dependencies:
  # Remove the overwritten package
  disappearer's-postrm disappear overwriter overwriter-version
  Remove package scripts
  Update package status to "Not-Installed"
If any files in the new package are also listed in other packages:
  Remove them
Remove temporary and backup files created during installation
Set the package status to "Unpacked"
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

The removal or purging of a package follows a structured sequence:

```
Run: prerm remove
If return status is not 0:
  If failure is due to conflict:
    Run: conflictor's-postinst abort-remove in-favour package new-version
  Else:
    Run: postinst abort-remove
  If return status is 0:
    Removal aborted; package remains installed
    Exit
  Else:
    Removal aborted; package is in a broken state
    Exit

Remove all package files (except configuration files listed in conffiles)
Remove all package maintenance scripts except postrm

If purging (not just removing):
  Remove configuration files and temporary/backup files created during installation
  Run: postrm purge
  Remove the package's file list from the system database
```

<br>
</details>

<details markdown='1'>
<summary>
6. .deb Package Preparation Checklist
</summary>

---

### 6.1. Create File and Folder Structure for the Package

A minimal directory structure for a package includes:

```
ProgramName-Version/
├── DEBIAN/
│   └── control
└── usr/
    └── bin/
        └── ProgramName
```

Additional files and directories you may need:

```
ProgramName-Version/
├── DEBIAN/
│   ├── control
│   ├── preinst
│   ├── postinst
│   ├── prerm
│   └── postrm
├── etc/
│   ├── ProgramName.conf
│   └── ProgramName/
├── usr/
│   ├── share/
│   │   ├── applications/
│   │   │   └── ProgramName.desktop
│   │   └── ProgramName/
│   │       └── ProgramFiles
│   └── bin/
│       └── ProgramName
└── (other directories as needed)
```

### 6.2. Copy Files

Place your program executable, control files, scripts, and other resources into the appropriate locations:

- **`/usr/share/ProgramName/`**: Use this directory if your program consists of multiple files.
- **`/etc/`** or **`/etc/ProgramName/`**: For configuration files (single file or a directory of configs).
- **`/usr/share/applications/`**: For desktop launcher files (`.desktop` entries).

### 6.3. Preparing and Building The Package

Once all files are in place, ensure executable files have the correct permissions:

```
chmod a+x ProgramName-Version/usr/bin/ProgramName
```

Then build the package using `dpkg-deb`:

```
dpkg-deb -Z xz --build --root-owner-group ProgramName-Version
```

The resulting `.deb` file (e.g., `ProgramName-Version.deb`) is your ready-to-use package.


<br>
</details>


<details markdown='1'>
<summary>
7. A Very Simple Package
</summary>

---

We will now create a very simple package named **"distro"**. This package contains a Python script that displays the Unix distribution name and version information.

The package includes only the executable script and the control file—no configuration files or maintenance scripts are required.

### 7.1. Create Folder Structure

First, create a `packages` directory in your home folder to organize your work:

```
mkdir ~/packages
```

Package naming follows the format: `packagename_version-revision_architecture.deb`. Create a folder for our package:

```
mkdir ~/packages/distro_1.0.0-1_all
```

Create subdirectories for the executable and control files:

```
mkdir -p ~/packages/distro_1.0.0-1_all/usr/bin
mkdir ~/packages/distro_1.0.0-1_all/DEBIAN
```

### 7.2. Create the Executable File

Create the Python script:

```
nano ~/packages/distro_1.0.0-1_all/usr/bin/distro
```

Add the following content:

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

Make the script executable:

```
chmod +x ~/packages/distro_1.0.0-1_all/usr/bin/distro
```

### 7.3. Create the Control File

Create the `control` file:

```
nano ~/packages/distro_1.0.0-1_all/DEBIAN/control
```

Add the following content:

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

Navigate to the packages directory and build the package:

```
cd ~/packages
dpkg-deb -Z xz --build --root-owner-group distro_1.0.0-1_all 
```

Your package, `distro_1.0.0-1_all.deb`, is now located in the `~/packages` folder.

**Note:** `dpkg-deb` typically uses `zst` compression, but we override it with the `-Z xz` flag for broader compatibility. Packages compressed with `zst` (default in Ubuntu 22.04) may not work on older Debian distributions.

<br>
</details>

<details markdown='1'>
<summary>
8. A More Complex Package: Watchbox
</summary>

---

OOur next package, **watchbox**, is more complex. It is a Python script designed to run as a systemd service.

The package must:

- Install as a systemd service
- Enable and start the service after installation
- Stop the service before removal or upgrade

Required control files: `control`, `conffiles`, `postinst`, and `prerm`.  
Data files: the script itself, a configuration file, and a systemd unit file.

### 8.0. About Watchbox

Watchbox is a demonstration service that periodically checks network connectivity for hosts, web pages, files, or services.

It consists of:
- `watchbox`: the main application
- `watchbox.conf`: configuration file
- `watchbox.service`: systemd service unit file

For more details, see: [https://github.com/enatsek/watchbox](https://github.com/enatsek/watchbox)

### 8.1. Download Watchbox Files

Download the necessary files from GitHub to a temporary location:

```
wget https://raw.githubusercontent.com/enatsek/watchbox/main/watchbox \
     -P /tmp
wget https://raw.githubusercontent.com/enatsek/watchbox/main/watchbox.conf \
     -P /tmp
wget https://raw.githubusercontent.com/enatsek/watchbox/main/watchbox.service \
     -P /tmp
```

### 8.2. Folder Structure

The package will have the following structure:

```
/packages/
~/packages/watchbox_0.9-1_all/
├── DEBIAN/
│   ├── control
│   ├── conffiles
│   ├── postinst
│   └── prerm
├── etc/
│   └── watchbox.conf
├── lib/
│   └── systemd/
│       └── system/
│           └── watchbox.service
└── usr/
    └── bin/
        └── watchbox
```

### 8.3. Create Folder Structure

Create the directories:

```
mkdir -p ~/packages/watchbox_0.9-1_all/DEBIAN/
mkdir -p ~/packages/watchbox_0.9-1_all/etc
mkdir -p ~/packages/watchbox_0.9-1_all/lib/systemd/system/
mkdir -p ~/packages/watchbox_0.9-1_all/usr/bin/
```

### 8.4. Copy Watchbox Files to Their Locations

```
cp /tmp/watchbox.conf ~/packages/watchbox_0.9-1_all/etc/
cp /tmp/watchbox.service ~/packages/watchbox_0.9-1_all/lib/systemd/system/
cp /tmp/watchbox -p ~/packages/watchbox_0.9-1_all/usr/bin/
```

Make the script executable:

```
chmod +x ~/packages/watchbox_0.9-1_all/usr/bin/watchbox
```

### 8.5. Create Control Files and Maintenance Scripts

**Control File (`control`):**

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/control
```

Add the following content:

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

**Configuration File List (`conffiles`):**

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/conffiles
```

Add:

```
/etc/watchbox.conf
```

**Post-Installation Script (`postinst`):**

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/postinst
```

Add:

```
#!/bin/bash
systemctl enable watchbox
systemctl start watchbox
```

Make it executable:

```
chmod +x ~/packages/watchbox_0.9-1_all/DEBIAN/postinst
```

**Pre-Removal Script (`prerm`):**

```
nano ~/packages/watchbox_0.9-1_all/DEBIAN/prerm
```

Fill as below (Stops watchbox service)

```
#!/bin/bash
systemctl stop watchbox
```

Make it executable:

```
chmod +x ~/packages/watchbox_0.9-1_all/DEBIAN/prerm
```

### 8.6. Build the Package

Navigate to the packages directory and build:

```
cd ~/packages
dpkg-deb -Z xz --build --root-owner-group watchbox_0.9-1_all 
```

Your package, `watchbox_0.9-1_all.deb`, is now ready in the `~/packages` folder.

</details>

