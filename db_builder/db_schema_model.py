# Future feature
from db_builder.db_model import DB_Model
from db_builder.fields import *

class INFO_SCHEMA(DB_Model):
    table_name = CharField(length=100)
    app_name = CharField(length=100)

    