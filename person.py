# Imports the human file
from human import *


class Person(Human):  # inherits characteristics from Human
    def __init__(self, eye_color, skin_color, hair_color, nose):
        super().__init__(eye_color, skin_color, hair_color)
        self.nose = nose  # unique to person only

    def printhuman(self):  # method is unique to Person
        self.inputDetails()
        print("Your nose is " + self.nose)


x = Person("Black", "Brown", "Blond", "crooked")  # inputs the variables for the characteristics
print(x.printhuman())  # prints out the result
