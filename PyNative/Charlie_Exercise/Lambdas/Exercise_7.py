'''
Exercise 7

Adult or Minor
'''

ages: list[int] = [5, 17, 18, 25, 12]
adult: list[int] = list(map(lambda x: 'adult' if x >= 18 else 'minor', ages))
print(adult)