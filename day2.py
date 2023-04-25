# Day 2 Project: Tip Calculator
print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? '))
num_people = int(input('How many people to split the bill? '))
total_each = "{:.2f}".format((bill + bill * (tip / 100)) / num_people)
print(f'Each person should pay: ${total_each}')
