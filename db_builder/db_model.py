import sys, inspect

class DB_Model():
    def model_create(self):
        self.model_name = self.__class__.__name__
        self.instance_dict = {}
        
        for i in self.__class__.__dict__:
            if not i.startswith("__"):
                self.instance_dict[i] = self.__class__.__dict__[i]

        self.migration_create()

    def migration_create(self):
        import datetime, os
        import pathlib
        # path tarafı düzelmeli
        path = pathlib.Path(__file__).parent.absolute()
        path = os.path.join(path,"migrations")
        if(not os.path.isdir(path)):
            os.mkdir(path) 
        e = datetime.datetime.now()
        file_name = "%s-%s-%s-" % (e.month, e.day, e.year) + self.randomword()+".py"
        f = open(path+"/"+file_name,"w")
        f.write("hi guys")

    def randomword(self):
        import random, string
        digits = string.digits
        return ''.join(random.choice(digits) for i in range(11))

class M(DB_Model):
    a = "hjkl"
    b = "hjkl"

    def __init__(self):
        self.x = "hjkl"

    



