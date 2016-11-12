


def check(row, col,b_length,board):
	#上边

	if row > b_length-1 or col > b_length-1:
		return False

	for i in range(row):
		if board[i][col] == 1:
			return False		
	#左上
	if row == col:
		for i in range(row):
			if board[i][i] == 1:
				return False
	elif row > col:
		for i in range(col):
			if board[row - i - 1][col - i - 1] == 1:
				return False
	else:
		for i in range(row):
			if board[row - i - 1][col - i - 1] == 1:
				return False

	#右上
	t_range = max(row, col)

	for i in range(t_range):
		t_row = row - i - 1
		t_col = col + i + 1
		if t_row > b_length - 1 or t_col > b_length - 1:
			break
		elif board[t_row][t_col] == 1:
			return False

	return True

def find(row,board):
	for i in range(len(board[row])):
		if board[row][i] == 1:
			return i
	return -1

def back_tracking(row,board):
	row -= 1
	t_col = find(row,board)
	board[row][t_col] = 0
	col = t_col + 1

	return row, col,board


def init_board(b_len):
	b = []
	for i in range(b_len):
		a = [0] * b_len
		b.append(a)
	
	return b


def eight_queens(value,board):
	

	current_row = 0
	current_col = 0
	count = 0
	while True:
	# print(current_row, current_col)
		if check(current_row, current_col,value,board) == True:
			board[current_row][current_col] = 1
			current_row += 1
			current_col = 0

			if current_row == value: 
				for i in board:
					print(i)
				print(" ")

				count += 1
				current_row, current_col, board = back_tracking(current_row,board)
				

			if current_row < 0 or current_row > value:
				break

		else:
			current_col += 1
			if current_col > value-1:
				current_row, current_col, board = back_tracking(current_row,board)

				if current_row < 0 or current_row > value:
					break
	print("Total Possibility: ", count)	

con = True
int_value = int

while con == True:
	print ("Please enter a valid digit:")
	a = input()
	if a.isdigit() == True:
		con = False
		int_value = int(a)

board = init_board(int_value)

eight_queens(int_value,board)

