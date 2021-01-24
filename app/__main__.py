import requests
import json
from models import *
from service import *

print(AvatarService.getAll())
print(AvatarService.getById(1))
print(AvatarService.getByTypeId(2))
