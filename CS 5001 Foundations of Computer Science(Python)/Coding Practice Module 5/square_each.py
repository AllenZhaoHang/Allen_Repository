'''
    Coding Practice Module 5
    receives a list as a parameter and
    returns the same list that has been
    modified so that all the elements are squared
    Hang Zhao
    10/07/2023
'''


def square_each(list):
    '''
    receives a list as a parameter and
    returns the same list that has been
    modified so that all the elements are squared
    Input: 
    Output: 
    '''
    lists = []
    for s in list:
        lists.append(s ** 2)
    return lists


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    ori_list = [1, 2, 3]
    res_list = square_each(ori_list)
    print(res_list)


if __name__ == "__main__":
    main()
