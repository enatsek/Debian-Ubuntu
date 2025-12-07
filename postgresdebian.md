##### Postgresql Debian
# Postgresql Tutorial for Debian

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. The What

PostgreSQL is a powerful, open-source relational database management system known for its reliability, feature robustness, and performance. It supports both SQL and non-SQL queries, making it versatile for various applications.

Debian 13 and Ubuntu 24.04 LTS Server include packages for different PostgreSQL versions (17 and 16). For ease of following tutorials, I've prepared separate guides for Debian and Ubuntu.

### 0.2. The Environment

**Server:**
- Debian 13
- IP: 192.168.1.201

**Workstation:**
- Debian 13
- IP: 192.168.1.181

### 0.3. Resources
- [www.postgresql.org](https://www.postgresql.org/docs)
- [www.postgresqltutorial.com](https://www.postgresqltutorial.com)
- **PostgreSQL 14 Administration Cookbook** by Simon Riggs & Gianni Ciolli
- **Learn PostgreSQL** by Luca Ferrari & Enrico Pirozzi 

<br>
</details>

<details markdown='1'>
<summary>
1. Introduction
</summary>

---
### 1.1. Terminology:
- **Cluster**: A PostgreSQL Instance. Can contain multiple databases.
- **Database**: Accessed by authorized users. Can contain schemas (namespaces).
- **Schema**: Used for organizing database objects. Can contain database objects.
- **Database Objects**: Tables, functions, triggers, data types etc.

### 1.2. Basic Information

All data and configuration information is stored in the PGDATA directory.

PostgreSQL supports the information schema but also maintains a catalog that provides more detailed information.

**Postmaster**: The first PostgreSQL process, responsible for coordinating all other processes.

**WAL (Write Ahead Logs)**: Database change logs used primarily for recovery.

### 1.3. Software Components

- **PostgreSQL server**: The database server.
- **PostgreSQL client**: Client tools for interacting with the server.
- **PostgreSQL contrib**: Extensions and additional utilities.
- **PostgreSQL docs**: Documentation.
- **PostgreSQL PL/Perl, PL/Python, and PL/Tcl**: Programming language interfaces.

The Debian `postgresql` package installs `postgresql-client` by default.

<br>
</details>

<details markdown='1'>
<summary>
2. Installation and Basic Management
</summary>

---
### 2.1. Installation

Update package repositories:

```
sudo apt update
```

Install PostgreSQL (Debian 13 installs version 17 by default):

```
sudo apt install --yes postgresql
```

Check the service status:

```
systemctl status postgresql
```

### 2.2. Cluster Management

Debian allows running multiple clusters (instances) on a single server.

List clusters on the server:

```
pg_lsclusters
```

Sample output:

```
Ver Cluster Port Status Owner    Data directory              Log file
17  main    5432 online postgres /var/lib/postgresql/17/main /var/log/...
```

The "Ver" (Version) and "Cluster" values are important for the `pg_ctlcluster` command. In this case, they are `17` and `main`.

`pg_ctlcluster` is a wrapper command for PostgreSQL's native `pg_ctl` command.

Check the status of a specific cluster:

```
sudo pg_ctlcluster 17 main status
```

Start a cluster:

```
sudo pg_ctlcluster 17 main start
```

Stop a cluster:

```
sudo pg_ctlcluster 17 main stop
```

There are three stop modes:
- `smart`: Wait for connections to finish (graceful shutdown)
- `fast`: Stop all connections immediately (default)
- `immediate`: Force immediate shutdown (may cause database corruption)


```
sudo pg_ctlcluster 17 main stop -m smart
sudo pg_ctlcluster 17 main stop -m fast
sudo pg_ctlcluster 17 main stop -m immediate
```

Restart or reload a cluster:

```
sudo pg_ctlcluster 17 main restart
sudo pg_ctlcluster 17 main reload
```

### 2.3. Adding and Deleting Clusters

You can run multiple clusters on a single server. While this might seem unnecessary at first, it can be useful when different databases require separate administrators.

Currently, we only have the `main` cluster. Let's add a second one named `second`.

Create another PostgreSQL 17 cluster named `second`:

```
sudo pg_createcluster 17 second
```

Start it:

```
sudo pg_ctlcluster 17 second start
```

Create a third cluster and start it immediately:

```
sudo pg_createcluster 17 third --start
```

Delete (drop) the third cluster:

```
sudo pg_dropcluster 17 third --stop
```

Rename the `second` cluster to `secondary`:

```
sudo pg_renamecluster 17 second secondary
```

List clusters again:

```
pg_lsclusters
```

Sample output:

```
Ver Cluster   Port Status Owner    Data directory                   Log file
17  main      5432 online postgres /var/lib/postgresql/17/main      /var/log/...
17  secondary 5433 online postgres /var/lib/postgresql/17/secondary /var/log/...
```

From this output, we can see:

- The `17-main` cluster listens on port 5432 (PostgreSQL's default port)
- The `17-secondary` cluster listens on port 5433
- Data directories are `/var/lib/postgresql/17/main/` and `/var/lib/postgresql/17/secondary/`

### 2.4. Service vs Cluster Management

PostgreSQL and its clusters can also be managed using `systemctl`.

Stop all PostgreSQL clusters:

```
sudo systemctl stop postgresql
```

Stop only the `17-main` cluster:

```
sudo systemctl stop postgresql@17-main
```

Other `systemctl` commands (`restart`, `enable`, `disable`, `reload`) work similarly.

### 2.5. Login to Postgres shell

After default installation, the `postgres` Linux user can log into the `psql` shell without password authentication:
```
sudo -u postgres psql
```

Type `exit` to quit the PostgreSQL shell.

By default, you connect to the `17-main` cluster. To connect to the `17-secondary` cluster:

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

After installing PostgreSQL, only the `postgres` user can log into the `psql` shell via Linux authentication. No other users are defined, and remote connections are not allowed.

We'll implement a user management scenario.

### 3.0. Backup Configuration Files

```
cd /etc/postgresql/17/main/
sudo cp postgresql.conf postgresql.conf.backup
sudo cp pg_hba.conf pg_hba.conf.backup
```
 
### 3.1. Scenario

- Leave the `postgres` user as is (will serve as the database administrator)
- Create a database named `test1`
- Create a user (role) `rwuser` with read/write permissions on all `test1` tables, accessible only from IP `IP: 192.168.1.181`
- Create a user (role) `rouser` with read-only permissions on all `test1` tables, accessible from the network `192.168.1.0/24`

### 3.2. Create Users

Create users with passwords:

```
sudo -u postgres createuser --pwprompt rwuser
sudo -u postgres createuser --pwprompt rouser
```

### 3.3. Create the `test1` Database and Set Permissions

Create the database:

```
sudo -u postgres createdb test1
```

Create a sample table and populate it with data.

Connect to the `test1` database:

```
sudo -u postgres psql test1
```

Run these commands in the `psql` shell:

```
CREATE TABLE Employees (Name char(15), Age int, Occupation char(15));
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
GRANT ALL ON ALL TABLES IN SCHEMA public to rwuser;
GRANT SELECT ON ALL TABLES IN SCHEMA public to rouser;
\q
```

### 3.4. Configure PostgreSQL to Allow Remote Connections

Edit `postgresql.conf` to allow network connections:

```
sudo nano /etc/postgresql/17/main/postgresql.conf
```

Uncomment and modify this line (around line 60):

```
#listen_addresses = 'localhost'         # what IP address(es) to listen on;
```

Change it to:

```
listen_addresses = '*'                  # what IP address(es) to listen on;
```

Edit `pg_hba.conf` to allow `rwuser` and `rouser` to connect from specified IPs/networks:

```
sudo nano /etc/postgresql/17/main/pg_hba.conf
```

Add these lines to the file:

```
host    test1           rwuser          192.168.1.181/32        scram-sha-256
host    test1           rouser          192.168.1.0/24              scram-sha-256
```

Restart the cluster:

```
sudo pg_ctlcluster restart 17 main
```

### 3.5. Connection Test from Workstation (IP: 192.168.1.181)

**Note: Run these commands on the workstation!**

Install the PostgreSQL client on the workstation:

```
sudo apt update
sudo apt install postgresql-client --yes	
```
 
Connect as `rwuser` and test data insertion (should succeed):

```
psql -h 192.168.1.201 -U rwuser test1
```

In the `psql` shell:

```
INSERT INTO Employees VALUES ('John Doe', '33', 'Kedi');
\q
```

Connect as `rouser` and test reading/inserting (reading should succeed, inserting should fail):

```
psql -h 192.168.1.201 -U rouser test1
```

In the `psql` shell:

```
SELECT * from Employees;
INSERT INTO Employees VALUES ('Halim Selim', '41', 'Hirsiz');
\q
```

If you try to connect from another workstation in the `192.168.1.0/24` network, you'll see that `rwuser` cannot connect while `rouser` can.

<br>
</details>

<details markdown='1'>
<summary>
4. Backup and Restore 
</summary>

---

You can back up individual databases or entire clusters. When backing up a single database, cluster-wide data like users and roles are not included. Therefore, when restoring a database to another cluster, you must recreate users and permissions.

### 4.0. Considerations

We need to use the `postgres` user for backup and restore operations. When using `sudo` for this user, we should change to the `/tmp` directory because the `postgres` user doesn't have permission to write to our home directory.

### 4.1. Backup a database

Back up a database using `pg_dump`:

```
pg_dump dbname > dumpfile
```

`pg_dump` uses the same connection parameters as `psql`.

Change to the `/tmp` directory:

```
cd /tmp
```

Back up the `test1` database from the `17-main` cluster:

```
sudo -u postgres pg_dump test1 > /tmp/test1.pg
```

Back up the `postgres` database from the `17-secondary` cluster (specify port):

```
sudo -u postgres pg_dump -p 5433 postgres > /tmp/sdb.pg
```

### 4.2. Restore a database

Restore a database dump using `psql`:

```
psql dbname < dumpfile
```

Restore the `test1` database to the `17-main` cluster:

```
sudo -u postgres psql test1 < /tmp/test1.pg
```

Restore the `test1` database to the secondary cluster. First, create an empty `test1` database:


```
sudo -u postgres createdb -p 5433 test1
```

Create `rwuser` and `rouser` on the secondary cluster (specify port 5433):

```
sudo -u postgres createuser -p 5433 --pwprompt rwuser
sudo -u postgres createuser -p 5433 --pwprompt rouser
```
 
Import the database:

```
sudo -u postgres psql -p 5433 test1 < /tmp/test1.pg
```

### 4.3. Backup and Restore Whole Cluster

When backing up a cluster, all cluster-wide data including users and access rights are included. However, configuration files must be handled separately.

Back up a cluster using `pg_dumpall` (uses the same connection parameters as `psql`):

Back up the `17-main` cluster:

```
sudo -u postgres pg_dumpall > /tmp/main.pg
```

Restore to the `17-secondary` cluster:

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

The `psql` command opens a PostgreSQL shell. After a fresh installation, only the `postgres` Linux user can connect without authentication:

```
sudo -u postgres psql
```

To allow other Linux users to log into `psql`, you would need to create them using `createuser` and add connection permissions in `pg_hba.conf`. In most of the cases, having one database administrator is sufficient.

### 5.2. The command arguments

`psql` has many arguments. If no arguments are provided, it attempts to connect using the current Linux username as both the username and database name. For example, if my username is `exforge`:

```
psql
```

I would receive an error:

```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432"
failed: FATAL:  role "exforge" does not exist
```

Even if I create a role named `exforge`, I would get:

```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "exforge" does not exist
```

Instead, connect to an existing database:

```
psql postgres
```

You can specify:
- Port number with `-p`
- Host with `-h`
- Username with `-U`

View all arguments:

```
psql --help
```

### 5.3. psql Commands

You can run SQL commands in the `psql` shell, as well as `psql` meta-commands (prefixed with `\`):

- `\x` - Toggle expanded display
- `\c` - Connect to a database
- `\d` - List tables
- `\du` - List roles (users)
- `\?` - Show psql command help

<br>
</details>

<details markdown='1'>
<summary>
6. Bonus: Postgres 17 and Postgres 18 together
</summary>

---

For testing purposes, we can install PostgreSQL 18 on the same server, allowing us to run clusters with different versions simultaneously.

Debian 13 includes PostgreSQL 17 in its repositories. For PostgreSQL 18, we need to add PostgreSQL repositories.

### 6.1. Add Postgresql Repository

Install necessary software:


```
sudo apt update
sudo apt install gpg curl --yes
```

Add the repository key:

```
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc \
    | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
```

Add the Repository:

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt \
       $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

### 6.2. Install PostgreSQL 18
```
sudo apt update
sudo apt install -y postgresql-18
```

Create a PostgreSQL 18 clusterÇ

```
sudo pg_createcluster 18 main --start
```

### 6.3. List Clusters

```
pg_lsclusters
```

Sample output (now with three clusters):

```
Ver Cluster   Port Status Owner    Data directory                   Log file
17  main      5432 online postgres /var/lib/postgresql/17/main      /var/log/...
17  secondary 5433 online postgres /var/lib/postgresql/17/secondary /var/log/...
18  main      5434 online postgres /var/lib/postgresql/17/main      /var/log/...
```

### 6.4. Connecting to the clusters with psql

Connect to the first cluster (17-main, port 5432):

```
sudo -u postgres psql -p 5432
```

Connect to the second cluster (17-secondary, port 5433):

```
sudo -u postgres psql -p 5433
```

Connect to the third cluster (18-main, port 5434):

```
sudo -u postgres psql -p 5434
```
</details>

