from flask import Flask, request, jsonify
from flask_smorest import abort
from http import HTTPStatus
from db import items, stores
import logging
import uuid


logging.basicConfig(filename="store_api.log", level=logging.DEBUG)

app = Flask(__name__)

# Create a store
# Body: {"name": "My Store 2"}
@app.post("/store")
def create_store():
    app.logger.debug("Creating new store")
    request_store = request.get_json()
    if not ("name" in request_store):
        app.logger.error("Missing store name.")
        abort(HTTPStatus.BAD_REQUEST, message="Missing store name.")
    if not isinstance(request_store["name"], (str)) or len(request_store["name"]) == 0:
        app.logger.error("Store name must be a non-empty string.")
        abort(HTTPStatus.BAD_REQUEST,
              message="Store name must be a non-empty string.")
    store_id = uuid.uuid4().hex
    new_store = {**request_store, "id": store_id}
    stores[store_id] = new_store
    app.logger.debug(f"Store '{new_store}' created")
    return jsonify(new_store), HTTPStatus.CREATED


# Get a store
@app.get("/store/<string:store_id>")
def get_store(store_id):
    app.logger.debug(f"Retrieving store '{store_id}'")
    try:
        store = stores[store_id]
    except KeyError:
        app.logger.error(f"Store '{store_id}' not found.")
        abort(HTTPStatus.NOT_FOUND, message="Store id not found.")
    return jsonify(store)


# Get all stores
@app.get("/store")
def get_all_stores():
    app.logger.debug("Retrieving and returning all stores")
    return jsonify({"stores": list(stores.values())})


# Delete a store
@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    app.logger.debug(f"Deleting store '{store_id}'.")
    try:
       del stores[store_id]
       app.logger.debug(f"Store '{store_id}' deleted.")
       return jsonify({"message": "Store deleted."}) 
    except KeyError:
        app.logger.error(f"Store '{store_id}' not found.")
        abort(HTTPStatus.NOT_FOUND, message="Store id not found.")


# Create item
# Body: {"store_id": "123", name": "Chair", "price": 175.50}
@app.post("/item")
def create_item():
    app.logger.debug(f"Creating new item.")
    request_item = request.get_json()
    if not all(field in request_item for field in ("store_id", "name", "price")):
        app.logger.error(
            "Missing required field from store_id, name and price.")
        abort(HTTPStatus.BAD_REQUEST,
              message="Missing required field from store_id, name and price.")
        
    if request_item["store_id"] not in stores:
        app.logger.error(f"Store not found.")
        abort(HTTPStatus.NOT_FOUND, message="Store not found.")

    if not isinstance(request_item["price"], (int, float)) or request_item["price"] < 0:
        app.logger.error("Price must be a positive number.")
        abort(HTTPStatus.BAD_REQUEST, message="Price must be a positive number.")

    item_id = uuid.uuid4().hex
    items[item_id] = {**request_item, "id": item_id}
    store_name = stores[request_item["store_id"]]["name"]
    app.logger.debug(
        f"Item '{items[item_id]}' created for store '{store_name}'")
    return jsonify(items[item_id]), HTTPStatus.CREATED


# Retrieve a particular item
@app.get("/item/<string:item_id>")
def get_item(item_id):
    app.logger.debug(f"Retrieving item '{item_id}'")
    try:
        item = items[item_id]
    except KeyError:
        app.logger.error(f"Item '{item_id}' not found.")
        abort(HTTPStatus.NOT_FOUND, message="Item id not found.")
    return jsonify(item)


# Retrieve all items
@app.get("/item")
def get_all_items():
    app.logger.debug("Retrieving and returning all items")
    return jsonify({"items": list(items.values())})


# Update item.
# Body: {name": "Chair", "price": 175.50}
@app.put("/item/<string:item_id>")
def update_item(item_id):
    app.logger.debug(f"Updating item '{item_id}'.")
    request_item = request.get_json()
    if not all(field in request_item for field in ("name", "price")):
        app.logger.error(
            "Missing required field from name and price.")
        abort(HTTPStatus.BAD_REQUEST,
              message="Missing required field from name and price.")
    if not isinstance(request_item["price"], (int, float)) or request_item["price"] < 0:
        app.logger.error("Price must be a positive number.")
        abort(HTTPStatus.BAD_REQUEST, message="Price must be a positive number.")
    try:
        item = items[item_id]
        # in-place update by merging two dictionaries.
        item |= request_item
    except KeyError:
        abort(HTTPStatus.NOT_FOUND, message="Item id not found.")            
    app.logger.debug(f"Item '{item}' updated.")
    return jsonify(item), HTTPStatus.CREATED


# Delete an item
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    app.logger.debug(f"Deleting item '{item_id}'.")
    try:
       del items[item_id]
       app.logger.debug(f"Item '{item_id}' deleted.")
       return jsonify({"message": "Item deleted."}) 
    except KeyError:
        app.logger.error(f"Item '{item_id}' not found.")
        abort(HTTPStatus.NOT_FOUND, message="Item id not found.")
