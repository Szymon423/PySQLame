# connect.py
import requests
import json

class Connection:
    def __init__(self, url:str):
        self.login = None
        self.password = None
        self.token = None
        self.url = url

    def log(self, login:str, password:str):
        self.password = password
        self.login = login
        print(f"Trying to authorise user: '{ self.login }'")
        headers = {
            'login': self.login,
            'password': self.password
        }
        response = requests.post(self.url + "/authorisation", headers=headers)
        if response.status_code != 200:
            raise Exception("Authorisation failed") 
        data = response.headers
        self.token = data["Authentication"]