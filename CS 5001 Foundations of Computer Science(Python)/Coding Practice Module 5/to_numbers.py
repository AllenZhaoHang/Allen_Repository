'''
    Coding Practice Module 5
    receives a list of string values each
    of which represents a number and returns a list of floats.
    Hang Zhao
    10/07/2023
'''


def to_numbers(str_list):
    '''
    receives a list of string values each
    of which represents a number and returns a list of floats.
    Input: a list
    Output: a list
    '''
    res_list = []
    for s in str_list:
        res_list.append(float(s))
    return res_list


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    ori_list = ['1', '2', '3', '4']
    res_list = to_numbers(ori_list)
    print(res_list)


if __name__ == "__main__":
    main()
