'''
    Make a function that asks the
    user for a number and then prints
    out the sum of the numbers from 1 to
    that number using a for loop
'''

def main():
    ''''''
    num = int(input("Enter a number: "))
    s = 0
    for x in range(num+1):
        s += x
    print(s)


if __name__ == '__main__':
    main()
