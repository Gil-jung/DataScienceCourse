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