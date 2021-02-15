class DB_Error(Exception):

    def __init__(self,priority,message):
        self.priority = priority
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.priority} ERROR -> {self.message}'