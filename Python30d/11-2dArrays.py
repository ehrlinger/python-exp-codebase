#!/bin/python3
""" 
Objective 
Today, we're building on our knowledge of Arrays by adding another dimension.

Context 
Given a 6x6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this 
pattern in A's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task 
Calculate the hourglass sum for every hourglass in A, then print the maximum 
hourglass sum.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers 
describing 2D Array A; every value in  will be in the inclusive range of -9 to 9.

Constraints
    * -9 <= A[i][j] < 9
    * 0<= i,j <=5

Output Format

Print the largest (maximum) hourglass sum found in A. 
"""
import sys

# Read the array.
arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


mx = -200
for i in range(4):
    for j in range(4):
        #print(i,j)
        #print(arr[i][j:(j + 3)])
        sm = sum(arr[i][j:(j + 3)]) + arr[(i+1)][(j+1)] + sum(arr[i+2][j:(j+3)])
        #print(sm)
        if(sm > mx): mx = sm
        
print(mx)
        