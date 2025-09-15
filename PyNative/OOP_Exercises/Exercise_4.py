'''
OOP Exercise 4: Class Inheritance

Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.
'''

from Exercise_1 import Vehicle

class Bus(Vehicle):

    def __init__(self, name, max_speed: float, mileage: float, capacity: int = 50):
        super().__init__(name, max_speed, mileage)
        self.__set_capacity(capacity)

    def __set_capacity(self, capacity: int) -> None:
        self.__capacity = capacity

    def get_seating_capacity(self) -> int:
        return self.__capacity
    
    def __repr__(self):
        return super().__repr__() + f' and the bus capacity is {self.get_seating_capacity()}'
    

if __name__ == '__main__':

    bus1: Bus = Bus('Volvo', 120.00, 12000.00, 75)
    print(bus1)