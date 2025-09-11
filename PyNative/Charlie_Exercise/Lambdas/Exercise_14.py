'''
Exercise 14
You’re given a list of numbers. Use a lambda with map() to label each number as "even" or "odd".
'''

nums: list[int] = [10, 15, 20, 21]
eve_odd: list[str] = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', nums))
print(eve_odd)