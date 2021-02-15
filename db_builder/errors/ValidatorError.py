from ..db_errors import DB_Error

class ValidatorError(DB_Error):
    def __init__(self,value_name,validation_name,validation_message):
        super().__init__("WARNING",f'"{value_name}" Is Not Valid => {validation_name} : {validation_message}')