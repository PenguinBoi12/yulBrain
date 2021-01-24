from models import *
from service import *
from asyncio import sleep

class CoronaController:
    def __init__(self):
        self.corona = None


    async def start(self):
        self.corona = await AvatarService.getById(1)
        await self.init_start_position()
        await self.move_forward()


    async def init_start_position(self):
        self.corona.x = 1
        self.corona.y = 0

        await AvatarService.moveAvatars([self.corona])


    async def move_forward(self):
        for _ in range(5):
            self.corona.y += 1
            await sleep(1)

            await AvatarService.moveAvatars([self.corona])
