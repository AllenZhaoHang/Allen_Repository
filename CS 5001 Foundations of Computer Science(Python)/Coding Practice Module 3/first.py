"""
    Hang Zhao
    9/18/2023
    receives two parameter values and return
    first
"""
# receives two parameter values and return
# first


def first(x, y):
    if isinstance(x, (float, int)) and isinstance(y, (float, int)):
        return min(x, y)
    elif isinstance(x, str) and isinstance(y, str):
        return min(x, y)
    else:
        return None


def main():
    str1 = input()
    str2 = input()
    print(first(str1, str2))


if __name__ == "__main__":
    main()
