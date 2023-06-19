import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

NATO_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input('Enter your word: ').upper()
output_list = [NATO_dict[letter] for letter in word]
