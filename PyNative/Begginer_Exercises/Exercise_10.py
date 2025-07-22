def evenodds(l1: list[int], l2: list[int]):
    new_list: list[int] = []
    for n in l1:
        if n % 2 == 0:
            new_list.append(n)
    for x in l2:
        if x % 2 != 0:
            new_list.append(x)
    return new_list