#main_game.py
#Mercy O.koku
#11/5/2022
#This file will run the whole game and gets the game started. 
#This start function is called by main_game, Also needs the player character as an input in order to interact with them.


#Import the main character and section files here
import main_character
import section_1



#Introduction text to the user
print("Welcome to the promised neverland!")
print("Click on 1 then press enter to wake up the game ")
input()

#1.Start the game
#2.Quit the game
Choice = int(input("Choose 1 to 'start' and begin or 2 to 'quit' the journey: "))
mode = "Invalid choice" # Set a default value
if (Choice == 1):
  mode = "begin our journey"
elif (Choice == 2):
  mode = "quit, Goodbye."
  quit("You choose to quit, Goodbye.")
print("You choose to" , mode)


#Welcoming the player
name = input('Enter you name: ')
print("Hello", name,"let's begin our journey!")

#And do/say anything else to get your game started
print("Let's go on an horrific journey")
print("")
#Then call your first section.

#Create the player character
print("The main character name is ",main_character.mc.name)
#This code will let your user name the character
#This is how you'll use the attributes in your main character file in the rest of the secctions
main_character.mc.name = input("What do you want to name your character?")
print("")
print("Welcome " + main_character.mc.name + "!")
print("Level 1 is our first journey")

#And do/say anything else to get your` game started.
#For example, intro narration, setting other player character values,
#   establishing NPCs, etc.

#Then call your first section.
#Pass the variable with your main_character as a parameter.


section_1.start(main_character.mc)








