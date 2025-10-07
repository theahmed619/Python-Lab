import mysql.connector as MyConn
mydb=MyConn.connect(host="localhost",user="root", password="root")

print(mydb,"Connection Establish")

