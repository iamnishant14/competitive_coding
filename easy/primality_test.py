"""
Author: Nishant

Problem : Check if number is prime or not.

Date : 13/11/2019
"""
import math


class PrimalityTest:
    def __init__(self):
        self.__is_prime = False

    @staticmethod
    def is_prime(number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        num = int(input())
        flag = PrimalityTest.is_prime(num)
        if flag:
            print('Yes')
        else:
            print('No')
        t -= 1
