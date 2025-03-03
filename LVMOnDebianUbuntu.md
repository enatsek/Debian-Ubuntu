##### LVMOnDebianUbuntu 
# Logical Volume Manager on Debian and Ubuntu Server

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.1. Info
LVM, or Logical Volume Manager allows for more flexible and dynamic  management of disk space compared to traditional partitioning schemes. 

It enables features such as resizing volumes, creating snapshots, and managing multiple physical storage devices more effectively.

To get the best of LVM, it must be defined when the OS is installed. That  way we can use LVM for (nearly) all of our disk space (boot partition can not be in LVM).

It is possible to install the OS without LVM and add it later too. But to use LVM on the / (root) partition, we need to install it when we install the OS.

### 0.2. Test Environment
Tested on the following environments:

- Debian 11
- Debian 12
- Ubuntu 22.04 LTS Server
- Ubuntu 24.04 LTS Server

### 0.3. Sources
[Red Hat Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/index)  
ChatGPT

<br>
</details>

<details markdown='1'>
<summary>
1. Layers of LVM
</summary>
---
### 1.0. Abstract
- Physical Volumes (PV) are defined from disks or partitions.
- Volume Groups (VG) are defined by combining PVs.
- Logical Volumes are defined within VGs.

### 1.1. Physical Volumes (PV)
Storage devices or partitions that LVM uses as a building block.

Could be a complete hard drive, a disk partition, or even a RAID array.

### 1.2. Volume Groups (VG)
Collections of one or more physical volumes.

Act as a pool that aggregates the storage space from multiple physical volumes.

Logical volumes are created within volume groups.

### 1.3. Logical Volumes (LV)
An abstraction that represents a portion of a volume group.

Similar to partitions in traditional disk management.

Can be resized and moved without affecting the data stored on them.

There are 6 main LV types.

#### 1.3.1. Linear Logical Volume
Default logical volume type.

Data is stored sequentially.

```
lvcreate -n mylv -L 10G myvg
```

#### 1.3.2. Mirrored Logical Volume
Provides data redundancy with multiple copies (mirrors) of the data.

Offers fault tolerance; if one mirror fails, the remaining mirrors can be  used.

```
lvcreate --type mirror --mirrors 2 -n mymirroredlv -L 10G myvg
```

#### 1.3.3. Snapshot Logical Volume
Creates a point-in-time copy (snapshot) of an existing logical volume.

Useful for backup purposes or creating consistent images of a volume for  testing.

```
lvcreate --type snapshot -n mysnapshotlv -L 5G --snapshot /dev/myvg/mylv
```

#### 1.3.4. Thin Logical Volume
Enables efficient storage allocation by using thin provisioning.

Allocates space only as needed, allowing for more flexible use of storage resources.

```
lvcreate --type thin-pool -n mythinpool -L 100G myvg
lvcreate --type thin -n mythinvolume -V 50G --thinpool myvg/mythinpool
```

#### 1.3.5. Cache Logical Volume
Used to cache data for another logical volume, providing improved  performance.

Typically used with SSDs to cache data from slower spinning disks.

```
lvcreate --type writeback --size 100M --name mycachelv myvg
lvconvert --type writecache --cachevol myvg/mycachelv \
     --name mycachedlv myvg/myoriginalvolume
```

#### 1.3.6. Striped Logical Volume
Stripes data evenly across multiple physical volumes to enhance I/O  performance. 

Allows parallel read and write operations.

```
lvcreate --type striped -i 2 -I 4M -L 200G -n striped_lv myvg
```

<br>
</details>

<details markdown='1'>
<summary>
2. Physical Volume Commands
</summary>
---
### 2.1. pvs
Provides physical volume information in a configurable form, displaying one line per physical volume

```
sudo pvs
sudo pvs /dev/sdb
```

### 2.2. pvscan
Scans all supported LVM block devices in the system for physical volumes.

```
sudo pvscan
```

Locates and identifies the physical volumes on the system and updates the metadata cache used by LVM.

### 2.3. pvdisplay
Provides a verbose multi-line output for each physical volume.

