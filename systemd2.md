##### Systemd2 
# Other Systemd Components on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. The What

The first [Systemd tutorial](systemd.html) focused on systemd's init and service management capabilities.

However, systemd includes many more services and tools. This tutorial explores these additional components from a Debian and Ubuntu perspective.

You might think I like systemd. On the contrary—I don't like it; in fact, I dislike it. But since my preferred distributions (Debian and Ubuntu) use it, I've had to learn it as well.

### 0.2. Sources

For this tutorial, I tried a different approach. Instead of gathering information solely from the internet and books, I posed questions to ChatGPT and compiled the answers.

Unfortunately (or perhaps fortunately), ChatGPT provided a significant amount of incorrect information. I verified every answer before preparing this tutorial.

AI still requires considerable refinement before becoming truly reliable.

<br>
</details>

<details markdown='1'>
<summary>
1. Services
</summary>

---

Several important systemd services present in Debian 13 and/or Ubuntu 24.04 Server include:

- `systemd-journald`
- `systemd-logind`
- `systemd-networkd`
- `systemd-resolved`
- `systemd-timesyncd`
- `systemd-udevd`
- `systemd-tmpfiles`
- `systemd-binfmt`
- `systemd-modules-load`
- `systemd-random-seed`
- `systemd-remount-fs`
- `systemd-sysctl`
- `systemd-sysusers`

### 1.1. systemd-journald

Responsible for collecting, storing, and managing log data on Linux systems. It is the default logging system on systems using systemd, including Debian and Ubuntu.

#### 1.1.1. Key Points

- Stores log data in binary format.
- Logs are stored in the `/var/log/journal/` directory.
- Automatic log rotation and compression.
- Includes rate-limiting mechanisms to prevent log flooding in high-traffic scenarios.
- The `journalctl` command queries and displays log data managed by `systemd-journald`.
- Manages user-specific logs as well.


#### 1.1.2. Configuration

The configuration file is `/etc/systemd/journald.conf`.

**Example configuration:**

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

**Activate configuration changes:**

```
sudo systemctl restart systemd-journald
```


### 1.2. systemd-logind

Manages user sessions and seat devices on Linux systems. It handles user logins, seat management (logical grouping of input/output devices), and various aspects of the user environment.


#### 1.2.1. Key Points

- Tracks user sessions, associating processes with specific logins.
- Involved in power management; can inhibit shutdown or sleep.
- Provides information about active and inactive sessions.
- Integrates with desktop environments and display managers for better session and device control.

#### 1.2.2. Configuration

Configuration file: `/etc/systemd/logind.conf`.

**Example configuration:**

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

### 1.3. systemd-networkd

**Note:** This service is **not active by default** in Debian 13. Ubuntu uses Netplan as a frontend for `networkd`.

Manages network configurations on Linux systems, providing a simple and efficient way to configure wired and wireless interfaces.

#### 1.3.1. Key Points

- Configures link settings: IP addresses, gateways, DNS servers, etc.
- Supports bridges and VLANs.
- Integrates with `systemd-resolved` for DNS resolution.
- Can dynamically discover and configure network interfaces.

#### 1.3.2. Configuration

Relies on configuration files (with `.network` extension) in `/etc/systemd/network/`.

**Example: DHCP configuration**

```
# /etc/systemd/network/eth0.network
[Match]
Name=eth0

[Network]
DHCP=yes
```

**Example: Static IP configuration**

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
 
- **Address:** The static IP address and subnet mask.
- **Gateway:** The default gateway.
- **DNS:** DNS server addresses.
- **Domains:** Search domains for DNS resolution.
- **NTP:** NTP server for time synchronization.
- **MTUBytes:** Maximum Transmission Unit size.
- **MACAddressPolicy:** Set to persistent to use a stable MAC address.

#### 1.3.3. Important Notes

- Debian 13 does not use `systemd-networkd` by default.
- Ubuntu 24.04 uses Netplan, which generates `networkd` configuration files in `/run/systemd/network/`—these should not be edited directly.



