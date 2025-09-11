'''
Exercise 12
You have a list of ages. Use a lambda with map() to return "adult" if age ≥ 18, otherwise "minor".
'''

ages: list[int] = [5, 17, 18, 25, 12]
adult = list(map(lambda x: 'adult' if x >= 18 else 'minor', ages))
print(adult)