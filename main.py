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

#Write your code below this line 👇
game_image = [rock, paper, scissors]
user = int(input('What do you choose? 0 for rock, 1 for paper, 2 for scissors.\n'))

# checking for invaild input before start
if user >= 3 or user < 0:
  print('Invalid input entered. You Lose.')
else:
  print(f'You chose:\n{game_image[user]}')
  # random computer choice
  com = random.randint(0,2)
  print(f'Computer chose:\n{game_image[com]}')
  # rock, paper scissor game logic
  if user == 0 and com == 2:
    print('You Win!')
  elif com == 0 and user == 2:
    print('You Lose.')
  elif user > com:
    print('You Win!')
  elif user == com:
    print('Draw.')
  elif user < com:
    print('You Lose')