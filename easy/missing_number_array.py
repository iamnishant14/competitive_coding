"""
Author: Nishant

Problem : Missing number from array containg number from 0-N

Date : 27/04/2019
"""


class MissingNumber:

    def find_missing_number(self, number_list, length):
        length_total = length
        sum = (length_total * (length_total + 1)) / 2
        list_sum = 0
        length_list = len(number_list)
        for i in range(0, length_list):
            list_sum += number_list[i]

        return int(sum - list_sum)


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        missing_number = MissingNumber()
        length = int(input())
        number_list = list(map(int, input().split()))
        print(missing_number.find_missing_number(number_list, length))
