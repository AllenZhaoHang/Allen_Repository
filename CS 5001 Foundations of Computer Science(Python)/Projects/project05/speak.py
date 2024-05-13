'''
'''

def leetspeak_converter(input_string):
    ''' '''
    result = ""
    leetspeak_dict = {
        'a': '4',
        'e': '3',
        'h': '#',
        'i': '1',
        'l': '|',
        'o': '0',
        'p': '|D',
        't': '7'
    }

    for char in input_string:
        if char.lower() in leetspeak_dict:
            result += leetspeak_dict[char.lower()]
        else:
            result += char

    return result

def main():
    ''''''
    print(leetspeak_converter("Hello World!"))
    

if __name__ == '__main__':
    main()
