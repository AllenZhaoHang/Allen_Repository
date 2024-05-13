'''
    Hang Zhao
    09/23/2023
    print even nums between 2 and 200
'''


def print_evens():
    ''' print even nums between 2 and 200 '''
    minnumber = 1
    while minnumber < 201:
        if minnumber % 2 == 0:
            print(minnumber)
        minnumber += 1


def main():
    ''' main function '''
    print_evens()


if __name__ == "__main__":
    main()
