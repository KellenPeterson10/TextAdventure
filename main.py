import os
from os import *

def clear():
    os.system("cls")
clear()

def start():
    clear()
    beginning

beginning = input("Welcome to DingleTron Into The Dingle-Verse!\n \n \nDo you want to start the game?\n \n \n")


def chooseYes():    
    clear()
    print("The year is 2400 b.c. \n \n \nYou are a lone dingle asleep in a small dingle apartment. You hear a loud smash in your home do you investigate? \n \n")

if beginning == "Y":
    chooseYes()
elif beginning == "N":
    clear()
    print("You cant start the game if u dont put yes!")
else:
    clear()
    print("INVALID ANSWER")
    start()

question1 = input() 


def chooseYes2():
    clear()
    print("You walk out of your room and down your hallway into your kitchen and see a racoon!\n \n \nDo you try to fight the racoon? \n \n")
if question1 == "Y":
  chooseYes2()
elif question1 == "N":
    clear()
    print("You stay in your room thinking about what might be making the noise and try to fall back asleep. \n \n")
    question12 = input("Do you stay in bed? \n \n \n")
else:
    print("INVALID ANSWER")


question2 = input()


def chooseYes3():
    clear()
    print("You punch the trash panda in the throat and throw it out your balcony window.\n \n \nYou feel sad and happy at the same time. Do you get up for work? \n \n")


if question2 == "Y":
    chooseYes3()
elif  question2 == "N":
    clear()
    print("You befriend the racoon and name him jim. \n \n \n")
else:
    clear()
    print("INVALID ANSWER")


def chooseYes12():
    clear()
    





