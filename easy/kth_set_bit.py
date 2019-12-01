"""
Author: Nishant

Problem : Kth bit set in a number or not.

Date : 01/12/2019
"""


class KthBitSet:
    def __init__(self):
        self.__is_set = False

    def check_kth_bit_set(self, k, number):
        if number & (1 << k):
            self.__is_set = True
            return
        self.__is_set = False

    def get_is_set(self):
        return self.__is_set


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        number = int(input())
        k = int(input())
        kth_bit_set = KthBitSet()
        kth_bit_set.check_kth_bit_set(k, number)
        print(kth_bit_set.get_is_set())
        t -= 1
