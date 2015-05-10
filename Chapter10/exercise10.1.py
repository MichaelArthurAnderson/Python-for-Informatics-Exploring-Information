#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 10.1 Revise a previous program as follows: Read and parse the 'From' lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read print the person with the most commits by creating a list of (count, email) tuples from the dictionary and then sorting the list in reverse
# order and print out the person who has the most commits.
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

lst = []

for key in counts:
    lst.append((counts[key],key))

lst.sort(reverse=True)

print max(lst)

sys.exit(0)

