from ..db_fields import DB_Field

class IntField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "INT"