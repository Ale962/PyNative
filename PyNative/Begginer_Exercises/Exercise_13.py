def matrix(x: int, y:int = None) -> None:
    mat: list[list[int]] = []
    if not y:
        for r in range(x):
            row: list[int] = []
            for c in range(x):
                n = (c+1) * (r+1)
                row.append(n)
            mat.append(row)
    else:
        for r in range(y):
            row: list[int] = []
            for c in range(x):
                n = (c+1) * (r+1)
                row.append(n)
            mat.append(row)
    for l in mat:
        print(*l, sep=', ')

if __name__ == '__main__':
    matrix(10)
    matrix(10, 8)