'''
    receives two rosters. The first roster
    represents the students who have successfully
    completed CS 5001 and the second roster represents
    the students who have successfully completed CS 5002.
    The function should return a list of students who have
    completed CS 5001 but still need to take CS 5002.
    Hang Zhao
    11/7/2023
'''


def needs_5002(roster_5001, roster_5002):
    cs_set = roster_5001.intersection(roster_5002)
    return list(roster_5001 - cs_set)
