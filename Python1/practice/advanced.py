def first_perfect_square(lst):
    for i in range(len(lst)):
        if lst[i] >= 0 and lst[i] ** 0.5 - int(lst[i] ** 0.5) == 0:
            return i
    return -1

def num_perfect_squares(lst):
    cnt = 0
    for i in range(len(lst)):
        if lst[i] >= 0 and lst[i] ** 0.5 - int(lst[i] ** 0.5) == 0:
            cnt += 1
    return cnt