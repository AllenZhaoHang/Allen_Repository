'''
    Hang Zhao
    09/28/203
    guess My Number game
'''
import random


def main():
    ''' main function '''
    print("Welcome to the Guess My Number game!")
    max_value = get_max_value()
    target_number = generate_random_number(max_value)
    print("random number is: " + str(target_number))
    attempts = 0
    guesses = []

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess == target_number:
            print(
                f"Congratulations! You've guessed the target number {target_number} in {attempts} attempts.")
            break
        else:
            guesses.append(guess)
            feedback = get_feedback(target_number, guesses)
            print(feedback)


def get_max_value():
    ''' get max value from user input '''
    while True:
        try:
            max_value = int(input("Enter the maximum value to choose from: "))
            if max_value > 0:
                return max_value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def generate_random_number(max_value):
    ''' get random number '''
    return random.randint(1, max_value)


def get_user_guess():
    ''' get user guess '''
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_feedback(secret_number, guesses):
    ''' print feedback to user '''
    last_guess = guesses[-1]
    previous_guess = guesses[-2] if len(guesses) >= 2 else None

    if previous_guess is not None:
        previous_distance = abs(secret_number - previous_guess)
        last_distance = abs(secret_number - last_guess)

        if last_distance < previous_distance:
            return "Getting Warmer"
        elif last_distance > previous_distance:
            return "Getting Colder"
        else:
            return "Same distance"
    else:
        return ""


if __name__ == "__main__":
    main()
