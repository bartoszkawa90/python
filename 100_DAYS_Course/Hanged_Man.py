# REAL HANGED MAN
from replit import clear
import random

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
from Hanged_man_words import words
word = random.choice(words)
lines = len(word)*['_']
count = 0
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


while count<6:
	letter = str(input("Guess a letter  "))
	clear()
	if letter in lines:
		print('You have already guessed that letter')
	for i in range(len(word)):
		if letter==word[i]:
			lines[i] = letter
	print(" ".join(lines))
	if '_' not in lines:
		print('YOU WIN')
		break
	if letter not in word:
		print("The ",letter,"is not correct letter")
		count+=1
	else:
		print("The ", letter, "is a correct letter")
	print(stages[len(stages)-count-1])
if count == 6:
	print("YOU LOSE")

