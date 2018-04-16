#!/bin/python3
""" 
Objective 
Today, we're working with binary numbers. 

Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and print
the base-10 integer denoting the maximum number of consecutive 1's in n's 
binary representation.

Input Format

A single integer, n.

Constraints

    * 1 <= n <= 10^6

Output Format

Print a single base-10 integer denoting the maximum number of consecutive 1's 
in the binary representation of n.
 """
 
import sys

def binary(n):
    #print(n)
    if n==0:
        return('')
    else: 
        return(binary(int(n/2)) + str(n%2))
    
        
n = int(input().strip())

ans = binary(n)
#print(ans)
count = 1
mx = count

for i in range(1,len(ans)):
    if(int(ans[i]) == 1):
        #print(count)
        if(ans[i-1]==ans[i]):
            count+=1
        if(count > mx): 
            mx = count
    else: count = 1

#print(ans)
print(mx)
