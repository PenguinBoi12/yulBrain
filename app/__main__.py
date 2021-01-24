import requests
import json
from models import *

URL = "http://localhost:8080/api"
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

response = requests.get(url=URL+"/map/1")
data = response.json()

map = []

for i in range(len(data['square'])):
    line = []
    for j in range(len(data['square'][i])):
        square = Square.parse(data['square'][i][j])
        line.append(square)
    map.append(line)



for x in range(len(map)):
    line = map[x]
    for y in range(len(line)):
        if "croisement" in line[y].image:
            print("croisement " + str(x) + " " + str(y))
            croisement = []
            if map[x-1][y].value == 1:
                print("feux " + str(x-1) + " " + str(y))
                feux1 = Avatar(-1, "feux", 5, "../assets/images/route_vert.png", 1, 0, x-1, y)
                croisement.append(feux1)
            if map[x+1][y].value == 1:
                print("feux " + str(x+1) + " " + str(y))
                feux2 = Avatar(-1, "feux", 5, "../assets/images/route_vert.png", 1, 0, x+1, y)
                croisement.append(feux2)
            if map[x][y-1].value == 1:
                print("feux " + str(x) + " " + str(y-1))
                feux3 = Avatar(-1, "feux", 5, "../assets/images/route_rouge.png", 1, 0, x, y-1)
                croisement.append(feux3)
            if map[x][y+1].value == 1:
                print("feux " + str(x) + " " + str(y+1))
                feux4 = Avatar(-1, "feux", 5, "../assets/images/route_rouge.png", 1, 0, x, y+1)
                croisement.append(feux4)     
            





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
