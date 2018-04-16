# Day 8: Dictionaries and Maps
# Given n names and phone numbers, assemble a phone book that maps 
# friends' names to their respective phone numbers. You will then 
# be given an unknown number of names to query your phone book for. 
# For each  queried, print the associated entry from your phone book 
# on a new line in the form name=phoneNumber; if an entry for n
#  is not found, print 'Not found' instead.
#
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.
#
# Input Format
#
# The first line contains an integer, , denoting the number of entries 
# in the phone book. 
# Each of the n subsequent lines describes an entry in the form of 2 
# space-separated values on a single line. The first value is a friend's 
# name, and the second value is an 8-digit phone number.
#
# After the n lines of phone book entries, there are an unknown number of 
# lines of queries. Each line (query) contains a name to look up, and you 
# must continue reading lines until there is no more input.
#
# Note: Names consist of lowercase English alphabetic letters and are 
# first names only.
# -----------------------------------------------------------------------
#
#  Read in the number of lines containing the dictionary entries 
ind = int(input())

# read the n lines into a list, each element contains a
# name/number pair
name_numbers = [input().split() for _ in range(ind)]
# Break the list into a dictionary of name/number pairs.
phone_book = {k: v for k,v in name_numbers}

# Infinite loop to read the remaining names to look up.
while True:
    try:
        # Read the name
        name = input()

        # lookup
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break