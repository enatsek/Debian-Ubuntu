##### PostgresqlOnUbuntu 
# Postgresql Tutorial On Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.0. Notes
Debian 12 and Ubuntu 24.04 LTS Server has packages for different versions of Postgresql (15 and 16). 

For the ease of following the tutorials, I prepared different versions  for Debian and Ubuntu.

### 0.1. Infrastructure
Server:
- Ubuntu 24.04 LTS Server 
- IP: 192.168.1.221

Workstation: 
- Ubuntu 24.04 LTS Server 
- IP: 192.168.1.182

### 0.2. Resources
[www.postgresql.org](https://www.postgresql.org/docs)  
[www.postgresqltutorial.com](https://www.postgresqltutorial.com)  
**PostgreSQL 14 Administration Cookbook** by Simon Riggs & Gianni Ciolli  
**Learn PostgreSQL** by Luca Ferrari & Enrico Pirozzi 

<br>
</details>

<details markdown='1'>
<summary>
1. Introduction
</summary>

---
### 1.1. Terminology:
**Cluster**: A PostgreSQL Instance. Can contain many databases

**Database**: Accessed by allowed users. Can contain schemas (namespaces)

**Schema**: Used for organizing database objects. Can contain database  objects.

**Database Objects**: Tables, functions, triggers, data types etc.

### 1.2. Basic Information
2 types of users: Normal and Superuser

All the data and configuration information is kept in PGDATA directory.

PostgreSQL supports information schema, but has catalog which is more  detailed.

Postmaster: The first process, responsible for all the executions.

WAL (Write Ahead Logs): Database change log, mainly used for recovering.

### 1.3. Software Components:
- PostgreSQL server  : Database server.
- PostgreSQL client  : Client tools
- PostgreSQL contrib : Extensions.
- PostgreSQL docs    : Documentation.
- PostgreSQL PL/Perl, PL/Python, and PL/Tcl: Programming interface.

Ubuntu postgresql package installs postgresql-client by default

<br>
</details>

<details markdown='1'>
<summary>
2. Installation and Basic Management
</summary>

---
### 2.1. Installation
Update repositories

```
sudo apt update
```

Install necessary packages

Ubuntu 24.04 installs Postgresql version 16

```
sudo apt install --yes postgresql
```

Check status

```
systemctl status postgresql
```

### 2.2. Cluster Management
Ubuntu allows running more than 1 clusters (instances) on a server.

See the list of clusters on a server:

```
pg_lsclusters
```

Sample output:

```
Ver Cluster Port Status Owner    Data directory              Log file
16  main    5432 online postgres /var/lib/postgresql/16/main /var/log/...
```

Values of Ver anf Cluster is important for us. We'll use them for  pg_ctlcluster command. Ours are 16 and main.

pg_ctlcluster is a wrapper command for the original pg_ctl command of  postgres.

See the status of a cluster:

```
sudo pg_ctlcluster 16 main status
```

Start a cluster

```
sudo pg_ctlcluster 16 main start
```

Stop a cluster

```
sudo pg_ctlcluster 16 main stop
```

There are 3 modes of stop: smart (wait for connections to stop), fast  (stop all connections), immediate (immediately). immediate option may  cause database to crash. Default mode is fast.

```
sudo pg_ctlcluster 16 main stop -m smart
sudo pg_ctlcluster 16 main stop -m fast
sudo pg_ctlcluster 16 main stop -m immediate
```

Restart, reload a cluster

```
sudo pg_ctlcluster 16 main restart
sudo pg_ctlcluster 16 main reload
```

### 2.3. Adding and Deleting Clusters
There might be more than 1 clusters on a server. At the first sight it  may not make sense, but for example if you need of 2 different admins for  2 different databases this solution could be very useful.

Currently we only have main cluster. We will add a second one with the  name second. 

Create another Postgres 15 cluster with the name second

```
sudo pg_createcluster 16 second
```

Start it

```
sudo pg_ctlcluster 16 second start
```

Create another Postgres 16 cluster with the name third and start it

```
sudo pg_createcluster 16 third --start
```

Delete (drop) third cluster

```
sudo pg_dropcluster 16 third --stop
```

Rename second cluster to secondary

```
sudo pg_renamecluster 16 second secondary
```

List clusters:

```
pg_lsclusters
```

Sample output:

```
Ver Cluster   Port Status Owner    Data directory                   Log file
16  main      5432 online postgres /var/lib/postgresql/16/main      /var/log/...
16  secondary 5433 online postgres /var/lib/postgresql/16/secondary /var/log/...
```

Here we can understand that, our 16 main cluster listens on port 5432  (default postgres listening port), and 16 secondary cluster listens on  port 5433.

Directory of configuration files for both clusters:  
/var/lib/postgresql/16/main/ and /var/lib/postgresql/16/secondary.

### 2.4. Service vs Cluster Management
Postgres and its clusters can be managed by systemctl command too.

Stop postgres (all the clusters):

```
sudo systemctl stop postgresql
```

Stop 16-main postgres cluster

```
sudo systemctl stop postgresql@16-main
```

Other systemctl options (like restart, stop, enable, disable, reload) can be used too.

### 2.5. Login to Postgres shell
With the default installation; postgres linux user can login to psql  shell without the need of password authentication. 

```
sudo -u postgres psql
```

Type exit to quit from postgres shell

As you may guess, you logged in to 16 Main cluster. To login 16 secondary cluster:

```
sudo -u postgres psql -p 5433
```

<br>
</details>

<details markdown='1'>
<summary>
3. User and Connection Management
</summary>

---
After installing Postgres, postgres user is able to login psql shell with Linux authentication. No other users are defined and noone can login  remotely.

We will implement a scenario for user management.

### 3.0. Backup Configuration Files
```
cd /etc/postgresql/16/main/
sudo cp postgresql.conf postgresql.conf.backup
sudo cp pg_hba.conf pg_hba.conf.backup
```
 
### 3.1. Scenario
- Leave postgres user as it is (will be used as DB admin)
- Create a database named test1
- Create a user (role) rwuser with read and write permission at all the  test1 tables. Can access only from 1 IP (192.168.1.182). 
- Create a user (role) rouser with read only permissons at all the test1  tables.
- Can access from a network (192.168.1.1/24).

### 3.2. Create users
Give their passwords too

```
sudo -u postgres createuser --pwprompt rwuser
sudo -u postgres createuser --pwprompt rouser
```

### 3.3. Create test1 database and give R/W and R/O permissions. 
Create database

```
sudo -u postgres createdb test1
```

Create a sample table and fill it with sample data.

# Run psql to connect test1 database

```
sudo -u postgres psql test1
```

Run on psql shell

```
CREATE TABLE Employees (Name char(15), Age int, Occupation char(15));
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
GRANT ALL ON ALL TABLES IN SCHEMA public to rwuser;
GRANT SELECT ON ALL TABLES IN SCHEMA public to rouser;
\q
```

### 3.4. Configure Postgres to allow remote connections
Edit postgres.conf file to allow network connections

```
sudo nano /etc/postgresql/16/main/postgresql.conf
```
Uncomment and change the line below (around line 60)

```
#listen_addresses = 'localhost'         # what IP address(es) to listen on;
```

as below

```
listen_addresses = '*'                  # what IP address(es) to listen on;
```

Edit pg_hba.conf file to allow rwuser and rouser to allow connections  from specified ip/networks.

```
sudo nano /etc/postgresql/16/main/pg_hba.conf
```

Add following lines to the file

```
host    test1           rwuser          192.168.1.182/32        scram-sha-256
host    test1           rouser          192.168.1.0/24          scram-sha-256
```

Restart our cluster

```
sudo pg_ctlcluster restart 16 main
```

### 3.5. Connection test from Workstation (192.168.1.182)
**!! Run on workstation !!**

Install Postgres Client to the workstation

```
sudo apt update
sudo apt install postgresql-client --yes	
```
 
Connect with rwuser and test adding data (test must be successfull)

```
psql -h 192.168.1.221 -U rwuser test1
```

Run on psql shell

```
INSERT INTO Employees VALUES ('John Doe', '33', 'Kedi');
\q
```

Connect with rouser and test reading and adding data  
(reading test must be successfull, adding test must fail)

```
psql -h 192.168.1.221 -U rouser test1
```

Run on psql shell

```
SELECT * from Employees;
INSERT INTO Employees VALUES ('Halim Selim', '41', 'Hirsiz');
\q
```

If you try to use psql from another workstation in 192.168.1.0/24  network, you will see that rwuser cannot connect and rouser can connect.

<br>
</details>

<details markdown='1'>
<summary>
4. Backup and Restore 
</summary>

---
You can backup a database or a whole cluster. When backing up a database, users (roles) and any other clusterwide data is not backed up. So if you backup a database and restore it on another cluster, you have to create users and (if necessary) access permissions there too.

### 4.0. Considerations
We need to use postgres user for backup and restore, when we sudo for  this user; we need to change the directory to /tmp, because postgres user  does not have permissions on our home directory.

### 4.1. Backup a database
Backing up a database is performed with pg_dump command:  
`pg_dump dbname > dumpfile`

pg_dump command's connection parameters are like psql command's. 

Move to /tmp directory

```
cd /tmp
```

Backup test1 database on 16 main cluster to test1.pg file

```
sudo -u postgres pg_dump test1 > /tmp/test1.pg
```

Backup postgres database on 16 secondary cluster to sdb.pg  
We need to specify the port of 16 secondary cluster

```
sudo -u postgres pg_dump -p 5433 postgres > /tmp/sdb.pg
```

### 4.2. Restore a database
You can restore a database dump with psql command:

```
psql dbname < dumpfile
```

Restore test1 database back on 16 main cluster

```
sudo -u postgres psql test1 < /tmp/test1.pg
```

Let's restore test1 db to secondary cluster  
We need an empty test1 database. 

Create test1 database on 16 secondary

```
sudo -u postgres createdb -p 5433 test1
```

Create users rwuser and rouser on secondary cluster.   

createuser command's connection parameter are like psql command's too. So  we need to specify port number 5433 for secondary cluster.

```
sudo -u postgres createuser -p 5433 --pwprompt rwuser
sudo -u postgres createuser -p 5433 --pwprompt rouser
```
 
Import the database

```
sudo -u postgres psql -p 5433 test1 < /tmp/test1.pg
```

### 4.3. Backup and Restore Whole Cluster
When we backup a cluster, all clusterwide data including users and  access rights are backed up too. But remember, you have to change the  configuration files by yourself.

Cluster dump is made by `pg_dumpall` command. This command too has the  same connection parameters as psql command. 

Backup 16 main cluster to main.pg file

```
sudo -u postgres pg_dumpall > /tmp/main.pg
```

Restore main.pg file to 16 secondary cluster

```
sudo -u postgres psql -p 5433 -f /tmp/main.pg
```

<br>
</details>

<details markdown='1'>
<summary>
5. psql - PostgreSQL Shell
</summary>

---
### 5.1. The Command
psql command is used to open a Postgres shell. At the fresh install, only postgres Linux user has the right to connect to Postgres shell. So we need to run it by impersonating postgres user:

```
sudo -u postgres psql
```

If we want another Linux user to login to psql shell, we have to create  them using createuser command and add connection permission to them at pg_hba.conf configuration file. I don't prefer that method. In my very  humble opinion, 1 database admin is enough.

### 5.2. The command arguments
psql command has a lot of arguments. If no argument is given; it tries to connect with the current Linux user name as the user name and again  current Linux user name as the database name. My Linux user name is  exforge, so when I run psql command, I get the following error message.

```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432"
failed: FATAL:  role "exforge" does not exist
```

If I go beyond and create exforge user (role actually, user=role in  postgres) only I have a different error message:

```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "exforge" does not exist
```

If I go even beyond and create a database named exforge then everything  goes fine.

Well, of course instead of creating a database with my user name, I can  connect to psql with specifying an existing database.

```
psql postgres
```

As we have seen before we can specify port number with -p switch, host  name with -h switch. We can also specify postgres user with -U switch.

Full list of arguments can be seen with --help switch

```
psql --help
```

### 5.3. psql Commands
You can run SQL commands at psql shell. You can also run psql commands,  some of which are very useful.

- \x	Toggles expanded display
- \c	Connect to a database
- \d	List tables
- \du 	List roles (users)
- \?	psql command help-

<br>
</details>

<details markdown='1'>
<summary>
6. Bonus: Postgres 16 and Postgres 15 together
</summary>

---
For testing purposes we will install Postgresql 15 on the same server. 

That way we will have different postgres clusters with different versions.

Ubuntu 24.04 has Postgres 16 in its repositories. For Postgres 15 we need to add a PPA.

### 6.1. Add Postgresql PPA
Add keys

```
curl -fSsL https://www.postgresql.org/media/keys/ACCC4CF8.asc \
    | gpg --dearmor \
    | sudo tee /usr/share/keyrings/postgresql.gpg > /dev/null
```

Add PPA

```
echo deb [arch=amd64,arm64,ppc64el \
    signed-by=/usr/share/keyrings/postgresql.gpg] \
    http://apt.postgresql.org/pub/repos/apt/ noble-pgdg main \
    | sudo tee -a /etc/apt/sources.list.d/postgresql.list
```

### 6.2. Install Postgresql 15
```
sudo apt update
sudo apt install -y postgresql-15
```

### 6.3. List clusters:
```
pg_lsclusters
```

Output will be like below, now we have 3 clusters namely 16-main, 16-secondary, and 15-main running on the same computer:

```
Ver Cluster   Port Status Owner    Data directory                   Log file
15  main      5434 online postgres /var/lib/postgresql/15/main      /var/log/...
16  main      5432 online postgres /var/lib/postgresql/16/main      /var/log/...
16  secondary 5433 online postgres /var/lib/postgresql/16/secondary /var/log/...
```

### 6.4. Connecting to the clusters with psql
Connect to the first cluster (16-main), remember it runs on port 5432

```
sudo -u postgres psql -p 5432
```

Connect to the second cluster (16-secondary), remember it runs on port  5433

```
sudo -u postgres psql -p 5433
```

Connect to the third cluster (15-main), remember it runs on port 5434

```
sudo -u postgres psql -p 5434
```
</details>

