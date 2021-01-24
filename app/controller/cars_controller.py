from models import *
from service import *
from random import choice

class CarsController:
    def __init__(self, max):
        self.max = max
        self.cars = []


    async def start(self):
        await self.new()


    async def new(self):
        new_car = Avatar(-1, "voiture", 5,  "../assets/images/car.png", 1, 0, 1, 9)
        self.cars.append(new_car)


    async def roam(self):
        map = await MapService.getById(1)
        next_positions = None

        for car in self.cars:
            if car.direction == "down" and car.y+1 < 29:
                car.y += 1
            elif car.direction == "up" and car.y-1 > 0:
                car.y -= 1
            elif car.direction == "right" and car.x+1 < 29:
                car.x += 1
            elif car.direction == "left" and car.x-1 > 0:
                car.x -= 1
            else:
                self.cars.remove(car)

            if car is not None:
                current_square = map.squares[car.y][car.x]
                if current_square.type == "croisement":
                    await self.get_directions(map.squares, car)

        return self.cars


    async def get_directions(self, squares, car):
        directions = []

        if squares[car.x][car.y+1].value == 1 and car.direction != "up":
            directions.append("down")
        if squares[car.x][car.y-1].value == 1 and car.direction != "down":
            directions.append("up")
        if squares[car.x+1][car.y].value == 1 and car.direction != "left":
            directions.append("right")
        if squares[car.x][car.y-1].value == 1 and car.direction != "right":
            directions.append("left")

        if len(directions) > 0:
            car.direction = choice(directions)


    def limit_exceeded(self):
        return len(self.cars) == self.max
