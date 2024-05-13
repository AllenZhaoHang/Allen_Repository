'''
    receives a file (by name) as a parameter
    and reads grades from the file
    Hang Zhao
    10/29/2023
'''
import os


def average_grades(file_name):
    '''
    receives a file (by name) as a parameter
    and reads grades from the file
    Parameter: file_name
    Return: average of those grades
    '''
    try:
        with open(file_name, 'r') as file:

            grades = file.read().splitlines()
            for line in grades:
                if line.strip() == '':
                    print("File abc.txt was not found")
                    return 0.0
            # if not grades:
            #     print(len(grades))
            #     print("File abc.txt was not found")
            #     print("")
            #     return 0.0

            total = sum(map(float, grades))
            average = total / len(grades)
            return average

    except FileNotFoundError:
        print(f"File {file_name} was not found")
        return None
    except PermissionError:
        print(f"Permission denied for {file_name}")
    except Exception as e:
        print(f"Error occurred while reading {file_name}: {e}")

    return None


def main():
    '''main function'''
    print(average_grades('empty.txt'))


if __name__ == '__main__':
    main()
