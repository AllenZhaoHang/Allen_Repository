'''
    Project 9: Stacks and Queues, a Stack class
    Hang Zhao
    11/16/2023
'''


class Stack:
    ''' stack class'''

    def __init__(self):
        ''' Constructor'''
        self.stack = []

    def push(self, item):
        ''' push -- adds something to the end of the stack '''
        self.stack.append(item)

    def pop(self):
        ''' pop -- removes something from the end of the stack '''
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        ''' is_empty -- returns True if the stack is empty, False otherwise '''
        return len(self.stack) == 0

    def peek(self):
        ''' peek -- returns the element at the end of the stack without removing it'''
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def __len__(self):
        ''' __len__ -- returns the number of elements in the stack'''
        return len(self.stack)
