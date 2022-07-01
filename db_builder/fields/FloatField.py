from ..db_fields import DB_Field

class FloatField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "REAL"

    def is_valid(self):
        return bool(
            isinstance(self.get_kwarg("value"), float)
            and self.get_validators_result()
        )

    def db_value(self):
        return self.get_kwarg("value") if self.is_valid() else False

    def get_value(self,value):
        pass