from tree import *

if __name__ == '__main__':

    print("##### f21: Returns the height of the tree #######")
    print(f21([]))
    print(f21([1, [], []]))
    print(f21([1, [1, [], []], []]))
    print()

    print("##### f22: Returns the number of the node in the tree #######")
    print(f22([]))
    print(f22([1, [], []]))
    print(f22([1, [1, [], []], [1, [], []]]))
    print()