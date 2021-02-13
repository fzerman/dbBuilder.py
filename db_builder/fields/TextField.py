from ..db_fields import DB_Field

class TextField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "TEXT"

    def is_valid(self):
        return True

    def get_value(self):
        if self.is_valid():
            return self.get_kwarg("value")
        return False