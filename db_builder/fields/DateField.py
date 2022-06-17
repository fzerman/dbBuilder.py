from ..db_fields import DB_Field
from datetime import datetime,date


class DateField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "varchar(64)"

    def is_valid(self):
        if self.get_kwarg("auto_now") == True:
            return True    
        elif type(self.get_kwarg("value")).__name__ == "datetime":
            return True
        return False

    def db_value(self):
        if self.is_valid():
            if self.get_kwarg("auto_now") != True:
                return self.get_kwarg("value")

            now = datetime.now()
            return date(now.year,now.month,now.day).isoformat()
        return False

    def get_value(self,value):
        pass