### 1.4. systemd-resolved

**Note:** This service is **not active by default** in Debian 13.

Provides network name resolution services, acting as a local DNS stub resolver and caching daemon.

#### 1.4.1. Key Points

- Runs as a daemon process.
- Forwards DNS queries to upstream servers.
- Caches DNS responses locally.
- Supports Multicast DNS (mDNS) and DNS over TLS (DoT).
- Dynamically reconfigures based on network changes.
- Integrates with `systemd-networkd`.
- Managed via the `resolvectl` command.

#### 1.4.2. Configuration

Configuration file: `/etc/systemd/resolved.conf`.

**Example configuration:**

```
# /etc/systemd/resolved.conf
[Resolve]
DNS=8.8.8.8 8.8.4.4
DNSOverTLS=yes
DNSSEC=yes
```

**Detailed example configuration:**

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



### 1.5. systemd-timesyncd

Synchronizes the system clock across a network using NTP (Network Time Protocol).

#### 1.5.1. Key Points

- Runs as a service.
- Functions as a lightweight NTP client.
- The `timedatectl` command provides clock and synchronization status.

#### 1.5.2. Configuration

Configuration file: `/etc/systemd/timesyncd.conf`.

**Example configuration:**

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

**Detailed example configuration:**

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

### 1.6. systemd-udevd

Responsible for handling device events and managing device nodes in the Linux kernel's `/dev` directory. It is a dynamic device management daemon that monitors hardware changes and triggers actions based on device-related events.

#### 1.6.1. Key Points

- Monitors the Linux kernel's netlink interface for device events (e.g., new device discovery or removal).
- Dynamically manages device nodes in `/dev`.
- Uses a rule-based configuration system to define responses to specific device events.
- Supports persistent device naming based on attributes like MAC addresses or other unique identifiers.
- Maintains a device database at `/run/udev/data`.

#### 1.6.2. Configuration

Rules are defined in the `/etc/udev/rules.d/` directory. They can specify actions such as running scripts, creating symlinks, setting permissions, and more. Common event actions include `add`, `remove`, `change`, and `move`.

**Example rule** that runs a script when a USB drive with a specific vendor ID is inserted:

```
# /etc/udev/rules.d/80-custom-network.rules

# Rule for a USB drive with vendor ID 1234
SUBSYSTEM=="block", ACTION=="add", ENV{ID_VENDOR_ID}=="1234", RUN+="/path/to/custom-script.sh"
```
     
- `SUBSYSTEM=="block"`: Applies to block devices.
- `ACTION=="add"`: Triggers when a new block device is added.
- `ENV{ID_VENDOR_ID}=="1234"`: Matches vendor ID 1234.
- `RUN+="/path/to/custom-script.sh"`: Script to execute.

Rules can use various conditions and variables (e.g., `SUBSYSTEM`, `KERNEL`, `ID_VENDOR_ID`, `ID_MODEL_ID`) to match devices based on attributes.


### 1.7. systemd-tmpfiles

Responsible for managing temporary files and directories on a Linux system. It provides a mechanism for creating and cleaning up temporary files and directories at system startup and during runtime.


#### 1.7.1. Configuration

Configuration files are located in `/usr/lib/tmpfiles.d/` (system-provided) and `/etc/tmpfiles.d/` (user-defined).

**Configuration Format:**

```
[Type] Path Mode Age Argument
```

- **Type**: Operation type (`d`=directory, `f`=file, `D`=remove old files, `L`=symlink, etc.)
- **Path**: File or directory path
- **Mode**: Permissions (octal)
- **Age**: Retention period before removal
- **Argument**: Additional options

**Example configuration:**

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

#### 1.7.2. Examples

**Create a temporary directory at boot:**

```
# /etc/tmpfiles.d/my_temp_directory.conf

# Type 'd' indicates creating a directory
d /var/my_temp_directory 0755 root root -
```

**Create an empty file:**

```
# /etc/tmpfiles.d/my_temp_file.conf

# Type 'f' indicates creating an empty file
f /var/my_temp_file 0644 root root -
```

