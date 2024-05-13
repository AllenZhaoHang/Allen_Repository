'''
    Demo
    Hang Zhao
    10/24/2023
'''


def main():
    '''main function'''
    student_scores = [["Alice", 95], ["Bob", 98], ["Charlie", 99], ["David", 100], ["Eve", 97]]
    for index in range(len(student_scores)):
        student_scores[index].append("100")
    print(student_scores)


if __name__ == '__main__':
    main()
