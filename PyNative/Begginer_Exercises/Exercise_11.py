def reverseNumber(x: int) -> None:
    x_str = str(x)

    for l in x_str[::-1]:
        print(l, end=' ')

if __name__ == '__main__':

    x = 7536
    reverseNumber(x)