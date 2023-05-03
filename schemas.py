from marshmallow import Schema, fields, validate

# Create item
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

# Update item
class ItemUpdateSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    price = fields.Float(validate=validate.Range(min=0))

# Create store
class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

