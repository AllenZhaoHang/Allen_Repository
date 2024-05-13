'''
    Hang Zhao
    9/19/2023
    return true or false whether or
    not the parameter is an even number.
'''

def is_even(num):
    # if num is an even number return true
    return num % 2 == 0

def main():
    str = input()
    print(is_even(str))


if __name__ == "__main__":
    main()