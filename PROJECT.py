import random

def display_intro():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the randomly chosen number within the given range.")

def get_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    random_number = get_random_number()
    attempts = 0
    
    while True:
        guess = get_user_guess()
        attempts += 1
        
        if guess < random_number:
            print("It's higher.")
        elif guess > random_number:
            print("It's lower.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return attempts

def main():
    display_intro()
    high_score = None
    
    while True:
        print("\nNew Game! Try to beat the high score!" if high_score else "\nLet's Start!")
        attempts = play_game()
        
        if high_score is None or attempts < high_score:
            high_score = attempts
            print(f"New High Score: {high_score} attempts!")
        
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

