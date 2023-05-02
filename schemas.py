from marshmallow import Schema, fields

# Create item
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

# Update item
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

# Create store
class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class ItemSchema(Schema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(Schema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
