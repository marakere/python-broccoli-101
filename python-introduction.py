#!/usr/bin/env python3
import math
from random import *

"""
    https://www.programiz.com/python-programming/examples
"""


def area_of_triangle():
    """
    1. Using base and height
    2. Using all 3 sides - Option1
    3. using all 3 sides - Option2

    :return: value
    """
    print("Using base(4) and height(3) of a triangle - " + str(float(0.5) * (3 * 4)))
    print("Using all 3 sides of a triangle  - 0.5(3+4+5) " + str(float(0.5) * (3 + 4 + 5)))
    print("Using all 3 sides of a triangle - sqrt(6(6-2)(6-3)(6-4)) " + str(math.sqrt(6 * (6 - 2) * (6 - 3) * (6 - 4))))


def swap_variable():
    x = 10
    y = 11
    print("Before swapping the variables " + str(x), str(y))
    temp = x
    x = y
    y = temp
    print("After swapping the variables " + str(x), str(y))


def km_to_mile(x):
    print("when " + str(x) + "km is converted to mile, it will be " + str(x / 1.6))


print("Hello World it is!")
print("Sum of 2 and 3 is " + str(float(2) + float(3)))
print("Square root of 100 is " + str(math.sqrt(100)))
area_of_triangle()
swap_variable()
print("Generate a random number between 1 to 100" + str(randint(1, 100)))
km_to_mile(100)
print("28 degree = " + str((float(28 * 1.8) + 32)) + "Fahrenheit")
