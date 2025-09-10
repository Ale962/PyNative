'''
Exercise 1
You have a list of numbers.

First, filter only the numbers greater than 0.

Then, map them to "even" or "odd".
'''

nums: list[int] = [-3, -2, -1, 0, 1, 2, 3]

eve_odd = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', filter(lambda x: x > 0, nums)))

print(eve_odd)