from flask import Flask, request


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
@app.get("/store")
def get_all_stores():
    return {"stores": stores}

# Get a particular store
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

# Get items in store
@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

# Create store
@app.post("/store")
def create_store():
    request_store = request.get_json()
    new_store = {"name": request_store["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

# Create item
# {"name": "Chair", "price": 175.50}
@app.post("/store/<string:name>/item")
def create_item(name):
    request_item = request.get_json()
    if not all(field in request_item for field in ("name", "price")):
        return {"message": "Missing required fields"}, 400
    try:
        store = next(store for store in stores if store["name"] == name)
    except StopIteration:
        return {"message": "Store not found"}, 404
    if not isinstance(request_item["price"], (int, float)) or request_item["price"] < 0:
        return {"message": "Price must be a positive number"}, 400
    new_item = {"name": request_item["name"], "price": request_item["price"]}
    store["items"].append(new_item)
    return new_item, 201
   