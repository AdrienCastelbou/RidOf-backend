import mysql.connector

mydb = mysql.connector.connect(
  host="45.63.119.169",
  user="python",
  password="password",
  database="ridof"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM items WHERE name ='phone'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
