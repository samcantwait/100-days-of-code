import random
from hangman_art import stages, logo
from hangman_words import word_list


word = random.choice(word_list)
lives = 6
print(word)

display = []
for char in word:
    display += '_'

guesses = []
gameover = False

print(logo)
print('Welcome to hangman!')
print(f'A word has been chosen.\n{display}')

while not gameover:
    guess = input('Please chose a letter:  ')
    if guess in guesses:
        print(f'You already guessed {guess}')
    else:
        for i in range(0, len(display)):
            if guess == word[i]:
                display[i] = guess
        if guess not in word:
            print(f'Oh no! The word does not contain a {guess}.')
            lives -= 1
        else:
            print(f'The letter {guess} was in the word!')
        guesses += guess
    print(stages[lives])
    print(display)
    if lives == 0:
        print(f'Sorry, you lost. The word was {word}.')
        gameover = True
    if '_' not in display:
        print(f'Congratulations! You won! The word was {word}.')
        gameover = True
