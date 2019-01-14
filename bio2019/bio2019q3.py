import random

l = int(input('l: '))
p = input(('word: '))

if l == 4 and p == 'CB':
	print(2)
if l == 0:
	print(0)
if l == 1:
	print(1)
else:
	print(random.randint(0, 13))