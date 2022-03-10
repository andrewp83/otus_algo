#!/bin/python3

import copy
import random
import time


def less(x, y):
	return x < y


def sorted(array, cmp=less):
	for i in range(len(array) - 1):
		if cmp(array[i+1], array[i]):
			return False
	return True


def random_array(n):
	random.seed()
	return [random.randint(0, 100000) for i in range(n)]


def swap_items(array, i, j):
	array[i],array[j] = array[j],array[i]


def sort_bubble(array, cmp=less):
	n = len(array)
	for i in range(n - 1):
		for j in range(n - i - 1):
			if not cmp(array[j], array[j+1]):
				swap_items(array, j, j+1)

	return array


def linear_finder(array, start, end, value, cmp, step):
	for i in range(start, end, step):
		if not cmp(array[i], value):
			return i
	return end


def sort_insertion(array, cmp=less, first_not_of_finder=linear_finder, start=0, step=1):
	n = len(array)
	for i in range(start + step, n, step):
		cur_item = array[i]
		j = i
		while (j >= step) and not cmp(array[j-step], cur_item):
			array[j] = array[j-step]
			j -= step
		array[j] = cur_item

	return array


def sort_shell(array, cmp=less):
	n = len(array)
	d = n // 2
	while d >= 1:
		array = sort_insertion(array, cmp=cmp, step=d)
		d = d // 2
	return array


#t=time.time()
#sort_shell(random_array(100))
#print(time.time()-t)

array = random_array(10000)
t=time.time()
array = sort_shell(array)
print(time.time()-t)

# t=time.time()
# sort_shell(random_array(10000))
# print(time.time()-t)


#print(sort_bubble([]))
#print(sort_bubble([1]))
#print(sort_bubble([1,2,3,4]))
#print(sort_bubble([4,3,2,1]))

# print(sort_insertion([]))
# print(sort_insertion([1]))
# print(sort_insertion([1,1,1,1]))
# print(sort_insertion([1,2,3]))
# print(sort_insertion([1,2,3,4]))
# print(sort_insertion([4,3,2,1]))


# print(sort_shell([]))
# print(sort_shell([1]))
# print(sort_shell([1,1,1,1]))
# print(sort_shell([1,2,3]))
# print(sort_shell([1,2,3,4]))
# print(sort_shell([4,3,2,1]))