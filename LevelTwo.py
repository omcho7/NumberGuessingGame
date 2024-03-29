import time
import os
import random


def Level2(x, current_points):
    from MiscFunc import save_progress, typewriterF, typewriterS
    from LevelThree import Level3
    from Mechanics import Combat

    typewriterS(
        "It seems there is more to you than meets the eye, wandering warrior.\n"
    )

    typewriterS(
        "As you continue your journey, traversing through murky swamps, you drop your guard for one second...\n"
    )
    time.sleep(0.5)
    typewriterF(
        "A possesed tree hits you with its branch from behind! You are knocked back. Quickly, cut the branch with your sword!\n"
    )

    success, points = Combat(x, 4, current_points)

    if success:
        current_points += points
        typewriterF("But that won't take it down, attack the other branch!\n")

        success2, points2 = Combat(x, 4, current_points)

        if success2:
            current_points += points2
            typewriterF("Outstanding! Now aim for its head!\n")

            success3, points3 = Combat(x, 4, current_points)

            if success3:
                current_points += points3

                typewriterS(
                    "The demonic tree fades into obsolesence! Amazing work brave traveller, continue your journey.\n"
                )

                playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
                if playerinp == 1:
                    time.sleep(2)
                    os.system("cls")
                    save_progress({"level": 3, "points": current_points})
                    Level3(
                        x, current_points
                    )  # Player chooses to continue, goes to Level 2, progress is saved.
                elif playerinp == 2:
                    save_progress({"level": 3, "points": current_points})
                    exit()  # Player chooses to exit, terminates program, progress is saved.

        else:
            typewriterS(
                "No luck! While damaged, the tree manages to get the upper hand and knocks you out."
            )
            save_progress({"level": 2, "points": 0})

    else:
        typewriterS(
            "No luck! You missed and the tree knocks you unconcious, ending your journey prematurely."
        )
        save_progress(
            {"level": 2, "points": 0}
        )  # Player fails, progress is set to the level that is failed.
