# -*- coding: UTF-8 -*-


class MyParentException(Exception):
    pass


class MyChildException1(MyParentException):
    pass


class MyChildException2(MyChildException1):
    pass


def test():
    raise MyParentException("MyParentException", 1, 2)


def test1():
    raise MyChildException1("MyChildException1", 3, 4)


def test2():
    raise MyChildException2("MyChildException2", 5, 6)


def run_exception():
    try:
        test()
    except MyParentException as my_p_ex:
        print(my_p_ex.args)
    try:
        test1()
    except MyChildException1 as my_c_ex1:
        print(my_c_ex1.args)
    try:
        test2()
    except MyChildException2 as my_c_ex2:
        print(my_c_ex2.args)


def run_exception_polymorphism():
    try:
        test2()
    except MyParentException as my_p_ex:
        print("\nPolymorphism (MyChildException2 was raised "
              "but caught by MyParentException):")
        print(my_p_ex.args)

if __name__ == '__main__':
    run_exception()
    run_exception_polymorphism()
