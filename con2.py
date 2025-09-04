import mysql.connector
import sys
import getpass


# DB class to connect and perform different CURD operations on mysql database

class DB:
    def __init__(self,user,password):
        self.state = 0
        self.actions = ["list db's","create db","drop db","select db","list tables","create table","alter table","drop table","read table","insert record","update record","delete record","describe_table","custom"]
        self.map = {1:self.show_databases,2:self.create_db,3:self.drop_db,4:self.select_db,5:self.show_tables,6:self.create_table,7:self.alter_table,8:self.drop_table,9:self.read_table,10:self.insert_record,11:self.update_record,12:self.delete_record,13:self.desc_table,14:self.custom_query}
        try:
            self.cnx = mysql.connector.connect(user = user, password = password,host = 'localhost',buffered = True) # connecting to database
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as e:
            s = str(e)
            print("Error:",s)
            sys.exit()

    def get_func(self,id):
        return self.map[id]             # returns a mapping function for appropriate choice 

    def custom_query(self,s):           # functions which executes a query s
        try:
            self.cursor.execute(s)
            self.cnx.commit()
            try:
                for tables in self.cursor:
                    print(tables)
            except:
                pass
        except mysql.connector.Error as e:
            s = str(e)
            print("Error:",s)

    def show_databases(self):
        s = "SHOW databases"
        self.custom_query(s)

    def create_db(self):
        name = input("db name:")
        s = "create database "+name
        print(s)
        self.custom_query(s)
    
    def drop_db(self):
        name = input("db name:")
        s = "drop database "+name
        self.custom_query(s)
    
    def select_db(self):
        name = input("db name:")
        s = "use "+name
        self.custom_query(s)

    def show_tables(self):
        s = "show tables"
        self.custom_query(s)

    def create_table(self):
        name = input("table name:")
        values = input("enter values:")
        q = "create table "+name+" ("+values+")"
        self.custom_query(q)

    def alter_table(self):
        q = input("Enter Query:")
        self.custom_query(q)

    def drop_table(self):
        name = input("table name:")
        s = "drop table "+name
        self.custom_query(s)

    def read_table(self):
        name = input("table name:")
        s = "select * from "+name
        self.custom_query(s)

    def insert_record(self):
        name = input("table name:")
        values=input("enter values:")
        q = "insert into "+name+" values("+values+")"
        self.custom_query(q)

    def update_record(self):
        name = input("table name:")
        values = input("Enter updated values:")
        where = input("where:")
        q = "update "+name+" set "+values+" where "+where
        self.custom_query(q)

    def delete_record(self):
        name = input("table name:")
        where = input("where:")
        if where:
            q = "delete from "+name+" where "+where
        else:
            q = "delete from "+name
        self.custom_query(q)

    def desc_table(self):
        name = input("table name:")
        q = "desc "+name
        self.custom_query(q)

def main():
    usr = input("Enter user:")      # username and password to connect to mysql database
    pwd = getpass.getpass()         
    db = DB(usr,pwd)                # intializing DB connection object
    while(1):
        print("\n")
        print("******************************************************************")
        # print options
        for i in range(len(db.actions)):
            print(i+1,":",db.actions[i], "      ",end = '')
            if (i+1)%4 == 0:
                print("\n",end = '')
        print("\n")
        op = input("Choose a valid action[or Enter 0 to exit]:")
        if op == '0':
            break
        try:
            if int(op) < 1 or int(op) > 14:          # validate the input
                continue
        except:
            continue
        if int(op) == 14:
            query = input("Enter a valid query[or Enter 0 to exit]:")
            if query == '0':
                break
            else:
                db.get_func(int(op))(query)
        else:
            db.get_func(int(op))()
    db.cnx.close()

main()