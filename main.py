import os
import time
import random
import json


def save_progress(player_data):
    with open("player_data.json", "w") as file:
        json.dump(player_data, file)


def load_progress():
    try:
        with open("player_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def Difficulty():
    print("-----------Choose Difficulty-----------")
    print("\n")
    print("           1. Easy (1 - 10)            ")
    print("           2. Medium (1 - 20)          ")
    print("           3. Hard (1 - 30)            ")
    print("\n")

    diffchoice = int(input("Choose option (1, 2, 3): "))

    if diffchoice < 1 or diffchoice > 3:
        while diffchoice < 1 or diffchoice > 3:
            diffchoice = int(input("Incorrect value, choose option (1, 2, 3): "))
    else:
        if diffchoice == 1:
            x = 10
            print("\nChosen difficulty: 1\n")
        elif diffchoice == 2:
            x = 20
            print("\nChosen difficulty: 2\n")
        elif diffchoice == 3:
            x = 30
            print("\nChosen difficulty: 3\n")
        time.sleep(1.5)
        os.system("cls")
        return x


def StartGame(x):
    player_data = load_progress()

    if player_data is not None and "level" in player_data:
        current_level = player_data["level"]
    else:
        current_level = 1

    print("Current level: " + str(current_level) + "\n")

    if current_level == 1:
        Level1(x)
    elif current_level == 2:
        Level2(x)


def Level1(x):
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
            Level2(x)
        elif playerinp == 2:
            save_progress({"level": 2})
            exit()

    else:
        print(
            "No, you have missed! Fortunately the monster tripped, you get another chance!"
        )
        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(monster1 - 1) <= damage <= monster1 + 1:
            print("The beast is defeated! You continue your journey.")
            playerinp = int(input("Enter 1 to continue or 2 to exit the game: "))
            if playerinp == 1:
                time.sleep(2)
                os.system("cls")
                save_progress({"level": 2})
                Level2(x)
            elif playerinp == 2:
                save_progress({"level": 2})
                exit()
        else:
            print("No luck! Attack was too weak and you have been defeated.")


def Level2(x):
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
        tree = random.randint(1, x)
        print(tree)
        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(tree - 1) <= damage <= tree + 1:
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
                Level3(x)
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
        tree = random.randint(1, x)
        print(tree)
        damage = int(input("Enter a number 1-" + str(x) + ": "))
        if abs(tree - 1) <= damage <= tree + 1:
            print(
                "Success! But that won't take it down. Attack again, don't let the beast rest!"
            )
            tree = random.randint(1, x)
            print(tree)
            damage = int(input("Enter a number 1-" + str(x) + ": "))
            if abs(tree - 1) <= damage <= tree + 1:
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
                    Level3(x)
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


def MainMenu():
    print("---------------Main Menu---------------")
    print("\n")
    print("             1. Start Game             ")
    print("                2. Exit                ")
    print("\n")
    mmchoice = int(input("Choose option (1, 2): "))

    while mmchoice != 1 and mmchoice != 2:
        mmchoice = int(input("Incorrect value, choose option (1, 2): "))

    if mmchoice == 1:
        os.system("cls")
        x = Difficulty()
        StartGame(x)
    elif mmchoice == 2:
        exit()


MainMenu()
