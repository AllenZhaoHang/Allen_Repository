'''
    sales
    Hang Zhao
    10/31/2023
'''


def salaryCaculate(base=200, commission=0.08):
    '''
    tips
    '''
    total = 0
    more = input("Are there more sales to enter?(Y/N)")
    more = more.upper()
    while more != "N":
        try:
            sales = float(input("Enter your sales: "))
        except TypeError as ex:
            print("Invalid Type, pls input a float number.", ex)
            sales = 0
            while sales <= 0.0:
                print("Your sales should above zero.")
                try:
                    sales = float(input("Enter your sales:"))
                except TypeError as ex:
                    print("Invalid Type, pls input a float number.", ex)
                    sales = 0
            total += sales
            more = input("Are there more sales to enter?(Y/N)")
            more = more.upper()
        except ValueError as ex:
            print("Invalid Value", ex)
    return base + total * commission


def main():
    '''main function'''
    print(salaryCaculate())


if __name__ == '__main__':
    main()
