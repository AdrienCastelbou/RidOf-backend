#imports
import mysql.connector

#connect to sql server
db_rid_of = mysql.connector.connect(
  host="45.63.119.169",
  user="python",
  password="password",
  database="ridof"
)

#example search
search_input = ["phone"]

#count input lenght
search_count = len(search_input)

#if there is no input
if search_count <= 0:
    print("No Input.")
    exit()

#item requests for every input made
itemcursor = db_rid_of.cursor()
item_request = f"SELECT * FROM items WHERE name ='{search_input[0]}'"
itemcursor.execute(item_request)
item_search_result = itemcursor.fetchall()

#category request
catcursor = db_rid_of.cursor()
cat_request = f"SELECT * FROM cats WHERE id ='{item_search_result[0][3]}'"
catcursor.execute(cat_request)
cat_search_result = catcursor.fetchall()

#print all items
for x in item_search_result:
    print(x)

#print all category
for y in cat_search_result:
    print(y)

#ToDo: multiple searches 