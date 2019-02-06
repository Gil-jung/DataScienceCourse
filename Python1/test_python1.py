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

    print("##### Binary Search Tree Simple #######")
    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
    bst = BinarySearchTreeSimple()
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

    print("##### Stack #######")
    myStack = Stack()
    myStack.push("john")
    myStack.push("kim")
    print(myStack.peek())
    print(myStack.pop())
    print(myStack.items)
    print()

    print("##### Queue #######")
    myQueue = Queue()
    myQueue.add("Bob")
    myQueue.add("Brodie")
    myQueue.add("Carrie")
    myQueue.add("Tanya")
    print(myQueue.size())
    print(myQueue.report())
    print(myQueue.delete())
    print(myQueue.report())

    print("##### Binary Search Tree #######")
    bst = BinarySearchTree()
    input_data = [17, 5, 25, 2, 11, 29, 38, 9, 16, 7, 8]
    for i in input_data:
        bst.put(i, i)
    bst.root.inorder_traverse()
    #
    print('remove 5')
    bst.delete(5)
    bst.root.inorder_traverse()
    #
    print('put 39')
    bst.put(39, 39)
    bst.root.inorder_traverse()
    print()

