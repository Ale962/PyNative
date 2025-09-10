def exponent(base: int, exp: int) -> None:
    result = base ** exp
    factors = ' * '.join([str(base)] * exp)

    print(f'base = {base}')
    print()
    print(f'exponent = {exp}')
    print()
    print()
    print(f'{base} raises to the power of {exp} is: {result} i.e ({factors} = {result})')

if __name__ == '__main__':
    exponent(2, 5)
    print()
    exponent(5, 4)