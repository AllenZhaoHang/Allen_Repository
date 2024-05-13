"""
    HANG ZHAO
    09/17/2023
    reads a 4-digit number from the keyboard and prints
    the first and last digits of the number.
"""
# reads a 4-digit number from the keyboard and prints the first
# and last digits of the number.


def main():
    num = input("Enter number: ")
    first_num = num[0]
    last_num = num[-1]
    print("The first number is " + first_num)
    print("The last number is " + last_num)


if __name__ == "__main__":
    main()
