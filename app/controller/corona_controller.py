from itertools import *
from models import *
from service import *
from asyncio import sleep

class CoronaController:
    def __init__(self, objectives=[]):
        self.objectives = objectives
        self.corona = None
        self.speed = 0.2

    async def start(self):
        self.corona = await AvatarService.get_by_id(1)
        await self.init_start_position()
        await self.do_objectives()


    async def do_objectives(self):
        objectives_cycle = cycle(self.objectives)
        current_objective = next(objectives_cycle)
        last_objective = self.objectives[len(self.objectives)-1]

        while self.corona.x is not last_objective[0] and self.corona.y is not last_objective[1]:
            if self.corona.x == current_objective[0] and self.corona.y == current_objective[1]:
                current_objective = next(objectives_cycle)
                print(f"Next obj : {current_objective}")
            else:
                await self.move_to(current_objective[0], current_objective[1])


    async def init_start_position(self):
        self.corona.x = 1
        self.corona.y = 0

        await AvatarService.move_avatars([self.corona])


    async def take_metro_to(self, x, y):
        self.corona.x = x
        self.corona.y = y

        await sleep(1)
        await AvatarService.move_avatars([self.corona])


    async def move_to(self, x, y):
        while self.corona.y != y:
            if self.corona.y > y:
                self.corona.y -= 1
            else:
                self.corona.y += 1


            await AvatarService.move_avatars([self.corona])
            await sleep(self.speed)


        while self.corona.x != x:
            if self.corona.x > x:
                self.corona.x -= 1
            else:
                self.corona.x += 1

            await AvatarService.move_avatars([self.corona])
            await sleep(self.speed)
