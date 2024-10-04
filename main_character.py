#main_character.py
#Mercy O.koku
#11/5/2022
#This file is a class that defines the character with the variables.
#Emma often proves herself to be one of the most reliable orphans.
#She is known for her incredible ability to learn and capable athleticism.

#import main_character



class main_character:
    name = "Emma"
    points = ["15"]
    attack = ["An enemy, attack!"]
    hp = 10
    inventory = ["Stick"]
    sibling_bond = ["10"]
    weapon = ["mace"]
global mc
mc =main_character
#print(mc.name)

#Functions in a class need to take "self" as a parameter like this.
#Watch your indentations!
    # def attack(self):
    #     print("You attack the monster!")
    #     print("You get hit by the monster!")
    #     #This will reduce the value of hp by 1
    #     #You'll need to add "self." in front of any variables
    #     #   in the class
    #     self.hp -= 1