#!/usr/bin/python

# Step through a list, and return the maximum element
def max(list):
	max = list[0]
	for num in list:
		if num>max:
			max=num
	return max
	
# step through a list and return 1 if all numbers are unique
def numbers_ok(list = []):
	#print list
	result = 1
	count = {}
	for num in list:
		if num not in count:
			count[num] = 1
		else:
			count[num] += 1
		#print num, count[num]
		if count[num]>1:
			result = 0
	return result
	
# Script to solve the math problem with a brute force method.

for a in range(1,9):
	for b in range(1,9):
		for c in range(1,9):
			for d in range(1,9):
				#if numbers_ok([a, b, c, d]):
				ef = (10*a+b) - (10*c+d)
				# make a character of the answer: three places integer with sign
				ef_char = '{:+03d}'.format(ef)
				#print a, b, c, d, ef, ef_char
				e = int(ef_char[1])
				f = int(ef_char[2])
				for g in range(1,9):
					for h in range(1,9):
						ppp = ef + (10 * g + h)
						ppp_char = '{:+04d}'.format(ppp)
						if numbers_ok([a, b, c, d, e, f, g, h]):
							#print a, b, c, d, e, f, g, h, ppp, ppp_char
							if (ppp_char[1] == ppp_char[2] == ppp_char[3]):
								print '***', a, b, c, d, e, f, g, h, ppp