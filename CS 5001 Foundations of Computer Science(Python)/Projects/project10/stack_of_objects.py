'''
    class StackOfObjects
    Hang Zhao
    11/10/2023
'''


class StackOfObjects:
    ''' class StackOfObjects '''

    def __init__(self):
        ''' init function '''
        self.stack = []

    def push(self, object):
        ''' push function '''
        self.stack.append(object)

    def pop(self):
        ''' pop function '''
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def top(self):
        ''' top function '''
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def isempty(self):
        ''' isempty function '''
        return len(self.stack) == 0
