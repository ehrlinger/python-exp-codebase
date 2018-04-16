#!/bin/python3
#------------------------------------------------------------------------------
# Objective 
# In this challenge, we're going to use loops to help us do some simple math. 
#
# Task 
# Given an integer, n, print its first 10 multiples. Each multiple n*i  
# (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.
#
#Input Format
#
# A single integer, n.
#
# Constraints
#
#  * 2 <= n <=20
# 
# Output Format
#
# Print  lines of output; each line  (where ) contains the  of  in the form: 
#     n x i = result.
#------------------------------------------------------------------------------
import sys

n = int(input().strip())
for ind in range(1,11):
    s = repr(n) + ' x ' + repr(ind) + ' = ' + repr(ind*n)
    print(s)
    