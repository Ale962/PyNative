pairs: list[tuple] = [(1, 5), (2, 3), (4, 1), (3, 4)]

pairs.sort(key=lambda x: x[1])

print(pairs)