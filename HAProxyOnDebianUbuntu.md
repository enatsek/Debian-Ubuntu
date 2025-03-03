##### HAProxyOnDebianUbuntu 
# High Availability with HAProxy Load Balancer on Debian and Ubuntu

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.0. Abstract
High Availability Load Balancing with Letsencrypt free certificates HTTPS support.

### 0.1. Definitions
HAProxy is a powerful software for Load Balancing. 

It can be used for Level 4 (TCP) or Level 7 (HTTP) load balancing. That  means you can use it to share load on web sites or directly client server  programs.

### 0.2. Configurations

srv    : Load Balancer floating IP --> 192.168.1.210  
srvlb1 : Load Balancer 1  --> 192.168.1.221   
srvlb2 : Load Balancer 2  --> 192.168.1.222   
srvaw1 : App/Web Server 1 --> 192.168.1.223  
srvaw2 : App/Web Server 2 --> 192.168.1.224  
srvaw3 : App/Web Server 3 --> 192.168.1.225  
My SMTP Server --> 192.168.1.140 (for keepalived notify messages)

Tested with Debian 12/11 and Ubuntu 24.04/22.04 LTS Servers

A keepalived cluster of 2 load balancers will be used. Normally the first server will run, but if an error happens on the first load balancer or if it is powered off, the second load balancer will take the control of balancing. This step is not absolutely necessary but it eliminates the risk of Single Point of Failure.

This way, our infrastructure keeps running if any of the servers go offline.

2 Load Balancers will be configured with the floating IP of 192.168.1.210. An email from keepalived@www.386387.xyz to notify@www.386387.xyz will be sent if any error occurs or main server changes. 

Our Application or Web Servers must be configured exactly the same way. That way the users will never know to which server they are connected. 

For our examples, we'll install Apache and Mariadb to each App/Web server.

We'll also install galera cluster to the servers to establish Mariadb clustering. 

That way, any change of the database on a server will be replicated to the others.

First we'll load balance the web server, than we'll load balance the Mariadb database usage. At that time, you'll realize, you can load balance any kind of software.

The users only see the floating IP (192.168.1.210) of the Load Balancers, they will never see or realize the other servers or their IPs.

