'''
    receives two rosters. The first roster
    represents the students who have successfully
    completed CS 5001 and the second roster represents
    the students who have successfully completed CS 5002.
    The function should return a list of students who have
    completed either CS 5001, or CS 5002, or both.
    Hang Zhao
    11/7/2023
'''


def either(roster_5001, roster_5002):
    '''either 5001 or 5002 or both'''
    return list(roster_5001.union(roster_5002))
    # cs5001_set = set(roster_5001)
    # cs5002_set = set(roster_5002)
    # try:
    #     either_set = cs5001_set | cs5002_set
    #     return list(either_set)
    # except AttributeError as e:
    #     print(f"There is a AttributeErro{e}")
