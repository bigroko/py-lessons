# -*- coding: UTF-8 -*-


def is_prime(n):
    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is prime
    if n == 2:
        return True

    # Even numbers are not primes
    if n % 2 == 0:
        return False

    # Main routine
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def prime_generator():
    n = 1
    while True:
        if is_prime(n):
            yield n
        n += 1

if __name__ == '__main__':
    g = prime_generator()
    for i in range(20):
        print(next(g))
    g.close()
