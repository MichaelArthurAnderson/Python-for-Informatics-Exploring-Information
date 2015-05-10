#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 8.5 Write a program to read through the mail box data and when you find line that starts with "From", you will split the line into words using the split
# function. We are interested in who sent the message which is the second word on the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line and then you will also count the number of From (not From:) lines and print out a count at the end.
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
	
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        print words[1].strip()
        count = count + 1
    
print "There were", count, "lines in the file with From as the first word"

sys.exit(0)