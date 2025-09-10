def evenodds(l1: list[int], l2: list[int]) -> list|None:
    new_list: list[int] = []
    for n in l1:
        if n % 2 == 0:
            new_list.append(n)
    for x in l2:
        if x % 2 != 0:
            new_list.append(x)
    
    new_list_2 = [(x for x in l1 if x%2 == 0) and (y for y in l2 if y%2 != 0)]
    print(new_list_2)
    print(new_list)
    return new_list


if __name__ == '__main__':
    l1: list[int] = [x for x in range(0,21,2)]
    l2: list[int] = [x for x in range(1,21,2)]

    print(l1)
    print(l2)

    evenodds(l1, l2)