'''
Exercise 5

Uppercase words

Use map() to make a list of words uppercase.
'''

words: list[str] = ["hello", "python", "lambda"]
upper: list[str] = list(map(lambda x: x.upper(), words))
print(upper) 