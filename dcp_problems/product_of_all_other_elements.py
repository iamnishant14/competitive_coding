"""
Author: Nishant

Problem : Find product of all the numbers except current number in an array.

Date : 18/04/2020
"""


class ProductOfAllOtherElements:
    def __init__(self, number_list):
        self.__number_list = number_list

    def calculate_prod(self):
        """
        Calculate left and right product of all the numbers in an array.
        :return: Final list of product of all numbers except numbers in current indices.
        """
        left_prod = [1] * (len(self.__number_list))
        left_prod[0] = self.__number_list[0]
        for i in range(1, len(self.__number_list)):
            left_prod[i] = left_prod[i - 1] * self.__number_list[i]

        right_prod = [1] * (len(self.__number_list))
        right_prod[len(self.__number_list) - 1] = self.__number_list[len(self.__number_list) - 1]
        for i in range(len(self.__number_list) - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * self.__number_list[i]

        print(left_prod, right_prod)
        final_prod = []
        for i in range(len(self.__number_list)):
            if i == 0:
                final_prod.append(right_prod[i + 1])
            elif i == len(self.__number_list) - 1:
                final_prod.append((left_prod[i - 1]))
            else:
                final_prod.append(left_prod[i - 1] * right_prod[i + 1])
        return final_prod


if __name__ == '__main__':
    tests = int(input())
    while tests > 0:
        length = int(input())
        nums = [int(x) for x in input().split()]
        prod_all_elem = ProductOfAllOtherElements(nums)
        print(prod_all_elem.calculate_prod())
        tests -= 1
