import time
import os
import random
import subprocess
import sys


def Level4(x, current_points):
    from MiscFunc import save_progress, typewriterS, load_progress
    from Mechanics import Combat

    typewriterS(
        "The path was rough, unrelenting and difficult for our hero, as he approaches ever so closely to his goal."
    )
    typewriterS(
        "Truly he showed his might, his wits and his courage. Is there a challenge worthy of him?\n"
    )
    typewriterS(
        "The map leads you at the top of Mount Chimerus, you find an old, seemingly abandoned castle ruin."
    )
    typewriterS("You enter inside, and see that couldn't be more far from the truth.\n")
    typewriterS(
        "Inside a cunning, mysterious oracle stands before you and the sacred treasure. He speaks:"
    )
    typewriterS(
        "'I knew you would come one day. Your goals are known to me from the start. Answer my questions and the treasure and its secrets are yours, brave one.'\n"
    )
    answer1 = int(
        input(
            typewriterS(
                """'I'm oceans' count, a simple quest,
Guess me right, be your best.
What am I, put to the test?': """
            )
        )
    )
    if answer1 == 7:
        typewriterS("\n'That shows me nothing. But hear this:'")
        typewriterS(
            """'In space so vast, a cosmic mystery
Planets dancing in celestial symmetry. 
Count them up, with accuracy, 
How many planets in our solar journey?'"""
        )
        answer2 = int(input(":"))
        if answer2 == 8:
            typewriterS(
                "\n'Good, good. It seems the apple doesn't fall far from the tree. There is still more to show."
            )
            typewriterS(
                """'In magical realms and potions brew,
Tell me, dear one, the days in a year that grew.
Not a riddle, but a truth so clear,
How many days make up our earthly sphere?'"""
            )
            answer3 = int(input(":"))
            if answer3 == 365:
                typewriterS(
                    "\n'At last, you've come this far. I will not interfere with the process of unlocking the treasure.'"
                )
                typewriterS(
                    "'The key you must have deducted. The sum of the Earth's oceans, the planets of the skies, and earthly days. Have at it, young one.'"
                )
                answer4 = int(input(":"))
                if answer4 == 365 + 8 + 7:
                    script_directory = os.path.dirname(sys.argv[0])
                    script_path = os.path.join(script_directory, "Firework.py")
                    subprocess.Popen([sys.executable, script_path]).wait()
                    # time.sleep(3)
                    current_points *= 100
                    os.system("cls")
                    save_progress({"level": 4, "points": current_points})
                    player_data = load_progress()
                    total_score = player_data.get("points", 0)
                    typewriterS(
                        "Congratulations! You have successfully beaten the game!"
                    )
                    typewriterS(f"Your final score is: {total_score}")
                    typewriterS("Press any button to exit...")
                    input()
                    exit()

                else:
                    typewriterS(
                        "'It seems that you lack the mental power to handle the sacred treasure. I banish you from this realm!'\n So close, yet so far away. You failed the wizards request and have been banished."
                    )
                    save_progress({"level": 4, "points": current_points})

            else:
                typewriterS(
                    "'It seems that you lack the mental power to handle the sacred treasure. I banish you from this realm!'\n So close, yet so far away. You failed the wizards request and have been banished."
                )
                save_progress({"level": 4, "points": current_points})

        else:
            typewriterS(
                "'It seems that you lack the mental power to handle the sacred treasure. I banish you from this realm!'\n So close, yet so far away. You failed the wizards request and have been banished."
            )
            save_progress({"level": 4, "points": current_points})

    else:
        typewriterS(
            "'It seems that you lack the mental power to handle the sacred treasure. I banish you from this realm!'\n So close, yet so far away. You failed the wizards request and have been banished."
        )
        save_progress({"level": 4, "points": current_points})
