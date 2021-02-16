from ..db_fields import DB_Field
from ..validators import EmailValidator


class EmailField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.max_length = 64
        self.field_name = ""
        if(self.get_kwarg("length")):
            self.field_type = "varchar("+str(self.get_kwarg("length"))+")"
            self.max_length = self.get_kwarg("length")
        else:
            self.field_type = "varchar(64)"

    def is_valid(self):
        return EmailValidator(value=self.get_kwarg("value")).check()

    def db_value(self):
        if self.is_valid():
            return self.get_kwarg("value")
        return False

    def get_value(self):
        pass