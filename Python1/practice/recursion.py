def f1(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + f1(lst[1:])

def f2(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + f2(n // 2)
        else:
            return 1 + f2(3 * n + 1)