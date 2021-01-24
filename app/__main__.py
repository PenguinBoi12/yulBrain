from models import *
from service import *


corona = AvatarService.getById(1)

corona.x = 1
corona.y = 4

AvatarService.moveAvatars([corona])
