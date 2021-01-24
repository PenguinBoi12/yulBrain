from .config import *
from requests import *
from models import Type
import json

class TypeService:

    @staticmethod
    def create(type):
        response = post(url=Config.url+"/type/", json = type.to_json(),  headers=Config.headers)
        return response.status_code == 200