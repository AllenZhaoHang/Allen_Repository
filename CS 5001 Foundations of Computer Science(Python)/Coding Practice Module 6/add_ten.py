'''
    receives a list of integer values
    and adds 10 to each element in the
    list. The list should then be returned.
    Hang Zhao
    10/13/2023
'''


def add_ten(values):
    '''
    add 10
    '''
    # values = [value + 10 for value in values]
    # print(values)
    for index in range(len(values)):
        values[index] += 10
    return values


def main():
    '''main'''
    num_list = [1, -2, 3, -6, 5, -10, 7, -14, 9, -18]
    num_list = add_ten(num_list)
    print(num_list)


if __name__ == '__main__':
    main()
