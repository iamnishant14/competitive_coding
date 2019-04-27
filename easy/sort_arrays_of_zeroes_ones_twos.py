"""
Author: Nishant

Problem : Sort array of 0s,1s and 2s.

Date : 01/05/2019
"""


class SortArrayOfZeroesOnesTwos:
    """
    Keep count of 0s , 1s and 2s and print them sequentially.
    """

    def __init__(self):
        self.__count_one = 0
        self.__count_two = 0
        self.__count_zero = 0

    def sort_array(self):
        number_list = list()
        self.__append_zeroes(number_list)
        self.__append_ones(number_list)
        self.__append_twos(number_list)
        return number_list

    def __append_zeroes(self, number_list):
        for i in range(0, self.__count_zero):
            number_list.append(0)

    def __append_ones(self, number_list):
        for i in range(0, self.__count_one):
            number_list.append(1)

    def __append_twos(self, number_list):
        for i in range(0, self.__count_two):
            number_list.append(2)

    def count_zeroes_ones_twos(self, number_list):
        for i in range(0, len(number_list)):
            if number_list[i] == 0:
                self.__count_zero += 1
            elif number_list[i] == 1:
                self.__count_one += 1
            else:
                self.__count_two += 1


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        sort_array = SortArrayOfZeroesOnesTwos()
        length = int(input())
        number_list = list(map(int, input().split()))
        sort_array.count_zeroes_ones_twos(number_list)
        number_list = sort_array.sort_array()
        print(*number_list)
