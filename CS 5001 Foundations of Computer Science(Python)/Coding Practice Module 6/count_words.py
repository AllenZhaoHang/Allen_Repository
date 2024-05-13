'''
    Write a program that reads in a
    sentence from the keyboard and
    prints each word on it's own line
    Hang Zhao
    10/13/2023
'''


def count_words(sentence):
    '''print'''
    words = sentence.split()
    for index, word in enumerate(words):
        print(f"{index}. {word}")


def main():
    '''main'''
    stringwords = input("Enter a sentence: ")
    count_words(stringwords)


if __name__ == '__main__':
    main()
