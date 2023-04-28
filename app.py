from flask import Flask, request, jsonify
from http import HTTPStatus


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
]y

# Retrieve all stores and their items
# URL: http://127.0.0.1:5000/store
@app.get("/store")
def get_all_stores():
    return jsonify({"stores": stores})

# Retrieve a particular store (Retrieve the store details of the single given store.)
# URL: http://127.0.0.1:5000/store/My Store
@app.get("/store/<string:name>")
def get_store(name):
    try:
        store = next(store for store in stores if store["name"] == name)
    except StopIteration:
        return handle_store_not_found(HTTPStatus.NOT_FOUND)
    
    return jsonify(store)  

# Retrieve items (Retrieve all items of the single given store.)
# URL: http://127.0.0.1:5000/store/My Store/item
@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})  
    return handle_store_not_found(HTTPStatus.NOT_FOUND)

# Create store (Create a single new store with no items.)
# URL: http://127.0.0.1:5000/store
# Body: {"name": "My Store 2"}
@app.post("/store")
def create_store():

    request_store = request.get_json()

    if not "name" in request_store:
        return jsonify({"message": "Missing required field"}), HTTPStatus.BAD_REQUEST
    
    if not isinstance(request_store["name"], (str)) or len(request_store["name"]) == 0:
        return jsonify({"message": "Store name must be a non-empty string"}), HTTPStatus.BAD_REQUEST
    
    new_store = {"name": request_store["name"], "items": []}

    stores.append(new_store)
    
    return jsonify(new_store), HTTPStatus.CREATED

# Create item (Create a single new item in the given store.)
# URL: http://127.0.0.1:5000/store/My Store/item
# Body: {"name": "Chair", "price": 175.50}
@app.post("/store/<string:name>/item")
def create_item(name):

    request_item = request.get_json()
    
    if not all(field in request_item for field in ("name", "price")):
        return jsonify({"message": "Missing required fields"}), HTTPStatus.BAD_REQUEST
    try:
        store = next(store for store in stores if store["name"] == name)
    except StopIteration:
        return handle_store_not_found(HTTPStatus.NOT_FOUND)
    
    if not isinstance(request_item["price"], (int, float)) or request_item["price"] < 0:
        return jsonify({"message": "Price must be a positive number"}), HTTPStatus.BAD_REQUEST
    
    new_item = {"name": request_item["name"], "price": request_item["price"]}
    
    store["items"].append(new_item)
    
    return jsonify(new_item), HTTPStatus.CREATED 

@app.errorhandler(HTTPStatus.NOT_FOUND)
def handle_store_not_found(error):
    response = jsonify({"message": "This store does not exist. Please review for typos in store name."})
    response.headers["Content-Type"] = "application/json"
    return response, HTTPStatus.NOT_FOUND