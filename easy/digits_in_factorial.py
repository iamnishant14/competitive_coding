"""
Author: Nishant

Problem : Count of digits in factorial of a number

Date : 13/11/2019
"""
import math


class DigitsInFactorial:
    def __init__(self):
        self.__count_digits = 0

    def count_digits(self, num):
        if num < 0:
            return 0
        if num <= 1:
            return 1
        for i in range(2, num + 1):
            self.__count_digits += math.log10(i)

        return math.floor(self.__count_digits) + 1


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        number = int(input())
        print(DigitsInFactorial().count_digits(number))
        t -= 1