```
sudo pvdisplay
sudo pvdisplay /dev/sdb
```

Display a mapping of the physical extents to the corresponding logical volumes.

```
sudo pvdisplay -m /dev/sdb
```

### 2.4. pvcreate 
Initializes a physical volume for use by LVM.

```
sudo pvcreate /dev/sdb
sudo pvcreate /dev/sdb1
```
  
Make sure the device or partition is not used. It will be erased.

After initializing, you can create or extend volume groups using the
vgcreate or vgextend commands, respectively.

### 2.5. pvremove
Removes LVM metadata from a physical volume.

```
sudo pvremove /dev/sdb
sudo pvremove /dev/sdb1
```

Make sure you are not removing a used PV. 

Remove any logical volumes and volume groups associated with the physical volume before running `pvremove`.

After pvremove, you can repurpose the device or partition for other uses, like creating a new partition, filesystem, etc.

### 2.6. pvmove 
Move allocated physical extents from one physical volume to another within the same volume group.
 
Move all the data in /dev/sda1 to /dev/sdb1. They must be in the same VG

```
sudo pvmove /dev/sda1 /dev/sdb1
```

### 2.7. pvresize
Resize a physical volume

```
sudo pvresize /dev/sdb1
```

Must be used when the underlying block device is resized.

### 2.8. pvchange
Changes the properties (allocatable, uuid, tags etc) of a physical volume.

Make the physical volume /dev/sdb1 allocatable

```
sudo pvchange -x y /dev/sdb1
```

Deactivate (disable) the physical volume in verbose mode.

```
sudo pvchange -x y /dev/sdb1
```

### 2.9. pvck
Checks and repairs LVM metadata on PVs

Check a PV

```
sudo pvck /dev/sdb1
```

<br>
</details>

<details markdown='1'>
<summary>
3. Volume Group Commands
</summary>
---
### 3.1. vgs
Provides volume group information in a configurable form, displaying one line per volume group

```
sudo vgs
sudo vgs myvg
```

### 3.2. vgscan
Scans all supported LVM block devices in the system for volume groups.

```
sudo vgscan
```

Updates the metadata cache used by LVM. This cache maintains information about the volume groups on the system.

### 3.3. vgdisplay
Displays volume group properties such as size, extents, number of physical volumes, and other options in a fixed form.

```
sudo vgdisplay
sudo vgdisplay myvg
```

### 3.4. vgcreate
Creates a new volume group.

Create a new volume group named myvg using the physical volume /dev/sdb1

```
sudo vgcreate myvg /dev/sdb1
```

Before vgcreate, physical volumes must be initialized with pvcreate.

Volume group names are case-sensitive.

When creating a volume group, LVM considers the total size of the physical volumes.

After creating a volume group with vgcreate, you can proceed to create logical volumes.

### 3.5. vgextend
Adds physical volumes to an existing volume group.

Add physical volume /dev/sdb2 to the volume group myvg

```
sudo vgextend myvg /dev/sdb2
```

Before using vgextend, ensure that the physical volumes you specify are initialized with pvcreate.

After extending a volume group with vgextend, you can use the additional storage space to either extend existing logical volumes or create new ones within the extended volume group.

### 3.6. vgreduce
Remove one or more physical volumes from a volume group. 

Remove /dev/sdb2 from volume group myvg

```
sudo vgreduce myvg /dev/sdb1
```

When removing a physical volume, the data on that physical volume is moved to other available physical volumes in the volume group.

Removing a physical volume from a volume group is a significant operation and can impact data availability. Ensure that you have proper backups before performing such operations.

### 3.7. vgremove
Removes a volume group.

```
sudo vgremove myvg
```

Before using `vgremove`, ensure that there are no logical volumes or other dependencies associated with the volume group.

Remove any logical volumes within the volume group using lvremove before using vgremove.

Ensure that any filesystems mounted from logical volumes within the volume group are unmounted before attempting to remove the volume group.

After removing a volume group with vgremove, the physical volumes that were part of the volume group become unallocated, and you can repurpose them for other uses.

