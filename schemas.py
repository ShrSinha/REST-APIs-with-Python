from marshmallow import Schema, fields

# Create item
class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

# Update item
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

# Create store
class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)