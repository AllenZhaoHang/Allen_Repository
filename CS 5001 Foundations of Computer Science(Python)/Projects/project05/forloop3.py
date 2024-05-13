'''
    Make a function that has an integer parameter and
    calculates the factorial of that number (ie 5! is 1*2*3*4*5)
'''

def factorial(num):
    ''''''
    if num == 0:
        return 1
    else:
        s = 1
        for x in range(1,num+1):
            s *= x
        return s
    
def main():
    print(factorial(5))

if __name__ == '__main__':
    main()
