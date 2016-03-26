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

What is a Brute Force method?  Simple: we test all possible solutions to the problem and print out all the answers that we find. 

The 'solution space', i.e. all the possible tests we have to run, is fairly small as these things go. The total possible options we need to consider are 9^6 or 531,441 possible states for six numbers. It's actually less than that, as we only consider the unique values from the six numbers, which is ( 9 C 6 ) in probability terms (9!/6!) or 504 possible combinations. Even considering all 531,000, this is a fairly trivial problem to solve with a brute force method for modern computers.

A [Perl][http://www.perl.org] script to solve this problem can be found here: [Solve Math Problem][] 

A more detailed algorithm is shown below. This is actually a [Python][http://www.python.org] script, but they tend to be a lot more readable than Perl...

# Solutions - Brute Force

# Solutions - Analytical

After solving it with the brute force method, it's pretty clear that P has to equal 1. In fact, if you think about it, you need to have each column (i.e. B - D + H) equal to 11 for the thing to work.


# Opinion

This problem is directed at primary school children in Hong Kong, and that is symptomatic of the disturbing trends in Hong Kong Education.  It is completely unreasonable to expect a primary school child to possess the 
