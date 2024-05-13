"""
    HANG ZHAO
    09/17/2023
    Write a program that prompts with "Enter value: "
    and reads in an integer value from the keyboard and
    prints the appropriate message depending upon the value
    of that input according to the following table:
    Even or odd	Value	Message
    Even	negative	"even negative number"
    Even (and 0)	positive	"even positive number"
    Odd	negative	"odd negative number"
    Odd	positive	"odd positive number"
"""
# reads in an integer value from the keyboard and
# prints the appropriate message


def main():
    value = int(input("Enter value: "))
    if value % 2 == 0:
        if value > 0:
            print("even positive number")
        elif value < 0:
            print("even negative number")
        else:
            print("even positive number")
    else:
        if value > 0:
            print("odd positive number")
        else:
            print("odd negative number")


if __name__ == "__main__":
    main()
