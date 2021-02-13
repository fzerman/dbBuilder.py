from ..db_validator import DB_Validator

class BigLetterValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            if "value" in kwargs:
                numbers = "1234567890"
                for i in numbers:
                    if i in kwargs["value"]:
                        return True
                return False
            return False
            
        return self._check(wrapper)