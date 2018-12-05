#!/usr/bin/python

# Script to solve a math problem
# dave o'brien 2016/03/24
# problem:
#   A B
# - C D
# -----
#   E F
# + G H
# -----
# P P P
# 
# Where ABCDEFGH, P are all [1-9], and unique
# e.g. AB = 21, if A=2, B=1

# subroutines come first in Python
# Step through a list, and return the maximum element

def max(list = []):
	max = list[0]
	for num in list:
		if num>max:
			max=num # if the current number is > max, it becomes max
	return max
	
# step through a list and return 1 if all numbers are unique, 0 otherwise

def numbers_ok(list = []):
	result = 1
	count = {} # this defines an empty dictionary
	for num in list:
		if num not in count:
			count[num] = 1 # if we haven't seen this number before, make a new dict. entry
		else:
			count[num] += 1 # otherwise increment the number of times we've seen this number
		#print num, count[num]
		if count[num]>1:
			result = 0 # if we've seen any number more than one, return 0
	return result
	
# Script to solve the math problem with a brute force method.

# python's range(start, stop, [step]) function is up to, but not including, stop. 
for a in range(1,10): # all the numbers from one to nine.
	for b in range(1,10):
		for c in range(1,10):
			for d in range(1,10):
				ef = (10*a+b) - (10*c+d)
				# make a character string of the answer: three places integer with sign
				ef_char = '{:+03d}'.format(ef)
				e = int(ef_char[1])
				f = int(ef_char[2])
				for g in range(1,10):
					for h in range(1,10):
						ppp = ef + (10 * g + h)
						ppp_char = '{:+04d}'.format(ppp)
						if numbers_ok([a, b, c, d, e, f, g, h]):
							if (ppp_char[1] == ppp_char[2] == ppp_char[3]):
								print 'solution: ', a, b, c, d, e, f, g, h, ppp