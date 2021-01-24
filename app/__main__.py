from models import *
from service import *
from controller import *
from asyncio import *

course = [(9,9), (3,21), (16,14), (13,18)]

async def start():
    await CoronaController(course).start()


# Démarre la boucle principale
try:
    loop = new_event_loop()
    set_event_loop(loop)
    loop.run_until_complete(start())
except KeyboardInterrupt:
    print("\nSimulation arrêtée!")
