'''
OOP Exercise 6: Class Inheritance

Given:

Create a Bus child class that inherits from the Vehicle class. The default fare charge for any vehicle is its seating capacity multiplied by 100 (seating capacity * 100).

If the vehicle is a Bus instance, we need to add an extra 10% to the full fare as a maintenance charge. Therefore, the total fare for a Bus instance will be the final amount, calculated as total fare plus 10% of the total fare. (final amount = total fare + 10% of the total fare.)

Note: The bus seating capacity is 50, so the final fare amount should be 5500.

Use the following code for your parent Vehicle class. We need to access the parent class from within a method of a child class.
'''
from Exercise_1 import Vehicle

class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage, capacity = 50):
        super().__init__(name, max_speed, mileage, capacity)

    def fare(self):
        return super().fare() + (0.1 * super().fare())
    
if __name__ == '__main__':

    bus1: Bus = Bus('Volvo', 120.00, 12000.00)
    print(bus1)
    print(bus1.get_fare())