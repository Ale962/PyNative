'''
OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.
'''

from Exercise_1 import Vehicle

class Bus(Vehicle):
    
    def __init__(self, name,  max_speed, mileage):
        super().__init__(name, max_speed, mileage)


if __name__ == '__main__':

    bus1: Bus = Bus('Volvo', 120.00, 12000.00)
    print(bus1)