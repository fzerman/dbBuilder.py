from ..db_fields import DB_Field

class BoolField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INT"
        self.value = 0

    def render(self):
        if self.control():
            if(self.value == 1):
                return True
        return False

    def control(self):
        if self.value in [0,1]:
            return True
        return False