from db_builder import *

db = dataBase()
"""
db.table('abc')
db.schema('id',db.id())
db.schema('baba','INT')
db.createTable()
db.insert('zerman',['a','b'])
db.delete('zerman',db.where('isim','ahmet'))
db.update('zerman','isim','a',db.where('yazar','v'))
db.delete('denemetable',db.where('isim',a))
info = db.selectAll('denemetable')
print(info)
info = db.selectAll('zerman')
info = db.select('zerman',"isim",db.sort('id',-1))
print(info)
info = db.select('zerman',"*")
info = db.filter(info,"avr","id","zerman")
print(info)
"""
info = db.select('zerman',"*")
info = db.filter(info,"avr","id","zerman")
print(info)