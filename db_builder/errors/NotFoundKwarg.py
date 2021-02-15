from ..db_errors import DB_Error

class NotFoundKwarg(DB_Error):
    def __init__(self,keyword):
        super().__init__("HIGH DEGREE",f'Not Found Keyword: {keyword}')