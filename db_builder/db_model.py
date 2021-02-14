#import sys, inspect
from .db_query import Query
from .db_field_object import DB_FieldObject

class DB_Model():
    def __init__(self,**kwargs):
        #object_values kaldırılıcak
        self.object_values = kwargs
        self.model_name = self.__class__.__name__
        self.instance_dict = {}
        
        for i in self.__class__.__dict__:
            if not i.startswith("__"):
                self.instance_dict[i+"_field"] = self.__class__.__dict__[i]
                self.__class__.__dict__[i] = DB_FieldObject(self.__class__,kwargs[i])

        for i in self.instance_dict:
            self.instance_dict[i+"_field"].kwargs["value"] = kwargs[i]
            self.instance_dict[i] = DB_FieldObject(self.__class__,kwargs[i])

    def set_value(self,**kwargs):
        for i in kwargs:
            self.instance_dict[i].kwargs["value"] = kwargs[i]

    def create_table(self):
        create_table_query = "Create Table If not exists {} (".format(self.model_name)

        for i in self.instance_dict:
            self.instance_dict[i].field_name = i
            q = self.instance_dict[i].set_query()
            create_table_query += q
            
            if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                create_table_query += ", "
            
        create_table_query += ")"
        
        def ct_wrapper(q,db_q):
            db_q.cursor.execute(q)

        Query.run(create_table_query,ct_wrapper)

    def _insert(self):
        query = "INSERT INTO {} (".format(self.model_name)

        for i in self.instance_dict:
            query += i
            
            if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                query += ", "
            
        query += ") VALUES("
        for i in self.instance_dict:
            query += "'{}'".format(self.instance_dict[i].db_value())
            
            if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                query += ", "
            
        query += ")"
        def ct_wrapper(q,db_q):
            db_q.cursor.execute(q)
            db_q.connection.commit()

        Query.run(query,ct_wrapper)
     
    def _update(self):

        query = "UPDATE {} SET ".format(self.model_name)

        for i in self.instance_dict:
            query += "{} = '{}'".format(i,self.instance_dict[i].db_value())
            
            if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                query += ", "
            
        query += " WHERE username = {}".format("'ali'")
        print(query)
        def ct_wrapper(q,db_q):
            db_q.cursor.execute(q)
            db_q.connection.commit()

        Query.run(query,ct_wrapper)
    



