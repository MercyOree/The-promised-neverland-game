#Section_3
#Mercy O. koku
#11/5/22
#The orphan children discover an archive and come across a letter signed by Willam Minerva
#In one of the books. They begin a search for Willam Minerva so give them answer for the outside world.

# import main_character and section_3 here
import main_character
import battle as battle
from main_character import mc
import section_4


def start(player):
    print("")
    print("You discover an archive, Come across the letter by a man with answers.")
    print("Are you willing to look for survival?")
    print("section 3 " + player.name)
    
    choice = int(input("1. Be independently meet at outside world  2. Use you and sibling ideas 3. Look for the man who owns the letter: "))
    if choice == 1:
        print("You and your siblings decide to go independent, You end up facing a demon")
        choice = input("I'll defeat you to protect by siblings! Y/N")
        if choice == 'Y':
            print("You won't harm me!,+5 strength, Inventory hp: ", mc.hp)
            print("Gain +2 sibling bond points. Inventory bond points: ", mc.sibling_bond)
        # Try to defeat the demon so the demon does not go back to harm you.
        # If the player defeats the demon then you gain strength!
        import random
        weapon = ["stick", "rock", "Bow & Arrow", "stone", "antler", "gun", "mace"]
        print("demon get defeated with a",random.choice(weapon),)
        print("You have now defeated the demon")

    elif choice == 2:
        print("Use you and sibling ideas and face escaping to the outside world")
        print("defeat the monster while following the clue on the letter to survival")
        time = 9
        while time < 12:
            print("check the time to see if you are running out of time before midnight")
            print(" ", time)
            print("you must hurry up!")
            time += 12
        # Let the player get clues from your siblings for the outside world.


    else:
        print("Look for William Minerva who owns the letter to find your way to the outside world.")
        print("The player begins to follow the journey to find William on their way to destiny in the outside world")
        print("")
        print("Let's stop and check to see if we have more then 6 weapons to keep you and your sibling alive. ")
        number = int(input("Enter the amount of weapons and survival kits you have: "))

        if number <= 5:
            print('Oh no, try selecting weapons on your journey!')
        elif number > 5 and number < 100:
            print("You have just the right amount of weapons to keep you and your siblings alive!")
        else:
            print("Ouch! Try selecting weapons and survival kits as you move along")


        
        # The player begins to follow the journey to find William
        # While on your journey use your weapons to fight demons to make it to the outside world.

        # This is the end of section 3 you can restart the game or this section:
    section_4.start(player)

    #Pseudocode
    # print("You and your siblings make it to the outside world, you end up lost")
    #   choice = input("The player goes on a search for her siblings")