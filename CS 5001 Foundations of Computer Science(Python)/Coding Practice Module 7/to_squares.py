'''
    Write a recursive function called
    to_squares that takes in a list of integers
    Hang Zhao
    10/19/2023
'''


def to_squares(num_list, index):
    '''a num list'''
    if index == len(num_list) - 1:
        num_list[index] = num_list[index] ** 2
    else:
        num_list[index] = num_list[index] ** 2
        to_squares(num_list, index + 1)
    return num_list


def main():
    '''main'''
    num_list = [1, 2, 3, 4, 5]
    print(to_squares(num_list, 2))


if __name__ == '__main__':
    main()
