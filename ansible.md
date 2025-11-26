##### Ansible 
# Ansible Tutorial For Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. The What 

Ansible is an open-source automation tool designed for configuration management, application deployment, and task automation. It enables you to manage servers from a central workstation, simplifying complex workflows through declarative configuration.

This tutorial aims to bring you to an intermediate level of proficiency with Ansible.

(Almost) all examples have been tested and verified as working. There might be minor mistakes; consider them learning opportunities.

While this tutorial focuses on Debian and Ubuntu servers, most concepts can be applied to other Linux distributions.

**Note:** I prepared this tutorial while learning Ansible myself, so it reflects a practical learning journey rather than expert-level knowledge.

### 0.1. Environment

**Workstation:**
- `wrk` -> Debian 13 or Ubuntu 24.04 LTS Desktop

**Hint:** You can use server editions as well, as Ansible does not require a graphical user interface.

### 0.2. Servers:

Local Virtual Servers:
- `debian13` -> Debian 13 Server
- `debian12` -> Debian 12 Server
- `ubuntu24` -> Ubuntu 24.04 LTS Server
- `ubuntu22` -> Ubuntu 22.04 LTS Server
        
### 0.3. Resources:
- Book: 978-1-4842-1660-6 Ansible From Beginner to Pro by Michael Heap
- Book: 978-1-78899-756-0 Mastering Ubuntu Server Second Edition by Jay LaCroix 
- [docs.ansible.com/ansible](https://docs.ansible.com/ansible/)
- [www.howtoforge.com](https://www.howtoforge.com/ansible-guide-ad-hoc-command/)
- [www.golinuxcloud.com](https://www.golinuxcloud.com/ansible-tutorial/)

<br>
</details>

<details markdown='1'>
<summary>
1. Installation and Main Configuration
</summary>

---
Install Ansible on the workstation. **Run on workstation only:**

```
sudo apt update
sudo apt install ansible --yes
```

Create an `ansible` user on all servers and the workstation. **Run on workstation and all servers:**

```
sudo useradd -d /home/ansible -m ansible -s /bin/bash
sudo passwd ansible
```

Add the user to the sudo group:

```
sudo usermod -aG sudo ansible
```

Verify the user was added to the sudo group:

```
getent group sudo
```

Copy the workstation's ansible user SSH key to the servers. **Run only on workstation:**

Switch to the ansible user:

```
sudo su ansible
```

Generate SSH key pair (leave the passphrase empty):

```
ssh-keygen -t rsa
```

Copy the SSH public key to all servers:

```
ssh-copy-id -i ~/.ssh/id_rsa.pub debian13
ssh-copy-id -i ~/.ssh/id_rsa.pub debian12
ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu24
ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu22
```

You should now be able to SSH to all servers as the ansible user without a password.

Configure the ansible user to use sudo without a password on all servers. **Run on all servers:**

Create the sudoers configuration file:

```
sudo nano /etc/sudoers.d/ansible
```

Add the following line:

```
ansible ALL=(ALL) NOPASSWD: ALL
```

Set proper ownership and permissions:

```
sudo chown root:root /etc/sudoers.d/ansible
sudo chmod 440 /etc/sudoers.d/ansible
```

**All preliminary work is now complete.**  
From this point forward, all commands should be run on the workstation unless otherwise specified.
<br>
</details>

<details markdown='1'>
<summary>
2. Configuration
</summary>

---
### 2.1. Configuration File

Ansible looks for configuration files in the following order:
1. File specified by the `ANSIBLE_CONFIG` environment variable
2. `./ansible.cfg` (in the current directory)
3. `~/.ansible.cfg` (in your home directory)
4. `/etc/ansible/ansible.cfg`

We will use option 3 (user-specific configuration).

Switch to the ansible user (if not already done):

```
sudo su ansible
```

Create and edit the Ansible configuration file:

```
nano /home/ansible/.ansible.cfg
```

Add the following content:

```
[defaults]
interpreter_python = auto_silent
inventory = .hosts
remote_user = ansible
roles_path = /home/ansible/ansible/playbooks
forks = 5
```

This configuration specifies:
- Python binary: Find automatically and do not display warning messages
- Inventory file: `/home/ansible/.hosts`
- Remote user: `ansible`
- Additional roles path: `/home/ansible/ansible/playbooks`
- Maximum of 5 parallel tasks

Many other options are available; you can reference `/etc/ansible/ansible.cfg` for examples.


Create a directory structure for Ansible files:

```
mkdir /home/ansible/ansible/playbooks
```

Create the inventory file:

```
touch /home/ansible/.hosts
```

Set appropriate ownership and permissions:

```
sudo chown ansible /home/ansible/.hosts
sudo chmod 600 /home/ansible/.hosts
```

Populate the inventory file with server information:

```
nano /home/ansible/.hosts
```

Add the following content:

```
[debian]
debian13
debian12

[ubuntu]
ubuntu24
ubuntu22
```

You can group hosts as shown above for organizational purposes.

Test the connection to all servers:

```
ansible all -m ping
```

For detailed output:

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
You can specify a custom inventory file for individual commands:

```
ansible all –i /path/to/inventory –m ping
```

To use a non-standard SSH port:

```
host1.example.com:50822
```

Using ranges in hostnames:

```
host[1:3].example.com
host[a:d][a:z].example.com
```

Setting connection parameters per host:

```
alpha.example.com ansible_user=bob ansible_port=50022
bravo.example.com ansible_user=mary ansible_ssh_private_key_file=/path/to/mary.key
frontend.example.com ansible_port=50022
yellow.example.com ansible_host=192.168.33.10
```

**Using Multiple Inventory Files**

You can use a directory containing multiple inventory files:

```
sudo su ansible
mkdir /home/ansible/ansible/inventory
nano /home/ansible/ansible/inventory/inventory1
```

Create the first inventory file:
```
nano /home/ansible/ansible/inventory/inventory1
```
Content:
```
ubuntu24
ubuntu22
```

Create the second inventory file:
```
nano /home/ansible/ansible/inventory/inventory2
```
Content:
```
debian13
debian12
```

Use the inventory directory:
```
ansible all -i /home/ansible/ansible/inventory -m ping
```

**Dynamic Inventory**

You can use scripts that output inventory in JSON format. Create a simple dynamic inventory script:

```
nano /home/ansible/ansible/inventory.py
```

Content:

```
#!/usr/bin/env python3
print('{"ubuntu": {"hosts" : ["ubuntu24", "ubuntu22"]}}')
```

Make it executable and test it:

```
chmod +x /home/ansible/ansible/inventory.py
ansible all -i /home/ansible/ansible/inventory.py -m ping
```

You can combine dynamic and static inventories using the methods above.

**Groups of Groups**

Create parent groups that include other groups using the `children` keyword:

```
[debian]
debian13
debian12

[ubuntu]
ubuntu24
ubuntu22

[ubuntuanddebian:children]
ubuntu
debian
```

**Inventory Variables**

Define variables in your inventory file for hosts or groups:

```
[debian]
debian13
debian12

[ubuntu]
ubuntu24
ubuntu22

[ubuntu:vars]
role="dbserver"
```

This allows you to conditionally install software based on roles (e.g., Apache for webservers, MariaDB for dbservers).

<br>
</details>

<details markdown='1'>
<summary>
4. Ansible Ad Hoc Commands
</summary>

---
Ansible commands can be executed in two ways: ad hoc (direct) or through playbooks. Ad hoc commands are suitable for one-time tasks, while playbooks are better for recurring tasks.

Ping all hosts in the default inventory:

```
ansible all -m ping
```

Ping with custom inventory:

```
ansible all -i /home/ansible/ansible/inventory.py -m ping
ansible all -i /home/ansible/ansible/inventory -m ping
```

Execute shell commands on remote hosts:

```
ansible all -m shell -a "ls -al"
```

The `-m` (module) parameter can be omitted for the `command` module:

```
ansible debian13 -a "ls -al"
```

**File and Directory Operations**

Copy a file to servers:

```
ansible all -m copy -a "src=/tmp/testfile dest=/tmp/testfile"
```

Create a directory:

```
ansible all -m file -a "dest=/tmp/test mode=777 owner=ansible group=ansible state=directory"
```

Delete a file or directory:

```
ansible all -m file -a "dest=/tmp/testfile state=absent"
```

Copy a file from a server to the workstation:

```
ansible debian13 -m fetch -a "src=/var/log/dmesg dest=/home/ansible/backup flat=yes" --become
```

**Reboot Servers**

Attempt to reboot all servers (will fail without proper privileges):

```
ansible all -a "/sbin/reboot"
```

Reboot with sudo privileges:

```
ansible all -a "/sbin/reboot" --become
```

Reboot with increased parallelism:

```
ansible all -a "/sbin/reboot" -f 10 --become
```

Reboot with sudo password prompt:

```
ansible all -a "/sbin/reboot" --become --ask-become-pass
```

**User Management**

Add a user:

```
ansible debian13 -m ansible.builtin.user -a "name=foo" --become
```

Remove a user:

```
ansible debian13 -m ansible.builtin.user -a "name=foo state=absent" --become
```

**Package Management (APT)**

Update package cache:

```
ansible debian13 -m apt -a "update_cache=yes" --become
```

Update cache and upgrade packages:

```
ansible debian13 -m apt -a "upgrade=dist update_cache=yes" --become
```

Install Apache (if not already installed):

```
ansible debian13 -m apt -a "name=apache2 state=present" --become 
```

Install/upgrade Apache to the latest version:

```
ansible debian13 -m apt -a "name=apache2 state=latest" --become
```

Remove Apache:

```
ansible debian13 -m apt -a "name=apache2 state=absent" --become
```

Remove Apache and its configuration files:

```
ansible debian13 -m apt -a "name=apache2 state=absent purge=yes" --become
```

Remove Apache, configurations, and unused dependencies:

```
ansible debian13 -m apt -a "name=apache2 state=absent purge=yes autoremove=yes" --become
```

**Service Management**

Start and enable Apache service:

```
ansible debian13 -m service -a "name=apache2 state=started enabled=yes" --become
```

Stop Apache service:

```
ansible debian13 -m service -a "name=apache2 state=stopped" --become
```

Restart Apache service:

```
ansible debian13 -m service -a "name=apache2 state=restarted" --become
```

<br>
</details>

<details markdown='1'>
<summary>
5. A Simple Playbook to Install Apache
</summary>

---
Playbooks are YAML files that define automation tasks. This playbook will install Apache and deploy a customized homepage.

Create the directory structure:

```
sudo su ansible
mkdir /home/ansible/ansible/playbooks/apache
mkdir /home/ansible/ansible/playbooks/apache/templates
cd /home/ansible/ansible/playbooks/apache
```

Create the playbook file:

```
nano /home/ansible/ansible/playbooks/apache/apache.yml
```

Content:

```
#!/usr/bin/env ansible-playbook
- name: Create webserver with apache
  become: True
  hosts: debian13
  tasks:
  - name: install apache
    apt: name=apache2 update_cache=yes
  - name: copy index.html
    template: src=templates/index.html.j2 dest=/var/www/html/index.html
      mode=0644
  - name: restart apache
    service: name=apache2 state=restarted
```

Create the HTML template:

```
nano /home/ansible/ansible/playbooks/apache/templates/index.html.j2
```

Content:

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

**Playbook Explanation**

- `name: Create webserver with Apache` - Descriptive name for the playbook
- `become: true` - Execute tasks with elevated privileges
- `hosts: debian13` - Target host or group
- `tasks:` - List of tasks to execute
  - Install Apache using the apt module
  - Deploy customized index.html using template module
  - Restart Apache service

**Template Variables**
- `{{ ansible_hostname }}` - Hostname gathered by Ansible facts
- `{{ inventory_hostname }}` - Hostname as defined in the inventory



Run the playbook:

```
ansible-playbook apache.yml
```

Or make it executable and run directly:

```
chmod +x apache.yml
./apache.yml
```

<br>
</details>

<details markdown='1'>
<summary>
6. A More Complex Playbook to Install LAMP
</summary>

---
This playbook installs a complete LAMP (Linux, Apache, MySQL/MariaDB, PHP) stack.

**Steps:**
- Update package cache (`apt update`)
- Install Apache (`apache2`)
- Install MariaDB (`mariadb-server`)
- Install PHP and dependencies (`php`, `libapache2-mod-php`, `php-mysql`)

Create the directory and playbook:

```
sudo su ansible
mkdir /home/ansible/ansible/playbooks/lamp
cd /home/ansible/ansible/playbooks/lamp
```

Create the LAMP playbook:

```
nano /home/ansible/ansible/playbooks/lamp/lamp.yml
```

Content:

```
#!/usr/bin/env ansible-playbook
- name: Install LAMP; Apache, MariaDB, PHP
  become: True
  hosts: debian13
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

Run the playbook:
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
While all Ansible modules are valuable, here are some commonly used ones. Remember that proper indentation is crucial in Ansible playbooks, similar to Python.

**Example Usage Structure:**

```
#!/usr/bin/env ansible-playbook
- name: Tutorial tasks
  become: True
  hosts: debian13
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
      - { hostname: debian13, ip: 192.168.0.231 }
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
      msg: Cannot continue with hostname debian13
    when: inventory_hostname == "debian13"
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
      line: 192.168.0.201 debian13.x386.xyz
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
      line: 192.168.0.201 debian13.x386.xyz
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
Roles allow you to organize playbooks into reusable components. We'll refactor the LAMP stack installation from section 6 into four roles:

- Cache update
- Apache installation
- MariaDB installation
- PHP installation

### 8.1. Role Structure
Create roles using `ansible-galaxy init`. The naming convention is `identifier.role`. We'll use `exforge` as our identifier.

```
ansible-galaxy init exforge.apache
```

This creates a directory structure:
- `README.md` - Documentation
- `defaults/main.yml` - Default variables (lowest priority)
- `files/` - Static files
- `handlers/main.yml` - Service handlers
- `meta/main.yml` - Role metadata
- `tasks/main.yml` - Main tasks file
- `templates/` - Jinja2 templates
- `tests/` - Test cases
- `vars/main.yml` - Role variables (higher priority)

**Note:** Newer Ansible versions may not create `templates` and `files` directories by default, but you should create them when needed.


### 8.2. Preparing LAMP Roles
Create the role directory structure:

```
mkdir -p /home/ansible/ansible/playbooks/roles
cd /home/ansible/ansible/playbooks/roles
```

Initialize the roles:
```
ansible-galaxy init exforge.aptcache
ansible-galaxy init exforge.apache
ansible-galaxy init exforge.mariadb
ansible-galaxy init exforge.php
```


### 8.3. Create the Role-Based Playbook

```
nano /home/ansible/ansible/playbooks/lamp.yml
```

Content:

```
#!/usr/bin/env ansible-playbook
---
- hosts: debian13
  become: true
  roles:
  - exforge.aptcache
  - exforge.apache
  - exforge.mariadb
  - exforge.php
```

Make it executable:

```
chmod +x /home/ansible/ansible/playbooks/lamp.yml
```

**Apt Cache Role**

```
nano /home/ansible/ansible/playbooks/roles/exforge.aptcache/tasks/main.yml
```

Content:

```
---
# tasks file for exforge.aptcache
- name: Update apt cache if not updated in 1 hour
  apt:
    update_cache: yes
    cache_valid_time: 3600
```

**Apache Role**

```
nano /home/ansible/ansible/playbooks/roles/exforge.apache/tasks/main.yml
```

Content:

```
---
# tasks file for exforge.apache
- name: Install apache
  apt:
    name: apache2
    state: present
```

**Mariadb Role**

```
nano /home/ansible/ansible/playbooks/roles/exforge.mariadb/tasks/main.yml
```

Content:

```
---
# tasks file for exforge.mariadb
- name: Install MariaDB
  apt:
    name: mariadb-server
    state: present
```

**PHP Role**

```
nano /home/ansible/ansible/playbooks/roles/exforge.php/tasks/main.yml
```

Content:

```
---
# tasks file for exforge.php
- name: Install PHP and dependencies
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - php
    - libapache2-mod-php
    - php-mysql
```

### 8.4. Running the new playbook

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

Gather all facts for a server:

```
ansible debian13 -m setup
```

The output will be long, something like:

```
debian13 | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "192.168.1.135"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::a00:27ff:feac:87e2"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/01/2006",
        "ansible_bios_vendor": "innotek GmbH",
        "ansible_bios_version": "VirtualBox",
        "ansible_board_asset_tag": "NA",
        "ansible_board_name": "VirtualBox",
        "ansible_board_serial": "NA",
        "ansible_board_vendor": "Oracle Corporation",
        "ansible_board_version": "1.2",
        "ansible_chassis_asset_tag": "NA",
        "ansible_chassis_serial": "NA",
        "ansible_chassis_vendor": "Oracle Corporation",
        "ansible_chassis_version": "NA",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-6.12.48+deb13-amd64",
            "quiet": true,
            "ro": true,
            "root": "UUID=76649b5f-2b95-4d0d-bf4a-4f21f8bbf1bd"
        },
        "ansible_date_time": {
            "date": "2025-11-19",
            "day": "19",
            "epoch": "1763581389",
            "epoch_int": "1763581389",
            "hour": "22",
            "iso8601": "2025-11-19T19:43:09Z",
            "iso8601_basic": "20251119T224309290590",
            "iso8601_basic_short": "20251119T224309",
            "iso8601_micro": "2025-11-19T19:43:09.290590Z",
            "minute": "43",
            "month": "11",
            "second": "09",
            "time": "22:43:09",
            "tz": "+03",
            "tz_dst": "+03",
            "tz_offset": "+0300",
            "weekday": "Wednesday",
            "weekday_number": "3",
            "weeknumber": "46",
            "year": "2025"
        },
        "ansible_default_ipv4": {
            "address": "192.168.1.135",
            "alias": "enp0s3",
            "broadcast": "192.168.1.255",
            "gateway": "192.168.1.1",
            "interface": "enp0s3",
            "macaddress": "08:00:27:ac:87:e2",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "network": "192.168.1.0",
            "prefix": "24",
            "type": "ether"
        },

```

**Accessing Facts in Playbooks:**
- First disk model: `{{ ansible_facts['devices']['xvda']['model'] }}`
- System hostname: `{{ ansible_facts['nodename'] }}`
- Another host's OS: `{{ hostvars['asdf.example.com']['ansible_facts']['os_family'] }}`

**Common Facts:**
- **Date/Time:** `ansible_date_time.date`, `ansible_date_time.time`
- **OS Info:** `ansible_os_family`, `ansible_distribution`, `ansible_distribution_version`
- **Hostname:** `ansible_hostname`

### 9.2. Magic Variables
- `inventory_hostname` - Hostname as in inventory
- `inventory_hostname_short` - Short hostname
- `ansible_play_hosts` - All active hosts in current play
- `ansible_playbook_python` - Python path used by Ansible
- `playbook_dir` - Playbook base directory
- `role_path` - Current role's path (works inside roles)
- `ansible_check_mode` - True if running with `--check`

<br>
</details>

<details markdown='1'>
<summary>
10. Cross-Distribution Compatibility
</summary>

---

Different Linux distributions use different package names and managers:

| Distribution | Web Server | Package Manager |
|-------------|------------|-----------------|
| Debian/Ubuntu | `apache2` | `apt` |
| Alpine Linux | `apache2` | `apk` |
| RHEL/Fedora | `httpd` | `dnf` |

### 10.1. Multi-OS Apache Installation Playbook

```
nano /home/ansible/ansible/playbooks/apache.yml
```

Content:

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

### 10.2. Common OS Families
- **Debian**: Linux Mint, Neon, Raspbian
- **RedHat**: CentOS, Fedora, Oracle Linux, Amazon Linux
- **SUSE**: OpenSUSE, SLES
- **Gentoo**, **Archlinux**, **Solaris**, **Slackware**, **Darwin** (macOS)


### 10.3. Role-Based Multi-OS Approach

```
cd /home/ansible/ansible/playbooks/roles
ansible-galaxy init exforge.apacheDRA
nano /home/ansible/ansible/playbooks/roles/exforge.apacheDRA/tasks/main.yml
```

Content:

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

Content:

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

Content:

```
- name: install apache if RedHat or Alma
  dnf: 
    name: httpd 
    state: present
```

```
nano  /home/ansible/ansible/playbooks/roles/exforge.apacheDRA/tasks/alpine.yml
```

Content:

```
- name: install apache if Alpine
  apk: 
    name: apache2 
    state: present
    update_cache: yes
```

Now we can create a playbook to consume this role:

```
nano  /home/ansible/ansible/playbooks/apacheDRA.yml
```

Content:

```
#!/usr/bin/env ansible-playbook
---
- hosts: all
  become: true
  roles:
  - exforge.apacheDRA
```

Run the playbook:

```
cd /home/ansible/ansible/playbooks
ansible-playbook apacheDRA.yml
```

<br>

</details>

<details markdown='1'>
<summary>
11. Role Variables
</summary>

---

Role variables allow for customizable, reusable roles. This example creates an Apache site with configurable parameters.

Create the apachesite role:

```
cd /home/ansible/ansible/playbooks/roles
ansible-galaxy init exforge.apachesite
mkdir /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates
```
 
Define default variables:
```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/defaults/main.yml
```

Content:

```
---
# defaults file for exforge.apachesite
server_name: www.example.com
server_alias: example.com
html_title: Welcome to {{ ansible_hostname }}
html_header: Welcome to {{ ansible_hostname }}
html_text: This page is created by Ansible
```

**Create Templates**

Apache configuration template:

```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/apache.conf.j2
```

Content:

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

HTML template:

```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/templates/index.html.j2
```

Content:

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

Define tasks:

```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/tasks/main.yml
```

Content:

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

Create and run the playbook:
```
nano /home/ansible/ansible/playbooks/apachesite.yml
```

Content:

```
#!/usr/bin/env ansible-playbook
---
- hosts: debian13
  become: true
  vars:
    server_name: debian13.x386.xyz
    server_alias: debian13
    html_title: debian13.x386.xyz Homepage
    html_header: This is the homepage of debian13.x386.xyz
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
Ansible provides various filters for variable manipulation in templates and playbooks.

**Syntax Filters**

Allows case manipulation: lowercase, uppercase, capital case, title case

- my_message: We are the world
- {{ my_message | lower }}  --> we are the world
- {{ my_message | upper }}  --> WE ARE THE WORLD
- {{ my_message | capitalize }}  --> We are the world
- {{ my_message | title }}  --> We Are The World

**Default Filter**

Using an undefined variable causes an error, to avoid that situation  default filter can be used.

- {{ my_message | default('No message') }}

**List Filters**

List definition is similar to Python: num_list: [1,2,3,4,5,6,7,8,9,0]

Some of the list filters are: max, min and random

- {{ num_list | max }}  --> 9
- {{ num_list | min }}  --> 0
- {{ num_list | random }}  --> a random one

**Pathname Filters**

First, let's define a variable containing a path

```
path: "/etc/apache2/apache2.conf"
```

Two of the most important filters are; dirname and basename

- {{ path | dirname }}   --> /etc/apache2
- {{ path | basename }}  --> apache2.conf

**Date and Time Filters**

- {{ '%d-%m-%Y' | strftime }}  --> Current date
- {{ '%H:%M:%S' | strftime }}  --> Current time
- {{ '%d-%m-%Y %H:%M:%S' | strftime }}  --> Current date and time

**Math Filters**

- {{ num | log }}     --> log of num on base e
- {{ num | log(10) }} --> log of num on base 10
- {{ num | pow(2) }}  --> square of num
- {{ num | root }}    --> square root of num
- {{ num | root(3) }} --> third root of num
- {{ num | abs }}     --> absolute of num
- {{ num | round }}   --> round of num

**Encryption Filters**

- {{ my_message | hash('sha1') }}  --> sha1 hash of variable
- {{ my_message | hash('md5') }}   --> md5 hash of variable
- {{ my_message | checksum }}     --> checksum of variable

**Example Playbook Demonstrating Filters:**

```
nano /home/ansible/ansible/playbooks/filters.yml
```

Content:

```
#!/usr/bin/env ansible-playbook
- name: Demonstration of Filters
  become: True
  hosts: debian13
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

Run the playbook:

```
cd /home/ansible/ansible/playbooks
ansible-playbook filters.yml
```


<br>
</details>

<details markdown='1'>
<summary>
13. Handlers
</summary>

---

### 13.0. Overview

If you want a task to run when something is changed, you can use  handlers. For example, a task tries to change a conf file for apache, and  you need to reload or restart apache if the file is changed. That is when  you use handlers.

You might remember, there is a folder for handlers for the roles. That is where you are expected to put your handlers. 

### 13.1. A Simple Example

Our example playbook will install apache and reload it if it is installed. 

```
nano /home/ansible/ansible/playbooks/simple_handler.yml
```

Content:

```
#!/usr/bin/env ansible-playbook
- name: Simple handler example
  become: true
  hosts: debian13
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

Run the playbook:

```
cd /home/ansible/ansible/playbooks
ansible-playbook simple_handler.yml
```

### 13.2. Handlers in Roles
Let's change the role in apachesite in 11. so that it includes handlers.

First change tasks in tasks folder:

```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/tasks/main.yml
```

Content:

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

Add handlers:


```
nano /home/ansible/ansible/playbooks/roles/exforge.apachesite/handlers/main.yml
```

Content:

```
---
# handlers file for exforge.apachesite
- name: reload_apache
  service:
    name: apache2
    state: reloaded
```

Now you can run the role with handlers by calling the playbook we wrote at 11:

Run the playbook:

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

Ansible provides exception handling similar to Python's try-except-finally.

### 14.1. Block-Rescue-Always Example

A very simple example playbook would be:

```
nano /home/ansible/ansible/playbooks/blocktest.yml
```

```
#!/usr/bin/env ansible-playbook
- name: Demonstration block-rescue-always
  become: True
  hosts: debian13
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

Run the playbook:

```
cd /home/ansible/ansible/playbooks
ansible-playbook blocktest.yml
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
The following topics are beyond this tutorial's scope but are worth exploring:
- Ansible Vault (encryption)
- Ansible Pull
- Ansible Collections
- Automated testing
- Custom module development
- Windows server management

These topics may be valuable for specific use cases but aren't essential for basic to intermediate Ansible proficiency.

</details>

