from ..db_errors import DB_Error

class ModelError(DB_Error):
    def __init__(self,model_name,message):
        super().__init__("HIGH DEGREE",f"{model_name} Model => {message}")
