'''
    Hang Zhao
    09/22/2023
    test loop
'''

def choose_menu():
    print(" L----Login: \n"
    " R----Register: \n"
    "Q----Quit\n")
    choice = input("Enter your choice: ")
    return choice


def main():
    while 1:
        option = choose_menu()
        if option == "Q":
            break
    print("Thanks for using our website! ")

if __name__ == "__main__":
    main()
