def sum_to_10() -> None:
    print('Printing current and previous number sum in a range(10)')
    s = 0
    for n in range(10):
        s += n
        if n == 0:
            print(f'Current Number: {n} Previous Number:  {n}  Sum:  {s}')
        else:
            print(f'Current Number: {n} Previous Number:  {n-1}  Sum:  {s}')


if __name__ == '__main__':
    sum_to_10()