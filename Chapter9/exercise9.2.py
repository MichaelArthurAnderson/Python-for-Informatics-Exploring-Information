#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 9.3 Write a program to read through a mail log, and build a histogram using a dictionary to count how many messages have come from each email address and print the dictionary.
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
    
    if not (len(words) >= 2 and words[0] == 'From') : continue
    
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1

print counts    

sys.exit(0)