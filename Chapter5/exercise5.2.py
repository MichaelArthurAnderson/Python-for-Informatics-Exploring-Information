#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 5.2 Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.

input = 0
number_list = []

while True:
    
    try:
        input = raw_input('Enter a number:\n')
        
        if input == "done":
            break
        
        input = float(input)
        
    except ValueError:
        print("Invalid input")
        continue

    number_list.append(input)

print str(min(number_list)), str(max(number_list))

sys.exit(0)
