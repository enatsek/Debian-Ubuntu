##### MariadbClusterOnDebianUbuntu 
# Mariadb Main-Main Replication with Galera Cluster Tutorial on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. Definitions
3 servers will be installed and configured as Mariadb clusters. 

All the changes in one server will be updated to others momentarily. At least 3 nodes are advised for Mariadb cluster, there is no upper limit.

**At least 2 of the cluster nodes must be online always**. If you fall  to 1 you may have problems. If you shut down all of the nodes, your cluster stops and you need some work to (hopefully) start again. !!!

### 0.2. My Configuration
srv1 -> 192.168.1.221 Debian 12/11 Ubuntu 24.04/22.04 LTS Server  
srv2 -> 192.168.1.222 Debian 12/11 Ubuntu 24.04/22.04 LTS Server  
srv3 -> 192.168.1.223 Debian 12/11 Ubuntu 24.04/22.04 LTS Server  

All the nodes must have the same version of Mariadb. That is, they must  have the same Linux distros.

### 0.3. Resources
[www.howtoforge.com](https://www.howtoforge.com/how-to-setup-mariadb-galera-multi-master-synchronous-replication-using-debian-10/)  
[www.symmcom.com](https://www.symmcom.com/docs/how-tos/databases/how-to-recover-mariadb-galera-cluster-after-partial-or-full-crash)  
[mariadb.com/docs](https://mariadb.com/docs/multi-node/galera-cluster/understand-mariadb-galera-cluster/)  
[mariadb.com/kb](https://mariadb.com/kb/en/galera-cluster-recovery/)

<br>
</details>

<details markdown='1'>
<summary>
1. Mariadb Installations (Run on all servers)
</summary>

---
### 1.1. Install Mariadb and Galera Cluster on all servers
```
sudo apt update
sudo apt install mariadb-server galera-4 --yes
```

### 1.2. Secure Mariadb Installations
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

<br>
</details>

<details markdown='1'>
<summary>
2. Mariadb Configurations (Run on all servers)
</summary>

---
### 2.1. Temporarily Stop Mariadb
```
sudo systemctl stop mariadb
```

### 2.2. Bind Address Enablement
Mariadb daemon must listen to the network for the cluster

```
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

Change the following line (Around line 27-30)

from:

```
bind-address = 127.0.0.1
```

to:

```
bind-address = 0.0.0.0
```

### 2.3. Cluster Options
Create a new conf file and fill it

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

Fill as below, remember to use your ip addresses

```
[galera]
# Mariadb only supports this lock mode
innodb_autoinc_lock_mode = 2
# Name of the cluster, you can change it
wsrep_cluster_name    = "x386_cluster"
# List of cluster nodes
wsrep_cluster_address = "gcomm://192.168.1.221,192.168.1.222,192.168.1.223"
# Galera plugin path
wsrep_provider = /usr/lib/galera/libgalera_smm.so
# If a node does not respond in 10 second, it is assumed to be offline
wsrep_provider_options = "evs.suspect_timeout=PT10S"
# Replication for this node is on
wsrep_on = on 
# Galera cluster supports InnoDB
default_storage_engine = InnoDB 
# Use InnoDB double write buffer
innodb_doublewrite = 1 
# Use ROW format for bin logs
binlog_format = ROW
```

<br>
</details>

<details markdown='1'>
<summary>
3. Start Cluster
</summary>

---
### 3.1. Start Cluster on One of the Nodes
**!!! You should run this only on one of the servers !!!**

```
sudo galera_new_cluster
```

This command should also start mariadb on this node, check it:

```
systemctl status mariadb
```

### 3.2. Start Mariadb on Other Nodes too
Run on the other servers:

```
sudo systemctl start mariadb
```

Our Cluster is established

<br>
</details>

<details markdown='1'>
<summary>
4. Test Mariadb Cluster 
</summary>

---
We will run commands on the nodes and see the changes on other nodes

### 4.1. Create a Database on the First Node
**!!! Run on the first server !!!**

```
sudo mariadb
```

Run on mariadb shell

```
CREATE DATABASE Test;
exit;
```

### 4.2. Create a Table on the Database on the Second Node
**!!! Run on second server !!!**

```
sudo mariadb
```

Run on mariadb shell

```
USE Test;
CREATE TABLE People (Name char(15), Age int(3));
exit;
```

### 4.3. Add Records to the Table on the Third Node
**!!! Run on third server !!!**

```
sudo mariadb
```

Run on mariadb shell

```
USE Test;
INSERT INTO People VALUES ('Exforge', '52');
INSERT INTO People VALUES ('Kedi', '8');
SELECT * FROM People;
exit;
```

### 4.4. Check First and Second Node for the Records
**!!! Run on first and second server !!!**

```
sudo mariadb
```

Run on mariadb shell

```
USE Test;
SELECT * FROM People;
exit;
```

<br>
</details>

<details markdown='1'>
<summary>
5. Maintenance
</summary>

---
### 5.1. Healthcheck
The following commands runs on Mariadb shell and show information about  Mariadb cluster.

Show the running nodes:

```
show status like 'wsrep_incoming_addresses' ;
```

Show the number of running nodes:

```
show status like 'wsrep_cluster_size';
```

Show the UUID of the cluster

```
show status like 'wsrep_cluster_state_uuid';
```

Show the status of the current node

```
show status like 'wsrep_local_state_comment';
```

### 5.2. Adding a Node to Mariadb Cluster
Install Mariadb and Galera Cluster to the new node, that is follow the  steps at 1. and 2. At step 2.3. at the line starting with  wsrep_cluster_address, add the IP of the new server too. Then start  mariadb:

```
sudo systemctl start mariadb
```

The new node is going to start replicating data, it may take some time  depending on the volume of the DBs. You can run following command and see the status of the replication:

```
show status like 'wsrep_local_state_comment';
```

When you see the value as "Synced", you can understand that the new node  is replicated.

You added the ip of the new node to the configuration of the new node  only.

Before it is too late, You need to add it to the other cluster member  configurations too. Otherwise, it would be very difficult to resolve if  any cluster error occurs in the future.

Run on other cluster members one by one:

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

At the line starting with wsrep_cluster_address, add the IP of the new  server.

Restart Mariadb after changing the configuration

```
sudo systemctl restart mariadb
```
 
### 5.3. Removing a Node from Mariadb Cluster
If you want to remove a node temporarily, it wouldn't be a problem. If  you don't change any configurations on the cluster servers, it would join  back to the cluster.

If you want to remove a node permanently, a good way would be uninstall  mariadb or permanently poweroff the computer. And then, remove its ip from other servers' `/etc/mysql/mariadb.conf.d/99-cluster.cnf` file and restart mariadb at the other servers one by one.

### 5.4. Shutting Down the Cluster
It is not advised to keep less than 2 nodes online. But if you really  need to shutdown all the cluster (e.g. to physically move to somewhere  else), or a total power failure occurs; you may try to shutdown servers one at a time and when they are ready to start, first you have to turn on the last shutdown node.

If the cluster doesn't go online, refer to 6.

<br>
</details>

<details markdown='1'>
<summary>
6. Recovery
</summary>

---
Mariadb Galera Cluster would run fine for a long time, as long as you  keep at least 2 nodes alive and running. If you have 3 nodes, you can  proceed on maintenance tasks (backup, upgrade etc) one at a time. 

But problems are for humans (and computers). There might come one day and cluster doesn't start. And when cluster doesn't start, Mariadb doesn't  start either.

In that case, we need to restart the cluster, but we need to find the  safe node to start the cluster.

### 6.1. Finding the Safe Node - 1st Try
run the following command on every node:

```
sudo cat /var/lib/mysql/grastate.dat
```

It's output will be something like below:

```
# GALERA saved state
version: 2.1
uuid:    2d878884-9ae6-11eb-955f-fa6fa258f122
seqno:   -1
safe_to_bootstrap: 0
```

or

```
# GALERA saved state
version: 2.1
uuid: 886dd8da-3d07-11e8-a109-8a3c80cebab4
seqno: 31929
safe_to_bootstrap: 1
```

If output in any node contains "safe_to_bootstrap: 1" or a positive value of "seqno: ", that means we can restart the cluster at that node. We  have found the safe node, proceed to 6.3.

Otherwise, we keep trying to find the safe node.

### 6.2. Finding the Safe Node - 2nd Try
**!!! Run on all nodes !!!**

sudo galera_recovery

Output will be something like as below:

```
WSREP: Recovered position 2d878884-9ae6-11eb-955f-fa6fa258f122:8
--wsrep_start_position=2d878884-9ae6-11eb-955f-fa6fa258f122:8
```

The node with the highest value after ":" will be our candidate to  restart the cluster. We have found the safe node. If more than 1 node has  the same highest value, just choose one.

We need to set safe node to restart the cluster:

**!!! Run on the Safe Node !!!**

```
sudo nano /var/lib/mysql/grastate.dat
```

Change the line starting with "safe_to_bootstrap" as below:

```
safe_to_bootstrap: 1
```

### 6.3. Restart the Galera Cluster
Run the following command at the safe node:

```
sudo galera_new_cluster
```

After a while (1-2minutes) Run following command at the other nodes:

```
sudo systemctl restart mariadb
```

The cluster is working again, we are done.

It would be wise to make a healthcheck as in 5.1. and see cluster is working.

If this step doesn't work either. We have just one more thing to do. Go  to the next step.

### 6.4. Last Chance
**!! On the safe node !!**

Disable mariadb and reboot

```
sudo systemctl disable mariadb
sudo reboot
```

Edit cluster config at the safe node:

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

Change the wsrep_cluster_address parameter to contain only the safe node. That is, if the 3rd node is the safe node as belowÇ

```
wsrep_cluster_address = "gcomm://192.168.1.223"
```

Enable mariadb 

```
sudo systemctl enable mariadb
```

Start Galera Cluster

```
sudo galera_new_cluster
```

**!! On the other nodes !!**

Restart mariadb 

```
sudo systemctl restart mariadb
```

If they cannot restart, it is because it cannot be stopped. Do the  disable, reboot, enable trick on them too

```
sudo systemctl disable mariadb
sudo reboot
```

After reboot enable and start mariadb

```
sudo systemctl enable mariadb
sudo systemctl start mariadb
```

If they start, most probably your cluster is working again Otherwise, you need a professional support.

**!! On the safe node !!**

Revert the first node to the original configuration

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

Change the wsrep_cluster_address parameter to original

```
wsrep_cluster_address = "gcomm://192.168.1.221,192.168.1.222,192.168.1.223"
```

Restart mariadb

```
sudo systemctl restart mariadb
```

</details>

