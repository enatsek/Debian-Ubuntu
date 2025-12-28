# Debian & Ubuntu Tutorials & Guides

A collection of practical documentation for Debian and Ubuntu system administration. These guides are written from real-world experience and serve as a reference for common tasks, configurations, and troubleshooting.

## About This Repository

This documentation started as personal notes to compensate for a terrible memory. What began as a single text file evolved into a comprehensive collection of tutorials covering web servers, databases, networking, virtualization, and system administration.

**Philosophy:** Keep it simple, text-based, and useful. Every guide here documents something I've actually configured or deployed.

---

## 📚 Contents

### Web Services & HTTPS

- [**Apache 2nd Ed.**](apache.md) — Apache HTTP server configuration with SSL support and sample configurations
- [**Nginx 2nd Ed.**](nginx.md) — Nginx HTTP server configuration with SSL support and LEMP stack setup
- [**Certbot**](certbot.md) — Automated SSL certificate management with Let's Encrypt for Apache and Nginx
- [**LAPP Stack**](lapp.md) — Linux, Apache, PostgreSQL, PHP stack installation and configuration
- [**LAMP Stack**](lamp.md) — Linux, Apache, MariaDB, PHP stack installation and configuration
- [**WordPress**](wordpress.md) — WordPress installation and activation guide
- [**Adminer Tool**](adminer.md) — Web-based database management (PHPMyAdmin alternative)

### Database Management

- [**MariaDB**](mariadb.md) — Installation, configuration, user management, and primary-replica replication
- [**MariaDB Cluster**](mariadbcluster.md) — Multi-master replication with Galera Cluster
- [**PostgreSQL (Ubuntu)**](postgresubuntu.md) — Installation, configuration, user management, cluster management, backup/restore on Ubuntu
- [**PostgreSQL (Debian)**](postgresdebian.md) — Installation, configuration, user management, cluster management, backup/restore on Debian

### Networking

- [**Debian Network Configuration**](networkdebian.md) — Basic network configuration for Debian systems
- [**Ubuntu Network Configuration**](networkubuntu.md) — Basic network configuration for Ubuntu systems
- [**UFW (Uncomplicated Firewall)**](ufw.md) — Firewall configuration and management
- [**Self-Hosted VPN**](shvpn.md) — WireGuard VPN server setup for remote access
- [**Site-to-Site VPN**](s2svpn.md) — WireGuard VPN configuration for connecting networks

### Infrastructure & Virtualization

- [**KVM Virtualization (Beginner)**](KVMOnDebianUbuntu1.md) — Introduction to KVM virtualization
- [**KVM Virtualization (Networking)**](KVMOnDebianUbuntu2.md) — Advanced KVM networking configurations
- [**HAProxy**](haproxy.md) — High-availability load balancing with SSL/TLS and keepalived
- [**Ansible**](ansible.md) — Configuration management and automation
- [**LVM (Logical Volume Management)**](lvm.md) — Flexible disk management with LVM
- [**Keepalived**](keepalived.md) — High-availability clustering
- [**DNS**](dns.md) — Primary and replica DNS server configuration
- [**Active Directory**](ad.md) — Simple AD domain with multiple domain controllers and file server
- [**Node.js**](nodejs.md) — Node.js installation and basic setup

### System Administration Guides

- [**User and Group Administration**](useradministration.md) — User and group management essentials
- [**/etc Folder Contents**](etcfolder.md) — Overview of the /etc directory structure
- [**Regular Expressions**](regex.md) — Regex tutorial for text processing
- [**File Compression**](filecompression.md) — Compression utilities overview and usage
- [**FHS (Filesystem Hierarchy Standard)**](fhs.md) — Linux filesystem structure specifications
- [**Systemd Basics**](systemd.md) — Introduction to systemd service management
- [**Systemd Advanced**](systemd2.md) — Additional systemd services and tools
- [**Debian Packaging**](debpackaging.md) — Creating and managing .deb packages
- [**Other Linux Distributions**](otherlinuxes.md) — Managing Debian, Ubuntu, Red Hat, Alpine, and Devuan systems

---

## 🎯 Who Is This For?

- System administrators managing Debian/Ubuntu servers
- Anyone learning Linux server administration
- People who prefer practical, tested documentation over theoretical explanations
- Those who need quick reference guides for common tasks

## 📖 How to Use

Each document is self-contained and includes step-by-step instructions. Browse the categories above, pick a topic, and dive in. All guides assume you have basic Linux command-line familiarity.

## 🤝 Contributing

Found an error? Have a suggestion? Feel free to open an issue or submit a pull request. These docs are maintained based on real-world usage, so practical feedback is always welcome.

## 📄 License

This documentation is provided as-is for anyone who finds it useful. Use freely, no strings attached.

---


