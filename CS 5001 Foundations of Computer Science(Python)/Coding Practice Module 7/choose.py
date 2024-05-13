'''
    Write a recursive function called
    choose that computes the number of
    combinations possible given k and n
    (in that order) where n ≥ k ≥ 0.
    Hang Zhao
    10/19/2023
'''


def choose(k, n):
    ''' choose recursion '''
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0

    # Recursive case: use the recursive formula
    return choose(k - 1, n - 1) + choose(k, n - 1)


def main():
    '''main function'''
    print(choose(2, 6))


if __name__ == '__main__':
    main()
