'''
Exercise 13
You have a list of words. Use map() and a lambda to transform them:

If the word length > 5 → uppercase it.

Otherwise → lowercase it.
'''


words: list[str] = ["Hi", "Lambda", "Python", "Go"]
low_up: list[str] = list(map(lambda x: x.lower() if len(x)<5 else x.upper(), words))
print(low_up)