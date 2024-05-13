'''
    Hang Zhao
    09/23/2023
    read words and print
'''


def main():
    ''' print words '''
    word = ""
    word_list = []
    while word != 'stop':
        word = input("Enter a word: ")
        if word != 'stop':
            word_list.append(word)
    print(' '.join(word_list))


if __name__ == "__main__":
    main()
