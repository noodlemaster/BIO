def F(position, direction):
	if direction == 'f':
		x = position[0]
		y = position[1] - 1
	elif direction == 'l':
		x = position[0] - 1
		y = position[1]
	elif direction == 'b':
		x = position[0]
		y = position[1] + 1
	elif direction == 'r':
		x = position[0] + 1
		y = position[1]
	if x > 4 or y > 4 or x < 0 or y < 0:
		return False
	else:
		return (x, y)

def L(position, direction):
	if direction == 'f':
		x = position[0] - 1
		y = position[1]
	elif direction == 'l':
		x = position[0]
		y = position[1] + 1
	elif direction == 'b':
		x = position[0] + 1
		y = position[1]
	elif direction == 'r':
		x = position[0]
		y = position[1] - 1
	if x > 4 or y > 4 or x < 0 or y < 0:
		return False
	else:
		return (x, y)

def R(position, direction):
	if direction == 'f':
		x = position[0] + 1
		y = position[1]
	elif direction == 'l':
		x = position[0]
		y = position[1] - 1
	elif direction == 'b':
		x = position[0] - 1
		y = position[1]
	elif direction == 'r':
		x = position[0]
		y = position[1] + 1
	if x > 4 or y > 4 or x < 0 or y < 0:
		return False
	else:
		return (x, y)

def check_tail(map, coord):
	if map[coord[0]][coord[1]] != 0:
		return False
	else:
		return True

def turn_right_90(direction):
	if direction == 'f':
		return 'r'
	elif direction == 'l':
		return 'f'
	elif direction == 'b':
		return 'l'
	elif direction == 'r':
		return 'b'

def update_map(map, list1, num_disappear):
	for each in list(set(list1)):
		map[each[0]][each[1]] = (map[each[0]][each[1]] + 1 )%num_disappear
	return map

def update_tailed(map, list1):
	list2 = list(set(list1))
	for each in list2:
		if map[each[0]][each[1]] == 0:
			list2.remove(each)
	return list2

def update_direction(direction, move):
	if direction == 'f':
		return move.lower()
	elif direction == 'r':
		return turn_right_90(move.lower())
	elif direction == 'b':
		return turn_right_90(turn_right_90(move.lower()))
	elif direction == 'l':
		return turn_right_90(turn_right_90(turn_right_90(move.lower())))

def convert_coord(coord):
	x = coord[0] - 2
	if coord[1] == 0:
		y = 2
	elif coord[1] == 1:
		y = 1
	elif coord[1] == 2:
		y = 0
	elif coord[1] == 3:
		y = -1
	elif coord[1] == 4:
		y = -2
	return (x, y)

def main(num_disappear, moves, num_moves):
	tailed = []
	map = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	position = (2, 2)
	index_instruction = 0
	direction = 'f'
	while num_moves > 0:
		tailed.append(position)
		move = moves[index_instruction%len(moves)]
		if move == 'F':
			if F(position, direction) and check_tail(map, F(position, direction)):
				position = F(position, direction)
				direction = update_direction(direction, move)
				map = update_map(map, tailed, num_disappear)
				tailed = update_tailed(map, tailed)
				index_instruction += 1
				num_moves -= 1
			else:
				direction = turn_right_90(direction)
		elif move == 'L':
			if L(position, direction) and check_tail(map, L(position, direction)):
				position = L(position, direction)
				direction = update_direction(direction, move)
				map = update_map(map, tailed, num_disappear)
				tailed = update_tailed(map, tailed)
				index_instruction += 1
				num_moves -= 1
			else:
				direction = turn_right_90(direction)
		elif move == 'R':
			if R(position, direction) and check_tail(map, R(position, direction)):
				position = R(position, direction)
				direction = update_direction(direction, move)
				map = update_map(map, tailed, num_disappear)
				tailed = update_tailed(map, tailed)
				index_instruction += 1
				num_moves -= 1
			else:
				direction = turn_right_90(direction)
	print(convert_coord(position))

t = int(input('Please enter the number of moves for the trial to disappear: '))
i = input('Please enter a sequence of instructions: ')
m = int(input('Please enter how many moves: '))
#print(F((2,2),'f'))
main(t, i, m)
#print(check_tail([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], (2,3)))
#print(update_direction('l', 'L'))
#print(update_map([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [(2,2)], 8)[0])
# m = [[0, 4, 3, 2, 0], [0, 5, 0, 1, 0], [0, 6, 7, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# if L((2,3), 'r') and check_tail(m, L((2,3), 'r')):
# 	print('y')
# else:
# 	print('n')