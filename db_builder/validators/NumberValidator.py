from ..db_validator import DB_Validator

class NumberValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            if "value" in kwargs:
                numbers = "1234567890"
                return any(i in kwargs["value"] for i in numbers)
            return False
            
        return self._check(wrapper)