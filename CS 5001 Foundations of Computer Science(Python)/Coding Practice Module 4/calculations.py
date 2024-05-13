'''
    Hang Zhao
    09/23/2023
    Calculations
'''


def main():
    ''' Calculations '''
    num = int(input("Enter the number of values to read: "))
    total = 0
    average = 0
    if num > 0:
        count = 0
        while count < num:
            value = int(input("Enter an integer:"))
            total += value
            count += 1
        average = total / num
    print("The sum is", total)
    print("The average is", average)


if __name__ == "__main__":
    main()
