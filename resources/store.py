from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from http import HTTPStatus
from db import stores
import uuid
from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # Get a store
    def get(self, store_id):
        try:
            store = stores[store_id]
        except KeyError:
            abort(HTTPStatus.NOT_FOUND, message="Store id not found.")
        return jsonify(store)

    # Delete a store
    def delete(self, store_id):
        try:
            del stores[store_id]
            return jsonify({"message": "Store deleted."})
        except KeyError:
            abort(HTTPStatus.NOT_FOUND, message="Store id not found.")


@blp.route("/store")
class StoreList(MethodView):
    # Create a store
    # Body: {"name": "My Store 2"}
    @blp.arguments(StoreSchema)
    def post(self, request_store):
        if len(request_store["name"]) == 0:
            abort(HTTPStatus.BAD_REQUEST,
                  message="Store name must be a non-empty string.")

        store_id = uuid.uuid4().hex
        new_store = {**request_store, "id": store_id}
        stores[store_id] = new_store
        return jsonify(new_store), HTTPStatus.CREATED

    # Get all stores
    def get(self):
        return jsonify({"stores": list(stores.values())})
