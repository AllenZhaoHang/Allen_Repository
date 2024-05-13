'''
    poems
    Hang Zhao
    10/29/2023
'''


def main():
    '''main function'''
    input = open("poems.txt", "r")
    output = open("poems-copy.txt", "w")
    for line in input:
        if line.strip() == "rose":
            output.write(line.upper())
        else:
            output.write(line)
    input.close()
    output.close()


if __name__ == '__main__':
    main()
