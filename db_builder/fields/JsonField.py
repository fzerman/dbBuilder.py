import json
from ..db_fields import DB_Field

class JsonField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "TEXT"

    def is_valid(self):
        if type(self.get_kwarg("value")).__name__ == "dict" or type(self.get_kwarg("value")).__name__ == "list":
            return True
        return False

    def db_value(self):
        if self.is_valid():
            return json.dumps( self.get_kwarg("value"))
        return False
