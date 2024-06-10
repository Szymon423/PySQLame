# definitions.py
from enum import Enum
from typing import List
import requests


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


class Connection:
    def __init__(self, url:str):
        self.login = None
        self.password = None
        self.token = None
        self.url = url

    def log(self, login:str, password:str):
        self.password = password
        self.login = login
        headers = {
            'login': self.login,
            'password': self.password
        }
        response = requests.post(self.url + "/authorisation", headers=headers)
        if response.status_code != 200:
            raise Exception("Authorisation failed") 
        data = response.headers
        self.token = data["Authentication"]