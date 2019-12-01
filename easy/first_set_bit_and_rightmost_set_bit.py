"""
Author: Nishant

Problem : First set bet in a number.

Date : 01/12/2019
"""
import math


class FirstSetBit:
    def __init__(self, num):
        self.__number = num

    def find_first_set_bit(self):
        if self.__number <= 0:
            return 0
        x = self.__number & (self.__number - 1)
        return int(math.log(self.__number - x, 2)) + 1


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        x = int(input())
        if x == 1:
            number = int(input())
            print(FirstSetBit(number).find_first_set_bit())
        else:
            number, nums = input().split()
            number = int(number)
            nums = int(nums)
            print(FirstSetBit(number ^ nums).find_first_set_bit())
        t -= 1
