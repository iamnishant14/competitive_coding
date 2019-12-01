"""
Author: Nishant

Problem : Modular multiplicative inverse of number under modulo m.

Date : 15/11/2019
"""


class ModularMultiplicativeInverse:
    def __init__(self, num, m):
        self.__number = num
        self.__m = m

    def calculate_modular_multiplicative_inverse(self):
        self.__number = self.__number % self.__m
        for i in range(1, self.__m):
            if (self.__number * i) % self.__m == 1:
                return i
        return -1


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        a, m = input().split()
        a = int(a)
        m = int(m)
        mod_inv = ModularMultiplicativeInverse(a, m)
        print(mod_inv.calculate_modular_multiplicative_inverse())
        t -= 1
