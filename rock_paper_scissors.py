import random
rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choices = [rock, paper, scissors]
choice = int(input(
    'What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n'))
if choice < 0 or choice > 2:
    print('Invalid number, you lose.')
    quit()
print(f'{choices[choice]}\n')
num = random.randint(0, 2)
print('The computer chooses: ')
print(f'{choices[num]}\n')
if num == choice:
    print("It's a tie")
elif (num == 0 and choice == 1) or (num == 1 and choice == 2) or (num == 2 and choice == 0):
    print('You win!')
else:
    print('You lose.')
