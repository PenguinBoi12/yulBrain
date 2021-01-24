from models import *
from service import *
from controller import *
from asyncio import *
import time

course = [(9,9), (3,21), (16,14), (13,18)]

corona = CoronaController(course)
map = MapController()
cars = CarsController(5)
pietons = PietonController(30)

async def start():
    await map.start()
    await corona.start()
    await cars.start()
    pietons.map = map.map
    await pietons.start()

    start = time.time()

    while True:
        avatars = await AvatarService.get_all()
        avatars += await cars.roam()
        await corona.do_objectives()
        await map.changeTrafficLight()
        # await cars.roam()
        await sleep(1)

        if time.time() - start > 30:
            start = time.time()
            avatars += await map.changeTrafficLight()

        if time.time() - start > 2:
            start = time.time()
            avatars += await pietons.moove()    

        if time.time() - start > 1 and not cars.limit_exceeded():
            start = time.time()
            await cars.new()

        await AvatarService.move_avatars(avatars)

# Démarre la boucle principale
try:
    loop = new_event_loop()
    loop.run_until_complete(start())
except KeyboardInterrupt:
    print("\nSimulation arrêtée!")
