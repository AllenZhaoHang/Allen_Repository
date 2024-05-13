'''
    receives two rosters. The first roster
    represents the students who have successfully
    completed CS 5001 and the second roster represents
    the students who have successfully completed CS 5002.
    Hang Zhao
    11/7/2023
'''


def completed(roster_5001, roster_5002):
    if type(roster_5001) is list or type(roster_5002) is list:
        raise AttributeError("roster_5001 and roster_5002 must be sets")
    return list(roster_5001.intersection(roster_5002))
