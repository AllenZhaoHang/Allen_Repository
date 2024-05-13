# File which will implement the IceCreamShoppe class
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Hang Zhao
# 11/2/2023
import Carton
import Scoop


class IceCreamShoppe:
    '''Class IceCreamShoppe
        Attributes: carton_radius, carton_height, cartons_used
        Methods: serve, cartonsUsed'''

    def __init__(self, carton_radius, carton_height):
        ''' Constructor
        Parameters: carton_radius, carton_height - dimensions for a carton
        Return: nothing'''
        self.carton_radius = carton_radius
        self.carton_height = carton_height
        self.cartons_used = 0

    def serve(self, numScoops, scooper):
        ''' serve method
        Parameters: numScoops - number of scoops wanted; 
            scooper - the specific Scoop to use
        Return: nothing'''
        required_volume = numScoops * scooper.volume()
        while required_volume > 0:
            carton = Carton.Carton(self.carton_radius, self.carton_height)
            while carton.hasEnoughFor(scooper) and required_volume > 0:
                carton.remove(scooper)
                required_volume -= scooper.volume()
            self.cartons_used += 1

    def cartonsUsed(self):
        ''' cartonsUsed method
        Parameters: none
        Return: the number of cartons used so far in the Shoppe'''
        return self.cartons_used
