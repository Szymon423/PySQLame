# definitions.py
from enum import Enum
from typing import List


class DataType(Enum):
	INT = 1
	BOOLEAN = 2
	DOUBLE = 3
	UNIX_TIME = 4
	TEXT = 5


class Attribute(Enum):
	UNIQUE = 1
	PRIMARY_KEY = 2
	AUTOINCREMENT = 3
	NOT_NULL = 4


class Column:
	def __init__(self, column_name:str, data_type:DataType, attributes:List[Attribute] = None):
		self.name = column_name
		self.data_type = data_type
		self.attributes = attributes if attributes is not None else []


class Table:
	def __init__(self, table_name:str, columns:List[Column]):
		self.name = table_name
		self.columns = columns
		if len(self.columns) < 1:
			raise ValueError("Table must have at least one column.")