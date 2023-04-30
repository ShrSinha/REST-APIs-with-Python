from flask import Flask, request, jsonify
from http import HTTPStatus
from db import items, stores
import logging
import uuid



logging.basicConfig(filename="store_api.log", level=logging.DEBUG)

app = Flask(__name__)

# Retrieve all stores
# URL: http://127.0.0.1:5000/store
@app.get("/store")
def get_all_stores():
    app.logger.debug("Retrieving and returning all stores")  
    return jsonify({"stores": list(stores.values())})

# Retrieve all items
#  URL: http://127.0.0.1:5000/item
@app.get("/item")
def get_all_items():
    app.logger.debug("Retrieving and returning all items")
    return jsonify({"items": list(items.values())})

# Retrieve a particular store
# URL: http://127.0.0.1:5000/store/fjhh#gh
@app.get("/store/<string:store_id>")
def get_store(store_id):
    app.logger.debug(f"Retrieving store '{store_id}'")   
    try:
        store = stores[store_id]
    except KeyError:
        app.logger.error(f"Store '{store_id}' not found")
        return handle_store_not_found(HTTPStatus.NOT_FOUND)   
    app.logger.debug(f"Returning store '{store_id}'")
    return jsonify(store)  

# Retrieve a particular item
# URL: http://127.0.0.1:5000/item/fjhyrbh#gh
@app.get("/item/<string:item_id>")
def get_item(item_id):
    app.logger.debug(f"Retrieving item '{item_id}'")
    try:
        item = items[item_id]
    except KeyError:
        app.logger.error(f"Item '{item_id}' not found")
        return jsonify({"message": "Item id not found"}), HTTPStatus.BAD_REQUEST
    return  jsonify(item)          

# Create store (Create a single new store with no items.)
# URL: http://127.0.0.1:5000/store
# Body: {"name": "My Store 2"}
@app.post("/store")
def create_store():
    app.logger.debug("Creating new store")
    request_store = request.get_json()
    if not ("name" in request_store):
        app.logger.error("Missing required field")
        return jsonify({"message": "Missing required field"}), HTTPStatus.BAD_REQUEST  
    if not isinstance(request_store["name"], (str)) or len(request_store["name"]) == 0:
        app.logger.error("Store name must be a non-empty string")
        return jsonify({"message": "Store name must be a non-empty string"}), HTTPStatus.BAD_REQUEST   
    store_id = uuid.uuid4().hex
    new_store = {**request_store, "id": store_id} 
    stores[store_id] = new_store 
    app.logger.debug(f"Store '{new_store}' created")   
    return jsonify(new_store), HTTPStatus.CREATED

# Create item (Create a single new item in the given store.)
# URL: http://127.0.0.1:5000/item
# Body: {"store_id": "123", name": "Chair", "price": 175.50}
@app.post("/store/item")
def create_item(name):
    app.logger.debug(f"Creating new item")
    request_item = request.get_json() 
    if not all(field in request_item for field in ("store_id", "name", "price")):
        app.logger.error("Missing required fields")
        return jsonify({"message": "Missing required fields"}), HTTPStatus.BAD_REQUEST
    if request_item["store_id"] not in stores:
        return handle_store_not_found(HTTPStatus.NOT_FOUND)
    if not isinstance(request_item["price"], (int, float)) or request_item["price"] < 0:
        app.logger.error("Price must be a positive number")
        return jsonify({"message": "Price must be a positive number"}), HTTPStatus.BAD_REQUEST   
    item_id = uuid.uuid4.hex()
    items[item_id] = {**request_item}
    store_name = stores[request_item["store_id"]]["name"]
    app.logger.debug(f"Item '{items[item_id]}' created for store '{store_name}'")   
    return jsonify(items[item_id]), HTTPStatus.CREATED 

@app.errorhandler(HTTPStatus.NOT_FOUND)
def handle_store_not_found(error):
    app.logger.error(f"Store not found: {error.description}")  
    response = jsonify({"message": "This store does not exist."})   
    response.headers["Content-Type"] = "application/json"   
    return response, HTTPStatus.NOT_FOUND