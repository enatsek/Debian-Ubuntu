0,1,2
3,4,5
6,7
8


##### HAProxy
# High Availability with HAProxy Load Balancer on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. The What

HAProxy is a free, open-source software that acts as a high-availability load balancer and proxy for TCP and HTTP-based applications. It efficiently distributes requests across multiple servers and is widely used by high-traffic websites. HAProxy offers features like SSL termination, caching, and health checking.

This tutorial demonstrates how to set up High Availability Load Balancing with free Let's Encrypt certificates for HTTPS support.

### 0.2. Environment

- srv    : Load Balancer floating (virtual) IP --> 192.168.1.200
- srvlb1 : Load Balancer 1  --> 192.168.1.201
- srvlb2 : Load Balancer 2  --> 192.168.1.202
- srvaw1 : App/Web Server 1 --> 192.168.1.203
- srvaw2 : App/Web Server 2 --> 192.168.1.204
- srvaw3 : App/Web Server 3 --> 192.168.1.205

Tested on Debian 13/12 and Ubuntu 24.04/22.04 LTS Servers.

### 0.3. Notes

We will use a Keepalived cluster of two load balancers. Under normal conditions, the first server will handle the traffic. However, if the first load balancer fails or is powered off, the second will take over. This step is not strictly necessary but eliminates the risk of a Single Point of Failure.

This setup ensures our infrastructure remains operational even if one of the servers goes offline.

The two Load Balancers will be configured with the floating IP `192.168.1.200`.  
Our Application or Web Servers must be configured identically so that users will never know which server they are connected to.

For this example, we will install Apache and MariaDB on each App/Web server.

We will also install a Galera cluster to establish MariaDB clustering. This ensures that any database change on one server is replicated to the others.

First, we will load balance the web server, then we will load balance the MariaDB database usage. This will demonstrate that you can load balance virtually any kind of software.

Users will only see the floating IP (`192.168.1.200`) of the Load Balancers and will not be aware of the other servers or their IPs.