### 3.8. vgchange
Change the attributes of a volume group.

Activate (enable) the volume group myvg.

```
sudo vgchange -a y myvg
```

- "-a y" or "-a n": Activates (-a y) or deactivates (-a n) the volume group.

### 3.9. vgrename
Renames a volume group.

```
sudo vgrename oldvg newvg
```

### 3.10. vgck
Checks the consistency of volume groups

```
sudo vgck
```

Rewrite VG metadata to correct problems.

```
sudo vgck --updatemetadata myvg -v
```

### 3.11. Other Commands:
- vgcfgbackup: Backup volume group configurations.
- vgcfgrestore: Restore volume group configuration
- vgconvert: Change volume group metadata format.
- vgexport: Unregister volume group(s) from the system.
- vgimport: Register exported volume group with system.
- vgimportclone: Import a VG from cloned PVs.
- vgmerge: Merge volume groups.
- vgmknodes: Create the special files for volume group devices in /dev.
- vgsplit: Move PVs into a new or existing volume group

<br>
</details>

<details markdown='1'>
<summary>
4. Logical Volume Commands
</summary>
---
### 4.1. lvs
Provides logical volume information in a configurable form, displaying one line per logical volume

```
sudo lvs
sudo lvs /dev/vg_name/lv_name
sudo lvs /dev/myvg/mylv
```

All LVs in a VG

```
sudo lvs /dev/vg_name
sudo lvs /dev/myvg
```

### 4.2. lvscan
Scans for all logical volumes in the system and lists them.

```
sudo lvscan
```

### 4.3. lvdisplay
Displays logical volume properties, such as size, layout, and mapping in a fixed format

```
sudo lvdisplay
sudo lvdisplay myvg/mylv
```

Specify units in megabytes

```
sudo lvdisplay --unit m myvg/mylv
```

### 4.4. lvcreate
Creates a new logical volume within a volume group.

Create a new LV named mylv in myvg VG with size 11 GB

```
sudo lvcreate -L 11G -n mylv myvg
```

Format created logical volume:

```
sudo mkfs -t ext4 /dev/myvg/mylv
```

Mount it

```
sudo mkdir /mnt/point
sudo mount /dev/myvg/mylv /mnt/point
```

Unmount it

```
sudo umount /mnt/point
```

### 4.5. lvextend
Extends the size of a logical volume.

Extend mylv logical volume by 2 GB

```
sudo lvextend -L +2G myvg/mylv
```
 
Resize the file system

```
sudo resize2fs /dev/myvg/mylv
```

`xfs_growfs` is used for XFS.

### 4.6. lvreduce
Reduces the size of a logical volume.

Reduce the logical volume mylv in the volume group myvg by 2 GB.

```
sudo lvreduce -L -1G myvg/mylv
```

Resize the file system (you may need to unmount the LV)

```
sudo resize2fs /dev/myvg/mylv
```

### 4.7. lvremove
Removes a logical volume.

Remove the logical volume mylv in the volume group myvg.

```
sudo lvremove myvg/mylv
```

The command permanently deletes the data.

Ensure that any filesystems mounted from the logical volume are unmounted before attempting to remove it.


### 4.8. lvchange
Changes the attributes and status of a logical volume. Activate or  deactivate a logical volume, modify its permission flags, or change its  allocation policy.  

Deactivate (or sets to "no") the activation of the logical volume mylv in the volume group myvg.

```
sudo lvchange -a n myvg/mylv
```

Activate it

```
sudo lvchange -a y myvg/mylv
```

Sets the read-only permission in a logical volume

```
sudo lvchange -p r myvg/mylv
```

Sets back the read/write permission in a logical volume

```
sudo lvchange -p rw myvg/mylv
```

### 4.9. lvrename
Renames a logical volume name

```
sudo lvrename myvg mylv mynewlv2
```

### 4.10. Other Commands
- lvconvert: Change logical volume layout.
- lvresize: Resize a logical volume.

<br>
</details>

