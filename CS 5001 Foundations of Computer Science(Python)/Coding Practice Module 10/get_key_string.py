'''
    receives a dictionary and returns
    the keys of the dictionary as a string
    with each key on its own line.
    Hang Zhao
    11/7/2023
'''


def get_key_string(dictionary):
    '''get_key_string'''
    key_string = ""
    for key in dictionary.keys():
        key_string += str(key) + "\n"
    return key_string.rstrip("\n")


def main():
    '''main'''
    dict_name = {
        "Maria": "Associate Professor",
        "John": "Clinical Instructor",
        "Carla": "Dean of Khoury"
    }
    print(get_key_string(dict_name))


if __name__ == '__main__':
    main()
