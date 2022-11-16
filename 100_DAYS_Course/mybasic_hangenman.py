#HANGED MAN

# COS POPISANE JAKOS DZIALA ALE TROCHE DALEKO DO TEGO CO MOGLO BY BYC

from __future__ import print_function
import sys, time

hang = [0]*7
hang[0] = ''' 
		  +---+
		  |	  |
		  0	  |
		 	  |
			  |
			  |
			  |
	=============='''
hang[1] = ''' 
		  +---+
		  |	  |
		  0	  |
		 /	  |
			  |
			  |
			  |
	=============='''
hang[2] = ''' 
		  +---+
		  |	  |
		  0	  |
		 /|   |
			  |
			  |
			  |
	=============='''
hang[3] = ''' 
		  +---+
		  |	  |
		  0	  |
		 /|\  |
			  |
			  |
			  |
	=============='''
hang[4] = ''' 
		  +---+
		  |	  |
		  0	  |
		 /|\  |
		  |   |
			  |
			  |
	=============='''
hang[5] = ''' 
		  +---+
		  |	  |
		  0	  |
		 /|\  |
		  |	  |
		 /	  |
			  |
	=============='''
hang[6] = ''' 
		  +---+
		  |	  |
		  0	  |
		 /|\  |
		  |	  |
		 / \  |
			  |
	=============='''



word = 'auetogowno'
print('Welcome to HANGED MAN game')
letter = input('''Choose a letter 
''')
letters = ['None']*100
letters[0] = letter

hanged_man_state=0
count = 0
WORD = []
for j in range(len(word)):
	if letter == word[j]:
		WORD.append(word[j])
		count+=1
	else:
		WORD.append('_')
if count < 0:
	print(hang[hanged_man_state])
	hanged_man_state+=1


i=0
count = 0
while hanged_man_state < 6:
	if i in letters:
		continue
	else: 
		for j in range(len(word)):
			if letter == word[j]:
				WORD[j]=word[j]
				count += 1
			else:
				WORD[j]=='_'
		if hanged_man_state == 6:
					print('POWIESZONY NARA')
					break		
		print(''.join(WORD))
		if count == 0:
			hanged_man_state+=1
			print(hang[hanged_man_state])
		else:
			print(hang[hanged_man_state])
		letter = input('''Choose a letter
''')
		letters[i]+=letter
		count = 0
	i+=1
	