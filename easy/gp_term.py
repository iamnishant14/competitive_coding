"""
Author: Nishant

Problem : Nth GP Term.

Date : 13/11/2019
"""
import math
import sys


class GPTerm:
    def __init__(self):
        self.__nth_gp_term = -1 * sys.maxsize

    def calculate_nth_term(self, a, b, n):
        return math.floor(a * (math.pow((b / a), n - 1)))


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        a, b = input().split()
        a = int(a)
        b = int(b)
        n = int(input())
        print(GPTerm().calculate_nth_term(a, b, n))
        t -= 1
