'''
Exercise 2

Negatives

Use map() to turn a list of numbers into their negatives.
'''

nums: list[int] = [1, 2, 3, 4, 5]
negative: list[int] = list(map(lambda x: -x, nums))
print(negative)