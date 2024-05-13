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
    print(str(value) + " of " + suit)

def main():
    value = 1
    suit = "Diamonds"
    printCard(1, suit)


if __name__ == "__main__":
    main()

