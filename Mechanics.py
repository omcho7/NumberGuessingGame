import random


def get_hint(enemy, current_attempt, damage):
    from MiscFunc import typewriterF, typewriterS

    if current_attempt == 2:
        if enemy > damage:
            return typewriterF("Hint: Guess higher!")
        else:
            return typewriterF("Hint: Guess lower!")

    elif current_attempt == 3:
        if enemy % 2 == 0:
            return typewriterF("Hint: the number is even.")
        else:
            return typewriterF("Hint: the number is not even.")

    elif current_attempt == 4:
        return typewriterF(
            f"Hint: the wanted number is one of these: {enemy-1}, {enemy}, {enemy+1}"
        )


def Combat(x, atm, current_points):
    from MiscFunc import typewriterS, typewriterF

    current_attempt = 1
    max_points = 50

    enemy = random.randint(1, x)

    while current_attempt <= atm:
        damage = int(input(f"Guess the number (1 - {x}): "))
        if damage == enemy:
            points = max_points - (current_attempt - 1) * 15
            typewriterS(
                f"Successful hit! You guessed in {current_attempt} attempt(s) and earned {points} points."
            )
            return True, points
        else:
            current_attempt += 1
            typewriterF("Missed! Try again.")
            if current_attempt >= 2:
                print(get_hint(enemy, current_attempt, damage))

    else:
        typewriterS(f"No luck! Ran out of attempts, the correct number was {enemy}.")
        return False, 0
