'''
    Write a recursive function called upper_triangle
    that takes in a number greater than or equal to
    3 and prints an upper left triangle of that size
    Hang Zhao
    10/19/2023
'''


def upper_triangle(n):
    ''' n >= 3'''
    if n == 1:
        print("*")
    elif n == 2:
        print("**")
        print("*")
    elif n == 3:
        print("***")
        print("**")
        print("*")
    else:
        print(n * "*")
        upper_triangle(n - 1)


def main():
    '''main'''
    upper_triangle(1)


if __name__ == '__main__':
    main()
