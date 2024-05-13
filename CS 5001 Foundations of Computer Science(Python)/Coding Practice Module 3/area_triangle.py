"""
    Hang Zhao
    9/18/2023
    returns the area of a triangle
"""
# returns the area of a triangle


def area_triangle(x, y, z):
    # A = √s(s−a)(s−b)(s−c)
    s = (x + y + z) / 2
    result = (s * (s - x) * (s - y) * (s - z)) ** 0.5
    return result


def main():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    print(area_triangle(num1, num2, num3))


if __name__ == "__main__":
    main()
