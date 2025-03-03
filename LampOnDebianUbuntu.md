##### LampOnDebianUbuntu 
# LAMP Stack On Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>
---
- L: Debian 12/11 or Ubuntu 24.04/22.04 LTS Server
- A: Apache 2 
- M: MariaDB (Mysql could be another option)
- P: PHP (Python or Perl could be other options)

Sources:  
[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)  
[geeksforgeeks](https://www.geeksforgeeks.org/how-to-retrieve-data-from-mysql-database-using-php/)

<br>
</details>

<details markdown='1'>
<summary>
1. Install Packages
</summary>
---
### 1.0. Update Repositories
```
sudo apt update
```

### 1.1. Install Apache
```
sudo apt install --yes apache2
```

### 1.2. Install MariaDB
```
sudo apt install --yes mariadb-server
```

### 1.3. Secure MariaDB
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

### 1.4. Install PHP, Mariadb and Apache dependencies
```
sudo apt install --yes php libapache2-mod-php php-mysql
```

### 1.5. Install other PHP dependencies 
Depending on the PHP code, you may need some more PHP library packages.

For example, Wordpress needs the following packages:

```
sudo apt install --yes php-curl php-gd php-mbstring php-xml php-xmlrpc \
     php-soap php-intl php-zip
```

### 1.6. Restart Apache
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

We'll create a test database, a table in that database, add some rows to the table on Mariadb. We will also create a test PHP file with the PHP code to retrieve the data from the database and display it as HTML. 

### 2.1. DB Operations
Connect to Mariadb shell

```
sudo mariadb
```

Create mysampledb database, connect to it, create a table, fill the table, create a user with the access permission to that database and the table.


Run on Mariadb shell.

```
CREATE DATABASE mysampledb;
USE mysampledb;
CREATE TABLE Employees (Name char(15), Age int(3), Occupation char(15));
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
INSERT INTO Employees VALUES ('John Doe', '33', 'Sleeper');
INSERT INTO Employees VALUES ('Mariadb Server', '14', 'RDBM');
GRANT ALL ON mysampledb.* TO 'appuser'@'localhost' IDENTIFIED BY 'password';
exit
```

### 2.2. Create Test PHP
```
sudo nano /var/www/html/test.php
```

Fill as below

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
    mysqli_close($conn);
?>

```

### 2.3. Test it
Now, from your workstation's browser, load the page (replace srv with your server's IP or name: 

`http:/srv/test.php`
</details>




