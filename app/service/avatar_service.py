from .config import *
from requests import *
from models import Avatar
import json

class AvatarService:
    @staticmethod
    def getAll():
        avatars = []

        response = get(url=Config.url+"/avatar/")
        data = response.json()

        for d in data:
            avatars.append(Avatar.parse(d))

        return avatars


    @staticmethod
    def getById(id):
        response = get(url=Config.url+"/avatar/"+str(id))
        data = response.json()

        return Avatar.parse(data)


    @staticmethod
    def getByTypeId(type_id):
        avatars = []

        response = get(url=Config.url+"/avatar/type/"+str(type_id))
        data = response.json()

        for d in data:
            avatars.append(Avatar.parse(d))

        return avatars
