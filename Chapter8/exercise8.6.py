#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 8.6 Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user
# enters 'done'. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

number_lst = []

while ( True ) :
    
    inp = raw_input('Enter a number or "done" when finished: ')

    if inp == 'done' : break
    
    try:
        value = float(inp)
    except ValueError:
        print "Enter a number or 'done' when finished."
    
    number_lst.append(value)

print "The max is " + str(max(number_lst)) + " and the min is "  + str(min(number_lst)) +  "."

sys.exit(0)