from models import *
from service import *

async def init_start_position():
    corona = await AvatarService.getById(1)

    corona.x = 1
    corona.y = 1

    await AvatarService.moveAvatars([corona])
