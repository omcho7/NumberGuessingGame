import time
import os
import random


def Level1(x):
    from LevelTwo import Level2
    from MiscFunc import save_progress, typewriterF, typewriterS

    # Level 1
    typewriterS("Welcome adventurer!\n")
    typewriterS(
        "After your late father left a note, giving you the knowledge of a long lost family treasure, you become eager to find it."
    )
    typewriterS(
        "Filled with determination, you begin your journey in the land of Falconia."
    )
    typewriterS(
        "Asking the townsfolk about the path ahead, they inform you to head south through the haunted forest out of town.\n"
    )
    typewriterS(
        "Armed with a map, a sword and a lions heart, you make your way through the forest keeping an eye on any foes.\n"
    )
    typewriterF(
        "Suddednly a werewolf stops you on your path! 'Back where you came from, or face your doom!'"
    )
    time.sleep(1)
    typewriterF("He leaps at you! Counter with your sword!\n")
    damage = int(input("Enter a number 1-" + str(x) + ": "))
    monster1 = random.randint(1, x)
    print(monster1)
    if abs(monster1 - 1) <= damage <= monster1 + 1:
        typewriterS(
            "The beast is defeated! You have proved yourself and continue the journey.\n"
        )
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
        typewriterF(
            "No, you have missed! Fortunately the monster tripped, you get another chance!"
        )

        # Hint if the first guess is wrong
        if monster1 > damage:
            typewriterF("Attack with more power!")
        else:
            typewriterF("Less power, more technique!")

        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(monster1 - 1) <= damage <= monster1 + 1:
            typewriterS(
                "The beast is defeated! You have proved yourself and continue the journey."
            )
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
            typewriterS("No luck! Attack was too weak and you have been defeated.")
            save_progress(
                {"level": 1}
            )  # Player fails, progress is set to the level that is failed.
