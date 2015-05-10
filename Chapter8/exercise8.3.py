#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 8.3 Rewrite the guardian code in the above example without two if statements. Instead use a compound logical expression using the and
# logical operator with a single if statement.
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
    if not (len(words) >= 3 and words[0] == 'From') : continue
    print words[2]

sys.exit(0)