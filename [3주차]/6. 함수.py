# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def is_odd(number):
	if number % 2 == 1:   # 2로 나누었을 때 나머지가 1이면 홀수이다.
		return '홀수'
	else:
		return '짝수'
	
number = int(input(""))
print(is_odd(number))
