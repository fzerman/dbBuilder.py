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
"""
a = 'a'
db.delete('denemetable',db.where('isim',a))


info = db.selectAll('denemetable')
print(info)