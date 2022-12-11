# Class is a blueprint fro creating objects, initialize them

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name}, nice to meet you"

    def has_birthday(self):
        self.age += 1


class Customer(User):

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name}, nice to meet you, I have {self.balance} BTC !"


# Instantiate, Initialize
daniel = User('Daniel', 'dan@dev.com', 26)
jane = User('Jane', 'Jane@dev.com', 36)

# access proprety
print(jane.email)
print(daniel.greeting())
jane.has_birthday()
print(jane.age)  # 37


# Edit property
jane.age = 60
print(jane.age)  # 37

# Init Costumer
dov = Customer('Dov', 'dov@dev.com', '25')
dov.set_balance(2000)

print(dov.greeting())
