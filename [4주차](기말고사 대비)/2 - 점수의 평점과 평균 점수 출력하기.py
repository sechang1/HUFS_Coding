# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def Grade (num):
	if num >= 90:
		return 'Grade: A'
	elif num >= 80:
		return 'Grade: B'
	elif num >= 70:
		return 'Grade: C'
	elif num >= 60:
		return 'Grade: D'
	else:
		return 'Grade: F'

average = 0

a = int(input('Enter the number of scores: '))

for i in range(a):
	score = int(input('Enter a score: '))
	average += score
	print(Grade(score))
	
print('Average test score: ', end='')
print(average / a)
