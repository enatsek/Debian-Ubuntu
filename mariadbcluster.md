##### Mariadb Galera Cluster 
# MariaDB Multi-Primary Replication with Galera Cluster Tutorial on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.1. The What

MariaDB Galera Cluster is a Linux-exclusive, multi-primary cluster solution for MariaDB. It offers:
- Active-active topology with read/write capabilities on any node
- Automatic membership management and node joining
- True parallel replication at the row level
- Direct client connections to any node
- Native MariaDB integration and experience

### 0.2. Important Notes

- Three servers will be configured as a MariaDB Galera Cluster.
- Changes on any node are replicated to all other nodes almost instantly.
- **A minimum of 3 nodes is recommended** for proper quorum and fault tolerance.
- **At least 2 cluster nodes must remain online at all times.** Operating with only one node can cause issues.
- **Warning:** If all nodes shut down, the cluster will stop and require recovery procedures to restart.


### 0.3. Environment
- **srv1**: 192.168.1.201 (Debian 13/12 or Ubuntu 24.04/22.04 LTS Server)
- **srv2**: 192.168.1.202 (Debian 13/12 or Ubuntu 24.04/22.04 LTS Server)
- **srv3**: 192.168.1.203 (Debian 13/12 or Ubuntu 24.04/22.04 LTS Server)

**Important:** All nodes must run the same version of MariaDB. Using identical Linux distributions is recommended to ensure compatibility.

