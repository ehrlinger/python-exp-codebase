#!/bin/python3
#------------------------------------------------------------------------------
# Objective 
# In this challenge, you'll work with arithmetic operators. 
#
# Task 
# Given the meal price (base cost of a meal), tip percent (the percentage of the
# meal price being added as tip), and tax percent (the percentage of the meal 
# price being added as tax) for a meal, find and print the meal's total cost.
#
# Note: Be sure to use precise values for your calculations, or you may end
#  up with an incorrectly rounded result!
#
# Input Format
#
# There are  lines of numeric input: 
# The first line has a double,  (the cost of the meal before tax and tip). 
# The second line has an integer,  (the percentage of  being added as tip). 
# The third line has an integer,  (the percentage of  being added as tax).
#
# Output Format
#
# Print The total meal cost is totalCost dollars., where  is the rounded 
# integer result of the entire bill ( with added tax and tip).
#------------------------------------------------------------------------------

import sys

# Function to calculate the result
def totalCost(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent/100. 
    tax = meal_cost * tax_percent/100. 
    return(meal_cost + tip + tax)

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    tot = round(totalCost(meal_cost, tip_percent, tax_percent))
    
    print("The total meal cost is %d dollars." % tot)