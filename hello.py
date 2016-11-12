#Type
#int整数, float浮点数, string文本, char单字节, bool布尔值

# #Variable	
# x=1
# y="abc"
# z= True
# # x,y,z 是我们的variable

#loop
# if true:
# 	print ("Hello")
	#如果_，就
# while z:
# 	print ("Hello")
# 	z= False
# 	#当_是正确的时候，执行_，直到_

# for i in range(5):
# 	print"hello"
# for i in range(101):
# 	if i % 3 == 0:
# 		print("buzz")
# 	if i % 5 == 0:
# 		print("fuzz")
# 	if i % 3 == 0:
# 		if  i % 5 == 0:
# 			print("buzz fuzz")	

# and
# or

# True and True
# False and True ==False
# True and False ==False
# False and False == False

# True or True == True
# True or False == True
# False or True == True
# False or False == False

# for i in range(101):
# 	if i % 3 == 0 and i % 5 != 0 :
# 		print("buzz")
# 	if i % 5 == 0 and i % 3 != 0 :
# 		print("fuzz")
# 	if i % 3 == 0 and i % 5 == 0 :
# 		print("buzz fuzz")

#Least and the Most

# structure 结构

# list 
# a = [1,5,2,4,3,0,6,8,7,9]
# b = ["a","b","c","d","e"]
# print(a)
# print	(b)

# nowMaximum = a[0]


# for i in a:
# 	print (nowMaximum,i)
# 	if nowMaximum < i:
# 		nowMaximum = i
# print(nowMaximum)

# nowMinimum = a[0]
# for i in a:
# 	print(nowMinimum,i)
# 	if nowMinimum > i:
# 		 nowMinimum = i
# print(nowMinimum)

# suma= 0

# for t in range(21):
# 	print(suma,"+",t,"=")
# 	suma = suma+ t
# 	print(suma)

result = ""
rows = 6

for a in range(rows):
	space = " "*(rows-a)
	result  = space + "*"*(a*2-1)
	print(result)

# currentFloor = 0
# maxFloor = 6
# stars = ""

# while currentFloor < maxFloor:
# 	space = " "*(maxFloor-currentFloor)
# 	stars =stars + "*"
# 	result = space + stars
# 	currentFloor = currentFloor + 1
	
# 	print (result)