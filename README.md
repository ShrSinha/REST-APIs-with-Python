# REST-APIs-with-Python

The **Stores REST API** provides endpoints for managing stores and items in a store. 

It's built using Flask (with extensions Flask-Smorest, Flask-JWT-Extended, and Flask-SQLAlchemy ) and Docker. 


## API Documentation

Here is the [OpenAPI Documentation of the Store REST API](OpenAPI.json)

### Authentication

This API does not require authentication.

### Endpoints

#### 1) Retrieve a Store

Retrieve a single store by its ID.

**Request**

```
GET /store/{store_id}
```

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| store_id | path | string | yes | The ID of the store to retrieve. |

**Response**

| HTTP Code | Description | Response Body |
| --- | --- | --- |
| 200 | Store retrieved successfully. | [Store](#store) |
| default | An error occurred. | [Error](#error) |


#### 2) Retrieve All Stores

Retrieve a list of all stores.

**Request**

```
GET /store
```

**Response**

| HTTP Code | Description | Response Body |
| --- | --- | --- |
| 200 | Stores retrieved successfully. | [Store[]](#store) |
| default | An error occurred. | [Error](#error) |


#### 3) Create a Store

Create a new store.

**Request**

```
POST /store
```

**Request Body**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Store | [Store](#store) | yes | The details of the store to create. |

**Response**

| HTTP Code | Description | Response Body |
| --- | --- | --- |
| 201 | Store created successfully. | [Store](#store) |
| 422 | Invalid input. | [Error](#error) |
| default | An error occurred. | [Error](#error) |


#### 4) Delete a Store

Delete a store by its ID.

**Request**

```
DELETE /store/{store_id}
```

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| store_id | path | string | yes | The ID of the store to delete. |

**Response**

| HTTP Code | Description | Response Body |
| --- | --- | --- |
| default | An error occurred. | [Error](#error) |


#### 5) Retrieve an Item

Retrieve a single item by its ID.

**Request**

```
GET /item/{item_id}
```

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | path | string | yes | The ID of the item to retrieve. |

**Response**

| HTTP Code | Description | Response Body |
| --- | --- | --- |
| 200 | Item retrieved successfully. | [Item](#item) |
| default | An error occurred. | [Error](#error) |


#### 6) Retrieve All Items

Retrieve a list of all items.

**Request**

```
GET /item
```

**Response**

| HTTP Code | Description | Response Body |
| --- | --- | --- |
| 200 | Items retrieved successfully. | [Item[]](#item) |
| default | An error occurred. | [Error](#error) |


#### 7)  Create an Item

Create a new item.

**Request**

```
POST /item
```

**Request Body**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Item | [Item](#item) | yes | The details of the item to create. |




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
