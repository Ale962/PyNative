'''
Exercise 8

Word case by length

Uppercase if length > 5, else lowercase.
'''

words: list[str] = ["Hi", "Lambda", "Python", "Go"]
low_up = list(map(lambda x: x.upper() if len(x) > 5 else x.lower(), words))
print(low_up)