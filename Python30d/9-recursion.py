 #!/bin/python3
""" 
Objective 
Today, we're learning and practicing an algorithmic concept called Recursion.

Recursive Method for Calculating Factorial 

    factorial(N) = \left{ 1                  N <1
                          N X factorail(N-1) otherwise      
Task 
Write a factorial function that takes a positive integer, N as a parameter and 
prints the result of  N! (N factorial).

Note: If you fail to use recursion or fail to name your recursive function 
factorial or Factorial, you will get a score of .

Input Format

A single integer, N (the argument to pass to factorial).

Constraints

  2 <= N <= 12

Your submission must contain a recursive function named factorial.

Output Format

Print a single integer denoting N!. 
"""

import sys

def factorial(n):
    # Complete this function
    if n <= 1: 
        return(1)
    else:
        res = n * factorial(n-1)
        return(res)
    
    
if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)


