'''
    Write a recursive function called
    find_value that takes a list of strings
    and a target value and returns whether
    the target value is in the list of strings.
    Hang Zhao
    10/19/2023
'''


def find_value(str_list, target):
    '''find value'''
    if not str_list:
        return False  # If the list is empty, the target cannot be found
    if str_list[0] == target:
        return True  # If the first element matches the target, it's found
    return find_value(str_list[1:], target)


def main():
    '''main'''
    str_list = ["apple", "banana", "cherry", "date", "fig"]
    print(find_value(str_list, "no"))


if __name__ == '__main__':
    main()
