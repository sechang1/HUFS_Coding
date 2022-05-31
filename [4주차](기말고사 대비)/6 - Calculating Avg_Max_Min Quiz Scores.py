# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
s1 = input('Enter quiz scores for student #1: ')
s2 = input('Enter quiz scores for student #2: ')
s3 = input('Enter quiz scores for student #3: ')

a = s1.split()
sa = sum(map(int, a))
aa = sa / 4
print('Total and average scores for student#1: %d ' %(sa), end='')
print(aa)

b = s2.split()
sb = sum(map(int, b))
ab = sb / 4
print('Total and average scores for student#2: %d ' %(sb), end='')
print(ab)

c = s3.split()
sc = sum(map(int, c))
ac = sc / 4
print('Total and average scores for student#3: %d ' %(sc), end='')
print(ac)

k = [a, b, c]

print('Average, high, and low scores for quiz#1: ', end = '')
d = []
for i in k:
	d.append(i[0])
print(sum(map(int, d)) / 3, max(map(int, d)), min(map(int, d)))

print('Average, high, and low scores for quiz#2: ', end = '')
e = []
for i in k:
	e.append(i[1])
print(sum(map(int, e)) / 3, max(map(int, e)), min(map(int, e)))

print('Average, high, and low scores for quiz#3: ', end = '')
f = []
for i in k:
	f.append(i[2])
print(sum(map(int, f)) / 3, max(map(int, f)), min(map(int, f)))

print('Average, high, and low scores for quiz#4: ', end = '')
g = []
for i in k:
	g.append(i[3])
print(sum(map(int, g)) / 3, max(map(int, g)), min(map(int, g)))
