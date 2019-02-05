from sequence import *
from sort import *
from search import *
from BinarySearchTree import *
from DataStructure import *

if __name__ == "__main__":

    print("##### fib: Fibonacci Numbers #######")
    print(fib(10))
    print()

    print("##### Selection Sort #######")
    print(selectionSort([29, 64, 73, 34, 20]))
    print()

    print("##### Insertion Sort #######")
    print(insertionSort([7, 5, 42, 6, 3, 15]))
    print()

    print("##### Bubble Sort #######")
    print(bubbleSort([32, 6, 41, 22, 15, 59]))
    print()

    print("##### Merge Sort #######")
    print(mergeSort([84, 27, 49, 91, 32, 53, 63, 17]))
    print()

    print("##### Quick Sort #######")            # enumerate 를 쓰면 값이 왜 return 안되는지...
    print(quickSort([7, 42, 6, 3, 15, 12]))
    print()

    print("##### Binary Search #######")
    print(bsearch([12, 25, 32, 37, 41, 48, 58, 60, 66, 73, 74, 79, 83, 91, 95], 73))
    print()

    print("##### Binary Search Tree #######")
    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
    bst = BinarySearchTree()
    for x in array:
        bst.insert(x)
    print(bst.find(15))
    print(bst.find(17))

    # depth first
    bst.pre_order_traversal()
    bst.in_order_traversal()
    bst.post_order_traversal()
    # breath first
    bst.level_order_traversal()

    print(bst.delete(55))

    # depth first
    bst.pre_order_traversal()
    bst.in_order_traversal()
    bst.post_order_traversal()
    # breath first
    bst.level_order_traversal()

    print(bst.delete(14))

    # depth first
    bst.pre_order_traversal()
    bst.in_order_traversal()
    bst.post_order_traversal()
    # breath first
    bst.level_order_traversal()

    print(bst.delete(11))

    # depth first
    bst.pre_order_traversal()
    bst.in_order_traversal()
    bst.post_order_traversal()
    # breath first
    bst.level_order_traversal()

    print()

    print("##### Linked List #######")
    node1 = Node("car")
    node2 = Node("bus")
    node3 = Node("lorry")
    node1.next = node2
    node2.next = node3
    print_list(node1)
    print()