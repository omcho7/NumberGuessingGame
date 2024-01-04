import time
import os
import random


def Level3(x):
    from MiscFunc import save_progress

    print(
        "The days ahead seem long and wary, how long until the famous treasure is in sight.\n"
    )
    time.sleep(2.5)
    print(
        "Nobody knows, perhaps because little to no man tried his luck on this path...\n"
    )
    time.sleep(2.5)
    print("Or none have lived to tell the tale...")
    time.sleep(2)
    print(
        "Before you, two paths are given, one leading over the fiery depths of Mount Blaviken (1),"
    )
    print(
        "the other, through the ice giant Kingdom of Kaldur (2), which do you choose?"
    )

    path = int(input("Choose a path (1 or 2): "))

    if path != 1 and path != 2:
        while path != 1 and path != 2:
            diffchoice = int(input("Incorrect value, choose option (1 or 2): "))

    else:
        if path == 1:
            os.system("cls")
            time.sleep(1)
            print(
                "The flame in your heart, burning for the thrill sets you out on the trail over Mount Blaviken."
            )
            time.sleep(2)
            print(
                "On your way you encounter a scaly red dragon, stopping you from getting over the bridge to your next destination."
            )
            print(
                "It lets out a loud roar, spewing fire out to the sky. It looks at you with yellow eyes of superiority, and asks you:\n"
            )
            print(
                "Foolish soul, I have heard of your mission to uncover the treasure of our lands. If you answer my riddle, I will let you through."
            )
            print("If not, ")
            time.sleep(2)
            print(
                "I will let out my wrath onto your poor kind, and feed myself to a fine lunch."
            )
            daughters = random.randint(1, x)
            brothers = random.randint(1, x)
            print(
                "My father, the dragon king, has ",
                daughters,
                " princess daughters, waiting for his throne. Each of them has ",
                brothers,
                " older dragon brothers.",
            )
            answer = int(
                input(
                    "How many descendants will have a chance at the kings pedestal? :"
                )
            )
            if answer != brothers:
                time.sleep(1)
                print(". . . .")
                time.sleep(3)
                print(
                    "Wrong you fool! - the Dragon exclaims, burning you to a fine crisp and ending your journey in the bowels of the beast."
                )
                save_progress({"level": 3})
                exit()

            else:
                time.sleep(1)
                print(". . . .")
                time.sleep(3)
                print(
                    "You seem more intelligent than you look. I will let you through this time, struggler.\n"
                )
                time.sleep(2)
                print(
                    "Success! That was a close one, best of luck warrior, you are getting closer and closer to your goal."
                )
                playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
                if playerinp == 1:
                    time.sleep(2)
                    os.system("cls")
                    save_progress({"level": 4})
                    Level3(x)
                elif playerinp == 2:
                    save_progress({"level": 4})
                    exit()

        elif path == 2:
            os.system("cls")
            time.sleep(1)
            print(
                "I see your heart is cold and unruly to the dangers ahead of Kingdom of Kaldur, brave one."
            )
            time.sleep(2)
            print(
                "You traverse through their town, filled with towering ice beings, but seemingly not hostile towards you."
            )
            print("Perhaps you are just a lost insect in their world.")
            time.sleep(2)
            print(
                "You find the exit gate. Thank god, you must think. Managed to escape without any conflict."
            )
            time.sleep(2)
            print(
                "Unfortunately two frost giants, each 15 meters tall, are seen guarding the thick steel gate leading out of the town."
            )
            print(
                "One says to the other: 'It seems that we have a tresspassing guest within our tribe. Let's have fun with this one'.\n"
            )
            print(
                "'Foolish soul, I have heard of your mission to uncover the treasure of our lands. If you answer our riddle, I will let you through.'"
            )
            print("'If not, ")
            time.sleep(2)
            print(
                "'Us ice giant have a sweet spot in our stomachs for human meat. So riddle me this tiny man:' "
            )
            daughters = random.randint(1, x)
            brothers = random.randint(1, x)
            print(
                "'My father, Lord Bjorn, ice heart of Kaldur, has ",
                daughters,
                " princess daughters, waiting for his throne. Each of them has ",
                brothers,
                " older frost giant brothers.",
            )
            answer = int(
                input(
                    "How many descendants will have a chance at the kings pedestal? :"
                )
            )
            if answer != brothers:
                time.sleep(1)
                print(". . . .")
                time.sleep(3)
                print(
                    "Wrong you fool! - the giant exclaims, trapping and freezing you to death. He splits the share and eats you with his other ice giant comrades."
                )
                save_progress({"level": 3})
                exit()

            else:
                time.sleep(1)
                print(". . . .")
                time.sleep(3)
                print(
                    "Hmm, You seem more intelligent than you look. I will let you through this time, struggler.\n"
                )
                time.sleep(2)
                print(
                    "Success! That was a close one, best of luck warrior, you are getting closer and closer to your goal."
                )
                playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
                if playerinp == 1:
                    time.sleep(2)
                    os.system("cls")
                    save_progress({"level": 4})
                    Level3(x)
                elif playerinp == 2:
                    save_progress({"level": 4})
                    exit()
