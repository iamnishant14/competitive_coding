"""
Author: Nishant

Problem : Reverse words in strings seperated by '.' .

Date : 03/05/2019
"""


class MaxSumIncreasingSubsequence:
    def __init__(self):
        self.__sum_list = []

    def calculate_max_sum_increasing_subsequence(self, number_list, length):
        self.__sum_list = [0 for x in range(length)]
        for i in range(length):
            self.__sum_list[i] = number_list[i]

        for i in range(1, length):
            for j in range(i):
                if number_list[i] > number_list[j] and self.__sum_list[i] < self.__sum_list[j] + number_list[i]:
                    self.__sum_list[i] = self.__sum_list[j] + number_list[i]

        max_sum = max(self.__sum_list)

        return max_sum


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        max_sum_increasing_subsequence = MaxSumIncreasingSubsequence()
        length = input()
        length = int(length)
        number_list = list(map(int, input().split()))
        max_sum = max_sum_increasing_subsequence.calculate_max_sum_increasing_subsequence(number_list, length)
        print(max_sum)
