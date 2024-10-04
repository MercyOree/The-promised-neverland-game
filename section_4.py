# Section_4
# Mercy O. koku
# 11/5/22
# Using the pen, Emma and Lucas unlock William Minerva's secret door. William Minerva give them the key clues to the outside would
# Within seven months after journeying to the Western Lands,
# You and your siblings found the Golden Waters and the Temple.

# import main_character and section_3 here
import main_character
from main_character import mc
import section_3
import battle as battle



def start(player):
    print("")
    print("You meet William, he give you the clues to outside world.")
    print("You are almost there!")
    print("While looking for weapons you hear a scream one of your siblings surrounded by demons ")


    print("section 4 " + player.name)

    choice = int(input("1. Look for weapons to defeat the demons 2. Distract the demons to try and attack you instead 3. Disregard this situation: "))
    if choice == 1:
        print("You're frightened, you quickly look for weapons to defeat the demons")
        choice = int(input("1. stick, 2. rock, 3. antler, 4. gun"))
        if choice == 1:
            print("You find a stick and defeat the demons")
        if choice == 2:
            print("You find a rock and defeat the demons")
        if choice == 3:
            print("You find a antler and defeat the demons")
        if choice == 4:
            print("You find a gun and defeat the demons")
        print("Gain +2 sibling bond points. Inventory bond points: ", mc.sibling_bond)
        print("You were just on time to defeat the demons great job! Making your way to the outside would!")


    elif choice == 2:
        print("You decide to distract the demons to attack you instead of your sibling")
        print("You try to defeat the demons while come after you and attack, You must be fast!")
        seconds = 10
        while seconds < 10:
            print("You have  ", seconds)
            print("you must hurry up!")
            seconds += 60
        print("Your inventory contains a stick",mc.inventory)
        print("You defeat the monster with a sharp stick and gain strength. Inventory points: ", mc.points)
        print("Gain +2 sibling bond points. Inventory bond points: ",mc.sibling_bond)
        print("You were just on time to defeat the demons and save your sibling great job!")
        print("Making your journey completed to the outside would!")

    else:
        print("Disregard this situation ")
        print("Would you like to reconsider fighting the demons to save your sister?")
        choice = int(input("you will lose points leaving your sibling behind? (1) for yes or (2) for No "))
        if choice == 1:
            print("You choose to save your sibling, Facing the demons. As you guys head to the outside world +2 points Inventory points: ",mc.points)
            print("Yay! You have now made to the outside world saving your bothers and sisters. Good job +10 points Inventory points: ", mc.points )
            quit("")
        if choice == 2:
            print("You fail at saving your siblings as you head to the outside world, you lose -2 points")
            print("Loosing a sibling bond with your siblings. Inventory points:",mc.points)
            print("You have now made it to end of the game! Inventory points: ", mc.points)
        else:
            mc.points = 15
            while mc.points > 0:
                mc.points -= 5

            if mc.points <= 0:
                print("Game over!")
                exit()







        # The player begins to follow the journey to the outside world sucessfully
        # If looses then the player can start the game over or quit

        # This is the end of section 4 you can restart the game or this section:


    # Pseudocode
    # print("You and your siblings make it to the outside world, you end up lost. You lose")
    #   choice = input("The player goes on a search for her siblings")