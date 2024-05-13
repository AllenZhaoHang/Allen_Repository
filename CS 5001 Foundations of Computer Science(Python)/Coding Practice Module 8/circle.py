'''
    Write a class called Circle that represents a circle
    Hang Zhao
    10/22/2023
'''
import math


class Circle():
    ''' calss circle '''

    def __init__(self, x, y, radius):
        if not isinstance(x, float):
            raise ValueError("x must be float")
        if not isinstance(y, float):
            raise ValueError("y must be float")
        if not isinstance(radius, float) or radius < 0:
            raise ValueError("radius must be float and positive")
        self.x = x
        self.y = y
        self.radius = float(radius)

    def get_area(self):
        '''area'''
        return 3.14 * (float(self.radius) ** 2)

    def get_distance(self, x, y):
        '''distance'''
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def __str__(self):
        '''
        Method -- returns a string that represents this coffee
        Parameters:
           self -- the current object
        '''
        a = f'Circle: center at ({self.x}, {self.y}) with radius {self.radius}'
        return a
