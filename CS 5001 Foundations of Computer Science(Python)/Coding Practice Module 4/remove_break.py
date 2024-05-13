'''
    Hang Zhao
    09/23/2023
    remove break
'''


def main():
    ''' main '''
    a = 0
    b = 1
    c = a + b
    print("0\n1")
    while c <= 1000:
        c = a + b
        print(c)
        a = b
        b = c


if __name__ == "__main__":
    main()
