nums: list[int] = [10, 15, 20, 21]

eve_odd = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', nums))

print(eve_odd)