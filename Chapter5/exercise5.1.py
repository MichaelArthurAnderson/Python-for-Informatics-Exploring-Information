#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 5.1 Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of
# the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
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

print str(sum(number_list)), str(len(number_list)), str(sum(number_list)/len(number_list))

sys.exit(0)
