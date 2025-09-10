def multiply_sum(n1: int , n2: int):
    m = n1 * n2

    if m <= 1000:
        return f'The result is {m}'
    else:
        s = n1 + n2
        return f'The result is {s}'
    

