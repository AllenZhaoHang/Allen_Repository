'''
    Animal Clinic
    Hang Zhao
    10/29/2023
'''
import os

def main():
    '''main function'''
    try:
        filename = input("Enter the file name: ")
        if os.path.isdir(filename):
            print("This is not a file")
        elif os.path.exists(filename):
            choice = input("Do you want to replace the file?(y/n)")
            if choice == "y":
                file = open(filename,"w")
            else:
                file = open(file, "a")
            number = 0
            while number != -1:
                try:
                    number = int(input("Enter the weight(or -1 to quit): "))
                    if number > 0:
                        file.write(str(number))
                        file.write("\n")
                except ValueError as ex:
                    print("Enter a integer value")
        file.close()
    except PermissionError as ex:
        print("You do not have the file permission")
    except OSError as ex:
        print("Something happend with your USB")

if __name__ == '__main__':
    main()
