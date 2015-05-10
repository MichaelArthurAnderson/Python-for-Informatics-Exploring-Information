#!/usr/bin/env python
import sys
import re

# Python for Informatics Exploring Information
# Exercise 11.1 Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

fname = raw_input("Enter file name: ")

try:
    
    fh = open(fname)
    
except IOError:
    
    print "IOError: No such file or directory: " + fname
    sys.exit(1)

regex = raw_input("Enter a regular expression: ")

count = 0

for line in fh:
    
    line = line.strip()
    
    if re.search(regex, line):
        count += 1

print fname + " had " + str(count) + " that matched " + regex + " . "

sys.exit(0)