<details markdown='1'>
<summary>
5. Case Study 1 - Installing LVM and Manipulating Disks, PVs, VGs, LVs
---
</summary>
### 5.0. Specs
We have a system installed without LVM. 

- Add a 20 GB disk and use it as a LV
- Add a 30 GB disk and extend the LV
- Add a 50 GB disk, extend the VG and move data to this disk
- Remove 20 GB and 30 GB disks.

The steps:

1. Install LVM
2. Add 20 GB disk
3. Create a PV from the disk
4. Create a VG from the PV
5. Create a LV within the VG
6. Create a Filesystem in the LV
7. Mount the FS 
8. Add 30 GB disk
9. Create a PV from the 2nd disk
10. Extend the VG with this PV
11. Extend the LV
12. Extend the Filesystem
13. Add 50 GB disk
14. Create a PV from the 3rd disk
15. Extend the VG with this PV
16. Move data from 20 GB and 30 GB disks to 50 GB disk
17. Remove 20 GB and 30 GB disks as PV
18. Remove 20 GB and 30 GB disks from the system and check everything

### 5.1. Install LVM Packages
```
sudo apt update
sudo apt -y install lvm2
```

### 5.2. Add 20 GB Disk
Output of `lsblk -i` command before adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
```

 For physical servers, you need to add a disk to the hardware. For virtual servers you have to define it and attach it to the VM.

I'm adding a 20 GB disk to my VM.

Output of `lsblk -i` command after adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
sdb      8:16   0   20G  0 disk 
```

That means, my new disk is /dev/sdb.

At the following steps, you need to change /dev/sdb to your disk device  name.

### 5.3. Create a PV from the Disk
Mark /dev/sdb as a PV

```
sudo pvcreate /dev/sdb
```

### 5.4. Create a VG from the PV
Create a VG named "myvg" using /dev/sdb

```
sudo vgcreate myvg /dev/sdb
```

### 5.5. Create a LV Within the VG
Create the LV using the maximum available size with name mylv

```
sudo lvcreate -l +100%FREE -n mylv myvg
```

### 5.6. Create a Filesystem in the LV
Format as Ext4

```
sudo mkfs -t ext4 /dev/myvg/mylv
```

### 5.7. Mount the FS 
Create a mount point

```
sudo mkdir /mnt/mylv
```

Mount mylv to the mount point /mnt/mylv

```
sudo mount /dev/myvg/mylv /mnt/mylv
```
 
If you want the mount to be persistent, add to the end of /etc/fstab

```
sudo nano /etc/fstab
```

Add to the end of the file

```
/dev/myvg/mylv    /mnt/mylv    ext4    defaults    0 0
```

Check with lsblk

```
lsblk -i
```

Output of the command

```
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 22.9G  0 disk 
|-sda1        8:1    0   22G  0 part /
|-sda2        8:2    0    1K  0 part 
`-sda5        8:5    0  976M  0 part [SWAP]
sdb           8:16   0   20G  0 disk 
`-myvg-mylv 254:0    0   20G  0 lvm  /mnt/mylv
```

Check with df -h

```
df -h
```

Output of the command

```
Filesystem             Size  Used Avail Use% Mounted on
udev                   457M     0  457M   0% /dev
tmpfs                   97M  544K   96M   1% /run
/dev/sda1               22G  1.8G   19G   9% /
tmpfs                  481M     0  481M   0% /dev/shm
tmpfs                  5.0M     0  5.0M   0% /run/lock
/dev/mapper/myvg-mylv   20G   44K   19G   1% /mnt/mylv
tmpfs                   97M     0   97M   0% /run/user/1000
```

Create some big files in the filesystem  
Create a directory for files

```
sudo mkdir /mnt/mylv/tmp
```

Make it writable for everyone

```
sudo chmod 777 /mnt/mylv/tmp
```

Create 3 files of 500 MB each

```
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file1
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file2
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file3
```

Check contents

```
ls -al /mnt/mylv/tmp
```

### 5.8. Add 30 GB disk
I'm adding a 30 GB disk to my VM.

