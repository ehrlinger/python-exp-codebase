#!/bin/python3
#------------------------------------------------------------------------------
# Objective 
# Today we're expanding our knowledge of Strings and combining it with what 
# we've already learned about loops. 
#
# Task 
# Given a string, S, of length N that is indexed from 0 to N-1, print its 
# even-indexed and odd-indexed characters as 2 space-separated strings on a 
# single line (see the Sample below for more detail).
#
# Note: 0 is considered to be an even index.
#
# Input Format
#
# The first line contains an integer, T (the number of test cases). 
# Each line i of the T subsequent lines contain a String, S.
#
# Constraints
#    * 1 <= T <= 10
#    * 2 <= length of S <= 10000
#
# Output Format
#
# For each String  S_j (where 0 <= j <= T-1), print S_j's even-indexed 
# characters, followed by a space, followed by S_j's odd-indexed characters.
#------------------------------------------------------------------------------
import sys

n = int(input())

for ind in range(n):
    wrd = str(input())
    l = len(wrd)
    evn = wrd[0:l:2]
    odd = wrd[1:l:2]
    print(evn + ' ' + odd)
