# REST-APIs-with-Python

**Store REST API** using Flask (with extensions Flask-Smorest, Flask-JWT-Extended, and Flask-SQLAlchemy ) and Docker. 


## API Documentation

Here is the [OpenAPI Documentation of the Store REST API](OpenAPI.json)

Few example OpenAPI endpoints documentation images from `http://localhost:5005/swagger-ui` :-

[Endponints of the Store REST API](OpenAPIEndpoints.png)

[Schema of the Store REST API](OpenAPISchema.png)


## Tech Stack 

Application has -
- Flask-Smorest web development framework.
- SQLAlchemy ORM library with SQLite relational database. Flask-SQLAlchemy extension to connect SQLAlchemy to Flask apps.
- Flask-Migrate to keep SQLAlchemy models and database table definitions in sync.
- Docker deployment.
- OpenAPI documentation.
- Data Quality checks for requests and responses with Marshmallow. 
- API testing using Insomnia.
- System testing for Store endpoints.

Application ToDos -
- User authentication with Flask-JWT-Extendeds.
- Implement a many:many relationship in SQLAlchemy ORM.
- System testing for Item endpoints.
- Automated testing.
