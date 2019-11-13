"""
Author: Nishant

Problem : Mean and median of list of numbers.

Date : 13/11/2019
"""
import math
import sys


class MeanAndMedian:
    def __init__(self):
        self.__mean = sys.maxsize
        self.__median = sys.maxsize

    @staticmethod
    def __calculate_mean(numbers):
        sums = 0
        for i in range(len(numbers)):
            sums += numbers[i]
        return int(sums / len(numbers))

    @staticmethod
    def __partition(low, high, numbers):
        s = low - 1
        pivot = numbers[high]
        for i in range(low, high + 1):
            if numbers[i] < pivot:
                s += 1
                numbers[i], numbers[s] = numbers[i], numbers[s]
        s += 1
        numbers[s], numbers[high] = numbers[high], numbers[s]
        return s

    def __quick_sort(self, low, high, numbers):
        if low < high:
            i = self.__partition(low, high, numbers)
            self.__quick_sort(low, i - 1, numbers)
            self.__quick_sort(i + 1, high, numbers)

    def __calculate_median(self, numbers):
        self.__quick_sort(0, len(numbers) - 1, numbers)
        size = len(numbers)
        if size % 2 == 0:
            return int((numbers[math.floor(size / 2)] + numbers[math.floor(size / 2) + 1]) / 2)
        else:
            return int(numbers[math.floor(size / 2)])

    def calculate_mean_and_median(self, numbers):
        self.__mean = self.__calculate_mean(numbers)
        self.__median = self.__calculate_median(numbers)

    def get_mean(self):
        return self.__mean

    def get_median(self):
        return self.__median


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = [int(x) for x in input().split()]
        mean_median = MeanAndMedian()
        mean_median.calculate_mean_and_median(a)
        print(mean_median.get_mean(), mean_median.get_median())
        t -= 1