**Remove log files older than 7 days:**

```
# /etc/tmpfiles.d/remove_old_logs.conf

# Type 'D' indicates removing files older than a specified age
D /var/log/my_logs/*.log - - - 7d
```

**Create a symbolic link:**

```
# /etc/tmpfiles.d/create_symlink.conf

# Type 'L' indicates creating a symbolic link
L /var/my_symlink - /var/my_target_file
```

**Apply changes:**

```
sudo systemd-tmpfiles --create
```

### 1.8. systemd-binfmt

Responsible for handling binary formats (executable file formats) on the system. It works with the kernel's `binfmt_misc` mechanism to execute binaries in non-native formats using registered interpreters.

#### 1.8.1. Key Points

- Requires kernel support (`CONFIG_BINFMT_MISC`).
- Registers interpreters with the kernel for specific binary formats.
- Interpreters are programs that can execute binaries in those formats.


#### 1.8.2. Configuration

The configuration files are in /etc/binfmt.d/. 

Configuration files are in `/etc/binfmt.d/`. Each file defines rules for handling specific binary formats. This directory is empty by default on Debian 13 and Ubuntu 24.04.

**Example configuration:**

Configuration files follow a simple key-value format. Each rule defines the binary format and specifies the interpreter to use.

```
# /etc/binfmt.d/my_format.conf
#
:my_format:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x3e\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/my_interpreter:OC
```

**Manage binfmt rules:**

```
# Enable a rule
sudo systemctl enable binfmt@my_format.service

# Disable a rule
sudo systemctl disable binfmt@my_format.service

# Check status
systemctl status binfmt@my_format.service
```


### 1.9. systemd-modules-load

Responsible for loading kernel modules at system boot. It runs as a service (`systemd-modules-load.service`) and starts automatically during boot.

Configuration files are in `/etc/modules-load.d/`. Each line specifies a module name to load.

**Example:**

```
# /etc/modules-load.d/my_modules.conf

# Load the 'vboxdrv' module for VirtualBox
vboxdrv
```

**Note:** Debian and Ubuntu also traditionally support `/etc/modules`, but `systemd-modules-load` primarily uses `/etc/modules-load.d/`.




### 1.10. systemd-random-seed

Responsible for initializing the kernel's entropy pool with random data during system startup. The entropy pool is essential for generating cryptographic keys and ensuring randomness in cryptographic operations.

The primary purpose of systemd-random-seed is to initialize the kernel's  entropy pool during the early boot phase. 

#### 1.10.1. Key Points

- Reads random data from `/var/lib/systemd/random-seed` to seed the kernel's entropy pool.
- The seed file is created during shutdown and preserved across reboots.
- Random data is collected from various sources: interrupt timing, keyboard/mouse events, hardware noise, etc.
- The seed file is secured (owned by root, readable only by root).
- Operates during early boot to ensure the entropy pool is seeded before cryptographic services start.


### 1.11. systemd-remount-fs

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

**Note:** Changing the mount options with systemd-remount-fs can impact the behavior of the system during boot. For example, setting the root file system to be mounted read-only (ro) can be useful for checking and repairing the file system.




### 1.12. systemd-sysctl

Provides runtime configuration of kernel parameters via `sysctl`. It applies settings during boot to influence kernel behavior and performance.

Sysctl settings are used to configure various aspects of the Linux  kernel, influencing its behavior and performance.

The main configuration file is `/etc/sysctl.conf`, but custom settings are best placed in `/etc/sysctl.d/`.

**Example configuration:**

```
# /etc/sysctl.d/99-my-custom-settings.conf

# Increase the maximum number of file handles
fs.file-max=65536

# Enable TCP window scaling
net.ipv4.tcp_window_scaling=1

# Increase the maximum number of network connections
net.ipv4.ip_local_port_range=1024 65000
```
     
**Apply changes:**

```
sudo sysctl --system
```

