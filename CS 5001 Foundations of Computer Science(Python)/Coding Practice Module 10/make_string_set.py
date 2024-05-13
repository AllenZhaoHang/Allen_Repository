'''
    takes in a string of student
    names separated by commas and converts
    that into a set of student names that is returned.
    Hang Zhao
    11/7/2023
'''


def make_string_set(name_string):
    if name_string == '':
        return set()
    name_list = name_string.split(", ")
    name_set = set(name_list)
    new_set = {item for item in name_set if item != ''}
    return new_set
