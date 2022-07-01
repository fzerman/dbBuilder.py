from ..db_fields import DB_Field
from ..errors import ValidatorError
from ..settings import UPLOAD_FOLDER, VERIFIED_IMG_FORMATS, UPLOAD_URL
from PIL import Image
import string, random, os

class ImageField(DB_Field):
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.field_name = ""
        self.field_type = "TEXT"

    def db_value(self):
        if self.is_valid():
            file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 20)) + '.'+self.img.format.lower()
            if os.path.isdir(UPLOAD_FOLDER):
                file_path = os.path.join(UPLOAD_FOLDER,file_name)
                self.img.save(file_path)
                return f"{UPLOAD_URL}/{file_name}"
            raise FileNotFoundError("Upload Directory Is Not Found!")
        raise ValidatorError("Image","ImageValidator","Image format is not in verified image formats!")
            
    def is_valid(self):
        img = Image.open(self.get_kwarg("value"))
        if img.format.lower() in VERIFIED_IMG_FORMATS and self.get_validators_result():   
            self.img = img
            return True
        raise ValidatorError("Image","ImageValidator","Image format is not in verified image formats!")

    
    def get_value(self,value):
        return value if os.path.isfile(value) else False