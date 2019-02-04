from advanced import *

if __name__ == '__main__':

    print("##### ch14-a-1. Searching #######")
    print(first_perfect_square(list(range(5))))
    print(first_perfect_square([2, 4, 6, 8, 10, 12]))
    print(first_perfect_square([6, 8, 10, 12, 9]))
    print(first_perfect_square([1, 1]))
    print(first_perfect_square([-6, 6, -2, 2, -3, 3]))
    print(first_perfect_square([42]))
    print(first_perfect_square([]))
    print(first_perfect_square([123456789123456789**2]))
    print()

    print("##### ch14-a-2. Counting #######")
    print(num_perfect_squares([]))
    print(num_perfect_squares([0]))
    print(num_perfect_squares([0, 1]))
    print(num_perfect_squares(list(range(10))))
    print(num_perfect_squares([3]*10))
    print(num_perfect_squares([4]*10))
    print(num_perfect_squares([-4, -2, 0, 2, 4]))
    print()