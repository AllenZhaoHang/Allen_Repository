'''
    receives a list of integer values
    and returns a new list that contains
    only the even elements of the argument.
    Hang Zhao
    10/13/2023
'''


def filter_evens(num_list):
    '''fliter'''
    new_list = []
    for x in num_list:
        if x % 2 == 0:
            new_list.append(x)
    return new_list


def main():
    '''main'''
    num_list = [2, 3, 4, 5, 6, 7, 8]
    new_list = filter_evens(num_list)
    print(new_list)


if __name__ == '__main__':
    main()
