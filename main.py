import os
from os import *

def clear():
    os.system("cls")



begining = input("You are Walter Jr. a 14 year old boy with cerebral palsy. You wake up grab your crutches and walk down the hallway to your kitchen where you greet your mother Skylar and your father Walter. You pull a chair out and sit down at the table.\n\n Do you eat your breakfast?  ")

def chooseYes():    
    clear()
    print("You eat your eggs and bacon and it gives you the energy you need to make it through the day.")

if begining == "Y":
    chooseYes()
else:
    print("You dont eat your breakfast and you go hungry for the day.")


question1 = input("")














