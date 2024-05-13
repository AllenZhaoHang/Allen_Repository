'''
    Hang Zhao
    09/23/2023
    multiple of the integer value
'''


def main():
    ''' main function '''
    while True:
        number = int(input("Enter a non-zero integer: "))
        if number == 0:
            print("Should enter a non-zero integer:")
            continue
        multiple = int(input("Enter multiple: "))
        while True:
            if multiple % number != 0:
                multiple = int(input("Try again: "))
            else:
                break
        break


if __name__ == "__main__":
    main()
