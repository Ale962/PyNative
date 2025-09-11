'''
Exercise 1

Cube a number

Write a lambda function that takes a number and returns its cube.
'''
from typing import Callable

cube: Callable[[int],int] = lambda x: x**3
print(cube(5)) 