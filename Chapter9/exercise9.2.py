#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 9.2 Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines which start with 'From',
# then look for the third word and then keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

fname = raw_input("Enter file name: ")

try:
    
    fh = open(fname)
    
except IOError:
    
    print "IOError: No such file or directory: " + fname
    sys.exit(1)
       
counts = dict()

for line in fh:
    words = line.split()
    
    if not (len(words) >= 3 and words[0] == 'From') : continue
    
    if words[2] not in counts:
        counts[words[2]] = 1
    else:
        counts[words[2]] += 1

print counts    

sys.exit(0)