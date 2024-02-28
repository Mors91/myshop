#Creating a database and table(s)
import pymysql

# Connect to the MySQL server
server = pymysql.connect(host="localhost", user="root", passwd="U2gtza(6xOND4GfO")

# Create a cursor object to interact with the database
cursor = server.cursor()

# Create or use the database 'test_db'
cursor.execute("CREATE DATABASE IF NOT EXISTS `test_db`;")
cursor.execute("USE `test_db`;")

# Create the 'owner' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS `owner` (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(50),
        gender VARCHAR(10),
        phone VARCHAR(15),
        PRIMARY KEY (id)
    );
''')

# Create the 'pets' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS `pets` (
        pet_id INT NOT NULL AUTO_INCREMENT,
        owner_id INT,
        name VARCHAR(30),
        gender VARCHAR(10),
        species VARCHAR(10),
        color VARCHAR(15),
        age INT,
        PRIMARY KEY (pet_id),
        FOREIGN KEY (owner_id) REFERENCES `owner`(id)
    );
''')

# Show the tables in the database
cursor.execute("SHOW TABLES;")
print(cursor.fetchall())

# Commit the changes and close the connection
server.commit()
server.close()