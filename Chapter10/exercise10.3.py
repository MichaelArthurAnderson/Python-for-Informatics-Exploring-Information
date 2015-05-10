#!/usr/bin/env python
import sys
import time

# Python for Informatics Exploring Information
# Exercise 10.3 Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctuation or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.#
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

for code in range(ord('a'), ord('z') + 1):
     counts[chr(code)] = 0
     
for line in fh:
    
    line = line.lower()
    
    for c in line:
        
        if c.isalpha():
            counts[c] += 1

lst = []

for key in counts:
    lst.append((key, counts[key]))

lst.sort()

print lst

sys.exit(0)

