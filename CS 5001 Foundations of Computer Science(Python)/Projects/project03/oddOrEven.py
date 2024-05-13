'''
    Hang Zhao
    09/21/2023
'''
import sys

# calculate whether a number is odd or even
def oddOrEven(number):
    print('determining if ' + str(number) + ' is odd or even:')

    # if statement
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")


def main():
    my_number = 10
    # assign values to variables
    print(sys.argv)
    # check for user input
    if len( sys.argv ) > 1:
    # re-assign the value if the user provided one
        my_number = int(sys.argv[1])
    # call the function
    oddOrEven(my_number)

if __name__ == "__main__":
    main()
