# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
Name = input('Name: ')
a = Name.split()

for i in range(len(a)):
	b = a[i][0]
	print(b, end = '')
	print('. ', end = '')
