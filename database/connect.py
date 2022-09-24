import mysql.connector

mydb = mysql.connector.connect(
  host="45.63.119.169",
  user="python",
  password="password",
  database="ridof"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")


for x in mycursor:
  print(x)
