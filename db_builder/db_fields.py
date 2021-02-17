from .validators import *

VALIDATORS_DICT = {
    "EmailValidator" : EmailValidator(),
    "BigLetterValidator" : BigLetterValidator(),
    "LengthValidator" : LengthValidator(),
    "NumberValidator" : NumberValidator(),
    "SmallLetterValidator" : SmallLetterValidator(),
    "SpecialCharValidator" : SmallLetterValidator()
}

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
        
        if(self.is_primary()):
            q.append("PRIMARY KEY")

        if(self.is_unique()):
            q.append("UNIQUE")

        if(self.is_auto_inc()):
            q.append("AUTOINCREMENT")

        if(self.get_foreign()):
            q.append("FOREIGN KEY REFERENCES "+ self.get_foreign() +"(id)")

        if(not self.is_nullable()):
            q.append("NOT NULL")

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

    def get_validators_result(self):
        validators = self.get_kwarg("validators")

        if not validators:
            return True
        
        result = True
        
        for i in validators:
            VALIDATORS_DICT[i].kwargs = validators[i]
            result = result and VALIDATORS_DICT[i].check()
            if result == False:
                return result

        return result
     


        
    

