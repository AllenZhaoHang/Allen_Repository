'''
    Test Point class
    Hang Zhao
    10/22/2023
'''
from point import Point
import unittest


class test_point(unittest.TestCase):
    def test_distance(self):
        point1 = Point(4, 5, 6)
        point2 = Point(1,2,3)
        distance = point1.get_distance(point2)
        self.assertAlmostEqual(distance, 5.196152422706632)


if __name__ == '__main__':
    unittest.main()