### 0.4. Resources
- [HowtoForge Tutorial](https://www.howtoforge.com/how-to-setup-mariadb-galera-multi-master-synchronous-replication-using-debian-10/)
- [Symmcom Documentation](https://www.symmcom.com/docs/how-tos/databases/how-to-recover-mariadb-galera-cluster-after-partial-or-full-crash)
- [MariaDB Galera Cluster Documentation](https://mariadb.com/docs/multi-node/galera-cluster/understand-mariadb-galera-cluster/)
- [MariaDB Knowledge Base - Galera Recovery](https://mariadb.com/kb/en/galera-cluster-recovery/)

<br>
</details>

<details markdown='1'>
<summary>
1. Mariadb Installation
</summary>

---

**Run on all servers**

Install MariaDB and Galera Cluster:

```
sudo apt update
sudo apt install mariadb-server galera-4 --yes
```

Run the security hardening script:

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

<br>
</details>

<details markdown='1'>
<summary>
2. Mariadb Configuration
</summary>

---

**Run on all servers**

Temporarily stop MariaDB:

```
sudo systemctl stop mariadb
```

Configure MariaDB to listen on the network for cluster communication:

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

Create and configure the cluster configuration file:

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

Add the following content (replace IP addresses with your servers'):

```
[galera]
# MariaDB Galera requires this lock mode
innodb_autoinc_lock_mode = 2

# Cluster name (can be customized)
wsrep_cluster_name    = "x386_cluster"

# List of all cluster nodes
wsrep_cluster_address = "gcomm://192.168.1.201,192.168.1.202,192.168.1.203"

# Galera plugin path
wsrep_provider = /usr/lib/galera/libgalera_smm.so

# Node considered offline if unresponsive for 10 seconds
wsrep_provider_options = "evs.suspect_timeout=PT10S"

# Enable replication
wsrep_on = on 

# Galera cluster supports InnoDB
default_storage_engine = InnoDB 

# Use InnoDB double write buffer
innodb_doublewrite = 1 

# Use ROW format for binary logs (required for Galera)
binlog_format = ROW
```

<br>
</details>

<details markdown='1'>
<summary>
3. Starting The Cluster
</summary>

---

**Step 1: Start the Cluster on One Node**  
**Run this command on ONLY ONE server (e.g., srv1):**

```
sudo galera_new_cluster
```

Verify MariaDB started successfully:

```
systemctl status mariadb
```

**Step 2: Start MariaDB on Other Nodes**  
**Run on the remaining servers (srv2 and srv3):**

```
sudo systemctl start mariadb
```

The Galera Cluster is now established and operational.

<br>
</details>

<details markdown='1'>
<summary>
4. Testing the MariaDB Cluster
</summary>

---
We will execute commands on different nodes to verify replication is working correctly.

### 4.1. Create a Database on the First Node
**Run on srv1:**

```
sudo mariadb
```

Execute in MariaDB shell:

```
CREATE DATABASE Test;
exit;
```

### 4.2. Create a Table on the Second Node
**Run on srv2:**

```
sudo mariadb
```

Execute in MariaDB shell:

```
USE Test;
CREATE TABLE People (Name char(15), Age int(3));
exit;
```

### 4.3. Add Records on the Third Node
**Run on srv3:**

```
sudo mariadb
```

Execute in MariaDB shell:

```
USE Test;
INSERT INTO People VALUES ('Exforge', '52');
INSERT INTO People VALUES ('Kedi', '8');
SELECT * FROM People;
exit;
```

### 4.4. Verify Replication on All Nodes
**Run on srv1 and srv2:**

```
sudo mariadb
```

Execute in MariaDB shell:

```
USE Test;
SELECT * FROM People;
exit;
```

You should see the same records on all nodes, confirming that replication is working.
<br>
</details>

<details markdown='1'>
<summary>
5. Maintenance
</summary>

---
### 5.1. Cluster Health Check
The following commands run in the MariaDB shell and display cluster status information.

Show connected nodes:

```
show status like 'wsrep_incoming_addresses' ;
```

Show number of active nodes:

```
show status like 'wsrep_cluster_size';
```

Show cluster UUID:

```
show status like 'wsrep_cluster_state_uuid';
```

Show current node status:

```
show status like 'wsrep_local_state_comment';
```

### 5.2. Adding a Node to the Cluster
1. Install MariaDB and Galera Cluster on the new node (follow Sections 1 and 2)
2. In the new node's `99-cluster.cnf` file, add its IP address to the `wsrep_cluster_address` parameter
3. Start MariaDB on the new node:

```
sudo systemctl start mariadb
```

The new node will begin synchronizing data. Monitor synchronization status:

```
show status like 'wsrep_local_state_comment';
```

When the value shows "Synced", the node is fully synchronized.

You added the ip of the new node to the configuration of the new node  only.

**Important:** Update all existing cluster members to include the new node's IP in their `wsrep_cluster_address` configuration, then restart MariaDB on each:

```
sudo systemctl restart mariadb
```
 
### 5.3. Removing a Node from the Cluster
- **Temporary removal:** Simply stop the node. It can rejoin later without configuration changes.
- **Permanent removal:** 
  1. Uninstall MariaDB or permanently power off the node
  2. Remove its IP from the `wsrep_cluster_address` parameter in all remaining nodes' `99-cluster.cnf` files
  3. Restart MariaDB on all remaining nodes

### 5.4. Shutting Down the Cluster
**Warning:** Avoid shutting down all nodes simultaneously. If necessary:

1. Shut down nodes one at a time
2. When restarting, start the node that was shut down last
3. If the cluster fails to start, proceed to Section 6 (Cluster Recovery)

<br>
</details>

<details markdown='1'>
<summary>
6. Cluster Recovery
</summary>

---
MariaDB Galera Cluster typically runs reliably as long as at least 2 nodes remain online. However, if all nodes go offline, recovery procedures are required.

### 6.1. Finding the Safe Node - First Attempt
Run on each node:

```
sudo cat /var/lib/mysql/grastate.dat
```

Sample output:
```
# GALERA saved state
version: 2.1
uuid:    2d878884-9ae6-11eb-955f-fa6fa258f122
seqno:   -1
safe_to_bootstrap: 0
```

Or:
```
# GALERA saved state
version: 2.1
uuid: 886dd8da-3d07-11e8-a109-8a3c80cebab4
seqno: 31929
safe_to_bootstrap: 1
```

**If any node shows `safe_to_bootstrap: 1` or has a positive `seqno` value**, this is your safe node. Proceed to Section 6.3.

### 6.2. Finding the Safe Node - Second Attempt
**Run on all nodes:**

```
sudo galera_recovery
```

Sample output:
```
WSREP: Recovered position 2d878884-9ae6-11eb-955f-fa6fa258f122:8
--wsrep_start_position=2d878884-9ae6-11eb-955f-fa6fa258f122:8
```

The node with the highest number after the colon (":") is the recovery candidate. If multiple nodes have the same highest value, choose any one.

**On the safe node only**, edit the state file:

```
sudo nano /var/lib/mysql/grastate.dat
```

Change the line to:

```
safe_to_bootstrap: 1
```

### 6.3. Restarting the Galera Cluster
**On the safe node:**
```
sudo galera_new_cluster
```

**On other nodes** (wait 1-2 minutes after starting the safe node):

```
sudo systemctl restart mariadb
```

Verify cluster health using the commands in Section 5.1.

### 6.4. Last Chance

If the above methods fail:

**On the safe node:**

Disable mariadb and reboot.

```
sudo systemctl disable mariadb
sudo reboot
```

Edit the cluster configuration to include only the safe node:

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

```
wsrep_cluster_address = "gcomm://192.168.1.203"  # IP of safe node only
```

Re-enable and start the cluster:

```
sudo systemctl enable mariadb
sudo galera_new_cluster
```

**On other nodes:**

If MariaDB won't restart normally:

```
sudo systemctl disable mariadb
sudo reboot
```

After reboot:

```
sudo systemctl enable mariadb
sudo systemctl start mariadb
```

**Finally, on the safe node**, restore the original cluster configuration:

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

```
wsrep_cluster_address = "gcomm://192.168.1.201,192.168.1.202,192.168.1.203"
```

Restart MariaDB:
```
sudo systemctl restart mariadb
```

If these steps don't resolve the issue, professional support may be required.
</details>

