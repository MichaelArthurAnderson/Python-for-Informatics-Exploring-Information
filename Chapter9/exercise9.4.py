#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 9.4 Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section 5.7.2) to find who has the most messages and print how many messages the person has.
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

max_count = 0
max_address = ''

for key in counts:
    if counts[key] >= max_count:
        max_count = counts[key]
        max_address = key

print max_address + ' ' + str(max_count)   

sys.exit(0)