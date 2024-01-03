import os
import time
import random
import json
from MiscFunc import StartGame


def Difficulty():
    print("-----------Choose Difficulty-----------")
    print("\n")
    print("           1. Easy (1 - 10)            ")
    print("           2. Medium (1 - 20)          ")
    print("           3. Hard (1 - 30)            ")
    print("\n")

    diffchoice = int(input("Choose option (1, 2, 3): "))

    if diffchoice < 1 or diffchoice > 3:
        while diffchoice < 1 or diffchoice > 3:
            diffchoice = int(input("Incorrect value, choose option (1, 2, 3): "))
    else:
        if diffchoice == 1:
            x = 10
            print("\nChosen difficulty: 1\n")
        elif diffchoice == 2:
            x = 20
            print("\nChosen difficulty: 2\n")
        elif diffchoice == 3:
            x = 30
            print("\nChosen difficulty: 3\n")
        time.sleep(1.5)
        os.system("cls")
        return x


def MainMenu():
    print("---------------Main Menu---------------")
    print("\n")
    print("             1. New Game               ")
    print("         2. Continue Last Save         ")
    print("                3. Exit                ")
    print("\n")
    mmchoice = int(input("Choose option (1, 2, 3): "))

    while mmchoice != 1 and mmchoice != 2 and mmchoice != 3:
        mmchoice = int(input("Incorrect value, choose option (1, 2): "))

    if mmchoice == 1:
        os.system("cls")
        x = Difficulty()
        StartGame(x, new_game=True)
    if mmchoice == 2:
        os.system("cls")
        x = Difficulty()
        StartGame(x)
    elif mmchoice == 3:
        exit()


MainMenu()
