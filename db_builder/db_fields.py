class DB_Field():
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = ""

    def get_kwarg(self,kw):
        if kw in self.kwargs:
            return self.kwargs[kw]
        return False

    def set_query(self):
        return " ".join([self.field_name,self.set_q()])
     
    def set_q(self):
        q = [self.field_type]

        if(not self.is_nullable()):
            q.append("NOT NULL")

        if(self.is_unique()):
            q.append("UNIQUE")

        if(self.is_auto_inc()):
            q.append("AUTO_INCREMENT")

        if(self.is_primary()):
            q.append("PRIMARY KEY")

        if(self.get_foreign()):
            q.append("FOREIGN KEY REFERENCES "+ self.get_foreign() +"(id)")

        default = self.get_default()
        if(default):
            q.append("DEFAULT " + default)

        return " ".join(q)
        
    def is_nullable(self):
        return self.get_kwarg("null") == True

    def is_unique(self):
        return self.get_kwarg("unique") == True

    def is_auto_inc(self):
        return self.get_kwarg("auto_inc") == True

    def is_primary(self):
        return self.get_kwarg("primary") == True

    def get_default(self):
        return self.get_kwarg("default")

    def get_foreign(self):
        return self.get_kwarg("foreign")


class CharField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        if(self.get_kwarg("length")):
            self.field_type = "varchar("+self.get_kwarg("length")+")"
        else:
            self.field_type = "varchar(64)"

class TextField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "TEXT"

        
    

