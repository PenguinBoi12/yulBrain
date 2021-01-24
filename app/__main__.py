from models import *
from service import *
import time
import asyncio

async def start():
    corona = await AvatarService.getById(1)

    corona.x = 1
    corona.y = 1

    await AvatarService.moveAvatars([corona])


# Démarre la boucle principale
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(start())
