from recursion import *

if __name__ == "__main__":

    print("##### f1: return the sum of the elements in the list #######")
    print(f1([1, 2, 3, 4]))
    print(f1([]))
    print()

    print("##### f2: return the number of the steps of Collatz Conjecture function #######")
    print(f2(1))
    print(f2(6))
    print(f2(11))
    print(f2(637228127))
    print()

    print("##### f3: prints out the elements in the list in reverse order #######")
    f3([1, 2, 3])
    f3([])
    f3([3, 2, 1])
    print()

    print("##### f4: multiplies all of the odd elements in the list by 3 and prints out each tripled element #######")
    f4([1, 2, 3, 4])
    f4([2, 4])
    f4([11, 42, 63, 15])
    print()

    print("##### f5: multiplies all of the odd elements in the list by 3 and prints out modified list in reverse order #######")
    f5([1, 2, 3, 4])
    f5([2, 4])
    f5([11, 42, 64, 15])
    print()

    print("##### f6: return one dimensional list #######")
    print(f6(['baa']))
    print(f6(['baa', [4, True, [10, 5], [1, 2, ['moo']]], ["chirp"]]))
    print(f6([]))
    print(f6([[[[[[[[[[[[[[[[[[[23]]]]]]]]]]]]]]]]]]]))
    print()