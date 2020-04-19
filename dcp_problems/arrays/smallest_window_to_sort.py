"""
Author: Nishant

Problem : Find smallest window to sort in ana array to make array increasingly sorted.

Date : 18/04/2020
"""
import sys


class SmallestWindowToSort:
    def __init__(self, list):
        self.__right = len(list) + 1
        self.__left = -1
        self.__list = list

    def calculate_window(self):
        maxm = -1 * sys.maxsize
        for i in range(len(self.__list)):
            maxm = max(maxm, self.__list[i])
            if self.__list[i] < maxm:
                self.__right = i

        minm = sys.maxsize
        for i in range(len(self.__list) - 1, -1, -1):
            minm = min(minm, self.__list[i])
            if self.__list[i] > minm:
                self.__left = i

    def get_window(self):
        return self.__left, self.__right


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        num_list = [int(x) for x in input().split()]
        smallest_window = SmallestWindowToSort(num_list)
        smallest_window.calculate_window()
        print(smallest_window.get_window())
