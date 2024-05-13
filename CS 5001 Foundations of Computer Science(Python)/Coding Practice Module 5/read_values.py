'''
    Coding Practice Module 5
    returns a list of positive integer values
    that are read from the keyboard one at a time.
    Hang Zhao
    10/07/2023
'''


def read_values():
    '''
    returns a list of positive integer values
    that are read from the keyboard one at a time.
    Input: None
    Output: a list
    '''
    num = int(input("Enter a number: "))
    listt = []
    while num > 0:
        listt.append(num)
        num = int(input("Enter a number: "))
    return listt


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    print(read_values())


if __name__ == "__main__":
    main()
