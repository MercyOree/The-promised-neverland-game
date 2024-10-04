#Section_2
#Mercy O. koku
#11/5/22
#Through the children's journey an underground passage in the demon forest.
#The children discover a Promised Pen functions as a key to shelter.

#import main_character and section_2 here
import main_character
import section_3
from main_character import mc
import battle as battle


def start(player):
    print("")
    print("During your journey of escape you discover a promised pen shelter in a underground passage but you meet a old orphange who threntens to kill you siblings ")
    print("Would you like to defeat him or run away?")
    print("section 2 " + player.name)
   
    choice = int(input("1. Runaway 2.Beg  3. Defeat and tie him up: "))
    if choice == 1:
        print("You runaway but you and your siblings face demons")
        choice = input("Would you like to use a weapon to defeat the demon? Y/N ")
    if choice == 'Y':
        print("I will defeat you! Gain +2 Inventory points: ",mc.points)
        print("+1 Inventory bond points: ", mc.sibling_bond)
        #The player tries to kill the demon but he insist to help you
        #The demon talks to the player and helps you gain strength
        print("Your inventory contains a stick" ,mc.inventory)
        print("You defeat the monster with a sharp stick and gain strength")
        print("You try to kill the demon but the demon insist to help you")

    elif choice == 2:
        print("You beg the man to help you and your siblings to find clues in the pen")
        print("You find your siblings dead and find out the man betrayed you, ",mc.attack)
        #The man decides to help you but betrays you by killing your siblings.
        print("You choose to defend the demon independently, your journey begins to get tougher")
        print("Let's stop and check to if the clue we have to find William is enough, 10 clues is enough to lead your path to him. ")
        number = int(input("Enter the amount of clue you came up with: "))

        if number <= 10:
            print('Yikes, try looking for more clues on your journey!')
        elif number > 10 and number < 100:
            print("You have a long list of clues and the key that leads you to William Minerva!")
        else:
            print("Ouch! Try selecting weapons and survival kits as you move along")
    else:
        print("Defeat him, Tie him up in a closet and gain strength +5, Inventory Hp:",mc.hp )
        print("You go back to the pen collect all the weapons, clues and survival kit")
        print()
        #If he ends up coming back kill him,



    #The next section will start in:
    section_3.start(player)

 
    #Pseudocode
    # print("You and your siblings come across a demon")
    #   choice = input("The player try to convince the demon to help you and your siblings defeat the man")

    # print ("The more you defeat the demons or find a survival item you earn 5 coins.")
    #  import main_character
    #         print("You gained 5 coins " ,main_character)
    #         print("You defeat the monster you gain 5 coins")
