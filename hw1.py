
print ("Please enter a string:")
w = input()
counter = 0

for i in w:
	if i.isdigit():
		counter += 1
	if i.isalpha():
		counter += 1


print ("You entered ",counter, "character(s).")