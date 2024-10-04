#Section_1
#Mercy O. koku
#11/5/22
#One night, a girl named Conny is sent away by mother Isabella to be adopted.

#import main_character and section_2 here
import main_character
import section_2
from main_character import mc
import battle as battle



def start(player):
    print("When three gifted kids at an isolated peaceful orphanage in Grace Field House discover the secret and purpose they were raised for,")
    print("They look for a way to escape from their evil caretaker and lead the other children in a risky escape plan.")
    print("At the gate, The orphans find Conny dead and discover the truth about their existence.")
    print("")
    print("What would you like to do, to escape being next?")
    print("section 1 " + player.name)

    #Give the player some options of things to do here.
    #Be sure to put their choice in a variable!
    choice = int(input("1. Inform the mother 2. Inform the orphans 3. Escape to the outside world: "))
    if choice == 1:
        print("You come across the mother she suspect you know something")
        choice = input("Inform and resist the mother to stop killing the orphans? Y/N ")
        if choice == 'Y':
            print("You and your siblings come up with a plan to kill the mother and inform her")
            print("Why are you killing my siblings?")
        choice = input("Try to poison the mother when dinner occurs Y/N")
        if choice == 'Y':
                print("You defeated the mother you gained 5+ points! Inventory point: ",mc.points)
                print("Time to escape out onto the forest.")
        elif choice == 'N':
            print("The mother has a chance of defeating you, sending the demons to eat you")
        # The mother sends a monster to attack you, player begins to escape from the mother
        # If the player defeat the demons trying to eat her, they'll receive a coins!

    elif choice == 2:
        print("You inform the orphans and they all look frighten")
        # Let the player see what ideas the orphans come up with staying or escape to defeat the demons
        print("Although with the scary news your sibling comes up with clues to survival")
        print("You begin gathering weapons as you face the forest of demons")
        import random
        weapon = ["stick", "rock", "mace"]
        print("You have can now defeat the demon with list of options " ,weapon)
        print("You randomly choose", random.choice(weapon),"you gain 5+ points",mc.points)
    else:
        print("You decide to escape to the outside world with your siblings")
        print("During your journey to escape if you end up with not enough survival items,")
        print("Try to find and consume them while on your journey battling demons to,")
        print()
        print("While random selecting weapons you come across a few that is defeatable to your enemy ")
        print("To see how close you are to facing a battle ")
        import math

        x1 = 700
        y1 = int(input("Enter the First Point Coordinate  = "))
        x2 = int(input("Enter the Second Point Coordinate = "))
        y2 = int(input("Enter the Third Point Coordinate = "))

        x = math.pow((x2 - x1), 2)
        y = math.pow((y2 - y1), 2)

        print(x)
        print(y)
        print(math.sqrt(x + y))
        distance = math.sqrt(x + y)

        print('The distance points between you and the demons are = {0} Units'.format(distance))








    #The next section will start in:
    section_2.start(player)
    

    #Pseudocode
    # print("You and your siblings come up with a plan to kill the mother")
    #   choice = input("Try to poison the mother when dinner occur")

    # print ("Learn new strength and survival abilities.")
    # print ("The player can gain coins or strength through her journey to the outside world")



