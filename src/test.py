from definitions import *
from table import *

c1 = Column("id", DataType.INT, [Attribute.PRIMARY_KEY, Attribute.NOT_NULL, Attribute.UNIQUE])
c2 = Column("name", DataType.TEXT)

t = Table("test_table", [c1, c2])

connection_string = "http://127.0.0.1:9443"
create_table(connection_string, t)

drop_table(connection_string, t.name)
