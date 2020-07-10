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
## Functions
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
  def select(name,thing,func = [])
```
* where()

name -> the column name

thing -> item that you want to select
```python
  def where(name,thing)
```
* insert()

name -> column name

thing -> values
```python
  def insert(name,thing = [])
```
* delete()

name -> table name

func -> callback function
```python
  def delete(name,func = [])
```
* update()

name -> table name

thing -> column name 

func -> callback
```python
  def update(name,thing,value,func=[])
```
* sort()

Returns "ORDER BY".
If "state = 1", returns "ASC". If "state = -1", returns "DESC".
Default value of "state" is 1.   
```python
	def sort(column,state = 1)
```

* getDBinfo()

Returns column infos of selected table.
```python
	def getDBinfo(name)
```

* filter()

Makes some calculations like "average" on data.
###### WARNİNG! :
It supports only "avr" now.

```python
	def filter(data,_filter,state,table)
```


