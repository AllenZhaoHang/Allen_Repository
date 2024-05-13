'''
    class ContainerOfObjects
    Hang Zhao
    11/10/2023
'''
from stack_of_objects import StackOfObjects
from queue_of_objects import QueueOfObjects
from object import Object


class ContainerOfObjects:
    ''' class ContainerOfObjects '''

    def __init__(self):
        ''' init function '''
        self.stack = StackOfObjects()
        self.queue = QueueOfObjects()

    def loadFromFile(self, filename):
        ''' loadFromFile function'''
        original_data = []
        with open(filename, "r") as f:
            for line in f:
                name, value = line.strip().split(",")
                obj = Object(name, value)
                original_data.append(obj)
        return original_data

    def printOriginalData(self, original_data):
        ''' printOriginalData function'''
        for obj in original_data:
            print(f"{obj.name}: {obj.value}")

    def printStack(self, original_data):
        ''' printStack function'''
        for obj in original_data:
            self.stack.push(obj)
        while not self.stack.isempty():
            obj = self.stack.pop()
            print(f"{obj.name}: {obj.value}")

    def printQueue(self, original_data):
        ''' printQueue function'''
        for obj in original_data:
            self.queue.enqueue(obj)
        while not self.queue.isEmpty():
            obj = self.queue.dequeue()
            print(f"{obj.name}: {obj.value}")
