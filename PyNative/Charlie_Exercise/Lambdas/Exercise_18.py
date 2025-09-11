'''
Exercise 18

Divisible by 5, then small/big
'''

nums: list[int] = [10, 25, 40, 55, 70, 3, 8]
small_big: list[str] = list(map(lambda x: 'big' if x >= 50 else 'small', filter(lambda x: x % 5 == 0, nums)))
print(small_big)