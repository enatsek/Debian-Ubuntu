##### Systemd 
# Basic Systemd Tutorial 
</details>

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. The What 

systemd is a suite of basic building blocks for a Linux system. It provides a system and service manager that runs as PID 1 and starts the rest of the system (from systemd.io).

systemd is a software suite that provides an array of system components for Linux operating systems (from Wikipedia).

systemd is an init system for Linux that replaces SysV init. Many distributions use it as their init system, including Debian, Ubuntu, and RHEL. However, several distributions do not use systemd, such as Slackware, Devuan, Alpine, and Gentoo.

A strong alternative to systemd is OpenRC.

### 0.2. Definitions

**D-Bus (Desktop Bus):** A message-oriented middleware mechanism that allows communication between multiple processes running concurrently on the same machine (from Wikipedia).

**cgroups (Control Groups):** A kernel feature that allows setting resource utilization limits for processes, such as CPU shares, memory usage, and block I/O per process. Originally developed by Google.

### 0.3. Sources
- [wiki.debian.org](https://wiki.debian.org/systemd/documentation)
- [www.digitalocean.com](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal)
- [www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
- [www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)
- [www.redhat.com](https://www.redhat.com/sysadmin/cgroups-part-one)
- [wikipedia.org](https://en.wikipedia.org/wiki/Systemd)
- [wikipedia.org](https://en.wikipedia.org/wiki/D-Bus)
- [access.redhat.com](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd)
- [www.howtogeek.com](https://www.howtogeek.com/675569/why-linuxs-systemd-is-still-divisive-after-all-these-years/)
- [systemd.io](https://systemd.io/)
- **The Debian Administrator’s Handbook** by Raphaël Hertzog and Roland Mas
- **Linux Service Management Made Easy with systemd** by Donald A. Tevault

<br>
</details>

<details markdown='1'>
<summary>
1. systemd Units
</summary>

---

Units are the resources that systemd knows how to manage and to operate.

### 1.1. Unit Locations

Unit files are located in the following directories (listed in increasing order of precedence):

- `/lib/systemd/system/`
- `/run/systemd/system/`
- `/etc/systemd/system/`


### 1.2. Unit Types:

- **`.service`**: Contains information for managing a service or application, including starting, stopping, automatic startup, and dependencies.
- **`.socket`**: Describes a socket for systemd's socket-based activation. Must have an associated `.service` file.
- **`.device`**: Describes a device that requires systemd management. Not all devices have a `.device` file.
- **`.mount`**: Describes mountpoints that need to be managed by systemd.
- **`.automount`**: Configures a mountpoint to be automatically mounted. Must have a corresponding `.mount` unit.
- **`.swap`**: Describes swap space on the system.
- **`.target`**: Used to synchronize with other units (similar to runlevels in SysV init).
- **`.path`**: Defines a path for path-based activation. A matching unit is started based on the path's existence or state.
- **`.timer`**: Defines a timer managed by systemd. A matching unit is started when the timer elapses.
- **`.snapshot`**: Created with the `systemctl snapshot` command. Saves the current system state but does not persist across reboots.
- **`.slice`**: Associated with cgroups (Linux Control Group nodes), allowing resource restrictions to be applied.
- **`.scope`**: Created automatically by systemd from information received via its bus interfaces. Manages sets of system processes created externally.

### 1.3. Example Unit Files

**Contents of `/lib/systemd/system/apache2.service`:**

```
[Unit]
Description=The Apache HTTP Server
After=network.target remote-fs.target nss-lookup.target
Documentation=https://httpd.apache.org/docs/2.4/

[Service]
Type=forking
Environment=APACHE_STARTED_BY_SYSTEMD=true
ExecStart=/usr/sbin/apachectl start
ExecStop=/usr/sbin/apachectl graceful-stop
ExecReload=/usr/sbin/apachectl graceful
KillMode=mixed
PrivateTmp=true
Restart=on-abort
OOMPolicy=continue

[Install]
WantedBy=multi-user.target
```

**Contents of `/lib/systemd/system/ssh.service`:**

```
[Unit]
Description=OpenBSD Secure Shell server
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target nss-user-lookup.target auditd.service
ConditionPathExists=!/etc/ssh/sshd_not_to_be_run

[Service]
EnvironmentFile=-/etc/default/ssh
ExecStartPre=/usr/sbin/sshd -t
ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
ExecReload=/usr/sbin/sshd -t
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure
RestartPreventExitStatus=255
Type=notify
RuntimeDirectory=sshd
RuntimeDirectoryMode=0755

[Install]
WantedBy=multi-user.target
Alias=sshd.service
```

**Contents of `/lib/systemd/system/ssh.socket`:**

```
[Unit]
Description=OpenBSD Secure Shell server socket
Before=sockets.target
ConditionPathExists=!/etc/ssh/sshd_not_to_be_run

[Socket]
ListenStream=22
Accept=no

[Install]
WantedBy=sockets.target
```

**Contents of `/etc/systemd/system/snap-firefox-2356.mount`:**

```
[Unit]
Description=Mount unit for firefox, revision 2356
After=snapd.mounts-pre.target
Before=snapd.mounts.target
Before=local-fs.target
[Mount]
What=/var/lib/snapd/snaps/firefox_2356.snap
Where=/snap/firefox/2356
Type=squashfs
Options=nodev,ro,x-gdu.hide,x-gvfs-hide
LazyUnmount=yes
[Install]
WantedBy=snapd.mounts.target
WantedBy=multi-user.target
```

### 1.4. Unit File Structure

Unit files consist of sections. The `[Unit]` and `[Install]` sections can exist in all unit types. Additional sections exist for specific unit types: `[Socket]`, `[Mount]`, `[Automount]`, `[Swap]`, `[Path]`, `[Timer]`, and `[Slice]`.

Sections contain directives, which can be general or specific to certain unit types.

For a complete list of directives, see:  
[https://www.freedesktop.org/software/systemd/man/systemd.directives.html](https://www.freedesktop.org/software/systemd/man/systemd.directives.html)

#### 1.4.1. [Unit] Section Directives (Applies to all unit types)

- **`Description`**: A brief description of the unit.
- **`Documentation`**: Location of documentation.
- **`Requires`**: Units this unit depends on. All must be activated for this unit to activate.
- **`Wants`**: Similar to `Requires` but less strict. Systemd attempts to activate listed units before this unit.
- **`BindsTo`**: Similar to `Requires`; also stops this unit when the listed unit stops.
- **`Before`**: This unit must start before listed units (does not imply dependency).
- **`After`**: Listed units must start before this unit (does not imply dependency).
- **`Conflicts`**: This unit cannot run simultaneously with listed units. Starting this unit stops others.
- **`Condition`**: Unit starts only if conditions are met; otherwise, it is skipped.
- **`Assert`**: Similar to `Condition`, but unmet conditions cause a failure.
- **`ConditionPathExists`**: Unit starts if the specified path exists. Prefix with `!` to negate.

#### 1.4.2. [Install] Section Directives (Applies to all unit types)

- **`WantedBy`**: Similar to the `Wants` directive; commonly used with targets.
- **`RequiredBy`**: Similar to `WantedBy` but stricter; failure occurs if dependency is unmet.
- **`Alias`**: Allows the unit to have an alias name (e.g., `ssh` for `sshd`).
- **`Also`**: Additional units to install/uninstall alongside this unit.
- **`DefaultInstance`**: Used only with template units; specifies the default instance name.

#### 1.4.3. [Service] Section Directives (Applies to service units)
- **`Type`**: Defines the service type:
    - **`simple`**: Systemd assumes the service starts immediately.
    - **`exec`**: Similar to `simple`, but systemd waits for the binary to execute.
    - **`forking`**: The service forks a child process and exits.
    - **`oneshot`**: The service runs briefly and exits.
    - **`dbus`**: The service acquires a name on the D-Bus.
    - **`notify`**: The service notifies systemd when startup is complete.
    - **`idle`**: The service runs only after all other jobs are dispatched.
- **`RemainAfterExit`**: Commonly used with `oneshot`; indicates the service remains active after the process exits.
- **`PIDFile`**: For `forking` type; specifies the file containing the child process PID.
- **`BusName`**: For `dbus` type; the D-Bus name to acquire.
- **`NotifyAccess`**: Controls which service status messages are notified (`main`, `exec`, or `none`).
- **`Environment`**: Environment variables to set.
- **`EnvironmentFile`**: File containing environment variables. Prefix with `-` to ignore if the file is missing.
- **`KillMode`**: How to stop the service: `process` (kill main process only), `mixed` (kill main and child processes), `none` (only run `ExecStop`).
- **`ExecStart`**: Command to start the service. Prefix with `-` to ignore failures.
- **`ExecStartPre`**: Commands to run before the main process.
- **`ExecStartPost`**: Commands to run after the main process starts.
- **`ExecReload`**: Command to reload the service.
- **`ExecStop`**: Command to stop the service.
- **`ExecStopPost`**: Commands to run after stopping the service.
- **`RestartSec`**: Time to wait before restarting.
- **`Restart`**: Conditions for automatic restart (`always`, `on-success`, `on-failure`, `on-abnormal`, `on-abort`, `on-watchdog`).
- **`RestartPreventExitStatus`**: Prevents restart if the specified exit code is received.
- **`RuntimeDirectory`**: Directory under `/run` for the service.
- **`RuntimeDirectoryMode`**: Permissions for the runtime directory (default: `0755`).
- **`TimeoutSec`**: Time to wait before marking start/stop as failed (or killing).
- **`TimeoutStartSec`**: Time to wait before marking start as failed.
- **`TimeoutStopSec`**: Time to wait before marking stop as failed.

#### 1.4.4. [Socket] Section Directives (Applies to socket units)

- **`ListenStream`**: Address to listen on for a TCP stream.
- **`ListenDatagram`**: Address to listen on for a UDP datagram.
- **`ListenSequentialPacket`**: Address to listen on for a Unix socket stream.
- **`ListenFIFO`**: Filesystem FIFO to listen on.
- **`Accept`**: If `yes`, a service instance is spawned for each connection; if `no`, all sockets are passed to the service unit.
- **`SocketUser`**: Unix username for the socket (default: `root`).
- **`SocketGroup`**: Unix group name for the socket (default: `root`).
- **`SocketMode`**: Filesystem permissions for the socket (default: `0666`).
- **`Service`**: Name of the connected service (if different from the socket name).

#### 1.4.5. [Mount] Section Directives (Applies to mount units)

- **`What`**: Path to mount.
- **`Where`**: Mountpoint path.
- **`Type`**: Filesystem type.
- **`Options`**: Comma-separated mount options.
- **`SloppyOptions`**: Boolean; if `true`, unrecognized mount options are ignored.
- **`DirectoryMode`**: Permissions for parent directories of the mountpoint.
- **`TimeoutSec`**: Time to wait before marking the operation as failed.

#### 1.4.6. [Automount] Section Directives (Applies to automount units)

- **`Where`**: Mountpoint path.
- **`DirectoryMode`**: Permissions for parent directories.

#### 1.4.7. [Swap] Section Directives (Applies to swap units)

- **`What`**: Path to the swap file or device.
- **`Priority`**: Swap priority (integer).
- **`Options`**: Comma-separated options for `/etc/fstab`.
- **`TimeoutSec`**: Time to wait before marking the operation as failed.

#### 1.4.8. [Path] Section Directives (Applies to path units)

- **`PathExists`**: Activates the associated unit if the path exists.
- **`PathExistsGlob`**: Similar to `PathExists` but supports glob patterns.
- **`PathChanged`**: Activates the unit when the file at the path is saved and closed.
- **`PathModified`**: Similar to `PathChanged` but also triggers on file modifications.
- **`DirectoryNotEmpty`**: Activates the unit if the specified directory is not empty.
- **`Unit`**: Name of the connected unit (if different from the path name).
- **`MakeDirectory`**: If `true`, creates directories before watching.
- **`DirectoryMode`**: Permissions for created directories (default: `0755`).

#### 1.4.9. [Timer] Section Directives (Applies to timer units)

- **`OnActiveSec`**: Activates the associated unit after this duration from timer activation.
- **`OnBootSec`**: Activates the unit after this duration from boot.
- **`OnStartupSec`**: Activates the unit after this duration from systemd startup.
- **`OnUnitActiveSec`**: Activates the unit after this duration from the last activation.
- **`OnUnitInactiveSec`**: Activates the unit after this duration from the last inactivation.
- **`OnCalendar`**: Absolute time to activate the unit.
- **`AccuracySec`**: Timer accuracy level.
- **`Unit`**: Name of the associated unit (if different from the timer name).
- **`Persistent`**: If `true`, stores the last trigger time on disk; triggers immediately if missed while inactive.

<br>
</details>

<details markdown='1'>
<summary>
2. Targets
</summary>

---
### 2.1. Definition and List

Targets are similar to SysV init runlevels. Their purpose is to group other systemd units through chains of dependencies.

A fresh Debian 13 server installation includes the following targets:

```
systemctl list-unit-files --type=target
```

```
UNIT FILE                     STATE    PRESET  
basic.target                  static   -       
blockdev@.target              static   -       
bluetooth.target              static   -       
boot-complete.target          static   -       
ctrl-alt-del.target           alias    -       
default.target                alias    -       
emergency.target              static   -       
exit.target                   disabled disabled
factory-reset.target          static   -       
final.target                  static   -       
first-boot-complete.target    static   -       
getty-pre.target              static   -       
getty.target                  static   -       
graphical.target              static   -       
halt.target                   disabled disabled
hibernate.target              static   -       
hybrid-sleep.target           static   -       
initrd-fs.target              static   -       
initrd-root-device.target     static   -       
initrd-root-fs.target         static   -       
initrd-switch-root.target     static   -       
initrd-usr-fs.target          static   -       
initrd.target                 static   -       
kexec.target                  disabled disabled
local-fs-pre.target           static   -       
local-fs.target               static   -       
multi-user.target             static   -       
network-online.target         static   -       
network-pre.target            static   -       
network.target                static   -       
nss-lookup.target             static   -       
nss-user-lookup.target        static   -       
paths.target                  static   -       
poweroff.target               disabled disabled
printer.target                static   -       
reboot.target                 disabled enabled 
remote-fs-pre.target          static   -       
remote-fs.target              enabled  enabled 
rescue-ssh.target             static   -       
rescue.target                 static   -       
rpcbind.target                static   -       
runlevel0.target              alias    -       
runlevel1.target              alias    -       
runlevel2.target              alias    -       
runlevel3.target              alias    -       
runlevel4.target              alias    -       
runlevel5.target              alias    -       
runlevel6.target              alias    -       
shutdown.target               static   -       
sigpwr.target                 static   -       
sleep.target                  static   -       
slices.target                 static   -       
smartcard.target              static   -       
sockets.target                static   -       
soft-reboot.target            static   -       
sound.target                  static   -       
ssh-access.target             static   -       
storage-target-mode.target    static   -       
suspend-then-hibernate.target static   -       
suspend.target                static   -       
swap.target                   static   -       
sysinit.target                static   -       
system-update-pre.target      static   -       
system-update.target          static   -       
time-set.target               static   -       
time-sync.target              static   -       
timers.target                 static   -       
tpm2.target                   static   -       
sigpwr.target                 static   -       
sleep.target                  static   -       
slices.target                 static   -       
smartcard.target              static   -       
sockets.target                static   -       
soft-reboot.target            static   -       
sound.target                  static   -       
ssh-access.target             static   -       
storage-target-mode.target    static   -       
suspend-then-hibernate.target static   -       
suspend.target                static   -       
swap.target                   static   -       
sysinit.target                static   -       
system-update-pre.target      static   -       
system-update.target          static   -       
time-set.target               static   -       
time-sync.target              static   -       
timers.target                 static   -       
tpm2.target                   static   -       
umount.target                 static   -       
usb-gadget.target             static   -   
```

Target configuration files are located in `/lib/systemd/system/`.

### 2.2. Example Target Files

**`network.target`:**

```
[Unit]
Description=Network
Documentation=man:systemd.special(7)
Documentation=https://systemd.io/NETWORK_ONLINE
After=network-pre.target
RefuseManualStart=yes
```

**`multi-user.target`:**

```
[Unit]
Description=Multi-User System
Documentation=man:systemd.special(7)
Requires=basic.target
Conflicts=rescue.service rescue.target
After=basic.target rescue.service rescue.target
AllowIsolate=yes
```

**`graphical.target`:**

```
[Unit]
Description=Graphical Interface
Documentation=man:systemd.special(7)
Requires=multi-user.target
Wants=display-manager.service
Conflicts=rescue.service rescue.target
After=multi-user.target rescue.service rescue.target display-manager.service
AllowIsolate=yes
```

<br>
</details>


<details markdown='1'>
<summary>
3. Unit Management: systemctl Command
</summary>

---

**Start a service:**

```
sudo systemctl start apache2.service
```

**Stop a service:**

```
sudo systemctl stop apache2.service
```

**Reload a service** (reloads configuration without restarting):

```
sudo systemctl reload apache2.service
```

**Restart a service:**

```
sudo systemctl restart apache2.service
```

**Reload if possible, otherwise restart:**

```
sudo systemctl reload-or-restart apache2.service
```

**Enable a service** (starts automatically at boot):

```
sudo systemctl enable apache2.service
```

**Disable a service** (does not start at boot):

```
sudo systemctl disable apache2.service
```

**Show status of a service:**

```
sudo systemctl status apache2.service
```

**Check if a service is active:**

```
systemctl is-active apache2.service
```

**Check if a service is enabled:**

```
systemctl is-enabled apache2.service
```

**Check if a service has failed:**

```
systemctl is-failed apache2.service
```

**Mask a service** (prevents it from being started, even manually):

```
sudo systemctl mask apache2.service
```

**Unmask a service:**

```
sudo systemctl unmask apache2.service
```

**List all active units:**

```
sudo systemctl list-units
```

**List all units** (including loaded and attempted):

```
sudo systemctl list-units --all
```

**List all installed unit files:**

```
sudo systemctl list-unit-files
```

**List services only:**

```
systemctl list-units --type=service
```

**View the contents of a unit file:**

```
systemctl cat apache2.service
```

**View dependencies of a unit:**

```
systemctl list-dependencies apache2.service
```

**View dependencies recursively:**

```
systemctl list-dependencies apache2.service --all
```

**View low-level details of a unit:**

```
systemctl show apache2.service
```

**Create an override or modify settings** (creates/edit a drop-in file):

```
sudo systemctl edit apache2.service
```

**Edit the entire unit file:**

```
sudo systemctl edit --full apache2.service
```

**Reload systemd** (after modifying unit files):

```
sudo systemctl daemon-reload
```

**Show the default target** (equivalent to runlevel):

```
systemctl get-default
```

**Set the default target:**

```
sudo systemctl set-default graphical.target
sudo systemctl set-default multi-user.target
```

**List available targets:**

```
systemctl list-unit-files --type=target
```

**List units associated with a target:**

```
systemctl list-dependencies multi-user.target
```

**Power off and reboot the system:**

```
sudo systemctl poweroff
sudo systemctl reboot
```

**Boot into rescue mode:**

```
sudo systemctl rescue
```

**Halt the system** (does not power off the machine):

```
sudo systemctl halt
```

**Control systemd on a remote system:**

```
systemctl --host user_name@host_name command
```

<br>
</details>

<details markdown='1'>
<summary>
4. Log Management: journalctl Command
</summary>

---

**View all log entries:**

```
journalctl
```

**View all log entries for the current boot:**

```
journalctl -b
```

**View only kernel entries:**

```
journalctl -k
```

**View only kernel entries for the current boot:**

```
journalctl -k -b
```

**View log entries for a specific unit (e.g., Apache):**

```
journalctl -u apache2.service
```

**View unit logs for the current boot:**

```
journalctl -b -u apache2.service
```

**View logs from the previous boot:**

```
journalctl -b -1
```

**View the list of the boots boots:**

```
journalctl --list-boots
```

**View logs within a time interval:**

```
journalctl --since "2023-01-10 17:15:00"
journalctl --since "2023-01-10" --until "2023-01-11 03:00"
journalctl --since yesterday
journalctl --since 09:00 --until "1 hour ago"
journalctl -u apache2.service --since today
```

**View log entries for a specific executable:**

```
journalctl /usr/bin/bash
```

**Output logs in JSON format:**

```
journalctl -b -u apache2 -o json
journalctl -b -u apache2 -o json-pretty
```

**Show the most recent 10 entries:**

```
journalctl -n
```

**Show the most recent 20 entries:**

```
journalctl -n 20
```

**Follow logs in real-time** (similar to `tail -f`; press Ctrl+C to exit):

```
journalctl -f
```

**Show disk usage of journal logs:**

```
journalctl --disk-usage
```

**Delete old logs to reduce size to a specified limit:**

```
sudo journalctl --vacuum-size=1G
```

**Delete logs older than a specified time:**

```
sudo journalctl --vacuum-time=1years
```

<br>
</details>

<details markdown='1'>
<summary>
5. Other systemd Components
</summary>

---

systemd includes several additional components. Some notable ones are:

- **systemd-boot**: A UEFI boot manager with basic configuration support. Integrates with `systemctl` and includes the `bootctl` command.

- **systemd-cat**: Adds records to the systemd journal via a pipeline.
  ```
  echo "Test" | systemd-cat -p info
  ```

- **systemd-localed**: Manages system locale settings. Controlled via the `localectl` command.

- **systemd-logind**: Manages user logins, tracks users and sessions, and handles device access for users.

- **systemd-machined**: Detects and monitors virtual machines and containers. Includes the `machinectl` command.

- **systemd-mount**: Manages `.mount` and `.automount` units.

- **systemd-networkd**: Handles network configuration. Configuration files are located in (in order of precedence):
    - `/lib/systemd/network`
    - `/run/systemd/network`
    - `/etc/systemd/network`

- **systemd-nspawn**: Runs commands or operating systems in lightweight namespace containers, similar to `chroot` in many respects.

- **systemd-resolved**: Provides network name resolution. Includes the `resolvectl` command.

- **systemd-sysusers**: Creates system users and groups.

- **systemd-timesyncd**: Synchronizes system time over the network with NTP servers. Includes the `timedatectl` command.

- **systemd-tmpfiles**: Manages volatile and temporary files and directories (creates, deletes, cleans up).

- **systemd-udevd**: Manages physical devices.

<br>
</details>

<details markdown='1'>
<summary>
6. Creating a Custom Service
</summary>

---

We will create a simple custom service that pings an IP address every 10 minutes. It logs an informational message if the ping succeeds, and an error message if it fails.

The service consists of a shell script placed in `/usr/local/bin`, a systemd unit file, and will be enabled, started, and tested.

### 6.1. Create the Shell Script

Create a script named `ipcheck.sh`:

```
nano ipcheck.sh
```

Add the following content:

```
#!/bin/bash
echo "ipcheck.service: Start. $(date)" | systemd-cat -p info
while true ; do
  ping -q -w 1 192.168.1.1 > /dev/null
  if [ $? = 0 ] ; then
     echo "ipcheck.service: Ping to IP is OK. $(date)" | systemd-cat -p info
  else
     echo "ipcheck.service: Error cannot ping IP. $(date)" | systemd-cat -p err
  fi
  sleep 600
done
```

### 6.2. Copy the Script to `/usr/local/bin`

Make the script executable and copy it:

```
chmod +x ipcheck.sh
sudo cp ipcheck.sh /usr/local/bin
```

### 6.3. Create the Unit File

Use `systemctl edit` to create the service unit:

```
sudo systemctl edit --force --full ipcheck.service
```

This command opens an editor. Add the following configuration:

```
[Unit]
Description=IPCheck Demo Service
Wants=network.target
After=syslog.target network-online.target

[Service]
ExecStart=/usr/local/bin/ipcheck.sh
Restart=on-failure
RestartSec=20
KillMode=process

[Install]
WantedBy=multi-user.target
```

Save and exit the editor.

### 6.4. Enable and Start The Service
```
sudo systemctl enable ipcheck.service
sudo systemctl start ipcheck.service
```

### 6.5. Test the Service

Check the recent logs to verify the service is working:

```
sudo journalctl -n 20
```

</details>
</summary>


