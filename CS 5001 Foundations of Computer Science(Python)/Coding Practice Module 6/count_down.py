'''
    uses a for loop to print the count
    down from 100 to 0 (inclusive) by 5s
    Hang Zhao
    10/13/2023
'''


def count_down():
    '''count down function '''
    for i in range(100, -1, -5):
        if i == 0:
            print("Blastoff!")
        else:
            print(i)


def main():
    '''main function'''
    count_down()


if __name__ == '__main__':
    main()
