'''
    Hang Zhao
    09/23/2023
    debug
'''


def main():
    '''' main function '''
    hi = int(input("Enter larger: "))
    lo = hi
    while lo >= hi:
        lo = int(input("Enter smaller: "))
    while lo <= hi:
        print(hi)
        hi -= 1


if __name__ == "__main__":
    main()
