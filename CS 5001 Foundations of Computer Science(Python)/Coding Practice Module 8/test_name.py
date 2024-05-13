'''
    test Name class
    Hang Zhao
    10/22/2023
'''
from name import Name
import unittest


class TestName(unittest.TestCase):
    ''' test name class '''

    def test_get_first_name(self):
        '''' constructor '''
        person = Name("Joe", "Biden")
        self.assertEqual(person.get_first_name(), "Joe")

    def test_get_last_name(self):
        ''' test '''
        person = Name("Joe", "Biden")
        self.assertEqual(person.get_last_name(), "Biden")

    def test_get_full_name(self):
        ''' test '''
        person = Name("Joe", "Biden")
        self.assertEqual(person.get_full_name(), "JoeBiden")

    def test_set_nick_name(self):
        ''' test '''
        person = Name("Joe", "Biden")
        person.set_nick_name("Bit")
        self.assertEqual(person.get_nick_name(), "Bit")


if __name__ == '__main__':
    unittest.main()
