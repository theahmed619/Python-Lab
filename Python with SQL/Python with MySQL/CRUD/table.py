import mysql.connector as MyConn
mydb=MyConn.connect(host="localhost",user="root", password="root", database="learn_coding")

db_cursor=mydb.cursor()

#db_cursor.execute("create table Emp(id int, name varchar(255))")
db_cursor.execute("show tables")

for i in db_cursor:
  print(i)
