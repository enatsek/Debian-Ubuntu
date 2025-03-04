##### SystemdOnDebianUbuntu2 
# Other Systemd Components on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. Intro
The first Systemd tutorial, namely [SystemdOnDebianUbuntu](SystemdOnDebianUbuntu.html) was about systemd's init and service management properties.

Systemd has more than that, it has a lot of other services and tools. This tutorial covers them.

You may think that I like systemd. Not at all, I don't like it, more precisely I hate it. Just because, my favorite distros (Debian and Ubuntu) uses it, I have to learn it too.

### 0.2. Sources
For this tutorial I tried another approach. Instead of searching information from the internet and the books; I asked questions to ChatGPT and collected the answers.

Unfortunately (or maybe fortunately) there were a lot of wrong information from ChatGPP. I checked every answer before I prepare this tutorial.

The AI still needs a lot of work before becoming really useful.

<br>
</details>

<details markdown='1'>
<summary>
1. Services
</summary>

---
Debian 12 and Ubuntu 24.04 Server has the following systemd services by  default:

- systemd-journald
- systemd-logind
- systemd-networkd
- systemd-resolved
- systemd-timesyncd
- systemd-udevd
- systemd-tmpfiles
- systemd-binfmt
- systemd-modules-load
- systemd-random-seed
- systemd-remount-fs
- systemd-sysctl
- systemd-sysusers

## 1.1. systemd-journald
Responsible for  collecting, storing, and managing log data on Linux systems. 

It is the  default logging system on systems using systemd, including Debian and Ubuntu Linux distributions.

### 1.1.1. Logs
- Stores log data in binary format
- log data stored in the /var/log/journal/ directory. 
- Log files undergo automatic rotation and compression.
- Includes rate-limiting mechanisms to prevent logs from being flooded in high-traffic situations.
- The journalctl command is used to query and display log data managed by systemd-journald. 
- Manages user specific logs too.

### 1.1.2. Configuration
Configuration file is /etc/systemd/journald.conf file. 

```
# /etc/systemd/journald.conf

[Journal]
# Specify the maximum disk space that journal files may use.
# The default is infinity (i.e., unlimited).
SystemMaxUse=50M

# Specify the maximum disk space that should be used for runtime logs.
RuntimeMaxUse=50M

# Specify the maximum disk space that may be used for log data.
# This controls both system and runtime logs.
# The default is infinity (i.e., unlimited).
MaxUse=100M

# Specify the maximum number of individual journal files to retain.
# Older files are deleted when the limit is reached.
SystemMaxFiles=100

# Specify the maximum number of runtime journal files to retain.
# Older files are deleted when the limit is reached.
RuntimeMaxFiles=100

# Specify the maximum number of journal files to retain.
# This controls both system and runtime logs.
# Older files are deleted when the limit is reached.
MaxFiles=200

# Compress and store journal files in a read-only archive directory.
# Uncomment the line below and specify the archive directory path.
# This reduces the disk space usage but prevents further writes to the archived 
# logs.
# Also, consider setting "Storage=auto" if using this option.
# Compress=yes
# SystemKeepFree=50M
# RuntimeKeepFree=50M
# KeepFree=100M

# Specify a higher verbosity level for detailed log information.
# Options: "emerg", "alert", "crit", "err", "warning", "notice", "info", "debug".
# The default is "info".
# LogLevel=debug

# Specify the maximum runtime for system services to finish startup.
# This helps in capturing early boot logs completely.
# The default is 30s.
# RuntimeMaxSec=30s

# Enable persistent journal storage across reboots.
# The default is "auto".
# Storage=auto

# Disable persistent journal storage.
# Storage=none

# Specify the maximum size of individual journal files.
# The default is 8M.
# SystemMaxFileSize=16M
# RuntimeMaxFileSize=16M
# MaxFileSize=32M

# Specify the rate limit for journal events in bytes per second.
# The default is 1M.
# RateLimitBurst=2M
# RateLimitIntervalSec=30s

# Enable forwarding of journal logs to syslog.
# ForwardToSyslog=yes

# Specify the syslog identifier to use when forwarding logs.
# ForwardToSyslogIdentifier=journal
```

Activate the changed configuration:

```
sudo systemctl restart systemd-journald
```


## 1.2. systemd-logind
Manages user sessions and seat devices on Linux systems. 

It is responsible for handling user logins, seat management (logical grouping of input and output devices), and various aspects of the user environment.

### 1.2.1. Key Points
- Tracks user sessions, allowing the system to associate processes with specific user logins.
- Involved in power management tasks. Can apply inhibition of shutdown and sleep.
- Keeps track of user sessions and provides information about active and  inactive sessions.
- Integrates with desktop environments and display managers, allowing for better control over user sessions and seat devices.

### 1.2.2. Configuration
Configuration file: /etc/systemd/logind.conf file.

