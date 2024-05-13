'''
    Write a main function that calls this function 20 times
    Hang Zhao
    10/29/2023
'''

import random
random.seed(0)


def generate_random_error():
    '''random error'''
    value = random.randint(0, 3)
    if value == 0:
        raise ZeroDivisionError(value)
    elif value == 1:
        raise TypeError(value)
    elif value == 2:
        raise ValueError(value)
    else:
        raise NameError(value)


def main():
    error_messages = {
        ZeroDivisionError: lambda e: f"Zero division error -- {e.args[0]}",
        TypeError: lambda e: f"Type error raised   -- {e.args[0]}",
        ValueError: lambda e: f"Value error raised  -- {e.args[0]}",
        NameError: lambda e: f"Name error raised   -- {e.args[0]}",
    }

    for i in range(20):
        try:
            generate_random_error()
        except Exception as e:
            error_type = type(e)
            error_message = error_messages.get(
                error_type, lambda e: f"Unknown error -- {e.args[0]}")
            print(error_message(e))


if __name__ == '__main__':
    main()
