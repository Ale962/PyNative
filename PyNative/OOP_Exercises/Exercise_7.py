'''
OOP Exercise 7: Check type of an object

Write a program to determine which class a given Bus object belongs to.

'''

from Exercise_6 import *

if __name__ == '__main__':

    bus1: Bus = Bus('Volvo', 120.00, 12000.00)
    print(type(bus1))