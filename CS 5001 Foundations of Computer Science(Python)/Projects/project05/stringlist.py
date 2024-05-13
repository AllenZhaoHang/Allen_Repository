'''
    hang zhao
    10//7/2023
    string
'''

def main():
    '''
    string list
    '''
    # a = 'center'
    # s = a.center(20,"-")
    # print(s)
    grades = [[98, 97 ,96, 95], [99, 98, 93, 95], [99, 100, 98, 97] ,[99, 93, 95,95]]
    row = 0
    while row < len(grades):
        column = 0
        while column < len(grades[row]):
            print(grades[row][column], end="\t")
            column +=1
        print()
        row += 1
    #word = input("Enter your word: ")
    # for s in word:
    #     print(s)
    # index = 0
    # while index < len(word):
    #     print(word[index])
    #     index += 1

if __name__ == "__main__":
    main()
