from models import *
from service import *
from controller import *
from asyncio import *

async def start():
    await CoronaController().start()


# Démarre la boucle principale
loop = new_event_loop()
set_event_loop(loop)
loop.run_until_complete(start())
