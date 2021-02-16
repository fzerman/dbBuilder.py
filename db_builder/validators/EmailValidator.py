from ..db_validator import DB_Validator
from .SpecialCharValidator import SpecialCharValidator
from ..errors import ValidatorError

class EmailValidator(DB_Validator):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def check(self):
        def wrapper(**kwargs):
            spev_at = SpecialCharValidator(spec="@",value=kwargs["value"]).check()
            spev_dot = SpecialCharValidator(spec=".",value=kwargs["value"]).check()

            if spev_at and spev_dot:
                dot_after_at = kwargs["value"].split("@")[1]
                if not dot_after_at.find(".") == -1:
                    return True
                raise ValidatorError("Email","EmailValidator","This email is not valid!")
            raise ValidatorError("Email","EmailValidator","This email is not valid!")
            
        return self._check(wrapper)