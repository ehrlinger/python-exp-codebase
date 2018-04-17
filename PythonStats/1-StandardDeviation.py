#!/bin/python3
#-------------------------------------------------------------------------------
# Objective 
# In this challenge, we practice calculating standard deviation. 
#
# Task 
# Given an array, X, of N integers, calculate and print the standard deviation.
# Your answer should be in decimal form, rounded to a scale of 1 decimal place 
# (i.e., 12.3 format). An error margin of +/- 0.1 will be tolerated for the 
# standard deviation.
#
# Input Format
#
# The first line contains an integer, N, denoting the number of elements in 
# the array. 
# The second line contains N space-separated integers describing the respective 
# elements of the array.
#
# Constraints
#   * 5 <= N <= 100
#   * 0 < x_i <= 10^5, where x_i is the ith element of array X.
#
# Output Format
#
# Print the standard deviation on a new line, rounded to a scale of 1 decimal 
# place (i.e., 12.3 format).
#
#-------------------------------------------------------------------------------
import sys
import math
n = int(input())

X = list(map(int, input().split()))

mn = sum(X)/n

dst = list(map(lambda x: (x - mn)**2, X))

std = math.sqrt(sum(dst)/n)

print(round(std,1))