import mysql.connector

class dataBase:
    def __init__(self, DB):
        self.DB = DB
        
    def show(self):
        DB = []
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nasrul',
        )
        mycursor = mydb.cursor()
        mycursor.execute('show databases')
        for x in mycursor:
            print(x)
            DB.append(x)
        return DB
             
    def create(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nasrul',
        )
        mycursor = mydb.cursor()
        mycursor.execute('create database ' + self.DB)
        
    def showTable(self):
        table = []
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nasrul',
            database=self.DB
        )
        mycursor = mydb.cursor()
        mycursor.execute('show tables')
        for x in mycursor:
            print(x)
            table.append(x)
        return table
    
    
class Table:
    def __init__(self, DB, table):
        self.DB = DB
        self.table = table 
        
    def selectTable(self):
        table = []
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nasrul',
            database=self.DB
        )
        mycursor = mydb.cursor()
        mycursor.execute('select * from ' + self.table)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
            table.append(x)
        return x
    
    def descTable(self):
        table = []
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nasrul',
            database=self.DB
        )
        mycursor = mydb.cursor()
        mycursor.execute('desc '+self.table)
        for x in mycursor:
            print(x)
            table.append(x)
        return table
              
    def search(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nasrul',
            database=self.DB
        )
        mycursor = mydb.cursor()
        Table = self.table
        colm = 'name'
        name = 'dani'
        
        mycursor.execute(f'select * from %s where %s = "%s"' % (Table, colm, name))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        