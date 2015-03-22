#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 7.2 Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with 'X-DSPAM-Confidence:" pull apart the line to extract the floating point number on the line. Count these lines and the
# compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

fname = raw_input("Enter file name: ")

try:
    
    fh = open(fname)
    
except IOError:
    
    print "IOError: No such file or directory: " + fname
    sys.exit(1)

sum = 0.0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(":")
    sum = sum + float(line[pos + 1:len(line)].strip())
    count = count + 1
    
print "Average spam confidence:", sum / count

sys.exit(0)
