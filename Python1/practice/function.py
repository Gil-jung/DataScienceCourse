from functools import *

def f1(lst):
    return len(list(filter(lambda x: x % 2 == 1, lst)))

def f2(lst):
    list(map(print, filter(lambda x: x % 2 == 1, lst)))

def f3(lst):
    return reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 == 1, lst)))

def f4(lst):
    return sum(map(lambda x: (x[1] % 2 == 1) * x[0], list(enumerate(lst))))

def f5(lst):
    return list(map(lambda x: x**2, lst))

def f6(lst):
    return reduce(lambda x, y: max(x, y), lst)