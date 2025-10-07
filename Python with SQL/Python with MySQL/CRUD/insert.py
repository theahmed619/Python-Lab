import mysql.connector as MyConn
mydb=MyConn.connect(host="localhost",user="root", password="root", database="learn_coding")

db_cursor=mydb.cursor()
db_insert="insert into Emp(id,name) values(%s,%s)"
db_list=[(30, "AK"),(40,"Joe"),(50,"Ro")]
db_cursor.executemany(db_insert,db_list)

db_cursor.execute("insert into emp(id,name) values (%s,%s)", (10,"Aj"))
mydb.commit()
print(db_cursor.rowcount,"Record Inserted")