**Note:** Default configurations are in `/usr/lib/sysctl.d/` and should not be modified, as they may be overwritten by package updates.



### 1.13. systemd-sysusers

**Note:** This service is **not active by default** in Debian 13.

Responsible for creating and managing system users and groups during early boot. It uses configuration files to define users, groups, their attributes, and removal instructions.

It operates based on configuration files that define the users and groups to be created, their attributes, and other related settings. This tool is often used in conjunction with other systemd components to ensure consistent and predictable user and group management.

Configuration files are in `/usr/lib/sysusers.d/` (system-provided) and `/etc/sysusers.d/` (user-defined).
Configuration files can also specify users and groups that should be removed.

This allows for cleaning up obsolete or unnecessary users and groups.

Attributes such as UID (User ID), GID (Group ID), home directory, shell, and user comment can be specified in the configuration files.

**Example configuration:**

```
# /etc/sysusers.d/my_users.conf

u johndoe - John Doe:/home/johndoe:/bin/bash
g mygroup - My Group
```

**Apply changes:**

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

### 2.1. systemctl

Used to control and query the state of the systemd system and service manager. It is the central tool for managing services, viewing logs, and interacting with the initialization system on systems using systemd.

**Check the status of a service:**

```
systemctl status apache2
```

**Stop a service:**

```
sudo systemctl stop apache2
```

**Start a service:**

```
sudo systemctl start apache2
```

**Disable a service from starting on boot:**

```
sudo systemctl disable apache2
```

**Enable a service to start on boot:**

```
sudo systemctl enable apache2
```

**Restart a service:**

```
sudo systemctl restart apache2
```

**Reload the configuration of a running service without restarting it:**

```
sudo systemctl reload apache2
```

**Show a service's dependencies:**

```
systemctl list-dependencies apache2
```

**List all loaded units (services, sockets, targets, etc.):**

```
systemctl list-units
```

**List failed units (units that failed to start):**

```
systemctl --failed
```

**Display detailed information about a unit, including its configuration:**

```
systemctl show apache2
```

**Mask a unit (prevent it from being started):**

```
sudo systemctl mask apache2
```

**Unmask a previously masked unit:**

```
sudo systemctl unmask apache2
```

**Enter rescue mode for system maintenance:**

```
sudo systemctl rescue
```

**Enter emergency mode for critical system recovery:**

```
sudo systemctl emergency
```
      
### 2.2. journalctl

Provides access to logs generated by the journal facility in the systemd system and service manager. On Debian and Ubuntu systems, `journalctl` is commonly used to query and display messages from the journal.

**View the entire journal:**

```
sudo journalctl
```

**View logs for a specific systemd unit:**

```
sudo journalctl -u apache2.service
```

**Filter by time:**

```
# Show logs from the last 30 minutes
sudo journalctl --since "30 minutes ago"

# Show logs from a specific date and time range
sudo journalctl --since "2025-01-01 08:00:00" --until "2025-01-01 12:00:00"
```

**Follow logs in real time (Ctrl+C to quit):**

```
sudo journalctl -f
```

**Display logs for the current boot:**

```
sudo journalctl --boot
```

**View kernel messages:**

```
sudo journalctl -k
```

**Export journal entries to a file:**

```
sudo journalctl > journal.log
```

**Change output format to JSON:**

```
sudo journalctl -o json
```

**Filter by priority level** (e.g., emerg, alert, crit, err, warning, notice, info,  debug):

```
sudo journalctl -p err
```

**View logs for a specific Process ID:**

```
sudo journalctl _PID=1234
```

**Clear the journal (e.g., limit to 50 MB):**

```
sudo journalctl --vacuum-size=50M
```

**Note:** Journal size is managed via `SystemMaxUse` and `RuntimeMaxUse` in `/etc/systemd/journald.conf`.


### 2.3. systemd-analyze

Used to analyze and display information about the system's boot and initialization process. It provides insights into boot duration, service timing, and other related metrics.

**Display basic boot time information:**

```
systemd-analyze
```

**Show the chain of units that took the most time during boot:**

