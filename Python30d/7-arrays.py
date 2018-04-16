#!/bin/python3
# #------------------------------------------------------------------------------
# Objective 
# Today, we're learning about the Array data structure. 
#
# Task 
# Given an array, A, of N integers, print A's elements in reverse order as a 
# single line of space-separated numbers.
#
# Input Format
#
# The first line contains an integer,  N (the size of our array). 
# The second line contains N space-separated integers describing array A's elements.
#
# Constraints
#    * 1 <= N <= 1000
#    * 1 <= A_i <=  10000, where A_i is the ith integer in the array.
# Output Format
#
# Print the elements of array A in reverse order as a single line of space-separated numbers.
#------------------------------------------------------------------------------

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(*reversed(arr), sep=' ')
