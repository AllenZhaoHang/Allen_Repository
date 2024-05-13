'''
    Function: validation
    perform multiplication with different types
    Parameters:
    one. an negative integer value
    two. a positive floating point number less than 1000
    Returns the product of the two parameter values
    Hang Zhao
    10/29/2023
'''


def validation(one, two):
    '''
    Function: validation
    perform multiplication with different types
    Parameters:
    one. an negative integer value
    two. a positive floating point number less than 1000
    Returns the product of the two parameter values
    '''
    if not isinstance(one, int):
        raise TypeError("one must be a integer.")
    if one >= 0:
        raise ValueError("one must be an negative value.")
    if not isinstance(two, float):
        raise TypeError("two must be a float.")
    if two <= 0:
        raise ValueError("two must be a positive value.")
    if two >= 1000:
        raise ValueError("two must less than 1000.")
    return one * two


def main():
    '''main function'''
    num1 = int(input("num1: "))
    num2 = float(input("num2: "))
    res = validation(num1, num2)
    print(res)


if __name__ == '__main__':
    main()
