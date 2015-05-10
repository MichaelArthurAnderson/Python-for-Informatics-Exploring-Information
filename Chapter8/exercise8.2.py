#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 8.2 Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to
# fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

fname = raw_input("Enter file name: ")

try:
    
    fh = open(fname)
    
except IOError:
    
    print "IOError: No such file or directory: " + fname
    sys.exit(1)

count = 0

for line in fh:
    words = line.split()
    if len(words) < 3 : continue
    if words[0] != 'From' : continue
    print words[2]

sys.exit(0)