from definitions import *
import requests
import json
from connect import Connection

def create_table(connection_string:Connection, table: Table):
    print(f"Creating table: '{table.name}' with columns:")
    columns = []
    for col in table.columns:
        attribs = ", "
        if len(col.attributes) > 0:
            attribs_list = [atr.name for atr in col.attributes]
            attribs += "Attributes: [" + ", ".join(attribs_list) + "]"
            print(f" > Column '{col.name}', DataType: {col.data_type.name}" + attribs)
        else:
            print(f" > Column '{col.name}', DataType: {col.data_type.name}")
        
        column_dict = {
            "NAME": col.name,
            "TYPE": col.data_type.name
        }
        if col.attributes:
            column_dict["ATTRIBUTES"] = [atr.name for atr in col.attributes]

        columns.append(column_dict)
    j = {
        "CREATE": {
            "TABLE" : {
                "NAME" : table.name,
                "COLUMNS" : columns,
            }
        }
    }

    headers = {
        'Authentication': connection_string.token
    }
    response = requests.post(connection_string.url + "/request", json=j, headers=headers)
    assert response.status_code == 200
    data = response.json()
    code = "OK" if data["code"] == 0 else "BAD"
    print(f"resoult: {code}")
    print(f"message: {data["message"]}")


def drop_table(connection_string:Connection, table_name:str):
    j = {
        "DROP": {
            "TABLE" : {
                "NAME" : table_name
            }
        }
    }
    headers = {
        'Authentication': connection_string.token
    }
    response = requests.post(connection_string.url + "/request", json=j, headers=headers)
    assert response.status_code == 200
    data = response.json()
    code = "OK" if data["code"] == 0 else "BAD"
    print(f"resoult: {code}")
    print(f"message: {data["message"]}")


def insert_values(connection_string:Connection, table_name:str, values:List):
    j = {
        "INSERT": {
            "INTO": table_name,
            "VALUES": values
        }
    }
    headers = {
        'Authentication': connection_string.token
    }
    response = requests.post(connection_string.url + "/request", json=j, headers=headers)
    assert response.status_code == 200
    data = response.json()
    code = "OK" if data["code"] == 0 else "BAD"
    print(f"resoult: {code}")
    print(f"message: {data["message"]}")