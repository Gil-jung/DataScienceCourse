from sort import *
import random, time

if __name__ == '__main__':

    print("##### Sorting Comparison Project #######")
    random_list = [ random.randint(0, 10000) for i in range(10000) ]

    startTime1 = time.clock()
    selectionSort(random_list)
    endTime1 = time.clock()
    elapsedTime1 = endTime1 - startTime1
    print("The elapsed time for Selection Sort is : ", elapsedTime1)

    startTime2 = time.clock()
    insertionSort(random_list)
    endTime2 = time.clock()
    elapsedTime2 = endTime2 - startTime2
    print("The elapsed time for Insersion Sort is : ", elapsedTime2)

    startTime3 = time.clock()
    bubbleSort(random_list)
    endTime3 = time.clock()
    elapsedTime3 = endTime3 - startTime3
    print("The elapsed time for Bubble Sort is : ", elapsedTime3)

    startTime4 = time.clock()
    mergeSort(random_list)
    endTime4 = time.clock()
    elapsedTime4 = endTime4 - startTime4
    print("The elapsed time for Merge Sort is : ", elapsedTime4)

    startTime5 = time.clock()
    quickSort(random_list)
    endTime5 = time.clock()
    elapsedTime5 = endTime5 - startTime5
    print("The elapsed time for Quick Sort is : ", elapsedTime5)

    startTime6 = time.clock()
    sorted(random_list)
    endTime6 = time.clock()
    elapsedTime6 = endTime6 - startTime6
    print("The elapsed time for Built in function Sort is : ", elapsedTime6)

