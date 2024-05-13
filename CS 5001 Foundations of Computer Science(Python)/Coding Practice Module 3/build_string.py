"""
    Hang Zhao
    9/18/2023
    repeat the specified times of str
"""
# repeat the specified times of str


def build_string(str, num1, num2, num3):
    line1 = str * num1
    line2 = str * num2
    line3 = str * num3
    result = f"{line1}\n{line2}\n{line3}"
    return result


def main():
    string = str(input("Enter a string: "))
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    output = build_string(string, num1, num2, num3)
    print(output)


if __name__ == "__main__":
    main()
