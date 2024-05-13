'''
    pizza version 5
    Hang Zhao
    10/28/2023
'''


def get_slices(pies, folks):
    ''' caculate slices '''
    if not isinstance(pies, int):
        raise TypeError("pies should be int")
    if pies < 0:
        raise ValueError("pies should > 0")
    if not isinstance(folks, int):
        raise TypeError("folks shoud be int")
    if folks <= 0:
        raise ValueError("folks shoud > 0")
    slices = pies * 8 // folks
    return slices


def main():
    '''main function'''
    try:
        pizzas = int(input("How many pizzas did you order? "))
        people = int(input("How many people do you have? "))
        slices = get_slices(pizzas, people)
        print(pizzas, "pizzas split", people, " ways is ", slices, "")
    except TypeError as ex:
        print("Invalid type", ex)
    except ValueError as ex:
        print("Invalid value", ex)
    print("Done")


if __name__ == '__main__':
    main()
