from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from http import HTTPStatus
from db import items
import uuid
from schemas import ItemSchema, ItemUpdateSchema



blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    # Retrieve a particular item
    def get(self, item_id):
        try:
            item = items[item_id]
        except KeyError:
            abort(HTTPStatus.NOT_FOUND, message="Item id not found.")
        return jsonify(item)

    # Update item.
    # Body: {name": "Chair", "price": 175.50}
    @blp.arguments(ItemUpdateSchema)
    def put(self, request_item, item_id):
        if request_item["price"] < 0:
            abort(HTTPStatus.BAD_REQUEST,
                  message="Price must be a positive number.")

        try:
            item = items[item_id]
            # in-place update by merging two dictionaries.
            item |= request_item
        except KeyError:
            abort(HTTPStatus.NOT_FOUND, message="Item id not found.")

        return jsonify(item), HTTPStatus.CREATED

    # Delete an item
    def delete(self, item_id):
        try:
            del items[item_id]
            return jsonify({"message": "Item deleted."})
        except KeyError:
            abort(HTTPStatus.NOT_FOUND, message="Item id not found.")


@blp.route("/item")
class ItemList(MethodView):
    # Create item
    # Body: {"store_id": "123", name": "Chair", "price": 175.50}
    @blp.arguments(ItemSchema)
    def post(self, request_item):
        # if request_item["store_id"] not in stores:
        #     app.logger.error(f"Store not found.")
        #     abort(HTTPStatus.NOT_FOUND, message="Store not found.")

        if request_item["price"] < 0:
            abort(HTTPStatus.BAD_REQUEST,
                  message="Price must be a positive number.")

        item_id = uuid.uuid4().hex
        items[item_id] = {**request_item, "id": item_id}
        return jsonify(items[item_id]), HTTPStatus.CREATED

    # Retrieve all items
    def get(self):
        return jsonify({"items": list(items.values())})
