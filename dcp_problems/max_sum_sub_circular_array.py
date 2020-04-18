"""
Author: Nishant

Problem : Maximum sum subarray when array can be moved in circular.

Date : 18/04/2020
"""

import sys


class MaxSumSubCircularArray:
    def __init__(self, num_list):
        self.__max_sum = -1 * sys.maxsize
        self.__min_sum = sys.maxsize
        self.__list = num_list

    def min_sum_subarray(self):
        min_so_far = sys.maxsize
        for i in range(len(self.__list)):
            min_so_far = min(min_so_far + self.__list[i], self.__list[i])
            self.__min_sum = min(self.__min_sum, min_so_far)

    def max_sum_subarray(self):
        max_so_far = -1 * sys.maxsize
        for i in range(len(self.__list)):
            max_so_far = max(max_so_far + self.__list[i], self.__list[i])
            self.__max_sum = max(max_so_far, self.__max_sum)

    def max_sum_subarray_circular(self):
        sums = 0
        for i in range(len(self.__list)):
            sums += self.__list[i]

        return max(self.__max_sum, (sums - self.__min_sum))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        nums_list = [int(x) for x in input().split()]
        max_circular_sum = MaxSumSubCircularArray(nums_list)
        max_circular_sum.max_sum_subarray()
        max_circular_sum.min_sum_subarray()
        print(max_circular_sum.max_sum_subarray_circular())
