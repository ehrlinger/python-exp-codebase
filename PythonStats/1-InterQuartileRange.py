#!/bin/python3
#-------------------------------------------------------------------------------
# Objective 
# In this challenge, we practice calculating the interquartile range. We 
# recommend you complete the Quartiles challenge before attempting this problem.
#
# Task 
# The interquartile range of an array is the difference between its first (Q_1) 
# and third (Q_3) quartiles (i.e., Q_3 - Q1).
#
# Given an array, X, of n integers and an array, F, representing the respective
# frequencies of X's elements, construct a data set, S, where each x_i occurs at
# frequency f_i. Then calculate and print S's interquartile range, rounded to a
# scale of 1 decimal place (i.e., 12.3 format).
#
# Tip: Be careful to not use integer division when averaging the middle two 
# elements for a data set with an even number of elements, and be sure to not 
# include the median in your upper and lower data sets.
#
# Input Format
#
# The first line contains an integer, n, denoting the number of elements in 
# arrays X and F. 
# The second line contains n space-separated integers describing the respective 
# elements of array X. 
# The third line contains n space-separated integers describing the respective 
# elements of array F.
#
# Constraints
#   * 5 <= n <= 50
#   * 0 < x_i <= 100, where x_i is the ith element of array X.
#   * 0 < \sum_{i=0}^{n-1} f_i <= 10^3, where f_i is the ith element of array F.
#   * The number of elements in S is equal to \sum F.
#
# Output Format
#
# Print the interquartile range for the expanded data set on a new line. Round 
# your answer to a scale of 1 decimal place (i.e., 12.3 format).
#-------------------------------------------------------------------------------
import sys
import math

# Stolen from interwebs at
# http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
def iter_flatten(iterable):
  it = iter(iterable)
  for e in it:
    if isinstance(e, (list, tuple)):
      for f in iter_flatten(e):
        yield f
    else:
      yield e


n = int(input())

X = list(map(float, input().split()))
F = list(map(int, input().split()))

S = []

# Get the correct number of items (f) of each x
for ind in range(n):
    S.append([X[ind]] * F[ind])

# S comes back as a 2d array, so we flatten it    
S = [i for i in iter_flatten(S)]

#---------------------------------------------------------
# Grab the quartile code from previous example. 
x = sorted(S)
n = len(x)
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
    q1 = (x1[ind-1] + x1[(ind)])/2
    q3 = (x2[ind-1] + x2[(ind)])/2
else:
    q1 = x1[ind]
    q3 = x2[ind]
#print(q1)
#print(q2)
#print(q3)

print(q3 - q1)