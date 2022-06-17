from ..db_validator import DB_Validator

class SmallLetterValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            if "value" in kwargs:
                smallletters = "abcdefghıjklmnopQrstuvwxyz"
                return any(i in kwargs["value"] for i in smallletters)
            return False
            
        return self._check(wrapper)
            