### 0.4. Sources:
- [www.haproxy.org](https://www.haproxy.org/)  
- [www.server-world.info](https://www.server-world.info/en/note?os=Ubuntu_20.04&p=haproxy&f=1)  
- [HAProxy Documentation](https://docs.haproxy.org/)  
- Book: ISBN: 9781519073846 **Load Balancing with HAProxy** by Nick Ramirez

<br>
</details>

<details markdown='1'>
<summary>
1. Install and Configure Load Balancers
</summary>

---

**Install Keepalived (on srvlb1 and srvlb2)**

```
sudo apt update
sudo apt install keepalived --yes
```

**Configure Keepalived on the First Load Balancer (srvlb1)**

Create a configuration file:

```
sudo nano /etc/keepalived/keepalived.conf
```

Fill it with the following content. Remember to replace `enp0s3` with your actual network adapter name.

```
global_defs {
	router_id node1
}
vrrp_instance VI_1 {
    state MASTER
	interface enp0s3
	virtual_router_id 51
	priority 100
	advert_int 5
	virtual_ipaddress {
	192.168.1.200
	}
}
```

**Configure Keepalived on the Second Load Balancer (srvlb2)**

Create a configuration file:

```
sudo nano /etc/keepalived/keepalived.conf
```

Fill it with the following content. Again, remember to replace `enp0s3` with your network adapter name.

```
global_defs {
	router_id node2
}
vrrp_instance VI_1 {
    state BACKUP
	interface enp0s3
	virtual_router_id 51
	priority 90
	advert_int 5
	virtual_ipaddress {
	192.168.1.200
	}
}
```

**Start Keepalived on Both Load Balancers (srvlb1 and srvlb2)**

```
sudo systemctl start keepalived
```

You can check the status of Keepalived with:

```
sudo systemctl status -l keepalived
```

**Install HAProxy on Both Load Balancers (srvlb1 and srvlb2)**

```
sudo apt install haproxy --yes
```

Stop the service for now; we will restart it after configuration:

```
sudo systemctl stop haproxy
```

<br>
</details>

<details markdown='1'>
<summary>
2. Install and Configure Application/Web Servers
</summary>

---

### 2.1. Install and Configure Apache

Install Apache, MariaDB, and Galera Cluster on all App/Web servers (srvaw1, srvaw2, and srvaw3):

```
sudo apt update
sudo apt install apache2 mariadb-server galera-4 --yes
```

Create a default web page for each server. For testing purposes, we'll include the server name to identify which server is responding. In a production environment, these files would be identical.

Delete the original file and create a new one on each server (srvaw1, srvaw2, and srvaw3):

```
sudo rm /var/www/html/index.html
sudo nano /var/www/html/index.html
```

**For srvaw1:**

```
<html>
<title>SrvAW1</title>
<body>
<h1>SrvAW1</h1>
<p>Empty yet.</p>
</body>
</html>
```

**For srvaw2:**

```
<html>
<title>SrvAW2</title>
<body>
<h1>SrvAW2</h1>
<p>Empty yet.</p>
</body>
</html>
```

**For srvaw3:**

```
<html>
<title>SrvAW3</title>
<body>
<h1>SrvAW3</h1>
<p>Empty yet.</p>
</body>
</html>
```

**Apache Configuration for Logs**

**Apache Configuration for Logs**

Since web access is forwarded through the load balancer, the App/Web servers will see the Load Balancer's IP as the client IP. As a result, all access and error logs will show the LB's IP instead of the real client IP. To log the correct client IPs, some configuration is required.

Enable the Apache2 `remoteip` module on all App/Web servers (srvaw1, srvaw2, and srvaw3):

```
sudo a2enmod remoteip
```

Configure Apache to use the `X-Forwarded-For` header (added by the load balancer) in its logs.

Edit the Apache configuration file on all app/web servers (srvaw1, srvaw2, and srvaw3):

```
sudo nano /etc/apache2/apache2.conf
```

Around line 212, add the first two lines and modify the next two lines as shown below. Remember to use your LB IPs.

```
RemoteIPHeader X-Forwarded-For
RemoteIPInternalProxy 192.168.1.201 192.168.1.202
LogFormat "%v:%p %a %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" vhost_combined
LogFormat "%a %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
```

Restart Apache on all app/web servers (srvaw1, srvaw2, and srvaw3):

```
sudo systemctl restart apache2
```

### 2.2. Configure Mariadb on App/Web Servers (srvaw1, srvaw2, and srvaw3)

**Secure Mariadb Installations** 

Run the security script to apply basic security settings to MariaDB (srvaw1, srvaw2, and srvaw3):

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

**Create a MariaDB User for Remote Access**

Create a user for testing from your workstation. Remember to use your LB IPs and a secure password. Run this on all App/Web servers (srvaw1, srvaw2, and srvaw3):
```
sudo mariadb
```

In the MariaDB shell, execute:

```
GRANT ALL ON *.* TO 'admin'@'192.168.1.201' IDENTIFIED BY 'Password12';
GRANT ALL ON *.* TO 'admin'@'192.168.1.202' IDENTIFIED BY 'Password12';
FLUSH PRIVILEGES;
EXIT;
```

**Configure Galera cluster***

Temporarily stop MariaDB on all app/web servers before configuration (srvaw1, srvaw2, and srvaw3):

```
sudo systemctl stop mariadb
```

Configure MariaDB to listen on all interfaces. This is necessary for the cluster and will also allow connections from your workstation.

Edit the configuration file on all app/web servers (srvaw1, srvaw2, and srvaw3):

```
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

Find the following line (around lines 27-30):

```
bind-address = 127.0.0.1
```

Change it to:

```
bind-address = 0.0.0.0
```

Create a new configuration file for the cluster on all app/web servers (srvaw1, srvaw2, and srvaw3):

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

Fill it with the following content, replacing the IP addresses with your own:

```
[galera]
innodb_autoinc_lock_mode = 2
wsrep_cluster_name    = "x386_cluster"
wsrep_cluster_address = "gcomm://192.168.1.203,192.168.1.204,192.168.1.205"
wsrep_provider = /usr/lib/galera/libgalera_smm.so
wsrep_provider_options = "evs.suspect_timeout=PT10S"
wsrep_on = on 
default_storage_engine = InnoDB 
innodb_doublewrite = 1 
binlog_format = ROW
```

**Start the Galera Cluster**

Initialize the cluster on the first App/Web server (srvaw1):

```
sudo galera_new_cluster
```

This command will start MariaDB on this node.

Now start MariaDB on the other nodes (srvaw2 and srvaw3):

```
sudo systemctl start mariadb
```

<br>
</details>

<details markdown='1'>
<summary>
3. Configure Web Server Load Balancing 
</summary>

---
We will configure HAProxy to load balance the three web servers (192.168.1.203, 192.168.1.204, and 192.168.1.205).

**Configure HAProxy on both Load Balancers (srvlb1 and srvlb2):**

```
sudo nano /etc/haproxy/haproxy.cfg
```

Add the following configuration to the end of the file:

```
# define frontend for apache
frontend fe_http_80
        # listen to port 80
        bind *:80
        # set the backend
        default_backend    be_http_80
        # send X-Forwarded-For header
        option   forwardfor
# define backend for apache
backend be_http_80
        # use roundrobin algorithm for balancing
        balance  roundrobin
        # define backend servers
        server   srvaw1 192.168.1.203:80 check
        server   srvaw2 192.168.1.204:80 check
        server   srvaw3 192.168.1.205:80 check
```

**Restart HAProxy on both Load Balancers (srvlb1 and srvlb2):**

```
sudo systemctl restart haproxy
```

**Explanations**

*   **Frontend:** Handles incoming connections to the Load Balancer (LB).
*   **Backend:** Defines the pool of servers to which connections are forwarded.

Let's break down the configuration:

*   `frontend fe_http_80`
    Defines a frontend and labels it `fe_http_80`. You can use any descriptive name.

*   `bind *:80`
    Instructs HAProxy to listen for incoming connections on all IP addresses of the LB on port 80.

*   `default_backend be_http_80`
    Specifies that incoming traffic for this frontend should be sent to the backend named `be_http_80`.

*   `option forwardfor`
    Captures the client's IP address and adds it to an `X-Forwarded-For` HTTP header. This allows Apache to log the real client IP instead of the LB's IP.

*   `backend be_http_80`
    Defines the backend named `be_http_80`.

*   `balance roundrobin`
    Uses the Round Robin algorithm for load balancing. This means requests are distributed to the backend servers one after the other in a circular order. Other algorithms will be explained in Section 5.

*   `server srvaw1 192.168.1.203:80 check`
    `server srvaw2 192.168.1.204:80 check`
    `server srvaw3 192.168.1.205:80 check`
    These lines list the backend servers. `srvaw1`, `srvaw2`, and `srvaw3` are labels. The IP and port specify where to forward the traffic. The `check` parameter instructs the LB to perform health checks on the backend server to see if it is alive. Other parameters will be explained in Section 5.

**Testing**

You can now connect to the website at `http://192.168.1.200` from different workstations. You should see that connections are being distributed across `192.168.1.203`, `192.168.1.204`, and `192.168.1.205`.

<br>
</details>

<details markdown='1'>
<summary>
4. Configure Mariadb Load Balancing
</summary>

---
**Notes:**

Load Balancing an application is similar to load balancing a web server. 

The key is to identify the TCP/IP port the application uses and configure HAProxy accordingly. For MariaDB, which uses port 3306, we will use the `mode tcp` directive in both the frontend and backend sections. This instructs HAProxy to perform Layer 4 (TCP) load balancing instead of Layer 7 (HTTP).

**Configure HAProxy on both Load Balancers (srvlb1 and srvlb2):**

```
sudo nano /etc/haproxy/haproxy.cfg
```

Add the following configuration to the end of the file:

```
# define frontend for mariadb
frontend fe_mariadb_3306
        mode            tcp
        # listen to port 3306
        bind *:3306
        # set the backend
        default_backend    be_mariadb_3306
# define backend for mariadb
backend be_mariadb_3306
        mode            tcp
        # use roundrobin algorithm for balancing
        balance  roundrobin
        # define backend servers
        server   srvaw1 192.168.1.203:3306 check
        server   srvaw2 192.168.1.204:3306 check
        server   srvaw3 192.168.1.205:3306 check
```

We can reload the configuration to apply these changes without interrupting the existing web server load balancing:

```
sudo systemctl reload haproxy
```

**Testing**

You can connect from your workstation using the following command.

**Remember:** You need to have the `mariadb-client` package installed on your workstation.

Use the password you set in section 2.2.

```
mariadb -u admin -p -h 192.168.1.200
```

Once connected to the MariaDB shell, you can run the following command to identify which server you are connected to:

```
SHOW VARIABLES LIKE 'hostname';
```

<br>
</details>

<details markdown='1'>
<summary>
5. More on HAProxy Configuration Options
</summary>

---
### 5.1. Default Configuration File

The default configuration file is `/etc/haproxy/haproxy.cfg`. Its initial contents are similar to the following:

```
global
        log /dev/log    local0
        log /dev/log    local1 notice
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
        stats timeout 30s
        user haproxy
        group haproxy
        daemon
        # Default SSL material locations
        ca-base /etc/ssl/certs
        crt-base /etc/ssl/private
        # See: https://ssl-config.mozilla.org/#server=haproxy&serve...
        ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDH...
        ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AE...
        ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets
defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
        errorfile 400 /etc/haproxy/errors/400.http
        errorfile 403 /etc/haproxy/errors/403.http
        errorfile 408 /etc/haproxy/errors/408.http
        errorfile 500 /etc/haproxy/errors/500.http
        errorfile 502 /etc/haproxy/errors/502.http
        errorfile 503 /etc/haproxy/errors/503.http
        errorfile 504 /etc/haproxy/errors/504.http
```

### 5.2. Explanation of Default Config Parameters

**`global` Section**

*   **`log`**: Configures logging for requests and errors. These settings usually do not need to be changed.
*   **`chroot`**: Enhances security by running HAProxy in a isolated directory, preventing access to other parts of the filesystem.
*   **`stats`**: Enables the HAProxy statistics socket for command-line access and sets its timeout value.
*   **`user`** and **`group`**: Define the system user and group under which the HAProxy process runs.
*   **`daemon`**: Runs HAProxy as a background daemon.
*   **`ca-base`** and **`crt-base`**: Define the default directories for TLS (SSL) certificates, which are used when load balancing HTTPS sites.
*   The three **`ssl-default-...`** options specify the default ciphers and protocols for SSL/TLS configuration.

Many more parameters are available. For a full reference, see: [cbonte.github.io/haproxy-dconv](https://cbonte.github.io/haproxy-dconv/2.3/configuration.html#3)

**`defaults` Section**

*   **`log global`**: Specifies that subsequent definitions will use the logging options set in the `global` section.
*   **`mode http`**: Sets the default load balancing mode to Layer 7 (HTTP). We overrode this with `mode tcp` for MariaDB to use Layer 4 (TCP) load balancing.
*   **`option httplog`**: Enables verbose logging for HTTP requests.
*   **`option dontlognull`**: Ignores and does not log connections that send no data.
*   **Timeout directives** (values in milliseconds):
    *   **`timeout connect`**: Maximum time to wait for a connection to a backend server to be established.
    *   **`timeout client`**: Maximum time to wait for client data.
    *   **`timeout server`**: Maximum time to wait for a response from a backend server.
*   **`errorfile`**: Defines the HTML files to be served when HAProxy encounters specific errors. These files can be customized.

**`frontend` Section**

This section defines the part of the Load Balancer that users connect to. Here, you define the listening IPs and ports and reference the backend section where requests should be forwarded.

**`backend` Section**

This section defines the pool of servers (IPs and ports) to which requests are forwarded. You can also define the load balancing algorithm, mode, and other server-specific parameters here.

**`listen` Section**

This is a third type of section that combines the `frontend` and `backend` definitions into a single block. It is useful for simpler configurations. Here is a basic example:

```
listen myproxy
     bind *:80
     server srv1 192.168.1.181:80
```

<br>
</details>

<details markdown='1'>
<summary>
6. Load Balancing Algorithms
</summary>

---

HAProxy supports several load balancing algorithms. Here are the most common ones:

*   **Round Robin:** Distributes traffic equally among servers in sequence.
*   **Weighted Round Robin:** Distributes traffic based on assigned server weights.
*   **Leastconn:** Sends new connections to the server with the least number of current connections.
*   **Weighted Leastconn:** Sends new connections to the server with the lowest (connections/weight) ratio.
*   **Hash (URI):** Uses a hash of the request (e.g., the URI) to always send the same type of request to the same server.
*   **First Available:** Each server accepts a defined number of connections sequentially.


### 6.1. Round Robin Algorithm

We used this algorithm for our Apache and MariaDB load balancers. It is a simple method to distribute traffic equally by forwarding requests to each server in turn.

**Example frontend and backend configuration:**

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  roundrobin
        server   srv1 192.168.1.203:80 check
        server   srv2 192.168.1.204:80 check
        server   srv3 192.168.1.205:80 check
```

### 6.2. Weighted Round Robin Algorithm

Weighted Round Robin is similar to the standard Round Robin but allows you to assign weights to backend servers. This is useful when some servers have more processing power and should handle a larger share of the traffic.

**Example configuration where `srv1` and `srv2` handle twice as much traffic as `srv3`:**

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  roundrobin
        server   srv1 192.168.1.202:80 weight 2 check
        server   srv2 192.168.1.203:80 weight 2 check
        server   srv3 192.168.1.204:80 weight 1 check
```

You can temporarily disable a backend server using the `disabled` keyword:

```
        server   srv3 192.168.1.204:80 weight 1 disabled
```

### 6.3. Leastconn Algorithm

The Leastconn algorithm distribributes traffic to the server with the fewest active connections. This is particularly useful for load balancing long-lived connections, such as with databases.

**Example frontend and backend configuration:**


```
frontend fe_mariadb_3306
        mode            tcp
        bind *:3306
        default_backend    be_mariadb_3306
backend be_mariadb_3306
        mode            tcp
        balance  leastconn
        server   srv1 192.168.1.203:3306 check
        server   srv2 192.168.1.204:3306 check
        server   srv3 192.168.1.205:3306 check
```

With this algorithm, a newly added server might immediately receive all new traffic because it has zero connections. To avoid this, use the `slowstart` parameter followed by a time period:

```
        server   srv4 192.168.1.232:3306 check slowstart 60s
```

### 6.4. Weighted Leastconn Algorithm

Weighted Leastconn is similar to the standard Leastconn algorithm but incorporates server weights. Servers with a higher weight will be able to handle more connections relative to their capacity.

**Example configuration where `srv1` and `srv2` can handle twice as many connections as `srv3`:**

```
frontend fe_mariadb_3306
        mode            tcp
        bind *:3306
        default_backend    be_mariadb_3306
backend be_mariadb_3306
        mode            tcp
        balance  leastconn
        server   srv1 192.168.1.203:3306 weight 2 check
        server   srv2 192.168.1.204:3306 weight 2 check
        server   srv3 192.168.1.205:3306 weight 1 check
```

### 6.5. HASH Uri Algorithm

This algorithm is highly useful for load balancing static web servers with caching. It hashes the request URI (or part of it) to ensure the same request is always forwarded to the same backend server, thereby increasing cache hits and performance.

**Example frontend and backend configuration:**

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  uri
        server   srv1 192.168.1.203:80 check
        server   srv2 192.168.1.204:80 check
        server   srv3 192.168.1.205:80 check
```

This algorithm can also be used in weighted mode to better utilize faster servers.

**Example with weights, where `srv1` and `srv2` handle more traffic:**

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  uri
        server   srv1 192.168.1.202:80 weight 2 check
        server   srv2 192.168.1.203:80 weight 2 check
        server   srv3 192.168.1.204:80 weight 1 check
```

### 6.6. First Available Algorithm

This algorithm uses servers sequentially. It directs connections to the first server until it reaches a specified maximum connection count, then moves to the next server. This can be useful for cost-saving when you don't want to spin up additional servers unless necessary.

**Example configuration where each server handles up to 50 connections:**

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  first
        server   srv1 192.168.1.203:80 maxconn 50
        server   srv2 192.168.1.204:80 maxconn 50
        server   srv3 192.168.1.205:80 maxconn 50
```

<br>
</details>

<details markdown='1'>
<summary>
7. URL Redirection
</summary>

---

HAProxy can redirect requests based on the URL path, URL parameters, HTTP headers, or the HTTP host address. This functionality can significantly optimize traffic handling in various scenarios.

### 7.1. URL Path Redirection

**Scenario**

Assume we have three folders on our web servers: `folder1`, `folder2`, and `folder3`. We want to redirect requests for `folder1` to `srvaw1`, `folder2` to `srvaw2`, and `folder3` to `srvaw3`. All other traffic should be load-balanced as defined in Section 3.

**Configuration**

Edit the HAProxy configuration file on the load balancers:

```
sudo nano /etc/haproxy/haproxy.cfg
```

Remove the previously added backend and frontend sections for HTTP and add the following to the end of the file:

```
frontend fe_http_80
	bind *:80
	acl acl_folder1 path_beg -i /folder1
	use_backend be_folder1 if acl_folder1
	acl acl_folder2 path_beg -i /folder2
	use_backend be_folder2 if acl_folder2
	acl acl_folder3 path_beg -i /folder3
	use_backend be_folder3 if acl_folder3
	default_backend    be_http_80
        option   forwardfor
backend be_folder1
        server   srvaw1 192.168.1.203:80 check
backend be_folder2
        server   srvaw2 192.168.1.204:80 check
backend be_folder3
        server   srvaw3 192.168.1.205:80 check
backend be_http_80
        balance  roundrobin
        server   srvaw1 192.168.1.203:80 check
        server   srvaw2 192.168.1.204:80 check
        server   srvaw3 192.168.1.205:80 check
```

**Restart or Reload HAProxy**

To apply the changes, you can restart HAProxy:


```
sudo systemctl restart haproxy
```

If HAProxy is already active and you want to avoid dropping connections, reload it instead:

```
sudo systemctl reload haproxy
```
 
**Explanations**

ACLs (Access Control Lists) are used to define conditions for matching requests.

*   `acl acl_folder1 path_beg -i /folder1`
    *   `acl` is the keyword to define an ACL.
    *   `acl_folder1` is the name given to this ACL.
    *   `path_beg` is the condition, meaning the URL path begins with the following string.
    *   `-i` makes the string match case-insensitive.
    *   `/folder1` is the string we are looking for.

The ACL `acl_folder1` is activated when a URL path starts with `/folder1`, for example:  
`http://www.386387.xyz/folder1`

For a URL like `http://www.386387.xyz/folder1/folder2/folder3`, the URL Path is `/folder1/folder2/folder3`.

*   `use_backend be_folder1 if acl_folder1`
    This directive instructs HAProxy to use the servers in the `be_folder1` backend when `acl_folder1` is activated.

Similar ACLs and backends are created for `/folder2` and `/folder3`.

There are other conditions for matching URL paths. Here is a list:

*   `path`: Exact URL path match.
*   `path_beg`: URL path begins with the string.
*   `path_end`: URL path ends with the string.
*   `path_sub`: URL path contains the string as a substring.
*   `path_dir`: URL path has the string as a subdirectory.
*   `path_len`: Exact length of the URL path.
*   `path_reg`: Regex match of the URL path.

**URL Path ACL Examples**

An ACL for an exact info page:
```
acl acl_info path -i /info/info.html
```

An ACL for JPG and PNG images:
```
acl acl_image path_end .jpg .png
```

An ACL for image directories:
```
acl acl_image2 path_dir -i /images
```

An ACL for URL paths longer than 20 characters:
```
acl acl_long path_len gt 20
```

An ACL for paths containing "cart":
```
acl acl_cart path_sub -i cart
```

An ACL for images using a regular expression:
```
acl acl_image3 path_reg (jpg|jpeg|bmp|gif|png)
```

### 7.2. URL Parameter Redirection

A URL parameter is a key-value pair (e.g., `variable=value`). Many websites, like Google and DuckDuckGo, use them. For example:  
`https://www.example.org/?s=searchterm`

Here, `s` is the variable (for "search") and `searchterm` is the value. HAProxy can capture these parameters and redirect specific key-value pairs to different backends.

**Example**

Assume we have a parameter named `block_number` with possible values: `first`, `second`, `third`, and `rest`. A URL for the first block would look like:  
`http://www.386387.xyz/?block_number=first`

We want to redirect:
*   `first` to one backend.
*   `second` and `third` to another backend.
*   `rest` to a third backend.

A sample frontend configuration would be:

```
frontend fe_blocks
	bind *:80
	acl acl_block1 url_param(block_number) -i -m str first
	use_backend be_block1 if acl_block1
	acl acl_block23 url_param(block_number) -i -m str second third
	use_backend be_block23 if acl_block23
	acl acl_blockrest url_param(block_number) -i -m str rest
	use_backend be_blockrest if acl_blockrest
	default_backend blocks
```

The `-i` directive enables case-insensitive matching. The `-m str` directive enables exact string matching for the values provided.

### 7.3. HTTP Header Redirection
HTTP headers contain information such as `User-Agent`, `Host` (the website address), `Content-Type`, and `Referer`. For a full list, please refer to:  
[https://en.wikipedia.org/wiki/List_of_HTTP_header_fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

A `User-Agent` header might look like this:  
`Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0`

A `Host` header might look like this:  
`Host: www.386387.xyz`

**Example: Redirecting Mobile Traffic**

The following frontend configuration redirects requests from mobile devices to a specific backend based on the `User-Agent` header.


```
frontend be_http
	bind *:80
	acl acl_mobile req.hdr(User-Agent) -i -m reg (android|iphone)
	use_backend be_mobile if acl_mobile
	default_backend be_http
```

<br>
</details>

<details markdown='1'>
<summary>
8. Enabling HTTPS at HAProxy
</summary>

---

This section covers enabling HTTPS in HAProxy using free TLS (SSL) certificates from Let's Encrypt, managed by the Certbot tool for automatic renewals every 90 days.

All steps described here have been tested. Since Let's Encrypt requires internet-accessible servers for domain validation, this section uses VPS servers. For simplicity, we'll use a single HAProxy server and two web servers (without Keepalived).

### 8.0. Configurations & Considerations (For this section only)

**Server Setup:**

- `www.386387.xyz`: Load Balancer → `159.203.70.143`
- `srv1.386387.xyz`: Web Server 1 → `64.225.29.174`
- `srv2.386387.xyz`: Web Server 2 → `165.227.176.14`


Tested on Debian 13/12 and Ubuntu 24.04/22.04 LTS Servers.

We start with freshly installed servers.

**Challenge:** To obtain and renew Let's Encrypt certificates with Certbot, a web server must be accessible on port 80. However, HAProxy also needs to bind to port 80. This creates a conflict.

**Solution:** We install Apache on the Load Balancer but bind it only to the loopback interface (`127.0.0.1`). HAProxy will bind to the server's public IPs. We then configure HAProxy to redirect Let's Encrypt validation requests (to the `/.well-known/acme-challenge` directory) to the local Apache instance. This allows both Apache and HAProxy to coexist on port 80.


### 8.1. Initial Installs 

**Install HAProxy on the Load Balancer (`www.386387.xyz`):**

```
sudo apt update
sudo apt install haproxy --yes
sudo systemctl stop haproxy
```

**Install Apache on the Web Servers (`srv1.386387.xyz` and `srv2.386387.xyz`):**

```
sudo apt update
sudo apt install apache2 --yes
```

**Create a test page on each web server:**

```
sudo rm /var/www/html/index.html
sudo nano /var/www/html/index.html
```

**For `srv1.386387.xyz`:**

```
<html>
<title>SrvAW1</title>
<body>
<h1>Srv1</h1>
<p>Empty yet.</p>
</body>
</html>
```

**For `srv2.386387.xyz`:**

```
<html>
<title>SrvAW1</title>
<body>
<h1>Srv2</h1>
<p>Empty yet.</p>
</body>
</html>
```

### 8.2. Install and Configure Apache on the Load Balancer (Run on `www.386387.xyz`)

```
sudo apt update
sudo apt install apache2 --yes
```

Apache might fail to start due to port 80 being occupied by HAProxy. This is expected and will be resolved.

**Configure Apache to bind only to the loopback interface:**

```
sudo nano /etc/apache2/ports.conf
```

Modify the file to look like this:

```
Listen 127.0.0.1:80
<IfModule ssl_module>
        Listen 127.0.0.1:443
</IfModule>
<IfModule mod_gnutls.c>
        Listen 127.0.0.1:443
</IfModule>
```

**Configure the default virtual host:**

```
sudo nano /etc/apache2/sites-available/000-default.conf
```

Update the file with your domain(s):

```
<VirtualHost 127.0.0.1:80>
        ServerAdmin webmaster@localhost
        ServerName www.386387.xyz
        ServerAlias 386387.xyz
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

**Create the Let's Encrypt challenge directory:**

```
sudo mkdir -p /var/www/html/.well-known/acme-challenge
```

**Restart Apache:**

```
sudo systemctl restart apache2
```

### 8.3. Configure HAProxy to Redirect to Apache (Run on `www.386387.xyz`)

Edit the HAProxy configuration file

```
sudo nano /etc/haproxy/haproxy.cfg
```

Add the following to the end of the file. Replace the IP address in the `bind` directive with your Load Balancer's public IP (find it using `ip a`).

```
frontend fe_http
        bind 159.203.70.143:80
        acl acl_acme path_beg -i /.well-known/acme-challenge
        use_backend be_acme if acl_acme
backend be_acme
        server self 127.0.0.1:80 check
```

**Restart HAProxy:**

```
sudo systemctl restart haproxy
```

### 8.4. Install and Run Certbot (Run on `www.386387.xyz`)

**Install Certbot:**

```
sudo apt update
sudo apt install --yes  certbot
```

**Generate certificates using the webroot plugin. Replace the domains with your own:**

```
sudo certbot certonly --webroot --webroot-path /var/www/html \
   -d www.386387.xyz,386387.xyz
```

### 8.5. Generate Certificate for HAProxy (Run on www.386387.xyz)

Let's Encrypt certificates are stored in `/etc/letsencrypt/live/`. Your directory will be named after your primary domain.

**Find your certificate directory:**

```
sudo ls -al /etc/letsencrypt/live
```

HAProxy requires the certificate and private key to be in a single file. Replace `www.386387.xyz` with your actual domain name from the command above.

```
sudo -i
cd /etc/letsencrypt/live/www.386387.xyz
cat fullchain.pem privkey.pem >> haproxy.pem
exit
```

### 8.6. Configure HAProxy (Run on www.386387.xyz)

We will now update the HAProxy configuration to handle HTTPS traffic and load balance the backend servers.

```
sudo nano /etc/haproxy/haproxy.cfg
```

Replace the configuration at the end of the file with the following:

 
```
frontend fe_http
        bind 159.203.70.143:80
        bind 159.203.70.143:443 ssl crt /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
        acl acl_acme path_beg -i /.well-known/acme-challenge
        use_backend be_acme if acl_acme
        default_backend    be_http
        option   forwardfor
backend be_acme
        server self 127.0.0.1:80 check
backend be_http
        balance  roundrobin
        server   srv1 64.225.29.174:80 check
        server   srv2 165.227.176.14:80 check
```

**Restart HAProxy:**

```
sudo systemctl restart haproxy
```

HTTPS is now active, but we will add further refinements.

### 8.7. Test Certificate Renewal and Add Renewal Hooks (Run on `www.386387.xyz`)

Let's Encrypt certificates are valid for 90 days. Certbot can automatically renew them. Test the renewal process with a dry run:

```
sudo certbot renew --dry-run
```

If this runs without errors, automatic renewal should work.

However, every time the certificate is renewed, we must regenerate the combined `haproxy.pem` file and reload HAProxy. We can automate this by placing a script in the Certbot renewal hooks directory.

Certbot executes scripts in `/etc/letsencrypt/renewal-hooks/deploy/` after a successful renewal.

**Create the hook script:**

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/haproxy.sh
```

Add the following content, replacing the domain name with yours:

```
cat /etc/letsencrypt/live/www.386387.xyz/fullchain.pem /etc/letsencrypt/live/www.386387.xyz/privkey.pem \
  >> /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
systemctl restart haproxy
```

**Make the script executable:**

```
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/haproxy.sh
```

### 8.8. Explanations

At this stage, we have a fully functional HTTPS setup with automatic certificate renewal. Note that only the traffic between the client and the Load Balancer is encrypted (TLS Termination). The traffic between the Load Balancer and the web servers is still in plain HTTP.

For enhanced security, especially if your web servers are internet-accessible, we can encrypt this backend traffic as well using TLS Re-Encryption. We will achieve this by using self-signed certificates on the web servers and configuring HAProxy to connect to them via HTTPS.

### 8.9. Enable HTTPS on the Web Servers (Run on `srv1.386387.xyz` and `srv2.386387.xyz`)

**Enable the Apache SSL module:**

```
sudo a2enmod ssl
sudo systemctl restart apache2
```

**Create a directory for certificates:**

```
sudo mkdir /etc/apache2/certs
```

**Generate a self-signed certificate (valid for ~20 years):**

```
sudo openssl req -x509 -nodes -days 7300 -newkey rsa:2048 \
-keyout /etc/apache2/certs/www.386387.xyz.key -out /etc/apache2/certs/www.386387.xyz.crt
```

Fill in the prompts appropriately when asked.

**Create a new virtual host configuration for SSL:**

```
sudo nano /etc/apache2/sites-available/000-virtual-ssl.conf
```

Add the following configuration:

```
<IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerName www.386387.xyz
        ServerAlias 386387.xyz
        ServerAdmin webmaster@www.386387.xyz
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/www.386387.xyz-error.log
        CustomLog ${APACHE_LOG_DIR}/www.386387.xyz-access.log combined
        SSLEngine on
        SSLCertificateFile	/etc/apache2/certs/www.386387.xyz.crt
        SSLCertificateKeyFile	/etc/apache2/certs/www.386387.xyz.key
    </VirtualHost>
</IfModule>
```

**Enable the SSL site and reload Apache:**

```
sudo a2ensite 000-virtual-ssl.conf
sudo systemctl reload apache2
```

The web servers are now ready for HTTPS connections. The next step is to configure HAProxy to use HTTPS for backend connections.

### 8.10. Configure HAProxy for Backend HTTPS (TLS Re-Encryption) (Run on `www.386387.xyz`)

```
sudo nano /etc/haproxy/haproxy.cfg
```

Locate the `backend be_http` section and modify the `server` lines to use port 443 and the `ssl` and `verify none` parameters (since we are using self-signed certificates):


```
backend be_http
        balance  roundrobin
        server   srv1 64.225.29.174:443 check ssl verify none
        server   srv2 165.227.176.14:443 check ssl verify none
```

**Restart HAProxy:**

```
sudo systemctl restart haproxy
```

### 8.11. Auto HTTP to HTTPS Redirection (Run on www.386387.xyz)

To ensure all traffic uses encryption, we can force HTTP requests to redirect to HTTPS.

Edit the HAProxy configuration:

```
sudo nano /etc/haproxy/haproxy.cfg
```

In the `frontend fe_http` section, add the following `redirect` rule after the `bind` lines:

```
        redirect scheme https if !{ ssl_fc }
```

The updated frontend section should look like this:

```
frontend fe_http
        bind 159.203.70.143:80
        bind 159.203.70.143:443 ssl crt /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
        redirect scheme https if !{ ssl_fc }
        acl acl_acme path_beg -i /.well-known/acme-challenge
        use_backend be_acme if acl_acme
        default_backend    be_http
        option   forwardfor
```

**Restart HAProxy:**

```
sudo systemctl restart haproxy
```

### 8.12. Server Persistence (Sticky Sessions) with Cookies

For applications that require session persistence (e.g., when users are logged in), we need to ensure a client is directed to the same backend server for the duration of their session. This can be achieved using cookies.

Edit the HAProxy configuration:

```
sudo nano /etc/haproxy/haproxy.cfg
```

Modify the `backend be_http` section to include cookie-based persistence:

```
backend be_acme
        server self 127.0.0.1:80 check
backend be_http
        balance roundrobin
        cookie ACTIVESERVER insert indirect nocache
        server srv1 64.225.29.174:443 check cookie srv1 ssl verify none 
        server srv2 165.227.176.14:443 check cookie srv2 ssl verify none 
```

**Restart HAProxy:**

```
sudo systemctl restart haproxy
```

### 8.13. Final Contents of HAProxy Config File

The final `/etc/haproxy/haproxy.cfg` file should look similar to this:

```
global
        log /dev/log    local0
        log /dev/log    local1 notice
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd lis>
        stats timeout 30s
        user haproxy
        group haproxy
        daemon
        # Default SSL material locations
        ca-base /etc/ssl/certs
        crt-base /etc/ssl/private
        # See: https://ssl-config.mozilla.org/#server=haproxy&server-version=2.>
        ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128>
        ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SH>
        ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets
defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
        errorfile 400 /etc/haproxy/errors/400.http
        errorfile 403 /etc/haproxy/errors/403.http
        errorfile 408 /etc/haproxy/errors/408.http
        errorfile 500 /etc/haproxy/errors/500.http
        errorfile 502 /etc/haproxy/errors/502.http
        errorfile 503 /etc/haproxy/errors/503.http
        errorfile 504 /etc/haproxy/errors/504.http
frontend fe_http
        bind 159.203.70.143:80
        bind 159.203.70.143:443 ssl crt /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
        redirect scheme https if !{ ssl_fc }
        acl acl_acme path_beg -i /.well-known/acme-challenge
        use_backend be_acme if acl_acme
        default_backend    be_http
        option   forwardfor
backend be_acme
        server self 127.0.0.1:80 check
backend be_http
        balance  roundrobin
        cookie ACTIVESERVER insert indirect nocache
        server srv1 64.225.29.174:443 check cookie srv1 ssl verify none 
        server srv2 165.227.176.14:443 check cookie srv2 ssl verify none 
```

</details>

