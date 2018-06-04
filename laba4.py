from time import clock
from numpy import arange, random
from pylab import plot, grid, legend, show

def merge(left, right):
	result = list()
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left[0])
			del left[0]
		else:
			result.append(right[0])
			del right[0]
	if len(left) != 0:
		result = result + left
	elif len(right) != 0:
		result = result + right
	return result

def count_keys_equal(arr, mrange):
	result = list()
	for x in range(0, mrange):
		result.append(0)
	for x in range(0, len(arr)):
		key = arr[x]
		result[key] = result[key] + 1
	return result
		
def count_keys_less(equal, mrange):
	result = list()
	for x in range(0, mrange):
		result.append(0)
	for x in range(1, mrange):
		result[x] = result[x - 1] + equal[x - 1]
	return result
		
def rearrange(arr, less, mrange):
	next = list()
	result = list()
	for x in range(0, len(arr)):
		result.append(0)
	for x in range(0, mrange):
		next.append(0)
	for x in range(0, mrange):
		next[x] = less[x] + 1
	for x in range(0, len(arr)):
		key = arr[x]
		index = next[key] - 1
		result[index] = arr[x]
		next[key] = next[key] + 1
	return result
	
def merge_sort(arr):
	if(len(arr) <= 1):
		return arr
	else:
		mid = int(len(arr) / 2)
		left = list()
		for x in arr[0 : mid]:
			left.append(x)
		right = list()
		for x in arr[mid : len(arr)]:
			right.append(x)
		left = merge_sort(left)
		right = merge_sort(right)
		result = merge(left, right)
		return result

def counting_sort(arr, mrange):
	equal = count_keys_equal(arr, mrange + 1)
	less = count_keys_less(equal, mrange + 1)
	result = rearrange(arr, less, mrange + 1)
	return result

def selection_sort(arr):
	for x in range(0, len(arr) - 1):
		smallest = x
		for y in range(x + 1, len(arr)):
			if arr[y] < arr[smallest]:
				smallest = y
		arr[x], arr[smallest] = arr[smallest], arr[x]
	return arr

#Y1 = [0.0999335457854435, 0.14083875791031697, 0.17081225174064762, 0.2065593330413371, 0.2441297518539205, 0.2845686517346042, 0.31756505716572647, 0.3558260711966241, 0.3912850583739882, 0.4352354593647618]

#Y2 = [0.617303771276676, 1.518539970699733, 2.714223089818912, 4.18485259246953, 6.002139372611802, 8.010427647973902, 10.494070471673894, 13.228133165184033, 16.19430721481325, 19.96337013487185]

#X = arange(25000, 275000, 25000)

#k  = 50000
# for x in range(0, 10):
	# A = random.randint(0, 100000, k * (x + 1)).tolist()
	
	# start_time = clock()
	# counting_sort(A, 100000)
	# t = clock() - start_time
	# Y1.append(t)
	
	# start_time = clock()
	# merge_sort(A)
	# t = clock() - start_time
	# Y2.append(t)
#print(Y1, Y2)

X = arange(0, 50, 1)
Y1 = []
Y2 = []
Y3 = []
Y3 = []
k = 20
for x in range(0,50):
	A = random.randint(0, 15, k * (x + 1)).tolist()
	start_time = clock()
	counting_sort(A, 20)
	t = clock() - start_time
	Y1.append(t)
	#print(t)
	
	start_time = clock()
	merge_sort(A)
	t = clock() - start_time
	Y2.append(t)
	#print(t)
	
	start_time = clock()
	selection_sort(A)
	t = clock() - start_time
	Y3.append(t)
	#print(t)
	
line_selection_sort = plot(X, Y3, label = "selection sort")
line_merge_sort = plot(X, Y2, label = "merge sort")
line_counting_sort = plot(X, Y1, label = "Counting sort")

grid()
legend()
show()









