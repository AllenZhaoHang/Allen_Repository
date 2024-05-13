'''
    Write a recursive function called
    factorial that takes in a positive
    number (> 0) and returns its factorial.
    Hang Zhao
    10/19/2023
'''


def factorial(n):
    ''' factorial '''
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


def main():
    '''main'''
    print(factorial(1))
    print(factorial(5))


if __name__ == '__main__':
    main()
