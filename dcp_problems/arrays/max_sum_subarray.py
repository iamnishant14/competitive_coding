"""
Author: Nishant

Problem : Maximum sum subarray for a given array.

Date : 18/04/2020
"""
import sys


class MaxSumSubarray:
    def __init__(self, num_list):
        self.__max_sum = -1 * sys.maxsize
        self.__list = num_list

    def calculate_max_sum_subarray(self):
        max_so_far = -1 * sys.maxsize
        for i in range(len(self.__list)):
            max_so_far = max(max_so_far + self.__list[i], self.__list[i])
            self.__max_sum = max(max_so_far, self.__max_sum)

    def get_max_sum(self):
        return self.__max_sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        num_list = [int(x) for x in input().split()]
        max_sum_subarray = MaxSumSubarray(num_list)
        max_sum_subarray.calculate_max_sum_subarray()
        print(max_sum_subarray.get_max_sum())
