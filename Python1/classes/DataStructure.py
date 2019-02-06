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

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items)-1]


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