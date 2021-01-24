import requests
import json
from models import *

URL = "http://localhost:8080/api"
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

response = requests.get(url=URL+"/map/1")
data = response.json()

square = data['square'][0][0]

x = Square.parse(square)
print(x.value)



response = requests.get(url=URL+"/avatar/")
data = response.json()

avatar = data[0]

x = Avatar.parse(avatar)
print(x.name)

print(data)
response = requests.post(url=URL+"/avatar/move-avatars/", data=json.dumps(data),  headers=headers)
print(response)
