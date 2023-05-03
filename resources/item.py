from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from http import HTTPStatus
from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    # Retrieve a particular item
    @blp.response(HTTPStatus.OK, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    # Update item.
    # Body: {name": "Chair", "price": 175.50}
    @blp.arguments(ItemUpdateSchema)
    @blp.response(HTTPStatus.CREATED, ItemSchema)
    def put(self, request_item, item_id):
        item = ItemModel.query.get(item_id)

        if item:
            item.price = request_item["price"]
            item.name = request_item["name"]
        else:
            item = ItemModel(id=item_id, **request_item)

        db.session.add(item)
        db.session.commit()

        return item

    # Delete an item
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return{"message": "Item deleted."}


@blp.route("/item")
class ItemList(MethodView):
    # Create item
    # Body: {"store_id": "123", name": "Chair", "price": 175.50}
    @blp.arguments(ItemSchema)
    @blp.response(HTTPStatus.CREATED, ItemSchema)
    def post(self, request_item):
        # if request_item["price"] < 0:
        #     abort(HTTPStatus.BAD_REQUEST,
        #           message="Price must be a positive number.")
        # request_item is a dict
        item = ItemModel(**request_item)

        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                HTTPStatus.BAD_REQUEST,
                message="An item with that name already exists.",
            )
        except SQLAlchemyError:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR,
                  message="An error occurred while inserting the item.")

        return item

    # Retrieve all items
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
