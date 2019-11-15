"""
Author: Nishant

Problem : Addition and multiplication of number under Modulo M(10^9+7).

Date : 15/11/2019
"""


class AddAndMultiplyUnderModulo:
    M = 1000000007

    def __init__(self):
        self.__addition = 0
        self.__multiplication = 1

    def get_addition(self, numbers):
        for i in range(len(numbers)):
            self.__addition = self.__addition % self.M
            numbers[i] = numbers[i] % self.M
            self.__addition += numbers[i]
            self.__addition = self.__addition % self.M
        return self.__addition

    def get_multiplication(self, numbers):
        for i in range(len(numbers)):
            self.__multiplication = self.__multiplication % self.M
            numbers[i] = numbers[i] % self.M
            self.__multiplication *= numbers[i]
            self.__multiplication = self.__multiplication % self.M
        return self.__multiplication


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        add_multiply = AddAndMultiplyUnderModulo()
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        print('Addition is: {0}'.format(add_multiply.get_addition(a)))
        print('Multiplication is: {0}'.format(add_multiply.get_multiplication(b)))
