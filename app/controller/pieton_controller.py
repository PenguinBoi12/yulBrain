from models import *
from service import *
from asyncio import sleep
import random

class PietonController:

    

    def __init__(self, nombre_pietons):
        self.pietonAvatars = []
        self.nombre_pietons = nombre_pietons
        self.map = None

    async def start(self):
        pietonAvatars = await AvatarService.get_by_type_id(3)

        if len(pietonAvatars) < self.nombre_pietons:
            for i in range(self.nombre_pietons):
                
                line = random.randint(0, 29)
                column =random.randint(0, 29)

                while self.map.square_value(line, column) == 1:
                    line = random.randint(0, 29)
                    column =random.randint(0, 29)
                pieton = Avatar(-1, "piéton", 3, "../assets/images/pieton.png", 1, 0, column, line)
                await AvatarService.create(pieton)

        await AvatarService.add_and_moove_avatars([])

    async def moove(self):
        pietons = await AvatarService.get_by_type_id(3)
        new_pietons_position = []
        for pieton in pietons:
            if pieton.x < 29 and self.map.square_value(pieton.y, pieton.x+1) != 1:
                pieton.x = pieton.x + 1
            elif pieton.y < 29 and self.map.square_value(pieton.y+1, pieton.x) != 1:     
                pieton.y = pieton.y + 1        
            elif pieton.x > 0 and self.map.square_value(pieton.y, pieton.x-1) != 1:    
                pieton.x = pieton.x - 1
            elif pieton.y > 0 and self.map.square_value(pieton.y-1, pieton.x) != 1:    
                pieton.y = pieton.y - 1    
                
            new_pietons_position.append(pieton)

        return new_pietons_position    

        