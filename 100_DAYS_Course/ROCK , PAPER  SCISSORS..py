#ROCK , PAPER  SCISSORS
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
RPS=[rock,paper,scissors]

choice=int(input("What do you choose? Type 0 for Rock , 1 for Peper or 2 for Scissors .\n"))
print(RPS[choice])

computer_choice=random.randint(0,2)
print(RPS[computer_choice])

if computer_choice==choice:
    print("Draw")
elif computer_choice==0 and choice==1:
    print("You win")
elif computer_choice==1 and choice==2:
    print("You win")
elif computer_choice==2 and choice==0:
    print("You win")
else:
    print("You lost")
    