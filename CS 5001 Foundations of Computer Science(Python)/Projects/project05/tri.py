'''
'''

def main():
    '''
    '''
    # for s in range(1,10):
    #     print(s * '*', end = " " )
    #     print()
    start =10
    while start>0:
        print(" "*(10-start)+'*'*start)
        start-=1

if __name__ == '__main__':
    main()
