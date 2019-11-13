"""
Author: Nishant

Problem : Factorial of a number.

Date : 13/11/2019
"""


class FactorialOfNumber:
    def __init__(self):
        self.__factorial = 1

    def calculate_factorial(self, num):
        while num > 0:
            self.__factorial *= num
            num -= 1
        return self.__factorial


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        number = int(input())
        print(FactorialOfNumber().calculate_factorial(number))
