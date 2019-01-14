def palindromic(num):
	copy = num
	while True:
		palindromic = str(num)[::-1]
		if palindromic == str(num) and num != copy:
			break
		else:
			num += 1
	print(num)

number = int(input('Please enter a number: '))
palindromic(number)