### 0.3. Sources:
[www.haproxy.org](https://www.haproxy.org/)  
[www.server-world.info](https://www.server-world.info/en/note?os=Ubuntu_20.04&p=haproxy&f=1)  
[cbonte.github.io/haproxy-dconv](https://cbonte.github.io/haproxy-dconv/2.3/configuration.html)  
[cbonte.github.io/haproxy-dconv](https://cbonte.github.io/haproxy-dconv/2.3/management.html)  
Book: ISBN: 9781519073846 **Load Balancing with HAProxy** by Nick Ramirez

<br>
</details>

<details markdown='1'>
<summary>
1. Install and Configure Load Balancers
</summary>
---
### 1.1. Install keepalived (srvlb1 and srvlb2)
```
sudo apt update
sudo apt install keepalived --yes
```

### 1.2. Configure First Load Balancer (srvlb1)
Create a config file

```
sudo nano /etc/keepalived/keepalived.conf
```

Fill it as below, remember to change to your IPs, also remember to rename your network adapter from enp0s3 to whatever yours is.

```
global_defs {
	notification_email {
	notify@www.386387.xyz
	}
	notification_email_from keepalived@www.386387.xyz
	smtp_server 192.168.1.140
	smtp_connect_timeout 30
	router_id load_balancer
}
vrrp_instance VI_1 {
	smtp_alert
	interface enp0s3
	virtual_router_id 51
	priority 100
	advert_int 5
	virtual_ipaddress {
	192.168.1.210
	}
}
```

### 1.3. Configure Second Load Balancer (srvlb2)
Create a config file

```
sudo nano /etc/keepalived/keepalived.conf
```

Fill it as below, remember to change to your IPs, also remember to rename your network adapter from enp0s3 to whatever yours is.

```
global_defs {
	notification_email {
	notify@www.386387.xyz
	}
	notification_email_from keepalived@www.386387.xyz
	smtp_server 192.168.1.140
	smtp_connect_timeout 30
	router_id load_balancer
}
vrrp_instance VI_1 {
	smtp_alert
	interface enp0s3
	virtual_router_id 51
	priority 90
	advert_int 5
	virtual_ipaddress {
	192.168.1.210
	}
}
```

### 1.4. Start keepalived on Load Balancers (srvlb1 and srvlb2)
```
sudo systemctl start keepalived
```

You can check the status of keepalived with the following command:

```
sudo systemctl status -l keepalived
```

### 1.5. Install haproxy on Load Balancers (srvlb1 and srvlb2)
```
sudo apt install haproxy --yes
```

Stop it for now, we'll restart it after configuring

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
### 2.1. Install Apache, Mariadb and Galera Cluster on App/Web Servers (srvaw1, srvaw2, and srwaw3)

```
sudo apt update
sudo apt install apache2 mariadb-server galera-4 --yes
```

### 2.2. Create Default Web Pages for App/Web Servers
#### 2.2.1. Create a Default Web Page for the First Server (srvaw1)
Delete the original one

```
sudo rm /var/www/html/index.html
```

Create and Fill the new one

```
sudo nano /var/www/html/index.html
```

Normally, they should have all the same html files, but just to test load balancing we'll put a slight information about the server name.

```
<html>
<title>SrvAW1</title>
<body>
<h1>SrvAW1</h1>
<p>Empty yet.</p>
</body>
</html>
```

#### 2.2.2. Create a Default Web Page for the Second Server (srvaw2)
Delete the original one

```
sudo rm /var/www/html/index.html
```

Create and fill the new one

```
sudo nano /var/www/html/index.html
```

Normally, they should have the same html files, but just to test load  balancing we'll put a slight information about the server name

```
<html>
<title>SrvAW2</title>
<body>
<h1>SrvAW2</h1>
<p>Empty yet.</p>
</body>
</html>
```

#### 2.2.3. Create a Default Web Page for the Third Server (srvaw3)
Delete the original one

```
sudo rm /var/www/html/index.html
```

Create and fill the new one

```
sudo nano /var/www/html/index.html
```

Normally, they should have the same html files, but just to test load  balancing we'll put a slight information about the server name

```
<html>
<title>SrvAW3</title>
<body>
<h1>SrvAW3</h1>
<p>Empty yet.</p>
</body>
</html>
```

### 2.3. Apache Configuration for Logs (srvaw1, srvaw2, and srvaw3)
Because the web access is forwarded through the load balancer, our app/web servers sees the IP of the LB (Load Balancer) as the connecting IP. 

That way, all of the access logs (and error logs) will contain the IP of  the LB only. To overcome this situation and log the correct IPs, some configurations are needed.

#### 2.3.1. Enable Apache2 remoteip Mod (srvaw1, srvaw2, and srvaw3)
```
sudo a2enmod remoteip
```

#### 2.3.2. Change Apache Log to Contain Real IPs (srvaw1, srvaw2, and srvaw3)
When the LB forward the request, it adds a X-Forwarded-For header to the  request. We'll configure Apache2 to include the contents of that header  in the log file.

Edit Apache config file

```
sudo nano /etc/apache2/apache2.conf
```

Around line 212, add the first 2 lines, and change the second 2 lines as  below. Remember to use both of your LB IPs.

```
RemoteIPHeader X-Forwarded-For
RemoteIPInternalProxy 192.168.1.221 192.168.1.222
LogFormat "%v:%p %a %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" vhost_combined
LogFormat "%a %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
```

#### 2.3. Restart Apache (srvaw1, srvaw2, and srvaw3)
```
sudo systemctl restart apache2
```

### 2.4. Configure Mariadb on App/Web Servers (srvaw1, srvaw2, and srvaw3)
#### 2.4.1. Secure Mariadb Installations (srvaw1, srvaw2, and srvaw3)
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

#### 2.4.2. Create a Mariadb User to Access from Our Workstation (srvaw1, srvaw2, and srvaw3)
Will be used for testing, remember to change to your LB IPs and give your  password.

```
sudo mariadb
```

Run on mariadb shell

```
GRANT ALL ON *.* TO 'admin'@'192.168.1.221' IDENTIFIED BY 'Password12';
GRANT ALL ON *.* TO 'admin'@'192.168.1.222' IDENTIFIED BY 'Password12';
FLUSH PRIVILEGES;
EXIT;
```

### 2.5. Configure Galera Cluster on Mariadb (srvaw1, srvaw2, and srvaw3)
#### 2.5.1. Temporarily Stop Mariadb Before Configuration (srvaw1, srvaw2, and srvaw3)

```
sudo systemctl stop mariadb
```

#### 2.5.2. Enable Mariadb Binds to Other Computers (srvaw1, srvaw2, and srvaw3)
This is necessary for the cluster, also will let us join Mariadb from our workstation.

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

#### 2.5.3. Configure Galera Cluster on Mariadb (srvaw1, srvaw2, and srvaw3)

Create a new conf file and fill it

```
sudo nano /etc/mysql/mariadb.conf.d/99-cluster.cnf
```

Fill as below, remember to use your ip addresses

```
[galera]
innodb_autoinc_lock_mode = 2
wsrep_cluster_name    = "x386_cluster"
wsrep_cluster_address = "gcomm://192.168.1.223,192.168.1.224,192.168.1.225"
wsrep_provider = /usr/lib/galera/libgalera_smm.so
wsrep_provider_options = "evs.suspect_timeout=PT10S"
wsrep_on = on 
default_storage_engine = InnoDB 
innodb_doublewrite = 1 
binlog_format = ROW
```

#### 2.5.4. Start Galera Cluster On First App/Web Server (srvaw1)
**!!! You should run this only on one of the servers !!!**

```
sudo galera_new_cluster
```

This command should also starts mariadb on this node

#### 2.5.5. Start Mariadb on Other Nodes too (srvaw2 and srvaw3)

Run on the other servers:

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
We'll configure HAProxy to load balance 3 web servers (192.168.1.223,  192.168.1.224 and 192.168.1.225. 

### 3.1. Configure HAProxy (srvlb1 and srvlb2)
```
sudo nano /etc/haproxy/haproxy.cfg
```

Add to the end of the file

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
        server   srvaw1 192.168.1.223:80 check
        server   srvaw2 192.168.1.224:80 check
        server   srvaw3 192.168.1.225:80 check
```

### 3.2. Restart haproxy (srvlb1 and srvlb2)
```
sudo systemctl restart haproxy
```

### 3.3. Explanations
frontend is the incoming connection(s) coming to LB (Load Balancer)  
backend is the forwarding places for these icoming connection(s)  

`frontend fe_http_80`

Define a frontend connection and label it as fe_http_80. You can label it  whatever you want.

`bind *:80`

Listen incoming connection from all the IPs of the LB at port 80

`default_backend    be_http_80`

The backend for this frontend is named as be_http_80

`option  forwardfor`

Capture the IP of the client at add it with a X-Forwarded-For header. We  will use this IP at Apache log.

`backend be_http_80`

Define the backend named as be_http_80

`balance  roundrobin`

Roundrobin algorithm is used for load balancing. There are some other  algorithms too, and they will be explained at 5. Round robin algorithm  means the servers will be selected as one by one. 

`server   srvaw1 192.168.1.223:80 check`  
`server   srvaw2 192.168.1.224:80 check`  
`server   srvaw3 192.168.1.225:80 check`  

List of backend servers. srvaw1, srvaw2 and srvaw3 are used as labels. IP  and port will be used as forwarding ip and port. check parameter informs # the LB to check the backend server if the ip and port is alive. There are  some other parameters too, and they will be explained at 5.

### 3.4. Testing
You can connect to web site http://192.168.1.210 from different  workstations and see it is connecting to 192.168.1.223, 192.168.1.224, and 192.168.1.225.

<br>
</details>

<details markdown='1'>
<summary>
4. Configure Mariadb Load Balancing
</summary>
---
### 4.1. Explanations
Load Balancing an application is similar to load balancing a web server. 

All we need is determining the TCP/IP port it is using and making the  configurations using that port. We also use mode directive with tcp  keyword at backend and frontend sections to instruct HAProxy that it will  use tcp (level 4) load balancing.

Mariadb uses port 3306, so we'll make configurations with that port.

### 4.2. Configure HAProxy (srvlb1 and srvlb2)
```
sudo nano /etc/haproxy/haproxy.cfg
```

Add to the end of the file:

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
        server   srvaw1 192.168.1.223:3306 check
        server   srvaw2 192.168.1.224:3306 check
        server   srvaw3 192.168.1.225:3306 check
```

### 4.3. Reload haproxy (srvlb1 and srvlb2)
We can reload the conf, without interrupting web server balancing 

```
sudo systemctl reload haproxy
```

### 4.4. Testing
You can connect from your workstation using the following command. 

**Remember:** you need to install mariadb-client package in your workstation, if you haven't done so already.

Use the password given at 2.4.2.

```
mariadb -u admin -p -h 192.168.1.210
```

If you run the following command on mariadb shell, you can tell which  server you connected.

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
Default configuration file is as below:

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
#### 5.2.1. global Section
The settings for "global" section is for HAProxy process settings.

- **log** options set up logging for requests and errors. Most of the time we don't need to change them.
- **chroot** option makes HAProxy run under that specific diretory, and  prevents it from accessing any other place, thus enables enhanced  security.
- **stats** options enables accessing HAProxy from the command line, and  sets it timeout value. 
- **user** and **group** options sets the user and group that HAProxy runs as.
- **daemon** option makes HAProxy run as a background process.
- **ca-base** and **crt-base** options defines the TLS (SSL) certificates if we enable SSL. We will use them when we load balance SSL sites.
- The 3 **ssl-default-**... options are specifications for SSL configuration.
 
There are much more parameters, refer to:  
[cbonte.github.io/haproxy-dconv](https://cbonte.github.io/haproxy-dconv/2.3/configuration.html#3)

#### 5.2.2. defaults Section
This section is for the default values for which we define load balancing. 

- **log global** option says that our definitions will use global log  options.
- **mode http** option states that load balancing operate on level 7 (http), if we set it as "home tcp" it operates at level 4 (tcp), as we did for mariadb load balancing.
- **option httplog** HTTP messages logging is verbosed
- **option dontlognull** don't log requests with no data
- 3 **timeout** options with milisecond values. **connect** for connection to backend servers, **client** for waiting for a client, **server** when a
response is expected from a backend server.
- **errorfile** options defines the error message html files when there is an error at the HAProxy itself. These files can be modified.

### 5.3. Other Sections
The other sections are the options we add to the end of the config file. 

At 3. and 4. we used "backend" and "frontend" sections. 

#### 5.3.1. frontend Section
frontend section defines the part of Load Balancing which is seen by the  users. We can define listening IPs and Ports here, and reference the  backend section to forward the requests.

#### 5.3.2. backend Section
In this section, we define the IPs and Ports to forwarded, we can define  algorithm, mode and some other values here.

#### 5.3.3. listen Section
There is one more possible section, which is "listen". Is it somewhat a  combination of frontend and backend. Below is a very simple example:

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
- Round Robin: Split Traffic Equally
- Weighted Round Robin: Split Traffic by Weight
- Leastconn: Split Connections Equally
- Weighted Leastconn: Split Connections by Weight
- Hash: The same requests always goes to the same servers.
- First Available: Each server sequentially take some number of connections.

### 6.1. Round Robin Algorithm
For our Apache and Mariadb LB, we used this algorithm. It is a very  simple way to split the traffic equally among the servers. All the  requests are forwarded to each server sequentially.

Example frontend and backend sections:

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  roundrobin
        server   srv1 192.168.1.223:80 check
        server   srv2 192.168.1.224:80 check
        server   srv3 192.168.1.225:80 check
```

### 6.2. Weighted Round Robin Algorithm
Weighted Round Robing is similar to standart Round Robin, just you can  set weights to the backends, so that they can have more traffic. It is  useful, if some of your servers have more processing power.

Example frontend and backend sections, srv1 and srv2 will have 2 times  more of traffic than srv3:

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  roundrobin
        server   srv1 192.168.1.222:80 weight 2 check
        server   srv2 192.168.1.223:80 weight 2 check
        server   srv3 192.168.1.224:80 weight 1 check
```

You can temporarily disable a backend server by disabled keyword:

```
        server   srv3 192.168.1.224:80 weight 1 disabled
```

### 6.3. Leastconn Algorithm
Leastconn algorithm splits the traffic amongst the server regarding the  connection numbers. So that, all the servers gets equal number of  connections. It is very useful for Load Balancing databases.

Example frontend and backend sections:

```
frontend fe_mariadb_3306
        mode            tcp
        bind *:3306
        default_backend    be_mariadb_3306
backend be_mariadb_3306
        mode            tcp
        balance  leastconn
        server   srv1 192.168.1.223:3306 check
        server   srv2 192.168.1.224:3306 check
        server   srv3 192.168.1.225:3306 check
```

With this algorith, a newly added server may have all the traffic # because it has no connection, to avoid it, there is a keyword named as  slowstart followed by time :

```
        server   srv4 192.168.1.232:3306 check slowstart 60s
```

### 6.4. Weighted Leastconn Algorithm
Weighted Leastconn is similar to standart Leastconn algorithm , just you  can set weights to the backends, so that they can have more traffic. It is # useful, if some of your servers have more processing power.

Example frontend and backend sections, srw1 and srv2 will have 2 times  more of connections than srv3:

```
frontend fe_mariadb_3306
        mode            tcp
        bind *:3306
        default_backend    be_mariadb_3306
backend be_mariadb_3306
        mode            tcp
        balance  leastconn
        server   srv1 192.168.1.223:3306 weight 2 check
        server   srv2 192.168.1.224:3306 weight 2 check
        server   srv3 192.168.1.225:3306 weight 1 check
```

### 6.5. HASH Uri Algorithm
This algorithm is very useful especially when load balancing static web  servers with caching. This algorithm always forwards the same requests to  the same nodes. This way, cache hits and performance increase.

Example frontend and backend sections:

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  uri
        server   srv1 192.168.1.223:80 check
        server   srv2 192.168.1.224:80 check
        server   srv3 192.168.1.225:80 check
```

This algorithm can be used in weighted mode too. This way you can utilize the faster servers better. 

Example frontend and backend sections, srw1 and srv2 will have 2 times  more of traffic than srv3:

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  uri
        server   srv1 192.168.1.222:80 weight 2 check
        server   srv2 192.168.1.223:80 weight 2 check
        server   srv3 192.168.1.224:80 weight 1 check
```

### 6.6. First Available Algorithm
This algorithm allows to use servers sequentially, but steps up to next  server when specified number of connection is established. That way, it  will use srv1 until the first (say) 50 connections, and after it will use  srv2 etc. This algorithm can be useful when you don't want to install a  server when it is not necessary.

Example frontend and backend sections:

```
frontend fe_http_80
        bind *:80
        default_backend    be_http_80
backend be_http_80
        balance  first
        server   srv1 192.168.1.223:80 maxconn 50
        server   srv2 192.168.1.224:80 maxconn 50
        server   srv3 192.168.1.225:80 maxconn 50
```

<br>
</details>

<details markdown='1'>
<summary>
7. URL Redirection
</summary>
---
The requested URL can be redirected depending on URL path, URL  parameters, HTTP headers, or HTTP address. This redirections could be very efficient at some circumstances.

### 7.1. URL Path Redirection
#### 7.1.0. Scenario
We have 3 folders at our webserver, folder1, folder2, and folder3. When  folder1 is requested it will be redirected to srvaw1, folder2 to srvaw2, folder3 to srvaw3. 

Otherwise the standart load balancing will keep going as it is at Section 3.

#### 7.1.1. Configuration  (srvlb1 and srvlb2)
```
sudo nano /etc/haproxy/haproxy.cfg
```

Remove previously added backend and frontend sections for HTTP and add to the end of the file:

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
        server   srvaw1 192.168.1.223:80 check
backend be_folder2
        server   srvaw2 192.168.1.224:80 check
backend be_folder3
        server   srvaw3 192.168.1.225:80 check
backend be_http_80
        balance  roundrobin
        server   srvaw1 192.168.1.223:80 check
        server   srvaw2 192.168.1.224:80 check
        server   srvaw3 192.168.1.225:80 check
```

Restart HAProxyy

```
sudo systemctl restart haproxy
```

You may prefer reloading haproxy, if it is already active

```
sudo systemctl reload haproxy
```
 
#### 7.1.2. Explanations
ACLs (Access Control Lists) are used to check if a URL path starts with  something.

- acl acl_folder1 path_beg -i /folder1

acl is a keyword to define an ACL, acl_folder1 is the given name for that acl, path_beg mean a condition of URL path (part of the URL after the  address) starts with something, -i means following string will be  considered as case insensitive, finally the /folder1 is the string we are  looking for.

ACL acl_folder1 is activated when a url path starts with /folder1 like in:

http://www.www.386387.xyz/folder1

For a URL of http://www.www.386387.xyz/folder1/folder2/folder3, the URL Path is: /folder1/folder2/folder3

- use_backend be_folder1 if acl_folder3

This command instructs HAProxy to use the server(s) in be_folder1 backend when acl_folder1 is activated.

Similar ACLs and Backends are created for /folder2 and /folder3 too.

There are other possible conditions for URL Path. List of them:

```
path    	exact URL path 
path_beg 	URL path begins with the string
path_end 	URL path ends with the string
path_sub 	URL path has the string as a substring
path_dir 	URL path has the string as a subdirectory
path_len 	Exact length of the URL path
path_reg 	Regex match of the URL path
```

#### 7.1.3. URL Path ACL Examples
An acl for info page

```
acl acl_info path -i /info/info.html
```

An acl for jpg and png images

```
acl acl_image path_end .jpg .png
```

An acl for image directories

```
acl acl_image2 path_dir -i /images
```

An acl for URL paths more than 20 chars

```
acl acl_long path_len gt 20
```

An acl for paths including cart

```
acl acl_cart path_sub -i cart
```

Another acl for images

```
acl acl_image3 path_reg (jpg|jpeg|bmp|gif|png)
```

### 7.2. URL Parameter Redirection
A URL parameter is a variable and  value pair. A lot of websites  including duckduckgo and google use it to send a search to the website.  Below is an example:

https://www.x386.org/?s=x386

s is the variable which stands for search and x386 is the value to search  for.

HAProxy can capture the parameter (the  variable and the value) and  redirect a certain pair to a certain website. 

#### 7.2.1. Example
Assume that we have a variable named block_number and it can have values  first, second, third, and rest. A URL for first block number will be like  something below:

http:/www.386387.xyz/?block_number=First

We want to redirect first block to a website, second and third to another website and the rest to another website. A frontend section would be like below:

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

As you might remember -i directive is for case-insensitive string match.  -m directive is used for exact string match.

### 7.3. HTTP Header Redirection
HTTP Headers may contain many information including User-Agent, Host  (website root address), Content-Type, Referer (not referrer). For a full list, please refer:

[wikipedia.org](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

A User-Agent HTTP Header would be something like below:

Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0

A host HTTP Header would be something like below:

Host: www.www.386387.xyz

A frontend section to redirect requests from mobile devices to a specific address would be:

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
This section deals with using https with HAProxy. Using TLS (SSL) certificates are easy with HAProxy. But we want to use LetsEncrypt certificates and certbot tool for frequent (every 2 months) renewals.

I test everything I write here, actually I write here what I do on the servers. To use LetsEncrypt certificates with certbot, the servers must be connected to the internet. So we need VPS servers. Therefore, for this section only, I use 1 HAProxy server and 2 web servers (No keepalived). 

### 8.0. Configurations & Considerations (For this section only)
www.386387.xyz: Load Balancer  --> 209.38.148.92  
srv1.386387.xyz: Web Server 1   --> 146.190.153.22  
srv2.386387.xyz: Web Server 2   --> 64.23.129.138  

Tested with Debian 12/11 and Ubuntu 24.04/22.04 LTS Servers

This section starts with fresh installed servers.

To receive (and then renew) certificates from LetsEncrypt with Certbot; either you should have a web server listening on port 80 on your server, or Certbot spins a temporary web server at port 80 when it is working. 

It is not so easy, because we bind port 80 at HAProxy configuration. 

There are some complicated solutions on the web. I found a solution which is not so painful, also looks safe to implement. 

- We install apache to our Load Balancer, but bind it on loopback adapter  (127.0.0.1). 
- HAProxy is binded to server's other IP addresses. 
- The request of LetsEncrypt's challenge directory is redirected to internal Apache server. That way Apache and HAProxy can survive together, both binding to port 80.


### 8.1. Initial Installs
We need to install HAProxy on www.386387.xyz; install apache on srv1.386387.xyz and srv2.386387.xyz and add test pages.

#### 8.1.1. Install HAProxy on Load Balancer Server (www.386387.xyz)
```
sudo apt update
sudo apt install haproxy --yes
sudo systemctl stop haproxy
```

#### 8.1.2. Install Apache on First Web Server (srv1.386387.xyz)
```
sudo apt update
sudo apt install apache2 --yes
```

Add a test page

```
sudo rm /var/www/html/index.html
sudo nano /var/www/html/index.html
```

Fill as below

```
<html>
<title>SrvAW1</title>
<body>
<h1>Srv1</h1>
<p>Empty yet.</p>
</body>
</html>
```

#### 8.1.3. Install Apache on First Web Server (srv2.386387.xyz)
```
sudo apt update
sudo apt install apache2 --yes
```

Add a test page

```
sudo rm /var/www/html/index.html
sudo nano /var/www/html/index.html
```

Fill as below

```
<html>
<title>SrvAW1</title>
<body>
<h1>Srv2</h1>
<p>Empty yet.</p>
</body>
</html>
```

### 8.2. Install And Configure Apache on Load Balancer (Run on www.386387.xyz)
```
sudo apt update
sudo apt install apache2 --yes
```

Apache may give error messages and cannot start. Don't worry, it is  because HAProxy uses port 80 already.

Configure Apache to bind only on loopback

```
sudo nano /etc/apache2/ports.conf
```

Change as Below

```
Listen 127.0.0.1:80
<IfModule ssl_module>
        Listen 127.0.0.1:443
</IfModule>
<IfModule mod_gnutls.c>
        Listen 127.0.0.1:443
</IfModule>
```

Configure the Default Site Conf to only bind to loopback IP

```
sudo nano /etc/apache2/sites-available/000-default.conf
```

Change as below, remember to change to your domains

```
<VirtualHost 127.0.0.1:80>
        ServerAdmin webmaster@localhost
        ServerName www.386387.xyz
        ServerAlias www.www.386387.xyz
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Create Letsencrypt's challenge directory

```
sudo mkdir -p /var/www/html/.well-known/acme-challenge
```

Restart Apache

```
sudo systemctl restart apache2
```

### 8.3. Configure HAProxy to Redirect to Apache (Run on www.386387.xyz)
Edit HAProxy configuration file

```
sudo nano /etc/haproxy/haproxy.cfg
```

Add to the end of the file, remember to use your servers' IPs at bind  directive. 

You can see them with "ip a" command.

```
frontend fe_http
        bind 209.38.148.92:80
        acl acl_acme path_beg -i /.well-known/acme-challenge
        use_backend be_acme if acl_acme
backend be_acme
        server self 127.0.0.1:80 check
```

Restart HAProxy

```
sudo systemctl restart haproxy
```

### 8.4. Install and Run Certbot (Run on www.386387.xyz)
Install Certbot

```
sudo apt update
sudo apt install --yes  certbot
```

Run Certbot to Produce Certificates, remember to change to your domain(s).

```
sudo certbot certonly --webroot --webroot-path /var/www/html \
   -d www.386387.xyz,386387.xyz
```

### 8.5. Generate Certificate for HAProxy (Run on www.386387.xyz)
Your LetsEncrypt certificates are located at the dir /etc/letsencrypt/live/www.386387.xyz.

Of course yours have your domain name instead of www.386387.xyz. You can see its  name with the following command: 

```
sudo ls -al /etc/letsencrypt/live
```

The directory that you see there, is your domain to replace with www.386387.xyz  at the following commands.

HAProxy certificate is generated by adding public key and private key  together to a file.

Temporarily become root and generate certificate

```
sudo -i
cd /etc/letsencrypt/live/www.386387.xyz
cat fullchain.pem privkey.pem >> haproxy.pem
exit
```

### 8.6. Configure HAProxy (Run on www.386387.xyz)
At 8.3. we made a configuration for redirecting to Apache. This time we  are configuring HAProxy website redirection with SSL.

```
sudo nano /etc/haproxy/haproxy.cfg
```

Change the end of the file as below. 

 
```
frontend fe_http
        bind 209.38.148.92:80
        bind 209.38.148.92:443 ssl crt /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
        acl acl_acme path_beg -i /.well-known/acme-challenge
        use_backend be_acme if acl_acme
        default_backend    be_http
        option   forwardfor
backend be_acme
        server self 127.0.0.1:80 check
backend be_http
        balance  roundrobin
        server   srv1 146.190.153.22:80 check
        server   srv2 64.23.129.138:80 check
```

Restart HAProxy

```
sudo systemctl restart haproxy
```

SSL redirection is running now, but we have some more work to polish it.

### 8.7. Check Certbot for Renewal and Add Renewal-Hooks (Run on www.386387.xyz)
We are going to wait for 60 days to renew our certificates, but we can  simulate it with the following command:

```
sudo certbot renew --dry-run
```

If it works without any errors, most probably it will work forever.

But there is some more things to consider. Everytime the certificates  are renewed, we have to generate certificate for HAProxy and restart HAProxy to use that new certificate. 

It is easier than you think. We will create a script to do that work, and make it run everytime our certificates renewed.

Certbot runs all scripts in /etc/letsencrypt/renewal-hooks/deploy/ folder after it successfully renews a certificate. So we'll add a file there with the necessary operations

```
sudo nano /etc/letsencrypt/renewal-hooks/deploy/haproxy.sh
```

Fill as below, remember to change to your domain

```
cat /etc/letsencrypt/live/www.386387.xyz/fullchain.pem /etc/letsencrypt/live/www.386387.xyz/privkey.pem \
  >> /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
systemctl restart haproxy
```

Make it executable

```
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/haproxy.sh
```

### 8.8. Explanations
Everything is fine until now. We have our SSL (actually TLS)  certificates, they are renewed automatically. We can connect to our site  using https.

Actually only the traffic between our browser and the Load Balancer is  encrypted, the traffic between Load Balancer and the Web Servers are cleartext. This is called TLS Termination. It may not be a problem if your web servers are not connected to the internet. But to be stay safe, we'd better encrypt that traffic too. And this is called TLS re-encryption.

To establish TLS re-encryption, we'll use self signed certificates on our Web Servers, and instruct our Load Balancer to reach them using https. 

### 8.9. Enable HTTPS at Web Servers (Run on srv1.386387.xyz and srv2.386387.xyz)

Enable Apache SSL module

```
sudo a2enmod ssl
```

Restart Apache

```
sudo systemctl restart apache2
```

Create a directory for the certificates

```
sudo mkdir /etc/apache2/certs
```

Create a self signed certificate

```
sudo openssl req -x509 -nodes -days 7300 -newkey rsa:2048 \
-keyout /etc/apache2/certs/www.386387.xyz.key -out /etc/apache2/certs/www.386387.xyz.crt
```

It will ask some questions, answer them with common sense

Create a conf file for ssl site

```
sudo nano /etc/apache2/sites-available/000-virtual-ssl.conf
```

Fill as below:

```
<IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerName www.386387.xyz
        ServerAlias www.www.386387.xyz
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

Enable the new ssl site

```
sudo a2ensite 000-virtual-ssl.conf
```

Reload apache

```
sudo systemctl reload apache2
```

Our web servers are ready for https. Now we need to instruct our Load  Balancer to connect them through https.

### 8.10. Instruct HAProxy to Access Web Servers Through HTTPS (Run on www.386387.xyz)

```
sudo nano /etc/haproxy/haproxy.cfg
```

Change Backend Sections as below

```
backend be_acme
        server self 127.0.0.1:80 check
backend be_http
        balance  roundrobin
        server   srv1 146.190.153.22:443 check ssl verify none
        server   srv2 64.23.129.138:443 check ssl verify none
```

Restart HAProxy

```
sudo systemctl restart haproxy
```

### 8.11. Auto HTTP to HTTPS Redirection
Now when someone types https://www.386387.xyz on the browser, all the traffic  between the client and our web servers are encrypted. But if someone types http://www.386387.xyz, all the traffic goes in plain, old, clear format (unless the browser automatically converts it to https, like Firefox does). We can force HTTP to HTTPS redirection by modifying frontend section.

```
sudo nano /etc/haproxy/haproxy.cfg
```

Add following line after the bind lines of the frontend section:

```
        redirect scheme https if !{ ssl_fc }
```

The modified frontend section will look like below:

```
frontend fe_http
        bind 209.38.148.92:80
        bind 209.38.148.92:443 ssl crt /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
        redirect scheme https if !{ ssl_fc }
        acl acl_acme path_beg -i /.well-known/acme-challenge
        use_backend be_acme if acl_acme
        default_backend    be_http
        option   forwardfor
```

Restart HAProxy

```
sudo systemctl restart haproxy
```

### 8.12. Server Persistance with Cookies
One final touch and we are good to go. We may want the same computers always connect to the same frontend servers. This is especially necessary  when the connection has a session information. Otherwise, the user must login again everytime the server changed. 

Server persistance can be established with cookies easily. At the backend session, a cookie directive is added and all servers are assigned to have a unique cookie.

```
sudo nano /etc/haproxy/haproxy.cfg
```

Change backend sections as below:

```
backend be_acme
        server self 127.0.0.1:80 check
backend be_http
        balance  roundrobin
	cookie ACTIVESERVER insert indirect nocache
        server   srv1 146.190.153.22:443 check ssl verify none cookie srv1
        server   srv2 64.23.129.138:443 check ssl verify none cookie srv2
```

Restart HAProxy

```
sudo systemctl restart haproxy
```

### 8.13. Final Contents of HAProxy Config File

```
cat /etc/haproxy/haproxy.cfg
```

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
        bind 209.38.148.92:80
        bind 209.38.148.92:443 ssl crt /etc/letsencrypt/live/www.386387.xyz/haproxy.pem
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
        server   srv1 146.190.153.22:443 check ssl verify none cookie srv1
        server   srv2 64.23.129.138:443 check ssl verify none cookie srv2
```

</details>

