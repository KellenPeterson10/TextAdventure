import os
from os import *

def clear():
    os.system("cls")
clear()


begining = input("Welcome to DingleTron Into The Dingle-Verse!\n \n \nDo you want to start the game?\n \n \n")

def chooseYes():    
    clear()
    print("The year is 2400 b.c. \n \n")

if begining == "Y":
    chooseYes()
else:
    print("You cant start the game if u dont put yes!")


question1 = input("You are a lone dingle asleep in a small dingle house. You hear a loud smash in your home do you investigate? \n \n \n") 


def chooseYes2():
    clear()
    print("You walk out of your room and down your hallway into your kitchen and see a racoob!\n \n \nDo you try to fight the racoob? \n \n \n")
 


if question1 == "Y":
  chooseYes2()
else:
    clear()
    print("You stay in your room thinking about what might be making the noise and eventually fall back asleep. \n \n ")


question2 = input("")












