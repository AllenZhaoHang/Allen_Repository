'''
    caculate distance between two points
    距离 = √((x2 - x1)² + (y2 - y1)² + (z2 - z1)²)
    Hang Zhao
    10/22/2023
'''
import math


class Point():
    '''class Point
    Attributes: x y z
    Methods: get_distance
    '''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, other=None):
        '''caculate distance'''
        if other is None:
            return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        else:
            x = (self.x - other.x) ** 2
            y = (self.y - other.y) ** 2
            z = (self.z - other.z) ** 2
            return math.sqrt(x + y + z)

    def __str__(self):
        '''
        Method -- returns a string that represents this coffee
        Parameters:
           self -- the current object
        '''
        return f'Point: ({self.x}, {self.y}, {self.z})'
