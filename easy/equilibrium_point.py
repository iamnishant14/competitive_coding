"""
Author: Nishant

Problem : Equilibrium point in array with sum of left subarray = sum of right subarray.

Date : 08/05/2019
"""


class EquilibriumPoint:
    """
    Maintain two lists to store sum of left and right subarray.
    """

    def __init__(self, size):
        self.__left_sum = [0 for i in range(size)]
        self.__right_sum = [0 for i in range(size)]

    def find_equilibrium_point(self, number_list):
        size = len(number_list)

        """
        Update the left subarray of sum of elements left to particular element.
        """
        for i in range(1, size):
            self.__left_sum[i] = self.__left_sum[i - 1] + number_list[i - 1]

        """
        Update the right subarray of sum of elements right to particular element.
        """
        for i in range(size - 2, -1, -1):
            self.__right_sum[i] = self.__right_sum[i + 1] + number_list[i + 1]

        eq_index = -1

        for i in range(size):
            if self.__right_sum[i] == self.__left_sum[i]:
                eq_index = i

        return eq_index


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        length = int(input())
        equilibrium_point = EquilibriumPoint(length)
        number_list = list(map(int, input().split()))
        eq_index = equilibrium_point.find_equilibrium_point(number_list)
        if eq_index is not -1:
            print(eq_index + 1)
        else:
            print(eq_index)
