from crypt import methods
from dataclasses import dataclass
from flask import Flask, request
import mysql.connector
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)
db_rid_of = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_NAME")
)
itemcursor = db_rid_of.cursor(dictionary=True)


@app.route("/items/<item_id>", methods=["GET"])
def get_item(item_id):
    itemId = item_id
    item_request = f"SELECT * FROM items INNER JOIN cats ON items.cats_id = cats.id WHERE items.id ='{itemId}'"
    itemcursor.execute(item_request)
    data = itemcursor.fetchall()
    return json.dumps({"data": data})

@app.route("/items", methods=["GET"])
def get_all_items():
    item_request = f"SELECT * FROM items INNER JOIN cats ON items.cats_id = cats.id"
    itemcursor.execute(item_request)
    data = itemcursor.fetchall()
    return json.dumps({"data": data})
    

@app.route("/items", methods=["POST"])
def get_items():
    data = request.json
    items_to_search = data["data"]
    names = f"name = '{items_to_search[0]}'"
    i = 0
    for item in items_to_search:
        if i > 0:
            names += f" OR name = '{item}'"
        i += 1
    item_request = "SELECT * FROM items INNER JOIN cats ON items.cats_id = cats.id WHERE " + names
    print(item_request)
    itemcursor.execute(item_request)
    data = itemcursor.fetchall()
    return json.dumps({"data": data})


@app.route('/')
def hello():
    return 'Hello, World!'