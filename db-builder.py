import sqlite3

DB = "kütüphane.db"
table = list()
col = list()

class dataBase():
    def __init__(self):
        self.connect(DB)
    
    def connect(self,DB):
        self.baglanti = sqlite3.connect(DB)
        self.cursor = self.baglanti.cursor()

    def table(self,name):
        table.append(name)

    def schema(self,name,tip):
        col.append(name + " " + tip)

    def createTable(self):
        sorgu = "Create Table If not exists " + table[0] + " ("
        for i in col:
            sorgu = sorgu + i
            if not( i == col[-1] ):
                sorgu = sorgu + ","
        sorgu = sorgu + ")"
        self.cursor.execute(sorgu)
        print(table[0] + " tablosu başarıyla oluşturuldu.")

    def select(self,name,şey = ""):
        sorgu = "Select " + şey + " From " + name
        self.cursor.execute(sorgu)
        results = self.cursor.fetchall()
        return results