# File which will hold the implementation of Carton
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Hang Zhao
# 11/2/2023
import math  # this gives you pi
import Scoop


class Carton:
    ''' Class: Carton
        Attributes: contains
        Methods: hasEnoughFor, remove'''

    def __init__(self, radius, height):
        ''' Constructor
            Parameters:
                self
                radius - radius of a carton
                height - height of a carton'''
        self.volume = math.pi * (radius ** 2) * height
        self.remaining_volume = self.volume

    def hasEnoughFor(self, scoop):
        ''' hasEnoughFor
            Parameters:
                scoop - the Scoop to be used on the Carton
            Return:
                whether or not the Carton contains enough to make a Scoop'''
        return self.remaining_volume >= scoop.volume()

    def remove(self, scoop):
        ''' remove
            Parameters:
                scoop - the Scoop to be used on the Carton
        '''
        if self.hasEnoughFor(scoop):
            self.remaining_volume -= scoop.volume()
