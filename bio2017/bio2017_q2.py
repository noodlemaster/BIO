def player_movement(edges, connected_edges):
	for each in edges:
		if each not in connected_edges:
			return each

def anticlock_neighbors(position):
	up = position - 6
	down = position + 6
	left = position - 1
	right = position + 1
	if position%6 == 1:
		neighbors = [up, down, right]
	elif position%6 == 0:
		neighbors = [up, left, down]
	else:
		neighbors = [up, left, down, right]
	for each in neighbors:
		if each < 1 or each > 36:
			neighbors.remove(each)
	return neighbors

def clock_neighbors(position):
	up = position - 6
	down = position + 6
	left = position - 1
	right = position + 1
	if position % 6 == 1:
		neighbors = [up, right, down]
	elif position % 6 == 0:
		neighbors = [up, down, left]
	else:
		neighbors = [up, right, down, left]
	for each in neighbors:
		if each < 1 or each > 36:
			neighbors.remove(each)
	return neighbors

def possible_edges(position, neighbors):
	edges = []
	for each in neighbors:
		edges.append([position, each])
		#edges.append([each, position])
	return edges

def generate_success_edges(row):
	success_edges = []
	top_left = int(row)*6 + 1
	#index = 0
	while top_left%6 != 0:
		#top_left = index*6 + 1
		top_right = top_left + 1
		bottom_left = top_left + 6
		bottom_right = top_right + 6
		success_edges.append([[top_left, top_right], [top_left, bottom_left], [top_right, bottom_right], [bottom_right, bottom_left]])
		top_left += 1
	return success_edges

def get_full_list():
	l=[]
	for i in range(0, 5):
		l1 = generate_success_edges(i)
		l += l1
	return l

def check_enclosed_square(connected_edges, successful_list, successful_squares):
	for each in successful_list:
		if each[0] in connected_edges and each[1] in connected_edges and connected_edges[2] in connected_edges and each[3] in connected_edges:
			num_square = successful_list.index(each)
			#print(num_square)
			if num_square not in successful_squares:
				successful_squares.append(num_square)
				return num_square


def update_board(board, num_square, WhoseTurn):
	y = int(int(num_square)/5)
	x = num_square%5
	if WhoseTurn == 1:
		board[y][x] = 'X'
	elif WhoseTurn == 2:
		board[y][x] = 'Y'
	return board

def display(board):
	for each in board:
		print(each)
		# for each1 in each:
		# 	print(each1)

def main(p1, m1, p2, m2, NumOfTurns):
	board = [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
	         ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
	success_squares = []
	num_player1 = 0
	num_player2 = 0
	position_1 = p1
	position_2 = p2
	WhoseTurn = 1
	connected_edges = []
	while NumOfTurns > 0:
		if WhoseTurn == 1:
			new_position_1 = (position_1 + m1)%36
			movement = player_movement(possible_edges(new_position_1, clock_neighbors(new_position_1)), connected_edges)
			if movement:
				connected_edges.append(movement)
				connected_edges.append([movement[1], movement[0]])
				if check_enclosed_square(connected_edges, get_full_list(), success_squares):
					board = update_board(board, check_enclosed_square(connected_edges, get_full_list(), success_squares), WhoseTurn)
					num_player1 += 1
				else:
					WhoseTurn = 2
				position_1 = new_position_1
				NumOfTurns -= 1
			else:
				position_1 += 1
		if WhoseTurn == 2:
			new_position_2 = (position_2 + m2)%36
			movement = player_movement(possible_edges(new_position_2, anticlock_neighbors(new_position_2)), connected_edges)
			if movement:
				connected_edges.append(movement)
				connected_edges.append([movement[1], movement[0]])
				if check_enclosed_square(connected_edges, get_full_list(), success_squares):
					board = update_board(board, check_enclosed_square(connected_edges, get_full_list(), success_squares), WhoseTurn)
					num_player2 += 1
				else:
					WhoseTurn = 1
				position_2 = new_position_2
				NumOfTurns -= 1
			else:
				position_2 += 1
	print(success_squares)
	display(board)
	print(str(num_player1) + ' ' + str(num_player2))
#print(clock_neighbors(27))
#generate_success_edges()
#get_full_list()
# board = [['*', '*', '*', '*', '*'], ['a', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
# 	         ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
# print(board[1][0])
main(4, 10, 14, 23, 25)
board = [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
	         ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
board[0][0] = 'X'
#print(board)