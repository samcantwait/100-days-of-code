with open('./input/names/invited_names.txt') as names_file:
    names = names_file.read().split()

with open('./input/letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

for name in names:
    with open(f'./output/readyToSend/letter_for_{name}.txt', mode='w') as letter_out:
        letter_out.write(letter.replace('[name]', name))
