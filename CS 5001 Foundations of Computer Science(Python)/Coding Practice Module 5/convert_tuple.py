'''
    Coding Practice Module 5
    takes a tuple as a parameter and
    returns a list that contains all of
    the same elements in the same order
    Hang Zhao
    10/07/2023
'''


def convert_tuple(tuple):
    '''
    takes a tuple as a parameter and
    returns a list that contains all of
    the same elements in the same order
    Input: a tuple
    Output: a list
    '''
    list = []
    for s in tuple:
        list.append(s)
    return list


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    tuplee = ('khoury', 'college', 'master')
    listt = convert_tuple(tuplee)
    print(listt)


if __name__ == "__main__":
    main()