```
# /etc/systemd/logind.conf

[Login]
# This controls whether systemd-logind shall remove all sessions and seats
# on logout. This includes killing all processes in these sessions and
# stopping any session scope units that may be active. Note that enabling
# this setting may result in multiple sessions being created and removed
# on login and logout of a user.
#Default: yes
KillUserProcesses=yes

# ConsoleKit compatibility
# In addition to SessionsActivated, which can be used to check whether a
# user session is registered with systemd-logind, this switch enables
# basic ConsoleKit compatibility.
#Default: yes
ConsoleKitCompatibility=yes

# ReserveVT=N tells logind to leave N VTs unbound from it and do not
# release them from its VT pool. This option is only useful for embedded
# and appliance-like systems where the system console shall always be
# bound to VT number 1 or similar. In this case, set this to 1.
#Default: 6
ReserveVT=6

# Kill only user processes that are part of the same session as the
# service that is being terminated. Setting this to "yes" is equivalent
# to enabling KillUserProcesses=yes.
#Default: no
KillOnlyUsers=no

# Enable power management features when requested by a graphical session
# (with "HandlePowerKey=ignore" in logind.conf). This includes
# logind's inhibitors mechanism that is used to block system sleep/shutdown
# via inhibitors of running multimedia sessions.
#Default: yes
HandlePowerKey=yes

# HandleRebootKey and HandlePowerKey are not handled by logind when
# the caller is not root or a member of the group root. The user is expected
# to start "systemctl start shutdown.target", "systemctl start reboot.target"
# manually in the session.
# NOTE: PowerKey and RebootKey must be set to "ignore" to disable any
# handling, even if HandlePowerKey/HandleRebootKey is set to "yes".
HandleSuspendKey=yes
HandleHibernateKey=yes
HandleLidSwitch=yes

# Disable user switching
# Allow users who are logged in on one virtual terminal to switch to
# another one.
#Default: yes
#AllowUserSwitching=yes

# Enable user switching
#DisallowUserSwitching=no

# Handle displays that are attached to seats (such as graphics cards).
# If all seats are taken, users with displays attached to a seat are not
# allowed to log in.
#Default: yes
#Multiseat=no

# Handle automatic handling of display numbering, based on the seat and
# hardware ID of the graphics card. See "systemd-localed.service" for details.
#Default: no
#AutomaticVTSwitch=no

# Controls whether logind shall use ACLs and other mechanisms to control the
# access to the devices seats depend on. ACLs and other controls might add
# security, but may lead to problems when running certain setups (e.g.
# multiseat). Turn this off if you experience problems.
#Default: yes
#RestrictAccessToVT=yes
```

Activate the new conf

```
sudo systemctl restart systemd-logind
```



## 1.3. systemd-networkd
This service is not active in default Debian 12 installation.

Ubuntu installations use netplan as an interface to networkd.

Manages network  configurations on Linux systems. It is designed to provide a simple and  efficient way to configure and manage network interfaces, including wired and  wireless connections. 

### 1.3.1. Key Points
- Configures various link settings, including IP addresses, gateways, DNS  servers, and other network parameters.
- Supports the configuration of bridges and VLANs
- Integrates with systemd-resolved to provide DNS resolution services.
- Can dynamically discover and configure network interfaces.

### 1.3.2. Configuration
Relies on configuration files (with a .network extension) in the /etc/systemd/network/ directory. 

A simple systemd-networkd configuration file for DHCP

```
# /etc/systemd/network/eth0.network
[Match]
Name=eth0

[Network]
DHCP=yes
```

This configuration file tells systemd-networkd to apply the settings to the network interface named "eth0" and to use DHCP for IP configuration.

A detailed configuration with a static IP address, DNS settings, and  additional options for a more comprehensive configuration.

```
# /etc/systemd/network/20-wired.network
[Match]
Name=enp0s3

[Network]
Address=192.168.1.2/24
Gateway=192.168.1.1
DNS=8.8.8.8
DNS=8.8.4.4
Domains=mydomain.local
NTP=pool.ntp.org

[Link]
MTUBytes=1400
MACAddressPolicy=persistent
```
 
- Address: The static IP address and subnet mask.
- Gateway: The default gateway.
- DNS: DNS server addresses.
- Domains: Search domains for DNS resolution.
- NTP: NTP server for time synchronization.
- MTUBytes: Maximum Transmission Unit size.
- MACAddressPolicy: Set to persistent to use a stable MAC address.

### 1.3.3. Important Notes
Please remember that; Debian 12 does not use systemd-networkd; and Ubuntu 24.04 uses Netplan for network configuration. Netplan generates networkd  configuration files on /run/systemd/network directory; you are not supposed to change those files.



## 1.4. systemd-resolved
This service is not active in a default Debian 12 installation.

Provides network name resolution services on Linux systems. It is responsible for DNS resolution and provides a local DNS stub resolver and caching daemon. 

### 1.4.1. Key Points
- Runs as a daemon process.
- Acts as a local DNS stub resolver, which means it forwards DNS queries to DNS servers on behalf of client applications.
- Caches DNS responses locally to reduce the need for repeated DNS queries.
- Supports Multicast DNS (mDNS), allowing resolution of hostnames in the local network without relying on a dedicated DNS server.
- Can be configured to use DNS over TLS (DoT)
- Can dynamically reconfigure itself based on changes in network  configuration, such as changes in DNS server addresses or domain search lists.
- Often used in conjunction with systemd-networkd
- Integrates with the Name Service Switch (NSS) configuration
- resolvectl command is used to query and interact with systemd-resolved.

### 1.4.2. Configuration
The configuration file is /etc/systemd/resolved.conf.

Simple example configuration

```
# /etc/systemd/resolved.conf
[Resolve]
DNS=8.8.8.8 8.8.4.4
DNSOverTLS=yes
DNSSEC=yes
```

Detailed example configuration

