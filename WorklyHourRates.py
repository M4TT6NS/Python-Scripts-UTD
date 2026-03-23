import random
import time

while True:
    x_coordinate = random.randint(-10, 10)
    y_coordinate = random.randint(-10, 10)
    x1 = 0 - x_coordinate
    y1 = 0 - y_coordinate
    slope = random.randint(-10, 10)
    print("Using the coordinate ({}, {})".format(x_coordinate, y_coordinate) + ", and the slope " + str(slope) + ", create a slope-intercept form liner equation.")
    input_answer = input("example: y = 2x + 3\n")
    y_intercept = x1 * slope - y1
    if y_intercept < 0:
        real_answer = f"y = {slope}x - {abs(y_intercept)}"
    else:
        real_answer = f"y = {slope}x + {y_intercept}"
    def check_answer(input_answer, real_answer):
        if input_answer == real_answer:
            print("That is the correct answer!")
        else:
            print("That is the wrong answer. The correct answer is " + str(real_answer))
    check_answer(input_answer, real_answer)
    time.sleep(1)
    print("Now for the next question...")
    time.sleep(1)