```
systemd-analyze critical-chain
```

**List time taken by each service during boot (sorted by duration):**

```
systemd-analyze blame
```

**Generate an SVG plot of boot time per unit:**

```
systemd-analyze plot > plot.svg
```

**Display security-relevant information about the system's boot:**

```
systemd-analyze security
```

### 2.4. hostnamectl

Used for querying and changing the system hostname and related settings. It provides a convenient way to manage the hostname and view system information.

**Display current hostname and related settings:**

```
hostnamectl
```

**Set the static hostname (fully qualified domain name):**

```
sudo hostnamectl hostname your-new-hostname
```

**Set the transient hostname (temporary, does not persist after reboot):**

```
sudo hostnamectl hostname --transient your-temporary-hostname
```

**Set the pretty hostname (free-form descriptive string):**

```
sudo hostnamectl hostname --pretty "Your Pretty Hostname"
```

**Check hostname status:**

```
hostnamectl status
```

### 2.5. loginctl

Used for introspecting and interacting with the state of the systemd login manager. It provides information about user sessions, seats, and the user manager.


**List current user sessions:**

```
loginctl list-sessions
```

**List available seats:**

```
loginctl list-seats
```

**Display properties of a specific session:**

```
loginctl show-session SESSION_ID
```

**Display properties of a seat:**

```
loginctl show-seat SEAT_NAME
```

**Show information about a user manager:**

```
loginctl show-user USER_NAME
```

**List processes associated with a session:**

```
loginctl session-status SESSION_ID
```

**Terminate a user session:**

```
loginctl terminate-session SESSION_ID
```

**List user session IDs:**

```
loginctl list-users
```


### 2.6. localectl

Allows querying and changing system locale and keyboard layout settings. It provides a convenient way to manage and inspect locale-related configurations.

**Show current system locale settings:**

```
localectl
```

**List available locales:**

```
localectl list-locales
```

**Set the system locale:**

```
sudo localectl set-locale LANG=en_US.UTF-8
```

**Display a concise status summary:**

```
localectl status
```

### 2.7. systemd-ask-password

Used to securely query the user for authentication-related information, such as passwords or passphrases, in a standardized manner. It is often employed by systemd services that require interactive authentication during system boot or runtime.

- **Usage:** Typically invoked by other systemd components (e.g., `systemd-cryptsetup` for encrypted disk volumes) rather than directly by users.
- **Modes:** Supports various modes: console prompts, password agent communication, or wall messages.
- **Password Agents:** Can communicate with agents like `systemd-tty-ask-password-agent` for handling requests in non-interactive or headless environments.
- **Security:** Designed to handle password prompts securely, preventing inadvertent exposure of sensitive information.
- **Integration:** Part of workflows involving system initialization, encryption, or authentication.

**Common use cases:**

- Disk decryption during boot
- Encrypted home directory access
- Runtime authentication for services



### 2.8. systemd-cat

A command-line utility that concatenates and sends messages to the systemd journal (`systemd-journald`). It can capture command output and log it with specified priorities.

**Log a simple message:**

```
systemd-cat echo "Hello, systemd!"
```
   
**Capture command output with a specific priority:**

```
systemd-cat -p info ls /etc
```
   
**Log with error priority** The priority levels include "emerg," "alert," "crit," "err," "warning," "notice," "info," and "debug.":

```
systemd-cat -p err echo "An error occurred."
```
   
**Pipe script output to the journal:**

```
echo "Script is running." | systemd-cat
```
   
**Retrieve logged messages:**

```
journalctl _SYSTEMD_UNIT=echo.service
```



### 2.9. systemd-cgls

Lists and displays the hierarchy of control groups (cgroups). Cgroups are a Linux kernel feature for organizing processes into hierarchical groups with resource constraints and accounting.

**Display the cgroup hierarchy:**
```
systemd-cgls
```

**Example output (simplified):**

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

The tree structure shows parent-child relationships among cgroups, with indentation indicating hierarchy.

