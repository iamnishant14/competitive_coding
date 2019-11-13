"""
Author: Nishant

Problem : Count of numbers less than N having exactly 3 divisors.

Date : 13/11/2019
"""
import math


class ExactlyThreeDivisors:

    def __init__(self):
        self.__count_numbers = 0

    @staticmethod
    def __is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def __is_perfect_square(number):
        n = int(math.sqrt(number))
        if n * n == number:
            return True
        return False

    def count_numbers_with_three_divisors(self, number):
        for i in range(1, number + 1):
            if self.__is_prime(math.sqrt(i)) and self.__is_perfect_square(i):
                self.__count_numbers += 1
        return self.__count_numbers


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        num = int(input())
        print(ExactlyThreeDivisors().count_numbers_with_three_divisors(num))
        t -= 1
