def palindromeNumber(n: int) -> None:
    textnumber = str(n)
    textinv = textnumber[::-1]
    if textnumber ==  textinv:
        print(f'Yes, {n} is a palindrome')
    else:
        print(f'No, {n} is not a palindrome')

    
if __name__ == '__main__':
    palindromeNumber(121)
    palindromeNumber(125)