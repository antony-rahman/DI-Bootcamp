from itertools import groupby
from operator import itemgetter

# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
# innit

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat('Jerry', 22)
cat2 = Cat('Tom', 11)
cat3 = Cat('Leo', 7)


cats = [cat1,cat2,cat3]
oldest_cat=cats[0]

for cat in cats:
    if oldest_cat.age < cat.age:
     oldest_cat=cat

     print(oldest_cat)
        
        
oldest_cat_fonction = lambda cat1,cat2: cat1 if cat1.age>cat2.age else cat2

print(oldest_cat.name)
        






# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog:
   
 def __init__(self ,dog_name , dog_height):
            self.name = dog_name
            self.height = dog_height


def bark(self):
    print(f"{self.name} goes wolf ")


def jump(self):
 x = self.height*2 
 print(f"{self.name} jump {x} cm high!")


def __str__(self):
    return f"s{self.name} , {self.height}"

davids_dog = Dog('rex', 50)
 
string_dog = str(davids_dog)

print(davids_dog)
davids_dog.bark()
davids_dog.jump()


sarahs_dog = Dog('Teacup', 20)



print(sarahs_dog)
sarahs_dog.bark()
sarahs_dog.jump()  

bigger_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name
print(bigger_dog)



# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


class Song:
    def __init__(self,  lyrics):
        self.lyrics = lyrics

def sing_me_a_song(self):
 for line in self.lyrics:
    print(line)
    
stairway= Song(["Theres a lady who's sure","all that glitters is gold", "and shes buying a stairway to heaven"]).sing_me_a_song()



# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


 

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

def add_animal(self, new_animal):
   if new_animal not in self.animals :
      self.animals.append(new_animal)
   else:
         print(f'{new_animal} already exists')
 
         


def get_animals(self):
    for animal in self.animals:
      print(animal)

def sell_animal(self , animal_sold):
   if animal_sold in self.animals:
    #    del animal_sold
      self.animals.remove(animal_sold)
   else:
            print(f'{animal_sold} not in zoo')

            

def sort_animals(self):

    sorted(self.animals)
    # ou  self.animals.sort()

new_dict = {}
x = [list(word) for letter, word in groupby(self.animals, key=itemgetter(0))]

for index, word in enumerate(x):
     if len(word) < 2:
        word = "".join(word)
     new_dict[index + 1] = word
     print(new_dict)
    
     


     def get_groups(self):
        d = self.sort_animals()
        for animal in d.values():
            print(animal)


ramat_gan_safari = Zoo('Ramat gan')
ramat_gan_safari.add_animal('monkey')
ramat_gan_safari.add_animal('tiger')
ramat_gan_safari.add_animal('goose')
ramat_gan_safari.add_animal('snake')
ramat_gan_safari.add_animal('epple')
ramat_gan_safari.add_animal('elephant')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('monkey')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()