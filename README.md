![dbBuilder.py Logo](https://github.com/Swindler36/dbBuilder.py/blob/master/db%20Builder%20py.png "dbBuilder.py Logo")

# dbBuilder.py v 0.1.2
This is a mini query library for python.
This library supports sqlite3 and uses it. 
Therefore, the sqlite3 is necessary.

## Features
* Management database with writing single row code
* Writing SQL quickly
* Simple use

## Quick Start

```python
  db = dataBase()
  //codes
```
### Creating a table
```python
  table("TABLE_NAME")
  schema("COLUMN1_NAME","TYPE_OF_COLUMN1")
  schema("COLUMN2_NAME","TYPE_OF_COLUMN2")
  schema("COLUMN3_NAME","TYPE_OF_COLUMN3")
  schema("COLUMN4_NAME","TYPE_OF_COLUMN4")
  createTable()
```
### Functions
* selectAll()

name -> table name that you want to select
```python
  def selectAll(name)
```
* select()

name -> table name that you want to select

thing -> "Select (here) From ..."

func -> a callback function like where()
```python
  def select(self,name,thing,func = [])
```
* where()

name -> the column name

thing -> item that you want to select
```python
  def where(self,name,thing)
```
* insert()

name -> column name

thing -> values
```python
  def insert(self,name,thing = [])
```
* delete()

name -> table name

func -> callback function
```python
  def delete(self,name,func = [])
```
* update()

name -> table name

thing -> column name 

func -> callback
```python
  def update(self,name,thing,value,func=[])
```
