'''
    creates and returns a dictionary 
    Hang Zhao
    11/7/2023
'''


def initialize():
    ''' function initialize '''
    dict_name = {
        "Maria": "Associate Professor",
        "John": "Clinical Instructor",
        "Carla": "Dean of Khoury"
    }
    return dict_name


def main():
    '''main'''
    result = initialize()
    for s, k in result.items():
        print(s, ":", k)


if __name__ == '__main__':
    main()
