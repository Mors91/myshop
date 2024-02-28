#Loading data into a Database with a python script
import pymysql

def load_owners(cursor):
    # Open the owners.txt file to read owner data
    with open("owners.txt") as owners_data:
        # Iterate over each line in the file
        for rowline in owners_data:
            # Split the row into fields
            row = rowline.strip().split(",")
            # SQL query to insert owner data into the owner table
            sql = "INSERT INTO owner (name, gender, phone) VALUES (%s, %s, %s);"
            # Execute the SQL query with the row data
            cursor.execute(sql, row)
    # Retrieve all data from the owner table
    cursor.execute("SELECT * FROM owner;")
    # Print the fetched data
    print(cursor.fetchall())

def load_pets(cursor):
    # Open the pets.txt file to read pet data
    with open("pets.txt") as pet_data:
        # Iterate over each line in the file
        for rowline in pet_data:
            # Split the row into fields
            row = rowline.strip().split(",")
            # SQL query to insert pet data into the pets table
            sql = "INSERT INTO pets (owner_id, name, gender, species, color, age) VALUES ((SELECT id FROM owner WHERE name = %s), %s, %s, %s, %s, %s);"
            # Execute the SQL query with the row data
            cursor.execute(sql, row)

if __name__ == "__main__":
    # Connect to the MySQL server
    db = pymysql.connect(host="localhost", user="root", passwd="U2gtza(6xOND4GfO", db="test_db")
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Call functions to load data into the database
    load_owners(cursor)
    load_pets(cursor)

    # Commit changes to the database
    db.commit()
    # Close the database connection
    db.close()
