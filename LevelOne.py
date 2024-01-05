import time
import os
import random


def Level1(x, current_points):
    from LevelTwo import Level2
    from MiscFunc import save_progress, typewriterF, typewriterS
    from Mechanics import Combat

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
        "Suddenly a werewolf stops you on your path! 'Back where you came from, or face your doom!'"
    )
    time.sleep(1)
    typewriterF("He leaps at you! Counter with your sword!\n")

    # After the narrative, the combat (number-guessing part) begins:

    success, points = Combat(x, 4, current_points)

    if success:
        current_points += points
        typewriterF("But that won't take it down, quickly strike again!")

        success2, points2 = Combat(x, 4, current_points)

        if success2:
            current_points += points2
            typewriterS(
                "The beast is defeated! You have proved yourself and continue the journey.\n"
            )
            playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
            if playerinp == 1:
                time.sleep(2)
                os.system("cls")
                save_progress({"level": 2, "points": current_points})
                Level2(
                    x, current_points
                )  # Player chooses to continue, goes to Level 2, progress is saved.
            elif playerinp == 2:
                save_progress({"level": 2, "points": current_points})
                exit()  # Player chooses to exit, terminates program, progress is saved.

        else:
            typewriterS(
                "Unfortunately, you fail at your attempt to finish off the beast. Your journey ends before it could properly begin."
            )
            save_progress({"level": 1, "points": 0})

    else:
        typewriterS(
            "Unfortunately, the sword proved too heavy for your fragile hands, you miss every swing and succumb to the beasts attacks. \n Your journey ends before it could properly begin."
        )
        save_progress(
            {"level": 1, "points": 0}
        )  # Player fails, progress is set to the level that is failed.
