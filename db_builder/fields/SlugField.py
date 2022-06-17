from ..db_fields import DB_Field
from ..validators.LengthValidator import LengthValidator
from slugify import slugify

class SlugField(DB_Field):
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
        return LengthValidator(value=self.get_kwarg("value"),length=self.max_length).check() and self.get_validators_result()

    def db_value(self):
        return slugify( self.get_kwarg("value") ) if self.is_valid() else False

    def get_value(self,value):
        pass