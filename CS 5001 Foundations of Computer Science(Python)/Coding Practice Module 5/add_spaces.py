'''
    Coding Practice Module 5
    takes a string as input and uses a 
    loop to print each character of the string 
    on the same line with 3 spaces between each letter
    Hang Zhao
    10/07/2023
'''


def add_spaces(string):
    '''
    add spaces
    Input: a string
    Output: None
    '''
    result = ""
    for s in string:
        result += s + "   "
    return result.strip()


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    string = input("Enter a string: ")
    print(add_spaces(string))


if __name__ == "__main__":
    main()
