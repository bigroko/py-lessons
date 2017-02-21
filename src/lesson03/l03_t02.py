# -*- coding: UTF-8 -*-

import math

TYPE = "type"
SIZE = "size"


def get_area(**kwargs):
    """
    Calculates area of rectangle, triangle or circle
    :param kwargs[TYPE]: Type of shape (1, 2 or 3)
    :param kwargs[SIZE]: Size of shape ([a, b], [a, b, c] or R)
    :return: Area of the shape (float)
    """
    if kwargs[TYPE] == 1:
        area = kwargs[SIZE][0] * kwargs[SIZE][1]
    elif kwargs[TYPE] == 2:  # Heron's formula
        s = (kwargs[SIZE][0] + kwargs[SIZE][1] + kwargs[SIZE][2]) / 2
        area = math.sqrt(s * (s - kwargs[SIZE][0]) *
                             (s - kwargs[SIZE][1]) *
                             (s - kwargs[SIZE][2]))
    else:
        area = math.pi * (kwargs[SIZE] ** 2)
    return area

# Get type of shape
while True:
    try:
        response = int(input(
            "Select a shape (1 - rectangle / 2 - triangle / 3 - circle): "))
    except ValueError:
        print("Not a number, try again.")
        continue
    else:
        if response not in (1, 2, 3):
            print("Wrong number, try again.")
            continue
        else:
            break

params = {TYPE: response}
# Fill params
if response == 1:
    while True:
        try:
            response = input("Enter rectangle wide and high (a, b): ")
            values = [float(x) for x in response.split(",")]
        except ValueError:
            print("Not the numbers, try again.")
            continue
        else:
            if len(values) != 2:
                print("Two numbers only, try again.")
                continue
            elif any([v <= 0 for v in values]):
                print("Only positive numbers, try again.")
                continue
            else:
                break
elif response == 2:
    while True:
        try:
            response = input("Enter triangle sides (a, b, c): ")
            values = [float(x) for x in response.split(",")]
        except ValueError:
            print("Not the numbers, try again.")
            continue
        else:
            if len(values) != 3:
                print("Three numbers only, try again.")
                continue
            elif any([v <= 0 for v in values]):
                print("Only positive numbers, try again.")
                continue
            elif any([v >= (sum(values) / 2) for v in values]):
                print("One side should be less than two others, try again.")
                continue
            else:
                break
else:
    while True:
        try:
            response = input("Enter circle radius (R): ")
            values = float(response)
        except ValueError:
            print("Not the number, try again.")
            continue
        else:
            if values <= 0:
                print("Only positive number, try again.")
                continue
            else:
                break

params[SIZE] = values
print("Area of this shape = {}".format(get_area(**params)))
