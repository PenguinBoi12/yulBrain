from models import *
from service import *


class CarsController:
    def __init__(self, max):
        self.max = max
        self.cars = []


    async def start(self):
        await self.new()


    async def new(self):
        new_car = Avatar(-1, "voiture", 5,  "../assets/images/car.png", 1, 0, 1, 6)
        self.cars.append(new_car)


    async def roam(self):
        map = await MapService.getById(1)

        for car in self.cars:
            if car.direction == "down" and car.y+1 < 29:
                car.y += 1
                next_square = map.squares[car.y+1][car.x]
            elif car.direction == "up":
                car.y -= 1
                next_square = map.squares[car.y-1][car.x]
            elif car.direction == "right":
                car.x += 1
                next_square = map.squares[car.y][car.x+1]
            elif car.direction == "left":
                car.x -= 1
                next_square = map.squares[car.y][car.x-1]

            if next_square.type == "croisement":
                print(f"{next_square.type}")

        print(f"({car.x},{car.y})")
        await AvatarService.move_avatars(self.cars)


    def limit_exceeded(self):
        return len(self.cars) == self.max
