"""
Author: Nishant

Problem : Check for balanced parenthesis in string.

Date : 01/05/2019
"""


class ParenthesisChecker:
    def __init__(self):
        self.__balanced = 'Empty'

    def get_balanced(self):
        return self.__balanced

    def check_for_balanced_parenthesis(self, string):
        stack = list()
        for char in string:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == '}':
                    if stack[len(stack) - 1] == '{':
                        stack.pop()
                    else:
                        stack.append(char)
                elif char == ']':
                    if stack[len(stack) - 1] == '[':
                        stack.pop()
                    else:
                        stack.append(char)
                elif char == ')':
                    if stack[len(stack) - 1] == '(':
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)

        if len(stack) == 0:
            self.__balanced = True
        else:
            self.__balanced = False


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        parenthesis_checker = ParenthesisChecker()
        string = str(input())
        parenthesis_checker.check_for_balanced_parenthesis(string)
        if parenthesis_checker.get_balanced() == True:
            print('balanced')
        else:
            print('not balanced')
