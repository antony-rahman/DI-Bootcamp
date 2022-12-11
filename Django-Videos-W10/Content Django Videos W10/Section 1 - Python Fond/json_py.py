
# JSON is commonly used with data APIS.
# Parsing JSON into a python dictionary

# don't forget to import
import json


# sample JSON - Has to be double quote to be JSON
userJSON = '{"first_name": "Daniel", "last_name": "Ach", "age": 26}'

# Parse to dict (to create a dict)
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# dump (to create json)
car = {
    'brand': 'Kia',
    'Model': 'Sportage',
    'year': '2016',
}

carJSON = json.dumps(car)
print(carJSON)
