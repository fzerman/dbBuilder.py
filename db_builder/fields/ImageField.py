from ..db_fields import DB_Field
from ..settings import UPLOAD_FOLDER, VERIFIED_IMG_FORMATS
from PIL import Image
import string, random, os

class ImageField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "TEXT"

    def db_value(self):
        if self.is_valid():
            file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 20))
            if os.path.isdir(UPLOAD_FOLDER):
                file_path = os.path.join(UPLOAD_FOLDER,file_name)
                image = open(file_path,"w")
                image.write(self.img)
                image.close()
                return file_path
            return False
        return False
            
    def is_valid(self):
        img = Image.open(self.get_kwarg("value"))
        if img.format.lower() in VERIFIED_IMG_FORMATS and img.verify():   
            self.img = img
            return True
        return False
    
    def get_value(self,value):
        if os.path.isfile(value):
            return value
        return False