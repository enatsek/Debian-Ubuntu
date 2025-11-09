Can you grammatically and semantically check and correct if necessary text below:



##### MariadbOnDebianUbuntu 
# MariaDB Tutorial on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.0. The What

This tutorial covers MariaDB installation, configuration, basic user and database management, and Primary-Replica (Master-Slave) Replication on Debian 12/13 and Ubuntu 22.04/24.04 Servers.

### 0.1. Environment

- **Server Distro:** Debian 12/13 or Ubuntu 22.04/24.04 LTS Server

### 0.2. Sources

- [Mastering Ubuntu Server 2nd Ed.](https://www.packtpub.com/networking-and-servers/mastering-ubuntu-server-second-edition) by Jay LaCroix. 

### 0.3. Notes

Almost everything in this tutorial (if not all) can be applied to MySQL.

MariaDB is a fork of MySQL. I prefer using it for a variety of reasons, one of which is simply a preference to avoid Oracle's products.

**Warning: Do not install MariaDB and MySQL on the same server.**

<br>
</details>

<details markdown='1'>
<summary>
1. Installation and Securing
</summary>

---

Install MariaDB:

```
sudo apt update
sudo apt install --yes mariadb-server
```

Check if MariaDB is running:

```
systemctl status mariadb
```

Run the security script to apply basic security settings to MariaDB:

```
sudo mariadb-secure-installation
```

You will be asked a series of questions. Here are recommended answers:

- `Enter current password for root (enter for none):`  
  Press **Enter** as there is no password set yet.

- `Switch to unix_socket authentication [Y/n]`  
  The root account is already protected on Debian/Ubuntu. You can answer **`n`**.

- `Change the root password? [Y/n]`  
  For the same reason, you can answer **`n`**.

- For the remaining questions (remove anonymous users, disallow root login remotely, remove test database, reload privilege tables), it is safe to accept the defaults by pressing **`Y`**.


Enter the MariaDB shell (use `EXIT;` or `QUIT;` to exit):

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
**All commands in this section must be run within the MariaDB shell.**

Enter the MariaDB shell:

```
sudo mariadb
```

For database administration, it is best practice to create a dedicated admin user. The following command creates an admin user that can only log in from `localhost`. Remember to change `'password'` to a strong password.

```
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

To allow the admin user to log in from any host, use:

```
CREATE USER 'admin'@'%' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

Grant the admin user full access to the DB server (can do anything except grant privileges to others):

```
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
```

To create a user with full administrative privileges, including the ability to grant permissions to others:

```
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

Create a read-only user for all databases:

```
GRANT SELECT ON *.* TO 'readonlyuser'@'localhost' IDENTIFIED BY 'password';
```

List all database users:

```
SELECT HOST, USER, PASSWORD FROM mysql.user;
```

Grant a user read-only access to a specific database:

```
GRANT SELECT ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
```

Grant a user full access to a specific database:

```
GRANT ALL ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
```

Show the grants for a specific user:

```
SHOW GRANTS FOR 'appuser'@'localhost';
```

Remove a user:
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
**All commands in this section must be run within the MariaDB shell.**

Enter MariaDB shell:

```
sudo mariadb
```

Create a database:

```
CREATE DATABASE mysampledb;
```

List all databases:

```
SHOW DATABASES;
```

Switch to a specific database (enter its workspace):

```
USE mysampledb;
```

Create a table:

```
CREATE TABLE Employees (Name char(15), Age int(3), Occupation char(15));
```

List the columns of a table:

```
SHOW COLUMNS IN Employees;
```

Insert a row into a table:

```
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
```

List the contents of a table:

```
SELECT * FROM Employees;
```

Remove an entry from a table:

```
DELETE FROM Employees WHERE Name = 'Joe Smith';
```

Drop a table:

```
DROP TABLE Employees;
```

Drop an entire database:
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

Backup a specific database to a file:

```
sudo mysqldump --databases mysampledb > mysampledb.sql
```

Restore a database from a backup file:

```
sudo mariadb < mysampledb.sql
```

<br>
</details>

<details markdown='1'>
<summary>
5. Primary - Replica (Master-Slave) Replication Configuration
</summary>
---

### 5.0. Specs and Preliminary Tasks

```
Primary Server            : 192.168.1.144 
Replica Server            : 192.168.1.145
Replication User          : 'replicate'@'192.168.1.145'
Replication User Password : Pass1234 
Database to replicate     : mysampledb
```

Mariadb Knowledge Base says that; primary and  replica server do not need to have the same version of Mariadb, although  it is preferred that the primary to have an older version: [MariaDB](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-overview).

Mariadb versions on Debian and Ubuntu Servers:

```
Ubuntu 22.04 : 10.6.12
Debian 12    : 10.11.3
Ubuntu 24.04 : 10.11.7
Debian 13    : 11.8.3
```

This tutorial has been tested with the following pairs:
- Ubuntu 22.04 Primary - Ubuntu 24.04 Replica
- Debian 12 Primary - Debian 13 Replica
- Ubuntu 24.04 Primary - Debian 13 Replica

   
**Preliminary Setup:**

- Install MariaDB on both servers.
- Complete the steps in **Section 1** on both servers.
- Complete the steps in **Section 3** on the primary server (create the database and table, but do not delete or drop anything).


**Important Note:**

Replication is not a substitute for backups. If you accidentally delete data on the primary, it will also be deleted on the replica. For production servers, implement a robust backup strategy (e.g., daily and weekly backups).

### 5.1. Primary Server Configuration

Configure the primary server for binary logging:

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

Modify the `bind-address` to allow connections from the replica:

```
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

Find the line (around lines 27-30):

```
bind-address = 127.0.0.1
```

Change it to:

```
bind-address = 0.0.0.0
```

Create a dedicated user for replication on the primary server:

```
sudo mariadb
```

Run the following command in the MariaDB shell:

```
GRANT REPLICATION REPLICA ON *.* to 'replicate'@'192.168.1.145' identified by 'Pass1234';
FLUSH PRIVILEGES;
EXIT;
```


Restart the MariaDB service on the primary server:

```
sudo systemctl restart mariadb
```

Lock the primary server's databases to prepare for the initial replication snapshot:

```
sudo mariadb
```


Run the following command in the MariaDB shell:

```
FLUSH TABLES WITH READ LOCK;
EXIT;
```

Backup the database on the primary server

```
sudo mysqldump --databases mysampledb > mysampledb.sql
```

At this step, you need to transfer the backup file (mysampledb.sql) to the replica server.

### 5.2. Replica Server Configuration

Restore the backup on the replica server:

```
sudo mariadb < mysampledb.sql
```

Update the replica server's configuration file

```
sudo nano /etc/mysql/conf.d/mysql.cnf
```

Change as below:

```
[mysql]
[mysqld]
server-id=2
```

*For environments with more than one replica, assign a unique `server-id` to each.*

Restart the MariaDB service on the replica server:

```
sudo systemctl restart mariadb
```

Configure the replica to connect to the primary. Enter the MariaDB shell on the replica:

```
sudo mariadb
```

Point to the primary server:

```
CHANGE MASTER TO MASTER_HOST="192.168.1.144", MASTER_USER='replicate', MASTER_PASSWORD='Pass1234', MASTER_SSL=0, MASTER_SSL_VERIFY_SERVER_CERT=0;
START REPLICA;
```


Check the replication status to ensure it is running correctly:

```
SHOW REPLICA STATUS\G
```
Look for `Slave_IO_Running: Yes` and `Slave_SQL_Running: Yes` in the output.

### 5.3. Unlock the Primary Server

On the primary server, unlock the tables to resume normal operations:

```
sudo mariadb
```

Run the following command in the MariaDB shell:

```
UNLOCK TABLES;
EXIT;
```

**Configuration Complete.**

You can now test the setup by manipulating data in the `mysampledb` database on the primary server. Changes should be replicated to the replica server within seconds.
</details>

