from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(text, shift, direction):
    new_text = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_position = (
                index + shift) % 26 if direction == 'encode' else (index + 26 - shift) % 26
            shifted_letter = alphabet[new_position]
            new_text += shifted_letter
        else:
            new_text += letter
    print(f"The {direction}d text is {new_text}")
    play_again = input('Would you like to go again? Type "yes" or "no".\n')
    if play_again == 'yes':
        init()
    else:
        print('Goodbye!\n')


def init():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)


init()
