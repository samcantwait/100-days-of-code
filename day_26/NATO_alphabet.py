import pandas

alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in alphabet.iterrows()}

user_word = input("Enter your word: ").upper()
in_code = [dictionary[letter] for letter in user_word]
print(in_code)
