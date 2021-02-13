from ..db_validator import DB_Validator

class SmallLetterValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            if "value" in kwargs:
                smallletters = "abcdefghıjklmnopQrstuvwxyz"
                for i in smallletters:
                    if i in kwargs["value"]:
                        return True
                return False
            return False
            
        return self._check(wrapper)
            