Output of `lsblk -i` command after adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 22.9G  0 disk 
|-sda1        8:1    0   22G  0 part /
|-sda2        8:2    0    1K  0 part 
`-sda5        8:5    0  976M  0 part [SWAP]
sdb           8:16   0   20G  0 disk 
`-myvg-mylv 254:0    0   20G  0 lvm  /mnt/mylv
sdc           8:32   0   30G  0 disk 
```

That means, my new disk is /dev/sdc.

At the following steps, you need to change /dev/sdc to your disk device  name.

### 5.9. Create a PV from the Second Disk
Mark /dev/sdc as a PV

```
sudo pvcreate /dev/sdc
```

### 5.10. Extend the VG with this PV
Add /dev/sdc to VG myvg

```
sudo vgextend myvg /dev/sdc
```

### 5.11. Extend the LV
Extend mylv LV to maximum

```
sudo lvextend -l +100%FREE  myvg/mylv
```

### 5.12. Extend the Filesystem
```
sudo resize2fs /dev/myvg/mylv
```

Check "df -h" command to check the new size

```
df -h
```

Output of the command

```
Filesystem             Size  Used Avail Use% Mounted on
udev                   457M     0  457M   0% /dev
tmpfs                   97M  548K   96M   1% /run
/dev/sda1               22G  3.2G   18G  16% /
tmpfs                  481M     0  481M   0% /dev/shm
tmpfs                  5.0M     0  5.0M   0% /run/lock
/dev/mapper/myvg-mylv   50G  1.5G   46G   4% /mnt/mylv
```

Add another big file

```
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file4
```

Check contents

```
ls -al /mnt/mylv/tmp
```

### 5.13. Add 50 GB disk
I'm adding a 50 GB disk to my VM.

Output of `lsblk -i` command after adding the disk:

```
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 22.9G  0 disk 
|-sda1        8:1    0   22G  0 part /
|-sda2        8:2    0    1K  0 part 
`-sda5        8:5    0  976M  0 part [SWAP]
sdb           8:16   0   20G  0 disk 
`-myvg-mylv 254:0    0   30G  0 lvm  /mnt/mylv
sdc           8:32   0   30G  0 disk 
`-myvg-mylv 254:0    0   30G  0 lvm  /mnt/mylv
sdd           8:48   0   50G  0 disk 
```

That means, my new disk is /dev/sdd.

At the following steps, you need to change /dev/sdd to your disk device  name.

### 5.14. Create a PV from the 3rd disk
Mark /dev/sdd as a PV

```
sudo pvcreate /dev/sdd
```

### 5.15. Extend the VG with this PV
Add /dev/sdd to VG myvg

```
sudo vgextend myvg /dev/sdd
```

### 5.16. Move data from 20 GB and 30 GB disks to 50 GB disk
Move from 20 GB disk to 50 GB disk

```
sudo pvmove /dev/sdb /dev/sdd
```

Move from 30 GB disk to 50 GB disk

```
sudo pvmove /dev/sdc /dev/sdd
```

These may take some time

### 5.17. Remove 20 GB and 30 GB disks as PV
First remove them from the VG

```
sudo vgreduce myvg /dev/sdb
sudo vgreduce myvg /dev/sdc
```

Now remove PVs (unmark them as PV)

```
sudo pvremove /dev/sdb
sudo pvremove /dev/sdc
```

### 5.18. Remove 20 GB and 30 GB disks from the system and check everything
At this step we physically remove (or unattach 20 GB and 30 GB disks)

Output of `lsblk -i` command after removing the disks

```
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 22.9G  0 disk 
|-sda1        8:1    0   22G  0 part /
|-sda2        8:2    0    1K  0 part 
`-sda5        8:5    0  976M  0 part [SWAP]
sdb           8:16   0   50G  0 disk 
`-myvg-mylv 254:0    0   30G  0 lvm  /mnt/mylv
```

As you can see, /dev/sdd became /dev/sdb but there is no problem. Our LVM is still working.

Check contents

```
ls -al /mnt/mylv/tmp
```

<br>
</details>

