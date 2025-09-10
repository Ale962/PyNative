words: list[str] = ["Hi", "Lambda", "Python", "Go"]

low_up = list(map(lambda x: x.lower() if len(x)<5 else x.upper(), words))

print(low_up)