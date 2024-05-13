"""
    Hang Zhao
    9/18/2023
    receives two parameter values and compare
"""
#  receives two parameter values


def is_equal(x, y):
    if x == y:
        return True
    else:
        return False


def main():
    num1 = input()
    num2 = input()
    print(is_equal(num1, num2))


if __name__ == "__main__":
    main()
