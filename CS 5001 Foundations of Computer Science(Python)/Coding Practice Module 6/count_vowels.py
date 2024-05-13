'''
    takes a string as an input and
    returns the number of vowels
    Hang Zhao
    10/13/2023
'''


def count_vowels(string):
    ''' count vowel '''
    count = 0
    strs = "aeiouAEIOU"
    for z in string:
        if z in strs:
            count += 1
    return count


def main():
    ''' main '''
    string = input("Enter a string: ")
    count = count_vowels(string)
    print("The num is: ", count)


if __name__ == '__main__':
    main()