```
# /etc/systemd/resolved.conf

[Resolve]
# Specify DNS servers to use for name resolution.
# Multiple servers can be separated by spaces.
# You can use IPv4 and IPv6 addresses.
# Example DNS settings for Google Public DNS:
# DNS=8.8.8.8 8.8.4.4
# DNS=2001:4860:4860::8888 2001:4860:4860::8844
 
# Enable DNS over TLS (DoT) for encrypted and authenticated communication with 
# DNS servers.
# This enhances the security and privacy of DNS queries.
# DNSOverTLS=yes
 
# Specify the DNSSEC (DNS Security Extensions) validation mode.
# Valid options: "allow-downgrade", "opportunistic", "require", and "no".
# DNSSEC=yes
 
# Enable DNSSEC negative trust anchors.
# DNSSECNegativeTrustAnchors=yes
 
# Specify the domains for which DNS queries should use DNS over TLS.
# Domains using DoT will not fall back to plaintext DNS.
# DNSOverTLSDomains=example.com test.net
 
# Specify the search domains for unqualified hostnames.
# Multiple domains can be separated by spaces.
# SearchDomains=example.com subdomain.example.net
 
# Specify the domains for which LLMNR (Link-Local Multicast Name Resolution) 
# should be used.
# LLMNR=yes
 
# Specify the multicast DNS (mDNS) domains.
# mDNS=yes
 
# Specify the time to live (TTL) for positive cache entries in seconds.
# CacheTTL=120
 
# Specify the TTL for negative cache entries in seconds.
# NegativeCacheTTL=120
 
# Specify the maximum size of the cache in kilobytes.
# CacheLimit=512M
 
# Specify the maximum number of DNS messages in transit.
# Messages max transit=4096
 
# Enable DNS fallback in case the resolved server cannot be contacted.
# FallbackDNS=8.8.8.8 8.8.4.4
 
# Enable caching DNS negative responses.
# CacheNegative=yes
 
# Enable automatic reconfiguration of resolved in response to network changes.
# DynamicUser=yes
```



## 1.5. systemd-timesyncd
Designed to synchronize the system clock across a network, ensuring accurate timekeeping on Linux systems. 

It acts as a simple NTP (Network Time Protocol) client, allowing your  system to regularly synchronize its clock with remote NTP servers.

### 1.5.1. Key Points
- Runs as a service.
- Functions as a lightweight NTP client, periodically querying remote NTP servers to obtain accurate time information.
- timedatectl command provides information about the system clock and its synchronization status.

### 1.5.2. Configuration
Example configuration:

```
# /etc/systemd/timesyncd.conf

[Time]
# Specify the NTP servers to use for time synchronization.
# Multiple servers can be specified, separated by spaces.
# Example NTP servers:
# NTP=pool.ntp.org time.google.com

# Specify the time to wait for the initial synchronization in seconds.
# The default is 1 minute.
# TimeoutStartSec=1min

# Specify the interval between updates.
# The default is 5 minutes.
# PollIntervalMinSec=5min

# Enable or disable systemd-timesyncd's NTP server.
# The default is "no".
# EnableNTP=yes

# Enable or disable setting the system clock from the RTC.
# The default is "yes".
# RTCUseUtc=yes
```

Detailed Example

```
# /etc/systemd/timesyncd.conf

[Time]
# Specify the NTP servers to use for time synchronization.
# Multiple servers can be specified, separated by spaces.
# Example NTP servers:
# NTP=pool.ntp.org time.google.com
NTP=pool.ntp.org

# Specify the time to wait for the initial synchronization in seconds.
# The default is 1 minute.
# TimeoutStartSec=1min

# Specify the interval between updates.
# The default is 5 minutes.
# PollIntervalMinSec=5min

# Enable or disable systemd-timesyncd's NTP server.
# The default is "no".
# EnableNTP=yes

# Enable or disable setting the system clock from the RTC.
# The default is "yes".
# RTCUseUtc=yes

# Specify the maximum allowed adjustment in seconds.
# If the difference between the system clock and the NTP server exceeds this 
# value, a larger step will be used to correct the time.
# The default is 0.2 seconds.
# MaxOffsetSec=1

# Specify the maximum acceptable root distance.
# This is the maximum possible error due to the network latency in seconds.
# The default is 5 seconds.
# RootDistanceMaxSec=5

# Specify the maximum acceptable polling interval for reaching out to NTP 
# servers.
# The default is 64 seconds.
# PollIntervalMaxSec=64

# Specify the minimum acceptable polling interval.
# The default is 32 seconds.
# PollIntervalMinSec=32
```


## 1.6. systemd-udevd
Responsible for handling device events and managing the device nodes in the Linux kernel's /dev directory. 

It is a dynamic device management daemon that  monitors hardware changes and triggers actions based on device-related events.

### 1.6.1. Key Points
- Monitors the Linux kernel's netlink interface for device-related events, such as the discovery of new devices or the removal of existing devices.
- Dynamically manages the device nodes in the /dev directory.
- Uses a rule-based configuration system to define how it should respond to specific device events. 
- Allows for persistent device naming based on attributes like MAC addresses or other unique identifiers.
- Maintains a device database (/run/udev/data) that stores device information.

### 1.6.2. Configuration
Rules are written in /etc/udev/rules.d/ directory. 

Rules can include actions such as running scripts, creating symlinks,  setting permissions, and more.

Rules specify actions to be taken for specific devices. Common actions  include "add," "remove," "change," and "move."

Rules can execute custom scripts or commands in response to events, allowing for fine-grained customization of device handling.

An example rule that runs a script when a USB drive with a specific vendor ID is inserted:

