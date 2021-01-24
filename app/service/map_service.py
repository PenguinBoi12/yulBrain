from .config import *
from requests import *
from models import Map
import json

class MapService:
    @staticmethod
    def getById(id):
        response = get(url=Config.url+"/map/"+str(id))
        data = response.json()

        return Map.parse(data)
