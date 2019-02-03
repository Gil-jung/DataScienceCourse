def selectionSort(lst):
    for i in range(len(lst)-1):
        ind = i
        for j in range(i+1, len(lst)):
            if lst[ind] > lst[j]:
                ind = j
        lst[i], lst[ind] = lst[ind], lst[i]
    return lst

def insertionSort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def mergeSort(lst):
    if len(lst) < 2:
        return lst
    else:
        halfway = len(lst) // 2
        list1 = lst[:halfway]
        list2 = lst[halfway:]
        newlist = merge(mergeSort(list1), mergeSort(list2))
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
    c.extend(a[index_a:])
    c.extend(b[index_b:])
    return c

def quickSort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        smaller_list = []
        equal_list = []
        larger_list = []
        for val in lst:
            if val < pivot:
                smaller_list.append(val)
            elif val > pivot:
                larger_list.append(val)
            else:
                equal_list.append(val)
        return quickSort(smaller_list) + equal_list + quickSort(larger_list)


        # pivot_index = len(lst) // 2
        # smaller_list = []
        # larger_list = []
        # for i, val in enumerate(lst):
        #     if i != pivot_index:
        #         if val < lst[pivot_index]:
        #             smaller_list.append(val)
        #         else:
        #             larger_list.append(val)
        # return quickSort(smaller_list) + list(lst[pivot_index]) + quickSort(larger_list)