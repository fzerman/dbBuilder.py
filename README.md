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
