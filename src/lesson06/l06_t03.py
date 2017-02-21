# -*- coding: UTF-8 -*-

import random
from l06_t02 import MyChildException2


def possible_fail(probability):
    try:
        n = round(random.random(), 2)
        text = "Probability: {}, random number: {}".format(probability, n)
        if n <= probability:
            raise MyChildException2("Exception was raised. {}".format(text))
        else:
            print("Not excepted. {}".format(text))
    except MyChildException2 as my_c_ex2:
        print(str(my_c_ex2))

if __name__ == '__main__':
    rnd = random.random()
    possible_fail(round(rnd, 2))
