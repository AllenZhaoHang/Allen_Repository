'''
    Hang Zhao
    09/28/203
    test guess My Number game
'''
from guessMyNumber import get_max_value
from guessMyNumber import generate_random_number
from guessMyNumber import get_user_guess
from guessMyNumber import get_feedback

def test_get_max_value():
    ''' test function get_max_value() '''
    print("Test function get_max_value() good example:")
    print(get_max_value())
    print("Test function get_max_value() bad example:")
    print(get_max_value())


def test_generate_random_number():
    ''' test generate_random_number '''
    print("Test function generate_random_number() good example:")
    print(generate_random_number(100))
    print("Test function generate_random_number() bad example:")
    print(generate_random_number(3))


def test_get_user_guess():
    ''' test get_user_guess '''
    print("Test function get_user_guess() good example:")
    print(get_user_guess())
    print("Test function get_user_guess() bad example:")
    print(get_user_guess())


def test_get_feedback():
    ''' test get_feedback '''
    guesses = [1, 2, 3, 10, 12]
    print("Test function get_feedback() good example:")
    print(get_feedback(3, guesses))
    print("Test function get_feedback() bad example:")
    print(get_feedback(5, guesses))


def main():
    ''' main function '''
    test_get_max_value()
    test_generate_random_number()
    test_get_user_guess()
    test_get_feedback()


if __name__ == "__main__":
    main()

