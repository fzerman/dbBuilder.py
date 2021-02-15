from ..db_errors import DB_Error

class FieldError(DB_Error):
    def __init__(self,model_name,field_name,message):
        super().__init__("HIGH DEGREE",f"{field_name} Field at{model_name} Model => {message}")