```
# /etc/udev/rules.d/80-custom-network.rules

# Rule for a USB drive with vendor ID 1234
SUBSYSTEM=="block", ACTION=="add", ENV{ID_VENDOR_ID}=="1234", RUN+="/path/to/custom-script.sh"
```
     
- SUBSYSTEM=="block": The rule applies to block devices.
- ACTION=="add": The rule triggers when a new block device is added.
- ENV{ID_VENDOR_ID}=="1234": Vendor ID should be 1234.
- RUN+="/path/to/custom-script.sh": The script to run

Various conditions can be used  to match devices based on attributes such as subsystem, kernel, device name, and more.

udev provides a set of variables that you can use in your rules. Like:  SUBSYSTEM, KERNEL, ID_VENDOR_ID, ID_MODEL_ID



## 1.7. systemd-tmpfiles
Responsible for managing temporary files and directories on a Linux  system. 

It provides a mechanism for creating and cleaning up temporary files and directories at system startup and during runtime. 

### 1.7.1. Configuration
Configuration files are in /usr/lib/tmpfiles.d/ and /etc/tmpfiles.d/  directories.

Configuration Format:  
[Type] Path Mode Age Argument

- Type: Specifies the type of operation (create, remove, modify).
- Path: Specifies the path to the file or directory.
- Mode: Specifies the permissions mode for the file or directory.
- Age: Specifies how long the file or directory should be retained before  removal.
- Argument: Additional arguments or options, depending on the type.

 Example configuration:

```
# /etc/tmpfiles.d/my_temporary_files.conf

# Create a directory with specific permissions
d /var/my_temp_dir 0755 root root -

# Create an empty file with specific permissions
f /var/my_temp_file 0644 root root -

# Remove files older than 7 days in a specific directory
D /var/log/my_logs/*.log - - - 7d
```

- d: Create a directory.
- f: Create an empty file.
- D: Remove files older than a specified age.
- F: Create file with contents
- L: Create symlink
- c: Create character device
- b: Create block device)

### 1.7.2. Examples
Create a temporary directory at boot.

```
# /etc/tmpfiles.d/my_temp_directory.conf

# Type 'd' indicates creating a directory
d /var/my_temp_directory 0755 root root -
```

- d: Specifies that a directory should be created.
- /var/my_temp_directory: Path to the directory.
- 0755: Permissions (owner: read, write, execute; group and others: read,  execute).
- root root: Specifies the owner and group.
- -: No specific age for removal.

Create an empty file with specific permissions.

```
# /etc/tmpfiles.d/my_temp_file.conf

# Type 'f' indicates creating an empty file
f /var/my_temp_file 0644 root root -
```

Remove log files older than 7 days:

```
# /etc/tmpfiles.d/remove_old_logs.conf

# Type 'D' indicates removing files older than a specified age
D /var/log/my_logs/*.log - - - 7d
```

Create a symbolic link:

```
# /etc/tmpfiles.d/create_symlink.conf

# Type 'L' indicates creating a symbolic link
L /var/my_symlink - /var/my_target_file
```

Apply the changes

```
sudo systemd-tmpfiles --create
```




## 1.8. systemd-binfmt
Responsible for handling binary formats. 

Binary formats are the different executable file formats that a system can support. 

### 1.8.1. Key Points
- binfmt_misc in the Linux kernel allows the execution of binaries in non- native formats. 

- Interpreters are programs that can execute binaries in specific formats. The systemd-binfmt service registers these interpreters with the kernel.

For binfmt_misc to work, the kernel must be compiled with support for  CONFIG_BINFMT_MISC.

### 1.8.2. Configuration
The configuration files are in /etc/binfmt.d/. 

Each configuration file defines rules for handling specific binary formats. This directory is empty at default Debian 12 and Ubuntu 24.04 installations.

Configuration files follow a simple key-value format. Each rule defines the binary format and specifies the interpreter to use.

```
# /etc/binfmt.d/my_format.conf
#
:my_format:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x3e\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/my_interpreter:OC
```

The last part of the configuration file specifies optional arguments for the interpreter. In the example, OC specifies that the interpreter should be called with the OC argument.

Enable a binfmt rule

```
sudo systemctl enable binfmt@my_format.service
```

Disable a binfmt rule

```
sudo systemctl disable binfmt@my_format.service
```

Check the status of binfmt rules

```
systemctl status binfmt@my_format.service
```


## 1.9. systemd-modules-load
Responsible for loading kernel modules at system boot. 

Runs as a service (systemd-modules-load.service) and is typically started automatically during system boot.

The configuration files are in /etc/modules-load.d/ directory. Files in /etc/modules-load.d/ specify which kernel modules should be loaded at boot  time. 

Syntax is simple: each line represents the name of a module to be loaded.

```
# /etc/modules-load.d/my_modules.conf

# Load the 'vboxdrv' module for VirtualBox
vboxdrv
```

In addition to using the /etc/modules-load.d/ directory, Debian and Ubuntu systems traditionally had an /etc/modules file where you could list modules to be loaded. This file is still supported, but systemd-modules-load primarily uses the /etc/modules-load.d/ directory.



## 1.10. systemd-random-seed
Responsible for initializing the kernel's entropy pool with random data during the system's startup. 

The entropy pool is essential for generating cryptographic keys and  ensuring the randomness of various cryptographic operations on a Linux system.

The primary purpose of systemd-random-seed is to initialize the kernel's  entropy pool during the early boot phase. 

The kernel maintains an entropy pool that serves as a source of randomness for cryptographic operations. Having a sufficient amount of entropy is crucial for the security of the system.

