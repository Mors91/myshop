import pymysql

# Initialize empty html string
htmlString = ""

# Create an HTML HEAD
def headhtml():
    return "<!DOCTYPE html><html lang=\"en\"><head>\n<title>owner of Pets</title></head>\n<body>"

# Create an HTML footer
def foothtml():
    return "</body>\n</html>"

# Query the database for owner
def ownerquery():
    print("start")
    db = pymysql.connect(host="localhost", user="root", passwd="U2gtza(6xOND4GfO", db="test_db")
    cursor = db.cursor()
    sql = "SELECT * FROM owner;"
    cursor.execute(sql)
    owner = cursor.fetchall()
    sql = "SELECT column_name from information_schema.COLUMNS where TABLE_NAME='owner';"
    cursor.execute(sql)
    columns = cursor.fetchall()
    print(columns)
    return owner, columns

# Create HTML table for owner
def ownerTable(owner_list, column_names):
    html = "<table border='1'><tr>"
    for name in column_names:
        html += "<th>" + name[0] + "</th>"
    html += "</tr>"
    for owner in owner_list:
        html += "<tr>"
        for data in owner:
            html += "<td>{0}</td>".format(data)
        html += "</tr>"
    html += "</table>"
    return html

# Query the database for pets
def petquery():
    db = pymysql.connect(host="localhost", user="root", passwd="U2gtza(6xOND4GfO", db="test_db")
    cursor = db.cursor()
    sql = "SELECT * FROM pets;"
    cursor.execute(sql)
    pets = cursor.fetchall()
    sql = "SELECT column_name from information_schema.COLUMNS where TABLE_NAME='pets';"
    cursor.execute(sql)
    columns = cursor.fetchall()
    print(columns)
    return pets, columns

# Create HTML table for pets
def petsTable(pets_list, column_names):
    html = "<table border='1'><tr>"
    for name in column_names:
        html += "<th>" + name[0] + "</th>"
    html += "</tr>"
    for pet in pets_list:
        html += "<tr>"
        for data in pet:
            html += "<td>{0}</td>".format(data)
        html += "</tr>"
    html += "</table>"
    return html

if __name__ == '__main__':
    htmlString += headhtml()
    owner, headers = ownerquery()
    htmlString += ownerTable(owner, headers)
    pets, headers = petquery()
    htmlString += petsTable(pets, headers)
    htmlString += foothtml()
    # Write to file
    with open('rendering.html', 'w') as outf:
        outf.write(htmlString)
