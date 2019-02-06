class Node:
    def __init__(self, contents=None, next=None):
        self.contents = contents
        self.next = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)


def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()


class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, item):
        self.top += 1
        return self.items.append(item)

    def pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.items.pop()

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    def peek(self):
        return self.items[self.top]


class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def delete(self):
        itemToDelete = self.items[0]
        del self.items[0]
        return itemToDelete

    def size(self):
        return len(self.items)

    def report(self):
        return self.items


class MaxHeap:
    def __init__(self, items=[]):
        self.heap = []
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def pop(self):
        self.__swap(0, len(self.heap) - 1)
        max = self.heap.pop()
        self.__bubbleDown(0)
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 0:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __inorder(self, index):
        if index >= len(self.heap):
            return
        else:
            self.__inorder(2 * index + 1)
            print(self.heap[index], end=' ')
            self.__inorder(2 * index + 2)

    def traverse(self):
        self.__inorder(0)
        print()

    def sort(self):
        tmp = self.heap[:]
        result = []
        for i in range(len(self.heap)):
            result.append(self.pop())
        self.heap = tmp
        result.reverse()
        return result




