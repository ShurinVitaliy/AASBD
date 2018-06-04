from time import clock
import numpy
import random
import sys

sys.setrecursionlimit(10000)

def linear_search(arr, x):
	start_time = clock()
	k = 0
	for i in arr:
		if i == x:		
			return (k, clock() - start_time)
		else:
			k = k + 1

def binary_search(arr, x):
	start_time = clock()
	p = 0
	r = len(arr) - 1
	while p <= r:
		q = int((p + r)/2)
		if arr[q] == x:
			return (q, clock() - start_time)	
		elif arr[q] > x:
			r = q - 1
		elif arr[q] < x:
			p = q + 1
	return (p, clock() - start_time)

def sentinel_linear_search(arr, x):
	start_time = clock()
	n = len(arr) - 1
	last = arr[n]
	i = 0
	while arr[i] != x:
		i = i + 1
		if i == n:
			return (None, clock() - start_time)
	arr[n] = last
	if i < n or arr[n] == x:
		return (i, clock() - start_time)

def recursive_linear_search(arr, i, x, start_time):
	n = len(arr) - 1
	if i > n:
		return None
	if arr[i] == x:
		return (i, clock() - start_time)
	else:
		return recursive_linear_search(arr, i + 1, x, start_time)

def delta_time_linear_search(arr):
	n = 1000
	i = 0 
	delta_time = 0
	while i < n:
		(position, time) = linear_search(arr, random.choice(arr))
		delta_time = delta_time + time
		i = i + 1
	return delta_time / n
	
def delta_time_sentinel_linear_search(arr):
	n = 1000
	i = 0 
	delta_time = 0
	while i < n:
		(position, time) = sentinel_linear_search(arr, random.choice(arr))
		delta_time = delta_time + time
		i = i + 1
	return delta_time / n

def delta_time_recursive_linear_search(arr):
	n = 1000
	i = 0 
	delta_time = 0
	while i < n:
		start_time = clock()
		(position, time) = recursive_linear_search(arr, 0, random.choice(arr), start_time)
		delta_time = delta_time + time
		i = i + 1
	return delta_time / n
		
A = [-7, 1, 3, 3, 4, 7, 11, 13]
B = [-7, 2, 2, 4, 4, 7, 8, 11, 13]
C = [-7, 1, 2, 3, 5, 7, 10, 13]

(position, time) = linear_search(A, 7)
print(position)

(position, time) = binary_search(B, 8)
print(position)

(position, time) = binary_search(C, 8)
print(position)

(position, time) = sentinel_linear_search(B, 8)
print(position)

start_time = clock()
(position, time) = recursive_linear_search(B, 0, 8, start_time)
print(position)


D1 = numpy.arange(0, 500, 1)	
D2 = numpy.arange(0, 1000, 1)
D3 = numpy.arange(0, 5000, 1)

print()

print("linear search n = 500:  ", delta_time_linear_search(D1))
print("linear search n = 1000: ", delta_time_linear_search(D2))
print("linear search n = 5000: ", delta_time_linear_search(D3))

print()

print("sentinel linear search n = 500:  ", delta_time_sentinel_linear_search(D1))
print("sentinel linear search n = 1000: ", delta_time_sentinel_linear_search(D2))
print("sentinel linear search n = 5000: ", delta_time_sentinel_linear_search(D3))

print()

print("recursive linear search n = 500:  ", delta_time_recursive_linear_search(D1))
print("recursive linear search n = 1000: ", delta_time_recursive_linear_search(D2))
print("recursive linear search n = 5000: ", delta_time_recursive_linear_search(D3))

