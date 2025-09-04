# Importing module 
import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tinku@143"
)
 
# Printing the connection object 
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")