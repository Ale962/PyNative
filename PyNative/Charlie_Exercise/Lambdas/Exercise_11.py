'''
Exercise 1
Use a lambda with map() to take this list of numbers and return "positive" if the number is greater than 0, "negative" if less than 0, and "zero" if equal to 0.
'''

nums: list[int] = [-3, -1, 0, 1, 5]
neg_zero_pos: list[str] = list(map(lambda x: 'negative' if x < 0 else 'zero' if x == 0 else 'positive', nums))
print(neg_zero_pos)