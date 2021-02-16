from ..db_fields import DB_Field

class IDField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INTEGER"
        self.kwargs["primary"] = True
        self.kwargs["auto_inc"] = True
