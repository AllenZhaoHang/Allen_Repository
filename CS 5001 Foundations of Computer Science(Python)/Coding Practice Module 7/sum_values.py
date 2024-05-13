'''
    Write a recursive function called sum_values
    that takes in a list of integers and an index
    of one element in the list 
    Hang Zhao
    10/19/2023
'''


def sum_values(list_num, index):
    ''' a number list'''
    if index == len(list_num) - 1:
        return list_num[index]
    else:
        return list_num[index] + sum_values(list_num, index + 1)


def main():
    '''main'''
    num_list = [1, 2, 3, 4, 5]
    print(sum_values(num_list, 0))


if __name__ == '__main__':
    main()
