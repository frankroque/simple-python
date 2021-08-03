print("Simple Python Progam")

print("Let us descend:")

def reverseArray(array):
	beg = 0
	last = len(array) - 1
	temp = 0
	for i in range(0, len(array)):
		temp = array[beg]
		array[beg] = array[last]
		array[last] = temp
		beg += 1
		last -= 1
	print(array)

orderArray = [1,2,3,4,5,6,7,8,9,10]
print(orderArray)

print("Descending using the built in python .sort(reverse = True) function:")
orderArray.sort(reverse = True)
print(orderArray)

print("Descending using our own function:")
reverseArray(orderArray)


