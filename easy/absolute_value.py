"""
Author: Nishant

Problem : Absolute value of the integer.

Date : 08/11/2019
"""
import sys


class AbsoluteValue:
    def __init__(self):
        self.__abs_value = sys.maxsize

    def calc_absolute_value(self, number):
        if number < 0:
            self.__abs_value = -1 * number
        else:
            self.__abs_value = number
        return self.__abs_value


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        number = int(input())
        abs_val = AbsoluteValue()
        print(abs_val.calc_absolute_value(number))
        t -= 1
