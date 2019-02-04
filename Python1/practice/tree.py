def f21(tree):
    if tree == []:
        return 0
    else:
        return 1 + max(f21(tree[1]), f21(tree[2]))

def f22(tree):
    if tree == []:
        return 0
    else:
        return 1 + f22(tree[1]) + f22(tree[2])