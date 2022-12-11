
# Dictionary is unordered, changeable, indexed. No Duplicate.

# Simple Dict
# person = dict({first_name='John'}) with constuctor
person = {
    # key: value
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,  # no =
}

# get value
print(person['first_name'])
print(person.get('first_name'))

# add key/value
person['phone'] = '05502200202'
print(person['phone'])

# get key or value
print(person.keys())
print(person.values())

# Make copy
person2 = person.copy()
person2['city'] = 'Brussels'

# remove items
del(person['age'])
person.pop('phone')

# clear
person.clear()
# len
print(len(person2))


# List of Dict

people = [
    {'first_name': 'John',
     'last_name': 'Doe',
     'age': 30, },
    {'first_name': 'Dani',
     'last_name': 'Odon',
     'age': 26, }
]

# get
print(people[1]['first_name'])
print(person2)
print(person)
