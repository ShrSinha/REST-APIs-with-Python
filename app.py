'''
TODO(shruti)
- Repeated handle_store_not_found
    - Add db
- Add automated testing
'''
from flask import Flask, request, jsonify
from http import HTTPStatus
import logging



logging.basicConfig(filename="store_api.log", level=logging.DEBUG)

app = Flask(__name__)

stores = [
    {
        "name": "My Store", 
        "items": [
                    {
                        "name": "Chair", 
                        "price": 15.99
                    }
                ]
    }
]

# Retrieve all stores and their items
# URL: http://127.0.0.1:5000/store
@app.get("/store")
def get_all_stores():

    app.logger.debug("Retrieving all stores")
    
    return jsonify({"stores": stores})

# Retrieve a particular store (Retrieve the store details of the single given store.)
# URL: http://127.0.0.1:5000/store/My Store
@app.get("/store/<string:name>")
def get_store(name):

    app.logger.debug(f"Retrieving store '{name}'")
    
    try:
        store = next(store for store in stores if store["name"] == name)
    except StopIteration:
        app.logger.error(f"Store '{name}' not found")
        return handle_store_not_found(HTTPStatus.NOT_FOUND)
    
    app.logger.debug(f"Returning store '{name}'")

    return jsonify(store)  

# Retrieve items (Retrieve all items of the single given store.)
# URL: http://127.0.0.1:5000/store/My Store/item
@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    try:
        store = next(store for store in stores if store["name"] == name)
    except StopIteration:
        app.logger.error(f"Store '{name}' not found")
        return handle_store_not_found(HTTPStatus.NOT_FOUND)
    
    app.logger.debug(f"Returning store '{name}'")

    return jsonify({"items": store["items"]})          

# Create store (Create a single new store with no items.)
# URL: http://127.0.0.1:5000/store
# Body: {"name": "My Store 2"}
@app.post("/store")
def create_store():

    app.logger.debug("Creating new store")

    request_store = request.get_json()

    if not ("name" in request_store):
        app.logger.error("Missing required fields")
        return jsonify({"message": "Missing required fields"}), HTTPStatus.BAD_REQUEST
    
    if not isinstance(request_store["name"], (str)) or len(request_store["name"]) == 0:
        app.logger.error("Store name must be a non-empty string")
        return jsonify({"message": "Store name must be a non-empty string"}), HTTPStatus.BAD_REQUEST
    
    new_store = {"name": request_store["name"], "items": []}

    stores.append(new_store)

    app.logger.debug(f"Store '{new_store}' created")
    
    return jsonify(new_store), HTTPStatus.CREATED

# Create item (Create a single new item in the given store.)
# URL: http://127.0.0.1:5000/store/My Store/item
# Body: {"name": "Chair", "price": 175.50}
@app.post("/store/<string:name>/item")
def create_item(name):

    app.logger.debug(f"Creating new item for store '{name}'")

    request_item = request.get_json()
    
    if not all(field in request_item for field in ("name", "price")):
        app.logger.error("Missing required fields")
        return jsonify({"message": "Missing required fields"}), HTTPStatus.BAD_REQUEST
    try:
        store = next(store for store in stores if store["name"] == name)
    except StopIteration:
        app.logger.error(f"Store '{name}' not found")
        return handle_store_not_found(HTTPStatus.NOT_FOUND)
    
    if not isinstance(request_item["price"], (int, float)) or request_item["price"] < 0:
        app.logger.error("Price must be a positive number")
        return jsonify({"message": "Price must be a positive number"}), HTTPStatus.BAD_REQUEST
    
    new_item = {"name": request_item["name"], "price": request_item["price"]}
    
    store["items"].append(new_item)

    app.logger.debug(f"Item '{new_item}' created for store '{name}'")
    
    return jsonify(new_item), HTTPStatus.CREATED 

@app.errorhandler(HTTPStatus.NOT_FOUND)
def handle_store_not_found(error):

    app.logger.error(f"Store not found: {error.description}")
    
    response = jsonify({"message": "This store does not exist. Please review for typos in store name."})
    
    response.headers["Content-Type"] = "application/json"
    
    return response, HTTPStatus.NOT_FOUND