import random
import os
from blackjack_art import logo

print(logo)
print("Welcome to Blackjack!")


def play():
    game_over = False

    def choose_card():
        all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(all_cards)

    def add_card(cards):
        cards.append(choose_card())
        if sum(cards) > 21:
            if 11 in cards:
                cards.remove(11)
                cards.append(1)

    player_cards = [choose_card(), choose_card()]
    computer_cards = [choose_card(), choose_card()]
    while not game_over:
        print(f"Computer's first card is {computer_cards[0]}")
        print(f"Your cards: {player_cards}, current score {sum(player_cards)}")
        if sum(computer_cards) == 21 or sum(player_cards) == 21:
            game_over = True
        else:
            hit = input("Would you like to hit? 'y' or 'n'?  ")
            if hit == "y":
                add_card(player_cards)
                if sum(player_cards) > 21:
                    game_over = True
            else:
                game_over = True
        if game_over == True:
            while sum(computer_cards) < 17:
                add_card(computer_cards)
            print(f"Your final hand: {player_cards}, final score {sum(player_cards)}")
            print(
                f"Computer's final hand: {computer_cards}, final score {sum(computer_cards)}"
            )
            player_total = sum(player_cards)
            computer_total = sum(computer_cards)
            if (
                player_total < 22
                and computer_total < 22
                and computer_total == player_total
            ):
                print("It was a draw! 🤝")
            elif player_total == 21 and computer_total != 21 and len(player_cards) == 2:
                print("BLACKJACK! You win!")
            elif computer_total == 21 and len(computer_cards) == 2:
                print("Your opponent got blackjack.  You lose.")
            elif player_total > 21:
                print("You went over, you lose. 😤")
            elif computer_total < 22 and computer_total > player_total:
                print("The computer beat you. 😫")
            elif computer_total > 21:
                print("Your opponent went over! You win! 🥳 ")
            else:
                print("Congratulations, you won! 🏆")


while input("Would you like to play a game? Type 'y' for yes or 'n' for no.  ") == "y":
    os.system("cls")
    print(logo)
    play()
