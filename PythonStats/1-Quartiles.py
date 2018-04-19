#!/bin/python3
#-------------------------------------------------------------------------------
# Objective 
# In this challenge, we practice calculating quartiles. 
#
# Task 
# Given an array, X, of n integers, calculate the respective first quartile (Q_1),
# second quartile (Q_2), and third quartile (Q_3). It is guaranteed that Q_1, Q_2,
# and Q_3 are integers.
#
# Input Format
#
# The first line contains an integer, n, denoting the number of elements in the array. 
# The second line contains n space-separated integers describing the array's elements.
#
# Constraints
#
#   * 5 <= n <=50
#   * 0 < x_i <= 100, where x_i is the ith element of the array.
#
# Output Format
#
# Print  lines of output in the following order:
#
#   1. The first line should be the value of Q_1.
#   2. The second line should be the value of Q_2.
#   3. The third line should be the value of Q_3.
#-------------------------------------------------------------------------------
import sys
import math

n = int(input())

X = list(map(float, input().split()))

x = sorted(X)
ind = math.floor(n/2)
#print(x)
if(n % 2 == 0):
    q2 = round((x[ind-1] + x[(ind)])/2)
    x1 = x[:ind]
    x2 = x[ind:]
else:
    q2 = round(x[ind])
    x1 = x[:ind]
    x2 = x[ind+1:]
       
#print(x1)
#print(x2)

lx = len(x1)
ind = math.floor(lx/2)
#print(ind)
if lx % 2 == 0 :
    q1 = round((x1[ind-1] + x1[(ind)])/2)
    q3 = round((x2[ind-1] + x2[(ind)])/2)
else:
    q1 = round(x1[ind])
    q3 = round(x2[ind])
print(q1)
print(q2)
print(q3)