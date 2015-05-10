#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 9.1 Write a program that reads the words in words.txt and stores them #as keys in a dictionary. It doesn matter what the values are. Then you can use
# the in operator as a fast way to check whether a string is in the dictionary.
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
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print counts    

sys.exit(0)