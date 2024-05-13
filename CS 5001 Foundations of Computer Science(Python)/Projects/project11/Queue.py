'''
    Project 9: Stacks and Queues, a queue class
    Hang Zhao
    11/16/2023
'''


class Queue:
    ''' queue class'''

    def __init__(self, max_size):
        ''' Constructor'''
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.items = [None] * max_size

    def is_empty(self):
        ''' is_empty -- returns True if the queue is empty, False otherwise'''
        return self.head == self.tail

    def is_full(self):
        ''' is_full -- returns True if the queue is full, False otherwise'''
        return (self.tail + 1) % self.max_size == self.head

    def enqueue(self, item):
        ''' enqueue -- adds something to the end of the queue'''
        if self.is_full():
            raise Exception("Queue is full")
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size

    def dequeue(self):
        ''' dequeue -- removes something from the front of the queue'''
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item

    def size(self):
        ''' size -- returns the number of elements in the queue'''
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.max_size - (self.head - self.tail)
