'''
    Hang Zhao
    09/23/2023
    prints all of the numbers between 1
    and that integer
'''


def count_down(num):
    ''' print number down to 1'''
    count = 1
    while count <= num:
        print(num)
        num -= 1


def main():
    ''' main function '''
    number = int(input("Enter a number: "))
    count_down(number)


if __name__ == "__main__":
    main()
