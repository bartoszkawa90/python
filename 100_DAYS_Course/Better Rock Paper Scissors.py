#ROCK , PAPER  SCISSORS (po swojemu)
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

RPS_dict={'rock':rock , 'paper':paper, 'scissors':scissors}
RPS_list=[rock,paper,scissors]

choice=input("What do you choose? Rock , paper or scissors.\n")
print(RPS_dict[choice])
computer_choice=random.randint(0,2)
print(RPS_list[computer_choice])

if RPS_list[computer_choice]==RPS_dict[choice]:
    print("Draw")
elif computer_choice==0 and choice=='paper':
    print("You win")
elif computer_choice==1 and choice=='scissors':
    print("You win")
elif computer_choice==2 and choice=='rock':
    print("You win")
else:
    print("You lost")

