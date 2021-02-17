from ..db_fields import DB_Field

class BoolField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INT"

    def db_value(self):
        if self.is_valid():
            if(self.get_kwarg("value") == True):
                return 1
            else:
                return 0
        return False
        
    def is_valid(self):
        if self.get_kwarg("value") in [True,False] and self.get_validators_result():
            return True
        return False
    
    def get_value(self,value):
        if(value == 1):
            return True
        return False