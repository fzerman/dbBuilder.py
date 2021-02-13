class DB_Validator():
    def _check(self,check_callback):
        if type(check_callback).__name__ == "function":
            return check_callback(**self.kwargs)
        return "no func"

    def get_kwarg(self,kw):
        if kw in self.kwargs:
            return self.kwargs[kw]
        return False