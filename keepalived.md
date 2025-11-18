##### Keepalived
# Keepalived Clustering on Debian and Ubuntu Servers

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.0. The What

Keepalived is a Linux daemon that provides high availability and load balancing using the Virtual Router Redundancy Protocol (VRRP). It is commonly used to ensure service continuity by automatically failing over to a backup server if the primary server becomes unavailable.

In this tutorial, we'll configure two servers with various Keepalived scenarios to demonstrate different high-availability configurations.


### 0.1. The Environment

- **Server OS:** Debian 13 or Ubuntu 24.04 Server
- **Virtual IP Address (VIP):** `192.168.1.240`


### 0.2. Scenarios

- **Scenario 1 - Simple Mode:** Two servers where the first server holds the VIP. If it fails, the second server takes over the VIP. When the first server recovers, it reclaims the VIP (preemptive mode).

- **Scenario 2 - Nonpreemptive Mode:** Similar to Scenario 1, but when the first server recovers, it does not automatically reclaim the VIP.

- **Scenario 3 - Apache High Availability:** Both servers run Apache. The VIP fails over to the backup server only if Apache becomes unreachable on the primary server, not just if the server itself is down.

- **Scenario 4 - Active/Active VIPs:** Two servers and two VIPs (`192.168.1.240` and `192.168.1.241`). Each server primarily holds one VIP, but can take over the other VIP if the peer server fails.

### 0.3. Sources

