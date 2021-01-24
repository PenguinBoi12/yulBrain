from models import *
from service import *
from controller import *
import time
import asyncio

async def start():
    await init_start_position()


# Démarre la boucle principale
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(start())
