"""
Author: Nishant

Problem : Max Contigous Subarray for maximum possible sum.

Date : 27/04/2019
"""

import sys


class KadaneProblem:

    def max_sum_contiguous_subarray(self, number_list):
        """
        Start from start and keep a counter of the current sum,
        current sum should be greater then current element and check if current sum is the max sum available.
        :param number_list: list of numbers to calculate max sum of continuous sublist
        :return:
        """
        length = len(number_list)
        max_sum = -sys.maxsize - 1
        max_sum_so_far = -sys.maxsize - 1
        for i in range(0, length):
            max_sum_so_far += number_list[i]
            max_sum_so_far = max(max_sum_so_far, number_list[i])
            max_sum = max(max_sum_so_far, max_sum)

        return max_sum


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        kadane_problem = KadaneProblem()
        length = int(input())
        number_list = list(map(int, input().split()))
        print(kadane_problem.max_sum_contiguous_subarray(number_list))
