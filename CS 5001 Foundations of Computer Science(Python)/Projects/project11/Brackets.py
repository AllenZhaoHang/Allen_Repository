'''
    Brackets
    Hang Zhao
    11/16/2023
'''
from Stack import Stack


class Brackets:
    ''' brackets class'''

    def __init__(self):
        ''' Constructor
        Parameters:
           self -- the current object
        '''
        pass

    def is_valid_brackets(self, string):
        ''' is_valid_brackets -- returns True if the brackets in the
        string are valid, False otherwise
        '''
        stack = Stack()
        opening_brackets = ['(', '{', '[', '<']
        closing_brackets = [')', '}', ']', '>']
        bracket_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}

        for char in string:
            if char in opening_brackets:
                stack.push(char)
            elif char in closing_brackets:
                if len(stack) == 0:
                    return False
                last_opening_bracket = stack.pop()
                if bracket_pairs[last_opening_bracket] != char:
                    return False

        if len(stack) == 0:
            value = True
        else:
            value = False

        if len(string) != 0 and string[0] in opening_brackets:
            value2 = True
        else:
            value2 = False

        return value and value2


def main():
    ''' main function'''
    user_input = input(
        "Enter a string, should consists of a valid set of brackets,Valid bracket options include: (), {}, [], <>: ")
    brackets = Brackets()
    if brackets.is_valid_brackets(user_input):
        print("Valid!")
    else:
        print("Invalid!")


if __name__ == '__main__':
    main()
