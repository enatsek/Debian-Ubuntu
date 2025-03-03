##### FileCompressionOnDebianUbuntu 
# File Compression and Packaging on Debian And Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.0. Info
When sharing files with other people, you may need to package and compress them. 

There are very good tools for them:
 
- gzip 
- bzip2 
- xz 
- tar 
- zip

### 0.1. Abstract
Package and compress the contents of a directory (including subdirs):

```
tar -czvf archive.tar.gz /tmp/testdir
```

Decompress and unpackage the archive:

```
tar -xzvf archive.tar.gz
```

### 0.2. Create Test Environment
All commands are tested on Debian 11 & 12 and Ubuntu Server 22.04 & 24.04 LTS

Create a temporary test directory

```
mkdir /tmp/testdir
```

Create 3 more directories d1, d2, d3

```
mkdir /tmp/testdir/d{1..3}
```

Create 3 files at each directory

```
touch /tmp/testdir/d1/f1{1..3}
touch /tmp/testdir/d2/f2{1..3}
touch /tmp/testdir/d3/f3{1..3}
```

Fill the files with random data with the given size

```
< /dev/urandom tr -dc "[:space:][:print:]" | head -c1M > /tmp/testdir/d1/f11
< /dev/urandom tr -dc "[:space:][:print:]" | head -c2M > /tmp/testdir/d1/f12
< /dev/urandom tr -dc "[:space:][:print:]" | head -c3M > /tmp/testdir/d1/f13
< /dev/urandom tr -dc "[:space:][:print:]" | head -c4M > /tmp/testdir/d2/f21
< /dev/urandom tr -dc "[:space:][:print:]" | head -c5M > /tmp/testdir/d2/f22
< /dev/urandom tr -dc "[:space:][:print:]" | head -c6M > /tmp/testdir/d2/f23
< /dev/urandom tr -dc "[:space:][:print:]" | head -c7M > /tmp/testdir/d3/f31
< /dev/urandom tr -dc "[:space:][:print:]" | head -c8M > /tmp/testdir/d3/f32
< /dev/urandom tr -dc "[:space:][:print:]" | head -c9M > /tmp/testdir/d3/f33
```

Final tree

```
├── d1
│   ├── f11
│   ├── f12
│   └── f13
├── d2
│   ├── f21
│   ├── f22
│   └── f23
└── d3
    ├── f31
    ├── f32
    └── f33
```

