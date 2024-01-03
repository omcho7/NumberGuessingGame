import os
import time
import random

def Difficulty():
    print("-----------Choose Difficulty-----------")
    print("\n")
    print("           1. Easy (1 - 10)            ")
    print("           2. Medium (1 - 20)          ")
    print("           3. Hard (1 - 30)            ")
    print("\n")
    diffchoice = int(input("Choose option (1, 2, 3): "))


    if diffchoice < 1 or diffchoice > 3:
        while (diffchoice < 1 or diffchoice > 3):
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
        os.system('cls')
        return x



def StartGame(x):
    print("Welcome to your adventure!\n")
    print("Monster #1 attacks you! Roll a number to do damage!\n")
    damage = int(input("Enter a number 1-" + str(x) + ": "))
    monster1 = random.randint(1,x)
    print(monster1)
    if abs(monster1-1) <= damage <= monster1+1:
        print("The beast is defeated! You continue your journey.")
    else:
        print("No, you have missed! Fortunately the monster tripped, you get another chance!")
        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(monster1-1) <= damage <= monster1+1:
            print("The beast is defeated! You continue your journey.")
        else:
            print("No luck! Attack was too weak and you have been defeated.")




def MainMenu():
    print("---------------Main Menu---------------")
    print("\n")
    print("             1. Start Game             ")
    print("                2. Exit                ")
    print("\n")
    mmchoice = int(input("Choose option (1, 2): "))
    
    while (mmchoice != 1 and mmchoice != 2):
            mmchoice = int(input("Incorrect value, choose option (1, 2): "))

    if mmchoice == 1:
        os.system('cls')
        x = Difficulty()
        StartGame(x)
    elif mmchoice == 2:
        exit()


MainMenu()



    





