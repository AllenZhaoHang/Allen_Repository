'''
    Write a recursive function called lower_triangle
    that takes in a number greater than or equal to 3
    and prints an lower left triangle of that size
    Hang Zhao
    10/19/2023
'''


def lower_triangle(n):
    '''lower triangle'''
    if n == 1:
        print("*")
    elif n == 2:
        print("*")
        print("**")
    elif n == 3:
        print("*")
        print("**")
        print("***")
    else:
        lower_triangle(n - 1)
        print(n * "*")


def main():
    '''main'''
    lower_triangle(5)


if __name__ == '__main__':
    main()
