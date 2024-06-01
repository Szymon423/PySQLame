from definitions import *
import requests
import json


def create_table(connection_string:str, table: Table):
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
    response = requests.post(connection_string, json=j)
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 200


def drop_table(connection_string:str, table_name:str):
    j = {
        "DROP": {
            "TABLE" : {
                "NAME" : table_name
            }
        }
    }
    response = requests.post(connection_string, json=j)
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 200