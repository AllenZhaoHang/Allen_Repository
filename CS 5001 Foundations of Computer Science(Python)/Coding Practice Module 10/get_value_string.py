'''
    receives a dictionary and returns
    the values of the dictionary as a string
    with each key on its own line.
    Hang Zhao
    11/7/2023
'''


def get_value_string(dictionary):
    '''get_value_string'''
    value_string = ""
    for values in dictionary.values():
        value_string += str(values) + "\n"
    return value_string.rstrip("\n")


def main():
    '''main'''
    dict_name = {
        "Maria": "Associate Professor",
        "John": "Clinical Instructor",
        "Carla": "Dean of Khoury"
    }
    print(get_value_string(dict_name))


if __name__ == '__main__':
    main()
