from ..db_fields import DB_Field
import time


class TimeField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "varchar(64)"

    def is_valid(self):
        if self.get_kwarg("auto_now") == True:
            return True    
        elif type(self.get_kwarg("value")).__name__ == "struct_time":
            return True
        return False

    def db_value(self):
        if self.is_valid():
            if self.get_kwarg("auto_now") == True:     
                now = time.localtime()
                return f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}" 
            else:
                return self.get_kwarg("value")

        return False

    def get_value(self,value):
        pass