---
title: "Docker"
description: "Docker tutorial for Debian and Ubuntu server"
sidebar: 
   label: Docker tutorial
---

##### Docker Tutorial for Debian and Ubuntu Server


## 0. Specs

### 0.1. The What

Docker is an open-source containerization platform leveraging native Linux kernel features, specifically **namespaces** and **cgroups**.

It facilitates packaging applications—along with their runtime, libraries, and system dependencies—into portable artifacts known as **images**. An image can be instantiated as one or more **containers**, which operate as isolated processes on the host system.

Unlike virtual machines (VMs), containers share the host kernel while maintaining strict process, network, and filesystem isolation. This architecture provides:

- **Minimal Overhead:** Low resource consumption due to the absence of hardware emulation.
- **Rapid Startup:** Near-instantaneous container initialization.
- **Environment Parity:** Absolute consistency between development, staging, and production environments.
- **Predictable Deployment:** Immutable infrastructure through repeatable image-based delivery.

### 0.2. The Environment

All scenarios and commands in this documentation have been validated on:

* **Debian 13 (Trixie)**
* **Ubuntu Server 24.04 LTS**

**Topology:**

* `docker`: Standalone Docker host.
* `node1` – `node5`: Docker Swarm cluster nodes.

This guide focuses on **production-grade** server management via CLI, rather than desktop-oriented development workflows.

### 0.3. Sources

