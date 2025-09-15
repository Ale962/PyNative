'''
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''

class Vehicle:

    color = 'White'

    def __init__(self, name: str, max_speed: float, mileage: float, capacity: int = 50) -> None:
        self.__set_name(name)
        self.__set_max_speed(max_speed)
        self.__set_mileage(mileage)
        self.__set_capacity(capacity)

    def __set_name(self, name: str) -> None:
        self.__name = name

    def __set_max_speed(self, max_speed: float) -> None:
        self.__max_speed = max_speed

    def __set_mileage(self, mileage: float) -> None:
        self.__mileage = mileage

    def __set_capacity(self, capacity: int) -> None:
        self.__capacity = capacity

    def fare(self) -> float:
        return self.get_seating_capacity() * 100

    def get_max_speed(self) -> float:
        return self.__max_speed
    
    def get_mileage(self) -> float:
        return self.__mileage
    
    def get_name(self) -> str:
        return self.__name
    
    def get_seating_capacity(self) -> int:
        return self.__capacity
    
    def get_fare(self) -> str:
        return f'The fare for this vehicle is {self.fare()}'

    def __repr__(self):
        return f'{Vehicle.color}, {self.get_name()}, speed: {self.get_max_speed()}, mileage: {self.get_mileage()}, capacity: {self.get_seating_capacity()}'