### 2.10. systemd-cgtop

Provides a real-time, dynamic view of resource usage by systemd control groups (cgroups). Similar to `top`, but focused on cgroup metrics.


**Monitor cgroup resource usage:**

```
sudo systemd-cgtop
```

**Display 5 updates and then exit:**

```
sudo systemd-cgtop -n 5
```


### 2.11. systemd-delta

Used to display the differences between configuration files provided by different packages and the runtime configuration of the system. It helps identify changes made to the default systemd configuration by administrators or other packages on the system.

When you run systemd-delta, it scans the system's configuration directories and compares the shipped configuration files from packages  with the runtime configuration on the system. It then displays the differences.

systemd-delta scans several directories for configuration files, including /etc/systemd/, /run/systemd/, and /usr/lib/systemd/.

Changes made by administrators are marked with +/ (additions) or ! (modifications). 

Changes made by packages are marked with +/ (additions) or -/ (deletions).

**List all changes to systemd configuration files:**

```
sudo systemd-delta
```
 
**Scan a specific directory for changes:**

```
sudo systemd-delta /etc/systemd/system/
```

**Output notation:**

- `+/`: Additions by administrators
- `!`: Modifications by administrators
- `+/` (package): Additions by packages
- `-/` (package): Deletions by packages

### 2.12. systemd-detect-virt

Used to detect the type of virtualization technology or hypervisor that a Linux system is currently running on. This can be useful in scripts or system initialization routines where the behavior might need to be adjusted based on whether the system is running on physical hardware or within a virtualized environment.

The command is typically used in shell scripts or systemd service files to conditionally execute specific actions based on the detected virtualization type.

**Detect virtualization type:**

```
systemd-detect-virt
```

**Common output values:**

- `qemu`: QEMU or KVM
- `kvm`: KVM (Kernel-based Virtual Machine)
- `vmware`: VMware
- `oracle`: Oracle VM VirtualBox
- `microsoft`: Microsoft Hyper-V
- `xen`: Xen
- `bochs`: Bochs
- `uml`: User-Mode Linux
- `parallels`: Parallels
- `none`: No virtualization detected

**Example script usage:**

```
if [ "$(systemd-detect-virt)" = "qemu" ]; then
  echo "Running on QEMU/KVM"
else
  echo "Not running on QEMU/KVM"
fi
```

**Exit codes:**

- `0`: Virtualization detected (type printed to stdout)
- `1`: No virtualization detected
- `2`: Invalid or missing arguments


### 2.13. systemd-escape

Escapes strings to make them suitable for use as filenames, unit names, or other identifiers in the systemd ecosystem. Replaces special characters with safe alternatives.

**Escape a string:**

```
systemd-escape "My Service"
```
   
**Output:**

```
My\x20Service
```

**Common transformations:**

- Spaces → `\x20`
- Slashes (`/`) → dashes (`-`)
- Other special characters → hexadecimal escape sequences

This ensures generated names are valid and safe for systemd units, files, and resources.



### 2.14. systemd-inhibit

Used to inhibit the system from performing certain actions or events for the duration of a specified command or until the command exits. This is useful for preventing actions that might interfere with critical operations like software installations, backups, or presentations.

**Command Syntax:**

```
systemd-inhibit [OPTIONS] COMMAND
```
     
**Common options:**

- `--what=EVENT`: Specifies the event to inhibit (e.g., `sleep`, `shutdown`, `idle`).
- `--why=REASON`: Provides a human-readable reason for the inhibition.
- `--mode=MODE`: Specifies the inhibition mode (`block`, `delay`, or `fail`).

**Example: Inhibit shutdown during a backup:**

```
sudo systemd-inhibit --what=shutdown --why="Backup in progress" \
    my_backup_script.sh
```

**Example: Inhibit sleep during a presentation:**

```
sudo  systemd-inhibit --what=sleep --why="Presentation in progress" \
    my_pres_command
```
     
**Inhibition modes:**

