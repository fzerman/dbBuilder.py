from ..db_fields import DB_Field

class BoolField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INT"

    def db_value(self):
        if self.is_valid():
            return 1 if (self.get_kwarg("value") == True) else 0
        return False
        
    def is_valid(self):
        return bool(
            self.get_kwarg("value") in [True, False]
            and self.get_validators_result()
        )
    
    def get_value(self,value):
        return value == 1