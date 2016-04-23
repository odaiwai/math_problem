# Math Problem

I saw [this math problem][1] on my news feed and decided to solve it by a brute force method.  This method avoids the analysis, but I'll come back to that, because this problem can be solved analytically as well.  

[1]: http://www.ejinsight.com/20160321-this-math-poser-is-frustrating-students-and-driving-parents-mad/

# Problem

Solve the following equation, such that all eight numbers (A, B, C, D, E, F, G, H) are unique, and the final result PPP is a three digit number with all digits the same.

      AB
    - CD
    =====
      EF
    + GH
    =====
     PPP

# Algorithm
The brute force method is actually pretty simple:
- Step over every possible value for the six numbers (A, B, C, D, G, H), (E and F are derived), and check every possible solution for the desired outcome.

What is a Brute Force method?  Simple: we test all possible solutions to the problem and print out all the answers that we find that match the solution criterion.

The 'solution space', i.e. all the possible tests we have to run, is fairly small as these things go. The total possible options we need to consider are 9^6 or 531,441 possible states for six numbers. It's actually less than that, as we only consider the unique values from the six numbers, which is ( 9 C 6 ) in probability terms (9!/6!) or 504 possible combinations. Even considering all 531,000, this is a fairly trivial problem to solve with a brute force method for modern computers.

A [Perl][http://www.perl.org] script to solve this problem can be found here: [Solve Math Problem][] 

A more detailed algorithm is shown below. This is actually a [Python][http://www.python.org] script, but they tend to be a lot more readable than Perl...

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

Not shown in that script are the subroutines max() and numbers_ok(), which determine the maximum number in a list and query if all numbers in a list are unique respectively.  They're in the Python Script: [math_problem.py][1], but contain a few language concepts which are probably a little complex for Python Neophytes, and not really relevant to solving the mathematics problem here.

# Solutions - Brute Force
Here are all the possible solutions:
| a| b| c| d| e| f| g| h| ppp	
| 3| 9| 1| 4| 2| 5| 8| 6| 111
| 3| 9| 1| 5| 2| 4| 8| 7| 111
| 4| 3| 1| 7| 2| 6| 8| 5| 111
| 4| 3| 2| 7| 1| 6| 9| 5| 111
| 4| 3| 2| 8| 1| 5| 9| 6| 111
| 4| 5| 2| 7| 1| 8| 9| 3| 111
| 4| 7| 3| 2| 1| 5| 9| 6| 111
| 4| 8| 1| 2| 3| 6| 7| 5| 111
| 4| 8| 1| 6| 3| 2| 7| 9| 111
| 4| 8| 3| 2| 1| 6| 9| 5| 111
| 5| 2| 3| 8| 1| 4| 9| 7| 111
| 6| 5| 4| 7| 1| 8| 9| 3| 111
| 6| 7| 5| 4| 1| 3| 9| 8| 111
| 7| 2| 5| 4| 1| 8| 9| 3| 111
| 7| 4| 5| 6| 1| 8| 9| 3| 111
| 7| 5| 1| 2| 6| 3| 4| 8| 111
| 7| 5| 1| 3| 6| 2| 4| 9| 111
| 7| 5| 6| 2| 1| 3| 9| 8| 111
| 8| 2| 6| 5| 1| 7| 9| 4| 111
| 8| 5| 4| 6| 3| 9| 7| 2| 111
| 8| 6| 1| 4| 7| 2| 3| 9| 111
| 8| 6| 5| 4| 3| 2| 7| 9| 111
| 8| 9| 1| 4| 7| 5| 3| 6| 111
| 9| 4| 1| 8| 7| 6| 3| 5| 111
| 9| 5| 2| 7| 6| 8| 4| 3| 111

# Solutions - Analytical

After solving it with the brute force method, it's pretty clear that P has to equal 1. In fact, if you think about it, you need to have each column (i.e. B - D + H) equal to 1 or 11 for the first column, and 11 for the second column for the whole thing to work.

The solution is somewhere within (0-99) - (0-99) + (0-99), and so can't be much greater than 100. Just to think of a maximum number, 98-12+75 = 161, so we clearly can't get to 200+, and therefore, the only possible solution is 111. (If we allow 0 as a possible number, there are a lot more possible solutions.)

# Opinion

This problem is directed at primary school children in Hong Kong, and that is symptomatic of the disturbing trends in Hong Kong Education.  It is completely unreasonable to expect a primary school child to possess the analytical skills to solve this problem, and it is, quite frankly, beyond the skills of most educated Hong Kong adults too.  The programming mindset is quite rare, and problem solving is not a skill that is developed or rewarded.
