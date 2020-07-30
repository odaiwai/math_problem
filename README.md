# Math Problem

I saw [this math problem](1) on my news feed and decided to solve it by a brute force method.  This method avoids the analysis, but I'll come back to it, because this problem can be solved analytically as well.

(1): http://www.ejinsight.com/20160321-this-math-poser-is-frustrating-students-and-driving-parents-mad/

## What is the Problem?

Solve the following equation, such that all eight numbers (A, B, C, D, E, F, G, H) are unique, and the final result PPP is a three digit number with all digits the same.

      AB
    - CD
    =====
      EF
    + GH
    =====
     PPP

## How to solve it?
When solving a problem like this, there are two ways to approach it: You can try to solve it analytically, or use a 'Brute Force' method.

The Analytical Method relies on figuring out the underlying mathematics of the problem. This is best suited to where a problem has a 'solution space' that is so large it's difficult to figure out all of the possible solutions on paper.

The Brute Force method, on the other hand relies on testing all possible solutions to the problem and printing out all the answers that we find that match the solution criterion. Obviously, this is not a method that we would choose if we were solving the problem on paper, but if we have a computing device, and a basic knowledge of programming, we can rely on the computer's ability to do many calculations to solve the problem for it.

The brute force method is actually pretty simple:
- Step over every possible value for the six numbers (A, B, C, D, G, H), (E and F are derived), and calculate the final solution PPP;
- If the final solution PPP matches the conditions (all the same digit), print out the solution.

The 'solution space', i.e. all the possible tests we have to run, is fairly small as brute force problems go. The total possible options we need to consider are 9^6 or 531,441 possible states for six numbers. It's actually less than that, as we only consider the unique values from the six numbers, which is ( 9 C 6 ) in probability terms (9!/6!) or 504 possible combinations. Even considering all 531,000, this is a fairly trivial problem to solve with a brute force method for modern computers.

