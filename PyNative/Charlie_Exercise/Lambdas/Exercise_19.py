'''
Exercise 19
You have a list of students with scores.

Keep only those who passed (≥ 60).

Map them into dictionaries with "name" and "status" where "status" is "pass".
'''

students: dict[str, str|int] = [
    {"name": "Anna", "score": 55},
    {"name": "Ben", "score": 75},
    {"name": "Cara", "score": 62}
]

pass_exam: list[dict[str, str]] = list(map(lambda x: {'name': x['name'], 'status': 'pass'}, filter(lambda x: x['score'] >= 60, students)))

for student in pass_exam:
    print(student)