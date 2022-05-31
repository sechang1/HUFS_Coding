# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
a = int(input('Enter a number: '))
c = []

if a == 1:
	print('1 is not prime')
elif a  == 2:
	print('%d is prime.' %a)
elif a >=3:
	for i in range(2, a):
		b = a % i
		c.append(b)
		if c.count(0) >= 1:
			print('%d is not prime' %a)
		elif c.count(0) == 0:
			print('%d is prime' %a)
