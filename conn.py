import mysql.connector
conn = mysql.connector.connect (user='root', password='Tinku@143',
                               host='localhost',buffered=True)
cursor = conn.cursor()
# databases = ("show databases")
# cursor.execute(databases)
# for (databases) in cursor:
#      print(databases[0])

# create = ("CREATE DATABASE mydatabase")
# cursor.execute(create)

databases = "show databases"
cursor.execute(databases)
print(type(cursor))
for databases in cursor:
     print(databases[0])