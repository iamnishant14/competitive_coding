"""
Author: Nishant

Problem : Celsius to Fahrenheit conversion.

Date : 09/11/2019
"""
import sys


class CelsiusToFahrenheit:
    def __init__(self, celsius):
        self.__celsius = celsius
        self.__fahreheit = sys.maxsize

    def celsius_to_fahreheit(self):
        self.__fahreheit = ((9 * self.__celsius) / 5) + 32

    def get_fahrenheit(self):
        return self.__fahreheit


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        celsius = int(input())
        c2f = CelsiusToFahrenheit(celsius)
        c2f.celsius_to_fahreheit()
        print(c2f.get_fahrenheit())
        t -= 1
