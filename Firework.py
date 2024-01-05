import random
import turtle
import time
from collections import deque

t = turtle.Turtle()
t.speed(0)


def pen(color):
    t.color(color)


pen("red")


def move():
    t.penup()
    x = random.randint(-165, 165)
    y = random.randint(-165, 165)
    t.goto(x, y)
    t.pendown()


def sky(color):
    wn = turtle.Screen()
    wn.bgcolor(color)


sky("#10102a")


def firework(size, used_positions):
    t.speed(0.005)  # Random speed between 1 and 10

    # Generate a random position, ensuring it's not too close to existing fireworks
    while True:
        x = random.randint(-165, 165)
        y = random.randint(-165, 165)
        if all(abs(x - px) > 100 or abs(y - py) > 100 for px, py in used_positions):
            break

    used_positions.append((x, y))
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Generate a random color for each firework
    color_r = hex(random.randint(0x10, 0xEF))[2:]
    color_g = hex(random.randint(0x10, 0xEF))[2:]
    color_b = hex(random.randint(0x10, 0xEF))[2:]
    pen("#" + color_r + color_g + color_b)

    for _ in range(20):
        t.forward(size)
        t.right(180 - (360 / 20))

    # Limit the size of used_positions
    max_positions = 100
    if len(used_positions) > max_positions:
        used_positions.popleft()


# Begin Config #
F_SIZE_MIN = 50
F_SIZE_MAX = 500
FIREWORK_PER_CLEAR = 2
WINDOW_DURATION = 5  # seconds
# End Config #

start_time = time.time()
used_positions = deque()

while time.time() - start_time < WINDOW_DURATION:
    for _ in range(FIREWORK_PER_CLEAR):
        firework(random.randint(F_SIZE_MIN, F_SIZE_MAX), used_positions)
    t.clear()

turtle.bye()
