'''
Exercise 6

Positive / Negative / Zero
'''

nums: list[int] = [-3, -1, 0, 1, 5]
neg_zero_pos = list(map(lambda x: 'negative' if x < 0 else 'zero' if x == 0 else 'positive', nums))
print(neg_zero_pos)