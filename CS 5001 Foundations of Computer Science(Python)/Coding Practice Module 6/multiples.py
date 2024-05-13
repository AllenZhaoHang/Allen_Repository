'''
    uses a for loop to print the multiples
    of 5 that are less than or equal to the number that was entered.
    Hang Zhao
    10/13/2023
'''


def mutipleFive(number):
    ''' function '''
    for i in range(5, number + 1, 5):
        print(i)


def main():
    '''main'''
    num = int(input("Enter a positive integer: "))
    mutipleFive(num)


if __name__ == '__main__':
    main()
