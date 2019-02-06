class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):

    def __str__(self):

    def __gt__(self, other):

    def __lt__(self, other):

    def __repr__(self):


class CircularQueue:
    M = 0
    front = 0
    rear = 0
    queue = [ ]

    def __init__(self, maxSize):
        self.M = maxSize
        self.queue = [None] * maxSize

    def enqueue(self, element):

    def dequeue(self):

    def multi_dequeue(self, count):

    def peek(self):

    def is_empty(self):

    def is_full(self):