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
def typewriterS(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the whole text


def typewriterSNL(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)


def typewriterF(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# function to start and load game based on the saved level
def StartGame(x, new_game=False):
    from LevelOne import Level1
    from LevelTwo import Level2
    from LevelThree import Level3

    if new_game or not load_progress():
        save_progress({"level": 1})
        Level1(x)
    else:
        player_data = load_progress()
        current_level = player_data["level"]
        print("Currently on level " + str(current_level))
        print("~ ~ ~ ~~~~~ ~ ~ ~ ~~~~~ ~ ~ ~ ~~~~~ ~ ~ ~ ~~~~~ \n")

        if current_level == 1:
            Level1(x)
        elif current_level == 2:
            Level2(x)
        elif current_level == 3:
            Level3(x)
