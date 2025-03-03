##### LappOnDebianUbuntu 
# LAPP Stack On Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>
---
- L: Debian 12/11 or Ubuntu 24.04/22.04 LTS Server
- A: Apache 2 
- P: Postgresql
- P: PHP (Python or Perl could be other options)

Sources:
[stackoverflow.com](https://stackoverflow.com/questions/49157928/how-to-fetch-data-from-postgresql-using-php)

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

### 1.2. Install Postgres
```
sudo apt install --yes postgresql
```

### 1.3. Install PHP, Postgres and Apache dependencies
```
sudo apt install --yes php libapache2-mod-php php-pgsql
```

### 1.4. Install other PHP dependencies 
Depending on the PHP code, you may need some more PHP library packages.  For example, Wordpress needs the following packages:

```
sudo apt install --yes php-curl php-gd php-mbstring php-xml php-xmlrpc \
     php-soap php-intl php-zip
```

### 1.5. Restart Apache
```
sudo systemctl restart apache2
```

<br>
</details>

<details markdown='1'>
<summary>
2. Test LAPP Stack
</summary>
---
We'll create a test database, a table in that database, add some rows to the table on Postgres. We will also create a test PHP file with the PHP code to retrieve the data from the database and display it as HTML. 

### 2.1. DB Operations
Create a test Postgres user and give its password 

```
sudo -u postgres createuser --pwprompt testuser
```

Create a test Database

```
sudo -u postgres createdb testdb
```

Connect to Postgres shell

```
sudo -u postgres psql testdb
```

Create a table, fill the table, give test user access permission to that database and the table.

**Run on Postgres shell**

```
CREATE TABLE Employees (Name char(15), Age int, Occupation char(15));
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
INSERT INTO Employees VALUES ('John Doe', '33', 'Sleeper');
INSERT INTO Employees VALUES ('Postgres Server', '14', 'RDBM');
GRANT SELECT ON ALL TABLES IN SCHEMA public to testuser;
exit
```
 
### 2.2. Create Test PHP
```
sudo nano /var/www/html/test.php
```

Fill it as below, remember to change to your password

```
<?php
    $dbh = 'localhost';
    $dbn= 'testdb';
    $dbu = 'testuser';
    $dbp = 'password';
    $dbconn = pg_connect("host=$dbh dbname=$dbn user=$dbu password=$dbp")
        or die('Connection Error: ' . pg_last_error());
   $query = 'SELECT * FROM Employees';
   $result = pg_query($query) or die('Error message: ' . pg_last_error());
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
               while ($row = pg_fetch_row($result)) {
            ?>
            <tr>
                <td><?php echo $row[0]; ?></td>
                <td><?php echo $row[1]; ?></td>
                <td><?php echo $row[2]; ?></td>
            </tr>
            <?php } ?>
        </tbody>
    </table>
</body>
</html>
<?php
    pg_free_result($result);
    pg_close($dbconn);
?>
```

### 2.3. Test it
Now, from your workstation's browser, load the page (replace srv with  your server's IP: 

http:/srv/test.php

</details>

