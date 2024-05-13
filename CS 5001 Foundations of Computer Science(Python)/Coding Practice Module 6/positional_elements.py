'''
    returns how many elements in
    the argument list have a value
    that is equal to the index of that element
    Hang Zhao
    10/13/2023
'''


def positional_elements(num_list):
    '''positon'''
    count = 0
    for i in range(len(num_list)):
        if i == num_list[i]:
            count += 1
    return count


def main():
    '''main'''
    num_list = [0, 1, 2, 4]
    count = positional_elements(num_list)
    print(count)


if __name__ == '__main__':
    main()
