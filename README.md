# REST-APIs-with-Python

**Store REST API** using Flask (with extensions Flask-Smorest, Flask-JWT-Extended, and Flask-SQLAlchemy ) and Docker. The API is production quality and has a straighforward documentation.

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


## Production Quality

Application has -
- Flask-Smorest web development framework.
- SQLAlchemy ORM library with SQLite relational database. Flask-SQLAlchemy extension to connect SQLAlchemy to Flask apps.
- Flask-Migrate to keep model and table definitions in sync.
- Docker deployment.
- OpenAPI documentation.
- Data Quality checks for requests and responses with Marshmallow. 

Application ToDos -
- Fully automate the API lifecycle for CI/CD integrations.
- User authentication with Flask-JWT-Extendeds.

