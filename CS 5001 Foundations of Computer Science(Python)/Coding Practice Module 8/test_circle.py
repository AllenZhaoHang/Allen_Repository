'''
    Test Circle
    Hang Zhao
    10/22/2023
'''
from circle import Circle
import unittest

class TestCircle(unittest.TestCase):
    '''test class'''
    def test_get_area(self):
        '''get area'''
        circle = Circle('2', '3', '5')
        self.assertAlmostEqual(circle.get_area(),78.53981633974483)

    def test_distance(self):
        '''distance'''
        circle = Circle('2', '3', '5')
        self.assertAlmostEqual(circle.get_distance(1, 1), 2.23606797749979)

if __name__ == '__main__':
    unittest.main()
