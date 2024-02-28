import pymysql

class Database:
    def __init__(self, databaseName, host, user, password):
        self.n = databaseName
        db = pymysql.connect(host=host, user=user, passwd=password)
        cursor = db.cursor()
        self.cursor = cursor
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(self.n))
        cursor.execute("USE {}".format(self.n))

    def addTable(self, tableName, **columns):
        sql = "CREATE TABLE IF NOT EXISTS " + tableName + " ("
        for c, t in columns.items():
            sql += " {} {}, ".format(c, t)
        sql = sql[:-2] + ");"  # remove the last comma and close bracket.
        self.cursor.execute(sql)

    def addElement(self, tableName, **values):
        columns = ", ".join(values.keys())
        # Convert all values to strings
        value = "', '".join(str(v) for v in values.values())
        sql = "INSERT INTO {} ({}) VALUES ('{}');".format(tableName, columns, value)
        self.cursor.execute(sql)


    def viewTable(self, tableName):
        self.cursor.execute("SELECT * FROM {}".format(tableName))
        print(self.cursor.fetchall())

newdb = Database('myDatabase', 'localhost', 'root', 'U2gtza(6xOND4GfO')
newdb.addTable('students', ID='int NOT NULL AUTO_INCREMENT PRIMARY KEY', First_name='varchar(50)', Last_name='varchar(50)', age='int')
newdb.addElement('students', First_name='Micheal', Last_name='Jackson', age=30)
newdb.addElement('students', First_name='Taylor', Last_name='Swift', age=19)
newdb.viewTable('students')
