class column():    
    def int(self):
        return "INTEGER"

    def text(self):
        return "TEXT"

    def blob(self):
        return "BLOB"

    def real(self):
        return "REAL"

    def numeric(self):
        return "NUMERIC"

    def unique(self):
        return "UNIQUE"

    def primary(self):
        return "PRIMARY KEY"

    def autoInc(self):
        return self.primary() + " AUTOINCREMENT"

    def id(self):
        return self.int() + " " + self.autoInc()
    

    
