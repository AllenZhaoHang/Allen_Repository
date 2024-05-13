'''
    Coding Practice Module 5
    takes a tuple as a parameter and
    returns a list that contains all of
    the same elements in the same order
    Hang Zhao
    10/07/2023
'''


def name_number(name):
    '''
    return the Number of a name
    Input: a name
    Output: a number
    '''
    name = name.lower()
    name_list = list(name)
    summ = 0
    for i in name_list:
        summ += ord(i) - 96
    return summ


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    name = input("Enter your name: ")
    print(name_number(name))


if __name__ == "__main__":
    main()
