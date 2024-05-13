'''
    functions
    Hang Zhao
    10/24/2023
'''


def equation(x, y):
    ''' equation function '''
    while True:
        x = int(input("Enter the value of x: "))
        y = int(input("Enter the value of y: "))

        # Validate the input
        if y == 2 * x + 3:
            print("Input is correct. It satisfies the equation.")
        else:
            print("Input is incorrect. It does not satisfy the equation.")
        break

def main():
    '''main function'''
    print("Correct Input: ")
    equation(1, 5)
    print("Incorrect Input: ")
    equation(2, 4)
if __name__ == '__main__':
    main()
