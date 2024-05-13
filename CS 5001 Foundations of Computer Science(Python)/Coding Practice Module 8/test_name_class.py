import unittest
from name import Name

class TestNameClass(unittest.TestCase):
    def test_get_first_name(self):
        person = Name(5, 6)
        self.assertEqual(person.get_first_name(), 5)

    def test_get_full_name(self):
        person = Name("John", "Doe")
        self.assertEqual(person.get_full_name(), "John Doe")

    def test_get_nick_name(self):
        person = Name("John", "Doe")
        self.assertEqual(person.get_nick_name(), "John")

    def test_set_nickname(self):
        person = Name("John", "Doe")
        person.set_nick_name("Johnny")
        self.assertEqual(person.get_nick_name(), "Johnny")

if __name__ == '__main__':
    unittest.main()