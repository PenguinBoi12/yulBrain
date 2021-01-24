from .config import *
from requests import *
from models import Avatar
import json

class AvatarService:
    @staticmethod
    async def getAll():
        avatars = []

        response = get(url=Config.url+"/avatar/")
        data = response.json()

        for d in data:
            avatars.append(Avatar.parse(d))

        return avatars


    @staticmethod
    async def getById(id):
        response = get(url=Config.url+"/avatar/"+str(id))
        data = response.json()

        return Avatar.parse(data)


    @staticmethod
    async def getByTypeId(type_id):
        avatars = []

        response = get(url=Config.url+"/avatar/type/"+str(type_id))
        data = response.json()

        for d in data:
            avatars.append(Avatar.parse(d))

        return avatars

    @staticmethod
    async def create(avatar):
        response = post(url=Config.url+"/avatar/", json = avatar.to_json(),  headers=Config.headers)
        return response.status_code == 200

    @staticmethod
    async def moveAvatars(avatars):
        json_avatars = []

        for avatar in avatars:
            json_avatars.append(avatar.to_json())

        response = post(url=Config.url+"/avatar/move-avatars/", json=json_avatars,  headers=Config.headers)
        return response.status_code == 200
