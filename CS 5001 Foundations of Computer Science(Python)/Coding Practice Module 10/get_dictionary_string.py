'''
    receives a dictionary and returns
    the key-value pairs as a string,
    each pairing on their own line
    Hang Zhao
    11/7/2023
'''


def get_dictionary_string(dictionary):
    '''get_dictionary_string'''
    result_string = ""
    for key, value in dictionary.items():
        result_string += str(key) + " - " + str(value) + "\n"
    return result_string.rstrip("\n")


def main():
    '''main'''
    dict_name = {
        "Maria": "Associate Professor",
        "John": "Clinical Instructor",
        "Carla": "Dean of Khoury"
    }
    print(get_dictionary_string(dict_name))


if __name__ == '__main__':
    main()
