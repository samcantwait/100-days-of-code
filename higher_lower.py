import random
import os
from higher_lower_data import data
from higher_lower_art import logo, vs


def choose():
    return random.choice(data)


def print_data(choice):
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    return f"{name}, a {description} from {country}."


def get_answer(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"


def play():
    print(logo)
    choice_b = choose()
    is_game_over = False
    score = 0
    while not is_game_over:
        choice_a = choice_b
        choice_b = choose()

        while choice_a == choice_b:
            choice_b = choose()

        print(f"Compare a: {print_data(choice_a)}")
        print(vs)
        print(f"Against b: {print_data(choice_b)}")
        selection = input("Who has more followers? Type 'a' or 'b':  ")

        answer = get_answer(choice_a, choice_b)

        os.system("cls||clear")
        print(logo)
        if selection == answer:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            is_game_over = True
            print(f"Sorry you're wrong. Final score: {score}")


play()
