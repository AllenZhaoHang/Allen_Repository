"""
    HANG ZHAO
    09/17/2023
    Write a program that reads the length of a
    rectangle's sides and then prints
    the area and perimeter of the rectangle
    the length of the diagonal
"""


def main():
    month = input("Enter month: ")
    # determine the number of days
    if month == "Jan" or month == "January" or month == str(1):
        days = 31
    elif month == "Feb" or month == "February" or month == str(2):
        days = 28
    elif month == "Mar" or month == "March" or month == str(3):
        days = 31
    elif month == "Apr" or month == "April" or month == str(4):
        days = 30
    elif month == "May" or month == "May" or month == str(5):
        days = 31
    elif month == "Jun" or month == "June" or month == str(6):
        days = 30
    elif month == "Jul" or month == "July" or month == str(7):
        days = 31
    elif month == "Aug" or month == "August" or month == str(8):
        days = 31
    elif month == "Sep" or month == "September" or month == str(9):
        days = 30
    elif month == "Oct" or month == "October" or month == str(10):
        days = 31
    elif month == "Nov" or month == "November" or month == str(11):
        days = 30
    elif month == "Dec" or month == "December" or month == str(12):
        days = 31
    else:
        days = "Unknown"
    print(month, "has", days, "days")


if __name__ == "__main__":
    main()
