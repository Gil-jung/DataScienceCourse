def selection_sort(lst):
    for i in range(len(lst)-1):
        ind = i
        for j in range(i+1, len(lst)):
            if lst[ind] > lst[j]:
                ind = j
        lst[i], lst[ind] = lst[ind], lst[i]
    return lst


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        halfway = len(lst) // 2
        list1 = lst[0:halfway]
        list2 = lst[halfway:len(lst)]
        newlist = merge(merge_sort(list1), merge_sort(list2))
    return newlist

def merge(a, b):
    c = []
    index_a = 0
    index_b = 0
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            c.append(a[index_a])
            index_a += 1
        elif a[index_a] >= b[index_b]:
            c.append(b[index_b])
            index_b += 1
    c.append(a[:len(a)])
    c.append(b[:len(b)])
    return c
