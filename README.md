# REST-APIs-with-Python

**Store REST API** using Flask (with extensions Flask-Smorest, Flask-JWT-Extended, and Flask-SQLAlchemy ) and Docker. 

## API Documentation

Following actions and corresponding endpoints are available via the API - 

- Create stores, each with a name and a list of stocked items.

    `POST /store {"name": "My Store"}`

- Create an item within a store, each with a name and a price.

    `POST /store/My Store/item {"name": "Chair", "price": 175.50}`


- Retrieve a list of all stores and their items.

    `GET /store`


- Given its name, retrieve an individual store and all its items.

    `GET /store/My Store`


- Given a store name, retrieve only a list of items within it.

    `GET /store/My Store/item`
