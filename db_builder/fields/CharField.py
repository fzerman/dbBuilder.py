from ..db_fields import DB_Field

class CharField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        if(self.get_kwarg("length")):
            self.field_type = "varchar("+str(self.get_kwarg("length"))+")"
        else:
            self.field_type = "varchar(64)"