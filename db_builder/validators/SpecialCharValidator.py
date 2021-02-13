from ..db_validator import DB_Validator

class SpecialCharValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            if "spec" in kwargs:
                if kwargs["spec"] in kwargs["value"]:
                    return True
                return False
            else:
                spec_list = '<!>£#^+-*/$%&}{[()]=?_-|.,;:@'
                for i in spec_list:
                    if i in kwargs["value"]:
                        return True
                return False

            
        return self._check(wrapper)
            

