"""
    HANG ZHAO
    09/17/2023
    reads a measurement in meters and the converts it to inches,
    feet, and miles.
"""
# reads a measurement in meters and the converts it to inches, feet, and miles.


def main():
    length_meter = float(input("Enter length: "))
    length_inch = 39.3701 * length_meter
    length_feet = 3.2808416666666666 * length_meter
    length_mile = 0.000621371 * length_meter
    print("The length in inches is " + str(length_inch))
    print("The length in feet is " + str(length_feet))
    print("The length in miles is " + str(length_mile))


if __name__ == "__main__":
    main()
