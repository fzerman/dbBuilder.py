#import sys, inspect
from .db_query import Query
from .db_field_object import DB_FieldObject
from .fields import IDField

class DB_Model():
    def __init__(self,**kwargs):
        self.model_name = self.__class__.__name__
        self.instance_dict = self.__class__.__dict__
        self.query_set = []
        # IDField
        id_field = IDField()
        setattr(self,"id_field",DB_FieldObject(self.__class__,id_field))
        setattr(self,"id",0)

        inst_dict = {}
        inst_dict["id"] = id_field
        for i in self.instance_dict:
            if not i.startswith("__"):
                setattr(self,i+"_field",DB_FieldObject(self.__class__,self.instance_dict[i]))
                
                if i in kwargs:
                    setattr(self,i,kwargs[i])
                else:
                    setattr(self,i,self.instance_dict[i].db_value())

                inst_dict[i] = self.instance_dict[i]
        
        self.instance_dict = inst_dict

        self.objects = self.DB_Objects(self)
       

    def create_table(self):
        create_table_query = "Create Table If not exists {} (".format(self.model_name)

        for i in self.instance_dict:
            self.__dict__[f"{i}_field"].field.field_name = i
            q = self.__dict__[f"{i}_field"].field.set_query()
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
            if not i == "id":
                query += i
            
                if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                    query += ", "
            
        query += ") VALUES("
        for i in self.instance_dict:
            if not i == "id" :
                self.__dict__[i+"_field"].field.kwargs["value"] = self.__dict__[i]
                query += "'{}'".format(self.__dict__[i+"_field"].field.db_value())
                
                if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                    query += ", "
                
        query += ")"
        def ct_wrapper(q,db_q):
            db_q.cursor.execute(q)
            db_q.connection.commit()

        Query.run(query,ct_wrapper)
    
    #for update first select
    def _update(self):

        query = "UPDATE {} SET ".format(self.model_name)

        for i in self.instance_dict:
            query += "{} = '{}'".format(i,self.instance_dict[i].db_value())
            
            if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                query += ", "
            
        query += " WHERE username = {}".format("'ali'")

        def ct_wrapper(q,db_q):
            db_q.cursor.execute(q)
            db_q.connection.commit()
        
        Query.run(query,ct_wrapper)
    
    class DB_Objects:
        def __init__(self,p_cls):
            self.p_cls = p_cls

        def get(self,ob_id):
            
            query = f"Select * From {self.p_cls.model_name} where id = {ob_id}" 

            def ct_wrapper(q,db_q):
                db_q.cursor.execute(q)
                q_set = db_q.cursor.fetchall()
                if len(q_set) > 0:
                    self.query_set = q_set
                else:
                    self.query_set = []
            
            Query.run(query,ct_wrapper)

            return self.query_set # will return a query set object here
    



