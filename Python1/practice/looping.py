def f1(n):
    list(map(lambda x: print(*range(1, x+1)), range(1, n+1)))

def f2(n):
    list(map(lambda x: print(*range(1+sum(range(x)), 1+sum(range(x))+x)), range(1, n+1)))

def f3(n):
    list(map(lambda x: print(*range(1+sum(range(x)), 1+sum(range(x))+x)), range(1, n+1)))
    list(map(lambda x: print(*range(1+sum(range(x)), 1+sum(range(x))+x)), range(n-1, 0, -1)))

def f4(n):
    list(map(lambda x: print(*range(1+sum(range(x)), 1+sum(range(x))+x)), range(1, n+1)))
    list(map(lambda x: print(*range(1+sum(range(n+1))+sum(range(n-1, x, -1)), 1+sum(range(n+1))+sum(range(n-1, x, -1))+x)), range(n-1, 0, -1)))
