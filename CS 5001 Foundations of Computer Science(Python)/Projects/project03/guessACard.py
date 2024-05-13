'''
    Hang Zhao
    09/21/2023
    guess A Card
'''

# Put any libararies to be imported below
from random import randint
from random import choice
import sys

def getSuit():
    '''  pick a random suit for a card '''
    suit_list = ["Diamonds", "Hearts", "Clubs", "Spades"]
    random_choice = choice(suit_list)
    return random_choice

def getValue():
    ''' will pick a random value for a card  '''
    random_number = randint(1, 13)
    return random_number


def printCard(value, suit):
    ''' print out the value of the card '''
    if value == 1:
        value = 'Ace'
    elif value == 11:
        value = 'Jack'
    elif value == 12:
        value = 'Queen'
    elif value == 13:
        value = 'King'
    message = str(value) + "of" + suit
    print(message)


def main():
    ''' test getValue() and getSuit() function '''
    value = getValue()
    suit = getSuit()
    print(value, suit)
    if len( sys.argv ) > 1:
        color = sys.argv[1]
        if color == 'black' and suit in ("Clubs", "Spades"):
            print("The card is the same color! ")
        elif color == 'red' and suit in ("Diamonds", "Hearts"):
            print("The card is not the same color! ")
        else:
            print("The color you enter is wrong!")


if __name__ == "__main__":
    main()
