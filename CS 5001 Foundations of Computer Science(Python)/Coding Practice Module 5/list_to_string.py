'''
    Coding Practice Module 5
    takes a list as a parameter and
    returns a string with each element of the list on its own line
    Hang Zhao
    10/07/2023
'''


def list_to_string(list):
    '''
    takes a list as a parameter and
    returns a string with each element of the list on its own line
    Input: a list
    Output: a list
    '''
    list_new = [str(x) for x in list]
    return_list = "\n".join(list_new)
    return return_list


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    lsit = ['khoury', 'college', 'align', 'masters']
    re_list = list_to_string(lsit)
    print(re_list)


if __name__ == "__main__":
    main()
