# File which will hold the implementation of Scoop
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Hang Zhao
# 11/2/2023
import math


class Scoop:
    '''Class Scoop
       Attributes: radius
       Methods: volume'''

    def __init__(self, radius):
        '''
        Constructor - creates a new instance of Scoop
        Parameters -
           self - the current object
           radius - the radius of the scoop
        '''
        self.radius = radius

    def volume(self):
        ''' Method - calculate the volume of the scoop
        Parameters:
           self - the current object
        '''
        return (4/3) * math.pi * self.radius ** 3