Reads random data from /var/lib/systemd/random-seed and uses it to seed the kernel's entropy pool during the system's startup. This file is typically created during the shutdown process and saved to preserve the entropy across reboots.

The random data used to seed the entropy pool is collected from various  sources, including interrupt timing, keyboard and mouse events, and other sources of hardware and environmental noise.

The seed file is restricted to ensure its security. It is owned by root and readable only by the root user.

systemd-random-seed operates during the early stages of the boot process, ensuring that the kernel's entropy pool is adequately seeded before cryptographic services and applications that rely on random data become active.


## 1.11. systemd-remount-fs
Responsible for remounting the root file system with specific mount options during the early boot process. 

This service is typically involved in adjusting the mount options for the root file system before other services are started, ensuring that the file system is mounted with the desired configuration.

Key aspects of systemd-remount-fs:

- The mount options applied by systemd-remount-fs are defined in the systemd configuration, specifically in the /etc/systemd/system.conf file.

- The /etc/systemd/system.conf file contains settings for the system manager, and it may include parameters related to the root file system's remounting.

```
# /etc/systemd/system.conf snippet:
[Manager]
# ...

DefaultTimeoutStartSec=10s
DefaultTimeoutStopSec=10s
DefaultRestartSec=10s
DefaultStartLimitIntervalSec=10s
DefaultStartLimitBurst=5
DefaultLimitNOFILE=4096
DefaultLimitNPROC=4096
# Set root file system mount options
DefaultMountOptions=ro
```

- Changing the mount options with systemd-remount-fs can impact the behavior of the system during boot. For example, setting the root file system to be mounted read-only (ro) can be useful for checking and repairing the file system.




## 1.12. systemd-sysctl
Provides a way to configure kernel parameters at runtime on Linux systems. It is a systemd service responsible for applying sysctl settings during the system's boot process. 

Sysctl settings are used to configure various aspects of the Linux  kernel, influencing its behavior and performance.

The main sysctl configuration file is /etc/sysctl.conf. It can be used to  set global sysctl settings. However, it is recommended to use the /etc/sysctl.d/ directory for custom configurations.

Example sysctl configuration file

```
# /etc/sysctl.d/99-my-custom-settings.conf

# Increase the maximum number of file handles
fs.file-max=65536

# Enable TCP window scaling
net.ipv4.tcp_window_scaling=1

# Increase the maximum number of network connections
net.ipv4.ip_local_port_range=1024 65000
```
     
Apply the changes:

```
sudo sysctl --system
```

The /usr/lib/sysctl.d/ directory contains default sysctl configuration files provided by packages. Files in this directory should not be modified, as changes may be overwritten during package updates.



## 1.13. systemd-sysusers
Responsible for creating and managing system users and groups during the early stages of system boot. 

It operates based on configuration files that define the users and groups to be created, their attributes, and other related settings. This tool is often used in conjunction with other systemd components to ensure consistent and predictable user and group management.

Configuration files are in /usr/lib/sysusers.d/ directory. Each file  contains instructions for creating or removing system users and groups.

Configuration files can also specify users and groups that should be removed.

This allows for cleaning up obsolete or unnecessary users and groups.

Attributes such as UID (User ID), GID (Group ID), home directory, shell, and user comment can be specified in the configuration files.

Example configuration file

```
# /etc/sysusers.d/my_users.conf

u johndoe - John Doe:/home/johndoe:/bin/bash
g mygroup - My Group
```

Applying Changes:

```
sudo systemd-sysusers
```

<br>
</details>

<details markdown='1'>
<summary>
2. Tools
</summary>

---
## 2.1. systemctl
Used to control and query the state of the systemd system and service manager. 

It is a central tool for managing services, viewing logs, and interacting with the initialization system on systems using systemd as the init system. 

Check the status of a service:

```
systemctl status apache2
```

Stop a service:

```
sudo systemctl stop apache2
```

Start a service:

```
sudo systemctl start apache2
```

Disable a service from starting on boot:

```
sudo systemctl disable apache2
```

Enable a service to start on boot:

```
sudo systemctl enable apache2
```

Restart a service:

```
sudo systemctl restart apache2
```

Reload the configuration of a running service without restarting it:

```
sudo systemctl reload apache2
```

Show a service's dependencies:

```
systemctl list-dependencies apache2
```

List all loaded units (services, sockets, targets, etc.):

```
systemctl list-units
```

List failed units (units that failed to start):

```
systemctl --failed
```

Display detailed information about a unit, including its configuration:

```
systemctl show apache2
```

Mask a unit (prevent it from being started):

```
sudo systemctl mask apache2
```

Unmask a previously masked unit:

```
sudo systemctl unmask apache2
```

Enter rescue mode for system maintenance:

```
sudo systemctl rescue
```

Enter emergency mode for critical system recovery:

```
sudo systemctl emergency
```
      
## 2.2. journalctl
Provides access to the logs  generated by the journal facility in the systemd system and service manager.

On Debian and Ubuntu systems, journalctl is commonly used to query and display messages from the journal.

View the journal

```
sudo journalctl
```

View the journal for a systemd unit or target

```
sudo journalctl -u apache2.service
```

Filtering by time.   
Show logs from the last 30 minutes

```
sudo journalctl --since "30 minutes ago"
```

Show logs from a specific date and time range

```
sudo journalctl --since "2024-01-01 08:00:00" --until "2024-01-01 12:00:00"
```

See live journal (Ctrl-C to quit)

```
sudo journalctl -f
```

Display logs for the current boot

