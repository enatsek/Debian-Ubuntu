##### LVM
# Logical Volume Manager on Debian and Ubuntu Server

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. The What

Logical Volume Manager (LVM) is a powerful tool for managing disk storage in Linux. It allows system administrators to create, resize, and manage disk partitions more flexibly than traditional partitioning methods.

LVM enables features such as volume resizing, snapshot creation, and effective management of multiple physical storage devices.

**Note:** For optimal use, LVM should be configured during OS installation. This allows LVM to manage nearly all disk space (except the boot partition, which cannot be in LVM).

It is also possible to install the OS without LVM and add it later. However, to use LVM for the `/` (root) partition, it must be set up during OS installation.

If the OS was installed without LVM, you can install the LVM package as follows:

```
sudo apt update
sudo apt -y install lvm2
```

### 0.2. Environment

Tested on the following distributions:

- Debian 12
- Debian 13
- Ubuntu 22.04 LTS Server
- Ubuntu 24.04 LTS Server

### 0.3. Sources
- [Red Hat Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/index)  
- [Deepseek](https://www.deepseek.com/)
- [ChatGPT](https://chatgpt.com/)

<br>
</details>

<details markdown='1'>
<summary>
1. Layers of LVM
</summary>

---
### 1.0. Abstract

LVM is structured in three layers:

1. **Physical Volumes (PV)** – Created from disks or partitions.
2. **Volume Groups (VG)** – Formed by combining PVs.
3. **Logical Volumes (LV)** – Defined within VGs.

### 1.1. Physical Volumes (PV)

Storage devices or partitions used by LVM as building blocks. These can be:

- A complete hard drive
- A disk partition
- A RAID array

### 1.2. Volume Groups (VG)

Collections of one or more physical volumes. VGs act as a storage pool, aggregating space from multiple PVs. Logical volumes are created within volume groups.

### 1.3. Logical Volumes (LV)

Abstract representations of a portion of a volume group, similar to partitions in traditional disk management. LVs can be resized and moved without affecting stored data.

There are six main types of logical volumes:

#### 1.3.1. Linear Logical Volume

The default logical volume type. Data is stored sequentially.


#### 1.3.2. Mirrored Logical Volume

Provides data redundancy by maintaining multiple copies (mirrors) of the data. Offers fault tolerance: if one mirror fails, the others remain usable.


#### 1.3.3. Snapshot Logical Volume

Creates a point-in-time copy (snapshot) of an existing logical volume. Useful for backups or creating consistent volume images for testing.


#### 1.3.4. Thin Logical Volume

Enables efficient storage allocation through thin provisioning. Space is allocated only as needed, allowing more flexible use of storage resources.


#### 1.3.5. Cache Logical Volume

Used to cache data for another logical volume, improving performance. Typically used with SSDs to cache data from slower spinning disks.


#### 1.3.6. Striped Logical Volume

Stripes data evenly across multiple physical volumes to enhance I/O performance. Allows parallel read and write operations.


<br>
</details>

<details markdown='1'>
<summary>
2. Physical Volume Commands
</summary>

---
### 2.1. pvs

Displays physical volume information in a configurable format, showing one line per physical volume.

```
sudo pvs
sudo pvs /dev/sdb
```

### 2.2. pvscan

Scans all supported LVM block devices for physical volumes.


```
sudo pvscan
```

Locates and identifies physical volumes on the system and updates the LVM metadata cache.

### 2.3. pvdisplay

Provides a verbose multi-line output for each physical volume.

```
sudo pvdisplay
sudo pvdisplay /dev/sdb
```

Display a mapping of physical extents to corresponding logical volumes:

```
sudo pvdisplay -m /dev/sdb
```

### 2.4. pvcreate 

Initializes a physical volume for use by LVM.

```
sudo pvcreate /dev/sdb
sudo pvcreate /dev/sdb1
```
  
**Warning:** Ensure the device or partition is not in use, as it will be erased.

After initialization, you can create or extend volume groups using `vgcreate` or `vgextend`, respectively.

### 2.5. pvremove

Removes LVM metadata from a physical volume.

```
sudo pvremove /dev/sdb
sudo pvremove /dev/sdb1
```

**Warning:** Ensure you are not removing a PV that is still in use. Remove any associated logical volumes and volume groups before running `pvremove`.

After removal, the device or partition can be repurposed (e.g., for a new partition or filesystem).

### 2.6. pvmove 

Moves allocated physical extents from one physical volume to another within the same volume group.

Move all data from `/dev/sda1` to `/dev/sdb1` (both must be in the same VG):

```
sudo pvmove /dev/sda1 /dev/sdb1
```

### 2.7. pvresize

Resizes a physical volume.

```
sudo pvresize /dev/sdb1
```

Used when the underlying block device has been resized.

### 2.8. pvchange

Changes properties (allocatable, UUID, tags, etc.) of a physical volume.

Make `/dev/sdb1` allocatable:

```
sudo pvchange -x y /dev/sdb1
```

Deactivate (disable) the physical volume in verbose mode:

```
sudo pvchange -x y /dev/sdb1
```

### 2.9. pvck

Checks and repairs LVM metadata on physical volumes.

Check a PV:

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

This command provides volume group information in a configurable form, displaying one line per volume group.

```
sudo vgs
sudo vgs myvg
```

### 3.2. vgscan

Scans all supported LVM block devices in the system for volume groups and updates the LVM metadata cache.

```
sudo vgscan
```

### 3.3. vgdisplay

Displays volume group properties such as size, extents, number of physical volumes, and other details in a fixed format.

```
sudo vgdisplay
sudo vgdisplay myvg
```

### 3.4. vgcreate

Creates a new volume group.

Create a new volume group named `myvg` using the physical volume `/dev/sdb1`:

```
sudo vgcreate myvg /dev/sdb1
```

**Prerequisite:** The specified physical volumes must be initialized with `pvcreate`.

**Note:** Volume group names are case-sensitive. The new volume group's total capacity will be the sum of the capacities of the specified physical volumes. After creation, you can proceed to create logical volumes within it.

### 3.5. vgextend

Adds physical volumes to an existing volume group.

Add physical volume `/dev/sdb2` to the volume group `myvg`:

```
sudo vgextend myvg /dev/sdb2
```

**Prerequisite:** The physical volumes to be added must already be initialized using `pvcreate`. After extending a volume group, you can use the additional space to extend existing logical volumes or create new ones.

### 3.6. vgreduce

Removes one or more physical volumes from a volume group.

Remove `/dev/sdb2` from volume group `myvg`:

```
sudo vgreduce myvg /dev/sdb1
```

**Note:** You must first ensure the PV contains no allocated extents (use `pvmove` to relocate data). Otherwise, the command will fail unless forced, which can lead to data loss.

### 3.7. vgremove

Removes a volume group.

```
sudo vgremove myvg
```

**Prerequisites:** You must first remove all logical volumes within the volume group using `lvremove`. Also, ensure any filesystems mounted from those logical volumes are unmounted. After removal, the physical volumes become unallocated and can be repurposed.

### 3.8. vgchange

Changes the attributes of a volume group.

Activate (enable) the volume group `myvg`:

```
sudo vgchange -a y myvg
```

*( `-a y` activates; `-a n` deactivates the volume group.)*

### 3.9. vgrename

Renames a volume group.

```
sudo vgrename oldvg newvg
```

### 3.10. vgck

Checks the consistency of volume group metadata.

```
sudo vgck
```

The `--updatemetadata` flag rewrites VG metadata to correct inconsistencies:

```
sudo vgck --updatemetadata myvg -v
```

### 3.11. Other Commands

- `vgcfgbackup`: Backs up volume group configurations.
- `vgcfgrestore`: Restores volume group configuration.
- `vgconvert`: Changes volume group metadata format.
- `vgexport`: Unregisters volume group(s) from the system.
- `vgimport`: Registers an exported volume group with the system.
- `vgimportclone`: Imports a VG from cloned PVs.
- `vgmerge`: Merges volume groups.
- `vgmknodes`: Creates the special device files for volume groups in `/dev`.
- `vgsplit`: Moves PVs into a new or existing volume group.


<br>
</details>

<details markdown='1'>
<summary>
4. Logical Volume Commands
</summary>

---
### 4.1. lvs

Provides logical volume information in a configurable form, displaying one line per logical volume.

```
sudo lvs
sudo lvs /dev/vg_name/lv_name
sudo lvs /dev/myvg/mylv
```

To list all LVs in a specific VG:

```
sudo lvs /dev/vg_name
sudo lvs /dev/myvg
```

### 4.2. lvscan

Scans for and lists all logical volumes in the system.

```
sudo lvscan
```

### 4.3. lvdisplay

Displays logical volume properties, such as size, layout, and mapping, in a fixed format.

```
sudo lvdisplay
sudo lvdisplay myvg/mylv
```

To display sizes in megabytes:

```
sudo lvdisplay --unit m myvg/mylv
```

### 4.4. lvcreate

Creates a new logical volume within a volume group.

Create a new LV named `mylv` in the `myvg` volume group with a size of 11 GB:

```
sudo lvcreate -L 11G -n mylv myvg
```

Format the newly created logical volume:

```
sudo mkfs -t ext4 /dev/myvg/mylv
```

Mount it:

```
sudo mkdir /mnt/point
sudo mount /dev/myvg/mylv /mnt/point
```

Unmount it:

```
sudo umount /mnt/point
```

### 4.5. lvextend

Extends the size of a logical volume.

Extend the `mylv` logical volume by 2 GB:

```
sudo lvextend -L +2G myvg/mylv
```
 
Resize the filesystem to use the new space:

```
sudo resize2fs /dev/myvg/mylv
```

**Note:** `resize2fs` may require a clean filesystem. If prompted, run `sudo e2fsck -f /dev/myvg/mylv` first.


For XFS filesystems, use `xfs_growfs` instead of `resize2fs`.

### 4.6. lvreduce

Reduces the size of a logical volume.

Reduce the logical volume mylv in the volume group myvg by 1 GB:

```
sudo lvreduce -L -1G myvg/mylv
```

Resize the file system (you may need to unmount the LV)

```
sudo resize2fs /dev/myvg/mylv
```

### 4.7. lvremove

Removes a logical volume.

Remove the logical volume `mylv` in the volume group `myvg`:

```
sudo lvremove myvg/mylv
```

**Warning:** This action is irreversible and will permanently destroy all data on the logical volume. Ensure any filesystems mounted from it are unmounted first.


### 4.8. lvchange

Changes the attributes and status of a logical volume, such as activation state or permission flags.

Deactivate the logical volume `mylv` in the volume group `myvg`:

```
sudo lvchange -a n myvg/mylv
```

Activate it:

```
sudo lvchange -a y myvg/mylv
```

Set the logical volume to read-only:

```
sudo lvchange -p r myvg/mylv
```

Set it back to read/write:

```
sudo lvchange -p rw myvg/mylv
```

### 4.9. lvrename

Renames a logical volume.

```
sudo lvrename myvg mylv mynewlv2
```

### 4.10. Other Commands

- `lvconvert`: Changes logical volume layout (e.g., to/from mirrored, snapshot).
- `lvresize`: A combined command that can extend or reduce a logical volume (use with the same caution as `lvreduce`).

<br>
</details>


<details markdown='1'>
<summary>
5. Case Study 1 - Installing LVM and Manipulating Disks, PVs, VGs, LVs
</summary>

---

### 5.0. Specs

We have a system installed without LVM. 

- Add a 20 GB disk and use it as a LV.
- Add a 30 GB disk and extend the LV.
- Add a 50 GB disk, extend the VG and move data to this disk.
- Remove 20 GB and 30 GB disks.

**The steps:**

1.  Install LVM.
2.  Add a 20 GB disk.
3.  Create a PV from the disk.
4.  Create a VG from the PV.
5.  Create an LV within the VG.
6.  Create a filesystem on the LV.
7.  Mount the filesystem.
8.  Add a 30 GB disk.
9.  Create a PV from the 2nd disk.
10. Extend the VG with this PV.
11. Extend the LV.
12. Extend the filesystem.
13. Add a 50 GB disk.
14. Create a PV from the 3rd disk.
15. Extend the VG with this PV.
16. Move data from the 20 GB and 30 GB disks to the 50 GB disk.
17. Remove the 20 GB and 30 GB disks as PVs.
18. Physically remove the 20 GB and 30 GB disks and verify everything works.

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

**For physical servers**, you need to add the disk to the hardware. **For virtual servers**, you need to define it and attach it to the VM.

I'm adding a 20 GB disk to my VM.

Output of the `lsblk -i` command after adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
sdb      8:16   0   20G  0 disk 
```

This means my new disk is `/dev/sdb`. **In the following steps, change `/dev/sdb` to your actual disk device name.**

### 5.3. Create a PV from the Disk

Mark `/dev/sdb` as a Physical Volume:

```
sudo pvcreate /dev/sdb
```

### 5.4. Create a VG from the PV

Create a Volume Group named `myvg` using `/dev/sdb`:

```
sudo vgcreate myvg /dev/sdb
```

### 5.5. Create a LV within the VG

Create the Logical Volume using the maximum available space and name it `mylv`:

```
sudo lvcreate -l +100%FREE -n mylv myvg
```

### 5.6. Create a Filesystem in the LV

Format it as Ext4:

```
sudo mkfs -t ext4 /dev/myvg/mylv
```

### 5.7. Mount the FS 

Create a mount point:

```
sudo mkdir /mnt/mylv
```

Mount `mylv` to the mount point `/mnt/mylv`:

```
sudo mount /dev/myvg/mylv /mnt/mylv
```
 
To make the mount persistent, add it to `/etc/fstab`:

```
sudo nano /etc/fstab
```

Add this line to the end of the file:

```
/dev/myvg/mylv    /mnt/mylv    ext4    defaults    0 0
```

Check with `lsblk`:

```
lsblk -i
```

Output:

```
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 22.9G  0 disk 
|-sda1        8:1    0   22G  0 part /
|-sda2        8:2    0    1K  0 part 
`-sda5        8:5    0  976M  0 part [SWAP]
sdb           8:16   0   20G  0 disk 
`-myvg-mylv 254:0    0   20G  0 lvm  /mnt/mylv
```

Check with `df -h`:

```
df -h
```

Output:

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

**Create some large files in the filesystem:**

Create a directory for files:

```
sudo mkdir /mnt/mylv/tmp
```

Make it writable for everyone:

```
sudo chmod 777 /mnt/mylv/tmp
```

Create 3 files of 500 MB each:

```
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file1
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file2
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file3
```

Check the contents:

```
ls -al /mnt/mylv/tmp
```

### 5.8. Add 30 GB Disk

I'm adding a 30 GB disk to my VM.

Output of `lsblk -i` after adding the disk:

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

This means my new disk is `/dev/sdc`. **Change `/dev/sdc` to your actual disk device name in the following steps.**

### 5.9. Create a PV from the Second Disk

Mark `/dev/sdc` as a Physical Volume:

```
sudo pvcreate /dev/sdc
```

### 5.10. Extend the VG with This PV

Add `/dev/sdc` to the Volume Group `myvg`:

```
sudo vgextend myvg /dev/sdc
```

### 5.11. Extend the LV

Extend the `mylv` Logical Volume to use all available free space:

```
sudo lvextend -l +100%FREE  myvg/mylv
```

### 5.12. Extend the Filesystem

Resize the filesystem to use the new space:

```
sudo resize2fs /dev/myvg/mylv
```

Check the new size with `df -h`:

```
df -h
```

Output:

```
Filesystem             Size  Used Avail Use% Mounted on
udev                   457M     0  457M   0% /dev
tmpfs                   97M  548K   96M   1% /run
/dev/sda1               22G  3.2G   18G  16% /
tmpfs                  481M     0  481M   0% /dev/shm
tmpfs                  5.0M     0  5.0M   0% /run/lock
/dev/mapper/myvg-mylv   50G  1.5G   46G   4% /mnt/mylv
```

Add another large file:

```
< /dev/urandom tr -dc "[:space:][:print:]" | head -c500M > /mnt/mylv/tmp/file4
```

Check the contents:

```
ls -al /mnt/mylv/tmp
```

### 5.13. Add 50 GB Disk

I'm adding a 50 GB disk to my VM.

Output of `lsblk -i` after adding the disk:

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

This means my new disk is `/dev/sdd`. **Change `/dev/sdd` to your actual disk device name in the following steps.**

### 5.14. Create a PV from the 3rd Disk

Mark `/dev/sdd` as a Physical Volume:

```
sudo pvcreate /dev/sdd
```

### 5.15. Extend the VG with This PV

Add `/dev/sdd` to the Volume Group `myvg`:

```
sudo vgextend myvg /dev/sdd
```

### 5.16. Move Data from the 20 GB and 30 GB Disks to the 50 GB Disk

Move data from the 20 GB disk (`sdb`) to the 50 GB disk (`sdd`):

```
sudo pvmove /dev/sdb /dev/sdd
```

Move data from the 30 GB disk (`sdc`) to the 50 GB disk (`sdd`):

```
sudo pvmove /dev/sdc /dev/sdd
```

**Note:** These operations may take some time, depending on the amount of data.

### 5.17. Remove the 20 GB and 30 GB Disks as PVs

First, remove them from the Volume Group:

```
sudo vgreduce myvg /dev/sdb
sudo vgreduce myvg /dev/sdc
```

Now, remove the Physical Volume metadata from the disks:

```
sudo pvremove /dev/sdb
sudo pvremove /dev/sdc
```

### 5.18. Physically Remove the 20 GB and 30 GB Disks and Verify

At this step, we physically remove (or detach) the 20 GB and 30 GB disks from the system.

Output of `lsblk -i` after removing the disks:

```
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 22.9G  0 disk 
|-sda1        8:1    0   22G  0 part /
|-sda2        8:2    0    1K  0 part 
`-sda5        8:5    0  976M  0 part [SWAP]
sdb           8:16   0   50G  0 disk 
`-myvg-mylv 254:0    0   30G  0 lvm  /mnt/mylv
```

As you can see, `/dev/sdd` has become `/dev/sdb`, but this is not a problem. Our LVM configuration is still working correctly.

Check the contents to confirm data integrity:

```
ls -al /mnt/mylv/tmp
```

<br>
</details>


<details markdown='1'>
<summary>
6. Case Study 2 - LVM and Snapshot
</summary>

---

A snapshot creates a point-in-time copy of a Logical Volume (LV). When files are changed on the original volume after the snapshot is taken, the original data blocks are preserved in the snapshot space. This allows you to revert to the snapshot state if needed.

Because only changed data blocks are stored, snapshots typically require much less space than the original volume.

**Important:** If a snapshot becomes full (runs out of space to track changes), it becomes invalid and is automatically dropped, which can lead to data loss. Snapshots are resizable to prevent this.

### 6.0. Specs

We have a system installed with LVM.
- Add a 20 GB disk and use it to extend the system (`/`) disk.
- Add a 30 GB disk and add it to the existing Volume Group.
- Create a snapshot of the root filesystem using space from the new 30 GB disk.
- Make significant changes to the system and revert using the snapshot.

**The steps:**

1.  Add a 20 GB disk.
2.  Create a PV from the disk.
3.  Extend the VG with this PV.
4.  Extend the root LV.
5.  Extend the filesystem.
6.  Add a 30 GB disk.
7.  Create a PV from the disk.
8.  Extend the VG with this PV.
9.  Create a snapshot of the system (root) disk.
10. Make some changes to the system disk.
11. Mount the snapshot and check its content.
12. Extend the snapshot.
13. Revert to the snapshot.

### 6.1. Add 20 GB Disk

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

**Note on Naming:**

When installing with LVM, Debian lets you choose the VG name (I chose `myvg`). Debian names the root LV `root`. Ubuntu uses `ubuntu-vg` and `lv-root` by default.

**In this section, replace `myvg` with your actual Volume Group name (`ubuntu-vg` for Ubuntu) in all commands.**

Output of `sudo pvs` before adding the disk:

```
  PV         VG   Fmt  Attr PSize   PFree
  /dev/sda5  myvg lvm2 a--  <19.52g    0 
```

Output of `sudo lvscan` before adding the disk:

```
  ACTIVE            '/dev/myvg/root' [18.56 GiB] inherit
  ACTIVE            '/dev/myvg/swap_1' [980.00 MiB] inherit
```

Output of `df -h` before adding the disk:

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

**For physical servers**, add the disk to the hardware. **For virtual servers**, define and attach it to the VM.

I'm adding a 20 GB disk to my VM.

Output of `lsblk -i` after adding the disk:

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

This means my new disk is `/dev/sdb`. **Change `/dev/sdb` to your actual disk device name in the following steps.**

### 6.2. Create a PV from the Disk

Mark `/dev/sdb` as a Physical Volume:

```
sudo pvcreate /dev/sdb
```

### 6.3. Extend the VG with This PV

Add `/dev/sdb` to the Volume Group `myvg`:

```
sudo vgextend myvg /dev/sdb
```

### 6.4. Extend the LV

Extend the root LV to use all available free space:

```
sudo lvextend -l +100%FREE  myvg/root
```

### 6.5. Extend the Filesystem

Resize the filesystem to use the new space:

```
sudo resize2fs /dev/myvg/root
```

Output of `df -h` after expanding:

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

### 6.6. Add 30 GB Disk

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

This means my new disk is `/dev/sdc`. **Change `/dev/sdc` to your actual disk device name in the following steps.**

### 6.7. Create a PV from the Disk

Mark `/dev/sdc` as a Physical Volume:

```
sudo pvcreate /dev/sdc
```

### 6.8. Extend the VG with This PV

Add `/dev/sdc` to the Volume Group `myvg`:

```
sudo vgextend myvg /dev/sdc
```

**Important:** Snapshots must be created within the same Volume Group as the original Logical Volume.

### 6.9. Create a Snapshot of the System Disk

Create a 2 GB snapshot named `mysnapshot` of the `root` LV:

```
sudo lvcreate --type snapshot -n mysnapshot -L 2G --snapshot /dev/myvg/root
```

**Tip:** Monitor snapshot usage with `sudo lvs -o lv_name,lv_size,snap_percent,origin`. If the usage nears 100%, extend it immediately.

### 6.10. Make Changes to the System Disk

To demonstrate the snapshot, we'll make significant changes by installing software:

```
sudo apt update
sudo apt install -y apache2 mariadb-server
```

Check the snapshot status to see if it's tracking changes:

```
sudo lvs -o lv_name,lv_size,origin
```

### 6.11. Mount the Snapshot and Check Its Content

Create a temporary mount point:

```
sudo mkdir /mnt/mysnapshot
```

Mount the snapshot (read-only is safer for inspection):

```
sudo mount -o ro /dev/myvg/mysnapshot /mnt/mysnapshot
```

Browse `/mnt/mysnapshot` to see the state of the root filesystem at the time the snapshot was taken (you won't see the newly installed packages).

Unmount it:

```
sudo umount /mnt/mysnapshot
```

### 6.12. Extend the Snapshot

If the snapshot is running low on space (check with `sudo lvs`), extend it to allow more changes to be tracked:

```
sudo lvextend -L+1G /dev/myvg/mysnapshot
```

### 6.13. Revert to the Snapshot

Reverting merges the snapshot back into the original volume, restoring it to the snapshot's state.

**⚠️ Critical for Root Volume:** Since the root (`/`) filesystem cannot be unmounted while the system is running, the merge is scheduled for the next boot.


Schedule the merge:

```
sudo lvconvert --merge myvg/mysnapshot
```

You will see a message like: *"Delayed merge scheduled for activation after next activation."*

Reboot the system. The merge will occur during the early boot process:

```
sudo reboot
```

**Note:** The snapshot LV (`mysnapshot`) will no longer exist after a successful merge.

<br>
</details>

<details markdown='1'>
<summary>
7. Case Study 3 - Export and Import of LVM
</summary>

---

It is possible to export and import entire Volume Groups (with their Logical Volumes) between systems. The process involves: unmounting the LVs, deactivating and exporting the VG, moving the physical disks to the new system, then importing, activating, and remounting the VG.

### 7.0. Specs

We have two systems installed without LVM: **srva** and **srvb**. We will create an LVM setup on **srva**, fill it with data, and then move the entire setup to **srvb**.

- **A. Prepare the first system (srva)**
    - -1. Install LVM on srva.
    - -2. Add 20 GB disk to srva.
    - -3. Create a PV from the disk.
    - -4. Create a VG from the PV.
    - -5. Create 2 LVs within the VG.
    - -6. Create filesystems in the LV.
    - -7. Mount the filesystems.
    - -8. Put test data on the filesystems. 
- B. **Export**
    - -9. Unmount the logical volumes.
    - -10. Deactivate all logical volumes in the VG.
    - -11. Export the VG and Unplug the disk.
- C. **Prepare the second system (srvb)**
    - -12. Install LVM on srvb.
    - -13. Plug the disk into srvb.
- D. **Import**
    - -14. Import the volume group.
    - -15. Activate the volume group.
    - -16. Mount the logical volumes.

### 7.1. Install LVM on srva

```
sudo apt update
sudo apt -y install lvm2
```

### 7.2. Add 20 GB Disk to srva

Output of `lsblk -i` before adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
```

**For physical servers**, add the disk to the hardware. **For virtual servers**, define and attach it to the VM.

I'm adding a 20 GB disk to my VM.

Output of `lsblk -i` after adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
sdb      8:16   0   20G  0 disk 
```

This means my new disk is `/dev/sdb`. **Change `/dev/sdb` to your actual disk device name in the following steps.**

### 7.3. Create a PV from the Disk

Mark `/dev/sdb` as a Physical Volume:

```
sudo pvcreate /dev/sdb
```

### 7.4. Create a VG from the PV

Create a Volume Group named `myvg` using `/dev/sdb`:

```
sudo vgcreate myvg /dev/sdb
```

### 7.5. Create 2 LVs within the VG

First LV is 10 GB:

```
sudo lvcreate -L 10G -n mylv1 myvg
```

Second LV uses the remaining space (~10 GB):

```
sudo lvcreate -l +100%FREE -n mylv2 myvg
```

### 7.6. Create Filesystems in the LVs

```
sudo mkfs -t ext4 /dev/myvg/mylv1
sudo mkfs -t ext4 /dev/myvg/mylv2
```

### 7.7. Mount the Filesystems

Create mount points:

```
sudo mkdir /mnt/mylv1
sudo mkdir /mnt/mylv2
```

Mount the LVs:

```
sudo mount /dev/myvg/mylv1 /mnt/mylv1
sudo mount /dev/myvg/mylv2 /mnt/mylv2
```

### 7.8. Put Test Data on the Filesystems 

Make the mount points writable for everyone (for testing):

```
sudo chmod 777 /mnt/mylv1
sudo chmod 777 /mnt/mylv2
```

Create 2 files of 100 MB for each LV:

```
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv1/d1f1
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv1/d1f2
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv2/d2f1
< /dev/urandom tr -dc "[:space:][:print:]" | head -c100M > /mnt/mylv2/d2f2
```

Check the contents:

```
ls -al /mnt/mylv1
ls -al /mnt/mylv2
```

### 7.9. Unmount Logical Volumes

```
sudo umount /mnt/mylv1
sudo umount /mnt/mylv2
```

### 7.10. Deactivate All Logical Volumes in the VG

Deactivate the entire Volume Group:

```
sudo vgchange -an myvg
```

Verify with `pvscan` (it should show the PV as belonging to `myvg` but not active):

```
sudo pvscan
```

### 7.11. Export the VG and Unplug the Disk

Export the Volume Group (this removes it from the system's LVM metadata cache):

```
sudo vgexport myvg
```

Now you can safely unplug or detach the 20 GB disk from **srva**.

Output of `lsblk -i` after removing the disk from **srva**:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
```

### 7.12. Install LVM on srvb

```
sudo apt update
sudo apt -y install lvm2
```

### 7.13. Plug the Disk into srvb

Output of `lsblk -i` on **srvb** before adding the disk:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
```

**For physical servers**, add the disk to the hardware. **For virtual servers**, define and attach it to the VM.

I'm adding the 20 GB disk to my **srvb** VM.

Output of `lsblk -i` after adding the disk to **srvb**:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 22.9G  0 disk 
|-sda1   8:1    0   22G  0 part /
|-sda2   8:2    0    1K  0 part 
`-sda5   8:5    0  976M  0 part [SWAP]
sdb      8:16   0   20G  0 disk 
```

This means the disk is now `/dev/sdb` on **srvb**.

### 7.14. Import the Volume Group

Scan for and import the exported Volume Group `myvg`:
```
sudo vgimport myvg
```

### 7.15. Activate the Volume Group

Activate the Volume Group and its logical volumes:

```
sudo vgchange -ay myvg
```

### 7.16. Mount the Logical Volumes

Create mount points and mount the LVs:

```
sudo mkdir /mnt/mylv1 /mnt/mylv2
sudo mount /dev/myvg/mylv1 /mnt/mylv1
sudo mount /dev/myvg/mylv2 /mnt/mylv2
```

Verify the data is intact:

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

The following LVM subjects are not covered in this tutorial:

- Striped logical volumes
- RAID logical volumes
- Thin-provisioned logical volumes
- Cache logical volumes
- Using shared storage (e.g., with iSCSI or Fibre Channel)
- Fine-grained control of logical volume activation
- Controlling physical extent allocation policies
- LVM object tags

</details>

