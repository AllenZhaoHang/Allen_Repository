'''
    Hang Zhao
    09/23/2023
    prints all of the numbers between 1
    and that integer
'''


def count_up(num):
    ''' print numbers from low to high'''
    count = 1
    while count <= num:
        print(count)
        count += 1


def main():
    ''' main function '''
    number = int(input("Enter a positive number: "))
    count_up(number)


if __name__ == "__main__":
    main()
