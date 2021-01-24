from itertools import *
from models import *
from service import *
from asyncio import sleep

class CoronaController:
    def __init__(self, objectives=[]):
        self.objectives = objectives
        self.corona = None
        self.current_objective = None
        self.speed = 0.2
        self.objectives_cycle = cycle(self.objectives)

    async def start(self):
        self.corona = await AvatarService.get_by_id(1)
        self.corona.x = 1
        self.corona.y = 1
        self.current_objective = next(self.objectives_cycle)

        await AvatarService.move_avatars(await self.replace_corona())


    async def replace_corona(self):
        avatars = await AvatarService.get_all()
        avatars[0] = self.corona

        return avatars


    async def do_objectives(self):
        last_objective = self.objectives[len(self.objectives)-1]

        if self.corona.x == self.current_objective[0] and self.corona.y == self.current_objective[1]:
            self.current_objective = next(self.objectives_cycle)
            print(f"Nouvel objectif: {self.current_objective[0]},{self.current_objective[1]}")
        else:
            await self.move_to(self.current_objective[0], self.current_objective[1])

        print(f"Objectif: {self.corona.x},{self.corona.y}")
        return (self.corona.x != last_objective[0] and self.corona.y != last_objective[1])


    async def take_metro_to(self, x, y):
        self.corona.x = x
        self.corona.y = y

        await sleep(15)
        await AvatarService.move_avatars(await self.replace_corona())


    async def move_to(self, x, y):
        if self.corona.y != y:
            if self.corona.y > y:
                self.corona.y -= 1
            else:
                self.corona.y += 1

        if self.corona.x != x:
            if self.corona.x > x:
                self.corona.x -= 1
            else:
                self.corona.x += 1

        await AvatarService.move_avatars(await self.replace_corona())
