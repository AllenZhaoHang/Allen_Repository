"""
    HANG ZHAO
    09/17/2023
    Write a program that reads the length of a rectangle's side
    and then prints
    the area and perimeter of the rectangle
    the length of the diagonal
"""
# reads the length of a rectangle's sides and then prints area
# perimeter and diagonal


def main():
    width = float(input('Enter width:'))
    height = float(input('Enter height:'))
    area = float(width * height)
    perimeter = float(2 * (width + height))
    diagonal = (width ** 2 + height ** 2) ** (0.5)
    print('The area of the rectangle is' + str(area))
    print("The perimeter of the rectangle is" + str(perimeter))
    print("The diagonal of the rectangle is" + str(diagonal))


if __name__ == "__main__":
    main()
