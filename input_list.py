c_1 = False
counter = 0
b = []

while c_1 == False:
	if counter == 5:
		c_1 = True
		break	
	else:
		print("Please type the number:")
		a = input()
		if a.isdigit() and counter <= 4:
			a = int(a)
			b = b + [a]
			counter += 1
		else:
			counter -= 1
			print("Type it again!")