#!/bin/python3
#-------------------------------------------------------------------------------
# Objective 
# In the previous challenge, we calculated a mean. In this challenge, we practice
#  calculating a weighted mean. 
#
# Task 
# Given an array, X, of N integers and an array, W, representing the respective 
# weights of X's elements, calculate and print the weighted mean of X's elements. 
# Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
#
# Input Format
#
# The first line contains an integer, N, denoting the number of elements 
# in arrays X and W. 
# The second line contains N space-separated integers describing the 
# respective elements of array X. 
# The third line contains N space-separated integers describing the
#  respective elements of array W.
#
# Constraints
#
# 5 <= N <= 50
# 0 < x_i <= 100, where x_i is the ith element of array X.
# 0 < w_i <= 100, where w_i is the ith  element of array W.
#
#  Output Format
#
# Print the weighted mean on a new line. Your answer should be rounded to a scale 
# of 1 decimal place (i.e., 12.3 format).
#
#-------------------------------------------------------------------------------

import sys
n = int(input())

X = list(map(float, input().split()))
W = list(map(float, input().split()))
mw = 0

for ind in range(n):
    mw = mw + X[ind] * W[ind]
    
mw = round(mw/sum(W), 1)

print(mw)