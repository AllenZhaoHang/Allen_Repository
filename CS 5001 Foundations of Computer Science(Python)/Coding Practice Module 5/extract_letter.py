'''
    Coding Practice Module 5
    returns the correct letter in a word. 
    It should take two parameters, the 
    word and the index of the letter to return
    Hang Zhao
    10/07/2023
'''


def extract_letter(str, index):
    '''
    returns the correct letter in a word
    Input: a string and the index
    Output: the correct letter
    '''
    return str[index]


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    strr = input("Enter a string: ")
    while True:
        index = int(input("Enter the index of the word: "))
        if index >= 0 and index < len(strr):
            result = extract_letter(strr, index)
            print(result)
        else:
            print("Index input error.")
            continue


if __name__ == "__main__":
    main()