- [Docker Official Documentation](https://docs.docker.com/)
- [Gemini](https://gemini.google.com/app)
- [Deepseek](https://www.deepseek.com/)
- [ChatGPT](https://chatgpt.com/) 
- [Claude](https://claude.ai/)
- Book: **Docker Quick Start Guide** by Earl Waud, ISBN: 9781789347326
- Book: **Getting Started with Docker** by Nigel Poulton, ISBN: 9781916585300
- Book: **Docker Deep Dive** by Nigel Poulton, ISBN: 9781916585133
- Book: **Learn Docker in a Month of Lunches 2nd Ed.** by Elton Stoneman, ISBN: 9781633438460
- Book: **Docker Up & Running** by Sean P. Kane with Karl Matthias, ISBN: 978-1-098-13182-1
- Book: **Painless Docker** by Aymen El Amri, ISBN: 9798870316826
- Book: **The Docker Workshop** by Vincent Sesto, Onur Yılmaz, Sathsara Sarathchandra, Aric Renzo, and Engy Fouda, ISBN: 9781838983444
- Book: **The Ultimate Docker Container Book** by Dr. Gabriel N. Schenker, ISBN: 978-1-80461-398-6

---

## 1. Installation

### 1.1. Installation Types

Docker can be installed using:

- Distribution packages (Debian/Ubuntu repositories)
- Docker’s official upstream repositories

**Distribution packages**

- Integrated with the OS lifecycle
- Conservative version updates
- Suitable for long-term stability-focused environments

**Docker upstream packages**

- Faster release cadence
- Access to latest features (BuildKit, Compose plugin updates, etc.)
- Preferred when feature parity with upstream documentation is required

### 1.2. Architectural Components

Docker is composed of multiple layers:

- **Docker CLI (`docker`):**   Command-line client. Sends REST API requests to the Docker daemon.
- **Docker Daemon (`dockerd`):** Background service managing images, containers, networks, volumes, and build operations.
- **containerd:** High-level container runtime responsible for container lifecycle management.
- **runc:** Low-level OCI runtime that interacts directly with Linux kernel features (namespaces, cgroups).
- **Docker Compose (v2 plugin):** Declarative multi-container orchestration via YAML.

**Execution Flow:**
`Docker CLI` → `dockerd` → `containerd` → `runc` → `Linux Kernel`

### 1.3. Debian 13 Installing from Debian Packages

```bash
sudo apt update
sudo apt install docker.io docker-compose
```

### 1.4. Ubuntu 24.04 Installing from Ubuntu Packages

```bash
sudo apt update
sudo apt install docker.io docker-compose-v2
```


### 1.5. Debian 13 Installing From Docker Repos

Remove any previously installed docker packages:

```bash
sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-doc podman-docker containerd runc | cut -f1)
```

Set up Docker's apt repository.

```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```

Install Docker packages:

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 1.6. Ubuntu 24.04 Installing from Docker Repos

Remove any previously installed docker packages:

```bash
sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc podman-docker containerd runc | cut -f1)
```

Set up Docker's apt repository.

```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```

Install Docker packages:

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 1.7. Post-Installation Steps 

**User Permissions:** Add the current user to the `docker` group to enable execution without `sudo` (requires logout/login to take effect).

```bash
sudo usermod -aG docker $USER

```

⚠ **Security Note:** Membership in the `docker` group effectively grants root-level privileges on the host system. This should be treated accordingly in production environments.


Verification:

```
docker version
docker info
docker compose version
docker container run hello-world
```

---

## 2. Docker Images

### 2.1. Overview

A **Docker Image** is a read-only, immutable template used to instantiate containers. Conceptually similar to a "Class" in Object-Oriented Programming, it encapsulates the root filesystem, application code, binaries, libraries, and environment variables required for execution.

Images are hosted in **Container Registries**. Common registries include:

* **Public:** [Docker Hub](https://hub.docker.com/), [GitHub Container Registry (GHCR)](https://github.com/features/packages), [Quay.io](https://quay.io/)
* **Cloud-Specific:** Amazon ECR, Azure ACR, Google Artifact Registry
* **Self-Hosted:** [Harbor](https://goharbor.io/)

**Image Naming Convention:**
An image is identified by a four-part fully qualified name (defaults in parentheses):
`[Registry (docker.io)] / [Owner (library)] / [Image Name] : [Tag (latest)]`

**Examples:**
All the following commands pull the same `nginx` image from Docker Hub:

```
docker image pull docker.io/library/nginx:latest
docker image pull library/nginx:latest
docker image pull nginx:latest
docker image pull nginx
```

List the downloaded images:

```
docker image ls
```

Example output:

```
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
nginx        latest    058f4935d1cb   8 days ago   152MB
```

Remove an image by Name or ID (partial ID is sufficient):

```
docker image rm nginx
docker image rm 058f
```

### 2.2. Image Layers

A Docker image consists of multiple **layers**, which are immutable filesystem differences (diffs). When a container is started, Docker utilizes a **Storage Driver** (typically `overlay2`) to stack these layers into a single unified root filesystem.

Key characteristics:

* **Immutability:** Existing layers cannot be changed.
* **Efficiency:** Layers are cached and shared across multiple images to save disk space and reduce download times.
* **Copy-on-Write (CoW):** Only changes made during the container's runtime are written to a temporary "container layer" on top.

### 2.3. Creating a Docker Image - Dockerfile

To create a Docker image, we need an empty folder and create a Dockerfile containing the image definition there.

An image is defined using a `Dockerfile`, a plain-text manifest containing ordered instructions.

**Example Build Workflow:**

```bash
mkdir ~/testimage && cd ~/testimage
nano Dockerfile
```

**Dockerfile Content:**

```dockerfile
# Step 1: Define Base Image
FROM debian:trixie

# Step 2: Install dependencies (Grouped to minimize layer count)
RUN apt-get update && apt-get install -y \
    fortune-mod \
    && rm -rf /var/lib/apt/lists/*

# Step 3: Set environment variables
ENV USER_NAME="Dear User"

# Step 4: Define default execution command
CMD ["/usr/games/fortune"]
```

**Building and Publishing:**

```bash
# Build with a local tag
docker image build -t welcome:1.0.0 .

# Build for a specific registry (e.g., Docker Hub user 'exforge')
docker image build -t exforge/welcome:1.0.0 .

# Authentication and Push
docker login
docker image push exforge/welcome:1.0.0
```

Some common keywords of Dockerfile syntax:

- **FROM**: Sets the starting point. Every Dockerfile must start with this.
- **RUN**:  Executes a command during the build. This creates a new permanent layer.
- **ENV**:  Sets environment variables that the container can use while running.
- **COPY**: Moves files from the computer into the image.
- **CMD**:  The default behavior when running the container. (Think of it like an entry in /etc/init.d/ or a systemd ExecStart).


### 2.4. Image Optimization & Multi-Stage Builds

Production-grade images must be **minimal** to reduce the attack surface and deployment latency.

**Optimization Strategies:**

* **Layer Minimization:** Chain commands (e.g., `apt update && apt install`) to reduce the number of layers.
* **Cleanup:** Remove package manager caches (`/var/lib/apt/lists/*`) in the same `RUN` instruction where they were created.
* **Multi-Stage Builds:** The most effective method for compiled languages. Use a "heavy" image for building and a "light" image for the final runtime.

**Multi-Stage Example (Go):**


Create a directory and a simple Go web server:

```bash
mkdir ~/gocontainer && cd ~/gocontainer
nano main.go
```

**main.go content:**

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "This Go program runs in a optimized container!")
    })

    fmt.Println("Server starting on port 8080...")
    http.ListenAndServe(":8080", nil)
}
```

Create the **Multi-Stage Dockerfile**:

```
nano Dockerfile
```

Fill as below:

```dockerfile
# --- STAGE 1: Build ---
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY main.go .
RUN go mod init go-app && \
    CGO_ENABLED=0 GOOS=linux go build -o go-binary .

# --- STAGE 2: Runtime ---
FROM alpine:latest
WORKDIR /root/
# Copy ONLY the artifact from the builder stage
COPY --from=builder /app/go-binary .
EXPOSE 8080
CMD ["./go-binary"]
```

Build the image:

```
docker image build -t go-app .
```

### 2.5. "docker image" Commands 

Some important `docker image` commands:

- **docker image ls:** Lists all locally stored images
- **docker image pull:** Downloads an image from a registry (e.g., Docker Hub).	
- **docker image build:** Creates an image from a Dockerfile.	
- **docker image inspect:** Displays low-level information of an image (JSON).	
- **docker image history:** Shows the history/layers of an image.
- **docker image tag:** Creates a new tag (alias) for an image.
- **docker image rm:** Removes one or more images from the host.
- **docker image prune:** Removes all unused (dangling) images.
- **docker image save:** Saves an image to a .tar archive.
- **docker image load:** Loads an image from a .tar archive.

---

## 3. Docker Containers

### 3.1. Overview

A **container** is a functional instance of a Docker image. While images are static and read-only, containers are dynamic, stateful (unless ephemeral), and executable.

Docker leverages Linux **Namespaces** to provide isolation for:

* **PID:** Process isolation (the container has its own `init` process).
* **NET:** Dedicated network stack (interfaces, routing tables, firewall rules).
* **MNT:** Isolated mount points and filesystem.
* **UTS:** Independent hostname and domain name.
* **IPC:** Inter-process communication isolation.

We can compare a container and a Virtual Machine in the following table :

| Feature | Virtual Machine | Container (Docker) |
| --- | --- | --- |
| **Kernel** | Separate Kernel per VM | Shared Host Kernel |
| **Isolation** | Hardware-level (Hypervisor) | Process-level (Namespaces) |
| **Speed** | Slow (Boots OS) | Instant (Starts Process) |
| **Size** | Large (GBs) | Small (MBs) |
| **Performance** | Near-native (with overhead) | Native execution speed |

### 3.2. Running Containers

To instantiate a container from the `welcome` image:

```bash
docker container run exforge/welcome:1.0.0
```

The container executes the defined `CMD`, outputs the result to `stdout`, and immediately transitions to an **Exited** state.

**Monitoring and Cleanup:**

```bash
# List only active (running) containers
docker container ls

# List all containers (including Exited/Stopped)
docker container ls -a

# Remove a specific container using Name or partial ID
docker container rm <ID_or_Name>

# Run and automatically remove the container upon exit (Ephemeral)
docker container run --rm exforge/welcome:1.0.0
```

### 3.3. Running Background Services (Detached Mode)

For long-running services like web servers, we use **Detached Mode** (`-d`).

**Practical Example: Apache on Alpine**

```bash
mkdir ~/simpleapache && cd ~/simpleapache
nano Dockerfile
```

**Dockerfile:**

```dockerfile
FROM alpine:latest

# Install Apache and initialize the runtime directory
RUN apk update && \
    apk add --no-cache apache2 && \
    mkdir -p /run/apache2

# Inject a static index page
RUN echo "<html><body><h1>Production Node</h1><p>Status: Online</p></body></html>" > /var/www/localhost/htdocs/index.html

# Documentation for the listener port
EXPOSE 80

# Execute Apache in the foreground to keep the container alive
CMD ["httpd", "-D", "FOREGROUND"]
```

**Deployment:**

```bash
# 1. Build the image
docker image build -t exforge/simpleapache .

# 2. Deploy multiple instances with Port Mapping (-p host_port:container_port)
docker container run -d --name web01 -p 8080:80 exforge/simpleapache
docker container run -d --name web02 -p 8088:80 exforge/simpleapache
```

**Resource Monitoring:**

```bash
# Real-time CPU, Memory, and I/O usage
docker container stats
```

Accessing containers:

```
http://docker:8080/
http://docker:8088/
```

**Removing Containers**

```bash
# Stop
docker container stop web01 web02
# And remove
docker container rm web01 web02
```

### 3.4. Advanced Runtime Configurations

System administrators can enforce constraints and modify container behavior using the following flags:

**Resource Constraints (Capping)**

- `--memory="512m"`: Limits the RAM usage; prevents a single container from exhausting host memory.
- `--cpus="1"`: Restricts the container to a specific number of CPU shares.
- `--restart`: Defines the recovery policy (`no`, `on-failure`, `always`, `unless-stopped`).

**Network & Identity**

- `-h` / `--hostname`: Sets the internal hostname (essential for cluster identification).
- `--network`: Attaches the container to a specific Docker network (e.g., `bridge`, `host`, `none`).
- `--add-host`: Injects custom entries into `/etc/hosts` for local DNS resolution.

**Security Hardening**

- `--read-only`: Mounts the container's root filesystem as read-only. Mandatory for high-security environments.
- `--user`: Runs the process as a non-root UID/GID to mitigate privilege escalation risks.
- `--privileged`: **(Use with Caution)** Grants the container direct access to host hardware and kernel capabilities.

### 3.5. "docker container" Commands

Some important ```docker container``` commands:

- **docker container run**: Create + Start.
- **docker container create**: Create only.
- **docker container start**: Start a stopped container. Use `-a` to attach to the output.
- **docker container stop**: Graceful stop.
- **docker container kill**: Forced stop.
- **docker container restart**: Stop + Start. Restarts the process inside.
- **docker container ls**: List running, like `ps`
- **docker container ls -a**: List all (even dead), like `ps -aux`
- **docker container logs -f**: Follow logs, like `tail -f /var/log/...`
- **docker container top**: Show processes, like `top` or `htop`
- **docker container stats**: Resource usage, like `vmstat` or `iostat`
- **docker container inspect**: Detailed config, like reading a `.conf` file.
- **docker container exec -it <name> bash**: Opens a shell *inside* an already running container.
- **docker container cp <local_path> <container_name>:<path>**: Just like `scp` but between the host and the container. 
- **docker container rm <name>**: Removes a stopped container.
* **docker container rm -f <name>**: Forces the removal of a running container (Stops then Removes).
* **docker container prune**: Deletes *every* stopped container on the system.

---

## 4. Docker Volumes

### 4.1. Overview

By design, containers are **ephemeral**. Any data written to the container's writable layer is lost when the container is deleted. To decouple data from the container lifecycle, Docker provides two primary mechanisms:

| Feature | **Bind Mounts** | **Named Volumes** |
| --- | --- | --- |
| **Host Location** | Any user-defined path (e.g., `/opt/app/conf`) | Managed by Docker (`/var/lib/docker/volumes/`) |
| **Management** | Managed by the OS/Sysadmin | Managed via Docker CLI/API |
| **"Copy-up"** | No (Host content overwrites container path) | Yes (Image content populates empty volumes) |
| **Use Case** | Configuration files and source code sharing | Database storage and production data |
| **Isolation** | Low (Container can modify sensitive host files) | High (Data is isolated from host users) |

### 4.2. Bind Mounts: Direct Host Mapping

Bind mounts are ideal to provide specific host files—such as configuration or static assets—to a container.

**Practical Exercise:**

Create a local directory and a custom index file:

```bash
mkdir ~/html
echo "<html><body><h1>Status: Bind Mount Active</h1></body></html>" > ~/html/index.html

```

Deploy the container using the `-v` (or `--mount`) flag:

```bash
docker container run -d -p 8080:80 \
   --name bind-test \
   -v $HOME/html:/var/www/localhost/htdocs \
   exforge/simpleapache
```

*Note: In bind mounts, the host path must be an absolute path (using `$HOME` or `/home/user`).*

If we point our browser to: ```http:/docker:8080/``` we'll see our new Bind Mount welcome page.

Remove the container after testing it:

```
docker container stop bind-test
docker container rm bind-test
```

Or combined:

```
docker container rm -f bind-test
```


### 4.3. Named Volumes: Docker-Managed Storage

Named volumes are the preferred method for persistent data in production. Docker handles storage driver optimizations and filesystem permissions automatically.

**The "Copy-up" Feature:** Unlike bind mounts, when mounting an **empty** named volume to a container path that already contains data (from the image), Docker copies that data *into* the volume first.


**Workflow:**

1. Create the volume:

```bash
docker volume create lv-web-data

```

2. Instantiate the container:

```bash
docker container run -d -p 8081:80 \
   --name volume-test \
   -v lv-web-data:/var/www/localhost/htdocs \
   exforge/simpleapache
```

If we point our browser to: ```http:/docker:8081/``` we'll see the original welcome page.


**Inspection & Maintenance:**
The actual data resides in the Docker root directory (typically `/var/lib/docker/volumes/`). We can inspect the metadata using:

```bash
docker volume inspect lv-web-data
```

**Output (JSON):**

```json
{
    "CreatedAt": "2026-03-04T01:00:00Z",
    "Driver": "local",
    "Mountpoint": "/var/lib/docker/volumes/lv-web-data/_data",
    "Scope": "local"
}

```

Remove the container and the volume after testing it:

```
docker container rm -f volume-test
docker volume rm lv-web-data
```

Some volume management commands:

- `docker volume ls`: Lists all volumes managed by the local daemon.
- `docker volume inspect <name>`: Displays detailed path and driver information.
- `docker volume rm <name>`: Deletes a volume (fails if attached to a container).
- `docker volume prune`: **Cleanup:** Removes all volumes not currently used by any container.



### 4.4. Case Study 1: Persistent Database Management

This scenario demonstrates decoupling data from the MariaDB engine. We will verify that data survives a container's destruction and recreation.

**Provision the Volume:**

```bash
docker volume create mariadb_data
```

**Deploy the Primary Instance:**
Attach the volume to MariaDB's internal data directory (`/var/lib/mysql`) and set the root password via Environment Variables.

```bash
docker container run -d \
  --name db-master \
  -e MARIADB_ROOT_PASSWORD=SysAdminPass123 \
  -v mariadb_data:/var/lib/mysql \
  mariadb:latest
```

**Data Injection (SQL Operations):**
Access the MariaDB shell inside the running container:

```bash
docker exec -it db-master mariadb -u root -pSysAdminPass123
```

Execute the following SQL commands:

```sql
CREATE DATABASE prod_db;
USE prod_db;
CREATE TABLE assets (id INT AUTO_INCREMENT PRIMARY KEY, hostname VARCHAR(50));
INSERT INTO assets (hostname) VALUES ('srv-web-01'), ('srv-db-01'), ('srv-proxy-01');
SELECT * FROM assets;
EXIT;
```

**Destruction and Recovery:**
Stop and remove the container, then instantiate a new one using the **same volume**.

```bash
docker container rm -f db-master

docker container run -d \
  --name db-recovery \
  -e MARIADB_ROOT_PASSWORD=SysAdminPass123 \
  -v mariadb_data:/var/lib/mysql \
  mariadb:latest
```

**Verification and Backup:**
Verify data persistence and perform a logical backup to the host filesystem:

```bash
# Direct query from host
docker exec -it db-recovery mariadb -u root -pSysAdminPass123 -e "SELECT * FROM prod_db.assets;"

# Perform mysqldump to host
mkdir -p ~/backups
docker exec db-recovery \
  /usr/bin/mariadb-dump -u root -pSysAdminPass123 prod_db \
  > ~/backups/prod_db_$(date +%F).sql
```

After testing, delete the container and the volume:


```bash
docker container rm -f db-recovery
docker volume rm mariadb_data
```

### 4.5. Case Study 2: Shared Storage for Log Aggregation

In this scenario, we use a shared volume to allow a secondary container to monitor logs from a web server. We apply the **Read-Only (:ro)** flag for the watcher container to ensure data integrity.

**Create the Shared Volume:**

```bash
docker volume create shared_logs

```

**Deploy the Producer (Web Server):**

```bash
docker container run -d \
  --name web-server \
  -p 8085:80 \
  -v shared_logs:/var/log/apache2 \
  exforge/simpleapache
```

**Deploy the Consumer (Log Watcher):**
The watcher mounts the same volume as **Read-Only** to prevent accidental log modification.

```bash
docker container run -d \
  --name log-watcher \
  -v shared_logs:/mnt/logs:ro \
  alpine tail -f /mnt/logs/access.log
```

**Testing the Pipeline:**
Monitor the logs of the `log-watcher` while generating traffic:

```bash
# In Terminal 1
docker logs -f log-watcher

# In Terminal 2 (Generate traffic)
curl http://localhost:8085
```

**Cleanup:**

```bash
docker container rm -f web-server log-watcher
docker volume rm shared_logs
```

### 4.6. "docker volume" Commands

Some important ```docker volume``` commands:

- **docker volume create:** Manual volume provisioning. Useful for setting up NFS or cloud storage.
- **docker volume ls:** Lists all volumes. Filtering helps find "orphan" volumes taking up space. |
- **docker volume inspect:**Returns JSON metadata. Essential for finding the **Mountpoint** path.
- **docker volume rm:** Hard deletion of a volume. Only works if no container (even stopped) is using it.
- **docker volume prune:** Bulk cleanup. Deletes every volume not currently attached to a container.
- **`docker volume rm $(docker volume ls -q)`:** *(Bash trick)* Force-delete all volumes (except those in use). A quick "reset" for admins.

---

## 5. Docker Networking

### 5.1. Standards: CNM vs. CNI

Networking in the container ecosystem is governed by two competing specifications:

- **CNM (Container Network Model):** The native Docker standard, implemented via `libnetwork`. It focuses on a modular design using **Sandboxes** (isolated stacks), **Endpoints** (interfaces), and **Networks** (virtual switches). It is deeply integrated into the Docker Engine and supports features like Docker Swarm's routing mesh.

- **CNI (Container Network Interface):** A simpler, vendor-neutral specification used by **Kubernetes**, OpenShift, and Podman. CNI focuses solely on the connectivity of the container at creation. It relies on external plugins (e.g., Calico, Flannel, Cilium) to manage the network lifecycle.


### 5.2. Native Docker Network Drivers

Upon installation, Docker initializes three default networks. We can verify these with:
`docker network ls`

#### 5.2.1. Bridge (The Default)

- **Implementation:** Acts as a software-defined virtual switch (typically interface `docker0` on the host).
- **Connectivity:** Each container is assigned a private IP (e.g., `172.17.0.x/16`). Communication with the external world is handled via **Source NAT (SNAT)**, while inbound traffic requires **Port Mapping** (`-p`).
- **Use Case:** Standard standalone applications requiring isolation with managed access.
- **Note:** All containers utilize this driver unless the `--network` flag is specified.


#### 5.2.2. Host

* **Implementation:** Removes the network stack isolation. The container shares the host's IP address, routing table, and ports directly.
* **Performance:** Offers the highest throughput and lowest latency as it bypasses the Docker NAT and bridge overhead.
* **Constraints:** Port mapping (`-p`) is ignored. Only one process can bind to a specific port on the host at a time.
* **Use Case:** Network-intensive applications (e.g., VoIP, high-load load balancers, or monitoring agents like Prometheus Exporters).

**Practical Example:**
Deploying Apache on the host network makes it instantly reachable on the host's port 80:

```bash
docker container run -d --name web-host --network host exforge/simpleapache
```

*Caution: Starting a second instance with `--network host` will result in a "Port already in use" error.*

**Cleanup:**

```bash
docker container rm -f web-host
```

#### 5.2.3. None

* **Implementation:** The container is provided with a loopback interface (`lo`) only. No external network interfaces are provisioned.
* **Security:** Provides the highest level of network air-gapping.
* **Use Case:** Sensitive batch processing, cryptographic operations, or any local filesystem-only task where network exfiltration must be physically impossible.

**Verification:**

```bash
docker run --rm --network none alpine ip addr
```


### 5.3. User-Defined Bridge Networks

In production environments, using the default `bridge` is considered a legacy practice. For professional deployments, **User-Defined Bridge Networks** are mandatory due to the following architectural advantages:

* **Automatic Service Discovery (Built-in DNS):** Unlike the default bridge where containers must communicate via static IP addresses, user-defined networks provide a resident DNS server. Containers can resolve and reach each other using their **names** as hostnames.
* **Granular Network Isolation:** We can create dedicated segments (e.g., `web-dmz`, `app-internal`, `db-secure`) to ensure that only authorized containers can communicate with sensitive services (like databases).
* **Hot-Plugging:** Network interfaces can be attached to or detached from running containers dynamically, without requiring a container restart.



#### Practical Exercise 1: Service Discovery Verification

This exercise demonstrates how Docker handles internal name resolution.

**Provision a Custom Network:**

```bash
docker network create net-internal
```

**Deploy Interconnected Nodes:**

```bash
docker container run -d --name srv-alpha --network net-internal alpine sleep 3600
docker container run -d --name srv-beta --network net-internal alpine sleep 3600
```

**Validate DNS Resolution:**

```bash
# Testing connectivity from alpha to beta using its name
docker container exec -it srv-alpha ping -c 3 srv-beta
```

**Clean Up:**

```bash
# Remove the containers
docker container rm -f srv-alpha srv-beta

# Remove the internal network
docker network rm net-internal
```


#### Practical Exercise 2: Multi-Homed Containers & Segregation

In this scenario, we architect a two-tier application where the web server acts as a gateway (bridge) between a public-facing network and a secure backend.

**Network Infrastructure:**

```bash
docker network create frontend-net
docker network create backend-net
```

**Secure Database Tier (Backend Only):**

```bash
docker container run -d --name srv-db \
  --network backend-net \
  -e MARIADB_ROOT_PASSWORD=topsecret \
  mariadb:latest
```

**Application Tier (Dual-Homed):**

We start the web server in `frontend-net`, then manually bridge it into `backend-net`.

```bash
docker container run -d --name srv-web --network frontend-net exforge/simpleapache

# Hot-plugging the second interface
docker network connect backend-net srv-web
```

**Network Audit & Security Validation:**

Verify that the `srv-web` has two interfaces and can reach the database, while a container only on `frontend-net` (e.g., a "hacker" or "unauthorized node") is blocked.

```bash
# Check connectivity from web server to DB
docker container exec -it srv-web ping -c 2 srv-db

# Audit network configurations
docker network inspect frontend-net
docker network inspect backend-net

```

**Cleanup:**

```bash
docker container rm -f srv-db srv-web
docker network rm frontend-net backend-net
```


### 5.4. Enterprise Network Drivers: Macvlan & Overlay

For complex infrastructure requirements, Docker provides advanced drivers that extend connectivity beyond a single host or integrate with existing physical network topologies.

#### 5.4.1. Macvlan: Containers as Physical Network Nodes

The **Macvlan** driver allows assigning a unique MAC address to each container, making it appear as a distinct physical device on the network.

* **How it works:** Instead of using the host's IP and port mapping (NAT), the container binds directly to the host's physical interface (e.g., `eth0`).
* **Key Benefits:**
* **Legacy Support:** Ideal for applications that expect to be on a direct physical network rather than behind a NAT.
* **External Visibility:** Network monitoring tools, firewalls, and IDSs can track and filter container traffic based on their individual MAC/IP addresses.
* **VLAN Integration:** Can be configured to work with existing 802.1Q VLAN trunking.


#### 5.4.2. Overlay: Multi-Host Mesh Networking

The **Overlay** driver is the backbone of distributed systems. It creates a virtual logical network that spans across multiple Docker hosts.

* **How it works:** It uses VXLAN encapsulation to "tunnel" traffic between containers residing on different physical servers.
* **Key Requirement:** Requires **Docker Swarm** mode (or an external Key-Value store) to manage the control plane and IP routing between nodes.
* **Use Case:** Microservices architecture where `container-A` on `Host-1` must communicate with `container-B` on `Host-2` securely and transparently.


### 5.5. "docker network" Commands

Some important ```docker network``` commands:

- **`docker network create [NAME]`** Creates a new virtual switch (network).
- **`docker network connect [NET] [CON]`** Connects an existing container to a network.
- **`docker network disconnect [NET] [CON]`** Safely removes a container from a network. 
- **`docker network inspect [NAME]`** Shows which containers are currently on this network and their IPs. 
- **`docker network rm [NAME]`** Deletes the network (only if no containers are using it).
- **`docker network prune`** Deletes all unused networks (not used by any containers).

---

## 6. Docker Compose

### 6.1. Overview

Docker Compose is an orchestration tool used to define and manage multi-container applications. Instead of executing lengthy, error-prone CLI commands for each resource, we define our infrastructure in a declarative **YAML** file (`docker-compose.yml`).

A standard Compose file is organized into three primary top-level sections:

- **Services:** Defines the containers (e.g., `web`, `db`, `cache`). This includes the image/build context, port mapping, and environment variables.
- **Networks:** Defines the virtual switches. Compose automatically creates a default network for the project, but custom networks allow for strict traffic isolation.
- **Volumes:** Defines persistent storage. Compose manages the lifecycle of these volumes, ensuring data survives service restarts.

**Key Benefits for Admins:**

- **Reproducibility:** The exact same environment can be stood up on any host with a single command.
- **Documentation:** The YAML file serves as living documentation of the application's infrastructure.
- **Project Isolation:** Compose uses "project names" (usually the folder name) to keep different environments on the same host from colliding.


### 6.2. Practical Exercise: Multi-Tier Go Application

In this scenario, we deploy a compiled Go web application and a MariaDB database with proper network segregation and scaling.

**Workspace Setup:**

```bash
mkdir ~/compose-project && cd ~/compose-project
```

Create the main.go program for the web app:

```bash
nano main.go
```

Contents:

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "This Go program runs in a optimized container!")
    })

    fmt.Println("Server starting on port 8080...")
    http.ListenAndServe(":8080", nil)
}
```

Create the Multi-Stage Dockerfile for the web app:

```
nano Dockerfile
```

Contents:

```
# --- STAGE 1: Build (Compile) ---
# Use a heavy image containing the Go SDK
FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY main.go .

# Initialize module and compile a static binary
RUN go mod init go-app && \
    CGO_ENABLED=0 GOOS=linux go build -o go-binary .

# --- STAGE 2: Final (Run) ---
# Use a tiny Alpine image for production
FROM alpine:latest

WORKDIR /root/

# Copy ONLY the compiled binary from the builder stage
COPY --from=builder /app/go-binary .

# Document the port the app listens on
EXPOSE 8080

CMD ["./go-binary"]
```

**Defining the Infrastructure (`docker-compose.yml`):**

```
nano docker-compose.yml
```


```yaml
services:
  webapp:
    build: .
    # Map a range of host ports to the container's 8080
    ports:
      - "8080-8090:8080"
    networks:
      - frontend-net
      - backend-net
    depends_on:
      - database

  database:
    image: mariadb:latest
    environment:
      MARIADB_ROOT_PASSWORD: "AdminPassword123"
    volumes:
      - db-data:/var/lib/mysql
    networks:
      - backend-net

networks:
  frontend-net:
  backend-net:

volumes:
  db-data:
```

**Operational Commands:**

* **Deployment:** Compose builds the image, creates networks/volumes, and respects the `depends_on` order.

```bash
docker compose up -d
```


* **Horizontal Scaling:** Increase the number of web server instances.
```bash
docker compose up -d --scale webapp=3
```

* **Monitoring:**
```bash
docker compose ls     # List active compose projects
docker compose ps     # Status of containers in the current project
docker compose top    # Display processes running within services
```


* **Decommissioning:**
```bash
# Stop and remove containers/networks (Preserves Volumes)
docker compose down

# Full Cleanup (Deletes Volumes as well)
docker compose down -v
```

### 6.3. "docker compose" Commands

Some important ```docker compose``` commands:

- **docker compose up -d:** Builds, (re)creates, starts, and detaches to containers for a service in the background.
- **docker compose down:** Stops and removes containers, networks, images, and volumes defined in the file.
- **docker compose ps:** Lists the status of containers in the current project.
- **docker compose logs -f**: Follows the log output from the services.
- **docker compose pause:** Pause services
- **docker compose scale:** Scale services 
- **docker compose top:** Display the running processes
- **docker compose unpause:** Unpause services

---

## 7. Advanced Management & Housekeeping

### 7.1. Overview

While most daily operations involve containers and images, high-level management requires interacting with the Docker Engine's global state and external endpoints. This is handled through three primary command groups:

* **`docker context`**: Manage connectivity to multiple Docker nodes (Local, Remote, or Cloud).
* **`docker system`**: Monitor resource consumption and perform global cleanup.
* **`docker trust`**: Enforce content trust through digital signatures (Image Provenance).


### 7.2. Multi-Node Management: `docker context`

`docker context` allows a sysadmin to switch the target of the Docker CLI seamlessly. Instead of setting environment variables like `DOCKER_HOST`, we define persistent named contexts.

**Practical Use Case: Remote Management via SSH**
To manage a production server from local workstation without exposing a TCP socket:

**Define a new context:**

```bash
docker context create prod-srv-01 \
  --description "Production Node 01" \
  --docker "host=ssh://adminuser@192.168.1.50"
```


**Switch the active target:**

```bash
docker context use prod-srv-01
```


*Now, any command like `docker ps` or `docker stats` runs directly on the production server.*

**Return to local daemon:**
```bash
docker context use default
```

**Quick Reference:**

```
docker context ls                  # list all contexts
docker context show                # show current active context
docker context create <name> ...   # create a new context
docker context rm <name>           # delete a context
```

### 7.3. Engine Housekeeping: `docker system`

This group is essential for maintaining host health and monitoring the daemon's internal state.

- **docker system df**: Displays a disk usage summary. Essential for identifying if images, containers, or local volumes are exhausting host storage.
- **docker system info**: Provides a comprehensive report on the daemon (Kernel version, Storage Driver, Cgroup version, and Security Options).
* **docker system events**: Real-time logging of daemon activity (e.g., container start/die, image pull, volume mount).

**The "Prune" Logic (Garbage Collection):**
System administrators should use `prune` regularly to reclaim space.

```bash
# Standard: Removes stopped containers, unused networks, and dangling images.
docker system prune

# Aggressive: Removes ALL unused images (not just dangling ones).
docker system prune -a

# Nuclear: Includes unused volumes. Use with extreme caution in production!
docker system prune -a --volumes
```


### 7.4. Security & Supply Chain: `docker trust`

`docker trust` implements **Docker Content Trust (DCT)**. It ensures that the images the infrastructure pulls are signed by authorized parties and have not been altered in transit.

* **Verification:** `docker trust inspect <image>` checks if the image has a valid signature.
* **Signing:** `docker trust sign <image>` pushes a signed version of the image to a registry.
* **Enforcement:** In high-security environments, setting `export DOCKER_CONTENT_TRUST=1` in the shell will cause the Docker CLI to **refuse** to pull or run any unsigned images.

**Quick Reference:**

```
docker trust inspect <image>        # show signing info for an image
docker trust sign <image>           # sign an image
docker trust revoke <image>         # revoke a signature
docker trust key generate <name>    # generate a signing key pair
docker trust key load <pem>         # load an existing key
docker trust signer add <name>      # add a signer to a repo
docker trust signer remove <name>   # remove a signer
```

---

## 8. Docker Swarm Orchestration

### 8.1. Architectural Overview

**Docker Swarm** is the native clustering and container orchestration solution for the Docker platform. It enables the management of a group of Docker hosts as a single, resilient, virtual entity.

**Core Concepts:**

- **Nodes:** Any Docker-enabled host participating in the cluster.
    - **Manager Nodes:** Handle cluster state management, task scheduling, and servicing HTTP API endpoints.
    - **Worker Nodes:** Execute containers (tasks) dispatched by the managers. In small clusters, managers often act as workers as well.


- **Services & Tasks:** A **Service** is the declarative definition of the state (e.g., "Run 3 Nginx replicas"). A **Task** is the atomic unit of the Swarm—essentially a container instance assigned to a node.
- **Reconciliation Loop (Desired State):** The Swarm Manager constantly monitors the cluster. If a node fails and a container stops, the manager automatically reschedules that task on an available node to maintain the "Desired State."
- **Ingress Routing Mesh:** A routing layer that allows any node in the cluster to accept connections for any published service port, regardless of whether the specific container is running on that node.

**Sysadmin Pro-Tip:**

- **Scale:** Swarm is ideal for small to medium deployments (up to 100 nodes, though it excels in the 3–20 range).
- **Quorum:** Always use an **odd number** of managers (3, 5, or 7) to maintain a Raft consensus and prevent "split-brain" scenarios. More than 7 managers can introduce unnecessary latency in state synchronization.


### 8.2. Cluster Deployment Workflow

Following these steps ensures a stable, production-ready Swarm initialization.

#### 8.2.1. Network Requirements

Ensure the following ports are open between all participating nodes (firewall/security groups):

* **2377/tcp:** Cluster management communications.
* **7946/tcp & udp:** Node-to-node control plane communication.
* **4789/udp:** Overlay network data traffic (VXLAN).

#### 8.2.2. Initializing the Leader

On the primary node (e.g., `node1`), initialize the cluster:

```bash
docker swarm init --advertise-addr <MANAGER-IP>

```

*The output will provide a join token for both workers and managers.*

#### 8.2.3. Expanding the Cluster

On all other nodes, use the token provided to join the Swarm:

```bash
# To join as a worker
docker swarm join --token <WORKER-TOKEN> <MANAGER-IP>:2377

```

#### 8.2.4. Managing Node Roles

From the leader node, promote workers to managers for high availability:

```bash
docker node promote node2 node3

```

#### 8.2.5. Image Distribution Strategy

Since containers can run on any node, images must be available cluster-wide.

* **Option A (Recommended):** Use a private/public Registry (Docker Hub, ECR, self-hosted Harbor).
* **Option B (Air-gapped):** Use `docker image save` and `docker image load` to manually sync images across nodes.

#### 8.2.6. Stack Deployment

Define the infrastructure in a `docker-stack.yml` file (similar to Compose) and deploy it:

```bash
docker stack deploy -c docker-stack.yml my_production_stack

```

#### 8.2.7. Cluster Health Audit

Use these essential commands to verify the operational state:

- `docker node ls`: Lists all nodes and their status/role.
- `docker stack ls`: Lists active stacks in the cluster.
- `docker stack services <name>`: Checks the status of services within a stack.
- `docker service logs -f <name>`: Follows cluster-wide logs for a specific service.
- `docker service inspect --pretty <name>`: Shows detailed configuration of a service.


### 8.3. Practical Lab: Deploying a 5-Node Cluster

In this scenario, we will implement a fault-tolerant Swarm cluster. To maintain a quorum while distributing the workload, we will configure **three nodes as Managers** and **two nodes as dedicated Workers**.

**Node Inventory:**

| Hostname | IP Address | Role | OS |
| --- | --- | --- | --- |
| `node1` | 192.168.1.201 | Manager (Leader) | Debian 13 / Ubuntu 24.04 |
| `node2` | 192.168.1.202 | Manager (Reachable) | Debian 13 / Ubuntu 24.04 |
| `node3` | 192.168.1.203 | Manager (Reachable) | Debian 13 / Ubuntu 24.04 |
| `node4` | 192.168.1.204 | Worker | Debian 13 / Ubuntu 24.04 |
| `node5` | 192.168.1.205 | Worker | Debian 13 / Ubuntu 24.04 |

#### 8.3.1. Cluster Initialization

Initialize the Swarm on `node1`. We specify `--advertise-addr` to ensure the manager explicitly listens on the correct network interface for cluster traffic.

**Run on node1:**

```bash
docker swarm init --advertise-addr 192.168.1.201
```

**Execution Output:**
The daemon will generate a unique join token. All subsequent nodes will join as workers by default using this token:

```text
Swarm initialized: current node (zm22...) is now a manager.

To add a worker to this swarm, run the following command:
    docker swarm join --token SWMTKN-1-2xqz... 192.168.1.201:2377

```

#### 8.3.2. Joining the Cluster

Execute the join command provided in the previous step on the remaining four nodes (`node2` through `node5`).

**Run on node2, node3, node4, and node5:**

```bash
docker swarm join --token <WORKER_TOKEN> 192.168.1.201:2377

```

#### 8.3.3. Role Promotion

For high availability, we need three managers. We will promote `node2` and `node3` from their default worker status to managers.

**Run on node1:**

```bash
docker node promote node2 node3
```

#### 8.3.4. Post-Deployment Audit

Verify the cluster topology from any of the manager nodes.

**Run on node1, node2, or node3:**

```bash
docker node ls
```

**Expected Output Summary:**

* **node1:** Status: Ready, Availability: Active, Manager Status: **Leader**
* **node2 & node3:** Status: Ready, Availability: Active, Manager Status: **Reachable**
* **node4 & node5:** Status: Ready, Availability: Active, Manager Status: (Empty/Worker)


### 8.4. Scenario 1: Deploying a Global Web Service

In this initial exercise, we will deploy a static web site across the entire cluster. We will use **Global Mode**, which instructs Swarm to instantiate exactly one container instance on every available node in the cluster.

#### 8.4.1. Image Preparation (Distributed Build)

For this example, we will manually build the image on all nodes. In production, this is typically handled by a Central Registry (which we will cover in the next section).

**Run on all 5 nodes:**

```bash
mkdir ~/example1 && cd ~/example1

# Create a sample index page
cat <<EOF > index.html
<html>
<head><title>Swarm Node</title></head>
<body>
    <h1>Distributed Web Service</h1>
    <p>This page is served by Docker Swarm Ingress Mesh.</p>
</body>
</html>
EOF

# Define the Dockerfile
cat <<EOF > Dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EOF

# Build the local image
docker image build -t web-server:v1 .
```



#### 8.4.2. Defining the Stack Configuration (`stack.yaml`)

We will now create the orchestration manifest. This file defines the services, networks, and deployment policies.

**Run on node1 (Leader) only:**

```bash
nano stack.yaml
```


**YAML Content:**

```yaml
services:
  # Service name: This will be the DNS name for internal communication.
  web-server:
    # The image to be deployed. Must be available on all nodes (or in a registry).
    image: web-server:v1
    
    ports:
      # Port Mapping (Host Port : Container Port)
      # Thanks to Ingress Routing Mesh, the service is accessible on any node's port 8080.
      - "8080:80"

    networks:
      # The virtual network this service will join.
      - web-net

    # 'deploy' block contains Swarm-specific configurations.
    # Note: These settings are ignored by 'docker-compose up'.
    deploy:
      # Deployment Mode:
      # global: Runs exactly one instance on every node in the cluster.
      # replicated: Runs a specific number of instances distributed across the cluster.
      mode: global

      # Policy for container restarts in case of failure.
      restart_policy:
        # condition: on-failure -> Restart only if the container exits with an error.
        condition: on-failure
        # How long to wait between restart attempts.
        delay: 5s
        # Maximum number of attempts before giving up.
        max_attempts: 3
        # Time window used to decide if a restart was successful.
        window: 120s

      # Configuration for rolling updates (e.g., when changing the image version).
      update_config:
        # Number of containers to update at a time.
        parallelism: 1
        # Delay between updating successive container groups.
        delay: 10s

      # Resource Constraints: Prevents a single container from consuming all host resources.
      resources:
        limits:
          # Limit CPU usage to 50% of a single core.
          cpus: '0.50'
          # Limit RAM usage to 512 Megabytes.
          memory: 512M

# Network Definitions
networks:
  web-net:
    # driver: overlay -> Enables multi-host communication. 
    # Containers on different physical nodes can communicate as if on the same LAN.
    driver: overlay
    # attachable: true -> Allows standalone containers (outside this stack) 
    # to manually connect to this network for debugging.
    attachable: true
```

#### 8.4.3. Stack Deployment & Verification

Deploy the stack to the cluster from the manager node.

**Run on node1:**

```bash
docker stack deploy -c stack.yaml example1
```

**Audit the Deployment:**

```bash
# Check service status and replica counts
docker service ls

# Verify task distribution across nodes
docker stack ps example1
```

#### 8.4.4. Accessing the Service

Thanks to the **Ingress Routing Mesh**, we can access the web service using the IP address of any node in the cluster (even if a specific node were only acting as a routing jump).

* `http://192.168.1.201:8080/`
* `http://192.168.1.202:8080/`
* `http://192.168.1.203:8080/`
* `http://192.168.1.204:8080/`
* `http://192.168.1.205:8080/`

#### 8.4.5. Teardown

To remove the stack and all associated containers/networks:

```bash
docker stack rm example1
```

### 8.5. Deploying a Private Local Registry

Building images manually on every node is inefficient and error-prone. While public registries like Docker Hub are convenient, a **Private Local Registry** provides lower latency and keeps the proprietary images within the local network.

#### 8.5.1. Configure Insecure Registry Access

By default, Docker requires HTTPS for registry communication. Since our local registry uses a self-signed or HTTP setup, we must explicitly tell the Docker daemon on **every node** to trust our registry.

**Run on all nodes:**

```bash
sudo nano /etc/docker/daemon.json
```

**JSON Configuration:**

```json
{
  "insecure-registries" : ["192.168.1.201:5000"]
}
```

**Apply changes:**

```bash
sudo systemctl restart docker
```


#### 8.5.2. Deploy the Registry Service

We will deploy the registry as a Swarm Service. To ensure the persistent data (the stored images) remains consistent, we use a **Node Constraint** to keep the service running on `node1`, where the volume resides.

**Run on node1:**

```bash
# Provision persistent storage
docker volume create local-registry-volume

# Deploy the registry service
docker service create --name my-registry \
  --publish published=5000,target=5000 \
  --mount type=volume,source=local-registry-volume,destination=/var/lib/registry \
  --constraint 'node.hostname == node1' \
  registry:2
```



#### 8.5.3. Image Lifecycle: Build, Tag, and Push

To use the local registry, images must follow a specific naming convention: `[REGISTRY-IP]:[PORT]/[IMAGE-NAME]:[TAG]`.

**Run on node1:**

```bash
mkdir ~/registry-test && cd ~/registry-test

# Simple Dockerfile for verification
cat <<EOF > Dockerfile
FROM debian:trixie
CMD ['bash'] 
EOF
# Build and Tag the image for the local registry
docker build -t 192.168.1.201:5000/local-test:v1 .

# Push the image to the local repository
docker push 192.168.1.201:5000/local-test:v1
```


#### 8.5.4. Verification from Other Nodes

Since the registry is now reachable across the network, any node in the Swarm can pull this image directly:

**Run on any other node (e.g., node4):**

```bash
docker pull 192.168.1.201:5000/local-test:v1
```


### 8.6. Scenario 2: Two-Tier Microservices Architecture

#### 8.6.1. Architectural Overview

In this advanced scenario, we will deploy a decoupled infrastructure consisting of a **Python Flask Backend** and an **Nginx Reverse Proxy Frontend**.

**Key Engineering Objectives:**

* **Service Discovery:** The Frontend will route traffic using the logical service name (`backend-service`) instead of volatile IP addresses.
* **Internal Load Balancing:** Swarm will automatically distribute incoming requests from the Frontend across multiple Backend replicas using Virtual IP (VIP).
* **Network Segregation:** We will implement two distinct overlay networks. The `internal-net` will isolate the Backend from public access, while the `public-net` serves as the entry point.
* **Workload Placement:** We will use **Placement Constraints** to ensure that application workloads run exclusively on Worker nodes, preserving Manager node resources for cluster orchestration.

#### 8.6.2. Backend Development (Python/Flask)

This service will identify which node and container is responding, allowing us to verify the load balancing in action.

**Build on node1:**

```bash
# Workspace setup
mkdir -p ~/example2/backend && cd ~/example2/backend

# Application logic
cat <<EOF > app.py
from flask import Flask
import os, socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Node name will be injected via environment variables in the stack file
    node_name = os.getenv('MY_NODE_NAME', 'unknown_node')
    container_id = socket.gethostname()
    return f"Response from Backend - Node: {node_name} | Container ID: {container_id}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
EOF

# Dockerfile definition
cat <<EOF > Dockerfile
FROM python:3.14-slim
RUN pip install flask
WORKDIR /app
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
EOF

# Build, Tag, and Push to Local Registry
docker image build -t 192.168.1.201:5000/example2-backend:v1 .
docker image push 192.168.1.201:5000/example2-backend:v1
```

#### 8.6.3. Frontend Development (Nginx Reverse Proxy)

The Frontend acts as the gateway. Its configuration points to the Backend service name, which Docker Swarm's internal DNS resolves to the service's Virtual IP.

**Build on node1:**

```bash
# Workspace setup
mkdir -p ~/example2/frontend && cd ~/example2/frontend

# Custom Nginx Reverse Proxy Configuration
cat <<EOF > custom.conf
server {
    listen 80;

    location / {
        # Routing to the logical service name defined in stack.yaml
        proxy_pass http://backend-service:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

# Dockerfile definition
cat <<EOF > Dockerfile
FROM nginx:alpine
COPY custom.conf /etc/nginx/conf.d/default.conf
EOF

# Build, Tag, and Push to Local Registry
docker image build -t 192.168.1.201:5000/example2-frontend:v1 .
docker image push 192.168.1.201:5000/example2-frontend:v1
```

#### 8.6.4. Orchestration & Deployment (The Stack)

We will now define the relationship between our services. Note the use of **Docker Template Variables** to inject host-specific data into the containers.

**Run on node1:**

```bash
cd ~/example2
nano stack.yaml
```

**YAML Manifest:**

```yaml
services:
  # BACKEND: Isolated tier running on worker nodes only
  backend-service:
    image: 192.168.1.201:5000/example2-backend:v1
    environment:
      # Templating: Automatically injects the host's name into the container
      MY_NODE_NAME: "{{.Node.Hostname}}"
    networks:
      - internal-net
    deploy:
      mode: replicated
      replicas: 2 
      placement:
        constraints:
          # High Availability Rule: Keep application logic away from Manager nodes
          - "node.role == worker"
      
      update_config:
        parallelism: 1
        delay: 10s
        # Zero-Downtime Strategy: Spawns new version before terminating the old one
        order: start-first

  # FRONTEND: Gateway tier acting as the cluster entry point
  frontend-service:
    image: 192.168.1.201:5000/example2-frontend:v1
    ports:
      - "80:80"
    networks:
      - internal-net
      - public-net
    deploy:
      # Ensures high availability by running on every node (Manager & Worker)
      mode: global

networks:
  internal-net:
    driver: overlay
    attachable: true
  public-net:
    driver: overlay
```

**Deploying the Stack:**

```bash
docker stack deploy -c stack.yaml example2
```

**Verification & Monitoring:**
Because of the **Ingress Routing Mesh**, any node IP will serve the response from the backend through the Nginx frontend. Refreshing the browser should show responses from different Container IDs due to the internal load balancing.

```bash
# Check task distribution and placement constraints
docker stack ps example2

# View overall service status
docker service ls
```

#### 8.6.5. Versioning & Rolling Updates

In production, updating a service must be handled without interrupting the user experience. Docker Swarm facilitates this through **Rolling Updates**, where it replaces containers one by one (or in batches) according to a defined strategy.

**Code Modification & Versioning**
We will create a new version of our backend to reflect a logic change.

**Run on node1:**

```bash
cd ~/example2/backend
# Modify the app logic
sed -i 's/Response from Backend/Updated response (v2) from Backend/g' app.py

# Build and Push the NEW version
docker image build -t 192.168.1.201:5000/example2-backend:v2 .
docker image push 192.168.1.201:5000/example2-backend:v2

```

**Implementing the Advanced Update Strategy**

We modify the `stack.yaml` to point to the new image and define how Swarm should handle the transition and potential failures.

**Update `stack.yaml` on node1:**

```
cd ~/example2
nano stack.yaml
```

Change as below:

```
services:
  backend-service:
    # We will change this to :v2 for the update test
    image: 192.168.1.201:5000/example2-backend:v2
    environment:
      MY_NODE_NAME: "{{.Node.Hostname}}"
    networks:
      - internal-net
    deploy:
      mode: replicated
      replicas: 2
      placement:
        constraints:
          - "node.role == worker"
      
      # --- ADVANCED UPDATE STRATEGY ---
      update_config:
        # How many containers to update at once
        parallelism: 1
        # Delay between updating each container group
        delay: 15s
        # start-first: New container starts before old one stops (Zero downtime)
        # stop-first: Old container stops before new one starts (Saves resources)
        order: start-first
        # What to do if the update fails? (continue, rollback, pause)
        failure_action: rollback
        # Maximum failure rate allowed during an update
        max_failure_ratio: 0.1
        # Time to wait after a container starts to consider it "healthy"
        monitor: 20s

      # --- ROLLBACK STRATEGY ---
      # Defines what happens if the update fails and triggers a rollback
      rollback_config:
        parallelism: 2
        order: stop-first

  frontend-service:
    image: 192.168.1.201:5000/example2-frontend:v1
    ports:
      - "80:80"
    networks:
      - internal-net
      - public-net
    deploy:
      mode: global

networks:
  internal-net:
    driver: overlay
  public-net:
    driver: overlay
```

**Executing the Zero-Downtime Update**

Re-deploying the stack triggers the update. Swarm detects the image change and begins the rolling update based on the parameters.

**Run on node1:**

```bash
docker stack deploy -c stack.yaml example2
```


While the update is in progress, we can watch Swarm killing the old tasks and spawning new ones:

```bash
# Watch the rolling transition in real-time
watch docker stack ps example2
```

As we refresh our browser, we will initially see a mix of `v1` and `v2` responses, eventually transitioning completely to `v2` as the rollout completes.

**Final Cleanup**

Once the verification is complete:

```bash
docker stack rm example2
```


### 8.7. Scenario 3: Reverse Proxy with TLS

#### 8.7.1. Architectural Design

In this scenario, we move towards a production-hardened infrastructure. We will implement a high-security boundary using **Nginx as a TLS-terminating Reverse Proxy**.

**Key Strategic Objectives:**

- **Security (Docker Secrets):** Use native Swarm Secrets to securely inject TLS certificates and private keys into the Proxy container at runtime. These never touch the disk in an unencrypted state.
- **Configuration Management (Docker Configs):** Externalize the Nginx configuration. This allows updating the proxy's behavior without rebuilding the Nginx image.
- **Role Separation:** 
    - **Proxy Tier:** Runs on **Manager Nodes** (often acting as the cluster edge/gateway).
    - **Application Tier:** Runs on **Worker Nodes** with multiple replicas for horizontal scaling.
- **Network Isolation:** The Backend remains completely hidden from the public internet, accessible only via the `proxy-net` overlay network.


#### 8.7.2. Backend Development (Stateless API)

Our backend will be a lightweight Python service designed to report its internal state, allowing us to verify versioning and load distribution.

**Build on node1:**

```bash
# Environment setup
mkdir -p ~/example3/backend && cd ~/example3/backend

# Application Logic: Simple HTTP Response with Versioning
cat <<EOF > app.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket

VERSION = os.environ.get("APP_VERSION", "1.0")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        response = f"""
Service: Backend API
Version: {VERSION}
Pod/Container: {socket.gethostname()}
"""
        self.wfile.write(response.encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print(f"Server started on port 8080 (v{VERSION})")
    server.serve_forever()
EOF

# Multi-stage optimized Dockerfile
cat <<EOF > Dockerfile
FROM python:3.14-alpine

WORKDIR /app
COPY app.py .

# Metadata and Default Version
ENV APP_VERSION=1.0
EXPOSE 8080

CMD ["python", "app.py"]
EOF

# Build, Tag, and Push to Enterprise Registry
docker image build -t 192.168.1.201:5000/example3-backend:1.0 .
docker image push 192.168.1.201:5000/example3-backend:1.0
```

#### 8.7.3. Infrastructure Security: Secrets & Configs

In this step, we prepare the sensitive credentials and externalize our configuration. Instead of baking these into an image, we inject them into the Swarm control plane.

**Generating TLS Assets (Self-Signed)**

We will generate a 2048-bit RSA key pair for our proxy. In a production environment, we would replace these with certificates from a CA (like Let's Encrypt or an internal PKI).

**Run on node1:**

```bash
cd ~/example3
# Generate a self-signed certificate valid for 1 year
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout domain.key \
  -out domain.crt \
  -subj "/CN=example3.local"
```

**Provisioning Docker Secrets**

When we create a secret, Docker Swarm encrypts it and distributes it only to the nodes running the specific service that requires it.

```bash
docker secret create tls_cert domain.crt
docker secret create tls_key domain.key

# Audit the secret store
docker secret ls
```

*Note: Secrets are mounted as read-only files inside the container at `/run/secrets/`.*

**Externalizing Nginx Configuration (Docker Configs)**
We define our Nginx behavior in a standalone file. This configuration uses the mounted secrets for SSL and defines the upstream load balancing to our backend.

```bash
nano nginx.conf
```

Configuration Content:

```nginx
events { worker_connections 1024; }

http {
    upstream backend_cluster {
        # Swarm's internal DNS resolves 'backend' to the Service VIP
        server backend:8080;
    }

    server {
        listen 443 ssl;
        server_name example3.local;

        # Direct reference to paths where Docker mounts the secrets
        ssl_certificate     /run/secrets/tls_cert;
        ssl_certificate_key /run/secrets/tls_key;

        # Standard SSL hardening (optional but recommended)
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;

        location / {
            proxy_pass http://backend_cluster;
            
            # Preserve client context
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

**Registering the Config Object**
Similar to secrets, **Configs** allow updating the service's behavior without rebuilding the Nginx image.

```bash
docker config create nginx_conf nginx.conf

# Verify registration
docker config ls
```



#### 8.7.4. Orchestration: Deploying the Secure Stack

The final piece of our puzzle is the `stack.yaml` file. This manifest bridges our local registry images with the pre-defined Docker Secrets and Configs stored in the Swarm control plane.

**Run on node1:**

```bash
nano stack.yaml
```

```
############################################################
# Swarm Stack: Reverse Proxy + Replicated Backend
#
# Demonstrates:
# - overlay networks
# - secrets
# - configs
# - placement constraints
# - rolling updates
# - restart policies
############################################################

services:

  ##########################################################
  # Reverse Proxy (TLS Termination)
  ##########################################################
  proxy:
    image: nginx:alpine

    ports:
      # Expose HTTPS externally
      - "443:443"

    networks:
      - frontend

    # Swarm secrets (mounted under /run/secrets/)
    secrets:
      - tls_cert
      - tls_key

    # Swarm config (overrides default nginx.conf)
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf

    deploy:
      replicas: 1

      placement:
        # Run proxy only on manager nodes
        constraints:
          - node.role == manager

      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3

      update_config:
        # Rolling update strategy
        parallelism: 1
        delay: 10s
        order: start-first

  ##########################################################
  # Backend Service (Internal Only)
  ##########################################################
  backend:
    image: 192.168.1.201:5000/example3-backend:1.0

    networks:
      - frontend

    deploy:
      replicas: 3

      placement:
        # Run backend only on worker nodes
        constraints:
          - node.role == worker

      restart_policy:
        condition: on-failure
        delay: 5s

      update_config:
        parallelism: 1
        delay: 10s
        order: start-first

############################################################
# Overlay Network
############################################################
networks:
  frontend:
    driver: overlay

############################################################
# External Secrets
############################################################
secrets:
  tls_cert:
    external: true
  tls_key:
    external: true

############################################################
# External Configs
############################################################
configs:
  nginx_conf:
    external: true
```

**Deployment Execution**

Deploy the stack using the defined manifest. Docker Swarm will fetch the secrets and configs from its internal encrypted store and mount them into the containers.

```bash
docker stack deploy -c stack.yaml example3
```

Monitor the deployment until all replicas are in the `Running` state:

```bash
docker stack services example3
docker stack ps example3
```


**Testing the TLS endpoint:**
Use `curl -k` (to ignore the self-signed certificate warning) and observe the **Hostname** changing with each request. This confirms that the Nginx proxy is successfully round-robin load balancing across the three backend replicas on the worker nodes.

```bash
# Repeat this command to see different Hostnames (Container IDs)
curl -k https://192.168.1.201
```

If we run repeatedly, we can see that hostname changes.

**Accessing via Browser**

we can point our browser to any node IP in the cluster (e.g., `https://192.168.1.204`). The **Ingress Routing Mesh** will intercept the traffic on port 443 and route it to the `proxy` service running on the Manager node, which in turn proxies it to a `backend` task on a Worker node.


#### 8.7.5. Executing the Rolling Update (v1.0 to v2.0)

In this phase, we will perform a **Zero-Downtime** update of our backend. Thanks to our `start-first` configuration, Docker Swarm will ensure the new version is healthy before deactivating the old one.

**Rebuilding the Backend Image**
We will increment the versioning inside the Dockerfile to track the rollout.

**Run on node1:**

```bash
cd ~/example3/backend
# Update the environment variable for visibility
sed -i 's/APP_VERSION=1.0/APP_VERSION=2.0/g' Dockerfile

# Build and Push the v2.0 image to our local registry
docker image build -t 192.168.1.201:5000/example3-backend:2.0 .
docker image push 192.168.1.201:5000/example3-backend:2.0
```

Update image definition in stack file too:

Change the line:

```
image: 192.168.1.201:5000/example3-backend:1.0
```

to:

```
image: 192.168.1.201:5000/example3-backend:2.0
```

```
cd ~/example3
nano stack.yaml
```

The final state of the file will be as below:

```
############################################################
# Swarm Stack: Reverse Proxy + Replicated Backend
#
# Demonstrates:
# - overlay networks
# - secrets
# - configs
# - placement constraints
# - rolling updates
# - restart policies
############################################################

services:

  ##########################################################
  # Reverse Proxy (TLS Termination)
  ##########################################################
  proxy:
    image: nginx:alpine

    ports:
      # Expose HTTPS externally
      - "443:443"

    networks:
      - frontend

    # Swarm secrets (mounted under /run/secrets/)
    secrets:
      - tls_cert
      - tls_key

    # Swarm config (overrides default nginx.conf)
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf

    deploy:
      replicas: 1

      placement:
        # Run proxy only on manager nodes
        constraints:
          - node.role == manager

      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3

      update_config:
        # Rolling update strategy
        parallelism: 1
        delay: 10s
        order: start-first

  ##########################################################
  # Backend Service (Internal Only)
  ##########################################################
  backend:
    image: 192.168.1.201:5000/example3-backend:2.0

    networks:
      - frontend

    deploy:
      replicas: 3

      placement:
        # Run backend only on worker nodes
        constraints:
          - node.role == worker

      restart_policy:
        condition: on-failure
        delay: 5s

      update_config:
        parallelism: 1
        delay: 10s
        order: start-first

############################################################
# Overlay Network
############################################################
networks:
  frontend:
    driver: overlay

############################################################
# External Secrets
############################################################
secrets:
  tls_cert:
    external: true
  tls_key:
    external: true

############################################################
# External Configs
############################################################
configs:
  nginx_conf:
    external: true
```

**Triggering the Deployment**

Apply the updated manifest. Swarm will detect the image change and begin the rolling update according to the `parallelism` and `delay` rules we defined.

```bash
docker stack deploy -c stack.yaml example3
```

**Monitoring the Rollout Strategy**

We can monitor the state of the tasks during the transition.

```bash
# Watch the transition in real-time (Ctrl+C to exit)
watch docker service ps example3_backend

# Audit the update policy and status in detail
docker service inspect example3_backend --pretty
```

**Verification via Ingress Mesh**

While the update is running, we can hit any node in the cluster. we will notice a period where both `Version: 1.0` and `Version: 2.0` responses appear as the load balancer routes traffic to old and new containers simultaneously.

```bash
# Test from terminal
curl -k https://192.168.1.201
```

**Expected Outcome:** Eventually, all responses will show `Backend Version: 2.0`. The TLS proxy (Nginx) continues to run without interruption on the Manager node throughout this process.


#### 8.7.6. Secret Rotation: Updating TLS Certificates

Docker Secrets are **immutable**; once created, they cannot be updated or overwritten. To rotate a certificate or password, we must create a new secret and update the service to point to the new resource.

We will use a mapping technique to ensure the container sees the new secret at the same file path, avoiding the need to modify our Nginx configuration file.

**Generate the New TLS Certificate (v2)**
**Run on node1:**

```bash
cd ~/example3
# Create a fresh certificate for the next year
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout domain_v2.key \
  -out domain_v2.crt \
  -subj "/CN=example3.local"
```

**Register New Secrets in Swarm**

```bash
docker secret create tls_cert_v2 domain_v2.crt
docker secret create tls_key_v2  domain_v2.key

# Verify the new objects coexist with the old ones
docker secret ls
```

**3. Update the Stack Manifest with Target Mapping**
The secret to a smooth rotation is the `source` and `target` definition. We change the `source` to the new version, but keep the `target` as `tls_cert` so Nginx finds it at `/run/secrets/tls_cert`.


**Edit `stack.yaml` on node1:**

```
nano stack.yaml
```

The parts to change:

```yaml
services:
  proxy:
    # ... (other settings)
    secrets:
      # Use the new version but mount it with the original filename
      - source: tls_cert_v2
        target: tls_cert
      - source: tls_key_v2
        target: tls_key

# ... (backend service remains v2.0)

# Declare the new external secrets
secrets:
  tls_cert_v2:
    external: true
  tls_key_v2:
    external: true

```



And the final state of the file:

```yaml
############################################################
# Swarm Stack: Reverse Proxy + Replicated Backend
#
# Final State:
# - Backend version 2.0
# - TLS secrets rotated (v2)
# - Rolling update strategy enabled
# - Placement constraints enforced
############################################################

services:

  ##########################################################
  # Reverse Proxy (TLS Termination)
  ##########################################################
  proxy:
    image: nginx:alpine

    ports:
      - "443:443"   # Expose HTTPS externally

    networks:
      - frontend

    # Secrets mounted under /run/secrets/
    secrets:
      # Rotate source secret but keep target filename stable
      - source: tls_cert_v2
        target: tls_cert
      - source: tls_key_v2
        target: tls_key

    # Override default nginx configuration
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf

    deploy:
      replicas: 1

      placement:
        constraints:
          - node.role == manager

      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3

      update_config:
        parallelism: 1
        delay: 10s
        order: start-first


  ##########################################################
  # Backend Service (Internal Only)
  ##########################################################
  backend:
    image: 192.168.1.201:5000/example3-backend:2.0

    networks:
      - frontend

    deploy:
      replicas: 3

      placement:
        constraints:
          - node.role == worker

      restart_policy:
        condition: on-failure
        delay: 5s

      update_config:
        parallelism: 1
        delay: 10s
        order: start-first


############################################################
# Overlay Network
############################################################
networks:
  frontend:
    driver: overlay


############################################################
# External Secrets (Must Already Exist in Swarm)
############################################################
secrets:
  tls_cert_v2:
    external: true
  tls_key_v2:
    external: true


############################################################
# External Configs (Must Already Exist in Swarm)
############################################################
configs:
  nginx_conf:
    external: true
```

**Execute the Rotation**

Apply the stack. Swarm will perform a rolling update of the proxy service, unmounting the old secrets and mounting the new `v2` versions.

```bash
docker stack deploy -c stack.yaml example3
```

**Post-Rotation Cleanup**

Once the update is verified and the old containers are gone, we can safely decommission the old secret objects from the cluster database.

```bash
docker secret rm tls_cert tls_key
```

**Stack Cleanup**

After finishing our test, we can remove the full stack.

```bash
docker stack rm example3
```

### 8.8. Docker Swarm stack.yml Cheat Sheet

**Basic Structure:**

```yaml
services:
  service_name:
    image: image:tag
    ports:
      - "published:target"
    networks:
      - network_name
    volumes:
      - volume_name:/path
    environment:
      - KEY=value
    secrets:
      - secret_name
    configs:
      - config_name
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == worker
      restart_policy:
        condition: on-failure
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first

networks:
  network_name:
    driver: overlay

volumes:
  volume_name:

secrets:
  secret_name:
    external: true

configs:
  config_name:
    external: true
```

**Frequently Used `deploy` Options**

Replication:

```
deploy:
  replicas: 3
```

Global Mode (run on every node):

```
deploy:
  mode: global
```

Placement Constraints:

```
deploy:
  placement:
    constraints:
      - node.role == worker
      - node.hostname == node3
      - node.labels.region == eu
```

To add a label:

`docker node update --label-add region=eu node3`

Restart Policy:

```
restart_policy:
  condition: on-failure
  delay: 5s
  max_attempts: 3
```

Rolling Update Strategy:

```
update_config:
  parallelism: 1
  delay: 10s
  order: start-first
```

Explanations:

- `parallelism`: how many tasks to update simultaneously
- `delay`: wait time between batches
- `order`:
    - `start-first` → minimal downtime
    - `stop-first` → resource conservative


**Secrets Usage**

Simple

```
secrets:
  - my_secret
```

Mounted at:

```
/run/secrets/my_secret
```

Advanced (rename target inside container):

```
secrets:
  - source: db_password_v2
    target: db_password
```

Secrets are immutable. Rotation = new secret + service update.

Configs:

```
configs:
  - source: nginx_conf
    target: /etc/nginx/nginx.conf
```

Unlike secrets; Not encrypted at rest, Intended for non-sensitive configuration


**Networking Patterns**

Internal Service (not exposed):

```
networks:
  - backend_net
```

No `ports:` → not reachable from host.

Public Service:

```
ports:
  - "443:443"
```


Volumes (Persistent Storage):

```
volumes:
  - db_data:/var/lib/mysql
```

Declare at bottom:

```yaml
volumes:
  db_data:
```

**Common Patterns**

Reverse Proxy + Backend:

- Proxy publishes ports
- Backend internal only
- Shared overlay network

Database + App

- DB secret for password
- App reads secret via `_FILE`
- Volume for DB persistence


**Useful Commands for Stack Debugging**

Deploy:

```
docker stack deploy -c stack.yaml mystack
```

List services:

```
docker stack services mystack
```

Watch tasks:

```
docker service ps mystack_service
```

Inspect service:

```
docker service inspect mystack_service --pretty
```

Remove stack:

```
docker stack rm mystack
```

---


## 9. Maintenance & Troubleshooting

As a system admin, our job starts after the deployment. Keeping the host healthy and knowing how to drain traffic is crucial.

### 9.1. Log Rotation (Preventing Disk Exhaustion)

By default, Docker captures the stdout/stderr of all containers and stores them in JSON files. Without limits, these files can grow indefinitely and fill the `/var` partition.

**Best Practice:** Configure global limits in `/etc/docker/daemon.json` on all nodes.

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

*This ensures no container uses more than 30MB (3x10MB) of log space.*


### 9.2. Node Maintenance (Drain Mode)

When we need to perform maintenance on a physical server (e.g., kernel update, hardware upgrade), we shouldn't just shut it down. we must first tell Swarm to migrate the tasks to other nodes.

**Set node to Drain mode:**

```bash
docker node update --availability drain node4
```

*Swarm will immediately stop tasks on node4 and reschedule them on other active nodes.*

**Perform maintenance & Reboot.**

**Set node back to Active mode:**

```bash
docker node update --availability active node4
```

*Note: Swarm won't automatically move old tasks back. New tasks or service updates will now consider this node again.*



### 9.3. Monitoring & Resource Auditing

When a service is slow, use these tools to identify the bottleneck:

* **`docker stats`**: Real-time stream of CPU, memory, and network usage for all containers on the **local** host.
* **`docker service ps --filter "desired-state=shutdown" <service>`**: Helps finding why a service is constantly restarting (Crash looping).
* **`docker service inspect --pretty <service>`**: Check if a service is hitting its `resources.limits`. If a container hits its memory limit, Docker will OOM-Kill (Out Of Memory) it.



### 9.4. Troubleshooting Workflow

If a service in Swarm isn't working:

1. **Check Service Status:** `docker service ls` (Look for `0/3` replicas).
2. **Locate the Error:** `docker service ps <service_name>` (Look for the `ERROR` column).
3. **Inspect Logs:** `docker service logs -f <service_name>`.
4. **Check Daemon Health:** `docker system events --since 30m` (See what the engine has been doing recently).

