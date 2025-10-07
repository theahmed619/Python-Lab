import mysql.connector as MyConn

mydb = MyConn.connect(
    host="localhost",
    user="root",
    password="root",
    database="learn_coding"
)

db_cursor = mydb.cursor()

db_update = "UPDATE Emp SET name=%s WHERE id=%s"
db_value = ("rohit", 50)  # Correct order

db_cursor.execute(db_update, db_value)
mydb.commit()

print(db_cursor.rowcount, "Done")
