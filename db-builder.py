import sqlite3

DB = "kütüphane.db"
table = list()
col = list()

class dataBase():
    def __init__(self):
        self.connect(DB)
        self.i = 0
    def connect(self,DB):
        self.baglanti = sqlite3.connect(DB)
        self.cursor = self.baglanti.cursor()

    def table(self,name):
        table.append(name)

    def schema(self,name,tip):
        col.append(name + " " + tip)

    def createTable(self):
        sorgu = "Create Table If not exists " + table[self.i] + " ("
        for i in col:
            sorgu = sorgu + i
            if not( i == col[-1] ):
                sorgu = sorgu + ","
        sorgu = sorgu + ")"
        self.cursor.execute(sorgu)
        print(table[self.i] + " tablosu başarıyla oluşturuldu.")
        self.i =+ 1
"""
    def where(self,name,şey):
        sorgu = "where "+ name + " = {}".format(şey)
        return sorgu

    def select(self,name,şey = ""):
        sorgu = "Select " + şey + " From " + name
        return sorgu

    def run(self,sorgu):
        self.cursor.execute(sorgu)
        results = self.cursor.fetchall()
        print(results)

db = dataBase()
db.run(db.select('zerman','*') + db.where('isim','ahmet'))
"""


