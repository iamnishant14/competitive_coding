"""
Author: Nishant

Problem : Leaders in an array where element is greater or qual to elements to it right.

Date : 08/05/2019
"""


class LeadersInArray:
    def __init__(self):
        self.__list_leaders = list()

    def find_leaders(self, number_list):
        size = len(number_list)
        leader_right = [0 for i in range(size)]

        for i in range(size - 1, -1, -1):
            if i == size - 1:
                leader_right[i] = number_list[i]
            else:
                if number_list[i] >= leader_right[i + 1]:
                    leader_right[i] = number_list[i]
                else:
                    leader_right[i] = leader_right[i + 1]

        for i in range(size):
            if number_list[i] == leader_right[i]:
                self.__list_leaders.append(number_list[i])

        return self.__list_leaders


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        length = int(input())
        leaders_in_array = LeadersInArray()
        number_list = list(map(int, input().split()))
        leaders_list = leaders_in_array.find_leaders(number_list)
        print(*leaders_list)
