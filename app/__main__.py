from models import *
from service import *
from controller import *
from asyncio import *
import time

course = [(9,9), (3,21), (16,14), (13,18)]

corona = CoronaController(course)
map = MapController()
cars = CarsController(5)

async def start():
    await map.start()
    await corona.start()
    await cars.start()

    start = time.time()

    while True:
        # print(await corona.do_objectives())
        # await map.changeTrafficLight()
        await cars.roam()
        await sleep(0.5)

        # if time.time() - start > 1 and not cars.limit_exceeded():
        #     start = time.time()
        #     await cars.new()


# Démarre la boucle principale
try:
    loop = new_event_loop()
    loop.run_until_complete(start())
except KeyboardInterrupt:
    print("\nSimulation arrêtée!")
