import os 

DB_SETTINGS = {
    "ENGINE" : "sqlite",
    "DB_URL" : "./test.db"
}

PROJECT_PATH = ""

INFO_SCHEMA = {
    "TABLE_NAME" : "INFO_SCHEMA"
}

UPLOAD_FOLDER = os.path.join(os.getcwd(),"uploads")
UPLOAD_URL = "/uploads"


VERIFIED_IMG_FORMATS = ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']
VERIFIED_FILE_FORMATS = ('pdf','xml','html','md')