<details markdown='1'>
<summary>
6. Case Study 2 - LVM and Snapshot
</summary>
When we take a snapshot, we create a place to save the original states of the files that are changed after the snapshot.

That way, those original states can be used to revert to the snapshot.

Because only the originals of the changed data is backed up, snapshots do not require a lot of place.

If a snapshot is full, the snapshot becomes invalid because it can no longer track changes on the original volume. 

Snapshots are resizable.

### 6.0. Specs
We have a system installed with LVM. 

- Add a 20 GB disk and use it to extend the system disk
- Add a 30 GB disk and create a new VG with it
- Create a snapshot using the 30 GB disk
- Change the system dramatically and revert to the snapshot

The steps:

1. Add 20 GB disk
2. Create a PV from the disk
3. Extend the VG with this PV
4. Extend the LV
5. Extend the Filesystem
6. Add 30 GB disk
7. Create a PV from the disk
8. Create a new VG with this PV
9. Create a snapshot of the system disk
10. Make some changes on the system disk
11. Mount the Snapshot and Check Its Content
12. Extend the Snapshot
13. Revert to the snapshot

### 6.1. Add 20 GB disk
Output of `lsblk -i` command before adding the disk:

```
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda               8:0    0   20G  0 disk 
|-sda1            8:1    0  487M  0 part /boot
|-sda2            8:2    0    1K  0 part 
`-sda5            8:5    0 19.5G  0 part 
  |-myvg-root   254:0    0 18.6G  0 lvm  /
  `-myvg-swap_1 254:1    0  980M  0 lvm  [SWAP]
```

**Note:** 

When installing LVM at the install time, Debian lets you choose the VG name, as I choose it as myvg. Debian chooses the LV name as root.

Ubuntu doesn't let us choosing VG and LV names, they are given as ubuntu-vg and root.

At this section, you need to change myvg to your Volume Group name (ubuntu-vg for Ubuntu) for all the commands.

Output of "pvs" before adding the disk

```
  PV         VG   Fmt  Attr PSize   PFree
  /dev/sda5  myvg lvm2 a--  <19.52g    0 
```

Output of "lvscan" before adding the disk

```
  ACTIVE            '/dev/myvg/root' [18.56 GiB] inherit
  ACTIVE            '/dev/myvg/swap_1' [980.00 MiB] inherit
```

Output of "df -h" before adding the disk

```
Filesystem             Size  Used Avail Use% Mounted on
udev                   458M     0  458M   0% /dev
tmpfs                   97M  544K   96M   1% /run
/dev/mapper/myvg-root   19G  1.6G   16G  10% /
tmpfs                  481M     0  481M   0% /dev/shm
tmpfs                  5.0M     0  5.0M   0% /run/lock
/dev/sda1              455M   98M  333M  23% /boot
tmpfs                   97M     0   97M   0% /run/user/1000
```

For physical servers, you need to add a disk to the hardware. For virtual servers you have to define it and attach it to the VM.

I'm adding a 20 GB disk to my VM.

Output of `lsblk -i` command after adding the disk:

```
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda               8:0    0   20G  0 disk 
|-sda1            8:1    0  487M  0 part /boot
|-sda2            8:2    0    1K  0 part 
`-sda5            8:5    0 19.5G  0 part 
  |-myvg-root   254:0    0 18.6G  0 lvm  /
  `-myvg-swap_1 254:1    0  980M  0 lvm  [SWAP]
sdb               8:16   0   20G  0 disk 
```

That means, my new disk is /dev/sdb.

At the following steps, you need to change /dev/sdb to your disk device  name.

### 6.2. Create a PV from the disk
Mark /dev/sdb as a PV

```
sudo pvcreate /dev/sdb
```

### 6.3. Extend the VG with this PV
Add /dev/sdb to VG myvg

```
sudo vgextend myvg /dev/sdb
```

### 6.4. Extend the LV
Extend the root LV (LV defined at the system install) to maximum

```
sudo lvextend -l +100%FREE  myvg/root
```

### 6.5. Extend the Filesystem
```
sudo resize2fs /dev/myvg/root
```

