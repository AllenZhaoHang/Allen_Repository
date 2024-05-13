"""
    HANG ZHAO
    09/17/2023
    reads in a number from the keyboard. Your program
    should ensure that the value entered is between 1
    nd 100 by clamping it and then print it to the screen.
"""
#  reads in a number from the keyboard.


def main():
    num = int(input("Enter value: "))
    if num > 100:
        print("Too big, clamping required")
        print("Value is 100")
    elif num < 1:
        print("Too small, clamping required")
        print("Value is 1")
    else:
        print("Value is " + str(num))


if __name__ == "__main__":
    main()
