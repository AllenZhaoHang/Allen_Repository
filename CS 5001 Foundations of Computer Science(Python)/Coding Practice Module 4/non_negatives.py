'''
    Hang Zhao
    09/23/2023
    print non-negative value
    stop negative value
'''


def main():
    ''' print value from keyboard '''
    while True:
        value = int(input("Enter an integer: "))
        if value < 0:
            break
        else:
            print(value)


if __name__ == "__main__":
    main()
