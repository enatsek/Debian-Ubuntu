##### LAMP Stack 
# Installing LAMP Stack On Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.0. The What

The LAMP stack is a popular open-source web development platform. The acronym stands for:
- **L**inux (the operating system)
- **A**pache (the web server)
- **M**ySQL/MariaDB (the database management system)
- **P**HP/Perl/Python (the programming language for application logic)

It provides a robust foundation for building and hosting dynamic websites and web applications.

In this guide, we will use **MariaDB** as our database and **PHP** as our server-side scripting language.

### 0.1. Environment

- **Server Distro:** Debian 12/13 or Ubuntu 22.04/24.04 LTS Server

### 0.2. Sources

- [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)  
- [geeksforgeeks](https://www.geeksforgeeks.org/how-to-retrieve-data-from-mysql-database-using-php/)

<br>
</details>

<details markdown='1'>
<summary>
1. Install Packages
</summary>

---

Update package repositories and install Apache:

```
sudo apt update
sudo apt install --yes apache2
```

Install MariaDB:

```
sudo apt install --yes mariadb-server
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


Install PHP along with the necessary modules for Apache and MySQL/MariaDB integration:

```
sudo apt install --yes php libapache2-mod-php php-mysql
```

**Optional:** Depending on your application (e.g., WordPress), you may need additional PHP extensions:

```
sudo apt install --yes php-curl php-gd php-mbstring php-xml php-xmlrpc \
     php-soap php-intl php-zip
```

Restart Apache to load the PHP module:

```
sudo systemctl restart apache2
```

<br>
</details>

<details markdown='1'>
<summary>
2. Test LAMP Stack
</summary>

---

We will create a test database, add a table with sample data, and then create a PHP script to retrieve this data and display it in a web page.

### 2.1. Database Operations

Access the MariaDB shell:

```
sudo mariadb
```

Run the following commands within the MariaDB shell to create a database, a table, sample data, and a dedicated database user:


```
CREATE DATABASE mysampledb;
USE mysampledb;
CREATE TABLE Employees (Name CHAR(15), Age INT, Occupation CHAR(15));
INSERT INTO Employees VALUES ('Joe Smith', 26, 'Ninja');
INSERT INTO Employees VALUES ('John Doe', 33, 'Sleeper');
INSERT INTO Employees VALUES ('MariaDB Server', 14, 'RDBMS');
GRANT ALL PRIVILEGES ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
EXIT;
```

### 2.2. Create a Test PHP File

Create a new PHP file in the web server's root directory:

```
sudo nano /var/www/html/test.php
```

Copy and paste the following content into the file:

```
<?php
   $mycon = new mysqli("localhost", "appuser", "password", "mysampledb");
   if ($mycon->connect_errno)
   {
      echo "Connection Error";
      exit();
   }
   $mysql = "SELECT * FROM Employees";
   $result = ($mycon->query($mysql));
   $rows = [];
   if ($result->num_rows > 0)
    {
        $rows = $result->fetch_all(MYSQLI_ASSOC);
    }
?>
<!DOCTYPE html>
<html>
<body>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>Occupation</th>
            </tr>
        </thead>
        <tbody>
            <?php
               if(!empty($rows))
               foreach($rows as $row)
              {
            ?>
            <tr>
                <td><?php echo $row['Name']; ?></td>
                <td><?php echo $row['Age']; ?></td>
                <td><?php echo $row['Occupation']; ?></td>
            </tr>
            <?php } ?>
        </tbody>
    </table>
</body>
</html>
<?php
    mysqli_close($mycon);
?>

```

### 2.3. Test the Setup

Open a web browser on your workstation and navigate to the following URL, replacing `srv` with your server's IP address or hostname:

`http://srv/test.php`

You should see a table displaying the data from the `Employees` table.

</details>




