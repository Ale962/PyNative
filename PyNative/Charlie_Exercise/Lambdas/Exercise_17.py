'''
Exercise 17

Adults in uppercase names from dicts
'''

people: list[dict[str, str|int]] = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30}
]
adult: list[str] = list(map(lambda x: x['name'].upper(), filter(lambda x: x['age'] >= 18, people)))
print(adult)