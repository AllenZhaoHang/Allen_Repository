'''
    Write a function called formula
    that returns the result of the following
    mathematical formula. You should write your
    solution recursively.
    Hang Zhao
    10/19/2023
'''


def formula(x):
    ''' '''
    if x == 1:
        return 3
    else:
        return 2 * formula(x - 1) + 5


def main():
    '''main'''
    print(formula(1))
    print(formula(3))


if __name__ == '__main__':
    main()
