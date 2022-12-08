class Farm:
    def __init__(self, name):
     self.name = name 
     self.animals = {}
     self.li = []

     
 

def add_animal(self, animal, quantity):
        self.li.append(animal)
        if quantity == 1:
            self.animals[animal] = self.li.count(animal)
        else:
            self.animals[animal] = quantity

def get_animal_types(self):
        new_li = []
        for key in self.animals.keys():
            new_li.append(key)
        new_li.sort()
        return new_li
        
def get_info(self):
        print(f'{self.name}\'s farm\n')
        for key, value in self.animals.items():
            print(f'{key} : {value}')
        return '\n    E-I-E-I-0!'

def get_short_info(self):
        animal_li = self.get_animal_types()
        x,y,z = animal_li
        return f'{self.name} has {x}s, {y}s and {z}.'











macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_animal_types()
print(macdonald.get_short_info())

print(macdonald.get_info())