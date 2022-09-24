from crypt import methods
from dataclasses import dataclass
from flask import Flask, request
import mysql.connector

app = Flask(__name__)
db_rid_of = mysql.connector.connect(
  host="45.63.119.169",
  user="python",
  password="password",
  database="ridof"
)
itemcursor = db_rid_of.cursor(dictionary=True)


@app.route("/items/<item_id>", methods=["GET"])
def get_item(item_id):
    itemId = item_id
    item_request = f"SELECT * FROM items INNER JOIN cats ON items.cats_id = cats.id WHERE items.id ='{itemId}'"
    itemcursor.execute(item_request)
    return itemcursor.fetchall()


@app.route("/items", methods=["POST"])
def get_items():
    data = request.json
    items_to_search = data["data"]
    
    response = []
    for item in items_to_search:
        print(item)
        item_request = f"SELECT * FROM items INNER JOIN cats ON items.cats_id = cats.id WHERE name ='{item}'"
        itemcursor.execute(item_request)
        response.append(itemcursor.fetchall())
    return response


@app.route('/')
def hello():
    return 'Hello, World!'