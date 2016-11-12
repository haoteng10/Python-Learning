b = [-1] * 8

def check (index):
	for i in range(index):
		if b[i] == b[index]:
			return False

	for i in range(index):
		if i - (index - b[index]) == b[i]:
			return False

	for i in range(index):
		if index + b[index] == i + b[i] and i < index:
			return False 
	return True

def back_tracking():
	pass
		
def eight_queens():
	i = 0
	while True:

		if b[i] == 7:
			b[i] = -1
			i -= 1

		for j in range(b[i] + 1,8):
			b[i] = j
			if check(i):
				i += 1
				break
			elif j == 7:
				b[i] = -1
				i -= 1

		if i == 8:
			print(b)
			return

eight_queens()
