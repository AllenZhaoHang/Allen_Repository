from pyrep.robots.mobiles.drone_base import DroneBase
from pyrep.backend import vrep

class Quadricopter(DroneBase):
    def __init__(self, count: int = 0, distance_from_target: float = 0):
        super().__init__(
            count, 4, distance_from_target, 'Quadricopter')

            