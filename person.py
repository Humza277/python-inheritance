from human import *


class Person(Human):
    def __init__(self, eye_color, skin_color, hair_color, nose):
        super().__init__(eye_color, skin_color, hair_color)
        self.nose = nose

    def printhuman(self):
        self.inputDetails()
        print("Your nose is " + self.nose)


x = Person("Black", "Brown", "Blond", "crooked")
print(x.printhuman())
