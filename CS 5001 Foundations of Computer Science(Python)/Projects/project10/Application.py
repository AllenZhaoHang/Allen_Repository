'''
    This file is the main file for the application. It will be used to run the application.
    Hang Zhao
    11/10/2023
'''
from container_of_objects import ContainerOfObjects


def main():
    ''' main function'''
    container = ContainerOfObjects()
    original_data = container.loadFromFile("data.txt")

    menu = """
    1. List Original Data (in Array of Objects)
    2. Report of Stack of Data
    3. Report of Queue of Data
    4. End Program
    """
    count = 1
    while True:
        print(menu)
        choice = input("Enter your choice: ")
        print("'" * 6,"your chosen: ", count, "'" * 10)
        count += 1
        if choice == "1":
            container.printOriginalData(original_data)
        elif choice == "2":
            container.printStack(original_data)
        elif choice == "3":
            container.printQueue(original_data)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
