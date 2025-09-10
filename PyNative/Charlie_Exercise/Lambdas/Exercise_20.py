'''
Exercise 5 (Challenge 🚀)
You have a list of words.

Keep only the words that start with a vowel (a, e, i, o, u).

Map them to uppercase if they have more than 4 letters, else lowercase.
'''

words: list[str] = ["apple", "egg", "cat", "owl", "up", "idea", "on"]

vowel: list[str] = ['a', 'e', 'i', 'o', 'u']

upp_vowel = list(map(lambda x: x.upper() if len(x)>4 else x.lower(), filter(lambda x: x[0] in vowel, words)))

print(upp_vowel)