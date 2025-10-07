import mysql.connector as MyConn
mydb=MyConn.connect(host="localhost",user="root", password="root", database="learn_coding")

db_cursor=mydb.cursor()

db_cursor.execute("select * from Emp")

# db_select=db_cursor.fetchall()

# for i in db_select:
#   print(i)

#print(db_select)

for db_select in db_cursor.fetchall():
  print(db_select)