- [DeepSeek](https://www.deepseek.com/)
- [ChatGPT](https://chatgpt.com/)
- [Claude](https://claude.ai/)
- [Keepalived Documentation](https://keepalived.readthedocs.io/)




<br>
</details>

<details markdown='1'>
<summary>
1. Scenario 1 - Simple Mode
</summary>

---

### 1.1. Install keepalived

Install on both servers (primary and backup):
```
sudo apt update
sudo apt -y install keepalived
```

**Note:** After installation, the service may attempt to start but will fail until a valid configuration is provided.

### 1.2. First Server Configuration

The configuration directory is `/etc/keepalived/`. Create the main configuration file:

```
sudo nano /etc/keepalived/keepalived.conf
```

Add the following configuration:

```
global_defs {
    router_id main   # Unique identifier for this node in logs
}

vrrp_instance VI_1 {
    state MASTER          # This node starts as the primary
    interface enp0s3      # Network interface name - CHANGE TO YOURS
    virtual_router_id 51  # Must be identical across all nodes in the group
    priority 100          # Election priority (higher = more preferred)
    advert_int 1          # Advertisement interval in seconds

    virtual_ipaddress {
        192.168.1.240/24  # Virtual IP to manage (include netmask)
    }
}
```

### 1.3. Second Server Config

Similar but with a few differences.


```
Create the configuration file on the backup server:
```

Fill as below:

```
global_defs {
    router_id backup    # Unique identifier for this node in logs
}

vrrp_instance VI_1 {
    state BACKUP          # This node starts as backup
    interface enp0s3      # Network interface name - CHANGE TO YOURS
    virtual_router_id 51  # Must match the primary server
    priority 90           # Lower priority than primary
    advert_int 1

    virtual_ipaddress {
        192.168.1.240/24
    }
}
```

### 1.5. Start keepalived

Run on both servers

```
sudo systemctl start keepalived
```

You can check the status of your cluster

```
systemctl status -l keepalived
```

**Testing:** You can test failover by stopping the primary server (`sudo systemctl stop keepalived` or shutting it down) and observing the VIP migration to the backup server.

</details>


<details markdown='1'>
<summary>
2. Scenario 2 - Nonpreemptive Mode
</summary>

---

### 2.0. Overview

Keepalived defaults to preemptive mode, where a higher-priority server that recovers will automatically reclaim the VIP. In nonpreemptive mode, once a backup server takes over the VIP, it will keep it even if the original primary server recovers.

To implement this, we add the `nopreempt` directive and remove the `state` declarations from both configurations.

### 2.1. Update Configurations

On the primary server, edit the configuration:

```
sudo nano /etc/keepalived/keepalived.conf
```

Update with the following content:

```
global_defs {
    router_id main
}

vrrp_instance VI_1 {
    interface enp0s3
    virtual_router_id 51
    priority 100
    advert_int 1
    nopreempt               # Disable automatic failback
    
    virtual_ipaddress {
        192.168.1.240/24 
    }
}
```

On the backup server, edit the configuration:

```
sudo nano /etc/keepalived/keepalived.conf
```

Update with the following content:


```
global_defs {
    router_id backup
}

vrrp_instance VI_1 {
    interface enp0s3
    virtual_router_id 51
    priority 90
    advert_int 1
    nopreempt           # Disable automatic failback
    
    virtual_ipaddress {
        192.168.1.240/24
    }
}
```

### 2.2. Restart Services

Restart Keepalived on both servers to apply the changes:

```
sudo systemctl restart keepalived
```

</details>



<details markdown='1'>
<summary>
3. Scenario 3 - Apache High Availability
</summary>

---

### 3.0. Overview

This scenario provides application-level high availability for Apache web server. The VIP will fail over only if Apache service itself becomes unavailable, not just if the server is unreachable.

We'll create a custom health check script and integrate it with Keepalived.

### 3.1. Create Health Check Script

On both servers, create the check script:

```
sudo nano /etc/keepalived/check_apache.sh
```

Add the following content:

```
#!/bin/bash
# Simple check: is Apache running?
# Works for both Apache2 and httpd-based systems.

if pidof apache2 >/dev/null 2>&1; then
    exit 0
else
    exit 1
fi
```

Make the script executable:

```
sudo chmod +x /etc/keepalived/check_apache.sh
```

### 3.2. Install and Verify Apache

Ensure Apache is installed and running on both servers:

```
sudo apt update
sudo apt install -y apache2
```


### 3.3. Update Keepalived Configuration

On the primary server, update the configuration:

```
sudo nano /etc/keepalived/keepalived.conf
```

Use the following configuration:

```
global_defs {
    router_id main
    script_user root           # User context for script execution
    enable_script_security     # Enable script security features
}

vrrp_script chk_apache {
    script "/etc/keepalived/check_apache.sh"
    interval 2        # Check every 2 seconds
    timeout 2         # Script must complete within 2 seconds
    fall 2            # 2 consecutive failures trigger a fault
    rise 2            # 2 consecutive successes clear a fault
    weight -20        # Deduct 20 from priority if Apache fails
}

vrrp_instance VI_1 {
    interface enp0s3
    virtual_router_id 51
    priority 100
    advert_int 1
    
    virtual_ipaddress {
        192.168.1.240/24
    }

    track_script {
        chk_apache    # Monitor Apache service health
    }
}
```

On the backup server, update the configuration:
```bash
sudo nano /etc/keepalived/keepalived.conf
```

Use the following configuration:
```bash
global_defs {
    router_id backup
    script_user root
    enable_script_security
}

vrrp_script chk_apache {
    script "/etc/keepalived/check_apache.sh"
    interval 2
    timeout 2
    fall 2
    rise 2
    weight -20
}

vrrp_instance VI_1 {
    interface enp0s3
    virtual_router_id 51
    priority 90
    advert_int 1

    virtual_ipaddress {
        192.168.1.240/24
    }

    track_script {
        chk_apache
    }
}
```

### 3.4. Restart Services

Restart Keepalived on both servers:

```
sudo systemctl restart keepalived
```

**Testing:** Stop Apache on the primary server (`sudo systemctl stop apache2`) and observe the VIP failing over to the backup server.

**Note:** For Nginx or other services, modify the check script accordingly (e.g., check for `nginx` instead of `apache2`).

</details>



<details markdown='1'>
<summary>
4. Scenario 4 - Active/Active VIPs
</summary>

---

### 4.0. Overview

This configuration provides active-active load distribution with two VIPs:
- **VIP1:** `192.168.1.240` (primarily on Server 1)
- **VIP2:** `192.168.1.241` (primarily on Server 2)

Both servers remain active simultaneously, but each can take over the other's VIP if a failure occurs.



### 4.1. Update Keepalived Configuration

On the first server, update the configuration:

```
sudo nano /etc/keepalived/keepalived.conf
```

On the first server, change as below:

```
global_defs {
    router_id first
}

vrrp_instance VIP_1 {
    state MASTER
    interface enp0s3
    virtual_router_id 100    # Unique ID for first VIP group
    priority 100
    advert_int 1
    virtual_ipaddress {
        192.168.1.240/24    # Primary VIP for this server
    }
}

vrrp_instance VIP_2 {
    state BACKUP
    interface enp0s3
    virtual_router_id 101    # Unique ID for second VIP group
    priority 90
    advert_int 1
    virtual_ipaddress {
        192.168.1.241/24    # Secondary VIP (backup role)
    }
}
```

On the second server, update the configuration:

```
sudo nano /etc/keepalived/keepalived.conf
```

Use the following configuration:

```
global_defs {
    router_id second
}

vrrp_instance VIP_1 {
    state BACKUP
    interface enp0s3
    virtual_router_id 100
    priority 90
    advert_int 1
    virtual_ipaddress {
        192.168.1.240/24    # Secondary VIP (backup role)
    }
}

vrrp_instance VIP_2 {
    state MASTER
    interface enp0s3
    virtual_router_id 101
    priority 100
    advert_int 1
    virtual_ipaddress {
        192.168.1.241/24    # Primary VIP for this server
    }
}
```

### 4.2. Restart Services

Restart Keepalived on both servers:

```
sudo systemctl restart keepalived
```

### 4.3. Optional: Add Service Health Checks

You can enhance this configuration by adding health check scripts (as shown in Scenario 3) to each `vrrp_instance` block to trigger failover based on application health rather than just server availability.


</details>
