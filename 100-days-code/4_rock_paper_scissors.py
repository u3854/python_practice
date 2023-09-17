import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Player input
player_input = 99
while player_input not in [0,1,2]:
    player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player_input not in [0,1,2]:
        print("Invalid input >:-(")
# Player ASCII art
if player_input == 0:
    print(rock)
elif player_input == 1:
    print(paper)
else:
    print(scissors)

# Getting random computer hand and printing ASCII art
comp_hand = random.randint(0,2)
print("Computer chose:\n")
if comp_hand == 0:
    print(rock)
elif comp_hand == 1:
    print(paper)
else:
    print(scissors)

outcome = player_input - comp_hand
# Checking outcome
if (outcome == 1) or (outcome == -2):
    print("\nYou win")
elif outcome == 0:
    print("\nDraw")
else:
    print("\nYou lose")