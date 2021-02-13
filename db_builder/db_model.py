#import sys, inspect
from .db_query import DB_Query
from .settings import DB_SETTINGS
Query = DB_Query(DB_SETTINGS["DB_URL"])


class DB_Model():
    def model_create(self):
        self.model_name = self.__class__.__name__
        self.instance_dict = {}
        
        for i in self.__class__.__dict__:
            if not i.startswith("__"):
                self.instance_dict[i] = self.__class__.__dict__[i]

        self.create_table()

    def create_table(self):
        create_table_query = "Create Table If not exists {} (".format(self.model_name)

        for i in self.instance_dict:
            self.instance_dict[i].field_name = i
            q = self.instance_dict[i].set_query()
            create_table_query += q
            
            if not list( self.instance_dict.keys() ).index(i) == len( self.instance_dict.keys() )-1:
                create_table_query += ", "
            
        create_table_query += ")"
        
        def ct_wrapper(q,execute):
            execute(q)

        Query.run(create_table_query,ct_wrapper)


    



