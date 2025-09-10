def fibonacci_sequence(n: int):
    first = 0
    num = 1
    for i in range(n):
        res = num + first
        print(first, end=' ')
        first = num
        num = res

if __name__ == '__main__':
    fibonacci_sequence(15)