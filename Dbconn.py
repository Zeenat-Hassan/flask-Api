import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="ToDo"
)
mycursor = mydb.cursor()
#create a new to-do

# sql = "INSERT INTO Tasks (text,status) VALUES (%s, %s)"
# val = ("second to do ", "Incomplete")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "to do  inserted.")


#update a to-do
# sql = "UPDATE Tasks SET status = 'Complete' WHERE id = '2'"
#
# mycursor.execute(sql)
#
# mydb.commit()

#deleting a to-do
# sql = "DELETE FROM Tasks WHERE id = '1'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) deleted")

#read a to do

mycursor.execute("SELECT text, status FROM Tasks")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)