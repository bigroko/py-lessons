# -*- coding: UTF-8 -*-

import random


def decorator_function(to_decorate):
    def wrapper_function():
        i = to_decorate() * 3
        print("wrapper_function(), i = {}".format(i))
        return i
    return wrapper_function


@decorator_function
def inner_function():
    i = random.randint(1, 100)
    print("inner_function(), i = {}".format(i))
    return i

inner_function()
