'''
    class QueueOfObjects
    Hang Zhao
    11/10/2023
'''


class QueueOfObjects:
    def __init__(self):
        self._queue = []

    def enqueue(self, object):
        ''' enqueue function'''
        self._queue.append(object)

    def dequeue(self):
        ''' dequeue function'''
        if len(self._queue) == 0:
            return None
        else:
            return self._queue.pop(0)

    def front(self):
        '''front function'''
        if len(self._queue) == 0:
            return None
        else:
            return self._queue[0]

    def isEmpty(self):
        '''isEmpty function'''
        return len(self._queue) == 0

    def __len__(self):
        '''len function'''
        return len(self._queue)

    def __str__(self):
        '''str function'''
        return f"QueueOfObjects({self._queue})"
