from ..db_fields import DB_Field
from ..errors import ValidatorError
from ..settings import UPLOAD_FOLDER, UPLOAD_URL, VERIFIED_FILE_FORMATS
import string, random, os

class FileField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "TEXT"

    def db_value(self):
        if self.is_valid():
            file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 20)) + '.'+self.file.split(".")[-1]
            if os.path.isdir(UPLOAD_FOLDER):
                file_path = os.path.join(UPLOAD_FOLDER,file_name)
                nf = open(self.file)
                f = open(file_path,"w")
                f.write(nf.read())
                nf.close()
                f.close()
                return file_path
            raise FileNotFoundError("Upload Directory Is Not Found!")
        raise ValidatorError("File","FileValidator","File format is not in verified file formats!")

            
    def is_valid(self):
        f = self.get_kwarg("value")
        if f.lower().endswith(VERIFIED_FILE_FORMATS):   
            self.file = f
            return True
        raise ValidatorError("File","FileValidator","File format is not in verified file formats!")

    
    def get_value(self,value):
        if os.path.isfile(value):
            return value
        return False