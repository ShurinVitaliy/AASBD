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

def count_keys_equal(arr, mrange):
	result = list()
	for x in range(0, mrange):
		result.append(0)
	for x in range(0, len(arr)):
		key = arr[x]
		result[key] = result[key] + 1
	print(result)
	return result
		
def count_keys_less(equal, mrange):
	result = list()
	for x in range(0, mrange):
		result.append(0)
	for x in range(1, mrange):
		result[x] = result[x - 1] + equal[x - 1]
	print(result)
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
	print(next)
	print(result)
	return result

def counting_sort(arr, mrange):
	equal = count_keys_equal(arr, mrange + 1)
	less = count_keys_less(equal, mrange + 1)
	result = rearrange(arr, less, mrange + 1)
	return result
	
A = [1, 4, 0, 2, 5, 3, 8, 6, 9, 10]
B = ["Ab","Aa", "Ac", "C", "B", "E", "D", "F", "G"]
C = [2, 0, 3, 9, 1, 6, 5, 4, 8, 6, 7, 9]

print(merge_sort(A))
print(merge_sort(B))
print(counting_sort(C, 9))