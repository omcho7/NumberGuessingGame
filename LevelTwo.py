import time
import os
import random


def Level2(x):
    from MiscFunc import save_progress

    print("It seems there is more to you than meets the eye, wandering warrior.\n")
    time.sleep(2)
    print(
        "As you continue your journey, traversing through murky swamps, you drop your guard for one second...\n"
    )
    time.sleep(3)
    print(
        "A possesed tree hits you with its branch from behind! You are knocked back.\n"
    )
    time.sleep(2)
    print("Quickly, cut the branch with your sword!")
    damage = int(input("Enter a number 1-" + str(x) + ": "))
    tree = random.randint(1, x)
    print(tree)

    # First try
    if abs(tree - 1) <= damage <= tree + 1:
        print(
            "Success! But that won't take it down. Attack again while it is recovering!"
        )
        tree1 = random.randint(1, x)
        print(tree1)
        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(tree1 - 1) <= damage <= tree1 + 1:
            time.sleep(1)
            print(". . . .")
            time.sleep(3)
            print(
                "The demonic tree fades into obsolesence! Amazing work brave traveller, continue your journey."
            )
            playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
            if playerinp == 1:
                time.sleep(2)
                os.system("cls")
                save_progress({"level": 3})

            elif playerinp == 2:
                save_progress({"level": 3})
                exit()
        else:
            print(
                "No luck! While damaged, the tree manages to get the upper hand and knocks you out."
            )

    # Second try
    else:
        print("No, you have missed! Attack the other one while it's recovering!")
        print(tree)
        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(tree - 1) <= damage <= tree + 1:
            print(
                "Success! But that won't take it down. Attack again, don't let the beast rest!"
            )
            tree2 = random.randint(1, x)
            print(tree2)
            damage = int(input("Enter a number 1-" + str(x) + ": "))
            if abs(tree2 - 1) <= damage <= tree2 + 1:
                time.sleep(1)
                print(". . . .")
                time.sleep(3)
                print(
                    "The demonic tree fades into obsolesence! Amazing work brave traveller, continue your journey."
                )
                playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
                if playerinp == 1:
                    time.sleep(2)
                    os.system("cls")
                    save_progress({"level": 3})

                elif playerinp == 2:
                    save_progress({"level": 3})
                    exit()
            else:
                print(
                    "No luck! While damaged, the tree manages to get the upper hand and knocks you out."
                )

        else:
            print(
                "No luck! You missed and the tree knocks you unconcious, ending your journey prematurely."
            )
