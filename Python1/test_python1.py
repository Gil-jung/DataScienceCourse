from sequence import *
from sort import *

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