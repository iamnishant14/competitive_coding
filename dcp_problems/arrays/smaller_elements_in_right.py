"""
Author: Nishant

Problem : Number of smallest elements in right of current element.

Date : 19/04/2020
"""


class SmallerElementsInRight:
    def __init__(self, num_list):
        self.__num_list = num_list
        self.__count_list = [0] * len(num_list)
        self.__sorted_list = []

    def __insert_number(self, number, index):
        """
        Method to insert number into perfect place in sorted list
        :param number: Number to be inserted
        :param index: index at which number fits
        :return: None
        """
        self.__sorted_list = self.__sorted_list[0:index] + [number] + self.__sorted_list[index:]
        # print(self.__sorted_list)

    def __find_index_in_sorted(self, number):
        """
        Method to find index of particular number should be inserted in sorted list
        :param number: Number to be inserted
        :return: index of the number in sorted list
        """
        high = len(self.__sorted_list) - 1
        low = 0
        while low <= high:
            mid = low + int(int(high - low) / 2)
            # print(mid)
            if mid + 1 > len(self.__sorted_list) - 1 and self.__sorted_list[mid] >= number:
                self.__insert_number(number, mid)
                return mid
            elif mid + 1 > len(self.__sorted_list) - 1 and self.__sorted_list[mid] <= number:
                self.__insert_number(number, mid + 1)
                return mid + 1
            elif self.__sorted_list[mid] <= number <= self.__sorted_list[mid + 1]:
                self.__insert_number(number, mid + 1)
                return mid + 1
            elif self.__sorted_list[mid] > number:
                high = mid - 1
            else:
                low = mid + 1
        return 0

    def calculate_count_smaller_items(self):
        self.__count_list[len(self.__num_list) - 1] = 0
        self.__sorted_list = [self.__num_list[len(self.__num_list) - 1]]
        # print(self.__sorted_list)
        for i in range(len(self.__num_list) - 2, -1, -1):
            self.__count_list[i] = self.__find_index_in_sorted(self.__num_list[i])
            # print('Count for index {0} ,{1}'.format(i, self.__count_list[i]))

        return self.__count_list


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        num_list = [int(x) for x in input().split()]
        smaller_elements = SmallerElementsInRight(num_list)
        print(smaller_elements.calculate_count_smaller_items())
        t -= 1
