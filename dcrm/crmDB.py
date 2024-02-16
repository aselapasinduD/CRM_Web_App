import mysql.connector

# Connect Database
dataBase = mysql.connector.connect(
    host = 'localhost',
    port = 3336,
    user = 'root',
    password = 'root'
)

# prepare a cousor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute('CREATE DATABASE crmsystemDB')

print("All Done!")