- `block`: Blocks the action until the command exits.
- `delay`: Delays the action until the command exits.
- `fail`: Fails the command if the action cannot be inhibited.


**List current inhibitions:**

```
systemd-inhibit --list
```
     
### 2.15. systemd-machine-id-setup

Used to initialize or regenerate the machine ID on a Linux system. The machine ID is a unique 32-character hexadecimal string stored in `/etc/machine-id` that identifies a specific OS installation.

**Key Points:**

- Generated automatically during first boot.
- Used by various system components and applications for identification.
- Should be regenerated when cloning system images to ensure uniqueness.

**Regenerate the machine ID:**

```
sudo systemd-machine-id-setup
```

**Note:** While `/etc/machine-id` can be edited manually, using this tool is recommended to avoid issues.



### 2.16. systemd-mount

Used for mounting and unmounting filesystems. It provides a convenient interface for mounting various filesystem types and network shares, integrating with systemd's service management.

**Mount an NFS share:**

```
sudo systemd-mount -t nfs server:/export /mnt/nfs
```
   
**Unmount a filesystem:**

```
sudo systemd-mount --umount /mnt/data
```

**Note:** Mounts managed by `systemd-mount` are associated with systemd mount units, offering additional control and configuration options.


### 2.17. systemd-notify

Allows a service or script to notify systemd about its status and readiness.

This tool is often used by long-running services to signal when they have completed initialization or specific milestones. It's a way for services to communicate with systemd and integrate with the overall service management infrastructure.

When a service uses systemd-notify, it sends signals to systemd, allowing  systemd to track the service's progress and readiness. This information is valuable for systemd's dependency tracking and ordering of services during startup.

**Example service unit configuration:**

```
[Service]
Type=simple
ExecStart=/path/to/myservice
ExecStartPost=/bin/systemd-notify --ready
```

**Key benefit:** Enables systemd to track service progress for dependency management and startup ordering.

### 2.18. systemd-path

Provides a way to query various system and user paths managed by systemd. It allows you to retrieve information about directories, files, and other paths that systemd uses or manages. This command is typically used for scripting or querying system information in a consistent manner.

**Print system and user paths:**

```
systemd-path 
```


### 2.19. systemd-run


Runs transient systemd services without requiring custom unit files. Ideal for testing, ad-hoc tasks, or short-lived processes.

**Basic usage:**

```
sudo systemd-run echo "Hello, systemd-run!"
```

**Capture output to journal:**

```
sudo systemd-run --pipe --collect echo "Capturing output in journal logs"
sudo journalctl -b -u transient-*.scope
```

**Set resource limits:**

This example sets a CPU time quota of 50% and a memory limit of 100 megabytes for the transient service.

```
sudo systemd-run --unit=my-service --service-type=exec --property=CPUQuota=50% \
   --property=MemoryLimit=100M -- /path/to/executable
```

**Run as a specific user:**

```
sudo systemd-run --uid=username --gid=groupname command-to-be-executed
```

**Run in background:**

This example uses --scope to create a transient service in the background and runs the sleep command for 300 seconds.

```
sudo systemd-run --scope --unit=my-background-service sleep 300
```

**Features:**

- No permanent unit files required
- Process isolation in separate scopes
- Automatic cleanup after completion
- Resource control via properties
 

### 2.20. systemd-socket-activate

Facilitates socket-based activation for services. Services are started on-demand when connections are made to specific network sockets, improving efficiency by delaying initialization until needed.

**How it works:**

1. A socket unit defines a network socket.
2. When a connection is made, systemd activates the associated service.
3. This replaces traditional always-running background services.


### 2.21. systemd-stdio-bridge

Acts as a bridge between standard input/output streams and a client-server architecture. It adapts traditional daemons (not designed for systemd) to work with socket activation.

**Purpose:**

- Allows non-systemd daemons to be socket-activated.
- Creates a bridge connecting the daemon's stdio to a socket.
- Enables communication between the daemon and clients via the socket.

**Typical use:** Adapting legacy daemons to integrate with systemd's socket activation mechanism.


</details>