Output of `df -h` after expanding the disk

```
Filesystem             Size  Used Avail Use% Mounted on
udev                   458M     0  458M   0% /dev
tmpfs                   97M  548K   96M   1% /run
/dev/mapper/myvg-root   38G  1.6G   35G   5% /
tmpfs                  481M     0  481M   0% /dev/shm
tmpfs                  5.0M     0  5.0M   0% /run/lock
/dev/sda1              455M   98M  333M  23% /boot
tmpfs                   97M     0   97M   0% /run/user/1000
```

### 6.6. Add 30 GB disk
I'm adding a 30 GB disk to my VM.

Output of `lsblk -i` command after adding the disk:

```
sda               8:0    0   20G  0 disk 
|-sda1            8:1    0  487M  0 part /boot
|-sda2            8:2    0    1K  0 part 
`-sda5            8:5    0 19.5G  0 part 
  |-myvg-root   254:0    0 38.6G  0 lvm  /
  `-myvg-swap_1 254:1    0  980M  0 lvm  [SWAP]
sdb               8:16   0   20G  0 disk 
`-myvg-root     254:0    0 38.6G  0 lvm  /
sdc               8:32   0   30G  0 disk 
```

That means, my new disk is /dev/sdc.

At the following steps, you need to change /dev/sdc to your disk device  name.

### 6.7. Create a PV from the disk
Mark /dev/sdc as a PV

```
sudo pvcreate /dev/sdc
```

### 6.8. Extend the VG with this PV
```
sudo vgextend myvg /dev/sdc
```

Snapshots must be in the same VG as the original LV

### 6.9. Create a snapshot of the system disk
Create a snapshot named mysnapshot of LV root from VG myvg. Size is 2 GB.

```
sudo lvcreate --type snapshot -n mysnapshot -L 2G --snapshot /dev/myvg/root
```

### 6.10. Make some changes on the system disk
Well, the idea is to change the data on the myvg/root LV. I'll try  installing some software.

```
sudo apt update
sudo apt install apache2 mariadb-server
```

Let's check our Snapshot

```
sudo lvs -o lv_name,lv_size,origin
```

### 6.11. Mount the Snapshot and Check Its Content
Create a temporary mount point

```
sudo mkdir /mnt/mysnapshot
```

Mount the snapshot to the mount point

```
sudo mount /dev/myvg/mysnapshot /mnt/mysnapshot
```

In /mnt/mysnapshot, you'll see the changed folders and files

Unmount it

```
sudo umount /mnt/mysnapshot
```

### 6.12. Extend the Snapshot
We may extend the snapshot to allow more changes on the origin LV

```
sudo lvextend -L+1G /dev/myvg/mysnapshot
```

### 6.13. Revert to the Snapshot
When we are done, we can revert to the snapshot. 

Normally, reverting to a snapshot requires the original volume to be  unmounted. But since we cannot unmount the root volume, we are going to need to reboot the system.

```
sudo lvconvert --merge myvg/mysnapshot
sudo reboot
```

Our snapshot LV is gone after the merge.

<br>
</details>

<details markdown='1'>
<summary>
7. Case Study 3 - Export and Import of LVM
</summary>
---
It is possible to export and import Volume Groups with their Logical Volumes.

LVs are unmounted, VG is deactivated and exported, physical disks are moved, VG is imported and activated, and finally LVs are mounted.

### 7.0. Specs
We have 2 systems installed without LVM, srva and srvb. We will install  a LV on srva, fill it with data, and we will move the LV to srvb.

- **A. Prepare the first system**
   - 1. Install LVM to srva
   - 2. Add 20 GB disk to srva
   - 3. Create a PV from the disk
   - 4. Create a VG from the PV
   - 5. Create 2 LVs within the VG
   - 6. Create 2 Filesystems in the LV
   - 7. Mount the filesystems
   - 8. Put test data on the filesystems 
- B. **Export**
   - 9. Unmount logical volumes
   - 10. Deactivate all logical volumes in the VG
   - 11. Export the VG and Unplug the disk
- C. **Prepare the second system**
   - 12. Install LVM to srvb
   - 13. Plug the disk to srvb
- D. **Import**
   - 14. Import the volume group
   - 15. Activate the volume group
   - 16. Mount the logical volumes

### 7.1. Install LVM to srva
```
sudo apt update
sudo apt -y install lvm2
```

### 7.2. Add 20 GB disk to srva
Output of `lsblk -i` command before adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
```

