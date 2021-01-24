from models import *
from service import *
from controller import *
from asyncio import *
import time

course = [(9,9), (3,21), (16,14), (13,18)]

corona = CoronaController(course)
map = MapController()
cars = CarsController(1)

async def start():
    await map.start()
    await corona.start()
    await cars.start()

    start = time.time()

    while True:
        avatars = await AvatarService.get_all()

        # await corona.do_objectives()

        avatars += await cars.roam()
        await sleep(0.5)

        if time.time() - start > 30:
            avatars += await map.changeTrafficLight()

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
