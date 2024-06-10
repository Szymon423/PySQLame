![SQLame logo](./img/logo.png)

# PySQLame

This project is `Python` library which allows to communicate with `SQLame` database.

## Example
```python
from definitions import *
from table import create_table, insert_values, drop_table
from connect import Connection

url = "http://127.0.0.1:9443"
connection_string = Connection(url)

try:
    connection_string.log("admin", "admin")
except:
    print("Unable to login")
    exit()

c1 = Column("id", DataType.INT, [Attribute.PRIMARY_KEY, Attribute.NOT_NULL, Attribute.UNIQUE])
c2 = Column("name", DataType.TEXT)
t = Table("test_table", [c1, c2])

create_table(connection_string, t)

val1 = {
    "id": 0,
    "name": "truskawki"
}
val2 = {
    "id": 1,
    "name": "maliny"
}
val3 = {
    "id": 2,
    "name": "porzeczki"
}

insert_values(connection_string, t.name, [val1, val2, val3])

drop_table(connection_string, t.name)
```

## TODO
 - [ ] handle select users
