'''
    Write a recursive function called
    in_english that takes a integer value
    as input and returns a string containing
    the digits of the number in English
    Hang Zhao
    10/19/2023
'''


def in_english(num):
    '''integer value'''
    digit_in_english = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    if num < 10:
        return digit_in_english[str(num)]
    last_digit = num % 10
    rest_of_num = num // 10
    rest_of_eng = in_english(rest_of_num)
    return rest_of_eng + ' ' + digit_in_english[str(last_digit)]


def main():
    '''main'''
    print(in_englist(153))


if __name__ == '__main__':
    main()
