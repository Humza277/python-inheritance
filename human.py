# parent class
class Human:
    # method initializes the variables
    def __init__(self, eye_color, skin_color, hair_color):
        self.eye_color = eye_color
        self.skin_color = skin_color
        self.hair_color = hair_color

    # method prints out the variable
    def inputDetails(self):
        print("Your eye color is " + self.eye_color)
        print("Your skin color is " + self.skin_color)
        print("Your hair color is " + self.hair_color)

