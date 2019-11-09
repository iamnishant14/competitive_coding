"""
Author: Nishant

Problem : Quadratic roots of a equation.

Date : 10/11/2019
"""
import math
import sys


class QuadraticRoots:
    def __init__(self):
        self.__pos_root = -1 * sys.maxsize
        self.__neg_root = sys.maxsize

    def calculate_roots(self, a, b, c):
        d = int(((b * b) - (4 * a * c)))
        root_list = list()
        if d < 0:
            root_list = [-1] * 3
            return root_list
        if d == 0:
            x3 = math.floor((-1 * b) / (2.0 * a))
            root_list.append(x3)
            root_list.append(x3)
            return root_list
        d = math.sqrt(d)
        x1 = math.floor(((-1 * b) + d) / (2.0 * a))
        x2 = math.floor(((-1 * b) - d) / (2.0 * a))
        root_list.append(x1)
        root_list.append(x2)
        return root_list


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        quad_roots = QuadraticRoots()
        root_lists = quad_roots.calculate_roots(a, b, c)
        if len(root_lists) == 3:
            print('Imaginary')
        else:
            print(root_lists[0], root_lists[1])
        t -= 1
