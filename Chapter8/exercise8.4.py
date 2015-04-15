#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 8.4 Download a copy of the file from www.py4inf.com/code/romeo.txt
# Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

fname = raw_input("Enter file name: ")

try:
    
    fh = open(fname)
    
except IOError:
    
    print "IOError: No such file or directory: " + fname
    sys.exit(1)

lst = list()

for line in fh:
	
    words = line.split()
    
    for word in words:
       if word not in lst:
            lst.append(word)
lst.sort()

print lst

sys.exit(0)
