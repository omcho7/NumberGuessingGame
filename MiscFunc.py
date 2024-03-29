import json
import time


# function for saving progress
def save_progress(player_data):
    with open("player_data.json", "w") as file:
        json.dump(player_data, file)


# function for loading progress
def load_progress():
    try:
        with open("player_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


# typewriter effect functions, all the same but with different speeds
def typewriterS(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the whole text
    return ""


def typewriterSNL(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    return ""


def typewriterF(text, delay=0.015):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
    return ""


# function to start and load saved levels and points
def StartGame(x, new_game=False):
    from LevelOne import Level1
    from LevelTwo import Level2
    from LevelThree import Level3
    from LevelFour import Level4

    if new_game or not load_progress():
        current_points = 0
        save_progress({"level": 1, "points": current_points})
        Level1(x, current_points)
    else:
        player_data = load_progress()
        current_level = player_data["level"]
        current_points = player_data["points"]
        print("Currently on level " + str(current_level))
        print("~ ~ ~ ~~~~~ ~ ~ ~ ~~~~~ ~ ~ ~ ~~~~~ ~ ~ ~ ~~~~~ \n")

        if current_level == 1:
            Level1(x, current_points)
        elif current_level == 2:
            Level2(x, current_points)
        elif current_level == 3:
            Level3(x, current_points)
        elif current_level == 4:
            Level4(x, current_points)
