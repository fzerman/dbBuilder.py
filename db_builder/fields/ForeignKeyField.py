from ..db_fields import DB_Field
from ..errors import FieldError
import inspect
 
class ForeignKeyField(DB_Field):
    def __init__(self,foreign_obj,**kwargs):
        self.kwargs = kwargs
        self.max_length = 64
        self.field_name = ""
        self.field_type = "INT"

        if inspect.isclass(foreign_obj):
            self.kwargs["foreign"] = str(foreign_obj.__name__)
        elif type(foreign_obj).__name__ == "str":
            self.kwargs["foreign"] = foreign_obj
        else:
            raise FieldError("","ForeignKeyField","Foreign Object is not declared!")

    def is_valid(self):
        return self.get_foreign() is not None and self.get_validators_result()

    def db_value(self):
        if self.is_valid():
            if inspect.isclass(self.get_kwarg("value")):
                if self.get_kwarg("value").id:
                    return self.get_kwarg("value").id
                else:
                    return FieldError("",self.field_name,"This Foreign Object is not recorded!")
            elif type(self.get_kwarg("value")).__name__ in ["str","int"]:
                return self.get_kwarg("value")

            else:
                raise FieldError("",self.field_name,"Foreign Key value is not object, int or str!")

        raise FieldError("",self.field_name,"Foreign Key value is not valid!")

    def get_value(self,value):
        pass