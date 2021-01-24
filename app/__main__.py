import requests
import json
from models import *
from service import *

print(AvatarService.getAll())
print(AvatarService.getById(1))
print(AvatarService.getByTypeId(2))

# map = []

# for i in range(len(data['square'])):
#     line = []
#     for j in range(len(data['square'][i])):
#         square = Square.parse(data['square'][i][j])
#         line.append(square)
#     map.append(line)


newtype = Type(-1, "TEST")
TypeService.create(newtype)


map = MapService.getById(1)


for x in range(len(map.squares)):
    line = map.squares[x]
    for y in range(len(line)):
        if "croisement" in line[y].image:
            print("croisement " + str(x) + " " + str(y))
            croisement = []
            if map.squares[x-1][y].value == 1:
                print("feux " + str(x-1) + " " + str(y))
                feux1 = Avatar(-1, "feux", 5, "../assets/images/traffic_light_green.png", 1, 0, x-1, y)
                croisement.append(feux1)
            if map.squares[x+1][y].value == 1:
                print("feux " + str(x+1) + " " + str(y))
                feux2 = Avatar(-1, "feux", 5, "../assets/images/traffic_light_green.png", 1, 0, x+1, y)
                croisement.append(feux2)
            if map.squares[x][y-1].value == 1:
                print("feux " + str(x) + " " + str(y-1))
                feux3 = Avatar(-1, "feux", 5, "../assets/images/traffic_light_red.png", 1, 0, x, y-1)
                croisement.append(feux3)
            if map.squares[x][y+1].value == 1:
                print("feux " + str(x) + " " + str(y+1))
                feux4 = Avatar(-1, "feux", 5, "../assets/images/traffic_light_red.png", 1, 0, x, y+1)
                croisement.append(feux4)
            for avatar in croisement:
                AvatarService.create(avatar)         
            

# square = data['square'][0][0]

# x = Square.parse(square)
# print(x.value)

# print(data['square'])



# response = requests.get(url=URL+"/avatar/")
# data = response.json()

# avatar = data[0]

# x = Avatar.parse(avatar)
# print(x.name)

# print(data)
# response = requests.post(url=URL+"/avatar/move-avatars/", data=json.dumps(data),  headers=headers)
# print(response)
print(MapService.getById(1).squares[0][0].image)

print()
