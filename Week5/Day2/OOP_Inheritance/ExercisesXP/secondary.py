# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from main import Dog

class PetDog(Dog):
    def __init__(self,trained):
        self.trained=trained
        trained=False
    def train(self):
        print(f"{self.bark}")
        self.trained=True
    def play(self,*Dog):
        print(f"{self.dog_name} all play together")
    
    def do_a_trick(self):
        if self.trained==True:
            dog_sentences=[f"{self.dog_name} does a barrel roll",f"{self.dog_name} stands on his back legs",f"{self.dog_name} shakes your hand",f"{self.dog_name} plays dead"]
            print(dog_sentences.shuffle())