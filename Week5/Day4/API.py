import requests 
import json

response = requests.get("https://api.chucknorris.io/jokes/random")

print(response)
#200 = Success
#300 = Redirect
#400 = Error
data = []
for i in range (10):
    response =  response = requests.get("https://api.chucknorris.io/jokes/random")
    data.append[response.json()]
    with open('./chucks_jokes.json', mode = 'a')as f:
        json.dump(data, f)
# print(type(data))
print(data['value'])
jokes = json.load('./chucks_jokes.json')