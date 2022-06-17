import json
from ..db_fields import DB_Field

class JsonField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "TEXT"

    def is_valid(self):
        return bool(
            type(self.get_kwarg("value")).__name__ == "dict"
            or type(self.get_kwarg("value")).__name__ == "list"
            and self.get_validators_result()
        )

    # value that send to db
    def db_value(self):
        return json.dumps( self.get_kwarg("value")) if self.is_valid() else False

    # value that get from db
    def get_value(self,value):
        return json.loads(value)