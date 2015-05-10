#!/usr/bin/env python
import sys
import time

# Python for Informatics Exploring Information
# Exercise 10.2 This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the 'From' line by finding the
# time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
#
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
    
    if not (len(words) >= 6 and words[0] == 'From') : continue
    
    hour = words[5].split(":")[0]
    
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] += 1

lst = []

for key in counts:
    lst.append((key, counts[key]))

lst.sort()

for pair in lst:
    print str(pair[0]) + ' ' + str(pair[1])

sys.exit(0)

