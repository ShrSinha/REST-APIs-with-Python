import logging
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from http import HTTPStatus
from db import db
from models import StoreModel
import uuid
from schemas import StoreSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


blp = Blueprint("stores", __name__, description="Operations on stores")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("store.log")
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # Get a store
    @blp.response(HTTPStatus.OK, StoreSchema)
    def get(self, store_id):
        logger.info(f"Get store: {store_id}.")
        store = StoreModel.query.get_or_404(store_id)
        return store

    # Delete a store
    def delete(self, store_id):
        logger.info(f"Delete store: {store_id}.")
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted."}


@blp.route("/store")
class StoreList(MethodView):
    # Create a store
    # Body: {"name": "My Store 2"}
    @blp.arguments(StoreSchema)
    @blp.response(HTTPStatus.CREATED, StoreSchema)
    def post(self, request_store):
        logger.info(f"Create store: {request_store}.")
        store = StoreModel(**request_store)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                HTTPStatus.BAD_REQUEST,
                message="A store with that name already exists.",
            )
        except SQLAlchemyError:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR,
                  message="An error occurred creating the store.")

        return store

    # Get all stores
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        logger.info(f"Get all stores.")
        return StoreModel.query.all()
