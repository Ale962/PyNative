'''
Exercise 3 

Names starting with “A”

Use filter() to extract names starting with “A”.
'''

names: list[str] = ["Alice", "Bob", "Amanda", "Charlie", "Angela"]
A_names = list(filter(lambda w: w[0] == 'A', names))
print(A_names)