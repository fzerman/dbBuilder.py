from ..db_fields import DB_Field

class BoolField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INT"
        self.value = 0

    def get_value(self):
        if self.is_valid():
            if(self.value == 1):
                return True
        return False

    def is_valid(self):
        if self.value in [0,1]:
            return True
        return False