'''
    Hang Zhao
    09/23/2023
    menu
'''


def main():
    ''' print menu '''
    show_up_menu = ""
    while True:
        print('0 -- Quit')
        print('1 -- Add "O"')
        print('2 -- Add "oo"')
        print('3 -- Add "xXx"')

        option = input("Option: ")

        if option == "0":
            print("Result:", show_up_menu)
            return show_up_menu
        elif option == "1":
            show_up_menu += "O"
        elif option == "2":
            show_up_menu += "oo"
        elif option == "3":
            show_up_menu += "xXx"
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
