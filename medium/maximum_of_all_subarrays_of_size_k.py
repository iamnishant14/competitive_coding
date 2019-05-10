"""
Author: Nishant

Problem : Maximum of all subarrays of size K(Given).

Date : 10/05/2019
"""
# from utils.logger import CompetitiveCodingLogger

# logger = CompetitiveCodingLogger(module_name=__name__).get_logger()
from collections import deque


class MaximumOfAllSubarraysOfSizeK:
    def __init__(self):
        self.__max_list = list()

    def calculate_max_of_all_subarrays_of_size_k(self, number_list, size):
        index_queue = deque()
        number_list_length = len(number_list)

        for i in range(size):
            while index_queue and int(number_list[i]) >= int(number_list[index_queue[-1]]):
                index_queue.pop()
            index_queue.append(i)

        for i in range(size, number_list_length):
            self.__max_list.append(number_list[index_queue[0]])
            """
            Remove indexes from queue if it's out of range for current subarray
            """
            while index_queue and index_queue[0] <= i - size:
                index_queue.popleft()
            # logger.info('Indexes in index queue after removing out of range elements: {0}'.format(index_queue))

            """
            Include only indexes where element at current index is greater than element at index = queue[last]
            """
            while index_queue and int(number_list[i]) > int(number_list[index_queue[-1]]):
                index_queue.pop()
            index_queue.append(i)
            # logger.info('Indexes in index queue after next element: {0}'.format(index_queue))

        self.__max_list.append(number_list[index_queue[0]])
        # logger.info('Max list is : {0}'.format(self.__max_list))
        return self.__max_list


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        length, size = input().split()
        length = int(length)
        size = int(size)
        max_of_all_subarrays = MaximumOfAllSubarraysOfSizeK()
        number_list = input().split()
        max_list = max_of_all_subarrays.calculate_max_of_all_subarrays_of_size_k(number_list, size)
        print(*max_list)