### 0.3. Sources
Man pages, the commands with --help option, and ChatGPT as always.  
**Never trust ChatGPT, check everything it says.**  
[linuxconfig.org](https://linuxconfig.org/create-a-random-character-text-file-using-linux-shell)

<br>
</details>

<details markdown='1'>
<summary>
1. gzip
</summary>
---
### 1.1. Info
Installation (Most probably, it is already installed).

```
sudo apt update
sudo apt install gzip
```

gzip compresses (and decompresses) only 1 file, it is not used to prepare a package of files. But it can be combined with tar to make a compressed  package of files.

### 1.2. Usage
Compress a file  
(Original file is removed, a new file is created there with .gz extension)

```
gzip /tmp/testdir/d1/f11
```

Decompress a file  
(.gz file is removed, a new file is created there without .gz extension)

```
gzip -d /tmp/testdir/d1/f11.gz
gunzip /tmp/testdir/d1/f11.gz
```

Compress a file, keep the original file

```
gzip -k /tmp/testdir/d1/f11
```

Decompress a file, keep the .gz file

```
gzip -kd /tmp/testdir/d1/f11.gz
```

Compress all files in a directory  
(All files are removed, new files are created there with .gz extensions)

```
gzip /tmp/testdir/d1/*
```

Decompress all files in a directory

```
gzip -d /tmp/testdir/d1/*
gunzip /tmp/testdir/d1/*
```

Compress all files recursively (including subdirectories)

```
gzip -r /tmp/testdir
```

Decompress all files recursively (including subdirectories)

```
gzip -rd /tmp/testdir
```

Some useful options:

- -l --list: List compressed file contents
- -q --quiet: Suppress all warnings
- -1 --fast: Compress faster
- -9 --best: Compress better

<br>
</details>

<details markdown='1'>
<summary>
2. bzip2
</summary>
---
### 2.1. Info
Installation (Most probably, it is already installed).

```
sudo apt update
sudo apt install bzip2
```

bzip2 compresses (and decompresses) only 1 file, it is not used to prepare a package of files. But it can be combined with tar to make a compressed  package of files.

Provides higher compression ratios compared to gzip, but may be slower.

### 2.2. Usage
Compress a file  
(Original file is removed, a new file is created there with .bz2 extension)

```
bzip2 /tmp/testdir/d1/f11
```

Decompress a file  
(.bz2 file is removed, a new file is created there without .bz2 extension)

```
bzip2 -d /tmp/testdir/d1/f11.bz2
bunzip2 /tmp/testdir/d1/f11.bz2
```

Compress a file, keep the original file

```
bzip2 -k /tmp/testdir/d1/f11
```

Decompress a file, keep the .bz2 file

```
bzip2 -kd /tmp/testdir/d1/f11.bz2
```

Compress all files in a directory  
(All files are removed, new files are created there with .bz2 extensions)

```
bzip2 /tmp/testdir/d1/*
```

Decompress all files in a directory

```
bzip2 -d /tmp/testdir/d1/*
bunzip2 /tmp/testdir/d1/*
```

Some useful options:

- -q --quiet: Suppress all warnings
- -1 --fast: Compress faster
- -9 --best: Compress better

<br>
</details>

<details markdown='1'>
<summary>
3. xz
</summary>
---
### 3.1. Info
Installation (Most probably, it is already installed).

```
sudo apt update
sudo apt install xz-utils
```

xz compresses (and decompresses) only 1 file, it is not used to prepare  a package of files. But it can be combined with tar to make a compressed  package of files.

### 3.2. Usage
Compress a file  
(Original file is removed, a new file is created there with .xz extension)

```
xz /tmp/testdir/d1/f11
```

Decompress a file  
(.gz file is removed, a new file is created there without .gz extension)

```
xz -d /tmp/testdir/d1/f11.xz
unxz /tmp/testdir/d1/f11.xz
```

Compress a file, keep the original file

```
xz -k /tmp/testdir/d1/f11
```

Decompress a file, keep the .xz file

```
xz -kd /tmp/testdir/d1/f11.xz
```

Compress all files in a directory  
(All files are removed, new files are created there with .xz extensions)

```
xz /tmp/testdir/d1/*
```

Decompress all files in a directory

```
xz -d /tmp/testdir/d1/*
unxz /tmp/testdir/d1/*
```

Some useful options:

- -l --list: List compressed file contents
- -q --quiet: Suppress all warnings
- -0: Compress faster
- -9: Compress better

<br>
</details>

<details markdown='1'>
<summary>
4. tar
</summary>
---
#### 4.1. Info
Installation (Most probably, it is already installed)

```
sudo apt update
sudo apt install tar
```

tar actually is an archiving utility, it is used to package files. It can  package many files to a file. It can also transparently be combined with gzip bzip2 and xz tools to compress files. 

### 4.2. Usage
#### 4.2.1. With Compression
Package and compress (with gzip) the contents of a directory (including subdirectories).  
Archive file is created in the current directory.

```
tar -czvf archive.tar.gz /tmp/testdir
```

Decompress and unpackage the archive  
Creates the directory structure under current directory

```
tar -xzvf archive.tar.gz
```

(package) compress & decompress (unpackage) with bzip2

```
tar -cjvf archive.tar.bz2 /tmp/testdir
tar -xjvf archive.tar.bz2
```

(package) compress & decompress (unpackage) with xz

```
tar -cJvf archive.tar.xz /tmp/testdir
tar -xJvf archive.tar.xz
```

See the contents of an archive

```
tar -tvf archive.tar.gz
tar -tvf archive.tar.bz2
tar -tvf archive.tar.xz
```

Extract files to another directory  
Directory must exist.

```
tar -xzvf archive.tar.gz -C /tmp
tar -xjvf archive.tar.bz2 -C /tmp
tar -xJvf archive.tar.xz -C /tmp
```

#### 4.2.2. Without Compression (Archiving)
Tar can be used without compressing too, actually it is the main usage of  the tar command.

All the conditions apply in 4.2.1., if you skip compression options (-z, -j, -J) then you get an archive without compression. This time you can add files to it, or remove files from it.

Archive a directory (and subdirectories)

```
tar -cvf archive.tar /tmp/testdir
```

List the contents

```
tar -tvf archive.tar
```

Unarchive it

```
tar -xvf archive.tar
```

Add a file to the archive

```
tar -rvf archive.tar test.txt
```

Remove a file from the archive

```
tar -vf archive.tar --delete test.txt
```

#### 4.2.3. Options
Tar has tons of options. You can list them all by:

```
tar --help
```

Some selected options:

- -c: Create a new archive.
- -t: List the contents of the archive.    
- -x: Extract files from the archive.
- -v: Verbose mode (show the progress and file names).
- -f: Specify the archive file name.
- -z: Use gzip compression.
- -j: Use bzip2 compression.
- -J: Use xz compression.
- -C: Change to the specified directory before extracting.
- -r: Append files to the end of an archive
- -a: use archive suffix to determine the compression program.
- --delete: delete from the archive
- --exclude=PATTERN: exclude files, given as a PATTERN
- --overwrite: overwrite existing files when extracting
- --remove-files: remove files after adding them to the archive

<br>
</details>

<details markdown='1'>
<summary>
5. zip
</summary>
---
### 5.1. Info
Although gzip, bzip2, xz, and tar is more than enough for compression and archiving; sometimes you may need to exchange files with the unlucky people using Wind*ws. zip tool may be helpful then.

Installation

```
sudo apt update
sudo apt install zip
```

### 5.2. Usage
Compress a file
(File zip file is created in the current dir, original file stays there)

```
zip f11.zip /tmp/testdir/d1/f11
```

Decompress a file
(Decompress to the current dir by creating the directory structure in zip file, zip file stays where it is).

```
unzip f11.zip
```

Compress all the files in a directory

```
zip d1.zip /tmp/testdir/d1/*
```

Compress all the files in a directory including subdirectories

```
zip -r test.zip /tmp/testdir/
```

Compress and encrypt

```
zip -er test.zip /tmp/testdir/
```

List the contents of a zip file

```
unzip -l test.zip
```

Add new files to a zip file

```
zip -u d1.zip /tmp/testdir/d2/*
```

Some options:

- -u: update; only changed or new files
- -d: delete entries in zipfile
- -m: move into zipfile (delete OS files)
- -r: recurse into directories
- -j: junk (don't record) directory names
- -1: compress faster
- -9: compress better
- -q: quiet operation
- -v: verbose operation/print version info
- -x: exclude the following names
- -i: include only the following names
- -e: encrypt

</details>
</summary>

