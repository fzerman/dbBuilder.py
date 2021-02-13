from ..db_fields import DB_Field

class BoolField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INT"
        self.value = 0

    def db_value(self):
        if self.is_valid():
            if(self.value == True):
                return 1
            else:
                return 0
        return False
        
    def is_valid(self):
        if self.value in [True,False]:
            return True
        return False
    
    def get_value(self,value):
        if(value == 1):
            return True
        return False