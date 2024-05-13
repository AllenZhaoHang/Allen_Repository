'''
    Project 5
    Spaceman Implementation
    The purpose of this project is to give you
    practice working with lists and strings.
    Specifically, to implement the game Spaceman.
    Hang Zhao
    10/05/2023
'''
from random import randint

def pick_random_word():
    '''Pick_random_word will create a word list, chooose a random
    word and return it
    Input: None
    Output: A random word from the list
    '''
    word_list = ["apple","boston","northeastern","university","portland","maine","harvard",
                "store","macbook","oyster","lobster","shame","study","computer","science",
                "random","string","synthesis","assignment","canvas"]
    index = randint(0, 19)
    return word_list[index]

def create_hidden_word(rand_word):
    '''create_hidden_word will create an obfuscated version of the random word
    Input: The random word
    Output: An obfuscated version of the word (ie banana would return *******
    '''
    length = len(rand_word)
    return '*' * length

def word_found(rand_word, hidden_word):
    '''word_found will detect whether the random word has been uncovered
    Input: the random word and the hidden version of the word
    Output: True if the hidden word has all been revealed, False otherwise
    '''
    return rand_word == hidden_word

def replace_character(rand_word, hidden_word, user_guess):
    '''Replaces all the occurences of user_guess in hidden_word with user_guess
    Input: the random word, the hidden word so far, and the user guess
    Output: the new hidden word
    '''
    new_hidden_word = ""
    for i in range(len(rand_word)):
        if rand_word[i] == user_guess:
            new_hidden_word += user_guess
        else:
            new_hidden_word += hidden_word[i]
    return new_hidden_word

def main():
    '''Main game playing location'''
    max_attempts = 6
    attempt = 0
    rand_word = pick_random_word()
    hidden_word = create_hidden_word(rand_word)
    print("|------------------------------------------------------|")
    print("|           Welcome to Allen's Spaceman Game           |")
    print("|------------------------------------------------------|")
    print("|                      Rules                           |")
    print("|          You are allowed up to 6 wrong guesses       |")
    print("|------------------------------------------------------|")
    print(hidden_word)
    while attempt < max_attempts:
        user_guess = str(input("Enter a letter:").lower())
        lenn = len(user_guess)
        #print(lenn)
        if (lenn != 1) or not user_guess.isalpha():
            print("Pls enter a single letter!")
            continue
        if user_guess in rand_word:
            hidden_word = replace_character(rand_word, hidden_word, user_guess)
            print(hidden_word)
            if word_found(rand_word, hidden_word):
                print("Good job! you guessed the word: " + rand_word)
                break
        else:
            attempt += 1
            print("Incorrect! Try again. Attempt left: ", max_attempts - attempt)
    if attempt == max_attempts:
        print("Sorry, you've run out of attempts. The word was:", rand_word)

if __name__ == "__main__":
    main()
