from ..db_errors import DB_Error

class QueryError(DB_Error):
    def __init__(self,query_string):
        super().__init__("FATAL",f'This Query Could Not Run: "{query_string}"')