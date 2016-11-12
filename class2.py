# newInt = 10
# twoInt = 5

# print (newInt + twoInt)

# k = 5 % 2
# l = -5 % 2
# m = 5.0 % 2

# print (k,l,m)

# cond = True

# if cond == True :
# 	print ("True")
# else:
#  	print ("False")

# iteration = 0
# while iteration == 10:
# 	my_sum += iteration
# 	iteration += 1
# print (my_sum)

# n = input()
# if n.isdigit():
# 	s1 = 0
# 	s2 = 0
# 	s3 = 0
# 	for i in range (1,11):
# 		s1 += i
# 		s2 += (2* i - 1)
# 		s3 += (2 * i )
# 	print (s1,s2,s3)
# else:
# 	print ("Invalid Input")

# s2 = 0
# s3 = 0
# current = 1
# current2 = 1
# counter = 0
# counter2 = 0
# end = 1001

# while True:
# 	if counter == end:
# 		break
# 	elif current % 2 == 1:
# 		s2 += current
# 		counter += 1

# 	current += 1

# while True:
# 	if counter2 == end:
# 		break
# 	elif current2 % 2 == 0:
# 		s3 += current2
# 		counter2 += 1

# 	current2 += 1

# print(s2,s3)


# for i in range (rows):
# 	print (" "*(rows-i) +"*" * i )

# rows = input()
# if rows.isdigit()== True:
# 	rows = int(rows)
	
# 	for i in range(rows):	
# 		stars = "*"*(i*2-1)
# 		space = " "*(rows - i) 
# 		result = space + stars
# 		print (result)
# else:
# 	print("Invalid String. It must be a integer!")

# rows = 10

# for i in range (rows):
# 	stars = "*" * (rows - i)
# 	result =stars
# 	print (result)

# rows = 10
# for i in range(rows):	
# 		stars = "*"*(rows - i)
# 		space = " "*(i) 
# 		result = space + stars
# 		print (result)	

# rows = 10
# for i in range (rows-1,-1,-1):
# 	stars = "*" * (2 * i + 1)
# 	space = " " * (rows - i)
# 	result = space + stars
# 	print (result)


# user_input = 3
# rows = user_input - 1
# space = ""

# for i in range(rows-1):	
# 		if rows >= 3:
# 			stars = "*"*(i*2-1)
# 		else:
# 			stars = "*"
# 		if rows >= 2:
# 			space = " "*(rows - i + 1) 
# 		else :
# 			space = " "
# 		result = space + stars
# 		print (result)

# for i in range (rows-1,-1,-1):
# 	stars = "*" * (2 * i + 1)
# 	space = " " * (rows - i)
# 	result = space + stars
# 	print (result)

rows = 3
space = ""

for i in range (1,rows):
	stars = "*" * (i*2-1)
	space = " " * (rows - i + 1)
	result = space + stars
	print (result)

for i in range (rows-1,-1,-1):
	stars = "*" * (2 * i + 1)
	space = " " * (rows - i)
	result = space + stars
	print (result)



# lines = 5
# for i in range(lines):
# 	stars = ""
# 	for j in range(lines * 2 - 1):
# 		if j < lines:
# 			if lines - i - 1 > j:
# 					stars = stars + " "
# 			else:
# 					stars = stars + "*" 
# 		elif j >= lines:
# 			if lines + i > j:
# 					stars = stars + "*" 
# 	print(stars)

# user_input = 7
# lines = user_input + 1
# a = 0
# b = 0
# stars = ""
# space = ""

# for x in range(lines*lines):
# 	stars = stars + space
# 	if 	a <= lines:
# 		for i in range(lines):
# 			stars = (i*2-1) * "*" + stars
# 			a += 1

# 	if b <= lines:
# 		for s in range (lines):
# 			space = (lines - s) * " "	
# 			b += 1
# 			stars = stars + space + stars

# print (stars)













