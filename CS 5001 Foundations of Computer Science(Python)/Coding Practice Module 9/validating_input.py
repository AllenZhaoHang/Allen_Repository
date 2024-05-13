'''
    Write a program that reads in two
    integer values from the keyboard,
    one positive and one negative, and
    prints them as an ordered pair. 
'''


def main():
    '''main function'''
    positive_value = None
    negative_value = None

    while positive_value is None:
        try:
            value = int(input("Enter value: "))
            if value == 0:
                print("Value should be either negative or positive")
                continue
            if value > 0:
                positive_value = value
            elif value < 0 and negative_value is None:
                negative_value = value
            else:
                print("Value should be positive")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    while negative_value is None:
        try:
            value = int(input("Enter value: "))
            if value == 0:
                print("Value should be either negative or positive")
                continue
            if value < 0:
                negative_value = value
            elif value > 0:
                # positive_value = value
                print("Value should be negative")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Pair: ({}, {})".format(negative_value, positive_value))


if __name__ == "__main__":
    main()
