ages = [5, 17, 18, 25, 12]

adult = list(map(lambda x: 'adult' if x >= 18 else 'minor', ages))

print(adult)