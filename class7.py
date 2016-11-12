# b = [0]
# for i in range(3):
# 	a = input()
# 	c = int(a)
# 	b = b + [c]

# nowMaximum = b[0]

# for i in b:
# 	if nowMaximum < i:
# 		nowMaximum = i
# print(nowMaximum)






# c_1 = False
# counter = 0
# b = [0]
# compare = 1

# while c_1 == False:
# 	print("Please type the list:")
# 	a = input()
# 	if a.isdigit() and counter <= 3:
# 		a = int(a)
# 		b = b + [a]
# 		counter += 1
# 	elif counter == 4:
# 		c_1 = True	

# print("Please type the number you want to compare with:")
# y = input()
# if y.isdigit():
# 	int_input = int(y)

# c_2 = False
# for i in range(len(b)):
# 	if int_input == b[i]:
# 		c_2 = True

# if c_2 == True:
# 	print(True)
# else:
# 	print(False)









# c_1 = False
# counter = 0
# b = []

# while c_1 == False:
# 	if counter == 5:
# 		c_1 = True
# 		break	
# 	else:
# 		print("Please type the number:")
# 		a = input()
# 		if a.isdigit() and counter <= 4:
# 			a = int(a)
# 			b = b + [a]
# 			counter += 1
# 		else:
# 			counter -= 1
# 			print("Type it again!")
	

# leng = len(b)

# c = [0,1]
# c[0] = b[0] 
# c[1] = b[leng -1]

# print(c)







# c = []
# for i in b:
# 	if i % 2 == 0:
# 		c = c + [i]

# print(c)

# e = []
# def no_duplicate(e):
# 	for x in range(len(b)):
# 		for y in b:
# 			if x != b[x]:
# 				e = e + [x]
# 	print(e)


# no_duplicate(e)








# a = "MysteryQ"
# b = ""

# for i in a:
# 	b = i + b
	
# print(b)










