"""
Author: Nishant

Problem : Reverse words in strings seperated by '.' .

Date : 03/05/2019
"""


class ReverseWords:
    """
    Reverse words based on list of words.
    """

    def reverseString(self, string_list):
        reversed_list = list()
        length = len(string_list)
        for items in range(0, length):
            reversed_list.append(string_list[length - items - 1])
        return reversed_list


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        reverse_words = ReverseWords()
        """
        Take input as list of string that are seperated by '.' 
        """
        string_list = input().split('.')
        reversed_list = reverse_words.reverseString(string_list)

        """
        Print list of string seperated by '.'
        """
        print(*reversed_list, sep='.')
