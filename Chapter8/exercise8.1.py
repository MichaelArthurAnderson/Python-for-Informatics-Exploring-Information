#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 8.1 Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

def chop(lst):
    
	lst.pop(0)
        
	lst.pop(len(lst) - 1)
	
	return

lst = ['a','b','c','d']

print lst

print chop(lst)

print lst

sys.exit(0)
