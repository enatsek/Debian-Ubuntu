##### AnsibleOnDebianUbuntu 
# Ansible Tutorial For Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. Servers managed from a workstation
This tutorial aims to bring you to a moderate level using Ansible.

(Almost) All examples are tested and verified as working. There might be  slight mistakes and you can think of them as small challenges. 

This tutorial is about using Ansible on Debian and Ubuntu servers, but I  believe you can apply most of the examples to other distributions.

I am not an expert of Ansible. Actually I prepared this tutorial while I  was learning it. 

### 0.1. Workstation: 
wrk -> Debian 12 or Ubuntu 24.04 LTS Desktop

**Hint:** You can use server editions, because Ansible does not need any graphical UI.

### 0.2. Servers:
Local Virtual Servers:

debian12 -> Debian 12 Server  
debian11 -> Debian 11 Server  
ubuntu24 -> Ubuntu 24.04 LTS Server  
ubuntu22 -> Ubuntu 22.04 LTS Server  
        
### 0.3. Resources:
Book: 978-1-4842-1660-6 Ansible From Beginner to Pro by Michael Heap  
Book: 978-1-78899-756-0 Mastering Ubuntu Server Second Edition by Jay LaCroix  
[docs.ansible.com/ansible](https://docs.ansible.com/ansible/)  
[www.howtoforge.com](https://www.howtoforge.com/ansible-guide-ad-hoc-command/)  
[www.golinuxcloud.com](https://www.golinuxcloud.com/ansible-tutorial/)

<br>
</details>

<details markdown='1'>
<summary>
1. Installation and Main Configuration
</summary>

---
### 1.1. Install ansible on workstation
**Run on workstation**

```
sudo apt update
sudo apt install ansible --yes
```

### 1.2. Create ansible user on all the servers and on the workstation
**Run on workstation and on all servers**

Create user ansible and give it a password 

```
sudo useradd -d /home/ansible -m ansible -s /bin/bash
sudo passwd ansible
```

add it to the sudo group

```
sudo usermod -aG sudo ansible
```

make sure it is added

```
getent group sudo
```

### 1.3. Copy workstation's ansible user's ssh key to servers
**Run only on workstation**

Change to ansible user

```
sudo su ansible
```

Create SSH keys, leave passfield empty

```
ssh-keygen -t rsa
```

Copy ansible user's SSH key to the servers

```
ssh-copy-id -i ~/.ssh/id_rsa.pub debian12
ssh-copy-id -i ~/.ssh/id_rsa.pub debian11
ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu24
ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu22
```

Now we can ssh to servers with ansible user without password

### 1.4. On all servers, configure ansible user to sudo without password
**Run on all servers**

create /etc/sudoers.d/ansible file

```
sudo nano /etc/sudoers.d/ansible
```

put the following line in it

```
ansible ALL=(ALL) NOPASSWD: ALL
```

make the file owned by root

```
sudo chown root:root /etc/sudoers.d/ansible
```

change the permissions of file 

```
sudo chmod 440 /etc/sudoers.d/ansible
```

All the preliminary work is completed  
From now on, all the commands will be run on the workstation
<br>
</details>

<details markdown='1'>
<summary>
2. Configuration
</summary>

---
### 2.1. Configuration File
Ansible looks for the configuration file in the following order:

- File specified by the ANSIBLE_CONFIG environment variable
- ./ansible.cfg (ansible.cfg in the current directory)
- ~/.ansible.cfg (.ansible.cfg in your home directory)
- /etc/ansible/ansible.cfg

My choice is to use the 3. option

First change to user ansible (If you haven't done already)

```
sudo su ansible
```

Edit ansible config ifle
```
nano /home/ansible/.ansible.cfg
```

Fill as below:

```
[defaults]
inventory = .hosts
remote_user = ansible
roles_path = /home/ansible/ansible/playbooks
forks = 5
```

We stated as:

- our hosts file will be /home/ansible/.hosts
- the remote user to use on servers is ansible
- look to /home/ansible/ansible/playbooks for extra roles
- maximum 5 parallel tasks between the workstation and servers

There are numerous thing to be configured, you may check them at file /etc/ansible/ansible.cfg


### 2.2. Making a home for Ansible files
I prefer placing all ansible files on /home/ansible/ansible

```
mkdir /home/ansible/ansible
```

And a subdirectory for playbooks (explained later)

```
mkdir /home/ansible/ansible/playbooks
```

### 2.3. Inventory File
Create a clean inventory file

```
touch /home/ansible/.hosts
```

Change ownership and permissions for ansible user

```
sudo chown ansible /home/ansible/.hosts
sudo chmod 600 /home/ansible/.hosts
```

Populate the file with server IPs or names

```
nano /home/ansible/.hosts
```

Fill as below:

```
[debian]
debian12
debian11

[ubuntu]
ubuntu24
ubuntu22
```

As in our example, you can group hosts

### 2.4. A simple test
Ping all our servers

```
ansible all -m ping
```

with full verbose

```
ansible all -m ping -vvvv
```

<br>
</details>

<details markdown='1'>
<summary>
3. More on Inventory
</summary>

---
### 3.1. Command based inventory
It is possible to use a different inventory for each ansible or ansible-playbook command:

```
ansible all –i /path/to/inventory –m ping
```

### 3.2. To use a different ssh port
```
host1.example.com:50822
```

### 3.3. Using ranges in host file names
```
host[1:3].example.com
host[a:d][a:z].example.com
```

### 3.4. Using options for user name, ssh port, ssh private key
```
alpha.example.com ansible_user=bob ansible_port=50022
bravo.example.com ansible_user=mary ansible_ssh_private_key_file=/path/to/mary.key
frontend.example.com ansible_port=50022
yellow.example.com ansible_host=192.168.33.10
```

### 3.5. Using more than 1 inventory
If you want to use more than 1 inventory file you can put all your  inventories in a directory and specify the directory as the inventory file. 

Below is a simple example.

```
sudo su ansible
mkdir /home/ansible/ansible/inventory
nano /home/ansible/ansible/inventory/inventory1
```

Contents:

```
ubuntu24
ubuntu22
```

```
nano /home/ansible/ansible/inventory/inventory2
```

Contents:

```
debian12
debian11
```

```
ansible all -i /home/ansible/ansible/inventory -m ping
```

### 3.6. Dynamic Inventory
If you want to use a dynamic host file, you can use a program which  outputs the inventory in Json format. Then you can give your program as  inventory file. 

Here is a very simple example:

```
sudo su ansible
nano /home/ansible/ansible/inventory.py
```

Fill as below:

```
#!/usr/bin/env python3
print('{"ubuntu": {"hosts" : ["ubuntu24", "ubuntu22"]}}')
```

```
chmod +x /home/ansible/ansible/inventory.py
ansible all -i /home/ansible/ansible/inventory.py -m ping
```

Needless to say; you can combine dynamic and static inventories, by 
combining methods in 3.5. and 3.6.

### 3.7. Groups of Groups
You can create master groups to include other groups. Master groups require children keyword.

In my inventory, if I want to combine all ubuntu adn debian servers I would modify my inventory file as follows:

```
[debian]
debian12
debian11

[ubuntu]
ubuntu24
ubuntu22

[ubuntuanddebian:children]
ubuntu
debian
```

### 3.8. Inventory Variables
You can define variables in inventory file. They might be host or group  based.

For group based variables; var keyword is used. 

Below, using my inventory file, I created a variable named role for a  group and # a host. 

```
[debian]
debian12
debian11

[ubuntu]
ubuntu24
ubuntu22

[ubuntu:vars]
role="dbserver"
```

That way, using ansible, you can install apache to servers with webserver role and install mariadb to servers with role dbserver.

<br>
</details>

<details markdown='1'>
<summary>
4. Ansible Ad Hoc Commands
</summary>

---
You can run Ansible commands in 2 ways, 1 is direct (adhoc), 2 is through  playbooks. 

In the next section we will work on our first playbook. 

Ad hoc commands might be suitable for one time tasks. For recurring tasks it # would be better to use playbooks.

### 4.1. Ping host(s)
Actually we ran our 1st command at 2.4. Ping all hosts in default  inventory.

```
ansible all -m ping
```

We can specify another inventory

```
ansible all -i /home/ansible/ansible/inventory.py -m ping
ansible all -i /home/ansible/ansible/inventory -m ping
```

### 4.2. Run a shell command on hosts
```
ansible all -m shell -a "ls -al"
```
-m can be ommitted

```
ansible ubuntu22 -a "ls -al"
```

List of open ports on the servers

```
ansible all -m shell -a 'netstat -plntu' --become
```

### 4.3. File and Directory Operations
Copy a file to servers

```
ansible all -m copy -a "src=/tmp/testfile dest=/tmp/testfile"
```

Create a directory on server

```
ansible all -m file -a "dest=/tmp/test mode=777 owner=ansible group=ansible state=directory"
```

Delete a file or directory on server

```
ansible all -m file -a "dest=/tmp/testfile state=absent"
```

Copy a file from server

```
ansible ubuntu22 -m fetch -a "src=/var/log/dmesg dest=/home/ansible/backup flat=yes" --become
```

### 4.4. Reboot Servers
Reboot all servers  (Does not reboot because of the permissions)

```
ansible all -a "/sbin/reboot"
```

Reboot all servers with sudo privilege

```
ansible all -a "/sbin/reboot" --become
```

Reboot all servers in 10 parallel forks (default is 5)

```
ansible all -a "/sbin/reboot" -f 10 --become
```

Reboot all servers with sudo privilege, manually enter sudo password

```
ansible all -a "/sbin/reboot" --become --ask-become-pass
```

### 4.5. User Management
Add a user

```
ansible debian12 -m ansible.builtin.user -a "name=foo" --become
```

Remove a user

```
ansible debian12 -m ansible.builtin.user -a "name=foo state=absent" --become
```

### 4.6. Package Management (apt)
Update cache (apt update)

```
ansible debian12 -m apt -a "update_cache=yes" --become
```

update cache and upgrade all modules (apt update && apt upgrade)

```
ansible debian12 -m apt -a "upgrade=dist update_cache=yes" --become
```

Install apache (don't do anything if it is already installed)

```
ansible debian12 -m apt -a "name=apache2 state=present" --become 
```

Install apache, if it is already installed, update it

```
ansible debian12 -m apt -a "name=apache2 state=latest" --become
```

Remove apache

```
ansible debian12 -m apt -a "name=apache2 state=absent" --become
```

Remove apache and remove all configuration about it

```
ansible debian12 -m apt -a "name=apache2 state=absent purge=yes" --become
```

Remove apache, remove all configuration about it, and also remove all unused packages

```
ansible debian12 -m apt -a "name=apache2 state=absent purge=yes autoremove=yes" --become
```

### 4.7. Service Management
Start and Enable Apache service

```
ansible debian12 -m service -a "name=apache2 state=started enabled=yes" --become
```

Stop Apache service

```
ansible debian12 -m service -a "name=apache2 state=stopped" --become
```

Restart Apache service

```
ansible debian12 -m service -a "name=apache2 state=restarted" --become
```

<br>
</details>

<details markdown='1'>
<summary>
5. A Simple Playbook to Install Apache
</summary>

---
Playbooks are files in YAML format. They contain commands to run by  Ansible.

Our playbook will install apache, and prepare a sample homepage  containing the host name

### 5.1. Create directories
```
sudo su ansible
mkdir /home/ansible/ansible/playbooks/apache
mkdir /home/ansible/ansible/playbooks/apache/templates
cd /home/ansible/ansible/playbooks/apache
```

### 5.2. Create ansible file and index.html template
```
nano /home/ansible/ansible/playbooks/apache/apache.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
- name: Create webserver with apache
  become: True
  hosts: debian12
  tasks:
  - name: install apache
    apt: name=apache2 update_cache=yes
  - name: copy index.html
    template: src=templates/index.html.j2 dest=/var/www/html/index.html
      mode=0644
  - name: restart apache
    service: name=apache2 state=restarted
```

```
nano /home/ansible/ansible/playbooks/apache/templates/index.html.j2
```

Fill as below:

```
<html>
<head>
<title>Welcome to ansible on {{ ansible_hostname }}</title>
</head>
<body>
<h1>Apache, configured by Ansible on {{ inventory_hostname }}</h1>
<p>If you can see this, Ansible successfully installed Apache.</p>
</body>
</html>
```

### 5.3. Explanations
- /home/ansible/ansible/playbooks/apache/apache.yml

```
#!/usr/bin/env ansible-playbook
- name: Create webserver with apache
# Name of the playbook, displayed when the playbook runs
  become: True
# Use sudo
  hosts: debian12
# Host or host group to run on
  tasks:
# Tasks to do in this playbook
  - name: install apache
# Name of task, displayed when the playbook runs, install apache
    apt: name=apache2 update_cache=yes
  # Install apache2, first update the cache
  # Equivalent to:
  #   apt update
  #   apt install apache2
  - name: copy index.html
# Name of task, displayed when the playbook runs, copy customized index.html
#   from the template
    template: src=templates/index.html.j2 dest=/var/www/html/index.html
  # variables in index.html.j2 are updated and copied to server
      mode=0644
    # File mode will be 0644
  - name: restart apache
# Name of task, displayed when the playbook runs, restart apache
    service: name=apache2 state=restarted
# Restart apache, systemctl restart apache2
```

Variables in /home/ansible/playbooks/apache/templates/index.html.j2:

{{ ansible_hostname }} : hostname as ansible gathers  
{{ inventory_hostname }} : hostname as in inventory file

### 5.4. Run the playbook
```
ansible-playbook apache.yml
```

or just

```
./apache.yml
```

<br>
</details>

<details markdown='1'>
<summary>
6. A More Complex Playbook to Install LAMP
</summary>

---
### 6.0. Necessary Steps
- Cache Update (sudo apt update)
- Install Apache (sudo apt install apache2)
- Install Mariadb (sudo apt install mariadb-server)
- Install PHP (sudo apt install php libapache2-mod-php php-mysql)

### 6.1. Create Directories
```
sudo su ansible
mkdir /home/ansible/ansible/playbooks/lamp
cd /home/ansible/ansible/playbooks/lamp
```

### 6.2. Create ansible playbook
```
nano /home/ansible/ansible/playbooks/lamp/lamp.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
- name: Install LAMP; Apache, MariaDB, PHP
  become: True
  hosts: debian12
  tasks:
  - name: Update apt cache if not updated in 1 hour
    apt:
      update_cache: yes
      cache_valid_time: 3600
  - name: Install apache
    apt:
      name: apache2
      state: present
  - name: Install MariaDB
    apt:
      name: mariadb-server
      state: present
  - name: Install PHP and dependencies
    apt: 
      name: "{{ item }}"
      state: present
    loop:
      - php
      - libapache2-mod-php
      - php-mysql
```

### 6.3. Run the playbook
```
ansible-playbook lamp.yml
```

<br>
</details>

<details markdown='1'>
<summary>
7. (IMHO) Important Ansible Modules
</summary>

---
Well, actually all of the Ansible modules are important. I just selected  some of them considering my very humble opinion.

To use an example, you have to put it in a playbook or in a role and  apply necessary indentation. Ansible is like Python, indentation is very  important.

Below is a sample, using an example in a playbook

```
#!/usr/bin/env ansible-playbook
- name: Tutorial tasks
  become: True
  hosts: debian12
  tasks:
  - name: Start apache if not started
    service:
      name: apache2
      state: started
```

<br>

### 7.0. apk Module: Manages Alpine Linux apk packages.
Examples:

```
  - name: Install apache, don't do anything if already installed
    apk:
      name: apache2
```

```
  - name: Install apache, don't do anything if already installed
    apk:
      name: apache2
      state: present
```

```
  - name: Install apache, upgrade to latest if already installed
    apk:
      name: apache2
      state: latest
```

```
  - name: Update repositories and install apache
    apk:
      name: apache2
      update_cache: yes
```

```
  - name: Remove apache
    apk:
      name: apache2
      state: absent
```

```
  - name: Install more than 1 packages
    apk:
      name: apache2, php
```

```
  - name: Update cache and update apache to latest
    apk:
      name: apache2
      state: latest
      update_cache: yes
```

```
  - name: Update all packages to their latest version
    apk:
      upgrade: yes
```

```
  - name: Update cache
    apk:
      update_cache: yes
```

<br>


### 7.1. apt Module: Manages Debian/Ubuntu apt packages.
Examples:

```
  - name: Install apache, don't do anything if already installed
    apt:
      name: apache2
```

```
  - name: Install apache, don't do anything if already installed
    apt:
      name: apache2
      state: present
```

```
  - name: Install apache, upgrade to latest if already installed
    apt:
      name: apache2
      state: latest
```

```
  - name: Update repositories and install apache
    apt:
      name: apache2
      update_cache: yes
```

```
  - name: Remove apache
    apt:
      name: apache2
      state: absent
```

```
  - name: Install more than 1 packages
    apt:
      pkg:
      - apache2
      - php
```

```
  - name: Update cache and update apache to latest
    apt:
      name: apache2
      state: latest
      update_cache: yes
```

```
  - name: Install latest php, ignore "install-recommends"
    apt:
      name: php
      state: latest
      install_recommends: no
```

```
  - name: Update all packages to their latest version
    apt:
      name: "*"
      state: latest
```

```
  - name: Upgrade the OS (apt-get dist-upgrade)
    apt:
      upgrade: dist
```

```
  - name: Update cache (apt-get update)
    apt:
      update_cache: yes
```

```
  - name: Update cache if the last update is more than 1 hour
    apt:
      update_cache: yes
      cache_valid_time: 3600
```

```
  - name: Remove unused packages
    apt:
      autoclean: yes
```

```
  - name: Remove unused dependencies
    apt:
      autoremove: yes
```

<br>

### 7.2. blockinfile Module: Insert/update/remove a text block between marked lines 
Examples:

```
  - name: Add or update a block to a html file
    blockinfile:
      path: /var/www/html/index.html
      marker: "<!-- {mark} MANAGED by ANSIBLE BLOCK -->"
    # The block will be wrapped by this marker
    # {mark} is replaced as BEGIN at the beginning
    #   and END at the end.
      insertafter: "<body>"
    # The block with the markers will be inserted after the last
    #   match of this this text. Regexps can be used. If there is no
    #   match or value is EOF, block is added at the end of file.
    # Similarly insertbefore can be used.
      block: |
        <h1>Web server: {{ ansible_hostname }}</h1>
        <p>Update time: {{ ansible_date_time.date }}
        {{ ansible_date_time.time }} </p>
```

```
  - name: Remove previously added block
    blockinfile:
      path: /var/www/html/index.html
      marker: "<!-- {mark} MANAGED by ANSIBLE BLOCK -->"
      block: ""
```

```
  - name: Add mappings to /etc/hosts file, make a backup of file
    blockinfile:
      path: /etc/hosts
      backup: yes
      block: |
        {{ item.ip }} {{ item.hostname }}
      marker: "<!-- {mark} {{ item.hostname }} MANAGED by ANSIBLE BLOCK -->"
    loop:
      - { hostname: debian12, ip: 192.168.0.231 }
      - { hostname: srv2, ip: 192.168.0.232 }
      - { hostname: srv3, ip: 192.168.0.233 }
```
  
<br>  
  
  
### 7.3. command Module: Execute commands
Examples:

```
  - name: Run a command on server and take its output to a variable
    command: free
    register: freevals
```

```
  - name: Run a command if a path does not exist
    command: /usr/sbin/reboot now creates=/etc/flag
```

```
  - name: Run a command if a path does not exist
    command:
      cmd: /usr/sbin/reboot now
      creates: /etc/flag
```

```
  - name: Run a command if a path does not exist
    command:
      argv:
        - /usr/sbin/reboot
        - now
      creates: /etc/flag
```

<br>  
  
### 7.4. copy Module: Copy files to remote servers
Examples

```
  - name: Copy a file with specified owner and permissions, backup the file
    copy:
      src: /home/ansible/main.cf
      dest: /etc/postfix/main.cf
      owner: root
      group: root
      mode: '0644'
      backup: yes
```

```
  - name: Copy a file with specified owner and permissions
    copy:
      src: /home/ansible/main.cf
      dest: /etc/postfix/main.cf
      owner: root
      group: root
      mode: u=rw,g=r,o=r
```

```
  - name: Copy a file with specified owner and permissions
    copy:
      src: /home/ansible/main.cf
      dest: /etc/postfix/main.cf
      owner: root
      group: root
      mode: u+rw,g-wx,o-rwx
```

```
  - name: Copy a file with specified owner and permissions, backup the file
    copy:
      src: /home/ansible/main.cf
      dest: /etc/postfix/main.cf
      owner: root
      group: root
      mode: '0644'
      backup: yes
```

```
  - name: Copy a file on the server to another location
    copy:
      src: /etc/apache2/apache2.conf
      dest: /etc/apache2/apache2.conf.backup
      remote_src: yes
```

```
  - name: Copy an inline text to a file
    copy:
      content: "This file is empty"
      dest: /etc/test
```
  
<br>  
  
### 7.5. debug Module: Print debug messages
Examples:

```
  - name: Display all variables/facts known for a host
    debug:
      var: hostvars[inventory_hostname]
```

```
  - name: Display a message
    debug:
      msg: Working fine so far
```

```
  - name: Print return information from a previous task part 1
    shell: /usr/bin/date
    register: result 
  - name: Print return information from a previous task part 2
    debug:
      var: result.stdout_lines
```

```
  - name: Print multi lines of information from variables part1
    shell: whoami
    register: var1
  - name: Print multi lines of information from variables part2
    shell: who -b
    register: var2
  - name: Print multi lines of information from variables part3
    debug:
      msg:
      - "Information gathered so far:"
      - "1. User name is {{ var1.stdout_lines }}"
      - "2. System is on since {{ var2.stdout_lines }}"
```
  
<br>
  
### 7.6. expect Module: Executes a command and responds to prompts
Examples:

```
  - name: Login to mariadb asking the root password and run a command from a file
    expect:
      command: /bin/bash -c "mariadb -u root -p < /tmp/test.sql"
      responses:
        (.*)password: "password12"
    register: DBUsers
    no_log: true
  # hide your password from log
  - name: Display Result
    debug:
      var: DBUsers.stdout_lines
```

```
  - name: Generic question with multiple different responses
    expect:
      command: command
    # Assuming a command asking 3 questions
      responses:
        Question:
          - Answer 1
          - Answer 2
          - Answer 3
```
  
<br>  
  
### 7.7. fail Module: Fail with a message
Examples:

```
  - name: Stop execution if hostname is something special
    fail:
      msg: Cannot continue with hostname debian12
    when: inventory_hostname == "debian12"
```
  
<br>  
  
### 7.8. fetch Module: Fetch files from server to the workstation
Examples:

```
  - name: Fetch server file, preserve directory information
    fetch:
      src: /etc/apache2/apache2.conf
      dest: /tmp/conf
    # File will be copied to /tmp/conf/hostname/etc/apache2/apache.conf
```

```
  - name: Fetch server file, directly to the specified directory
    fetch:
      src: /etc/apache2/apache2.conf
      dest: /tmp/conf/apache.conf
    # File will be copied to /tmp/conf/apache.conf
    # Consecutive files will be overwritten
      flat: yes
```

```
  - name: Fetch server file, directly to the specified directory
#   directly to the specified directory for every server
    fetch:
      src: /etc/apache2/apache2.conf
      dest: /tmp/conf/{{ inventory_hostname }}/apache.conf
      flat: yes
```
  
<br>  
  
### 7.9. file Module: File and directory management
Examples:

```
  - name: Change ownership and permission of a file
    file:
      path: /tmp/test.conf
      owner: ansible
      group: ansible
      mode: '0644'
```

```
  - name: Create a symbolic link of a file, change ownership of the original file
    file:
      src: /tmp/test.conf
      dest: /home/ansible/test.conf
      owner: ansible
      group: ansible
      state: link
```

```
  - name: Create a hard link
    file:
      src: /tmp/test.conf
      dest: /home/ansible/test.conf
      state: hard
```

```
  - name: Touch a file and set permissions
    file:
      path: /tmp/test.conf
      state: touch
      mode: u=rw,g=r,o=r
```

```
  - name: Touch a file, but preserve its times. 
#  so there is no change if it was touched before
    file:
      path: /tmp/test.conf
      state: touch
      modification_time: preserve
      access_time: preserve
```

```
  - name: Create a directory, do nothing if it already exists
    file:
      path: /tmp/test
      state: directory
      mode: '0755'
```

```
  - name: Update modification and access time of a file to now
    file:
      path: /tmp/test.conf
      state: file
      modification_time: now
      access_time: now
```

```
  - name: Change ownership of a directory recursively 
    file:
      path: /var/www
      state: directory
      recurse: yes
      owner: www-data
      group: www-data
```

```
  - name: Delete a file
    file:
      path: /tmp/test.conf
      state: absent
```

```
  - name: Remove a directory recursively
    file:
      path: /tmp/test
      state: absent
```
  
<br>  
  
### 7.10. geturl Module: Download files
Examples:

```
  - name: Download a file (wordpress)
    get_url:
      url: https://wordpress.org/latest.tar.gz
      dest: /tmp/wordpress.tar.gz
      mode: '0440'
```

```
  - name: Download file with md5 checksum
    get_url:
      url: https://wordpress.org/latest.tar.gz
      dest: /tmp/wordpress.tar.gz
      checksum: md5:4bdc05b00725cc0fb72991d3290e4b8d
```
  
<br>
  
### 7.11. group Module: Linux group management
Examples:

```
  - name: Create a group named admins
    group:
      name: admins
      state: present
```

```
  - name: Create a group named admins gid 1250
    group:
      name: admins
      state: present
      gid: 1250
```

```
  - name: Delete admins group
    group:
      name: admins
      state: absent
```
  
<br>  
  
### 7.12. lineinfile Module: Manage lines in text files
Uses a back referenced rexexp, and puts, updates or deletes a line in a file

Examples:

```
  - name: Change or add the name of an host in /etc/hosts
    lineinfile:
      path: /etc/hosts
      regexp: '^192\.168\.0\.201'
      line: 192.168.0.201 debian12.x386.xyz
```

```
  - name: Remove previously added line in /etc/hosts
    lineinfile:
      path: /etc/hosts
      regexp: '^192\.168\.0\.201'
      state: absent
```

```
  - name: Create a file if it does not exist and add a line
    lineinfile:
      path: /tmp/test
      line: 192.168.0.201 debian12.x386.xyz
      create: yes
```
  
 <br> 
  
### 7.13. pause Module: Pause execution
Examples:

```
  - name: Pause for 5 minutes
    pause:
      minutes: 5
```

```
  - name: Pause for 30 seconds
    pause:
      seconds: 30
```

```
  - name: Pause until prompted
    pause:
```

```
  - name: Pause until prompted with message
    pause:
      prompt : "Press enter to continue"
```

```
  - name: Pause to get password
    pause:
      prompt: "Enter password"
      echo: no
    register: password
```
  
<br>  
  
### 7.14. reboot Module: Reboot server
Examples:

```
  - name: Reboot and connect again
    reboot:
```

```
  - name: Reboot and wait up to 1 hour for connecting again
    reboot:
      reboot_timeout: 3600
```

```
  - name: Display a message to users, wait 5 minutes and reboot
    reboot:
      pre_reboot_delay: 300
      msg: "Rebooting in 5 minutes, please save your work and exit"
```
  
 <br> 
  
### 7.15. replace Module: Replace a string in a file using a back ref regexp
Examples:

```
  - name: Replace all .org names with .com names in /etc/hosts
    replace:
      path: /etc/hosts
      regexp: '(.*)\.org(\s+)'
    # Starts with anything, then comes .org and one or more whitespace
      replace: '\1.com\2'
    # \1 = (.*)   \2 = (\s+)
```

```
  - name: Do the same, but start after and expression and end before another
    replace:
      path: /etc/hosts
      after: 'Start Here'
      before: 'End Here'
      regexp: '(.*)\.org(\s+)'
    # Starts with anything, then comes .org and one or more whitespace
      replace: '\1.com\2'
    # \1 = (.*)   \2 = (\s+)
```

```
  - name: Comment every line containing TEST, backup the original file
    replace:
      path: /tmp/test.sh
      regexp: '^(.*)TEST(.*)$'
      replace: '#\1TEST\2'
      backup: yes
```
  
<br>
  
  
### 7.16. script Module: Transfer and run a script from workstation to server
A script on the worktation is copied to the server(s) and run there

Examples:

```
  - name: Run a script 
    script: /home/ansible/ansible/backup.sh
```

```
  - name: Run a script
    script:
      cmd: /home/ansible/ansible/backup.sh
```

```
  - name: Run a script only if a file does not exist on the server
    script: /home/ansible/ansible/backup.sh
    args:
      creates: /tmp/backup.txt
```

```
  - name: Run a script only if a file exists on the server
    script: /home/ansible/ansible/backup.sh
    args:
      removes: /tmp/backup.txt
```

```
  - name: Run a script using bash
    script: /home/ansible/ansible/backup.sh
    args:
      executable: /bin/bash
```

```
  - name: Run a python script
    script: /home/ansible/ansible/backup.py
    args:
      executable: python3
```
  
 <br> 
  
### 7.17. service Module: Manage services
Examples:

```
  - name: Start apache if not started
    service:
      name: apache2
      state: started
```

```
  - name: Stop apache if started
    service:
      name: apache2
      state: stopped
```

```
  - name: Restart apache
    service:
      name: apache2
      state: restarted
```

```
  - name: Reload apache
    service:
      name: apache2
      state: reloaded
```

```
  - name: Enable apache service, do not touch the state
    service:
      name: apache2
      enabled: yes
```
  
<br>  
  
### 7.18. shell Module: Execute shell commands on servers
Different from command module, redirection and pipes are safe

Examples:

```
  - name: Execute command on remote shell; stdout to a file
    shell: backup.sh >> backup.log
```

```
  - name: Execute command on remote shell; stdout to a file
    shell: 
      cmd: backup.sh >> backup.log
```

```
  - name: Change to a directory before executing a command
    shell: backup.sh >> backup.log
    args:
      chdir: /tmp/
```

```
  - name: command only if a file does not exist
    shell: backup.sh >> backup.log
    args:
      creates: backup.log
```

```
  - name: Change to a directory before executing a command, disable warning
    shell: backup.sh >> backup.log
    args:
      chdir: /tmp/
      warn: no
```
  
<br>  
  
### 7.19. tempfile Module: Create a temporary file or directory
Examples:

```
  - name: Create a temporary directory with suffix tempdir
    tempfile:
      state: directory
      suffix: tempdir
```

```
  - name: Create a temporary file with suffix and save its name to a variable
    tempfile:
      state: file
      suffix: temp
    register: tempfilename
```

```
  - name: Use the variable created above to remove the file
    file:
      path: "{{ tempfilename.path }}"
      state: absent
    when: tempfilename.path is defined
```
  
<br>  
  
  
  
### 7.20. template Module: Copy a file to servers using a template
Unlike file module, you can use variables in template files like in 5.2.

Examples:

```
  - name: Create an html file from a template
    template:
      src: /home/ansible/ansible/playbooks/apache/templates/index.html.j2
      dest: /var/www/html/index.html
      owner: www-data
      group: www-data
      mode: '0660'
```

```
  - name: Create an html file from a template
    template:
      src: /home/ansible/ansible/playbooks/apache/templates/index.html.j2
      dest: /var/www/html/index.html
      owner: www-data
      group: www-data
      mode: u=rw,g=r
```
  
  <br>
  
### 7.21. unarchive Module: Unpack an archive
The archive might be on the workstation or on the server

Examples:

```
  - name: Extract a tar.xz file
    unarchive:
      src: /home/ansible/test.tar.xz
      dest: /tmp
```

```
  - name: Unarchive a file on the server
    unarchive:
      src: /home/ansible/test.zip
      dest: /tmp
      remote_src: yes
```

```
  - name: Download and unpack wordpress
    unarchive:
      src: https://wordpress.org/latest.tar.gz
      dest: /var/www/html
      remote_src: yes
```
      
<br>  
  
### 7.22. user Module: User management
Examples:

```
  - name: Add user exforge with a primary group with the same name
# group must exist
    user:
      name: exforge
      comment: main user
      group: exforge
```

```
  - name: Add user exforge with a primary group with the same name,
#   with a specific uid. group must exist.
    user:
      name: exforge
      comment: main user
      uid: 1111
      group: exforge
```

```
  - name: Add user exforge with bash shell, append the user to www-data and postfix group
    user:
      name: exforge
      shell: /bin/bash
      groups: www-data,postfix
      append: yes
```

```
  - name: Add vmail user with a specific home dir
    user:
      name: vmail
      comment: Postfix Mail User
      uid: 2222
      group: vmail
      home: /var/mail
```

```
  - name: Remove user exforge
    user:
      name: exforge
      state: absent
```

```
  - name: Remove user exforge, remove directories too
    user:
      name: exforge
      state: absent
      remove: yes
```


<br>
</details>

<details markdown='1'>
<summary>
8. Roles
</summary>

---
### 8.0. Introduction
Playbooks can be splitted into roles. That way, we can create reusable  code. The lamp example at 7. will be rewritten using 4 roles:

- Cache Update
- Install Apache
- Install MariaDB
- Install PHP and dependencies

### 8.1. Role Structure
Roles are created with ansible-galaxy init command. Naming convention  for roles is as identifier.role. I use exforge as my identifier, you can  use anything you want. For a role to install apache, my rolename would be exforge.apache: 

```
ansible-galaxy init exforge.apache
```

A directory with role.name is created under the current directory with  the following structure:

- README.md (file)
- defaults (directory)
   - defaults/main.yml  (file)
- files (directory)
- handlers (directory)
   - handlers/main.yml (file)
- meta (directory)
   - meta/main.yml (file)
- tasks (directory)
   - tasks/main.yml (file)
- templates (directory)
- tests (directory)
   - tests/inventory (directory)
   - tests/test.yml (file)
- vars (directory)
   - vars/main.yml (file)

All of the directories and files are optional.

**README.md** file is used for documentation. Expected to contain the  purpose of the role and any other important information.

**defaults/main.yml** is used as a configuration file to define default  variables in the role. Variables in vars/main.yml overrides variables  defined here.

**files** directory is used to place static files. Files used in roles  without any manipulation can be stored here.

**handlers/main.yml** is used to define handlers (like starting, stopping or restarting services). 

**meta/main.yml** is used to contain metadata for the role. Metadata can be used if you want to publish your role to Ansible Galaxy.

**tasks/main.yml** is the main file of the role. Expected to contain role  actions. Actions here will be executed when your role runs.

**templates** directory is used to place template (dynamic) files. The files here can contain variables to interpolate them before using on target  systems.

**test** directory is used to create test playbooks to consume the role.  Mostly used to test roles with a system like Jenkins or Travis.

**vars/main.yml** is similar to defaults/main.yml with an exception.  Variables defined here overrides the variables defined at fact gathering  section. 

Variables defined here also overrides the variables defined in defaults/main.yml.

**Note:** The new version of Ansible, does not create templates and files  directories, but they still exist in the documentation. I am not sure if  it is a bug or something else. In any way, I create this directories when I need them.


### 8.2. Preparing LAMP Roles
We will have 4 roles for LAMP installation. Namely; aptcache, apache,  mariadb and php.

Create a directory for the roles and init the roles:

```
mkdir -p /home/ansible/ansible/playbooks/roles
cd /home/ansible/ansible/playbooks/roles
ansible-galaxy init exforge.aptcache
ansible-galaxy init exforge.apache
ansible-galaxy init exforge.mariadb
ansible-galaxy init exforge.php
```

### 8.3. Create the new playbook with the roles
```
nano /home/ansible/ansible/playbooks/lamp.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
---
- hosts: debian12
  become: true
  roles:
  - exforge.aptcache
  - exforge.apache
  - exforge.mariadb
  - exforge.php
```

Make it executable

```
chmod +x /home/ansible/ansible/playbooks/lamp.yml
```

### 8.4. aptcache role
```
nano /home/ansible/ansible/playbooks/roles/exforge.aptcache/tasks/main.yml
```

Fill as below:

```
---
# tasks file for exforge.aptcache
- name: Update apt cache if not updated in 1 hour
  apt:
    update_cache: yes
    cache_valid_time: 3600
```

### 8.5. apache role
```
nano /home/ansible/ansible/playbooks/roles/exforge.apache/tasks/main.yml
```

Fill as below:

```
---
# tasks file for exforge.apache
- name: Install apache
  apt:
    name: apache2
    state: present
```

### 8.6. mariadb role
```
nano /home/ansible/ansible/playbooks/roles/exforge.mariadb/tasks/main.yml
```

Fill as below:

```
---
# tasks file for exforge.mariadb
- name: Install MariaDB
  apt:
    name: mariadb-server
    state: present
```

### 8.7. php role
```
nano /home/ansible/ansible/playbooks/roles/exforge.php/tasks/main.yml
```

Fill as below:

```
- name: Install PHP and dependencies
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - php
    - libapache2-mod-php
    - php-mysql
```

### 8.8. Running the new playbook
```
cd /home/ansible/ansible/playbooks
ansible-playbook lamp.yml
```

<br>
</details>

<details markdown='1'>
<summary>
9.Ansible Facts and Magic Variables
</summary>

---
### 9.1. Ansible Facts
#### 9.1.1. Getting Facts
Get all facts for debian12 server

```
ansible debian12 -m setup
```

The output will be long, something like:

```
debian12 | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "192.168.0.111"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::a00:27ff:fe10:9"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/01/2006",
        "ansible_bios_version": "VirtualBox",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-5.4.0-48-generic",
            "maybe-ubiquity": true,
            "ro": true,
            "root": "UUID=8842fb18-ffef-4b0d-8c10-419865ae27a2"
        },
        "ansible_date_time": {
            "date": "2020-10-16",
            "day": "16",
            "epoch": "1602869883",
            "hour": "17",
            "iso8601": "2020-10-16T17:38:03Z",
            "iso8601_basic": "20201016T173803661252",
            "iso8601_basic_short": "20201016T173803",
            "iso8601_micro": "2020-10-16T17:38:03.661346Z",
            "minute": "38",
            "month": "10",
            "second": "03",
            "time": "17:38:03",
            "tz": "UTC",
            "tz_offset": "+0000",
            "weekday": "Friday",
            "weekday_number": "5",
            "weeknumber": "41",
            "year": "2020"
        },
        "ansible_system_capabilities_enforced": "True",
        "ansible_system_vendor": "innotek GmbH",
        "ansible_uptime_seconds": 244,
        "ansible_user_dir": "/home/ansible",
        "ansible_user_gecos": "",
        "ansible_user_gid": 1001,
        "ansible_user_id": "ansible",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 1001,
        "ansible_userspace_architecture": "x86_64",
        "ansible_userspace_bits": "64",
        "ansible_virtualization_role": "guest",
        "ansible_virtualization_type": "virtualbox",
        "discovered_interpreter_python": "/usr/bin/python3",
        "gather_subset": [
            "all"
        ],
        "module_setup": true
    },
    "changed": false
```

#### 9.1.2. Accessing Ansible Facts
You can use any value from the facts as a variable. Some examples:

Model of first disk: `{{ ansible_facts['devices']['xvda']['model'] }}`  
System hostname : `{{ ansible_facts['nodename'] }}`  

Using another system's fact:  
`{{ hostvars['asdf.example.com']['ansible_facts']['os_family'] }}`

#### 9.1.3. Important Ansible Facts
Date and time

- ansible_date_time.date -->  "2020-11-11"
- ansible_date_time.time -->  "08:44:06"

OS

- ansible_os_family      -->  "Debian" for Debian and Ubuntu, "RedHat" for CentOS
- ansible_distribution   -->  "Ubuntu" for Ubuntu, "Debian" for Debian, "CentOS" for CentOS
- ansible_hostname       -->  "test201"
- ansible_distribution_version --> "20.04"

### 9.2. Ansible Magic Variables
- inventory_hostname: Hostname as in inventory
- inventory_hostname_short: Hostname as in inventory short format
- ansible_play_hosts: list of all hosts still active in the current play.
- ansible_play_batch: list of hostnames that are in scope for the current ‘batch’ of the play.
- ansible_playbook_python: Path to the python executable used to invoke the Ansible command line tool.
- inventory_dir: Pathname of the directory holding Ansible’s inventory 
- inventory_file: Pathname and the filename pointing to the Ansible’s inventory host file.
- playbook_dir: Playbook base directory.
- role_path: current role’s pathname and only works inside a role.
- ansible_check_mode: Boolean, set to True if you run Ansible with --check.

<br>
</details>

<details markdown='1'>
<summary>
10. Distinguishing Linux Distribution
</summary>

---
Debian and Ubuntu name Apache Server as apache2 and use apt package  manager. 

Alpine also names Apache Server as apache2 and uses apk package manager.

RHEL (and Alma & Rocky) names it as httpd and use dnf package manager. 

Our example role will distinguish the distribution and call appropriate  tasks.

### 10.1. A Playbook to install Apache on Ubuntu (and Debian) and Alma (and Redhat)

```
nano /home/ansible/ansible/playbooks/apache.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
- name: Install Apache on Ubuntu (Debian), RHEL (Alma) and Alpine
  become: True
  hosts: all
  tasks:
  - name: install apache if Ubuntu or Debian
    apt: 
      name: apache2 
      update_cache: yes
    when: ansible_os_family == "Debian"
  - name: install apache if Redhat or Alma
    dnf: 
      name: httpd
    when: (ansible_os_family == "RedHat") or (ansible_os_family == "AlmaLinux")
  - name: install apache if Alpine
    apk: 
      name: apache2 
      update_cache: yes
    when: ansible_os_family == "Alpine"
```

### 10.2. Other OS Families
Some of the other possible ansible_os_family options are:

- "Debian" for Linux Mint, Neon, KDE Neon, Raspbian
- "RedHat" for Centos, Fedora, Scientific, CloudLinux, PSBM, OracleLinux, Amazon
- "AlmaLinux" for Alma
- "Suse" for Suse, OpenSuSe, SLES, SLED
- "Gentoo" for Gentoo
- "Archlinux" for ArchLinux, Manjaro
- "Mandrake" for Mandrake, Mandriva
- "Solaris"  for Solaris, Nexenta, OnmiOS, OpenIndiana, SmartOS
- "Slackware" for Slackware
- "Darwin" for MacOSX

### 10.3. A Role to install Apache on Ubuntu (Debian), Alma (Redhat), and Alpine
```
cd /home/ansible/ansible/playbooks/roles
ansible-galaxy init exforge.apacheDRA
nano /home/ansible/ansible/playbooks/roles/exforge.apacheDRA/tasks/main.yml
```

Fill as below:

```
---
# tasks file for exforge.apacheDRA
- include_tasks: debian.yml
  when: ansible_os_family == "Debian"
- include_tasks: redhat.yml
  when: (ansible_os_family == "RedHat") or (ansible_os_family == "AlmaLinux")
- include_tasks: alpine.yml
  when: ansible_os_family == "Alpine"
```

```
nano  /home/ansible/ansible/playbooks/roles/exforge.apacheDRA/tasks/debian.yml
```

Fill as below:

```
- name: install apache if Ubuntu or Debian
  apt: 
    name: apache2 
    state: present
    update_cache: yes
```

```
nano  /home/ansible/ansible/playbooks/roles/exforge.apacheDRA/tasks/redhat.yml
```

Fill as below:

```
- name: install apache if RedHat or Alma
  dnf: 
    name: httpd 
    state: present
```

```
nano  /home/ansible/ansible/playbooks/roles/exforge.apacheDRA/tasks/alpine.yml
```

Fill as below:

```
- name: install apache if Alpine
  apk: 
    name: apache2 
    state: present
    update_cache: yes
```

Now we can create a playbook to consume this role

```
nano  /home/ansible/ansible/playbooks/apacheDRA.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
---
- hosts: all
  become: true
  roles:
  - exforge.apacheDRA
```

Run the playbook

```
cd /home/ansible/ansible/playbooks
ansible-playbook apacheDRA.yml
```

### 10.4. Exercise
Redesign apacheDRA role, using package module.

<br>

</details>

<details markdown='1'>
<summary>
11. Role Variables
</summary>

---
You can set role variables when you consume a role in a playbook. The  variables are defined in the roles and can be set values at the playbook.

Our example will install apache (if it is not installed), create a  configuration with the given site name and create a default page with the  given parameters.

After creating the role, default variables will be defined in defaults/main.yml dir, apache conf file and html templates will be created at  templates/ dir, and role tasks will be coded at tasks/main.yml. After all, we will create a playbook, set all variables there and run the role.

### 11.1. Create the apachesite role
```
cd /home/ansible/ansible/playbooks/roles
ansible-galaxy init exforge.apachesite
mkdir /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates
```
 
### 11.2. Define Variables
```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/defaults/main.yml
```

Fill as below:

```
---
# defaults file for exforge.apachesite
server_name: www.example.com
server_alias: example.com
html_title: Welcome to {{ ansible_hostname }}
html_header: Welcome to {{ ansible_hostname }}
html_text: This page is created by Ansible
```

### 11.3. Create Apache conf file and index.html file templates
```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/apache.conf.j2
```

Fill as below:

```
<VirtualHost *:80>
  ServerAdmin webmaster@{{ server_name }}
  ServerName {{ server_name }}
  ServerAlias {{ server_alias }}
  DocumentRoot /var/www/{{ server_name }}
  ErrorLog ${APACHE_LOG_DIR}/{{ server_name }}-error.log
  CustomLog ${APACHE_LOG_DIR}/{{ server_name }}-access.log combined
</VirtualHost>
```

```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/index.html.j2
```

Fill as below:

```
<html>
<head>
<title>{{ html_title }}</title>
</head>
<body>
<h1>{{ html_header }}</h1>
<p>{{ html_text }}</p>
</body>
</html>
```

### 11.4. Create Tasks
```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/tasks/main.yml
```

Fill as below:

```
---
# tasks file for exforge.apachesite
- name: Stop execution if OS is not in Debian family
  fail:
    msg: Only works on Debian and her children (Ubuntu, Mint, ..)
  when: ansible_os_family != "Debian"
- name: Install apache2 if not already installed
  apt: 
    name: apache2 
    state: present
    update_cache: yes
- name: Create apache conf file from the template
# File is named as servername.conf and will be put in /etc/apache2/sites-available
  template:
    src: /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/apache.conf.j2
    dest: /etc/apache2/sites-available/{{ server_name }}.conf
    mode: "0644"
    owner: root
    group: root
- name: Enable new conf
# It will be enabled if we create a link to this conf file in /etc/apache2/sites-enabled
  file:
    src: /etc/apache2/sites-available/{{ server_name }}.conf
    dest: /etc/apache2/sites-enabled/{{ server_name }}.conf
    owner: root
    group: root
    state: link
- name: Create home directory for the site
# Home directory will be /var/www/server_name
  file:
    path: /var/www/{{ server_name }}
    state: directory
    mode: "0770"
    owner: www-data
    group: www-data
- name: Copy index.html to site's home directory
  template:
    src: /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/index.html.j2
    dest: /var/www/{{ server_name }}/index.html
    mode: "0644"
    owner: www-data
    group: www-data
- name: Reload apache2
  service:
    name: apache2
    state: reloaded
```

### 11.5. Create a playbook and consume the role
```
nano /home/ansible/ansible/playbooks/apachesite.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
---
- hosts: debian12
  become: true
  vars:
    server_name: debian12.x386.xyz
    server_alias: debian12
    html_title: debian12.x386.xyz Homepage
    html_header: This is the homepage of debian12.x386.xyz
    html_text: This is a sample page created by Ansible    
  roles:
  - exforge.apachesite
```

Run the playbook

```
cd /home/ansible/ansible/playbooks
ansible-playbook apachesite.yml
```

<br>
</details>

<details markdown='1'>
<summary>
12. Variable Filters
</summary>

---
There are a number of filters available for the variables used in  templates, playbooks and roles.

### 12.1. Syntax Filters
Allows case manipulation: lowercase, uppercase, capital case, title case

- my_message: We are the world
- {{ my_message | lower }}  --> we are the world
- {{ my_message | upper }}  --> WE ARE THE WORLD
- {{ my_message | capitalize }}  --> We are the world
- {{ my_message | title }}  --> We Are The World

### 12.2. Default Filter
Using an undefined variable causes an error, to avoid that situation  default filter can be used.

- {{ my_message | default('No message') }}

### 12.3. List Filters
List definition is similar to Python: num_list: [1,2,3,4,5,6,7,8,9,0]

Some of the list filters are: max, min and random

- {{ num_list | max }}  --> 9
- {{ num_list | min }}  --> 0
- {{ num_list | random }}  --> a random one

### 12.4. Pathname Filters
First, let's define a variable containing a path

```
path: "/etc/apache2/apache2.conf"
```

Two of the most important filters are; dirname and basename

- {{ path | dirname }}   --> /etc/apache2
- {{ path | basename }}  --> apache2.conf

### 12.5. Date and Time Filters
- {{ '%d-%m-%Y' | strftime }}  --> Current date
- {{ '%H:%M:%S' | strftime }}  --> Current time
- {{ '%d-%m-%Y %H:%M:%S' | strftime }}  --> Current date and time

### 12.6. Math Filters
- {{ num | log }}     --> log of num on base e
- {{ num | log(10) }} --> log of num on base 10
- {{ num | pow(2) }}  --> square of num
- {{ num | root }}    --> square root of num
- {{ num | root(3) }} --> third root of num
- {{ num | abs }}     --> absolute of num
- {{ num | round }}   --> round of num

### 12.7. Encryption Filters
- {{ my_message | hash('sha1') }}  --> sha1 hash of variable
- {{ my_message | hash('md5') }}   --> md5 hash of variable
- {{ my_message | checksum }}     --> checksum of variable

### 12.8. An Example Playbook to Cover all the Filters Here
```
nano /home/ansible/ansible/playbooks/filters.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
- name: Demonstration of Filters
  become: True
  hosts: debian12
  vars:
    my_message: "We are the world"
    num_list: [1,2,3,4,5,6,7,8,9,0]
    path: "/etc/apache2/apache2.conf"
    num: 85
    num2: -8
    num3: 2.6
  tasks:
  - name: All the filters
    debug:
      msg:
        - "My original message: {{ my_message }}"
        - "My message in lowercase: {{ my_message | lower }}"
        - "My message in upper: {{ my_message | upper }}"
        - "My message in sentence case: {{ my_message | capitalize }}"
        - "My message in title case: {{ my_message | title }}"
        - "Sha1 hash of my message: {{ my_message | hash('sha1') }}"
        - "Md5 hash of my message: {{ my_message | hash('md5') }}" 
        - "checksum of my message: {{ my_message | checksum }}"
        - "---"
        - "Default value: {{ my_message2 | default('No message') }}"
        - "---"
        - "My list: {{ num_list }}"
        - "Maximum of list: {{ num_list | max }}"
        - "Minimum of list: {{ num_list | min }}"
        - "A random item of list: {{ num_list | random }}"
        - "---"
        - "Path: {{path}}"
        - "Directory of path: {{ path | dirname }}"
        - "Filename of path: {{ path | basename }}"
        - "---"
        - "Current date: {{ '%d-%m-%Y' | strftime }}"
        - "Current time: {{ '%H:%M:%S' | strftime }}"
        - "Current date and time: {{ '%d-%m-%Y %H:%M:%S' | strftime }}"
        - "---"
        - "e base log of {{ num }}: {{ num | log }}"
        - "10 base log of {{ num }}: {{ num | log(10) }}"
        - "Square of {{ num }}: {{ num | pow(2) }}"
        - "4th power of {{ num }}: {{ num | pow(4) }}"
        - "Square root of {{ num }}: {{ num | root }}"
        - "3rd root of {{ num }}: {{ num | root(3) }}"
        - "Absolute of {{ num2 }}: {{ num2 | abs }}"
        - "Round of {{ num3 }}: {{ num3 | round }}"
```

<br>
</details>

<details markdown='1'>
<summary>
13. Handlers
</summary>

---
If you want a task to run when something is changed, you can use  handlers. For example, a task tries to change a conf file for apache, and  you need to reload or restart apache if the file is changed. That is when  you use handlers.

You might remember, there is a folder for handlers for the roles. That is where you are expected to put your handlers. 

### 13.1. A Simple Example
Our example playbook will install apache and reload it if it is  installed. 

```
nano /home/ansible/ansible/playbooks/simple_handler.yml
```

Fill as below:

```
#!/usr/bin/env ansible-playbook
- name: Simple handler example
  become: true
  hosts: debian12
  tasks:
  - name: Install Apache
    apt:
      name: apache2
      state: present
    notify: restart_apache
  handlers:
  - name: restart_apache
    service:
      name: apache2
      state: restarted
```

### 13.2. Handlers in Roles
Let's change the role in apachesite in 11. so that it includes handlers.

First change tasks in tasks folder:

```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/tasks/main.yml
```

Fill as below:

```
---
# tasks file for exforge.apachesite
- name: Stop execution if OS is not in Debian family
  fail:
    msg: Only works on Debian and her children (Ubuntu, Mint, ..)
  when: ansible_os_family != "Debian"
- name: Install apache2 if not already installed
  apt: 
    name: apache2 
    state: present
    update_cache: yes
- name: Create apache conf file from the template
# File is named as servername.conf and will be put in /etc/apache2/sites-available
  template:
    src: /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/apache.conf.j2
    dest: /etc/apache2/sites-available/{{ server_name }}.conf
    mode: "0644"
    owner: root
    group: root
  notify: reload_apache
- name: Enable new conf
# It will be enabled if we create a link to this conf file in 
#   /etc/apache2/sites-enabled
  file:
    src: /etc/apache2/sites-available/{{ server_name }}.conf
    dest: /etc/apache2/sites-enabled/{{ server_name }}.conf
    owner: root
    group: root
    state: link
  notify: reload_apache
- name: Create home directory for the site
# Home directory will be /var/www/server_name
  file:
    path: /var/www/{{ server_name }}
    state: directory
    mode: "0770"
    owner: www-data
    group: www-data
  notify: reload_apache
- name: Copy index.html to site's home directory
  template:
    src: /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/index.html.j2
    dest: /var/www/{{ server_name }}/index.html
    mode: "0644"
    owner: www-data
    group: www-data
  notify: reload_apache
```


Handlers run after the play is finished, so if a handler is called twice  (or more), it will run only once.

Add handlers


```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/handlers/main.yml
```

Fill as below:

```
---
# handlers file for exforge.apachesite
- name: reload_apache
  service:
    name: apache2
    state: reloaded
```

Now you can run the role with handlers by calling the playbook we wrote at 11:

Run the playbook

```
cd /home/ansible/ansible/playbooks
ansible-playbook apachesite.yml
```

<br>
</details>

<details markdown='1'>
<summary>
14. Error Recovery (Block and rescue)
</summary>

---
Ansible has an exception handling (error recovery) mechanism similar to  Python's try-except-finally block.

### 14.1. Block-Rescue-Always usage
A very simple example playbook would be:

```
nano /home/ansible/ansible/playbooks/blocktest.yml
```

```
#!/usr/bin/env ansible-playbook
- name: Demonstration block-rescue-always
  become: True
  hosts: debian12
  vars:
    message1: "1. Message"
    message2: "2. Message"
  tasks:
  - block:
    - name: Task 1
      debug:
        msg: "{{ message1 }}"
    - name: Task 2
      debug:
        msg: "{{ message2 }}"
    - name: Task 3  (Error expected, variable is not defined)
      debug:
        msg: "{{ message3 }}"
    - name: Task 4  (Never expected to run)
      debug:
        msg: "{{ message4 }}"
    rescue:
      - name: Rescue Task
        debug:
          msg: "Some of the messages could not be displayed"
    always:
      - name: Always Task
        debug:
          msg: "Job finished"
```

### 14.2. Explanations
Tasks in the block (Tasks 1, 2, 3 and 4 in our example) run  sequentially. 

If an error occurs in any task (Task 3 in our example), execution stops  and the control goes to rescue task. Then the tasks in rescue block  (Rescue Task in our example) run. Then the tasks in always block (Always  task in our example) run.

If there are no errors in tasks, rescue block is skipped and the tasks in always block (Always task in our example) run.

Error recovery is a very important subject in all kinds of programming. I believe you should use it as much as possible to prevent an unexpected  termination of programs (playbooks for ansible).

<br>
</details>

<details markdown='1'>
<summary>
15. Skipped Content
</summary>

---
I skipped the following subjects just because I think I won't use them. I believe most of you won't use them ever. 

- Ansible vault
- Ansible pull
- Ansible collections
- Testing (with a test tool)
- Writing your own modules
- Using Ansible on Windows servers
- And may be some more that I am not able to know now :)

</details>

