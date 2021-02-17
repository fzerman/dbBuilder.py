from urllib.request import urlopen
from ..db_fields import DB_Field
from ..validators.LengthValidator import LengthValidator

def is_valid_url(url):
    try:
        urlopen(url)
        return True
    except Exception:
        return False

class URLField(DB_Field):
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
        return is_valid_url(self.get_kwarg("value")) and LengthValidator(value=self.get_kwarg("value"),length=self.max_length).check() and self.get_validators_result()

    def db_value(self):
        if self.is_valid():
            return slugify( self.get_kwarg("value") )
        return False

    def get_value(self,value):
        pass