from DataStructure import *

def match(string):
    s = Stack()
    for i in range(len(string)):
        if string[i] == '(':
            s.push(i)
        elif string[i] == ')':
            print("(" + str(s.pop()) + ', ' + str(i) + ')')


def hanoi(n):
    t1 = Stack()
    t2 = Stack()
    t3 = Stack()
    for i in range(n, 0, -1):
        t1.push(i)
    print(t1.items, t2.items, t3.items)

    def move(n, x, y, z):
        if n > 0:
            move(n-1, x, z, y)
            y.push(x.pop())
            print(t1.items, t2.items, t3.items)
            move(n-1, z, y, x)

    move(n, t1, t2, t3)