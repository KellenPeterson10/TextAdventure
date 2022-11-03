import os
from os import *
import time
def clear():
    os.system("cls")
clear()
start()


def start():
    clear()
    print("You enter a doungoen and have 4 options of weapons to choose from. ")
    q1()

def q1():
    time.sleep(3)
    print("What weapon do you want to choose?")
    if q1 == ("1,2,3,4"):
        time.sleep(3)
        q2()

def q2():
    print("What item do you want to choose?")

def q3():
    print("What pet do you want to choose?")

