'''
    receives a list of integer values
    and calculates the average of the
    values in the list.
    Hang Zhao
    10/13/2023
'''


def calculate_average(values):
    ''' function '''
    if not values:
        return 0
    total = sum(values)
    average = total / len(values)
    return average


def main():
    ''' main '''
    num_list = list(input("Enter a list of inter numbers: "))
    aver = calculate_average(num_list)
    print(aver)


if __name__ == '__main__':
    main()
