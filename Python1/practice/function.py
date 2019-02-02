def f1(lst):
    return len(list(filter(lambda x: x % 2 == 1, lst)))

def f2(lst):
    list(map(print, filter(lambda x: x % 2 == 1, lst)))