import sqlite3
from configDB import *

table = list()
col = list()

class dataBase():
    def __init__(self):
        self.connect(DB)
        self.i = 0
        self.s = list()
    
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

    def selectAll(self,name):
        sorgu = "Select * From " + name
        self.cursor.execute(sorgu)
        results = self.cursor.fetchall()
        if(len(results) >0):
            return results
        else:
            return False

    def select(self,name,thing,func = []):
        if len(func) > 0:
            sorgu = "Select " + thing + " From " + name + " " + func[0]
        else:
            sorgu = "Select " + thing + " From " + name 
        if len(func) > 1:
            self.cursor.execute(sorgu,(func[1],))
            results = self.cursor.fetchall()
        else:
            self.cursor.execute(sorgu)
            results = self.cursor.fetchall()
        if(len(results) >0):
            return results
        else:
            return False
    
    def where(self,name,thing):
        sorgu = "where " + name + " = ?"
        return [sorgu,thing]
    
    def insert(self,name,thing = []):
        sorgu = "Insert into " + name + " Values('"
        for i in thing:
            if i == thing[-1]:
                sorgu += i + "')"
            else:
                sorgu += i+"','"
        print(sorgu)
        self.cursor.execute(sorgu)
        self.baglanti.commit()
        print("başarıyla eklendi.")

    def delete(self,name,func = []):
        result = self.select(name,'*',func)
        if result:
            sorgu = "Delete From " + name + " " +func[0]
            if len(func) > 1:
                self.cursor.execute(sorgu,(func[1],))
            else:
                self.cursor.execute(sorgu)
            self.baglanti.commit()
            print("başarıyla silindi")
        else:
            print("item bulunamadı.")

    def update(self,name,thing,value,func=[]):
        sorgu = "Update " + name + " set " + thing + " = ? " + func[0]
        if len(func) > 1:
            self.cursor.execute(sorgu,(value,func[1]))
        else:
            self.cursor.execute(sorgu)
        self.baglanti.commit()
        print("başarıyla güncellendi.")

    def sort(self,column,state = 1):
        if(type(state) == int):
            if(state == 1 ):
                sorgu = "ORDER BY " + column + " ASC"
            elif(state == -1):
                sorgu = "ORDER BY " + column + " DESC"
            return [sorgu]
        else:
            print("ERROR")   

    def getDBinfo(self,name):
        info = []
        sorgu = "PRAGMA table_info("+name+")"
        self.cursor.execute(sorgu)
        results = self.cursor.fetchall()
        if results:
            for result in results:
                info.append(result[1])   
            return info
    
    def filter(self,data,_filter,state,table):
        if data:
            if _filter == "avr":
                list_column = self.getDBinfo(table)
                index = -1
                averange = 0
                for column in list_column:
                    index += 1
                    if state == column:
                        for i in data:
                            averange += int(i[index])
                return averange / len(data)
            
            #elif _filter == "grt":
               
            else:
                print("Filter Error: '" + _filter + "' not supported.")
        else:
            print("Data Error: Data cannot be founded.")
