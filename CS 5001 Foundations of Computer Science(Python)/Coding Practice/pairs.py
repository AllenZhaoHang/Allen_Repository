"""
    HANG ZHAO
    09/17/2023
    reads four integers from the keyboard and prints 
    "two pairs" if the input consists of two matching
    pairs (in some order) and "not two pairs" otherwise.
"""
# reads four integers from the keyboard and prints "two pairs"
# if the input consists of two matching pairs (in some order)
# and "not two pairs" otherwise.


def main():
    num = input("Enter a 4-digit number: ")
    if num[0] == num[-1] and num[1] == num[2]:
        print("two pairs")
    else:
        print("not two pairs")


if __name__ == "__main__":
    main()
