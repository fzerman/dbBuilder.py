from ..db_validator import DB_Validator
from ..errors import ValidatorError, NotFoundKwarg

class BigLetterValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            if "value" in kwargs:
                bigletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                for i in bigletters:
                    if i in kwargs["value"]:
                        return True
                raise ValidatorError(kwargs["field"],"BigLetterValidator","Not Found Big Letter")
            raise NotFoundKwarg("value")

            
        return self._check(wrapper)
            

