'''
    Teset the Brackets.py and Stack.py
    Hang Zhao
    11/16/2023
'''
from Brackets import Brackets


class TestBrackets:
    '''test brackets class'''

    def test_is_valid_brackets(self):
        ''' test is_valid_brackets'''
        brackets = Brackets()

        # Test valid strings
        assert brackets.is_valid_brackets("()") is True
        assert brackets.is_valid_brackets("{}") is True
        assert brackets.is_valid_brackets("[]") is True
        assert brackets.is_valid_brackets("<>") is True
        assert brackets.is_valid_brackets("{jkll}") is True
        assert brackets.is_valid_brackets("[jkll]") is True
        assert brackets.is_valid_brackets(
            "({[]})") is True  # Valid nested brackets

        # Test invalid strings
        assert brackets.is_valid_brackets("") is False  # Empty string
        assert brackets.is_valid_brackets("(}") is False
        assert brackets.is_valid_brackets(")(") is False
        assert brackets.is_valid_brackets(">>") is False
        assert brackets.is_valid_brackets("[)") is False
        assert brackets.is_valid_brackets("jkll") is False
        assert brackets.is_valid_brackets("{jkll") is False

    def run_tests(self):
        ''' run all tests'''
        self.test_is_valid_brackets()
        print("All tests passed!")


if __name__ == "__main__":
    testBracketsstack = TestBrackets()
    testBracketsstack.run_tests()
