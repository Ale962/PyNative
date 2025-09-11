'''
Exercise 10

Pass / Fail scores
'''

scores: list[int] = [30, 55, 60, 85, 59]
passes: list[str] = list(map(lambda x: 'pass' if x >= 60 else 'fail', scores))
print(passes)