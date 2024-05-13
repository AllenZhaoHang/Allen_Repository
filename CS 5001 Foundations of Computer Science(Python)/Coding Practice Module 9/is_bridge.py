'''
    Function: is_bridge
    Tests whether course is part of the bridge
    Parameters:
    course. a number of a course (without the CS)
    Returns True if the course number is 5001, 5002,
    5003, 5004, 5005, 5008, or 5009
    or False otherwise
    Raises TypeError if the value of the course is not an integer
    Hang Zhao
    10/29/2023
'''


def is_bridge(course):
    '''
    Tests whether course is part of the bridge
    Parameters:
    course. a number of a course (without the CS)
    Returns True if the course number is 5001, 5002,
    5003,5004, 5005, 5008, or 5009
    or False otherwise
    Raises TypeError if the value of the course is not an integer
    '''
    if not isinstance(course, int):
        raise TypeError("course should be an integer.")
    if course <= 0:
        raise ValueError("course should be more than zero.")
    return course in [5001, 5002, 5003, 5004, 5005, 5008, 5009]


def main():
    '''main funciont'''
    print(is_bridge(5008))
    # print(is_bridge("a"))
    print(is_bridge(4006))


if __name__ == '__main__':
    main()
