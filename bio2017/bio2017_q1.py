def triangle(initial_row):
	choices = ['R', 'G', 'B']
	new_row = initial_row
	while len(new_row) > 1:
		next_row = ''
		for i in range(0, len(new_row) - 1):
			a = new_row[i]
			b = new_row[i + 1]
			if a == b:
				next_row += a
			else:
				l = [a, b]
				for each in choices:
					if each not in l:
						next_row += each
		new_row = next_row
	print(new_row)
#triangle('RBG')
triangle('RBGBGBGBGR')