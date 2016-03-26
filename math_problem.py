#!/usr/bin/python

# Step through a list, and return the maximum element
def max(list):
	max = list[0]
	for num in list:
		if num>max:
			max=num
	return max
	
# step through a list and return 1 if all numbers are unique
def numbers_ok(list):
	result = 1
	for num in list:
		count[num]++
		if count[num]>1:
			result = 0
	return result
	
# Script to solve the math problem with a brute force method.

for a in range(1,9):
	for b in range(1,9):
		for c in range(1,9):
			for d in range(1,9):
				cd = (10*a+b) - (10*c+d)

