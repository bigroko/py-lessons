# -*- coding: UTF-8 -*-


def main():
    # Calculates fib (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...) by number (loop)
    print(fib1(10))
    # Calculates fib (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...) by number (recurs.)
    print(fib2(10))


def fib1(num):
    i = 1
    (a, b) = (0, 1)
    while i < num:
        (a, b) = (b, b + a)
        i += 1
    return a


def fib2(num):
    def fib_r(n):
        if n <= 1:
            return n
        else:
            return fib_r(n-2) + fib_r(n-1)
    return fib_r(num - 1)

if __name__ == "__main__":
    main()
