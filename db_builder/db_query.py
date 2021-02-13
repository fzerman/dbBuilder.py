import sqlite3 

class DB_Query():
    def __init__(self,db_url):
        self.db_url = db_url
        self.s = sqlite3
        self.query = ""
        self._connect()

    def _connect(self):
        self.connection = self.s.connect(self.db_url)
        self.cursor = self.connection.cursor()

    def run(self,query,callback):
        callback(query,self.cursor.execute)
        self.results = self.cursor.fetchall()
        

