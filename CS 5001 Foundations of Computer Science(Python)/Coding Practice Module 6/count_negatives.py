'''
    receives a list of integer values
    and returns how many of the values
    in the list are negative.
    Hang Zhao
    10/13/2023
'''


def count_negatives(num_list):
    ''' count '''
    count = 0
    for num in num_list:
        if int(num) < 0:
            count += 1
    return count


def main():
    '''main'''
    num_list = input("Enter a num list: ")
    inter_list = [int(num) for num in num_list.split()]
    count = count_negatives(inter_list)
    print("count is: ", count)


if __name__ == '__main__':
    main()