```
sudo journalctl --boot
```

View kernel messages

```
sudo journalctl -k
```

Export journal entries to a file

```
sudo journalctl > journal.log
```

Change output format to Json

```
sudo journalctl -o json
```

Filter by priority (e.g., emerg, alert, crit, err, warning, notice, info,  debug).

```
sudo journalctl -p err
```

View logs for a specific Process ID

```
sudo journalctl _PID=1234
```

Clear the journal

```
sudo journalctl --vacuum-size=50M
```

The size of the journal can be managed through the SystemMaxUse and  RuntimeMaxUse options in the /etc/systemd/journald.conf configuration file.


## 2.3. systemd-analyze
Used to analyze and display information about the system's boot and initialization process. It provides insights into how long the system took to boot, the time spent by individual services, and other related information.

Basic Boot Time Information

```
systemd-analyze
```

Display the chain of units that took the most time during boot.

```
systemd-analyze critical-chain
```

Show the time taken by each service during boot, sorted by the time taken.

```
systemd-analyze blame
```

Generate a SVG plot of the time spent by each unit during boot.

```
systemd-analyze plot > plot.svg
```

Display security-relevant information about the system's boot.

```
systemd-analyze security
```

Create a detailed graphical representation of time usage for different units.

```
systemd-analyze plot > plot.svg
```

## 2.4. hostnamectl
Used for querying and changing the system hostname and related settings on Linux systems. It provides a convenient way to manage the system's hostname and view additional information about the system.

Display information about the system's hostname and related settings

```
hostnamectl
```

This command provides information such as the static hostname, transient  hostname, icon name, chassis type, and more.

