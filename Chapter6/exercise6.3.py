#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
#  Exercise 6.3 Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.

def count(string, letter):
    
    count = 0
    
    for current_letter in string:
            if current_letter == letter:
                count += 1

    return count

string = str(raw_input('Enter a string:\n'))

letter = str(raw_input('Enter a letter:\n'))

print letter + " appears in " + string + " " + str(count(string,letter)) + " times."

sys.exit(0)
