def half_star_pyramid(n: int) -> None:
    if n == 0:
        return n
    else:
        print('* ' * n)
        half_star_pyramid(n-1)


if __name__ == '__main__':
    half_star_pyramid(5)