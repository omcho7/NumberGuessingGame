import time
import os
import random


def Level1(x):
    from LevelTwo import Level2
    from MiscFunc import save_progress

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
            Level2(x)  # Player chooses to continue, goes to Level 2, progress is saved.
        elif playerinp == 2:
            save_progress({"level": 2})
            exit()  # Player chooses to exit, terminates program, progress is saved.

    else:
        print(
            "No, you have missed! Fortunately the monster tripped, you get another chance!"
        )

        # Hint if the first guess is wrong
        if monster1 > damage:
            print("Attack with more power!")
        else:
            print("Less power, more technique!")

        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(monster1 - 1) <= damage <= monster1 + 1:
            print("The beast is defeated! You continue your journey.")
            playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))

            if playerinp == 1:
                time.sleep(2)
                os.system("cls")
                save_progress({"level": 2})
                Level2(
                    x
                )  # Player chooses to continue, goes to Level 2, progress is saved.

            elif playerinp == 2:
                save_progress({"level": 2})
                exit()  # Player chooses to exit, terminates program, progress is saved.
        else:
            print("No luck! Attack was too weak and you have been defeated.")
            save_progress(
                {"level": 1}
            )  # Player fails, progress is set to the level that is failed.