A more detailed algorithm is shown below. This is actually a [Python][http://www.python.org] script, but Python is well known for being 'pseudo-code' masquerading as a language...

I've added some comments, and (as is normal with Python) the indentation is important.

````python
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
````

Not shown in that script are the subroutines max() and numbers_ok(), which determine the maximum number in a list and query if all numbers in a list are unique respectively.  They're in the Python Script: [math_problem.py][1], but contain a few language concepts which are probably a little complex for Python Neophytes, and not really relevant to solving the mathematics problem here.

## Solutions - Brute Force

Here are all the possible solutions:
<table>
<tr><th> a</th><th> b</th><th> c</th><th> d</th><th> e</th><th> f</th><th> g</th><th> h</th><th> ppp</th></tr>
<tr><td> 3</td><td> 9</td><td> 1</td><td> 4</td><td> 2</td><td> 5</td><td> 8</td><td> 6</td><td> 111</td></tr>
<tr><td> 3</td><td> 9</td><td> 1</td><td> 5</td><td> 2</td><td> 4</td><td> 8</td><td> 7</td><td> 111</td></tr>
<tr><td> 4</td><td> 3</td><td> 1</td><td> 7</td><td> 2</td><td> 6</td><td> 8</td><td> 5</td><td> 111</td></tr>
<tr><td> 4</td><td> 3</td><td> 2</td><td> 7</td><td> 1</td><td> 6</td><td> 9</td><td> 5</td><td> 111</td></tr>
<tr><td> 4</td><td> 3</td><td> 2</td><td> 8</td><td> 1</td><td> 5</td><td> 9</td><td> 6</td><td> 111</td></tr>
<tr><td> 4</td><td> 5</td><td> 2</td><td> 7</td><td> 1</td><td> 8</td><td> 9</td><td> 3</td><td> 111</td></tr>
<tr><td> 4</td><td> 7</td><td> 3</td><td> 2</td><td> 1</td><td> 5</td><td> 9</td><td> 6</td><td> 111</td></tr>
<tr><td> 4</td><td> 8</td><td> 1</td><td> 2</td><td> 3</td><td> 6</td><td> 7</td><td> 5</td><td> 111</td></tr>
<tr><td> 4</td><td> 8</td><td> 1</td><td> 6</td><td> 3</td><td> 2</td><td> 7</td><td> 9</td><td> 111</td></tr>
<tr><td> 4</td><td> 8</td><td> 3</td><td> 2</td><td> 1</td><td> 6</td><td> 9</td><td> 5</td><td> 111</td></tr>
<tr><td> 5</td><td> 2</td><td> 3</td><td> 8</td><td> 1</td><td> 4</td><td> 9</td><td> 7</td><td> 111</td></tr>
<tr><td> 6</td><td> 5</td><td> 4</td><td> 7</td><td> 1</td><td> 8</td><td> 9</td><td> 3</td><td> 111</td></tr>
<tr><td> 6</td><td> 7</td><td> 5</td><td> 4</td><td> 1</td><td> 3</td><td> 9</td><td> 8</td><td> 111</td></tr>
<tr><td> 7</td><td> 2</td><td> 5</td><td> 4</td><td> 1</td><td> 8</td><td> 9</td><td> 3</td><td> 111</td></tr>
<tr><td> 7</td><td> 4</td><td> 5</td><td> 6</td><td> 1</td><td> 8</td><td> 9</td><td> 3</td><td> 111</td></tr>
<tr><td> 7</td><td> 5</td><td> 1</td><td> 2</td><td> 6</td><td> 3</td><td> 4</td><td> 8</td><td> 111</td></tr>
<tr><td> 7</td><td> 5</td><td> 1</td><td> 3</td><td> 6</td><td> 2</td><td> 4</td><td> 9</td><td> 111</td></tr>
<tr><td> 7</td><td> 5</td><td> 6</td><td> 2</td><td> 1</td><td> 3</td><td> 9</td><td> 8</td><td> 111</td></tr>
<tr><td> 8</td><td> 2</td><td> 6</td><td> 5</td><td> 1</td><td> 7</td><td> 9</td><td> 4</td><td> 111</td></tr>
<tr><td> 8</td><td> 5</td><td> 4</td><td> 6</td><td> 3</td><td> 9</td><td> 7</td><td> 2</td><td> 111</td></tr>
<tr><td> 8</td><td> 6</td><td> 1</td><td> 4</td><td> 7</td><td> 2</td><td> 3</td><td> 9</td><td> 111</td></tr>
<tr><td> 8</td><td> 6</td><td> 5</td><td> 4</td><td> 3</td><td> 2</td><td> 7</td><td> 9</td><td> 111</td></tr>
<tr><td> 8</td><td> 9</td><td> 1</td><td> 4</td><td> 7</td><td> 5</td><td> 3</td><td> 6</td><td> 111</td></tr>
<tr><td> 9</td><td> 4</td><td> 1</td><td> 8</td><td> 7</td><td> 6</td><td> 3</td><td> 5</td><td> 111</td></tr>
<tr><td> 9</td><td> 5</td><td> 2</td><td> 7</td><td> 6</td><td> 8</td><td> 4</td><td> 3</td><td> 111</td></tr>
</table>

## Solutions - Analytical

After solving it with the brute force method, it's pretty clear that P has to equal 1. In fact, if you think about it, you need to have each column (i.e. B - D + H) equal to 1 or 11 for the first column, and 11 for the second column for the whole thing to work.

The solution is somewhere within (0-99) - (0-99) + (0-99), and so can't be much greater than 100. Just to think of a maximum number, 98-12+75 = 161, so we clearly can't get to 200+, and therefore, the only possible solution is 111. (If we allow 0 as a possible number, there are a lot more possible solutions.)

This is a clear example of how the Brute Force method can assist with analysing the problem to see if there's an Analytical Method to be discovered.
