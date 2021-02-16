from ..db_fields import DB_Field

class FloatField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "REAL"

    def is_valid(self):
        if isinstance( self.get_kwarg("value"), float):
            return True
        return False

    def db_value(self):
        if self.is_valid():
            return self.get_kwarg("value") 
        return False

    def get_value(self,value):
        pass