'''
Exercise 4

Sort by second element

Sort a list of tuples by the second value using a lambda.
'''

pairs: list[tuple] = [(1, 5), (2, 3), (4, 1), (3, 4)]
pairs.sort(key=lambda x: x[1])
print(pairs)