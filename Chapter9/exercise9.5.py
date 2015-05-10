#!/usr/bin/env python
import sys
import re

# Python for Informatics Exploring Information
# Exercise 9.5 This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e. the
# whole e-mail address). At the end of the program print out the contents of your dictionary.
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
    
    domain = re.search("@[\w.]+", words[1]).group()
    
    domain = domain[1:]
    
    if domain not in counts:
        counts[domain] = 1
    else:
        counts[domain] += 1

print counts

sys.exit(0)