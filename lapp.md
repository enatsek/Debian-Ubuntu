##### LAPP Stack 
# Installing LAPP Stack On Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>

---

### 0.1. The What

The LAPP stack is another popular open-source web development platform. The acronym stands for:

- **L**inux (the operating system)
- **A**pache (the web server)
- **P**ostgreSQL (the database management system)
- **P**HP/Perl/Python (the programming language for application logic)

It provides a robust foundation for building and hosting dynamic websites and web applications.

In this guide, we will use **PHP** as our server-side scripting language.

### 0.2. Environment

- **Server Distribution:** Debian 12/13 or Ubuntu 22.04/24.04 LTS Server

### 0.3. Sources

- [stackoverflow.com](https://stackoverflow.com/questions/49157928/how-to-fetch-data-from-postgresql-using-php)

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

Install PostgreSQL:

```
sudo apt install --yes postgresql
```

Install PHP along with the necessary modules for Apache and Postgresql integration:

```
sudo apt install --yes php libapache2-mod-php php-pgsql
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
2. Test LAPP Stack
</summary>

---

We will create a test database, add a table with sample data, and then create a PHP script to retrieve this data and display it in a web page.

### 2.1. Database Operations

Create a test PostgreSQL user with a password:

```
sudo -u postgres createuser --pwprompt testuser
```

Create a test database:

```
sudo -u postgres createdb testdb
```

Connect to the PostgreSQL shell:

```
sudo -u postgres psql testdb
```

Create a table, populate it with data, and grant the test user access permissions.

Enter PostgreSQL shell:

```
sudo -u postgres psql testdb
```

**Run the following commands in the PostgreSQL shell:**

```
CREATE TABLE Employees (Name char(15), Age int, Occupation char(15));
INSERT INTO Employees VALUES ('Joe Smith', '26', 'Ninja');
INSERT INTO Employees VALUES ('John Doe', '33', 'Sleeper');
INSERT INTO Employees VALUES ('PostgreSQL', '14', 'RDBMS');
GRANT SELECT ON ALL TABLES IN SCHEMA public TO testuser;
\q
```
 
### 2.2. Create a Test PHP File

Create a new PHP file in the web server's root directory:

```
sudo nano /var/www/html/test.php
```

Copy and paste the following content into the file. **Replace `'password'` with the actual password you set for `testuser`:**

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

### 2.3. Test the Setup

Open a web browser on your workstation and navigate to the following URL, replacing `srv` with your server's IP address or hostname:

`http://srv/test.php`

You should see a table displaying the data from the `Employees` table.

</details>




