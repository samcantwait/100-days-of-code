import random
from number_guess_art import logo

EASY = 10
HARD = 5


def check_guess(num, guess, attempts):
    if num == guess:
        print(f"You got it! The answer was {num}!")
        return
    elif num < guess:
        print("Too high.")
    else:
        print("Too low.")
    return attempts - 1


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ")
    if difficulty == "easy":
        return EASY
    else:
        return HARD


def play():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    num = random.randint(2, 99)
    print(f"Testing.... #{num}")
    attempts = set_difficulty()

    guess = 0
    while guess != num:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:  "))
        attempts = check_guess(num, guess, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != num:
            print("Guess again.")


play()
