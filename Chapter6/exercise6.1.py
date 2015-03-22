#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
#  Exercise 6.1 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

string = str(raw_input('Enter a string to print backwards:\n'))

index = -1

while abs(index) <= len(string):
    print string[index]
    index -= 1

sys.exit(0)
