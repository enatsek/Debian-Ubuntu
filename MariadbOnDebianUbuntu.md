##### MariadbOnDebianUbuntu 
# MariaDB Tutorial on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
Mariadb Installation, configuration, simple user and DB management, and  Primary - Replica (Master - Slave) Replication on Debian 12 (also 11) and  Ubuntu 24.04 (also 22.04) Server.

Based on the book [Mastering Ubuntu Server 2nd Ed.](https://www.packtpub.com/networking-and-servers/mastering-ubuntu-server-second-edition) by Jay LaCroix. This book has introduced me to Ubuntu Server and I have to thank him for this excellent book. 

Almost (if not all) everything on this tutorial can be applied to Mysql.

Mariadb is a fork or Mysql, and I prefer using it, besides a lot of other  reasons, I just don't like Or*cle

**Do not ever install Mariadb and Mysql on the same server**

<br>
</details>

<details markdown='1'>
<summary>
1. Installation and Securing
</summary>

---
### 1.1. Install MariaDB
```
sudo apt update
sudo apt install --yes mariadb-server
```

### 1.2. Check if installation is OK
```
systemctl status mariadb
```

### 1.3. Secure MariaDB
The following command makes some fine tunes regarding Mariadb security.

```
sudo mysql_secure_installation
```

You will be asked some questions.  

`Enter current password for root (enter for none):`  

There is no password yet, so press enter.

The next 2 questions 

`Switch to unix_socket authentication [Y/n]`   
and  
`Change the root password? [Y/n]`   

are about securing root account. In Ubuntu and Debian root account is  already protected, so you can answer n.

For the next questions you can select default answers.

### 1.4. Enter Mariadb shell
`EXIT;` to exit

```
sudo mariadb
```

<br>
</details>

<details markdown='1'>
<summary>
2. Basic User Management
</summary>

---
**All commands must be run on Mariadb shell**

```
sudo mariadb
```

### 2.1. Admin User
For administrating the db, it is best to create an admin user on mariadb shell. admin can only login from localhost  
Remember to change password to a good one.

```
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

### 2.2. To let admin login from anywhere use:
```
CREATE USER 'admin'@'%' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

### 2.3. Give admin full access DB server. 
Can do anything but grant

```
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
```

### 2.4. Following command makes a full admin, with grant permissions
```
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### 2.5. Create a readonly user for DB
```
GRANT SELECT ON *.* TO 'readonlyuser'@'localhost' IDENTIFIED BY 'password';
```

### 2.6. List database users
```
SELECT HOST, USER, PASSWORD FROM mysql.user;
```

### 2.7. Grant a user readonly access for one database
```
GRANT SELECT ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
```

### 2.8. Grant a user full access for a database
```
GRANT ALL ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
```

### 2.9. Show the grants for a particular user:
```
SHOW GRANTS FOR 'appuser'@'localhost';
```

### 2.10. Remove a user
```
DELETE FROM mysql.user WHERE user='myuser' AND host='localhost';
```

<br>
</details>

<details markdown='1'>
<summary>
3. Database Manipulation
</summary>

---
**All commands must be run on Mariadb shell**

### 3.1. Create a database
```
CREATE DATABASE mysampledb;
```

### 3.2. List databases
```
SHOW DATABASES;
```

### 3.3. Enter the workspace of a database
```
USE mysampledb;
```

### 3.4. Create a table
```
CREATE TABLE Employees (Name char(15), Age int(3), Occupation char(15));
```

### 3.5. List columns of a table
```
SHOW COLUMNS IN Employees;
```

### 3.6. Insert a row into a table
```
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
```

### 3.7. List contents of a table
```
SELECT * FROM Employees;
```

### 3.8. Remove an entry from a database
```
DELETE FROM Employees WHERE Name = 'Joe Smith';
```

### 3.9. Drop a table
```
DROP TABLE Employees;
```

### 3.10. Drop an entire database:
```
DROP DATABASE mysampledb;
```

<br>
</details>

<details markdown='1'>
<summary>
4. Backup and Restore
</summary>

---
### 4.1. Backup a database
```
sudo mysqldump --databases mysampledb > mysampledb.sql
```

### 4.2. Restore it
```
sudo mariadb < mysampledb.sql
```

<br>
</details>

<details markdown='1'>
<summary>
5. Primary - Replica (Master-Slave) Replication Configuration
</summary>
### 5.1. Specs and Preliminary Tasks
```
Primary Server       : 192.168.1.216 
Replica Server       : 192.168.1.221 
Replication User     : 'replicate'@'192.168.1.221'
Rep. User Password   : Pass1234 
Database instance to replicate: mysampledb
```

As in the following link, Mariadb Knowledge Base says that; primary and  replica server do not need to have the same version of Mariadb, although  it is preferred to have the primary an older version.  
[MariaDB](https://mariadb.com/kb/en/database-version-on-master-slave-replication/)


Mariadb versions on Debian and Ubuntu Servers:

```
Debian 11    : 10.5.19
Ubuntu 22.04 : 10.6.12
Debian 12    : 10.11.3
Ubuntu 24.04 : 10.11.7
```

I made the tests with the following pairs.
  
- Debian 11 Primary - Debian 12 Replica  
- Ubuntu 22.04 Primary - Ubuntu 24.04 Replica  
- Ubuntu 22.04 Primary - Debian 12 Replica  
   
- Install mariadb on both servers, 
- Apply steps in 1 on both servers
- Apply steps 3.1 to 3.7 on primary server

**Please Remember:**

Replication doesn't mean that you don't have to backup. If you delete   something accidentally, it is automatically deleted at slave too. So if   you are running a production server, backup (at least) daily and weekly.

### 5.2. Primary Server Configuration
#### 5.2.1. Configure primary for bin log
```
sudo nano /etc/mysql/conf.d/mysql.cnf
```

Change as below:

```
[mysql]
[mysqld]
log-bin
binlog-do-db=mysampledb
server-id=1
```

#### 5.2.2. Change bind address to outside
```
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

Change following line (Around lines 27-30)

```
bind-address = 127.0.0.1
```

to

```
bind-address = 0.0.0.0
```

#### 5.2.3. Create replication user
Run following command on primary mariadb shell

```
GRANT REPLICATION SLAVE ON *.* to 'replicate'@'192.168.1.221' identified by 'Pass1234';
EXIT;
```

#### 5.2.4. Restart primary mariadb server
```
sudo systemctl restart mariadb
```

#### 5.2.5. Lock Primary server for initial full replication
Run on Primary server Mariadb shell

```
FLUSH TABLES WITH READ LOCK;
EXIT;
```

#### 5.2.6. Backup the database at the primary server
```
sudo mysqldump --databases mysampledb > mysampledb.sql
```

At this step, you need to copy the backup file (mysampledb.sql) to the replica server.

### 5.3. Replica Server Config
#### 5.3.1. Restore database backed up at primary
```
sudo mariadb < mysampledb.sql
```

#### 5.3.2. Update replica server's conf file
```
sudo nano /etc/mysql/conf.d/mysql.cnf
```

Change as below:

```
[mysql]
[mysqld]
server-id=2
```

For more than 1 replicas, give different server-id numbers

#### 5.3.3. Restart replica mariadb
```
sudo systemctl restart mariadb
```

#### 5.3.4. Run the commands on replica mariadb shell
```
CHANGE MASTER TO MASTER_HOST="192.168.1.216", MASTER_USER='replicate', MASTER_PASSWORD='Pass1234';
```

Check to see if replica is running (on mariadb shell)

```
SHOW SLAVE STATUS;
```

If Slave_IO_State is empty, run (on mariadb shell)

```
START SLAVE;
```

### 5.4. Unlock Primary Mariadb
Run on master mariadb shell

```
UNLOCK TABLES;
```

### 5.5. All set. 
You can try manipulating the DB on the primary, changes will be applied  on the replica slave in a few seconds.

</details>

