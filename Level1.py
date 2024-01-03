import time
import os
import random


def Level1(x):
    # Level 1
    print("Welcome to your adventure!\n")
    print("Monster #1 attacks you! Roll a number to do damage!\n")
    damage = int(input("Enter a number 1-" + str(x) + ": "))
    monster1 = random.randint(1, x)
    print(monster1)
    if abs(monster1 - 1) <= damage <= monster1 + 1:
        print("The beast is defeated! You continue your journey.\n")
        playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
        if playerinp == 1:
            time.sleep(2)
            os.system("cls")
            save_progress({"level": 2})
            Level2(x)
        elif playerinp == 2:
            save_progress({"level": 2})
            exit()

    else:
        print(
            "No, you have missed! Fortunately the monster tripped, you get another chance!"
        )
        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(monster1 - 1) <= damage <= monster1 + 1:
            print("The beast is defeated! You continue your journey.")
            playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
            if playerinp == 1:
                time.sleep(2)
                os.system("cls")
                save_progress({"level": 2})
                Level2(x)
            elif playerinp == 2:
                save_progress({"level": 2})
                exit()
        else:
            print("No luck! Attack was too weak and you have been defeated.")