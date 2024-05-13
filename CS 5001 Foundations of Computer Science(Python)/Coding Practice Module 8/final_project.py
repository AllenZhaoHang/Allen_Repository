import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    return "Computer wins!"

def play_game():
    user_wins = 0
    computer_wins = 0
    rounds = int(input("Enter the number of rounds: "))

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1

    print(f"Game Over! You won {user_wins} rounds, and the computer won {computer_wins} rounds.")

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    play_game()