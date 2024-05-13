"""
    HANG ZHAO
    9/17/2023
"""
def eculicaion(x1, y1, x2, y2):
    x_long = (x2 - x1) ** 2
    y_long = (y2 - y1) ** 2
    num = (x_long + y_long) ** 0.5
    return num

def test_suit(x1, y1, x2, y2, excepted):
    print("Testing points: ", str(x1), str(y1), str(x2), str(y2))
    actual = eculicaion(x1, y1, x2, y2)
    print("Excepted result: " + str(excepted))
    print("Actual result: " + str(actual))

def main():
    test_suit(0, 0, 0 , 0, 0.0)
    test_suit(2, -1, -2 , 2, 5.0)
    test_suit(0, 0, 1 , 1, 1.414)
    test_suit(-5.2, 3.8, -13.4 , 0.2, 8.955)
main()
