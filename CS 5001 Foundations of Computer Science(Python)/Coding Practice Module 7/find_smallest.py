'''
    Write a recursive function which, given a list of numbers, finds the smallest number in the list.
    Hang Zhao
    10/21/2023
'''


def find_smallest(lst):
    ''' find the smallest number in a list '''
    if len(lst) == 1:
        return lst[0]
    remain_lst = find_smallest(lst[1:])
    if lst[0] > remain_lst:
        return remain_lst
    else:
        return lst[0]


def main():
    '''main'''
    lst = [2, 3, 4, -1, -21]
    print(find_smallest(lst))


if __name__ == '__main__':
    main()
