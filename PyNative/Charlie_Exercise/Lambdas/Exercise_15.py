'''
Exercise 15
You have a list of students with their scores. Use map() and a lambda to return "pass" if score ≥ 60, else "fail".
'''

scores: list[int] = [30, 55, 60, 85, 59]
passes = list(map(lambda x: 'pass' if x >= 60 else 'fail', scores))
print(passes)