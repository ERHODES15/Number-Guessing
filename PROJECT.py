import random
play = "Yes"
tries = 0
guess = 999 
name = input("What is your name? ")
print(f"Hey {name} it is nice to meet you.")
print("Lets play a game.")
print(" Pick a number 1 to 10 and i will tell you if it is higher or lower.")
while play == "Yes" or "yes":
    answer = random.randrange(1,10)
    while guess != answer:
        guess = input("What is your guess ")
        guess = int(guess) 
        if guess > answer:
            print("the answer is lower")
            tries =+ 1
            continue 
        elif guess < answer:
            print("the answer is higher")
            tries =+ 1
            continue
        elif guess == answer:
            print(f"You got it right good job, It took you {tries} tries")
            break
    play = input("Would you like to play again? ")
    if play == "no" or  play == "No":
        break
print("Thanks for playing.")
