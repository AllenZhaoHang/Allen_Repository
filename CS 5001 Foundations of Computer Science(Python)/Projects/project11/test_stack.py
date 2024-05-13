'''
    test stack class and methods
    Hang Zhao
    11/16/2023
'''
from stack import Stack


class TestStack:
    '''test stack class'''
    def test_is_valid_brackets(self):
        ''' test is_valid_brackets'''
        stack = Stack()

        # Test valid strings
        assert stack.is_valid_brackets("") is True  # Empty string
        assert stack.is_valid_brackets("()") is True
        assert stack.is_valid_brackets("{}") is True
        assert stack.is_valid_brackets("[]") is True
        assert stack.is_valid_brackets("<>") is True
        assert stack.is_valid_brackets(
            "({[]})") is True  # Valid nested brackets

        # Test invalid strings
        assert stack.is_valid_brackets("(}") is False
        assert stack.is_valid_brackets(")(") is False
        assert stack.is_valid_brackets(">>") is False
        assert stack.is_valid_brackets("[)") is False
        assert stack.is_valid_brackets("jkll") is False

    def run_tests(self):
        ''' run all tests'''
        self.test_is_valid_brackets()
        print("All tests passed!")


if __name__ == "__main__":
    test_stack = TestStack()
    test_stack.run_tests()
