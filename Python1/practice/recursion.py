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

def f3(lst):
    if lst == []:
        pass
    else:
        print(lst[-1])
        f3(lst[0:-1])

def f4(lst):
    if lst == []:
        pass
    else:
        if lst[0] % 2 == 1:
            print(lst[0] * 3)
        f4(lst[1:])

def f5(lst):
    if lst == []:
        pass
    else:
        if lst[-1] % 2 == 1:
            print(lst[-1] * 3)
        else:
            print(lst[-1])
        f5(lst[:-1])

def f6(lst):
    if lst == []:
        return lst
    else:
        if type(lst[0]) == list:
            return f6(lst[0]) + f6(lst[1:])
        else:
            return [lst[0]] + f6(lst[1:])