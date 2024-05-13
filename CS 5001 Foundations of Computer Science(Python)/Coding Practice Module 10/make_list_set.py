'''
    takes a list and converts it into a set then returns the set.
    Hang Zhao
    11/7/2023
'''


def make_list_set(a_list):
    '''make_list_set'''
    a_set = set()
    for i in a_list:
        a_set.add(i)
    return a_set


def main():
    '''main'''
    num_list = {1, 2, 3, 4, 4, 4, 6, 7, 8, 9}
    res_set = make_list_set(num_list)
    print(res_set)


if __name__ == '__main__':
    main()
