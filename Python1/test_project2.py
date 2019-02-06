from DataStructure import *
from datastructureapplication import *

if __name__ == '__main__':

    print("##### Parenthesis Matching #######")
    match("(a+(b+c)+d)")
    print()

    print("##### Tower of Hanoi #######")  #ch.22 Page 26
    hanoi(3)
    print()

    print("##### MaxHeap #######")
    h = MaxHeap([15, 35, 65, 20, 17, 80, 12, 45, 2, 4])
    print(h.heap)
    h.traverse()
    print(h.sort())
    print()