#!/usr/bin/env python
import sys
import re

# Python for Informatics Exploring Information
# Exercise 11.2 Write a program to look for lines of the form New Revision: 39772 and extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

fname = raw_input("Enter file name: ")

try:
    
    fh = open(fname)
    
except IOError:
    
    print "IOError: No such file or directory: " + fname
    sys.exit(1)

regex = 'New Revision: ([0-9]+)'

lst = []

for line in fh:
    
    match = re.findall(regex, line)
    
    if len(match) > 0:
        try:
            lst.append(float(match[0]))
        except ValueError:
            continue
        
print str(sum(lst) / len(lst))

sys.exit(0)

