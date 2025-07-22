def printEvenIndex():
    text = input('Write in here the word or text to be printed: ')
    text.replace(' ', '', -1)
    for l in text[::2]:
        print(l)

if __name__ == '__main__':
    printEvenIndex()