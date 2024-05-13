'''
    Coding Practice Module 5
    takes a string as a parameter
    and returns each letter diagonally on a new line
    Hang Zhao
    10/07/2023
'''


def diagonal_string(string):
    '''
    takes a string as a parameter
    and returns each letter diagonally on a new line
    Input: a string
    Output: None
    '''
    result = ""
    for i, char in enumerate(string):
        spaces = " " * i
        if i == len(string) - 1:
            result += spaces + char
        else:
            result += spaces + char + "\n"
    return result


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    string = input("Enter a word: ")
    print(diagonal_string(string))


if __name__ == "__main__":
    main()