For physical servers, you need to add a disk to the hardware. For virtual  servers you have to define it and attach it to the VM.

I'm adding a 20 GB disk to my VM.

Output of `lsblk -i` command after adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
sdb      8:16   0   20G  0 disk 
```

That means, my new disk is /dev/sdb.

At the following steps, you need to change /dev/sdb to your disk device  name.

### 7.3. Create a PV from the disk
Mark /dev/sdb as a PV

```
sudo pvcreate /dev/sdb
```

### 7.4. Create a VG from the PV
Create a VG named "myvg" using /dev/sdb

```
sudo vgcreate myvg /dev/sdb
```

### 7.5. Create 2 LVs within the VG
First LV is 10 GB

```
sudo lvcreate -L 10G -n mylv1 myvg
```

Second LV is the rest (~10GB)

```
sudo lvcreate -l +100%FREE -n mylv2 myvg
```

### 7.6. Create Filesystems in the LVs
```
sudo mkfs -t ext4 /dev/myvg/mylv1
sudo mkfs -t ext4 /dev/myvg/mylv2
```

### 7.7. Mount the filesystems
Create mount points

```
sudo mkdir /mnt/mylv1
sudo mkdir /mnt/mylv2
```

Mount 

```
sudo mount /dev/myvg/mylv1 /mnt/mylv1
sudo mount /dev/myvg/mylv2 /mnt/mylv2
```

### 7.8. Put test data on the filesystems 
Make them writable for everyone

```
sudo chmod 777 /mnt/mylv1
sudo chmod 777 /mnt/mylv2
```

Create 2 files of 100 MB for each LV

```
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv1/d1f1
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv1/d1f2
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv2/d2f1
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv2/d2f2
```

Check the contents of the LVs

```
ls -al /mnt/mylv1
ls -al /mnt/mylv2
```

### 7.9. Unmount logical volumes
```
sudo umount /mnt/mylv1
sudo umount /mnt/mylv2
```

### 7.10. Deactivate all logical volumes in the VG
```
sudo vgchange -an myvg
```

Check with pvscan

```
sudo pvscan
```

### 7.11. Export the VG and Unplug the disk
Export the VG

```
sudo vgexport myvg
```

Now it is time to unplug the 20 GB disk.

Output of `lsblk -i` command after removing the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
```

### 7.12. Install LVM to srvb
```
sudo apt update
sudo apt -y install lvm2
```

### 7.13. Plug the disk to srvb
- Output of `lsblk -i` command before adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
```

For physical servers, you need to add a disk to the hardware. For virtual  servers you have to define it and attach it to the VM.

I'm adding a 20 GB disk to my VM.

Output of `lsblk -i` command after adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
sdb      8:16   0   20G  0 disk 
```

That means, my new disk is /dev/sdb.

### 7.14. Import the volume group
```
sudo vgimport myvg
```

### 7.15. Activate the volume group
```
sudo vgchange -ay myvg
```

### 7.16. Mount the logical volumes
```
sudo mkdir /mnt/mylv1 /mnt/mylv2
sudo mount /dev/myvg/mylv1 /mnt/mylv1
sudo mount /dev/myvg/mylv2 /mnt/mylv2
```

Check the contents of the LVs

```
ls -al /mnt/mylv1
ls -al /mnt/mylv2
```

<br>
</details>

<details markdown='1'>
<summary>
8. Uncovered Subjects
</summary>
---
The following subjects are not covered in this tutorial:

- Striped logical volumes
- RAID logical volumes
- Thin-provisioned logical volumes
- Cache volumes
- Using shared storage
- Logical volume activation
- Controlling All
ocation
- LVM object tags

</details>

