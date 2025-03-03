##### SystemdOnDebianUbuntu 
# systemd Tutorial On Debian and Ubuntu
</details>

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.0. Intro 
systemd is a suite of basic building blocks for a Linux system. It  provides a system and service manager that runs as PID 1 and starts the  rest of the system (from systemd.io site).

systemd is a software suite that provides an array of system components  for Linux operating systems (from wikipedia).

systemd is an init system for Linux. It replaces SysV init. There are a  lot of distros that use it as an init system, like Debian, Ubuntu, RHEL.  Also there are a lot of distros that don't use systemd, like Slackware,  Devuan, Alpine, Gentoo.

A strong alternative of systemd is OpenRC.

### 0.1. Definitions
**D-Bus (Desktop Bus)**:  A message-oriented middleware mechanism that  allows communication between multiple processes running concurrently on  the same machine (from wikipedia).

**cgroups**: A part built into kernel, that allows setting resource  utilization limits for processes. Like; cpu shares, memory usage, block  I/O per process. Developed by Google.

### 0.2. Sources
[wiki.debian.org](https://wiki.debian.org/systemd/documentation)  
[www.digitalocean.com](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal)  
[www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)  
[www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)  
[www.redhat.com](https://www.redhat.com/sysadmin/cgroups-part-one)  
[wikipedia.org](https://en.wikipedia.org/wiki/Systemd)  
[wikipedia.org](https://en.wikipedia.org/wiki/D-Bus)  
[access.redhat.com](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd)  
[www.howtogeek.com](https://www.howtogeek.com/675569/why-linuxs-systemd-is-still-divisive-after-all-these-years/)    
[systemd.io](https://systemd.io/)  
**The Debian Administrator’s Handbook** by Raphaël Hertzog and Roland Mas  
**Linux Service Management Made Easy with systemd** by Donald A. Tevault

<br>
</details>

<details markdown='1'>
<summary>
1. systemd Units
</summary>
---
Units are the resources that systemd knows how to manage and to operate.

### 1.1. Unit Locations
Locations of unit files (in increasing precedence):

- /lib/systemd/system
- /run/systemd/system
- /etc/systemd/system

### 1.2. Unit Types:
**.service**: Contains information on managing a service or application.  Managing includes starting, stopping, automatic starting, dependencies  etc.

**.socket**: Describes a socket for systemd's socket based activation. It  must have an associated .service file for a service.

**.device**: Describes a device that needs systemd management. Not all  devices has a .device file.

**.mount**: Mountpoints needed to be managed by systemd.

**.automount**: Configures a mountpoint to be automatically mounted. Must  have a .mount unit.

**.swap**: Describes swap space on the system.

**.target**: Used to provide syncronization with other units. 

**.path**: Defines a path for path based activation. A matching unit is  started depending on the path existence or inexistence.

**.timer**: Defines a timer to be managed by systemd. A matching unit is  started when the timer is reached.

**.snapshot**: Created with systemctl snapshot command. Saves a state of the system. Does not survive among sessions.

**.slice:** Associated with cgroups (Linux Control Group nodes). Allows resources to be restricted.  

**.scope:** Created automatically by systemd from information received from its bus interfaces. Used to manage sets of system processes that are 
created externally.

### 1.3. Example Unit Files
Contents of /lib/systemd/system/apache2.service

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
[Install]
WantedBy=multi-user.target
```

Contents of /lib/systemd/system/ssh.service

```
[Unit]
Description=OpenBSD Secure Shell server
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target auditd.service
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

Contents of /lib/systemd/system/ssh.socket

```
[Unit]
Description=OpenBSD Secure Shell server socket
Before=ssh.service
Conflicts=ssh.service
ConditionPathExists=!/etc/ssh/sshd_not_to_be_run
[Socket]
ListenStream=22
Accept=yes
[Install]
WantedBy=sockets.target
```

Contents of /etc/systemd/system/snap-firefox-2356.mount

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
Unit files are made of sections. Unit and Install sections can exist in  all types of units. Also there are some other sections which can exist in  certain unit types. They are Socket, Mount, Automount, Swap, Path, Timer,  and Slice.

Sections contain directives. Some directives are unit type specific and  some are general.

For a full list of directives see:  
<https://www.freedesktop.org/software/systemd/man/systemd.directives.html>

#### 1.4.1. Unit Section Directives (Applies to all unit types)
**Description:** A short description of the unit.  
**Documentation:** Location of documentation.  
**Requires:** The units that this unit depends. All of them must be  activated for this unit to be activated.  
**Wants:** Similar to Requires, but not strict. Systemd tries to activate  the list of units before activating this unit.  
**BindsTo:** Similar to Requires, also stops this unit when the listed unit stops.
**Before:** This unit must be started before the listed units. Does not  imply dependency.  
**After:** The list of units must be started before this unit. Does not  imply dependency.  
**Conflicts:** This unit can not be run at the same time with the listed  unit. If this unit starts, other units stop.  
**Condition:** This unit starts if the conditions are met. If conditions are not met, this unit is skipped.  
**Assert:** Similar to condition. But if conditions are not met, a failure is caused.  
**ConditionPathExists:** Unit starts if this path exists. Start the path  with ! to negate.

#### 1.4.2. Install Section Directives (Applies to all unit types)
**WantedBy:** Similar to Wants directive of the Unit section. Mostly used  with targets.  
**RequiredBy:** Similar to WantedBy but is more strict. Causes a failure if the dependency is not met.  
**Alias:** Allows the unit have an alias name. (Like ssh, sshd).  
**Also:** Additional units to install/deinstall when this unit is installed/deinstalled.  
**DefaultInstance:** Only used with template units. Default instance name of the unit enabled from a template.

### 1.4.3. Service Section Directives (Applies to Service unit types)
**Type:** Could be one of the following

- **simple:** Systemd considers that the service starts immediately.
- **exec:** Similar to simple, but systemd waits for binary to execute.
- **forking:** The service forks a child process and exists.
- **oneshot:** The service live for a short time and then exit.
- **dbus:** The service will take a name on the D-Bus bus.
- **notify:** The service will notify when finishes starting up.
- **idle:** This indicates that the service will not be run until all jobs  are dispatched.

**RemainAfterExit:** Commonly used with the oneshot type. Indicates that the service isactive even after the process exits.  
**PIDFile:** For forking type, file to contain the PID of the child process.  
**BusName:** For dbus type, name to acquire as D-Bus name.  
**NotifyAccess:** Takes none, main, exec or none values. Controls which  service status messages are notified.   
**Environment:** Environment values to set.  
**EnvironmentFile:** Read a list of environment values from this file. (-) sign before the file name means, ignore if the file is not found.  
**Killmode:** How to stop the service. process means only to kill the main process, mixed means to kill the main process and the others, none means  just run ExecStop.  
**ExecStart:** Command to start the service. If starts with -, ignore  failure.
**ExecStartPre:** Additional commands to run before the main process.   
**ExecStartPost:** Additional commands to run after the main process.  
**ExecReload:** Command to reload the service.  
**ExecStop:** Command to stop the service.  
**ExecStopPost:** Additional commands to run after stopping the process.  
**RestartSec:** Amount of time to wait before restart.  
**Restart:** Circumstances to automatically restart the service. Could be: always, on-success, on-failure, on-abnormal, on-abort, on-watchdog etc.  
**RestartPreventExitStatus:** Prevents the service from automatically  restarting if the given exit code is received.  
**RuntimeDirectory:** Directory to run the service (under /run).  
**RuntimeDirectoryMode:** Permissions of the runtime directory (Default  0755).  
**TimeoutSec:** Amount of time to wait before starting or stopping the  service before marking as failed (or killing it).  
**TimeoutStartSec:** Amount of time to wait before starting service before marking as failed (or killing it).  
**TimeoutStopSec:** Amount of time to wait before starting service before marking as failed (or killing it).

#### 1.4.3. Socket Section Directives (Applies to Socket unit types)
**ListenStream:** Address to listen on for a TCP stream.  
**ListenDatagram:** Address to listen on for a UDP stream.  
**ListenSequentialPacket:** Address to listen on for a Unix socket stream.  
**ListenFIFO:** File system FIFO to listen on.  
**Accept:** If yes, a service instance is spawned for each incoming  connection, if no, all listening sockets are passed to the started service unit.  
**SocketUser:** Unix user name for the socket (default root).  
**SocketGroup:** Unix group name for the socket (default root).  
**SocketMode:** System access permissions for the socket (default 0666).  
**Service:** Connected service name (if different than the socket name).

#### 1.4.4. Mount Section Directives (Applies to Mount unit types)
**What:** Path to be mounted.  
**Where:** Path to mount.  
**Type:** The filesystem type of the mount.  
**Options:** A comma-separated list of the mount options.  
**SloppyOptions:** Boolean to determine whether the mount will fail if there  is an unrecognized mount option.  
**DirectoryMode:** Permission mode for the parent dirs of the mount point.  
**TimeoutSec:** Amount of time to wait before the operation is marked as  failed.

#### 1.4.5. Automount Section Directives (Applies to Automount unit types)
**Where:** Path to mount.  
**DirectoryMode:** Permission mode for the parent dirs of the mount point.

#### 1.4.6. Swap Section Directives (Applies to Swap unit types)
**What:** Path of the location of swap (file or device).  
**Priority:** Swap priority in integer form.  
**Options:** Comma separated list of options for /etc/fstab file.  
**TimeoutSec:** Amount of time to wait before the operation is marked as failed.  

#### 1.4.7. Path Section Directives (Applies to Path unit types)
**PathExists:** If this path exists, associated unit will be activated.  
**PathExistsGlob:** Similar to PathExists, supports file glob expressions.  
**PathChanged:** Activates the associated unit when the file in the path is  saved and closed.  
**PathModified:** Similar to PathChanged but also activates the unit when the file is changed.  
**DirectoryNotEmpty:** Activates the associated unit when the specified  directory is not empty.  
**Unit:** Connected unit name (if different than the path name).  
**MakeDirectory:** If true, the directories to watch are created before  watching.  
**DirectoryMode:** Permissions to use if MakeDirectory is true (Default 755)

#### 1.4.8. Timer Section Directives (Applies to Timer unit types)
**OnActiveSec:** Activate the associated unit after this amount of time  after the activation time of the timer unit.  
**OnBootSec:** Activate the associated unit after this amount of the time after the boot.  
**OnStartupSec:** Activate the associated unit after this amount of the time after systemd process started.  
**OnUnitActiveSec:** Activate the associated unit after this amount of the time after the associated unit last activated.  
**OnUnitInactiveSec:** Activate the associated unit after this amount of the time after the associated unit last marked as inactive.  
**OnCalendar:** Absolute time to activate the associated unit.  
**AccuracySec:** Level of accuracy of the timer.  
**Unit:** Associated unit name (if different than the timer name).  
**Persistent:** If true, the time when the service unit was last triggered  is stored on disk. When the timer is activated, the service unit is  triggered immediately if it would have been triggered at least once during the time when the timer was inactive. 

<br>
</details>

<details markdown='1'>
<summary>
2. Targets
</summary>
---
### 2.1. Definition and List
Similar to SysV init runlevel. Their purpose is to group together other  systemd units through a chain of dependencies.

A fresh install Ubuntu 24.04 server has the following targets:

```
systemctl list-unit-files --type=target
```

```
UNIT FILE                     STATE    PRESET  
basic.target                  static   -       
blockdev@.target              static   -       
bluetooth.target              static   -       
boot-complete.target          static   -       
cloud-config.target           static   -       
cloud-init.target             static   -       
cryptsetup-pre.target         static   -       
cryptsetup.target             static   -       
ctrl-alt-del.target           alias    -       
default.target                alias    -       
emergency.target              static   -       
exit.target                   disabled disabled
factory-reset.target          static   -       
final.target                  static   -       
first-boot-complete.target    static   -       
friendly-recovery.target      static   -       
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
integritysetup-pre.target     static   -       
integritysetup.target         static   -       
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
remote-cryptsetup.target      disabled enabled 
remote-fs-pre.target          static   -       
remote-fs.target              enabled  enabled 
remote-veritysetup.target     disabled enabled 
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
snapd.mounts-pre.target       static   -       
snapd.mounts.target           static   -       
sockets.target                static   -       
soft-reboot.target            static   -       
sound.target                  static   -       
storage-target-mode.target    static   -       
slices.target                 static   -       
smartcard.target              static   -       
snapd.mounts-pre.target       static   -       
snapd.mounts.target           static   -       
sockets.target                static   -       
soft-reboot.target            static   -       
sound.target                  static   -       
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
umount.target                 static   -       
usb-gadget.target             static   -       
veritysetup-pre.target        static   -       
veritysetup.target            static   -       
```

Target configuration files reside in /lib/systemd/system/

### 2.2. Example Target Files
network.target

```
[Unit]
Description=Network
Documentation=man:systemd.special(7)
Documentation=https://www.freedesktop.org/wiki/Software/systemd/NetworkTarget
After=network-pre.target
RefuseManualStart=yes
```

multi-user.target

```
[Unit]
Description=Multi-User System
Documentation=man:systemd.special(7)
Requires=basic.target
Conflicts=rescue.service rescue.target
After=basic.target rescue.service rescue.target
AllowIsolate=yes
```

graphical.target

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
Start a service

```
sudo systemctl start apache2.service
```

Stop a service

```
sudo systemctl stop apache2.service
```

Reload a service

```
sudo systemctl reload apache2.service
```

Restart a service

```
sudo systemctl restart apache2.service
```

Try to reload if possible, otherwise restart a service

```
sudo systemctl reload-or-restart apache2.service
```

Enable a service (starts at boot)

```
sudo systemctl enable apache2.service
```

Disable a service (does not start at boot)

```
sudo systemctl disable apache2.service
```

Show status of a service

```
sudo systemctl status apache2.service
```

Show if service is active

```
systemctl is-active apache2.service
```

Show if service is enabled

```
systemctl is-enabled apache2.service
```

Show if service is failed

```
systemctl is-failed apache2.service
```

Mask a service (completely unstartable)

```
sudo systemctl mask apache2.service
```

Unmask a service

```
sudo systemctl unmask apache2.service
```

List all active units

```
sudo systemctl list-units
```

Including loaded and attempted to load

```
sudo systemctl list-units --all
```

Including all installed

```
sudo systemctl list-unit-files
```

List services only

```
systemctl list-units --type=service
```

See contents of a unit file

```
systemctl cat apache2.service
```

See dependencies of a unit

```
systemctl list-dependencies apache2.service
```

See dependencies of a unit recursively

```
systemctl list-dependencies apache2.service --all
```

See low level details of a unit

```
systemctl show apache2.service
```

Append or modify settings in a unit file

```
sudo systemctl edit apache2.service
```

Edit entire contents of a unit file

```
sudo systemctl edit --full apache2.service
```

Reload systemd

```
sudo systemctl daemon-reload
```

Show default target (run level) of a system

```
systemctl get-default
```

Set default target

```
sudo systemctl set-default graphical.target
sudo systemctl set-default multi-user.target
```

List of available targets

```
systemctl list-unit-files --type=target
```

List of units tied to a target

```
systemctl list-dependencies multi-user.target
```

Poweroff and reboot

```
sudo systemctl poweroff
sudo systemctl reboot
```

Boot into rescue mode

```
sudo systemctl rescue
```

Halt (Does not poweroff the machine)

```
sudo systemctl halt
```

Control systemd of a remote system

```
systemctl --host user_name@host_name command
```

<br>
</details>

<details markdown='1'>
<summary>
4. Log Management: journal-ctl Command
</summary>
---
See all log entries

```
journalctl
```

See all log entries for the current boot

```
journalctl -b
```

See only kernel entries

```
journalctl -k
```

See only kernel entries for the current boot

```
journalctl -k -b
```

See only apache log entries

```
journalctl -u apache2.service
```

See only apache log entries for the current boot

```
journalctl -b -u apache2.service
```

See logs from previous boot

```
journalctl -b -1
```

List boots

```
journalctl --list-boots
```

Logs in a time interval

```
journalctl --since "2023-01-10 17:15:00"
journalctl --since "2023-01-10" --until "2023-01-11 03:00"
journalctl --since yesterday
journalctl --since 09:00 --until "1 hour ago"
journalctl -u apache2.service --since today
```

Log entries for an executable

```
journalctl /usr/bin/bash
```

Log in json format

```
journalctl -b -u apache2 -o json
journalctl -b -u apache2 -o json-pretty
```

Most recent 10 entries

```
journalctl -n
```

Most recent 20 entries

```
journalctl -n 20
```

Actively follow logs (like tail -f). Press Ctrl-C to exit.

```
journalctl -f
```

Disk usage

```
journalctl --disk-usage
```

Delete old logs up to size

```
sudo journalctl --vacuum-size=1G
```

Delete old logs up to time

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
systemd has some other components too. Some of them:

**systemd-boot:** UEFI boot manager. Supports basic boot manager  configuration. Integrates with systemctl command. Has the command bootctl.

**systemd-cat:** Adds a record to the systemd log with a pipeline.

```
echo "Test" | systemd-cat -p info
```

**systemd-localed:** Manages system locale settings. Has the command  localectl.

**systemd-logind:** Manages user logins. Keeps track of users and sessions.  Handles device access management for users.

**systemd-machined:** Detects and monitors virtual machines and containers.  Has machinectl command.

**systemd-mount:** Handles .mount and .automount units.

**systemd-networkd:** Network configuration management. Configuration files  are in /lib/systemd/network, /run/systemd/network, and /etc/systemd/network in increasing precedence.

**systemd-nspawn:** May be used to run a command or OS in a light-weight  namespace container. In many ways it is similar to chroot

**systemd-resolved:** Provides network name resolution. Has resolvectl  command.

**systemd-sysusers:** Creates system users and groups.

**systemd-timesyncd:** Provides system time synchronization across the  network with a remote NTP server. Has timedatectl command.

**systemd-tmpfiles:** Creates, deletes, and cleans up volatile and temporary  files and directories.

**systemd-udevd:** Manages physical devices.

<br>
</details>

<details markdown='1'>
<summary>
6. Creating a Service
</summary>
---
We will create a very simple service. Our service will ping an IP address in every 10 minutes. It will create an info log if the ping is OK,  otherwise it will create and error log.

The application will be a shell script, the script will be put into /usr/local/bin, a unit file will be created, enabled, started and tested.

### 6.1. Create Shell Script
```
nano ipcheck.sh
```

Fill as below

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

### 6.2. Copy it into /usr/local/bin
Make it executable

```
chmod +x ipcheck.sh
```

Copy

```
sudo cp ipcheck.sh /usr/local/bin
```

### 6.3. Create Unit File
```
sudo systemctl edit --force --full ipcheck.service
```

The command will open a nano editor

Fill it as below, save and exit

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

### 6.4. Enable and Start The Service
```
sudo systemctl enable ipcheck.service
sudo systemctl start ipcheck.service
```

### 6.5. Test it
```
sudo journalctl -n 20
```

</details>
</summary>


