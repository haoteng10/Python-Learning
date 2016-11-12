a = [5,2,6,7,9,1,0,3]
b = [1,2,3,5641,21,455,1,5,3,6,4,10,4,5,2,7,11,8,5,99,42,36,42,2,234,5,32,87,55,6,90,56,3,456,3,45,63,45,63,46,3,56,34]
def find_min(list):
	if len(list) > 0:
		return min(list)
	else:
		print("Invalid")

def find_index(list,item):
	if len(list) > 0:
		for i in range(len(list)):
			if list[i] == item:
				return i
	else:
		return "Invalid"

def selection_sort(list):
	new_list = []
	while len(list) > 0:
		#find minimum
		x = find_min(list)
		#remove min
		y = find_index(list,x)
		list.pop(y)
		#append min
		new_list.append(x)
	return new_list

def swap(x,y):
	return y,x

def _bubble_sort(list):
	for i in range(1,len(list)):
		index_b = i
		index_a = i - 1

		if list[index_b] <= list[index_a]:
			list[index_b],list[index_a] = swap(list[index_b],list[index_a])

def bubble_sort(list):
	if len(list) <= 1:
		return list
	
	# for _ in range(len(list)):
	
	for _ in list:
		_bubble_sort(list)

	print (list)

bubble_sort(b)


# new_list = selection_sort(list)
# print(new_list)

