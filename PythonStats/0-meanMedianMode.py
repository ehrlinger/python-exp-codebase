#!/bin/python3
#-------------------------------------------------------------------------------
# Objective 
# In this challenge, we practice calculating the mean, median, and mode. Check 
# out the Tutorial tab for learning materials and an instructional video!
#
# Task 
# Given an array, X, of N integers, calculate and print the respective mean, 
# median, and mode on separate lines. If your array contains more than one modal 
# value, choose the numerically smallest one.
#
# Note: Other than the modal value (which will always be an integer), your answers 
# should be in decimal form, rounded to a scale of 1 decimal place 
# (i.e., 12.3, 7.0 format).
#
# Input Format
#
# The first line contains an integer, N, denoting the number of elements in the 
# array. 
# The second line contains N space-separated integers describing the array's
#  elements.
#
# Constraints
#   * 10 <= N <= 2500
#   * 0 < x_i <= 10^5 , where x_i is the ith element of the array.
#
# Output Format
#
# Print  lines of output in the following order:
#
#   1. Print the mean on a new line, to a scale of  decimal place 
#       (i.e., 12.3, 7.0).
#   2. Print the median on a new line, to a scale of  decimal place 
#       (i.e., 12.3, 7.0).
#   3. Print the mode on a new line; if more than one such value exists, print the 
#       numerically smallest one.
#-------------------------------------------------------------------------------
import sys

n = int(input())
nums = list(map(int, input().strip().split()))

# Mean
print(sum(nums)/float(n))

# Median
nums.sort()
if(n % 2 == 0):
    print((nums[int(n/2)] + nums[int(n/2 - 1)])/2)
else:
    print(nums.sort[(n-1)/2]) 
    
# mode
from scipy import stats
print(int(stats.mode(nums)[0]))
