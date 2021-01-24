from models import *
from service import *
from asyncio import sleep
import random

class MapController:

    def __init__(self):
        self.map = None


    async def start(self):
        self.map = await MapService.getById(1)
        await TypeService.create(Type(-1, "feux"))
        await self.setTrafficLight()

    async def setTrafficLight(self):
        for lineIndex in range(len(self.map.squares)):
            line = self.map.squares[lineIndex]
            for squareIndex in range(len(line)):
                if "croisement" in line[squareIndex].image:
                    croisement = []
                    colors = ["../assets/images/traffic_light_green.png", "../assets/images/traffic_light_red.png"]
                    colorSet1 = colors[random.randint(0, 1)]
                    colorSet2 = "../assets/images/traffic_light_green.png"
                    if colorSet1 == "../assets/images/traffic_light_green.png":
                        colorSet2 = "../assets/images/traffic_light_red.png"

                    if self.map.squares[lineIndex][squareIndex-1].value == 1:
                        feux1 = Avatar(-1, "feux", 4, colorSet1, 1, 0, squareIndex-1, lineIndex)
                        croisement.append(feux1)
                    if self.map.squares[lineIndex][squareIndex+1].value == 1:
                        feux2 = Avatar(-1, "feux", 4, colorSet1, 1, 0, squareIndex+1, lineIndex)
                        croisement.append(feux2)
                    if self.map.squares[lineIndex-1][squareIndex].value == 1:
                        feux3 = Avatar(-1, "feux", 4, colorSet2, 1, 0, squareIndex, lineIndex-1)
                        croisement.append(feux3)
                    if self.map.squares[lineIndex+1][squareIndex].value == 1:
                        feux4 = Avatar(-1, "feux", 4, colorSet2, 1, 0, squareIndex, lineIndex+1)
                        croisement.append(feux4)
                    for avatar in croisement:
                        await AvatarService.create(avatar)


    async def changeTrafficLight(self):
        print("change light")
        lights = await AvatarService.get_by_type_id(4)
        for light in lights:
            if light.image == "../assets/images/traffic_light_red.png":
                light.image = "../assets/images/traffic_light_green.png"
            else:
                light.image = "../assets/images/traffic_light_red.png"

        return lights