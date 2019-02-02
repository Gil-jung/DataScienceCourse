def fib(n):
    a, b = 0, 1
    c = []
    for i in  range(n):
        c.append(a)
        a, b = b, b + a
    return c
