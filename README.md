<p align="center">
    <img src="https://swindler36.github.io/dbBuilder.py/db%20Builder%20py.png" alt="DB Builder Logo">
</p>

<p align="center">
<h1 align="center">dbBuilder.py v 1.0.0 - Beta </h1>
</p>

> This project is my #oneweekchallenge project. 
> 
> Start: 12 February 2021
> 
> End : 18 February 2021

This is a mini orm library for python. This library uses sqlite3. Therefore, the sqlite3 is necessary.

## Features

### Easy Model Registeration
```python
from db_builder.fields import *
from db_builder.db_model import DB_Model

class MyPost(DB_Model):
    title = CharField(length=100)
    content = TextField()
    created_time = DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
# for creating table
MyPost().create_table()
```

### Easy Insert, Update and Delete Operation
```py
# for inserting a new record
post = MyPost(title="My first post","Hello everyone. This is my first post!")
post.save()

# for updating a exist record
post = MyPost().objects().filter(title="My first post") # returns a queryset array
post[0].title = "New title of my first post"
post[0].save()

#for delete a exist record
post = MyPost().objects().filter(title="My first post") # returns a queryset array
post[0].delete()
```

### Get record with id
```py
MyPost().objects().get(post_id)
```

### Filter records
```py
post = MyPost().objects().filter(title="My first post") # using one column
post = MyPost().objects().filter(title="My first post",content="Hello everyone. This is my first post!") # using multiple columns
```

### Built-in Validators and Parent Validator Class(for creating custom validator) 
* DB_Validator (parent class)
    * BigLetterValidator
    * EmailValidator
    * LengthValidator
    * NumberValidator
    * SmallLetterValidator
    * SpecialCharValidator

### Built-in 17 Fields and Parent Field Class(for creating custom field) 
* DB_Field (parent class)
  * TextField
  * CharField 
  * DateField 
  * DateTimeField 
  * TimeField 
  * BooleanField 
  * IntegerField 
  * JsonField 
  * IDField 
  * URLField 
  * SlugField 
  * FileField - need config
  * ImageField - need config
  * FloatField 
  * EmailField 
  * ForeignKeyField 

### Built-in 5 Errors and Parent Error Class(for creating custom error) 
* DB_Error (parent class)
  * .NotFoundKwarg 
  * .ModelError 
  * .OperationError - not exist
  * .QueryError 
  * .FieldError 
  * .ValidatorError 
  * .SettingError - not exist
  * .StructureError - not exist


### Utilities
* StringStructureParser (have some bugs)
```py
structure = StringStructureParser("user@example.com","<user>@<company>.<extension>")
print( structure.parse() )
"""
Output:
{'user': 'user', 'company': 'example', 'extension': 'com'}
"""
```

## Implementations
### Flask
```py
from flask.globals import g
# flask app contruction

def connect_db():
    Query = DB_Query("DB_URL")
    class ob():
        pass
    MyPost.__Query__ = Query
    ob.MyPost = MyPost

    return ob
    
@app.before_request
def before_request():
    g.db = connect_db()
    
# codes...
# Usage
g.db.Mypost(...) # classical usage
```




