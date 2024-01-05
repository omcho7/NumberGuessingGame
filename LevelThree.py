import time
import os
import random


def Level3(x, current_points):
    from LevelFour import Level4
    from MiscFunc import save_progress, typewriterF, typewriterS, typewriterSNL
    from Mechanics import Combat

    typewriterS(
        "The days ahead seem long and wary, how long until the famous treasure is in sight."
    )

    typewriterS(
        "Nobody knows, perhaps because little to no man tried his luck on this path..."
    )

    typewriterS("Or none have lived to tell the tale...\n")

    typewriterS(
        "Before you, two paths are given, one leading over the fiery depths of Mount Blaviken (1),"
    )
    typewriterS(
        "the other, through the ice giant Kingdom of Kaldur (2), which do you choose?"
    )

    path = int(input("Choose a path (1 or 2): "))

    if path != 1 and path != 2:
        while path != 1 and path != 2:
            diffchoice = int(input("Incorrect value, choose option (1 or 2): "))

    else:
        # If chosen path is 1

        if path == 1:
            os.system("cls")
            time.sleep(1)
            typewriterS(
                "The flame in your heart, burning for the thrill sets you out on the trail over Mount Blaviken."
            )

            typewriterS(
                "On your way you encounter a scaly red dragon, stopping you from getting over the bridge to your next destination."
            )
            typewriterS(
                "It lets out a loud roar, spewing fire out to the sky. It looks at you with yellow eyes of superiority, and exclaims:\n"
            )
            typewriterS(
                "'Foolish soul, I have heard of your mission to uncover the treasure of our lands. If you answer my riddle, I will let you through."
            )
            typewriterS("If not, ")

            typewriterS(
                "I will let out my wrath onto your poor kind, and feed myself to a fine lunch.'\n"
            )

            daughters = random.randint(1, x)
            brothers = random.randint(1, x)
            typewriterSNL("'My father, the dragon king, has ")
            print(daughters),
            typewriterSNL(
                " princess daughters, waiting for his throne. Each of them has "
            )
            print(brothers)
            typewriterSNL(" older dragon brothers.'")

            time.sleep(1)
            print("\n")
            answer = int(
                input(
                    f"'How many descendants will have a chance at the kings pedestal?'\n Answer (Type 'x' for trial by combat!):"
                )
            )
            if answer != brothers:
                typewriterS(". . . .")
                time.sleep(2)
                typewriterS(
                    "Wrong you fool! - the Dragon exclaims, burning you to a fine crisp and ending your journey in the bowels of the beast."
                )
                save_progress({"level": 3, "points": current_points})
                exit()

            elif answer == "x" or answer == "X":
                success, points = Combat(x, 2, current_points)
                if success:
                    current_points += points
                    typewriterF(
                        "'Impossible! You got away this time scum!' - the dragon exclaims, what sheer luck, you manage to escape and flee Mount Blaviken..."
                    )
                    playerinp = int(
                        input("Enter 1 to continue or 2 to exit the game: ")
                    )
                    if playerinp == 1:
                        time.sleep(2)
                        os.system("cls")
                        save_progress({"level": 4, "points": current_points})
                        Level4(x)
                    elif playerinp == 2:
                        save_progress({"level": 4, "points": current_points})
                        exit()
                else:
                    typewriterS(
                        "High risk, high reward. Unfortunately no reward for you, traveller. Your lack of wit gets you burned by the dragon."
                    )
                    save_progress({"level": 3, "points": current_points})

            else:
                typewriterS(". . . .")
                time.sleep(2)
                typewriterS(
                    "You seem more intelligent than you look. I will let you through this time, struggler.\n"
                )
                current_points += 20
                time.sleep(2)
                typewriterS(
                    "Success! That was a close one, best of luck warrior, you are getting closer and closer to your goal."
                )
                playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
                if playerinp == 1:
                    time.sleep(2)
                    os.system("cls")
                    save_progress({"level": 4, "points": current_points})
                    Level4(x)
                elif playerinp == 2:
                    save_progress({"level": 4, "points": current_points})
                    exit()

        # If chosen path is 2

        elif path == 2:
            os.system("cls")
            time.sleep(1)
            typewriterS(
                "I see your heart is cold and unruly to the dangers ahead of Kingdom of Kaldur, brave one."
            )

            typewriterS(
                "You traverse through their town, filled with towering ice beings, but seemingly not hostile towards you."
            )
            typewriterS("Perhaps you are just a lost insect in their world.")

            typewriterS(
                "You find the exit gate. Thank God, you must think. Managed to escape without any conflict."
            )

            typewriterS(
                "Unfortunately two frost giants, each 15 meters tall, are seen guarding the thick steel gate leading out of the town."
            )
            typewriterS(
                "One says to the other: 'It seems that we have a tresspassing guest within our tribe. Let's have fun with this one'.\n"
            )
            typewriterS(
                "'Foolish soul, I have heard of your mission to uncover the treasure of our lands. If you answer our riddle, I will let you through.'"
            )
            typewriterS("'If not, ")

            typewriterS(
                "'Us ice giant have a sweet spot in our stomachs for human meat. So riddle me this tiny man:' "
            )
            daughters = random.randint(1, x)
            brothers = random.randint(1, x)
            typewriterSNL("'My father, Lord Bjorn, ice heart of Kaldur, has ")
            print(daughters)
            typewriterSNL(
                " princess daughters, waiting for his throne. Each of them has "
            )
            print(brothers)
            typewriterS(" older frost giant brothers.")

            time.sleep(0.5)
            answer = int(
                input(
                    "How many descendants will have a chance at the kings pedestal? \n Answer (Type 'x' for trial by combat!):"
                )
            )
            if answer != brothers:
                typewriterS(". . . .")
                time.sleep(2)
                typewriterS(
                    "Wrong you fool! - the giant exclaims, trapping and freezing you to death. He shares your remains with his comrades for a fine lunch."
                )
                save_progress({"level": 3, "points": current_points})
                exit()

            elif answer == "x" or answer == "X":
                success, points = Combat(x, 2, current_points)
                if success:
                    current_points += points
                    typewriterF(
                        "'Impossible! You got away this time puny human!' - the giant exclaims, what sheer luck, you manage to escape and flee Kaldur..."
                    )
                    playerinp = int(
                        input("Enter 1 to continue or 2 to exit the game: ")
                    )
                    if playerinp == 1:
                        time.sleep(2)
                        os.system("cls")
                        save_progress({"level": 4, "points": current_points})
                        Level4(x)
                    elif playerinp == 2:
                        save_progress({"level": 4, "points": current_points})
                        exit()
                else:
                    typewriterS(
                        "High risk, high reward. Unfortunately no reward for you, traveller. Your lack of wit gets you stomped to death by the giant."
                    )
                    save_progress({"level": 3, "points": current_points})

            else:
                typewriterS(". . . .")
                time.sleep(2)
                typewriterS(
                    "Hmm, You seem more intelligent than you look. I will let you through this time, struggler.\n"
                )
                current_points += 20
                time.sleep(2)
                typewriterS(
                    "Success! That was a close one, best of luck warrior, you are getting closer and closer to your goal."
                )
                playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
                if playerinp == 1:
                    time.sleep(2)
                    os.system("cls")
                    save_progress({"level": 4, "points": current_points})
                    Level4(x)
                elif playerinp == 2:
                    save_progress({"level": 4, "points": current_points})
                    exit()
