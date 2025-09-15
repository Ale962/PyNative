'''
OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
'''
from Exercise_6 import *

if __name__ == '__main__':

    bus1: Bus = Bus('Volvo', 120.00, 12000.00)
    print(isinstance(bus1, Vehicle))