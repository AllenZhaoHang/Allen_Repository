'''
   Write a recursive function called find_max
   that takes in a list of integers and returns
   the maximum value from that list. 
    Hang Zhao
    10/19/2023
'''


def find_max(num_list):
    '''find'''
    def find_max_recursive(index):
        if index == len(num_list) - 1:
            return num_list[index]
        else:
            max_from_rest = find_max_recursive(index + 1)
            if num_list[index] > max_from_rest:
                return num_list[index]
            else:
                return max_from_rest

    if not num_list:
        return None  # Return None for an empty list

    return find_max_recursive(0)


def main():
    '''main'''
    my_list = [3, 7, 2, 12, 4, 5, 1]
    print(find_max(my_list))


if __name__ == '__main__':
    main()
