import sqlite3 

class DB_Query():
    def __init__(self,db_url):
        self.db_url = db_url
        self.s = sqlite3
        self.query = ""
        self._connect()

    def _connect(self):
        self.connection = self.s.connect(self.db_url)
        self.connection.row_factory = self.dict_factory
        self.cursor = self.connection.cursor()

    def dict_factory(self,cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def run(self,query,callback):
        callback(query,self)
        
from .settings import DB_SETTINGS
Query = DB_Query(DB_SETTINGS["DB_URL"])