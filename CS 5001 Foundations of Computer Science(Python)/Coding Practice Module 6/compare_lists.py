'''
     receives two lists of integer values.
     The function should return true if all
     of the elements in the first list are
     contained in the second list 
    Hang Zhao
    10/13/2023
'''


def compare_lists(list_a, list_b):
    '''compare lists'''
    return all(x in list_b for x in list_a)


def main():
    '''main'''
    list1 = [1, 2, 3]
    list2 = [3, 1, 2, 4, 5]
    print(compare_lists(list1, list2))


if __name__ == '__main__':
    main()
