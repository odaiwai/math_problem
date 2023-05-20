#!/usr/bin/env python3
"""
Script to solve a math problem
dave o'brien 2016/03/24
problem:
  A B
- C D
-----
  E F
+ G H
-----
P P P

Where ABCDEFGH, P are all [1-9], and unique
e.g. AB = 21, if A=2, B=1
"""
from itertools import permutations


def numbers_ok(numbers: list) -> bool:
    """
    step through a list and return True if all numbers are unique,
    False otherwise
    """
    unique = True
    count = {}
    for num in numbers:
        count[num] = 1 + count.setdefault(num, 0)
        if count[num] > 1:
            unique = False  # if we've seen any number more than one, return 0
    return unique


def main():
    """
    Main part
    """
    for a, b, c, d, g, h in permutations(range(1, 10), 6):
        ef = (10*a+b) - (10*c+d)
        # make a character string of the answer:
        #  three places integer with sign
        ef_char = '{:+03d}'.format(ef)
        e = int(ef_char[1])
        f = int(ef_char[2])
        ppp = ef + (10 * g + h)
        ppp_char = '{:+04d}'.format(ppp)
        if numbers_ok([a, b, c, d, e, f, g, h]):
            if (ppp_char[1] == ppp_char[2] == ppp_char[3]):
                print('solution: ', a, b, c, d, e, f, g, h, ppp)


if __name__ == '__main__':
    main()
