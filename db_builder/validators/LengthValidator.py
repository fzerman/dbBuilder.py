from ..db_validator import DB_Validator

class LengthValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            if "length" in kwargs:
                if kwargs["length"] > len(kwargs["value"]):
                    return True
                return False
            
            elif "max" in kwargs and "min" in kwargs:
                if kwargs["max"] > len(kwargs["value"]) and kwargs["min"] < len(kwargs["value"]):
                    return True
                return False
            
            elif "max" in kwargs:
                if kwargs["max"] > len(kwargs["value"]):
                    return True
                return False

            elif "min" in kwargs:
                if kwargs["min"] < len(kwargs["value"]):
                    return True
                return False


            return False

            
        return self._check(wrapper)