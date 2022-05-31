# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import random
random.seed(1)

n = True

while n:
	a = int(input('Enter 1 for Rock, 2 for Paper, and 3 for Scissors: '))

	if a == 1:
		print('Your choice: Rock')
	elif a == 2:
		print('Your choice: Paper')
	elif a == 3:
		print('Your choice: Scissors')

	b = random.randint(1,3)
	if b == 1:
		print("Computer's choice: Rock")
	elif b == 2:
		print("Computer's choice: Paper")
	elif b == 3:
		print("Computer's choice: Scissors")

	if a == 1 and b == 3:
		print('You won!')
		n =  False
	elif a == 2 and b == 1:
		print('You won!')
		n =  False
	elif a == 3 and b == 2:
		print('You won!')
		n =  False
	elif a == 1 and b ==2:
		print('You lost')
		n =  False
	elif a == 2 and b == 3:
		print('You lost')
		n =  False
	elif a == 3 and b == 1:
		print('You lost')
		n =  False
	elif a == 1 and b == 1:
		print('Tie')
		n =  True
	elif a == 2 and b == 2:
		print('Tie')
		n =  True
	elif a == 3 and b == 3:
		print('Tie')
		n =  True