Set the static hostname (the system's fully qualified domain name)

```
sudo hostnamectl set-hostname your-new-hostname
```

Set the transient hostname. The transient hostname is a runtime hostname  that is set temporarily and may not persist after a reboot.

```
sudo hostnamectl set-hostname --transient your-temporary-hostname
```

Set the pretty hostname. The pretty hostname is a free-form UTF-8 encoded  string describing the host.

```
sudo hostnamectl set-hostname --pretty "Your Pretty Hostname"
```

Check hostname status.

```
hostnamectl status
```

## 2.5. loginctl
Used for introspecting and interacting with the state of the systemd login manager. 

It provides information about user sessions, seats, and the status of the 
user manager. 

**Some common uses of the loginctl command:**

Display a list of current user sessions

```
loginctl list-sessions
```

Display a list of seats

```
loginctl list-seats
```

Displaying session properties

```
loginctl show-session SESSION_ID
```

Displaying seat properties

```
loginctl show-seat SEAT_NAME
```

Show information about the user manager

```
loginctl show-user USER_NAME
```

Display a list of processes associated with a specific session:

```
loginctl session-status SESSION_ID
```

Terminate a specific user session:

```
loginctl terminate-session SESSION_ID
```

Display a list of user session IDs:

```
loginctl list-users
```


## 2.6. localectl
Allows to query and change system locale and keyboard layout settings. It provides a convenient way to manage and inspect the system's locale-related configurations.

Show the current system locale settings.

```
localectl
```

Show a list of available locales that can be set on the system.

```
localectl list-locales
```

Set the system locale.

```
sudo localectl set-locale LANG=en_US.UTF-8
```

Display a concise status summary, including locale and keyboard layout  information.

```
localectl status
```
 
## 2.7. systemd-ask-password
Used for querying the user for authentication-related information, such as passwords or passphrases, in a secure and standardized way. It is often used in conjunction with various systemd services or components that may need to request passwords during the system boot process or at runtime.

Some key aspects of systemd-ask-password:

**Usage:** The command is typically used by other systemd components or services to request passwords interactively.

**Invocation:** systemd-ask-password is usually invoked by other systemd components or services and may not be used directly by users from the command line.

**Systemd Components Using systemd-ask-password:** Components like  systemd-cryptsetup, which handles encrypted disk volumes, or services requiring authentication during boot, may use systemd-ask-password to prompt the user for passwords in a secure manner.

**Modes:** systemd-ask-password supports different modes of operation, such as prompting the user on the console, querying a password agent, or sending the password request to a wall message.

**Password Agents:** In some cases, systemd-ask-password may communicate with a password agent, such as systemd-tty-ask-password-agent, to handle password requests. This allows for a more flexible and secure way of handling passwords, especially in non-interactive or headless environments.

**Communication:** Communication between systemd-ask-password and password agents is done through file descriptors, ensuring a secure and reliable means of passing sensitive information.

**Security:** systemd-ask-password is designed to handle password prompts securely, ensuring that passwords are not inadvertently leaked or exposed  during the authentication process.

**Wall Message:** The --wall option can be used to send a wall message (broadcast message to all users) requesting a password.

```
systemd-ask-password --wall "Please enter the encryption password:"
```
   
This might be used by services like disk decryption to inform users about the need for a password.

**Integration with Other Tools:** systemd-ask-password is often part of a larger workflow involving other systemd tools and services, especially those related to system initialization, encryption, or authentication.

**Examples of Use:**  
- Password requests during disk decryption.
- Password requests for encrypted home directories.
- Authentication requests for services during runtime.



## 2.8. systemd-cat
systemd-cat is a command-line utility that is part of the systemd suite. Its primary purpose is to concatenate and print messages to the journal, which is managed by systemd-journald. 

Can be used as a prefix to other commands or scripts to capture their  output and send it to the journal.

```
systemd-cat echo "Hello, systemd!"
```
   
Redirect the standard output and standard error of a command or script to the journal.

```
systemd-cat -p info ls /etc
```
   
Set message priority. The priority levels include "emerg," "alert," "crit," "err," "warning," "notice," "info," and "debug."

```
systemd-cat -p err echo "An error occurred."
```
   
Logging from scripts

```
echo "Script is running." | systemd-cat
```
   
you can use journalctl to retrieve and filter these messages.

```
journalctl _SYSTEMD_UNIT=echo.service
```



## 2.9. systemd-cgls
Used for listing and displaying the hierarchy of control groups (cgroups). 

Control groups are a feature of the Linux kernel that enables the organization and management of processes into hierarchical groups with  resource constraints and accounting.

systemd-cgls is primarily used to visualize the hierarchy of control groups and their relationships. It provides a tree-like representation of the cgroup hierarchy.

```
systemd-cgls
```

The output of systemd-cgls shows the control groups arranged in a tree structure, indicating the parent-child relationships. Each line represents a cgroup, and indentation indicates the hierarchy.

Example simplified output:


```
 └─user.slice
   ├─user-1000.slice
   │ ├─session-c1.scope
   │ │ └─1337 sshd: johndoe@pts/0
   │ └─session-c2.scope
   │   ├─1445 bash
   │   ├─1452 systemd-cgls
   │   └─1453 less
   └─user-2000.slice
 └─session-c3.scope
   └─1555 sshd: janedoe@pts/1
```

## 2.10. systemd-cgtop
Provides a real-time, dynamic view of the resource usage of systemd control groups (cgroups) on a Linux system. 

Run `systemd-cgtop` with default settings:

```
sudo systemd-cgtop
```

This will display real-time statistics for all control groups.

Quits displaying after 5 updates.

```
sudo systemd-cgtop -n 5
```

Display tree view

```
sudo systemd-cgtop -t
```


## 2.11. systemd-delta
Used to display the differences between configuration files provided by different packages and the runtime configuration of the system. It helps identify changes made to the default systemd configuration by administrators or other packages on the system.

When you run systemd-delta, it scans the system's configuration directories and compares the shipped configuration files from packages  with the runtime configuration on the system. It then displays the differences.

systemd-delta scans several directories for configuration files, including /etc/systemd/, /run/systemd/, and /usr/lib/systemd/.

Changes made by administrators are marked with +/ (additions) or ! (modifications). 

Changes made by packages are marked with +/ (additions) or -/ (deletions).

List all changes made to systemd unit files and configuration files:

```
sudo systemd-delta
```
 
Display changes in a specific directory (e.g., `/etc/systemd/system/`):

```
sudo systemd-delta /etc/systemd/system/
```

## 2.12. systemd-detect-virt
Used to detect the type of virtualization technology or hypervisor that a Linux system is currently running on. This can be useful in scripts or system initialization routines where the behavior might need to be adjusted based on whether the system is running on physical hardware or within a virtualized environment.

The command is typically used in shell scripts or systemd service files to conditionally execute specific actions based on the detected virtualization type.

```
systemd-detect-virt
```

The command outputs the detected virtualization type or "none" if no  virtualization is detected.

**qemu:** QEMU or KVM  
**kvm:** KVM (Kernel-based Virtual Machine)  
**vmware:** VMware  
**oracle:** Oracle VM VirtualBox  
**microsoft:** Microsoft Hyper-V  
**xen:** Xen  
**bochs:** Bochs  
**uml:** User-Mode Linux  
**parallels:** Parallels


Using systemd-detect-virt in a script

```
if [ "$(systemd-detect-virt)" = "qemu" ]; then
  echo "Running on QEMU/KVM"
else
  echo "Not running on QEMU/KVM"
fi
```

**Exit Codes:**

0: Detected virtualization. The detected virtualization type will be printed to stdout.
1: No virtualization detected.
2: Invalid or missing arguments.


## 2.13. systemd-escape
Used to escape strings, making them suitable for use as filenames, unit  names, or other identifiers in the systemd ecosystem. This is particularly useful for generating valid and safe names for systemd units, files, and other resources.

Escapes special characters in the input string, replacing them with safe alternatives. For example, slashes ("/") might be replaced with dashes ("-").

```
systemd-escape "My Service"
```
   
Output:

```
My\x20Service
```


## 2.14. systemd-inhibit
Used to inhibit the system from certain actions or events for the duration of a specified command or until the command exits. This is useful for preventing actions that might interfere with a running operation or task. 

The command is commonly employed to avoid disruptions during critical  processes like software installations, backups, or presentations.

Command Syntax

```
systemd-inhibit [OPTIONS] COMMAND
```
     
Various options can be used to specify the actions to be inhibited and other properties. Some common options include:

- --what=EVENT: Specifies the event to inhibit (e.g., sleep, shutdown).
- --why=REASON: Provides a human-readable reason for the inhibition.
- --mode=MODE: Specifies the inhibition mode (e.g., block, delay, fail).

**Example Usage:**  
Inhibit shutdown while a backup operation is in progress:

```
sudo systemd-inhibit --what=shutdown --why="Backup in progress" \
    my_backup_script.sh
```

Inhibit sleep while a presentation is running:

```
sudo  systemd-inhibit --what=sleep --why="Presentation in progress" \
    my_pres_command
```
     
Inhibition Modes:

**block:** Blocks the action until the command exits.  
**delay:** Delays the action until the command exits.  
**fail:** Fails the command if the action cannot be inhibited.

List current inhibitions

```
systemd-inhibit --list
```
     
## 2.15. systemd-machine-id-setup
Used to initialize or regenerate the machine ID on a Linux system. 

The machine ID is a unique identifier associated with a specific installation of an operating system. It is often used by various system components and applications to distinguish between different systems.

The machine ID is stored in the /etc/machine-id file. It is a 32-character hexadecimal string that uniquely identifies the system. Applications and services often use the machine ID for various purposes, such as generating unique identifiers or ensuring system-specific configurations.

During the first boot of a Linux system, systemd-machine-id-setup is  typically called to generate a random machine ID and store it in  /etc/machine-id.

If, for any reason, the machine ID needs to be regenerated (for example, in the case of system cloning or copying an installation), administrators can run systemd-machine-id-setup to create a new machine ID.

```
sudo systemd-machine-id-setup
```

This command generates a new machine ID and updates the /etc/machine-id file.

In scenarios where system images are cloned or deployed to multiple machines, it's essential to regenerate the machine ID on each cloned system using systemd-machine-id-setup to ensure uniqueness.

While systemd-machine-id-setup is the recommended way to manage the machine ID, the /etc/machine-id file can also be edited manually. However, it's generally advised to use the provided tools to avoid potential issues.



## 2.16. systemd-mount
Used for mounting and unmounting file systems. It provides a convenient  interface to mount and manage various types of filesystems and network shares.

The utility is designed to work with systemd's broader system and service management capabilities.

Can be used to mount network file systems like NFS or SMB.

```
sudo systemd-mount -t nfs server:/export /mnt/nfs
```
   
To unmount a filesystem, use the --umount option.

```
sudo systemd-mount --umount /mnt/data
```

Mounts managed by systemd-mount are often associated with systemd mount units, providing additional control and configuration options.



## 2.17. systemd-notify
Allows a service or script to notify systemd about its status and readiness.

This tool is often used by long-running services to signal when they have completed initialization or specific milestones. It's a way for services to communicate with systemd and integrate with the overall service management infrastructure.

When a service uses systemd-notify, it sends signals to systemd, allowing  systemd to track the service's progress and readiness. This information is valuable for systemd's dependency tracking and ordering of services during startup.

Example in a Service Unit:

```
[Service]
Type=simple
ExecStart=/path/to/myservice
ExecStartPost=/bin/systemd-notify --ready
```

In this example, myservice is expected to call systemd-notify --ready after it has completed its initialization.


## 2.18. systemd-path
Provides a way to query various system and user paths managed by systemd. It allows you to retrieve information about directories, files, and other paths that systemd uses or manages. This command is typically used for scripting or querying system information in a consistent manner.

Print the system and users path 

```
systemd-path 
```


## 2.19. systemd-run
Allows users to run transient systemd services and service units. It provides a simple way to create and manage temporary or one-shot services without the need to write custom unit files. This can be useful for testing, ad-hoc tasks, or running short-lived processes.

Unlike traditional systemd services, using systemd-run does not require  writing and managing unit files. Instead, the user provides the command to be executed directly on the command line.

Transient units created by systemd-run are isolated from the calling terminal, and they run in their own scope. This helps prevent interference with other services or processes.

Transient services created by systemd-run can be of different types, such as simple services (--service-type=simple), forking services (--service-type=forking), or executed directly (--service-type=exec).

Once the transient service completes, systemd-run provides information about the service's exit status, runtime, and resource usage.

Transient services created by systemd-run are automatically cleaned up once the service completes, making it suitable for short-lived tasks.

Execute the echo command within a transient service.

```
sudo systemd-run echo "Hello, systemd-run!"
```

This example uses the --pipe option to capture the output, and --collect to ensure that the transient service's logs are collected and stored.

```
sudo systemd-run --pipe --collect echo "Capturing output in journal logs"
sudo journalctl -b -u transient-*.scope
```

This example sets a CPU time quota of 50% and a memory limit of 100 megabytes for the transient service.

```
sudo systemd-run --unit=my-service --service-type=exec --property=CPUQuota=50% \
   --property=MemoryLimit=100M -- /path/to/executable
```

Run a command as a specific user:

```
sudo systemd-run --uid=username --gid=groupname command-to-be-executed
```

This example uses --scope to create a transient service in the background and runs the sleep command for 300 seconds.

```
sudo systemd-run --scope --unit=my-background-service sleep 300
```

 
## 2.20. systemd-socket-activate
Facilitates socket-based activation for services. 

Socket activation is a mechanism that allows services to be started on-demand when a connection is made to a specific network socket. This approach helps improve system efficiency by delaying the initialization of services until they are actually needed.

Socket activation is an alternative to the traditional method of starting  services at boot time. Instead of having services running continuously in the background, services are started dynamically when a connection is made to a specific socket.

In systemd, a socket unit is defined to represent a network socket. When a connection is made to this socket, systemd activates the associated service.


## 2.21. systemd-stdio-bridge
Designed to act as a bridge between standard input/output streams and a client-server architecture. It facilitates communication between a traditional (non-systemd) daemon that expects input/output on standard input/output and a systemd service that runs in a separate process.

It is used to adapt daemons that are not originally designed to work with systemd socket activation. It allows these daemons to be socket-activated by systemd.

When a daemon is adapted to use systemd-stdio-bridge, systemd creates a socket for the daemon and starts systemd-stdio-bridge as a separate process. The bridge connects the standard input/output of the daemon to the socket, allowing it to communicate with clients through the socket.

</details>

